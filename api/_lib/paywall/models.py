"""Types for gating a content product and licensing access to it.

The vocabulary, in one place:

* A **bundle** is the whole product as data — every chapter, every document,
  every translation. It never leaves the build machine intact.
* A **gate** says which parts of it a stranger may read. Applying the gate
  splits the bundle into a **free** half that ships inside the public page and
  a **paid** half that only an endpoint hands out.
* An **entitlement** is what one rung of the ladder unlocks: some grants, and
  a number of seats. `core` unlocks the chapters; `upsell` unlocks no new
  content and five more seats. Both are real products.
* A **licence** is a signed string proving a buyer holds some entitlements. It
  verifies with the secret alone — no database lookup — so the unlock endpoint
  stays a pure function of the key plus a revocation check.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

SLUG = re.compile(r"[a-z0-9][a-z0-9-]*")
CODE = re.compile(r"[a-z0-9]")


class GateError(ValueError):
    """A gate configuration that must not be built."""


@dataclass(frozen=True)
class GateRule:
    """How one collection of the bundle is divided.

    `free_fields` are dotted paths kept in the public page — `id`, `s.scope`.
    Everything else on the item is withheld. `samples` name items handed over
    whole: a paywall with no readable sample asks a stranger to trust a
    description, and the sample is the only part of the offer that is evidence
    rather than copy.
    """

    collection: str
    key: str = "id"
    samples: tuple[str, ...] = ()
    free_fields: tuple[str, ...] = ()
    #: Ship the whole collection publicly. For things that are not the
    #: product — interface translations, for instance.
    free_whole: bool = False

    def __post_init__(self) -> None:
        if self.free_whole:
            return
        if not self.free_fields:
            raise GateError(
                f"gate for {self.collection!r} frees no fields at all — the "
                "public page would have nothing to show and no reason to buy"
            )
        if self.key not in self.free_fields:
            raise GateError(
                f"gate for {self.collection!r} must free its key field "
                f"{self.key!r}, or the page cannot tell which item is which"
            )


@dataclass(frozen=True)
class Entitlement:
    """What one purchasable rung unlocks.

    `code` is a single character carried inside the licence key. It is the one
    field here that must never change once a key has been issued: keys in the
    wild are read against these codes, so re-lettering an entitlement silently
    re-points every licence that contains it.
    """

    offer: str
    code: str
    grants: tuple[str, ...] = ()
    seats: int = 1
    #: Offers that must be held alongside this one. A batch licence is five
    #: seats *of the product*; on its own it is five seats of nothing.
    requires: tuple[str, ...] = ()
    name: str = ""

    def __post_init__(self) -> None:
        if not SLUG.fullmatch(self.offer):
            raise GateError(f"entitlement offer must be kebab-case: {self.offer!r}")
        if not CODE.fullmatch(self.code):
            raise GateError(
                f"entitlement {self.offer!r} needs a single lower-case "
                f"alphanumeric code, got {self.code!r}"
            )
        if self.seats < 1:
            raise GateError(f"entitlement {self.offer!r} must carry at least one seat")


@dataclass(frozen=True)
class Product:
    """A gated content product: the manifest, loaded and checked."""

    slug: str
    name: str
    audience: str
    tagline: str = ""
    currency: str = "USD"
    #: Import path of the module whose `bundle()` returns the content.
    extractor: str = "extract"
    app: str = "app/app.src.html"
    ladder: str = ""
    funnel: str = ""
    rules: tuple[GateRule, ...] = ()
    entitlements: tuple[Entitlement, ...] = ()
    packs: tuple[str, ...] = ()
    #: Directory the build writes, relative to the product directory.
    deploy: str = "deploy"
    support_email: str = ""
    site_url: str = ""
    sample_note: str = ""

    def __post_init__(self) -> None:
        if not SLUG.fullmatch(self.slug):
            raise GateError(f"product slug must be kebab-case: {self.slug!r}")
        if not self.entitlements:
            raise GateError(f"product {self.slug!r} has no entitlements to sell")

        codes = [e.code for e in self.entitlements]
        if len(codes) != len(set(codes)):
            raise GateError(f"product {self.slug!r} reuses an entitlement code: {codes}")
        offers = [e.offer for e in self.entitlements]
        if len(offers) != len(set(offers)):
            raise GateError(f"product {self.slug!r} has two entitlements for one offer")

        known = set(offers)
        for entitlement in self.entitlements:
            unknown = [o for o in entitlement.requires if o not in known]
            if unknown:
                raise GateError(
                    f"entitlement {entitlement.offer!r} requires unknown "
                    f"offer(s): {', '.join(unknown)}"
                )
        if not any(e.grants for e in self.entitlements):
            raise GateError(
                f"product {self.slug!r} gates content that nothing unlocks — "
                "at least one entitlement must grant something"
            )

    @classmethod
    def from_runtime(cls, data: dict) -> "Product":
        """Rebuild a product from the JSON the build writes for the endpoints.

        The endpoints run somewhere with no YAML parser and no content, so they
        read this instead of `product.yaml`. Going through the same class means
        the arithmetic that decides what a key opens exists once, rather than
        once in the build and again in a function where a divergence would be
        invisible until someone was locked out.
        """
        return cls(
            slug=str(data.get("slug") or "product"),
            name=str(data.get("name") or ""),
            audience=str(data.get("audience") or ""),
            support_email=str(data.get("support_email") or ""),
            entitlements=tuple(
                Entitlement(
                    offer=str(e["offer"]), code=str(e["code"]),
                    grants=tuple(e.get("grants") or ()),
                    seats=int(e.get("seats", 1)),
                    requires=tuple(e.get("requires") or ()),
                    name=str(e.get("name", "")),
                )
                for e in data.get("entitlements") or ()
            ),
        )

    def entitlement(self, offer: str) -> Entitlement | None:
        return next((e for e in self.entitlements if e.offer == offer), None)

    def by_code(self, code: str) -> Entitlement | None:
        return next((e for e in self.entitlements if e.code == code), None)

    def rule(self, collection: str) -> GateRule | None:
        return next((r for r in self.rules if r.collection == collection), None)

    def codes_for(self, offers: list[str]) -> str:
        """Entitlement codes for the offers in a purchase, sorted.

        Sorted rather than in manifest order so that one set of entitlements
        has exactly one spelling: `licence.issue` canonicalises the codes it
        signs, and a grant record that spelled the same purchase differently
        would compare unequal to its own key. Display order comes from
        `grants_for`, which walks the manifest.
        """
        wanted = set(offers)
        return "".join(sorted(e.code for e in self.entitlements if e.offer in wanted))

    def grants_for(self, codes: str) -> list[str]:
        """Grant names a set of codes unlocks, in manifest order, deduplicated."""
        out: list[str] = []
        for entitlement in self.entitlements:
            if entitlement.code in codes:
                out.extend(g for g in entitlement.grants if g not in out)
        return out

    def seats_for(self, codes: str) -> int:
        """Seats a set of codes carries.

        The largest, not the sum: a buyer who takes the core and then the
        five-seat batch licence has five seats, not six. Adding them would
        hand out a seat for every rung bought.
        """
        held = [e.seats for e in self.entitlements if e.code in codes]
        return max(held) if held else 0

    def missing_requirements(self, codes: str) -> list[str]:
        """Offers a code set claims to build on but does not hold."""
        held = {e.offer for e in self.entitlements if e.code in codes}
        missing: list[str] = []
        for entitlement in self.entitlements:
            if entitlement.code not in codes:
                continue
            for required in entitlement.requires:
                if required not in held and required not in missing:
                    missing.append(required)
        return missing


@dataclass(frozen=True)
class Licence:
    """A verified licence: who may read what, and until when."""

    order_id: str
    codes: str
    issued: int          # days since the unix epoch
    expires: int = 0     # 0 = never
    #: Entitlement codes present in the key that this build does not know.
    #: Kept rather than rejected: a key issued after a rung was renamed must
    #: still open what it can, instead of locking out a paying buyer.
    unknown_codes: str = ""


@dataclass
class Grant:
    """What the webhook recorded when a purchase completed."""

    order_id: str
    provider: str
    email: str
    codes: str
    key: str
    nonce: str = ""
    created: float = 0.0
    total: float = 0.0
    currency: str = "USD"
    test_mode: bool = False
    revoked_at: float = 0.0
    activations: list[str] = field(default_factory=list)

    @property
    def revoked(self) -> bool:
        return bool(self.revoked_at)
