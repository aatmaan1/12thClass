"""Loading ladders from YAML/JSON, and seeding one from a reskin product."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Ladder, Offer, Rung


def load_ladder(path: str | Path) -> Ladder:
    data = _load(Path(path))
    missing = [k for k in ("slug", "product_name", "audience") if not data.get(k)]
    if missing:
        raise ValueError(f"{path}: missing {', '.join(missing)}")

    currency = str(data.get("currency", "USD"))
    return Ladder(
        slug=str(data["slug"]),
        product_name=str(data["product_name"]),
        audience=str(data["audience"]),
        currency=currency,
        offers=[_offer(o, currency) for o in data.get("offers", [])],
    )


def load_copy(path: str | Path | None) -> dict[str, Any]:
    """Load a funnel copy file — the words the offer and thank-you pages use.

    Absent, empty or unreadable-as-a-mapping all mean "use the defaults": a
    build should not fail because nobody has written the sales copy yet, it
    should render the generic page and let the operator see how generic it is.
    """
    if not path:
        return {}
    data = _load(Path(path))
    return data if isinstance(data, dict) else {}


def ladder_from_product(product: Any, *, bump: float = 0.4, upsell: float = 2.0) -> dict[str, Any]:
    """Draft a ladder around a reskin product.

    Prices are seeded off the vertical's own price: a bump at roughly 40% of
    core (bumps convert on being trivial) and an upsell at twice it (upsells
    should be the richer offer). Both are starting points to test, not
    findings — the pre-sell measures the core price, never the ladder.
    """
    core_price = float(getattr(product, "price", None) or 49)
    name = getattr(product, "name", "Product")
    slug = getattr(product, "slug", "product").replace("--", "-")

    return {
        "slug": slug,
        "product_name": name,
        "audience": getattr(product, "audience", ""),
        "offers": [
            {
                "slug": "core",
                "name": name,
                "rung": "core",
                "price": core_price,
                "description": getattr(product, "headline", ""),
            },
            {
                "slug": "bump",
                "name": "TODO: a small, obvious companion",
                "rung": "bump",
                "price": round(core_price * bump),
                "description": "TODO: one line. Bumps convert on being trivial.",
            },
            {
                "slug": "upsell",
                "name": "TODO: the richer version",
                "rung": "upsell",
                "price": round(core_price * upsell),
                "description": "TODO: what the buyer wanted next, offered after paying.",
            },
        ],
    }


def _offer(raw: dict[str, Any], currency: str) -> Offer:
    return Offer(
        slug=str(raw["slug"]),
        name=str(raw["name"]),
        rung=Rung(str(raw.get("rung", "core"))),
        price=float(raw["price"]),
        take_rate=_rate(raw.get("take_rate")),
        description=str(raw.get("description", "")),
        deliverable=raw.get("deliverable"),
        currency=str(raw.get("currency", currency)),
    )


def _rate(value: Any) -> float | None:
    if value in (None, ""):
        return None
    rate = float(value)
    # Accept both 0.28 and 28 — the second is what people type.
    return rate / 100 if rate > 1 else rate


def _load(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in (".yaml", ".yml"):
        try:
            import yaml
        except ImportError as exc:
            raise ImportError("YAML configs need PyYAML, or use JSON.") from exc
        return yaml.safe_load(text) or {}
    return json.loads(text)
