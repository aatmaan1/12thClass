"""The manifest's own rules — the arithmetic that decides what a key opens."""

from __future__ import annotations

import pytest

from paywall.models import Entitlement, GateError, Grant, Product

from .conftest import build_product


def test_codes_map_both_ways(product):
    assert product.codes_for(["core", "bump"]) == "bc"
    assert product.by_code("u").offer == "upsell"
    assert product.by_code("z") is None
    assert product.entitlement("core").grants == ("chapters", "docs")
    assert product.entitlement("nope") is None


def test_grants_are_listed_in_manifest_order_without_repeats(product):
    assert product.grants_for("bc") == ["chapters", "docs", "packs.revision"]
    assert product.grants_for("cu") == ["chapters", "docs"]
    assert product.grants_for("") == []


def test_seats_are_the_largest_not_the_sum(product):
    """Buying the batch licence on top of the core is five devices, not six."""
    assert product.seats_for("c") == 1
    assert product.seats_for("u") == 5
    assert product.seats_for("cu") == 5
    assert product.seats_for("bcu") == 5
    assert product.seats_for("") == 0


def test_a_rung_bought_alone_reports_what_it_needs(product):
    assert product.missing_requirements("u") == ["core"]
    assert product.missing_requirements("cu") == []
    assert product.missing_requirements("c") == []


def test_a_product_must_sell_something():
    with pytest.raises(GateError, match="no entitlements"):
        build_product(entitlements=())


def test_a_product_must_unlock_something():
    with pytest.raises(GateError, match="nothing unlocks"):
        build_product(entitlements=(
            Entitlement(offer="core", code="c", grants=(), seats=1),
        ), packs=())


def test_codes_cannot_collide():
    with pytest.raises(GateError, match="reuses an entitlement code"):
        build_product(entitlements=(
            Entitlement(offer="core", code="c", grants=("chapters",)),
            Entitlement(offer="bump", code="c", grants=("docs",)),
        ))


def test_a_requirement_must_name_something_real():
    with pytest.raises(GateError, match="requires unknown"):
        build_product(entitlements=(
            Entitlement(offer="core", code="c", grants=("chapters",)),
            Entitlement(offer="bump", code="b", grants=("docs",), requires=("ghost",)),
        ))


def test_an_entitlement_code_is_one_character():
    for bad in ("", "core", "C", "-"):
        with pytest.raises(GateError, match="single lower-case"):
            Entitlement(offer="core", code=bad)


def test_slugs_are_kebab_case():
    with pytest.raises(GateError, match="kebab-case"):
        Entitlement(offer="Core Offer", code="c")
    with pytest.raises(GateError, match="kebab-case"):
        build_product(slug="Marks First")


def test_a_seat_count_below_one_is_refused():
    with pytest.raises(GateError, match="at least one seat"):
        Entitlement(offer="core", code="c", seats=0)


def test_a_runtime_manifest_carries_the_same_arithmetic(product):
    runtime = {
        "slug": product.slug, "name": product.name, "audience": product.audience,
        "entitlements": [
            {"offer": e.offer, "code": e.code, "grants": list(e.grants),
             "seats": e.seats, "requires": list(e.requires)}
            for e in product.entitlements
        ],
    }
    rebuilt = Product.from_runtime(runtime)
    for codes in ("c", "b", "u", "bc", "bcu"):
        assert rebuilt.grants_for(codes) == product.grants_for(codes)
        assert rebuilt.seats_for(codes) == product.seats_for(codes)
        assert rebuilt.missing_requirements(codes) == product.missing_requirements(codes)


def test_a_grant_knows_whether_it_was_withdrawn():
    grant = Grant(order_id="1", provider="ls", email="", codes="c", key="K")
    assert not grant.revoked
    grant.revoked_at = 1.0
    assert grant.revoked
