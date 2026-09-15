"""The gate: what reaches the public page, and what does not.

Every test here is really one question asked a different way — is the paid
content absent from the free half? A paywall that answers "mostly" does not
answer at all.
"""

from __future__ import annotations

import json

import pytest

from paywall.models import Entitlement, GateError, GateRule
from paywall.split import LOCK_FIELD, split_bundle

from .conftest import build_product


def by_id(items, identifier):
    return next(item for item in items if item["id"] == identifier)


def test_paid_fields_are_absent_from_the_free_half(bundle, product):
    split = split_bundle(bundle, product)
    free = json.dumps(split.free, ensure_ascii=False)

    for identifier in ("a1", "a2"):
        chapter = by_id(bundle["chapters"], identifier)
        assert chapter["s"]["sol"] not in free
        assert chapter["s"]["pyq"] not in free
        assert chapter["recall"] not in free
        # and the free parts are still there
        assert chapter["s"]["scope"] in free
        assert chapter["intro"] in free


def test_samples_are_free_in_full(bundle, product):
    split = split_bundle(bundle, product)
    sample = by_id(split.free["chapters"], "a3")
    assert sample["s"]["sol"] == by_id(bundle["chapters"], "a3")["s"]["sol"]
    assert LOCK_FIELD not in sample
    assert "a3" not in split.paid["chapters"]


def test_gated_items_say_what_is_withheld(bundle, product):
    split = split_bundle(bundle, product)
    locked = by_id(split.free["chapters"], "a1")
    assert locked[LOCK_FIELD] == ["recall", "s.pyq", "s.sol"]
    # the shape of the product stays public even when its content does not
    assert locked["title"] == "Chapter 1"


def test_the_paid_half_is_keyed_by_what_unlocks_it(bundle, product):
    split = split_bundle(bundle, product)
    assert set(split.paid) == {"chapters", "docs"}
    assert set(split.paid["chapters"]) == {"a1", "a2"}
    assert set(split.paid["chapters"]["a1"]) == {"recall", "s"}
    assert set(split.paid["chapters"]["a1"]["s"]) == {"pyq", "sol"}
    assert set(split.paid["docs"]) == {"paid-doc"}


def test_a_whole_collection_can_be_public(bundle, product):
    split = split_bundle(bundle, product)
    assert split.free["langs"] == bundle["langs"]


def test_freeing_a_subtree_frees_everything_under_it(bundle):
    product = build_product(rules=(
        GateRule(collection="chapters", samples=(),
                 free_fields=("id", "num", "title", "intro", "s")),
        GateRule(collection="docs", samples=(), free_fields=("id", "title", "blurb")),
        GateRule(collection="langs", free_whole=True),
    ))
    split = split_bundle(bundle, product)
    chapter = by_id(split.free["chapters"], "a1")
    assert set(chapter["s"]) == {"scope", "pyq", "sol"}
    assert chapter[LOCK_FIELD] == ["recall"]


def test_an_empty_field_is_not_locked(bundle, product):
    """A padlock over content that does not exist is a promise we cannot keep."""
    bundle["chapters"][0]["recall"] = ""
    split = split_bundle(bundle, product)
    assert by_id(split.free["chapters"], "a1")[LOCK_FIELD] == ["s.pyq", "s.sol"]
    assert "recall" not in split.paid["chapters"]["a1"]


def test_a_collection_the_gate_ignores_is_refused(bundle, product):
    bundle["secrets"] = [{"id": "x", "body": "..."}]
    with pytest.raises(GateError, match="says nothing about"):
        split_bundle(bundle, product)


def test_a_gate_naming_a_missing_collection_is_refused(bundle, product):
    del bundle["docs"]
    with pytest.raises(GateError, match="bundle does not have"):
        split_bundle(bundle, product)


def test_a_sample_that_does_not_exist_is_refused(bundle):
    product = build_product(rules=(
        GateRule(collection="chapters", samples=("a9",),
                 free_fields=("id", "num", "title", "intro", "s.scope")),
        GateRule(collection="docs", samples=(), free_fields=("id", "title", "blurb")),
        GateRule(collection="langs", free_whole=True),
    ))
    with pytest.raises(GateError, match="sample"):
        split_bundle(bundle, product)


def test_a_rule_that_withholds_nothing_is_refused(bundle):
    """Freeing every field is not a paywall, and should not look like one."""
    product = build_product(rules=(
        GateRule(collection="chapters", samples=(),
                 free_fields=("id", "num", "title", "intro", "recall", "s")),
        GateRule(collection="docs", samples=(), free_fields=("id", "title", "blurb")),
        GateRule(collection="langs", free_whole=True),
    ))
    with pytest.raises(GateError, match="withholds nothing"):
        split_bundle(bundle, product)


def test_gated_content_nothing_unlocks_is_refused(bundle):
    product = build_product(entitlements=(
        Entitlement(offer="core", code="c", grants=("chapters",), seats=1),
    ), packs=())
    with pytest.raises(GateError, match="no entitlement grants 'docs'"):
        split_bundle(bundle, product)


def test_a_pack_nothing_unlocks_is_refused(bundle):
    product = build_product(packs=("packs.mystery",))
    with pytest.raises(GateError, match="no entitlement grants"):
        split_bundle(bundle, product)


def test_a_gated_collection_must_be_a_list(bundle, product):
    bundle["chapters"] = {"a1": {"id": "a1"}}
    with pytest.raises(GateError, match="must be lists"):
        split_bundle(bundle, product)


def test_free_key_field_is_required():
    with pytest.raises(GateError, match="key field"):
        GateRule(collection="chapters", key="id", free_fields=("title",))


def test_a_rule_freeing_no_fields_is_refused():
    with pytest.raises(GateError, match="frees no fields"):
        GateRule(collection="chapters", free_fields=())


def test_a_gate_with_no_readable_sample_warns(bundle, product):
    """Byte share cannot see this, and it is the failure that loses the sale."""
    stingy = build_product(rules=(
        GateRule(collection="chapters", samples=(),
                 free_fields=("id", "num", "title", "intro", "s.scope")),
        GateRule(collection="docs", samples=("free-doc",),
                 free_fields=("id", "title", "blurb")),
        GateRule(collection="langs", free_whole=True),
    ))
    warnings = split_bundle(bundle, stingy).warnings
    assert any("readable in full" in w and "chapters" in w for w in warnings)
    # the shipped fixture names a sample, so it does not warn
    assert not any("readable in full" in w for w in split_bundle(bundle, product).warnings)


def test_giving_away_most_of_it_warns(bundle):
    product = build_product(rules=(
        GateRule(collection="chapters", samples=("a1", "a2"),
                 free_fields=("id", "num", "title", "intro", "s.scope", "s.pyq")),
        GateRule(collection="docs", samples=("free-doc", "paid-doc"),
                 free_fields=("id", "title", "blurb")),
        GateRule(collection="langs", free_whole=True),
    ))
    split = split_bundle(bundle, product)
    assert any("tip jar" in w for w in split.warnings)


def test_the_report_adds_up(bundle, product):
    split = split_bundle(bundle, product)
    chapters = next(c for c in split.collections if c.collection == "chapters")
    assert (chapters.items, chapters.samples, chapters.gated) == (3, 1, 2)
    assert 0 < split.free_share < 1
    assert split.paid_bytes > 0
