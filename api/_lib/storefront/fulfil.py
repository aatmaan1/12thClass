"""Verifying provider webhooks and delivering exactly once.

Two failure modes matter here and they pull in opposite directions.

**Delivering to someone who did not pay.** A webhook endpoint is a public URL
that hands out paid goods when POSTed the right JSON. The only thing between
it and anyone on the internet is the signature check, so it has to be done
properly: HMAC over the *raw bytes* of the request (re-serialising the JSON
changes the bytes and the signature will never match), compared in constant
time, with the provider's timestamp checked so a captured request cannot be
replayed later.

**Delivering twice, or not at all.** Providers retry on any non-2xx, and they
retry aggressively. So delivery must be idempotent on the provider's event
id, and the endpoint must return 200 for an event it has already handled —
returning an error to say "I've seen this" just guarantees it comes back.

Gumroad is the awkward one: its pings carry no signature at all. That is
called out rather than papered over.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol

from .models import Order

#: Reject a signed request older than this. Long enough to survive a slow
#: retry, short enough that a captured request stops working.
MAX_SIGNATURE_AGE_SECONDS = 300


class WebhookError(Exception):
    """A webhook that must not be acted on."""


class SignatureError(WebhookError):
    """The request did not come from the provider, or was tampered with."""


class EventStore(Protocol):
    """Somewhere to remember which events have been handled."""

    def seen(self, event_id: str) -> bool: ...
    def remember(self, event_id: str) -> None: ...


class MemoryEventStore:
    """For tests and single-process use."""

    def __init__(self) -> None:
        self._seen: set[str] = set()

    def seen(self, event_id: str) -> bool:
        return event_id in self._seen

    def remember(self, event_id: str) -> None:
        self._seen.add(event_id)


class FileEventStore:
    """Append-only file. Survives restarts, needs no database.

    Fine for the volumes this project will see; swap for a real store when
    more than one process is handling webhooks, since this is not atomic
    across processes.
    """

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._cache: set[str] = set()
        if self.path.exists():
            self._cache = {
                line.strip() for line in self.path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            }

    def seen(self, event_id: str) -> bool:
        return event_id in self._cache

    def remember(self, event_id: str) -> None:
        if event_id in self._cache:
            return
        self._cache.add(event_id)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(event_id + "\n")


@dataclass(frozen=True)
class Delivery:
    """The outcome of handling one webhook."""

    order: Order | None
    delivered: bool
    duplicate: bool
    reason: str = ""

    @property
    def http_status(self) -> int:
        """A duplicate is a success: any error just triggers another retry."""
        return 200 if (self.delivered or self.duplicate) else 202


# ------------------------------------------------------------- signatures


def verify_lemonsqueezy(raw_body: bytes, headers: Mapping[str, str], secret: str) -> None:
    """`X-Signature` is a hex HMAC-SHA256 of the raw body."""
    provided = _header(headers, "x-signature")
    if not provided:
        raise SignatureError("missing X-Signature header")
    expected = hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, provided.strip()):
        raise SignatureError("signature does not match")


def verify_paddle(
    raw_body: bytes,
    headers: Mapping[str, str],
    secret: str,
    *,
    now: float | None = None,
    max_age: int = MAX_SIGNATURE_AGE_SECONDS,
) -> None:
    """`Paddle-Signature: ts=<unix>;h1=<hex>` over `ts:body`.

    The timestamp is part of the signed payload, so an attacker cannot move
    it — which is what makes checking its age meaningful.
    """
    raw = _header(headers, "paddle-signature")
    if not raw:
        raise SignatureError("missing Paddle-Signature header")

    parts = dict(
        piece.split("=", 1) for piece in raw.split(";") if "=" in piece
    )
    timestamp, provided = parts.get("ts"), parts.get("h1")
    if not timestamp or not provided:
        raise SignatureError("malformed Paddle-Signature header")

    try:
        age = (now if now is not None else time.time()) - int(timestamp)
    except ValueError:
        raise SignatureError("malformed timestamp in Paddle-Signature") from None
    if age > max_age:
        raise SignatureError(f"signature is {int(age)}s old; replay window is {max_age}s")
    if age < -max_age:
        raise SignatureError("signature timestamp is in the future")

    signed = timestamp.encode() + b":" + raw_body
    expected = hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, provided):
        raise SignatureError("signature does not match")


def verify_gumroad(raw_body: bytes, headers: Mapping[str, str], secret: str) -> None:
    """Gumroad pings are unsigned — there is nothing to verify.

    Raising rather than silently passing: a caller who thinks they are
    authenticating this endpoint should find out here, not after someone
    posts a forged sale to it. If you must use Gumroad, verify each sale
    against its API before delivering, and treat the ping as a hint only.
    """
    raise SignatureError(
        "Gumroad pings carry no signature. Verify the sale against Gumroad's "
        "API before delivering, or use a provider that signs its webhooks."
    )


VERIFIERS = {
    "lemonsqueezy": verify_lemonsqueezy,
    "paddle": verify_paddle,
    "gumroad": verify_gumroad,
}


# ----------------------------------------------------------------- orders


def parse_order(provider: str, payload: dict[str, Any]) -> Order:
    """Reconstruct an Order from a provider's payload."""
    if provider == "lemonsqueezy":
        return _parse_lemonsqueezy(payload)
    if provider == "paddle":
        return _parse_paddle(payload)
    if provider == "gumroad":
        return _parse_gumroad(payload)
    raise WebhookError(f"no order parser for provider {provider!r}")


def event_id(provider: str, payload: dict[str, Any], raw_body: bytes) -> str:
    """A stable id for this event, for deduplication.

    Falls back to a hash of the body when the provider supplies no id: a
    retry sends identical bytes, so the hash is stable for the case that
    matters.
    """
    if provider == "lemonsqueezy":
        meta = payload.get("meta") or {}
        if identifier := meta.get("event_id") or meta.get("webhook_id"):
            return f"ls:{identifier}"
        if order_id := (payload.get("data") or {}).get("id"):
            return f"ls:order:{order_id}"
    if provider == "paddle":
        if identifier := payload.get("event_id") or payload.get("notification_id"):
            return f"paddle:{identifier}"
    if provider == "gumroad":
        if identifier := payload.get("sale_id"):
            return f"gumroad:{identifier}"
    return f"{provider}:sha256:{hashlib.sha256(raw_body).hexdigest()[:32]}"


def _parse_lemonsqueezy(payload: dict[str, Any]) -> Order:
    data = payload.get("data") or {}
    attributes = data.get("attributes") or {}
    custom = ((payload.get("meta") or {}).get("custom_data")) or {}
    items = attributes.get("first_order_item") or {}

    slugs = _slugs(custom)
    if not slugs and items.get("product_name"):
        slugs = [str(items["product_name"])]

    return Order(
        order_id=str(data.get("id") or attributes.get("identifier") or ""),
        provider="lemonsqueezy",
        email=str(attributes.get("user_email") or ""),
        offer_slugs=slugs,
        total=_money(attributes.get("total")),
        currency=str(attributes.get("currency") or "USD"),
        test_mode=bool(attributes.get("test_mode")),
        raw=payload,
    )


def _parse_paddle(payload: dict[str, Any]) -> Order:
    data = payload.get("data") or {}
    custom = data.get("custom_data") or {}
    totals = (data.get("details") or {}).get("totals") or {}
    return Order(
        order_id=str(data.get("id") or ""),
        provider="paddle",
        email=str((data.get("customer") or {}).get("email") or ""),
        offer_slugs=_slugs(custom),
        total=_money(totals.get("grand_total")),
        currency=str(totals.get("currency_code") or "USD"),
        test_mode=str(data.get("status", "")).lower() == "draft",
        raw=payload,
    )


def _parse_gumroad(payload: dict[str, Any]) -> Order:
    return Order(
        order_id=str(payload.get("sale_id") or ""),
        provider="gumroad",
        email=str(payload.get("email") or ""),
        offer_slugs=_slugs(payload.get("url_params") or payload),
        total=_money(payload.get("price")),
        currency=str(payload.get("currency") or "USD").upper(),
        test_mode=str(payload.get("test")).lower() == "true",
        raw=payload,
    )


def _slugs(custom: Mapping[str, Any]) -> list[str]:
    """Offer slugs we sent through the checkout as custom data."""
    raw = custom.get("offers") or custom.get("offer") or ""
    if isinstance(raw, list):
        return [str(item) for item in raw if str(item).strip()]
    return [piece.strip() for piece in str(raw).split(",") if piece.strip()]


def _money(value: Any) -> float:
    """Providers send minor units as ints and majors as strings. Normalise.

    An int is treated as cents, which is the convention for every provider
    here; a string or float is already a major-unit amount.
    """
    if value is None:
        return 0.0
    if isinstance(value, bool):
        return 0.0
    if isinstance(value, int):
        return round(value / 100, 2)
    try:
        return round(float(value), 2)
    except (TypeError, ValueError):
        return 0.0


# ---------------------------------------------------------------- handler


def handle_webhook(
    provider: str,
    raw_body: bytes,
    headers: Mapping[str, str],
    secret: str,
    store: EventStore,
    *,
    deliver=None,
    accepted_events: tuple[str, ...] = ("order_created", "transaction.completed", "sale"),
    now: float | None = None,
) -> Delivery:
    """Verify, deduplicate, then deliver.

    `deliver` is called with the Order exactly once per event; anything it
    raises propagates, so the provider retries and the event is *not* marked
    handled. That ordering is deliberate: marking first would lose the sale
    if delivery failed.
    """
    verifier = VERIFIERS.get(provider)
    if verifier is None:
        raise WebhookError(f"no verifier for provider {provider!r}")
    if provider == "paddle":
        verifier(raw_body, headers, secret, now=now)
    else:
        verifier(raw_body, headers, secret)

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError as exc:
        raise WebhookError(f"body is not JSON: {exc}") from None
    if not isinstance(payload, dict):
        raise WebhookError("body is not a JSON object")

    name = event_name(provider, payload)
    if accepted_events and name and name not in accepted_events:
        return Delivery(None, delivered=False, duplicate=False, reason=f"ignored event {name!r}")

    identifier = event_id(provider, payload, raw_body)
    if store.seen(identifier):
        return Delivery(None, delivered=False, duplicate=True, reason="already handled")

    order = parse_order(provider, payload)
    if deliver is not None:
        deliver(order)
    store.remember(identifier)
    return Delivery(order, delivered=True, duplicate=False)


def event_name(provider: str, payload: dict[str, Any]) -> str:
    """The provider's name for this event, or "" when it does not say.

    Public because what an event *is* decides more than delivery: a refund and
    a sale arrive at the same URL, and a caller that grants access needs to be
    able to take it back.
    """
    if provider == "lemonsqueezy":
        return str((payload.get("meta") or {}).get("event_name") or "")
    if provider == "paddle":
        return str(payload.get("event_type") or "")
    return "sale" if payload.get("sale_id") else ""


def _header(headers: Mapping[str, str], name: str) -> str | None:
    """Case-insensitive lookup: header casing varies by web framework."""
    for key, value in headers.items():
        if key.lower() == name:
            return value
    return None


def sign_for_testing(secret: str, raw_body: bytes) -> str:
    """The signature Lemon Squeezy would send. For tests and local replay."""
    return hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()
