"""The three endpoints. These are the public surface, so the refusals matter.

The endpoint hands out the product. Everything it says no to has to stay no
under a mistyped key, a forged one, a replayed one, a sixth device and a
refund — and everything it says yes to has to be exactly what was bought and
nothing next to it.
"""

from __future__ import annotations

import json

import pytest

from paywall import licence as licence_mod
from paywall.endpoints import BAD_KEY, claim, unlock
from paywall.models import Grant
from paywall.serverless import (
    ConfigError,
    dispatch,
    load_runtime,
    open_events,
    open_store,
)
from paywall.store import MemoryGrantStore
from storefront.fulfil import MemoryEventStore, sign_for_testing

SECRET = "sign-secret"
HOOK = "hook-secret"

PAID = {
    "chapters": {"a1": {"s": {"sol": "the solution to a1"}}},
    "docs": {"paid-doc": {"body": "the formula sheet"}},
    "packs.revision": {"pack": {"sheets": [{"id": "a1"}]}},
}


@pytest.fixture
def grants():
    return MemoryGrantStore()


def key_for(codes="c", order="9001"):
    return licence_mod.issue(SECRET, order_id=order, codes=codes)


def call(payload, product, grants, **kw):
    return unlock(payload, product=product, secret=SECRET, paid=PAID, grants=grants, **kw)


# ------------------------------------------------------------------ unlock


def test_a_valid_key_returns_what_it_covers(product, grants):
    response = call({"key": key_for("c"), "install": "device-a"}, product, grants)
    assert response.ok
    assert set(response.body["grants"]) == {"chapters", "docs"}
    assert response.body["grants"]["chapters"]["a1"]["s"]["sol"] == "the solution to a1"
    assert (response.body["seats"], response.body["used"]) == (1, 1)


def test_a_key_gets_nothing_it_did_not_buy(product, grants):
    """The bump grants the pack; the core alone must not receive it."""
    core_only = call({"key": key_for("c"), "install": "device-a"}, product, grants)
    assert "packs.revision" not in core_only.body["grants"]

    with_bump = call({"key": key_for("bc", order="9002"), "install": "device-b"},
                     product, grants)
    assert "packs.revision" in with_bump.body["grants"]


def test_the_batch_licence_carries_its_seats(product, grants):
    response = call({"key": key_for("cu"), "install": "device-a"}, product, grants)
    assert response.body["seats"] == 5
    # and unlocks no extra content, which is what it is honestly sold as
    assert set(response.body["grants"]) == {"chapters", "docs"}


def test_a_key_with_no_recorded_purchase_registers_itself(product, grants):
    """Hand-issued keys have no grant record; devices still have to count."""
    response = call({"key": key_for("c", order="comp-1"), "install": "device-a"},
                    product, grants)
    assert response.ok
    assert grants.by_order("comp-1") is not None
    refused = call({"key": key_for("c", order="comp-1"), "install": "device-b"},
                   product, grants)
    assert refused.status == 403


def test_every_bad_key_gets_the_same_answer(product, grants):
    """Telling a forged key from an expired one only helps someone probing."""
    forged = licence_mod.issue("another-secret", order_id="9001", codes="c")
    expired = licence_mod.issue(SECRET, order_id="9001", codes="c",
                                expires_days=1, now=0)
    for bad in ("", "nonsense", "MF1-AAAAA-AAAAA", forged, expired):
        response = call({"key": bad, "install": "device-a"}, product, grants,
                        now=90 * 86400)
        assert response.status == 400
        assert response.body == {"error": BAD_KEY}


def test_the_sixth_device_is_refused_and_told_why(product, grants):
    key = key_for("cu")
    for index in range(5):
        assert call({"key": key, "install": f"device-{index}"}, product, grants).ok
    refused = call({"key": key, "install": "device-6"}, product, grants)
    assert refused.status == 403
    assert "5 device(s)" in refused.body["error"]
    assert "revoked" not in refused.body


def test_the_same_device_can_unlock_again(product, grants):
    key = key_for("c")
    assert call({"key": key, "install": "device-a"}, product, grants).ok
    again = call({"key": key, "install": "device-a"}, product, grants)
    assert again.ok and again.body["used"] == 1


def test_a_revoked_licence_is_refused_and_says_so(product, grants):
    """The app clears its cached copy on this answer, so it has to be distinct."""
    key = key_for("c")
    call({"key": key, "install": "device-a"}, product, grants)
    grants.revoke("9001")
    response = call({"key": key, "install": "device-a"}, product, grants)
    assert response.status == 403
    assert response.body["revoked"] is True


# ------------------------------------------------------------------- claim


def test_a_nonce_finds_the_purchase_that_made_it(product, grants):
    grants.put(Grant(order_id="9001", provider="ls", email="b@example.test",
                     codes="c", key=key_for("c"), nonce="n-abcdef123456"))
    response = claim({"nonce": "n-abcdef123456", "install": "device-a"},
                     product=product, secret=SECRET, paid=PAID, grants=grants)
    assert response.ok
    assert set(response.body["grants"]) == {"chapters", "docs"}


def test_peeking_returns_the_key_without_spending_a_device(product, grants):
    grants.put(Grant(order_id="9001", provider="ls", email="", codes="c",
                     key=key_for("c"), nonce="n-abcdef123456"))
    response = claim({"nonce": "n-abcdef123456", "peek": True},
                     product=product, secret=SECRET, paid=PAID, grants=grants)
    assert response.body["key"] == key_for("c")
    assert grants.by_order("9001").activations == []


def test_an_unknown_or_short_nonce_finds_nothing(product, grants):
    for nonce in ("", "abc", "n-doesnotexist12"):
        response = claim({"nonce": nonce}, product=product, secret=SECRET,
                         paid=PAID, grants=grants)
        assert response.status == 404


def test_a_refunded_purchase_cannot_be_claimed(product, grants):
    grants.put(Grant(order_id="9001", provider="ls", email="", codes="c",
                     key=key_for("c"), nonce="n-abcdef123456"))
    grants.revoke("9001")
    response = claim({"nonce": "n-abcdef123456", "peek": True},
                     product=product, secret=SECRET, paid=PAID, grants=grants)
    assert response.status == 403


# ---------------------------------------------------------------- dispatch


def runtime(product, grants, **env):
    from paywall.serverless import Runtime
    return Runtime(product=product, paid=PAID, secret=SECRET,
                   webhook_secret=env.get("hook", HOOK),
                   provider="lemonsqueezy", grants=grants,
                   events=MemoryEventStore())


def test_dispatch_routes_and_never_raises_on_bad_input(product, grants):
    rt = runtime(product, grants)
    assert dispatch("unlock", b"not json", {}, rt).status == 400
    assert dispatch("unlock", b'["a list"]', {}, rt).status == 400
    assert dispatch("nope", b"{}", {}, rt).status == 404
    assert dispatch("unlock", b"", {}, rt).status == 400


def test_dispatch_runs_the_whole_sale_to_unlock_path(product, grants):
    rt = runtime(product, grants)
    payload = {
        "meta": {"event_name": "order_created", "event_id": "e1",
                 "custom_data": {"offers": "core,bump", "nonce": "n-abcdef123456"}},
        "data": {"id": "9001", "attributes": {"user_email": "b@example.test",
                 "total": 64800, "currency": "INR"}},
    }
    raw = json.dumps(payload).encode()
    hook = dispatch("webhook", raw, {"X-Signature": sign_for_testing(HOOK, raw)}, rt)
    assert hook.ok and hook.body["codes"] == "bc"

    peek = dispatch("claim", b'{"nonce":"n-abcdef123456","peek":true}', {}, rt)
    opened = dispatch(
        "unlock",
        json.dumps({"key": peek.body["key"], "install": "device-a"}).encode(), {}, rt,
    )
    assert set(opened.body["grants"]) == {"chapters", "docs", "packs.revision"}


def test_a_forged_webhook_is_a_400_not_a_crash(product, grants):
    rt = runtime(product, grants)
    raw = b'{"meta":{"event_name":"order_created"},"data":{"id":"1"}}'
    response = dispatch("webhook", raw, {"X-Signature": "00"}, rt)
    assert response.status == 400
    assert "signature" in response.body["error"]


def test_a_webhook_with_no_secret_configured_refuses(product, grants):
    rt = runtime(product, grants, hook="")
    response = dispatch("webhook", b"{}", {}, rt)
    assert response.status == 500
    assert "PAYWALL_WEBHOOK_SECRET" in response.body["error"]


# ----------------------------------------------------------------- runtime


def test_the_runtime_says_what_is_missing(tmp_path):
    with pytest.raises(ConfigError, match="product.json is missing"):
        load_runtime(tmp_path, {"PAYWALL_SECRET": "x"})

    (tmp_path / "product.json").write_text(json.dumps({
        "slug": "p", "name": "P", "audience": "a",
        "entitlements": [{"offer": "core", "code": "c", "grants": ["chapters"]}],
    }), encoding="utf-8")
    (tmp_path / "paid.json").write_text("{}", encoding="utf-8")

    with pytest.raises(ConfigError, match="PAYWALL_SECRET"):
        load_runtime(tmp_path, {})
    with pytest.raises(ConfigError, match="no grant store"):
        load_runtime(tmp_path, {"PAYWALL_SECRET": "x"})

    loaded = load_runtime(tmp_path, {"PAYWALL_SECRET": "x"},
                          grants=MemoryGrantStore())
    assert loaded.product.slug == "p"


def test_there_is_no_silent_in_memory_fallback_for_the_store():
    """It would look like it worked and lose every purchase."""
    with pytest.raises(ConfigError, match="no grant store"):
        open_store({})
    # and the refusal points at the way to look without selling
    with pytest.raises(ConfigError, match="PAYWALL_DEMO"):
        open_store({})


def test_demo_mode_is_opt_in_and_changes_nothing_about_access(product):
    """It keeps state in memory. It does not let anyone in who was not.

    Worth pinning, because everything demo mode relaxes is something that
    must not be relaxed on a deployment taking money — so the one thing it
    must never touch is the signature check.
    """
    from paywall.serverless import demo_mode, demo_warning

    assert demo_mode({}) is False
    assert demo_mode({"PAYWALL_DEMO": "1"}) is True
    assert demo_mode({"PAYWALL_DEMO": "no"}) is False
    assert demo_warning({}) == ""
    assert "per-instance" in demo_warning({"PAYWALL_DEMO": "1"})

    grants = open_store({"PAYWALL_DEMO": "1"})
    events = open_events({"PAYWALL_DEMO": "1"}, grants)
    assert events is not grants and hasattr(events, "seen")

    # a real key still opens the product, and a forged one still does not
    good = call({"key": key_for("c"), "install": "device-a"}, product, grants)
    assert good.ok
    forged = licence_mod.issue("not-the-secret", order_id="9001", codes="c")
    assert call({"key": forged, "install": "device-b"}, product, grants).status == 400


def test_a_file_store_is_accepted_where_there_is_a_disk(tmp_path):
    store = open_store({"PAYWALL_STORE_FILE": str(tmp_path / "g.jsonl")})
    assert store.by_order("1") is None


def test_the_webhook_always_has_somewhere_to_deduplicate(tmp_path):
    """A grant store that cannot remember events must not be used as one.

    Providers retry hard. Handing the webhook a store with no `seen` would
    fail inside a live callback, after the money had been taken.
    """
    from paywall.kv import FakeKV, RestKVGrantStore

    kv = RestKVGrantStore(transport=FakeKV())
    assert open_events({}, kv) is kv          # the KV store does it itself

    file_store = open_store({"PAYWALL_STORE_FILE": str(tmp_path / "g.jsonl")})
    events = open_events({"PAYWALL_STORE_FILE": str(tmp_path / "g.jsonl")}, file_store)
    assert events is not file_store
    events.remember("evt-1")
    assert events.seen("evt-1")

    with pytest.raises(ConfigError, match="deduplicate"):
        open_events({}, MemoryGrantStore())


def test_a_file_backed_runtime_wires_both_stores(tmp_path):
    (tmp_path / "product.json").write_text(json.dumps({
        "slug": "p", "name": "P", "audience": "a",
        "entitlements": [{"offer": "core", "code": "c", "grants": ["chapters"]}],
    }), encoding="utf-8")
    (tmp_path / "paid.json").write_text("{}", encoding="utf-8")
    loaded = load_runtime(tmp_path, {
        "PAYWALL_SECRET": "x", "PAYWALL_STORE_FILE": str(tmp_path / "grants.jsonl"),
    })
    assert loaded.grants is not None and loaded.events is not None
    assert loaded.events is not loaded.grants


def test_product_ids_can_be_pasted_as_json_or_pairs(tmp_path):
    (tmp_path / "product.json").write_text(json.dumps({
        "slug": "p", "name": "P", "audience": "a",
        "entitlements": [{"offer": "core", "code": "c", "grants": ["chapters"]}],
    }), encoding="utf-8")
    (tmp_path / "paid.json").write_text("{}", encoding="utf-8")

    def ids(raw):
        return load_runtime(
            tmp_path, {"PAYWALL_SECRET": "x", "PAYWALL_PRODUCT_IDS": raw},
            grants=MemoryGrantStore(),
        ).product_ids

    assert ids('{"core": "111"}') == {"core": "111"}
    assert ids("core=111,bump=222") == {"core": "111", "bump": "222"}
    assert ids("") == {}
