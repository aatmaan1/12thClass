"""The grant store: seats, nonces, revocation, and surviving a restart.

The seat count is the whole of one rung of the ladder, so the cases that would
quietly give it away — unlocking twice on one device, buying a second rung,
replaying the log — are the ones worth pinning.
"""

from __future__ import annotations

import json

import pytest

from paywall.models import Grant
from paywall.store import FileGrantStore, MemoryGrantStore


def grant(order="1", **kw) -> Grant:
    base = dict(order_id=order, provider="lemonsqueezy", email="buyer@example.test",
                codes="c", key="MF1-KEY", nonce="nonce-123456", created=1000.0)
    return Grant(**{**base, **kw})


@pytest.fixture(params=["memory", "file"])
def store(request, tmp_path):
    if request.param == "memory":
        return MemoryGrantStore()
    return FileGrantStore(tmp_path / "grants.jsonl")


def test_a_grant_can_be_found_three_ways(store):
    store.put(grant())
    assert store.by_order("1").key == "MF1-KEY"
    assert store.by_nonce("nonce-123456").order_id == "1"
    assert [g.order_id for g in store.by_email("BUYER@example.test")] == ["1"]


def test_missing_lookups_are_empty_not_errors(store):
    assert store.by_order("nope") is None
    assert store.by_nonce("") is None
    assert store.by_nonce("nope") is None
    assert store.by_email("") == []


def test_a_grant_needs_an_order_id(store):
    with pytest.raises(ValueError, match="order id"):
        store.put(grant(order=""))


def test_the_same_device_does_not_spend_a_second_seat(store):
    store.put(grant())
    first = store.activate("1", "device-a", 1)
    second = store.activate("1", "device-a", 1)
    assert (first.allowed, first.used) == (True, 1)
    assert (second.allowed, second.used) == (True, 1)


def test_the_seat_limit_is_enforced(store):
    store.put(grant(codes="cu"))
    assert store.activate("1", "device-a", 2).allowed
    assert store.activate("1", "device-b", 2).allowed
    refused = store.activate("1", "device-c", 2)
    assert not refused.allowed
    assert "2 device(s)" in refused.reason
    assert refused.remaining == 0


def test_activation_needs_a_device_id(store):
    store.put(grant())
    refused = store.activate("1", "", 1)
    assert not refused.allowed and "device id" in refused.reason


def test_activating_an_unknown_order_is_refused(store):
    assert not store.activate("nope", "device-a", 1).allowed


def test_revoking_stops_activation(store):
    store.put(grant())
    assert store.revoke("1")
    assert store.by_order("1").revoked
    refused = store.activate("1", "device-a", 1)
    assert not refused.allowed and "withdrawn" in refused.reason


def test_revoking_something_that_is_not_there_says_so(store):
    assert store.revoke("nope") is False


def test_buying_another_rung_does_not_cost_a_seat(store):
    """The second webhook for one order must not reset its devices."""
    store.put(grant())
    store.activate("1", "device-a", 1)
    store.put(grant(codes="cu", key="MF1-KEY-2"))
    assert store.by_order("1").activations == ["device-a"]
    assert store.activate("1", "device-a", 5).used == 1


def test_a_revocation_survives_a_second_grant(store):
    store.put(grant())
    store.revoke("1")
    store.put(grant(codes="cu"))
    assert store.by_order("1").revoked


# ------------------------------------------------- the file store only


def test_the_file_store_replays_everything(tmp_path):
    path = tmp_path / "grants.jsonl"
    first = FileGrantStore(path)
    first.put(grant())
    first.activate("1", "device-a", 2)
    first.put(grant(order="2", nonce="nonce-abcdef"))
    first.revoke("2")

    second = FileGrantStore(path)
    assert second.by_order("1").activations == ["device-a"]
    assert second.by_order("2").revoked
    assert second.by_nonce("nonce-123456").order_id == "1"
    assert [g.order_id for g in second.all()] == ["1", "2"]


def test_one_corrupt_line_does_not_lose_the_sales_after_it(tmp_path):
    path = tmp_path / "grants.jsonl"
    store = FileGrantStore(path)
    store.put(grant())
    with path.open("a", encoding="utf-8") as handle:
        handle.write("{not json at all\n\n")
    store.put(grant(order="2"))

    reloaded = FileGrantStore(path)
    assert {g.order_id for g in reloaded.all()} == {"1", "2"}


def test_compaction_keeps_the_state_and_shrinks_the_log(tmp_path):
    path = tmp_path / "grants.jsonl"
    store = FileGrantStore(path)
    store.put(grant())
    store.activate("1", "device-a", 3)
    store.activate("1", "device-b", 3)
    before = len(path.read_text(encoding="utf-8").splitlines())

    assert store.compact() == 1
    after = path.read_text(encoding="utf-8").splitlines()
    assert len(after) == 1 < before
    assert json.loads(after[0])["activations"] == ["device-a", "device-b"]
    assert FileGrantStore(path).by_order("1").activations == ["device-a", "device-b"]


def test_the_log_is_append_only(tmp_path):
    """The history of a sale stays readable, which is the point of the format."""
    path = tmp_path / "grants.jsonl"
    store = FileGrantStore(path)
    store.put(grant())
    store.activate("1", "device-a", 1)
    store.revoke("1")
    kinds = [json.loads(line)["t"] for line in path.read_text(encoding="utf-8").splitlines()]
    assert kinds == ["grant", "activate", "revoke"]
