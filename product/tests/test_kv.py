"""The key-value store, which is the one that runs in production.

`FileGrantStore` is the tested reference; this has to behave the same way
while talking a wire protocol, and it has one thing the file store does not: a
seat count that survives two devices arriving at once.
"""

from __future__ import annotations

import json

import pytest

from paywall.kv import EVENT_TTL_SECONDS, FakeKV, KVError, RestKVGrantStore
from paywall.models import Grant


def grant(order="1", **kw) -> Grant:
    base = dict(order_id=order, provider="lemonsqueezy", email="Buyer@Example.test",
                codes="c", key="MF1-KEY", nonce="nonce-123456", created=1000.0)
    return Grant(**{**base, **kw})


@pytest.fixture
def kv():
    return FakeKV()


@pytest.fixture
def store(kv):
    return RestKVGrantStore(transport=kv, namespace="test")


def test_it_behaves_like_the_file_store(store):
    store.put(grant())
    assert store.by_order("1").key == "MF1-KEY"
    assert store.by_nonce("nonce-123456").order_id == "1"
    assert [g.order_id for g in store.by_email("buyer@example.test")] == ["1"]
    assert store.by_order("nope") is None
    assert store.by_nonce("nope") is None


def test_keys_are_namespaced(store, kv):
    store.put(grant())
    assert "test:grant:1" in kv.values
    assert "test:nonce:nonce-123456" in kv.values


def test_seats_are_counted_in_a_set_not_the_document(store, kv):
    store.put(grant())
    store.activate("1", "device-a", 2)
    assert kv.sets["test:seats:1"] == {"device-a"}
    # the document itself carries no activations, so rewriting it is safe
    assert json.loads(kv.values["test:grant:1"])["activations"] == []
    assert store.by_order("1").activations == ["device-a"]


def test_the_same_device_does_not_spend_a_second_seat(store):
    store.put(grant())
    assert store.activate("1", "device-a", 1).used == 1
    assert store.activate("1", "device-a", 1).allowed
    assert store.activate("1", "device-a", 1).used == 1


def test_the_seat_limit_holds(store):
    store.put(grant())
    assert store.activate("1", "device-a", 2).allowed
    assert store.activate("1", "device-b", 2).allowed
    refused = store.activate("1", "device-c", 2)
    assert not refused.allowed and "2 device(s)" in refused.reason


def test_a_device_refused_in_a_race_does_not_stay_in_the_set(store, kv):
    """Two devices arriving together must not both be let in.

    The set is added to first and counted afterwards, so the loser sees the
    count over the limit. It has to take its own member back out, or the set
    stays permanently oversized and every later device is refused for a seat
    nobody is using.
    """
    store.put(grant())
    store.activate("1", "device-a", 1)
    refused = store.activate("1", "device-b", 1)
    assert not refused.allowed
    assert kv.sets["test:seats:1"] == {"device-a"}
    assert refused.used == 1


def test_revoking_stops_activation_and_keeps_the_devices(store, kv):
    store.put(grant())
    store.activate("1", "device-a", 2)
    assert store.revoke("1")
    assert store.by_order("1").revoked
    assert not store.activate("1", "device-b", 2).allowed
    assert kv.sets["test:seats:1"] == {"device-a"}


def test_buying_another_rung_keeps_the_devices(store):
    store.put(grant())
    store.activate("1", "device-a", 1)
    store.put(grant(codes="cu", key="MF1-KEY-2"))
    assert store.by_order("1").activations == ["device-a"]
    assert store.by_order("1").codes == "cu"


def test_it_also_deduplicates_webhooks(store, kv):
    assert not store.seen("evt-1")
    store.remember("evt-1")
    assert store.seen("evt-1")
    # with an expiry, so handled markers do not accumulate for ever
    assert any(
        call[0] == "SET" and str(EVENT_TTL_SECONDS) in call[1] for call in kv.calls
    )


def test_a_corrupt_document_reads_as_absent(store, kv):
    kv.values["test:grant:1"] = "{ not json"
    assert store.by_order("1") is None


def test_an_error_from_the_store_is_raised_not_swallowed():
    def angry(command, args, body):
        raise KVError("connection refused")

    store = RestKVGrantStore(transport=angry)
    with pytest.raises(KVError):
        store.by_order("1")


def test_it_refuses_to_start_without_credentials():
    with pytest.raises(KVError, match="base URL and a token"):
        RestKVGrantStore()
    with pytest.raises(KVError):
        RestKVGrantStore("https://kv.example.test", "")


def test_email_index_holds_several_orders(store):
    store.put(grant("1"))
    store.put(grant("2", nonce="nonce-abcdef"))
    assert [g.order_id for g in store.by_email("buyer@example.test")] == ["1", "2"]
