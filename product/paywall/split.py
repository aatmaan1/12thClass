"""Dividing a content bundle into what ships publicly and what is sold.

This is the load-bearing file. Everything else is plumbing around one claim:
**the paid content is never in the public page.** A study app that ships all
27 chapters and hides 25 of them behind a CSS class is not a paywall, it is a
suggestion — view-source defeats it in one keystroke, and the first buyer to
notice is entitled to a refund and a bad review.

So the split happens at build time and produces two artefacts that go to
different places: a free bundle compiled into the page, and a paid bundle that
only the unlock endpoint can read. Nothing withheld is present in the public
file in any form, encoded or otherwise.

What a paywall cannot do is stop a buyer copying what they paid for. Once
unlocked, the content is in their browser. That is true of every digital
product ever sold and it is not what the gate is for: the gate stops casual
free-riding, and the honest version of that claim is in the README rather than
implied by encryption theatre.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from .models import GateError, GateRule, Product

#: Field name added to each gated item, listing the paths withheld from it.
#: The app reads it to decide where to draw a padlock, so the *shape* of the
#: product stays public even when its content does not — a buyer can see
#: exactly what they are being sold before paying.
LOCK_FIELD = "lock"

#: Free share of the product, by bytes, past which the paid half is a tip jar.
#: A judgement call, and better argued with than tripped over silently.
#:
#: There is deliberately no lower bound. The obvious symmetric check — warn
#: when the free half is a tiny fraction of the bytes — cannot be set to a
#: number that means anything: ids and titles alone come to several percent of
#: a small product while telling a reader nothing at all about it. The
#: question worth asking is whether any of it is *readable*, and
#: `_check_samples` asks that instead.
MAX_FREE_SHARE = 0.60


@dataclass
class CollectionSplit:
    """What happened to one collection."""

    collection: str
    items: int = 0
    samples: int = 0
    gated: int = 0
    free_bytes: int = 0
    paid_bytes: int = 0
    withheld_paths: list[str] = field(default_factory=list)


@dataclass
class Split:
    """The two halves, plus what it did — so a build can print it."""

    free: dict[str, Any]
    #: {grant name: {item id: withheld fields}}. Keyed by grant so the unlock
    #: endpoint can hand over exactly what a licence covers, no more.
    paid: dict[str, Any]
    collections: list[CollectionSplit] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def free_bytes(self) -> int:
        return len(json.dumps(self.free, ensure_ascii=False).encode("utf-8"))

    @property
    def paid_bytes(self) -> int:
        return len(json.dumps(self.paid, ensure_ascii=False).encode("utf-8"))

    @property
    def free_share(self) -> float:
        total = self.free_bytes + self.paid_bytes
        return self.free_bytes / total if total else 0.0


def split_bundle(bundle: dict[str, Any], product: Product) -> Split:
    """Apply `product`'s gate to `bundle`.

    Raises `GateError` when the gate is incoherent — a collection that does
    not exist, a sample that is not in it, a rule that withholds nothing.
    Those are build-time mistakes and every one of them ships either a broken
    page or an unpriced product.
    """
    grant_of = _grant_owner(product)
    free: dict[str, Any] = {}
    paid: dict[str, dict[str, Any]] = {}
    report: list[CollectionSplit] = []
    warnings: list[str] = []

    ungated = [key for key in bundle if product.rule(key) is None]
    if ungated:
        raise GateError(
            f"the bundle has collections the gate says nothing about: "
            f"{', '.join(sorted(ungated))}. Add a rule, or list them under "
            "gate.free_collections to ship them publicly on purpose."
        )

    for rule in product.rules:
        if rule.collection not in bundle:
            raise GateError(
                f"gate names collection {rule.collection!r}, which the content "
                f"bundle does not have (it has: {', '.join(sorted(bundle))})"
            )
        value = bundle[rule.collection]

        if rule.free_whole:
            free[rule.collection] = value
            report.append(
                CollectionSplit(
                    rule.collection,
                    items=len(value) if isinstance(value, (list, dict)) else 1,
                    free_bytes=_size(value),
                )
            )
            continue

        if not isinstance(value, list):
            raise GateError(
                f"collection {rule.collection!r} is a {type(value).__name__}; "
                "gated collections must be lists of items"
            )

        grant = grant_of.get(rule.collection)
        if grant is None:
            raise GateError(
                f"collection {rule.collection!r} is gated but no entitlement "
                f"grants {rule.collection!r} — it would be unsellable"
            )

        summary, free_items, paid_items = _split_collection(rule, value)
        free[rule.collection] = free_items
        if paid_items:
            paid.setdefault(grant, {}).update(paid_items)
        report.append(summary)

    for pack in product.packs:
        grant = grant_of.get(pack)
        if grant is None:
            raise GateError(f"pack {pack!r} is built but no entitlement grants it")

    split = Split(free=free, paid=paid, collections=report, warnings=warnings)
    warnings.extend(_check_share(split))
    warnings.extend(_check_samples(product, split))
    return split


def _split_collection(
    rule: GateRule, items: list[dict[str, Any]]
) -> tuple[CollectionSplit, list[dict[str, Any]], dict[str, Any]]:
    summary = CollectionSplit(rule.collection, items=len(items))
    ids = {str(item.get(rule.key)) for item in items}
    unknown = [s for s in rule.samples if s not in ids]
    if unknown:
        raise GateError(
            f"gate for {rule.collection!r} names sample(s) not in the content: "
            f"{', '.join(unknown)}"
        )

    free_items: list[dict[str, Any]] = []
    paid_items: dict[str, Any] = {}
    withheld_paths: set[str] = set()

    for item in items:
        identifier = str(item.get(rule.key))
        if identifier in rule.samples:
            free_items.append(dict(item))
            summary.samples += 1
            summary.free_bytes += _size(item)
            continue

        kept, withheld = _project(item, rule.free_fields)
        if not withheld:
            raise GateError(
                f"gate for {rule.collection!r} withholds nothing from "
                f"{identifier!r} — every field is in free_fields, so there is "
                "nothing to sell"
            )
        kept[LOCK_FIELD] = sorted(withheld)
        withheld_paths.update(withheld)
        free_items.append(kept)
        paid_items[identifier] = _pick(item, withheld)
        summary.gated += 1
        summary.free_bytes += _size(kept)
        summary.paid_bytes += _size(paid_items[identifier])

    summary.withheld_paths = sorted(withheld_paths)
    return summary, free_items, paid_items


def _project(
    item: dict[str, Any], free_fields: tuple[str, ...]
) -> tuple[dict[str, Any], list[str]]:
    """Split one item into its free projection and the paths withheld.

    A path names a leaf or a whole subtree: freeing `s.scope` keeps that one
    section and withholds its siblings; freeing `s` keeps all of them.
    """
    kept: dict[str, Any] = {}
    withheld: list[str] = []
    for path, value in _leaves(item):
        if _covered(path, free_fields):
            _put(kept, path, value)
        elif value not in (None, "", [], {}):
            # An empty field is nothing to sell and nothing to hide. Withholding
            # it would draw a padlock over content that does not exist.
            withheld.append(path)
    return kept, withheld


def _covered(path: str, free_fields: tuple[str, ...]) -> bool:
    """True when `path` is freed outright or sits under a freed subtree."""
    return any(path == f or path.startswith(f + ".") for f in free_fields)


def _leaves(value: Any, prefix: str = "") -> list[tuple[str, Any]]:
    """Every leaf of a nested dict, as (dotted path, value).

    Lists are leaves. A list of gated sub-items would need its own rule, and
    silently treating one as a subtree would hide that from whoever wrote the
    gate.
    """
    if isinstance(value, dict):
        out: list[tuple[str, Any]] = []
        for key, child in value.items():
            out.extend(_leaves(child, f"{prefix}.{key}" if prefix else str(key)))
        return out
    return [(prefix, value)]


def _pick(item: dict[str, Any], paths: list[str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for path in paths:
        _put(out, path, _get(item, path))
    return out


def _get(item: dict[str, Any], path: str) -> Any:
    cursor: Any = item
    for part in path.split("."):
        cursor = cursor[part]
    return cursor


def _put(target: dict[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    cursor = target
    for part in parts[:-1]:
        cursor = cursor.setdefault(part, {})
    cursor[parts[-1]] = value


def _grant_owner(product: Product) -> dict[str, str]:
    """Which grant name covers each collection or pack.

    A grant is named after what it unlocks, so `chapters` is granted by the
    entitlement listing `chapters`. Two entitlements granting the same thing
    is fine — the first in manifest order owns the payload.
    """
    owner: dict[str, str] = {}
    for entitlement in product.entitlements:
        for grant in entitlement.grants:
            owner.setdefault(grant, grant)
    return owner


def _check_share(split: Split) -> list[str]:
    share = split.free_share
    if not (split.free_bytes + split.paid_bytes):
        return []
    if share > MAX_FREE_SHARE:
        return [
            f"{share:.1%} of the product is readable free. Past about "
            f"{MAX_FREE_SHARE:.0%} the paid half is a tip jar — check the "
            "samples list and the free fields."
        ]
    return []


def _check_samples(product: Product, split: Split) -> list[str]:
    """A gate with nothing readable behind it is the sharper failure.

    Byte share cannot see this: a collection can free every id and title and
    look like a few percent of the product while giving a stranger no way to
    judge whether any of it is any good. The sample is the only part of an
    offer that is evidence rather than copy.
    """
    warnings: list[str] = []
    for collection in split.collections:
        rule = product.rule(collection.collection)
        if rule is None or rule.free_whole:
            continue
        if collection.samples == 0 and collection.items > 1:
            warnings.append(
                f"nothing in {collection.collection!r} is readable in full — "
                "a buyer is being asked to trust the description. Name at "
                "least one item under samples."
            )
    return warnings


def _size(value: Any) -> int:
    return len(json.dumps(value, ensure_ascii=False).encode("utf-8"))
