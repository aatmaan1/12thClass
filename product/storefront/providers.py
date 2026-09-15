"""Adapters for the checkout providers.

Each adapter does three things: declare what the provider can actually do,
emit the setup a human must perform in its dashboard, and build checkout URLs
that carry our attribution through to the webhook.

The capability declaration is the load-bearing part. A ladder designed around
native order bumps and one-click upsells degrades very differently on a
provider that has neither — there, the upsell becomes a second checkout with
the card re-entered, and its take rate collapses. Better to know that when
choosing than after building the funnel.

Facts checked September 2026 and they move: verify against the provider's own
documentation before committing money. Fees especially.
"""

from __future__ import annotations

import urllib.parse
from dataclasses import dataclass, field
from typing import Any

from .models import Ladder, Offer, Rung


@dataclass(frozen=True)
class Capabilities:
    """What a provider can do, and what it costs.

    `merchant_of_record` is the one that matters most for an India-based
    seller with global buyers: without it, VAT/GST registration and remittance
    across dozens of jurisdictions becomes your problem.
    """

    merchant_of_record: bool
    handles_eu_vat: bool
    native_order_bump: bool
    one_click_upsell: bool
    #: Percentage plus fixed fee, as a rough all-in for international sales.
    #: The fixed part is quoted in US dollars by every provider here, which
    #: matters the moment a ladder is priced in anything else.
    fee_percent: float
    fee_fixed: float
    notes: str = ""


@dataclass
class SetupStep:
    """One thing to do in the provider's dashboard before this can sell."""

    offer_slug: str
    action: str
    detail: str
    native: bool = True


@dataclass
class ProviderPlan:
    """Everything needed to stand this ladder up on one provider."""

    provider: str
    capabilities: Capabilities
    steps: list[SetupStep] = field(default_factory=list)
    degradations: list[str] = field(default_factory=list)
    estimated_fee_per_sale: float = 0.0


class Provider:
    """Base adapter. Subclasses declare capabilities and URL shape."""

    name = "base"
    capabilities = Capabilities(False, False, False, False, 0.0, 0.0)

    def __init__(self, store: str, **config: Any) -> None:
        self.store = store
        self.config = config

    # -- setup -----------------------------------------------------------

    def plan(self, ladder: Ladder, *, usd_rate: float = 1.0) -> ProviderPlan:
        """What to create in the dashboard, and how the ladder degrades."""
        steps = [self._step(offer) for offer in ladder.ordered]
        return ProviderPlan(
            provider=self.name,
            capabilities=self.capabilities,
            steps=steps,
            degradations=self._degradations(ladder),
            estimated_fee_per_sale=self.fee_on(ladder.core.price, usd_rate=usd_rate),
        )

    def _step(self, offer: Offer) -> SetupStep:
        native = self._is_native(offer.rung)
        return SetupStep(
            offer_slug=offer.slug,
            action=f"Create a product '{offer.name}' at {offer.display()}",
            detail=self._detail(offer, native),
            native=native,
        )

    def _detail(self, offer: Offer, native: bool) -> str:
        if offer.rung is Rung.CORE:
            return "This is the product the offer page links to."
        if native:
            return f"Attach as a native {offer.rung.value} on the core product."
        return (
            f"No native {offer.rung.value} here — this becomes a separate "
            "checkout the buyer must complete again."
        )

    def _is_native(self, rung: Rung) -> bool:
        if rung is Rung.CORE:
            return True
        if rung is Rung.BUMP:
            return self.capabilities.native_order_bump
        return self.capabilities.one_click_upsell

    def _degradations(self, ladder: Ladder) -> list[str]:
        notes: list[str] = []
        if not self.capabilities.merchant_of_record:
            notes.append(
                "Not a merchant of record: sales tax, VAT and GST registration "
                "and remittance are yours to handle in every jurisdiction you "
                "sell into."
            )
        elif not self.capabilities.handles_eu_vat:
            notes.append("Does not remit EU VAT on your behalf — check before selling into the EU.")
        if ladder.rung(Rung.BUMP) and not self.capabilities.native_order_bump:
            notes.append(
                "No native order bump. The bump has to become a second product "
                "on the offer page, which is a worse moment to ask."
            )
        if ladder.rung(Rung.UPSELL) and not self.capabilities.one_click_upsell:
            notes.append(
                "No one-click upsell. The buyer re-enters card details, so "
                "expect the take rate well below the benchmark."
            )
        return notes

    # -- checkout --------------------------------------------------------

    def checkout_url(
        self,
        offer: Offer,
        *,
        email: str | None = None,
        reference: str | None = None,
        custom: dict[str, str] | None = None,
    ) -> str:
        raise NotImplementedError

    def fee_on(self, amount: float, *, usd_rate: float = 1.0) -> float:
        """Fee on a sale of `amount`, in the currency `amount` is in.

        `usd_rate` is how many of those units make a dollar: the percentage
        scales with the price, the fixed fee does not, so a rupee ladder that
        adds $0.50 to a rupee total under-counts the fee by a factor of about
        eighty. Passing 1.0 means "these are dollars".
        """
        cap = self.capabilities
        return round(amount * cap.fee_percent / 100 + cap.fee_fixed * usd_rate, 2)

    def custom_param(self, key: str) -> str:
        """Query parameter that carries `key` through to the webhook.

        Empty when the provider cannot carry arbitrary data. That is not a
        detail: anything that has to be handed back to the buyer *after*
        payment — a licence key, an unlock — needs a value the browser chose
        before it left, or the only alternative is trusting an order number
        that anyone can guess.
        """
        return ""

    def _product_id(self, offer: Offer) -> str:
        """Provider-side id for an offer, from config keyed by offer slug."""
        ids = self.config.get("product_ids", {})
        if offer.slug not in ids:
            raise KeyError(
                f"no {self.name} product id configured for offer {offer.slug!r} — "
                f"create it in the dashboard, then add it under product_ids"
            )
        return str(ids[offer.slug])


class LemonSqueezy(Provider):
    """Merchant of record, creator-focused, native bumps and upsells.

    The default recommendation for this project: it absorbs global tax, and
    it is the one provider of the four with both native order bumps and
    one-click upsells, so the ladder does not degrade.
    """

    name = "lemonsqueezy"
    capabilities = Capabilities(
        merchant_of_record=True,
        handles_eu_vat=True,
        native_order_bump=True,
        one_click_upsell=True,
        fee_percent=5.0,
        fee_fixed=0.50,
        notes=(
            "Adds roughly 1.5% on international cards, so budget nearer 7% "
            "all-in. Stripe-owned since 2024; payouts to ~79 countries by bank "
            "and 200+ via PayPal — confirm India before relying on it."
        ),
    )

    def custom_param(self, key: str) -> str:
        return f"checkout[custom][{key}]"

    def checkout_url(self, offer, *, email=None, reference=None, custom=None) -> str:
        params: dict[str, str] = {}
        if email:
            params["checkout[email]"] = email
        for key, value in (custom or {}).items():
            params[f"checkout[custom][{key}]"] = value
        if reference:
            params["checkout[custom][reference]"] = reference
        base = f"https://{self.store}.lemonsqueezy.com/buy/{self._product_id(offer)}"
        return _with_params(base, params)


class Paddle(Provider):
    """Merchant of record aimed at SaaS. Solid tax handling, heavier setup."""

    name = "paddle"
    capabilities = Capabilities(
        merchant_of_record=True,
        handles_eu_vat=True,
        native_order_bump=False,
        one_click_upsell=False,
        fee_percent=5.0,
        fee_fixed=0.50,
        notes=(
            "Built for SaaS subscriptions rather than one-off digital goods. "
            "All-in nearer 7-8% internationally once currency conversion is "
            "counted. Approval is a real onboarding step, not instant signup."
        ),
    )

    def custom_param(self, key: str) -> str:
        return f"custom_data[{key}]"

    def checkout_url(self, offer, *, email=None, reference=None, custom=None) -> str:
        params = {"items[0][price_id]": self._product_id(offer), "items[0][quantity]": "1"}
        if email:
            params["customer_email"] = email
        if reference:
            params["custom_data[reference]"] = reference
        for key, value in (custom or {}).items():
            params[f"custom_data[{key}]"] = value
        return _with_params(f"https://{self.store}.paddle.com/checkout", params)


class Gumroad(Provider):
    """Easiest to start on, and no longer a full merchant of record.

    As of 2026 Gumroad does not remit EU VAT for most sellers, which shifts
    that liability back to you. It also lacks native bumps and one-click
    upsells, so a ladder built here loses most of its uplift.
    """

    name = "gumroad"
    capabilities = Capabilities(
        merchant_of_record=False,
        handles_eu_vat=False,
        native_order_bump=False,
        one_click_upsell=False,
        fee_percent=10.0,
        fee_fixed=0.0,
        notes=(
            "Fastest to launch and the weakest on both tax and ladder support. "
            "Reasonable for a first validation sale, poor as a destination."
        ),
    )

    def custom_param(self, key: str) -> str:
        return key

    def checkout_url(self, offer, *, email=None, reference=None, custom=None) -> str:
        params = {"wanted": "true"}
        if email:
            params["email"] = email
        if reference:
            params["reference"] = reference
        params.update(custom or {})
        return _with_params(
            f"https://{self.store}.gumroad.com/l/{self._product_id(offer)}", params
        )


class StripePaymentLink(Provider):
    """Lowest fees, and you become the merchant of record.

    Included because it is the right answer once volume makes 5% hurt more
    than tax compliance costs — but that crossover is a long way off, and
    until then this is the expensive option wearing a cheap price tag.
    """

    name = "stripe-link"
    capabilities = Capabilities(
        merchant_of_record=False,
        handles_eu_vat=False,
        native_order_bump=False,
        one_click_upsell=False,
        fee_percent=2.9,
        fee_fixed=0.30,
        notes=(
            "You are the seller of record: registration, collection and "
            "remittance of VAT/GST everywhere you sell is yours. Stripe Tax "
            "calculates but does not remit. Payment Links carry only "
            "client_reference_id, so a post-purchase unlock has to arrive by "
            "email rather than on the thank-you page."
        ),
    )

    def checkout_url(self, offer, *, email=None, reference=None, custom=None) -> str:
        params: dict[str, str] = {}
        if email:
            params["prefilled_email"] = email
        if reference:
            params["client_reference_id"] = reference
        return _with_params(f"https://buy.stripe.com/{self._product_id(offer)}", params)


REGISTRY: dict[str, type[Provider]] = {
    LemonSqueezy.name: LemonSqueezy,
    Paddle.name: Paddle,
    Gumroad.name: Gumroad,
    StripePaymentLink.name: StripePaymentLink,
}

#: Default for this project. Merchant of record, and the only one of the four
#: where the whole ladder is native.
RECOMMENDED = LemonSqueezy.name


def get_provider(name: str, store: str, **config: Any) -> Provider:
    try:
        return REGISTRY[name](store, **config)
    except KeyError:
        raise ValueError(
            f"unknown provider {name!r}; available: {', '.join(sorted(REGISTRY))}"
        ) from None


def compare_providers(ladder: Ladder, *, usd_rate: float = 1.0) -> list[ProviderPlan]:
    """Every provider's plan for this ladder, best tax posture first."""
    plans = [cls("example").plan(ladder, usd_rate=usd_rate) for cls in REGISTRY.values()]
    return sorted(
        plans,
        key=lambda p: (
            p.capabilities.merchant_of_record,
            p.capabilities.one_click_upsell,
            p.capabilities.native_order_bump,
            -p.estimated_fee_per_sale,
        ),
        reverse=True,
    )


def _with_params(base: str, params: dict[str, str]) -> str:
    if not params:
        return base
    return f"{base}?{urllib.parse.urlencode(params, quote_via=urllib.parse.quote)}"
