"""From a provider webhook to a licence: what was bought, and what we grant.

The dangerous errors here are asymmetric. Granting less than was paid for is a
support ticket; granting more is giving the product away. So the fallback when
an order cannot be read is the cheapest rung, and the tests say so.
"""

from __future__ import annotations

import json

import pytest

from paywall.fulfilment import codes_for_order, custom_data, handle
from paywall.models import Entitlement, Grant
from paywall.store import MemoryGrantStore
from storefront.fulfil import MemoryEventStore, SignatureError, sign_for_testing
from storefront.models import Order

from .conftest import build_product

HOOK_SECRET = "hook-secret"
SIGN_SECRET = "sign-secret"


def ls_payload(**attributes):
    """A Lemon Squeezy order_created body, in the shape it documents."""
    custom = attributes.pop("custom", {"offers": "core"})
    return {
        "meta": {"event_name": attributes.pop("event", "order_created"),
                 "event_id": attributes.pop("event_id", "evt-1"),
                 "custom_data": custom},
        "data": {"id": attributes.pop("order_id", "9001"),
                 "attributes": {
                     "user_email": "buyer@example.test", "total": 64800,
                     "currency": "INR", "test_mode": False,
                     "first_order_item": attributes.pop("item", {"product_id": "111"}),
                     **attributes,
                 }},
    }


def post(payload, *, product=None, grants=None, events=None, product_ids=None, secret=HOOK_SECRET):
    raw = json.dumps(payload).encode()
    return handle(
        product or build_product(), "lemonsqueezy", raw,
        {"X-Signature": sign_for_testing(secret, raw)},
        webhook_secret=HOOK_SECRET, licence_secret=SIGN_SECRET,
        events=events or MemoryEventStore(), grants=grants or MemoryGrantStore(),
        product_ids=product_ids,
    )


def order(provider="lemonsqueezy", slugs=("core",), raw=None) -> Order:
    return Order(order_id="9001", provider=provider, email="b@example.test",
                 offer_slugs=list(slugs), total=499.0, currency="INR", raw=raw or {})


# ---------------------------------------------------------- what was bought


def test_offers_come_from_the_checkout_link_we_built():
    product = build_product()
    assert codes_for_order(product, order(slugs=("core", "bump"))) == "bc"


def test_a_bump_taken_at_checkout_is_read_from_the_line_item():
    """The link said "core"; the buyer added the bump a moment later."""
    product = build_product()
    notes: list[str] = []
    codes = codes_for_order(
        product,
        order(slugs=("core",), raw=ls_payload(item={"product_id": "222"})),
        product_ids={"core": "111", "bump": "222"},
        notes=notes,
    )
    assert codes == "bc"
    assert notes == []


def test_an_unreadable_order_grants_the_cheapest_rung_and_says_so():
    product = build_product()
    notes: list[str] = []
    codes = codes_for_order(product, order(slugs=()), notes=notes)
    assert codes == "c"
    assert any("no recognisable offer" in note for note in notes)


def test_offers_we_do_not_sell_are_reported():
    notes: list[str] = []
    codes = codes_for_order(build_product(), order(slugs=("core", "mystery")), notes=notes)
    assert codes == "c"
    assert any("does not sell" in note for note in notes)


def test_a_rung_bought_alone_gets_what_it_builds_on():
    """Five seats of nothing is not the product anyone paid for."""
    notes: list[str] = []
    codes = codes_for_order(build_product(), order(slugs=("upsell",)), notes=notes)
    assert set(codes) == {"c", "u"}
    assert any("granting those too" in note for note in notes)


def test_a_product_with_no_standalone_offer_cannot_fall_back():
    product = build_product(entitlements=(
        Entitlement(offer="core", code="c", grants=("chapters", "docs"),
                    requires=("extra",)),
        Entitlement(offer="extra", code="e", grants=("packs.revision",), requires=("core",)),
    ))
    with pytest.raises(ValueError, match="no standalone offer"):
        codes_for_order(product, order(slugs=()))


def test_custom_data_is_read_per_provider():
    assert custom_data(order(raw=ls_payload(custom={"nonce": "n-1"})))["nonce"] == "n-1"
    paddle = Order(order_id="1", provider="paddle", email="", offer_slugs=[], total=0,
                   raw={"data": {"custom_data": {"nonce": "n-2"}}})
    assert custom_data(paddle)["nonce"] == "n-2"
    gumroad = Order(order_id="1", provider="gumroad", email="", offer_slugs=[], total=0,
                    raw={"url_params": {"nonce": "n-3"}})
    assert custom_data(gumroad)["nonce"] == "n-3"
    assert custom_data(Order("1", "stripe-link", "", [], 0.0)) == {}


# ------------------------------------------------------------- the handler


def test_a_sale_produces_a_recorded_licence():
    grants = MemoryGrantStore()
    result = post(ls_payload(custom={"offers": "core,bump", "nonce": "n-abcdef123456"}),
                  grants=grants)
    assert result.delivery.delivered
    assert result.http_status == 200
    assert result.grant.codes == "bc"
    assert result.grant.nonce == "n-abcdef123456"
    assert result.grant.email == "buyer@example.test"
    assert grants.by_order("9001").key == result.grant.key


def test_a_forged_webhook_is_refused():
    with pytest.raises(SignatureError):
        post(ls_payload(), secret="not-the-secret")


def test_a_retry_is_not_delivered_twice():
    events, grants = MemoryEventStore(), MemoryGrantStore()
    first = post(ls_payload(), events=events, grants=grants)
    second = post(ls_payload(), events=events, grants=grants)
    assert first.delivery.delivered
    assert second.delivery.duplicate and not second.delivery.delivered
    assert second.http_status == 200      # erroring would only invite another retry


def test_an_event_we_do_not_act_on_is_ignored():
    result = post(ls_payload(event="subscription_created"))
    assert not result.delivery.delivered
    assert "ignored" in result.delivery.reason


def test_a_refund_revokes_the_licence():
    events, grants = MemoryEventStore(), MemoryGrantStore()
    post(ls_payload(), events=events, grants=grants)
    refund = post(ls_payload(event="order_refunded", event_id="evt-2"),
                  events=events, grants=grants)
    assert refund.revoked == "9001"
    assert grants.by_order("9001").revoked


def test_a_refund_flagged_only_in_the_body_is_caught():
    events, grants = MemoryEventStore(), MemoryGrantStore()
    post(ls_payload(), events=events, grants=grants)
    refund = post(ls_payload(event_id="evt-3", refunded=True), events=events, grants=grants)
    assert refund.revoked == "9001"


def test_a_refund_for_something_we_never_granted_is_noted_not_crashed():
    result = post(ls_payload(event="order_refunded"))
    assert result.revoked == ""
    assert any("never granted" in note for note in result.notes)


def test_the_licence_key_verifies_against_what_it_granted():
    from paywall import licence as licence_mod

    product = build_product()
    result = post(ls_payload(custom={"offers": "core,upsell"}), product=product)
    licence = licence_mod.verify(SIGN_SECRET, result.grant.key, product=product)
    assert licence.order_id == "9001"
    assert product.seats_for(licence.codes) == 5
    assert product.grants_for(licence.codes) == ["chapters", "docs"]


def test_a_grant_records_what_was_paid():
    result = post(ls_payload())
    assert result.grant.total == 648.0        # minor units, normalised
    assert result.grant.currency == "INR"
    assert result.grant.test_mode is False


def test_a_test_mode_sale_is_marked_as_one():
    result = post(ls_payload(test_mode=True))
    assert result.grant.test_mode is True
    assert isinstance(result.grant, Grant)
