"""Designing the ladder before building it.

Brunson's claim (notes/day4-scale.md) is that a funnel multiplies revenue on
identical traffic: same product, same audience, 3-10x the money, purely from
what happens after the first yes. That is true, and it is also the kind of
claim that makes people bolt rungs onto a checkout until it converts worse
than the plain page did.

The asymmetry nobody in those sources models is **when** a rung is offered:

* An **order bump** sits inside the checkout. It costs the buyer a decision
  at the exact moment they were about to pay, so it carries a real risk of
  losing the core sale. It has to earn its place.
* A **post-purchase upsell** happens after the money is taken and the card is
  on file. Declining it costs nothing. There is no downside to offering one.

So this module projects revenue per visitor with that friction priced in, and
reports the **break-even take rate** for the bump: below it, the bump is
losing you more core sales than it adds. That number is the whole point —
without it, "add an order bump" is advice you cannot evaluate.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .models import Ladder, Offer, Rung

#: Take rates to assume when a rung has not been measured yet. Brunson reports
#: roughly one in three on bumps; upsells and downsells are softer. Replace
#: these with real numbers the moment the pre-sell or first launch gives you
#: any — they are starting points, not findings.
BENCHMARK_TAKE_RATES: dict[Rung, float] = {
    Rung.BUMP: 0.28,
    Rung.UPSELL: 0.16,
    Rung.DOWNSELL: 0.14,
}

#: Share of core sales an order bump costs you by adding a decision at the
#: moment of payment. Small, but it applies to every buyer, whereas the bump
#: revenue only applies to those who take it.
DEFAULT_BUMP_FRICTION = 0.02

#: Landing-page conversion for a product with proven demand. From the KPI
#: benchmarks in notes/src-affiliate-funded-free-product.md (2-5%).
DEFAULT_CORE_CONVERSION = 0.03


@dataclass
class RungContribution:
    """What one rung adds per buyer."""

    offer: Offer
    take_rate: float
    revenue_per_buyer: float
    share_of_total: float
    measured: bool

    @property
    def rung(self) -> Rung:
        return self.offer.rung


@dataclass
class Projection:
    """Expected revenue for a ladder, with the friction cost priced in."""

    ladder_slug: str
    visitors: int
    core_conversion: float
    effective_conversion: float
    buyers: float
    revenue_per_buyer: float
    revenue_per_visitor: float
    total_revenue: float
    contributions: list[RungContribution] = field(default_factory=list)
    #: Revenue per visitor for the core offer alone, as the comparison.
    baseline_revenue_per_visitor: float = 0.0
    bump_breakeven_take_rate: float | None = None
    warnings: list[str] = field(default_factory=list)

    @property
    def uplift(self) -> float:
        """Multiple over selling the core alone. The number Brunson quotes."""
        if not self.baseline_revenue_per_visitor:
            return 1.0
        return round(self.revenue_per_visitor / self.baseline_revenue_per_visitor, 3)

    def to_row(self) -> dict[str, object]:
        return {
            "ladder": self.ladder_slug,
            "visitors": self.visitors,
            "core_conversion": round(self.core_conversion, 4),
            "effective_conversion": round(self.effective_conversion, 4),
            "buyers": round(self.buyers, 1),
            "revenue_per_buyer": round(self.revenue_per_buyer, 2),
            "revenue_per_visitor": round(self.revenue_per_visitor, 3),
            "baseline_revenue_per_visitor": round(self.baseline_revenue_per_visitor, 3),
            "uplift": self.uplift,
            "total_revenue": round(self.total_revenue, 2),
            "bump_breakeven_take_rate": (
                round(self.bump_breakeven_take_rate, 4)
                if self.bump_breakeven_take_rate is not None
                else ""
            ),
            "warnings": "; ".join(self.warnings),
        }


def project(
    ladder: Ladder,
    *,
    visitors: int = 1_000,
    core_conversion: float = DEFAULT_CORE_CONVERSION,
    bump_friction: float = DEFAULT_BUMP_FRICTION,
) -> Projection:
    """Expected revenue for `ladder`, against the core-only baseline."""
    core = ladder.core
    has_bump = ladder.rung(Rung.BUMP) is not None

    # Friction applies only when something interrupts the checkout itself.
    effective_conversion = core_conversion * (1 - bump_friction) if has_bump else core_conversion
    buyers = visitors * effective_conversion

    contributions = _contributions(ladder)
    revenue_per_buyer = sum(c.revenue_per_buyer for c in contributions)
    total = revenue_per_buyer * (1.0 if not contributions else 1.0)  # per-buyer already summed

    for contribution in contributions:
        contribution.share_of_total = (
            round(contribution.revenue_per_buyer / revenue_per_buyer, 4)
            if revenue_per_buyer
            else 0.0
        )

    revenue_per_visitor = revenue_per_buyer * effective_conversion
    baseline = core.price * core_conversion

    return Projection(
        ladder_slug=ladder.slug,
        visitors=visitors,
        core_conversion=core_conversion,
        effective_conversion=effective_conversion,
        buyers=buyers,
        revenue_per_buyer=round(revenue_per_buyer, 2),
        revenue_per_visitor=round(revenue_per_visitor, 3),
        total_revenue=round(revenue_per_visitor * visitors, 2),
        contributions=contributions,
        baseline_revenue_per_visitor=round(baseline, 3),
        bump_breakeven_take_rate=bump_breakeven(ladder, bump_friction),
        warnings=_warnings(ladder, contributions, bump_friction),
    )


def bump_breakeven(ladder: Ladder, bump_friction: float = DEFAULT_BUMP_FRICTION) -> float | None:
    """Take rate at which an order bump stops costing more than it adds.

    Adding a bump loses `friction` of every core sale, and each lost sale
    costs the whole per-buyer revenue it would have produced without the
    bump. It gains `bump_price x take_rate` from the buyers who remain. Set
    those equal and solve.
    """
    bump = ladder.rung(Rung.BUMP)
    if bump is None or bump.price <= 0:
        return None
    if bump_friction <= 0:
        return 0.0

    # Per-buyer revenue if the bump were not offered at all.
    without_bump = ladder.core.price + sum(
        offer.price * _take_rate(offer) * _conditional(ladder, offer)
        for offer in ladder.offers
        if offer.rung in (Rung.UPSELL, Rung.DOWNSELL)
    )
    # loss = friction * without_bump  (per buyer who would have converted)
    # gain = (1 - friction) * bump.price * rate
    rate = (bump_friction * without_bump) / ((1 - bump_friction) * bump.price)
    return round(min(rate, 1.0), 4)


def compare(projections: list[Projection]) -> list[Projection]:
    """Best ladder first, by revenue per visitor."""
    return sorted(projections, key=lambda p: p.revenue_per_visitor, reverse=True)


def _contributions(ladder: Ladder) -> list[RungContribution]:
    contributions: list[RungContribution] = []
    for offer in ladder.ordered:
        rate = _take_rate(offer)
        conditional = _conditional(ladder, offer)
        contributions.append(
            RungContribution(
                offer=offer,
                take_rate=rate,
                revenue_per_buyer=round(offer.price * rate * conditional, 2),
                share_of_total=0.0,
                measured=offer.take_rate is not None,
            )
        )
    return contributions


def _take_rate(offer: Offer) -> float:
    if offer.rung is Rung.CORE:
        return 1.0
    if offer.take_rate is not None:
        return offer.take_rate
    return BENCHMARK_TAKE_RATES.get(offer.rung, 0.0)


def _conditional(ladder: Ladder, offer: Offer) -> float:
    """A downsell is only seen by buyers who declined the upsell."""
    if offer.rung is not Rung.DOWNSELL:
        return 1.0
    upsell = ladder.rung(Rung.UPSELL)
    return 1.0 - _take_rate(upsell) if upsell else 1.0


def _warnings(
    ladder: Ladder, contributions: list[RungContribution], bump_friction: float
) -> list[str]:
    warnings: list[str] = []

    if any(not c.measured for c in contributions if c.rung is not Rung.CORE):
        warnings.append(
            "some take rates are benchmarks, not measurements — treat the "
            "projection as a design tool, not a forecast"
        )

    bump = ladder.rung(Rung.BUMP)
    if bump:
        breakeven = bump_breakeven(ladder, bump_friction)
        assumed = _take_rate(bump)
        if breakeven is not None and assumed < breakeven:
            warnings.append(
                f"the bump needs {breakeven:.0%} take-up to pay for the checkout "
                f"friction it adds, and you are assuming {assumed:.0%} — drop it "
                "or make it cheaper"
            )
        if bump.price > ladder.core.price * 0.6:
            warnings.append(
                f"the bump at {bump.display()} is steep against a "
                f"{ladder.core.display()} core; bumps convert on being trivial"
            )

    if not ladder.rung(Rung.UPSELL):
        warnings.append(
            "no post-purchase upsell — it is the one rung with no downside, "
            "since the money is already taken and a decline costs nothing"
        )

    upsell = ladder.rung(Rung.UPSELL)
    if upsell and upsell.price < ladder.core.price:
        warnings.append(
            "the upsell is cheaper than the core; upsells are normally the "
            "richer offer, and a cheaper one anchors the wrong way"
        )

    return warnings
