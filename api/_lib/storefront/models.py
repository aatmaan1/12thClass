"""Types for offer ladders, providers and orders."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

SLUG = re.compile(r"[a-z0-9][a-z0-9-]*")

#: Currency symbols, for display only. A ladder priced in rupees that reports
#: its totals with a dollar sign is not a formatting slip: it is a number
#: nobody can act on.
SYMBOLS = {"USD": "$", "GBP": "\u00a3", "EUR": "\u20ac", "INR": "\u20b9",
           "AUD": "A$", "CAD": "C$", "SGD": "S$", "AED": "AED "}


def currency_symbol(currency: str) -> str:
    return SYMBOLS.get((currency or "").upper(), "")


def money(amount: float, currency: str, *, decimals: bool = False) -> str:
    """An amount with its currency marked, however that currency is written."""
    symbol = currency_symbol(currency)
    text = f"{amount:,.2f}" if decimals or amount != int(amount) else f"{amount:,.0f}"
    return f"{symbol}{text}" if symbol else f"{text} {(currency or '').upper()}"


class Rung(str, Enum):
    """Where an offer sits in the ladder.

    The order matters: each is shown at a different moment, and the moment
    determines how much friction the buyer will tolerate.
    """

    CORE = "core"          # the thing they came for
    BUMP = "bump"          # a checkbox at checkout, no extra decision
    UPSELL = "upsell"      # after paying, card already on file
    DOWNSELL = "downsell"  # shown only if the upsell is declined


#: Friction ordering. A bump interrupts nothing; a downsell is a second ask
#: after a refusal. Take rates fall accordingly, and the projection uses this.
RUNG_ORDER = (Rung.CORE, Rung.BUMP, Rung.UPSELL, Rung.DOWNSELL)


@dataclass(frozen=True)
class Offer:
    """One rung: a thing that can be bought, at a price, at a moment."""

    slug: str
    name: str
    rung: Rung
    price: float
    #: Share of buyers who take this, 0..1. From the pre-sell test where one
    #: exists, from the benchmark table in `economics` where it does not.
    take_rate: float | None = None
    description: str = ""
    #: Path to the file this delivers, relative to the product directory.
    deliverable: str | None = None
    currency: str = "USD"

    def __post_init__(self) -> None:
        if not SLUG.fullmatch(self.slug):
            raise ValueError(f"offer slug must be kebab-case: {self.slug!r}")
        if self.price < 0:
            raise ValueError(f"offer {self.slug!r} has a negative price")
        if self.take_rate is not None and not 0 <= self.take_rate <= 1:
            raise ValueError(f"offer {self.slug!r} take_rate must be 0..1")

    def display(self) -> str:
        return money(self.price, self.currency)


@dataclass
class Ladder:
    """A core offer and the rungs stacked on it.

    Exactly one core; at most one of each other rung. More than that is a
    menu, and a menu converts worse than a sequence — the buyer starts
    comparing instead of deciding.
    """

    slug: str
    product_name: str
    audience: str
    offers: list[Offer] = field(default_factory=list)
    currency: str = "USD"

    def __post_init__(self) -> None:
        if not SLUG.fullmatch(self.slug):
            raise ValueError(f"ladder slug must be kebab-case: {self.slug!r}")
        cores = [o for o in self.offers if o.rung is Rung.CORE]
        if len(cores) != 1:
            raise ValueError(f"ladder {self.slug!r} needs exactly one core offer")
        for rung in (Rung.BUMP, Rung.UPSELL, Rung.DOWNSELL):
            if len([o for o in self.offers if o.rung is rung]) > 1:
                raise ValueError(f"ladder {self.slug!r} has more than one {rung.value}")
        slugs = [o.slug for o in self.offers]
        if len(slugs) != len(set(slugs)):
            raise ValueError(f"ladder {self.slug!r} has duplicate offer slugs")

    @property
    def symbol(self) -> str:
        return currency_symbol(self.currency)

    def money(self, amount: float, *, decimals: bool = False) -> str:
        return money(amount, self.currency, decimals=decimals)

    @property
    def core(self) -> Offer:
        return next(o for o in self.offers if o.rung is Rung.CORE)

    def rung(self, rung: Rung) -> Offer | None:
        return next((o for o in self.offers if o.rung is rung), None)

    @property
    def ordered(self) -> list[Offer]:
        return [o for r in RUNG_ORDER for o in self.offers if o.rung is r]


@dataclass(frozen=True)
class Order:
    """A completed purchase, as reconstructed from a provider webhook."""

    order_id: str
    provider: str
    email: str
    offer_slugs: list[str]
    total: float
    currency: str = "USD"
    test_mode: bool = False
    raw: dict[str, Any] = field(default_factory=dict)
