"""From a verified provider webhook to a licence the buyer can use.

`storefront.fulfil` already does the security and the deduplication: HMAC over
the raw bytes, constant-time comparison, timestamp checks, one delivery per
event id. This module is the delivery itself for a gated product — work out
what was bought, sign a licence for it, record the grant so the thank-you page
can claim it, and take access back when the money goes back.

The awkward part is working out *what* was bought, and it is worth being
explicit about why. We put the offer slugs into the checkout URL as custom
data, so a link that sells the core says so and comes back saying so. An order
bump taken inside the provider's checkout is not in that link — the buyer
added it a moment later — so it has to be recognised from the order's line
items instead, which means mapping the provider's product ids back to offer
slugs. Lemon Squeezy's `order_created` payload exposes only the *first* order
item, so a bump can be invisible in the webhook body.

That is a real limit, not a rounding error: it means the bump must be
configured with its own product id in `product_ids`, and that an order whose
first item is the core may still hide a bump. Where it matters, read the order
back from the provider's API before granting. This module reports what it
resolved and what it had to fall back on, rather than guessing quietly.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Mapping

from storefront.fulfil import Delivery, EventStore, event_name, handle_webhook
from storefront.models import Order

from . import licence as licence_mod
from .models import Grant, Product
from .store import GrantStore

#: Events that mean money arrived. Names are the providers' own.
SALE_EVENTS = ("order_created", "transaction.completed", "sale")

#: Events that mean it went back. Lemon Squeezy's refund event is verified
#: against its documented payload shape; the others are best-effort, and the
#: `paywall revoke` command is the fallback for anything not caught here.
REFUND_EVENTS = ("order_refunded", "subscription_payment_refunded",
                 "adjustment.created", "refund")


@dataclass
class Purchase:
    """What handling one webhook did to a product's access."""

    delivery: Delivery
    grant: Grant | None = None
    revoked: str = ""
    event: str = ""
    notes: list[str] = field(default_factory=list)

    @property
    def http_status(self) -> int:
        return self.delivery.http_status


def handle(
    product: Product,
    provider: str,
    raw_body: bytes,
    headers: Mapping[str, str],
    *,
    webhook_secret: str,
    licence_secret: str,
    events: EventStore,
    grants: GrantStore,
    product_ids: Mapping[str, str] | None = None,
    expires_days: int = 0,
    now: float | None = None,
) -> Purchase:
    """Verify a webhook, then grant or revoke access.

    Anything raised inside the delivery propagates, which leaves the event
    unmarked so the provider retries. That ordering is `storefront.fulfil`'s
    and it is the right one: marking first would lose the sale.
    """
    result = Purchase(delivery=Delivery(None, delivered=False, duplicate=False))

    def deliver(order: Order) -> None:
        name = event_name(provider, order.raw)
        result.event = name
        if name in REFUND_EVENTS or _is_refund(provider, order.raw):
            if grants.revoke(order.order_id, now=now):
                result.revoked = order.order_id
            else:
                result.notes.append(
                    f"refund for order {order.order_id!r}, which was never granted here"
                )
            return
        result.grant = grant_purchase(
            product, order,
            licence_secret=licence_secret, grants=grants,
            product_ids=product_ids, expires_days=expires_days, now=now,
            notes=result.notes,
        )

    result.delivery = handle_webhook(
        provider, raw_body, headers, webhook_secret, events,
        deliver=deliver,
        accepted_events=SALE_EVENTS + REFUND_EVENTS,
        now=now,
    )
    return result


def grant_purchase(
    product: Product,
    order: Order,
    *,
    licence_secret: str,
    grants: GrantStore,
    product_ids: Mapping[str, str] | None = None,
    expires_days: int = 0,
    now: float | None = None,
    notes: list[str] | None = None,
) -> Grant:
    """Sign a licence for `order` and record the grant."""
    notes = notes if notes is not None else []
    codes = codes_for_order(product, order, product_ids=product_ids, notes=notes)
    key = licence_mod.issue(
        licence_secret, order_id=order.order_id, codes=codes,
        expires_days=expires_days, now=now,
    )
    grant = Grant(
        order_id=order.order_id,
        provider=order.provider,
        email=order.email,
        codes=codes,
        key=key,
        nonce=str(custom_data(order).get("nonce") or ""),
        created=now if now is not None else time.time(),
        total=order.total,
        currency=order.currency,
        test_mode=order.test_mode,
    )
    grants.put(grant)
    return grant


def codes_for_order(
    product: Product,
    order: Order,
    *,
    product_ids: Mapping[str, str] | None = None,
    notes: list[str] | None = None,
) -> str:
    """Entitlement codes for what this order actually contains.

    Three sources, in order of how much they can be trusted:

    1. The offer slugs we put in the checkout link ourselves.
    2. The provider's product id on the order's line items, mapped back
       through `product_ids`.
    3. The core offer, as the fallback — with a note saying so.

    The fallback is deliberate. An order that arrived through a checkout we
    built is a real payment whatever we can parse out of it, and refusing to
    grant anything would turn our parsing problem into the buyer's problem.
    Granting *more* than was paid for would be the worse error, so the
    fallback is the cheapest rung, never the richest.
    """
    notes = notes if notes is not None else []
    known = {e.offer for e in product.entitlements}

    slugs = [s for s in order.offer_slugs if s in known]
    unknown = [s for s in order.offer_slugs if s not in known]
    if unknown:
        notes.append(f"order names offers this product does not sell: {', '.join(unknown)}")

    from_items = _slugs_from_items(order, product_ids or {})
    for slug in from_items:
        if slug in known and slug not in slugs:
            slugs.append(slug)

    if not slugs:
        core = next((e.offer for e in product.entitlements if not e.requires), None)
        if core is None:
            raise ValueError(
                f"cannot tell what order {order.order_id!r} bought, and "
                f"product {product.slug!r} has no standalone offer to fall back on"
            )
        slugs = [core]
        notes.append(
            f"order {order.order_id!r} carried no recognisable offer — granting "
            f"{core!r} only. Check the checkout link's custom data and the "
            "product_ids map."
        )

    codes = product.codes_for(slugs)
    missing = product.missing_requirements(codes)
    if missing:
        # A rung bought without the thing it builds on: five seats of nothing.
        # Add what it needs rather than handing over a licence that opens no
        # content — the buyer paid for the richer offer, not for a puzzle.
        notes.append(
            f"order {order.order_id!r} holds {', '.join(sorted(set(slugs)))} "
            f"which needs {', '.join(missing)}; granting those too"
        )
        codes = product.codes_for(list(set(slugs) | set(missing)))
    return codes


def custom_data(order: Order) -> dict[str, Any]:
    """The custom data we sent through the checkout, wherever it comes back."""
    raw = order.raw or {}
    if order.provider == "lemonsqueezy":
        return dict(((raw.get("meta") or {}).get("custom_data")) or {})
    if order.provider == "paddle":
        return dict((raw.get("data") or {}).get("custom_data") or {})
    if order.provider == "gumroad":
        return dict(raw.get("url_params") or {})
    return {}


def _slugs_from_items(order: Order, product_ids: Mapping[str, str]) -> list[str]:
    """Offer slugs for the provider product ids on this order's line items."""
    if not product_ids:
        return []
    by_id = {str(pid): slug for slug, pid in product_ids.items()}
    return [by_id[pid] for pid in _item_ids(order) if pid in by_id]


def _item_ids(order: Order) -> list[str]:
    raw = order.raw or {}
    ids: list[str] = []
    if order.provider == "lemonsqueezy":
        # Only the first item is in the order_created payload. Documented in
        # the module docstring because it is a real hole, not a detail.
        item = ((raw.get("data") or {}).get("attributes") or {}).get("first_order_item") or {}
        ids += [str(item.get(k)) for k in ("product_id", "variant_id") if item.get(k)]
    elif order.provider == "paddle":
        for item in (raw.get("data") or {}).get("items") or []:
            price = item.get("price") or {}
            for key in ("product_id", "id"):
                if price.get(key):
                    ids.append(str(price[key]))
    elif order.provider == "gumroad":
        for key in ("product_id", "product_permalink"):
            if raw.get(key):
                ids.append(str(raw[key]))
    return ids


def _is_refund(provider: str, payload: dict[str, Any]) -> bool:
    """Refunds that announce themselves in the body rather than the name."""
    if provider == "lemonsqueezy":
        attributes = ((payload.get("data") or {}).get("attributes")) or {}
        return bool(attributes.get("refunded")) or str(attributes.get("status")) == "refunded"
    if provider == "paddle":
        data = payload.get("data") or {}
        return str(data.get("status", "")).lower() in ("refunded", "chargeback")
    if provider == "gumroad":
        return str(payload.get("refunded")).lower() == "true"
    return False
