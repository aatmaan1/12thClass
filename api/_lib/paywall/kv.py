"""A grant store for somewhere with no disk.

`FileGrantStore` is the right thing on a machine that keeps its filesystem. A
serverless function does not have one: `/tmp` survives until the instance is
recycled, several instances run at once, and none of them see each other's
writes. A paywall built on that would count devices per instance and lose the
claim record between the checkout and the thank-you page.

So this speaks the Redis REST protocol that Upstash and Vercel KV both expose
— HTTP GET and POST with a bearer token, no client library, no dependency
beyond `urllib`. Everything goes through an injectable transport, so the
behaviour is testable without a network or an account.

Seat counting uses a **set**, not a counter: `SADD` returns 1 only when the
member was new, so re-unlocking the same browser cannot spend a second seat
however many times it happens, and two devices racing cannot both be told
they were the last one in. When a race does push the set past the seat limit,
the loser removes its own member and is refused — the alternative, trusting a
read-then-write count, hands out an extra device every time two people unlock
at once.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict
from typing import Any, Callable

from .models import Grant
from .store import Activation, grant_from_record

#: How long a handled-event marker is kept. Providers retry for hours, not
#: weeks, and keeping them for ever makes the store grow without bound.
EVENT_TTL_SECONDS = 7 * 24 * 3600

Transport = Callable[[str, list[str], str | None], Any]


class KVError(RuntimeError):
    """The store could not be reached or answered unexpectedly."""


class RestKVGrantStore:
    """Grants, seats, nonces and webhook dedup in a Redis-compatible KV.

    Keys, all namespaced so one database can hold several products:

        <ns>:grant:<order>     the grant, as JSON
        <ns>:nonce:<nonce>     order id, for the thank-you page's claim
        <ns>:email:<email>     JSON list of order ids, for support lookups
        <ns>:seats:<order>     set of install ids
        <ns>:event:<event id>  a handled webhook, with a TTL
    """

    def __init__(
        self,
        base_url: str = "",
        token: str = "",
        *,
        namespace: str = "paywall",
        transport: Transport | None = None,
        timeout: float = 5.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.namespace = namespace
        self.timeout = timeout
        self._transport = transport or self._http
        if transport is None and not (self.base_url and self.token):
            raise KVError("a KV store needs a base URL and a token")

    # -- grants ----------------------------------------------------------

    def put(self, grant: Grant) -> None:
        if not grant.order_id:
            raise ValueError("a grant needs an order id")
        existing = self.by_order(grant.order_id)
        if existing is not None:
            grant.revoked_at = grant.revoked_at or existing.revoked_at
        # Activations live in their own set, not in the document, so a grant
        # rewritten by a second purchase cannot drop the devices already in use.
        grant.activations = []
        self._command(["SET", self._key("grant", grant.order_id)],
                      json.dumps(asdict(grant), ensure_ascii=False))
        if grant.nonce:
            self._command(["SET", self._key("nonce", grant.nonce)], grant.order_id)
        if grant.email:
            self._index_email(grant.email, grant.order_id)

    def by_order(self, order_id: str) -> Grant | None:
        raw = self._command(["GET", self._key("grant", order_id)])
        if not raw:
            return None
        try:
            record = json.loads(raw)
        except (TypeError, json.JSONDecodeError):
            return None
        grant = grant_from_record(record)
        grant.activations = self._activations(order_id)
        return grant

    def by_nonce(self, nonce: str) -> Grant | None:
        if not nonce:
            return None
        order_id = self._command(["GET", self._key("nonce", nonce)])
        return self.by_order(str(order_id)) if order_id else None

    def by_email(self, email: str) -> list[Grant]:
        wanted = (email or "").strip().lower()
        if not wanted:
            return []
        raw = self._command(["GET", self._key("email", wanted)])
        try:
            orders = json.loads(raw) if raw else []
        except (TypeError, json.JSONDecodeError):
            orders = []
        found = [self.by_order(str(o)) for o in orders]
        return [g for g in found if g is not None]

    def revoke(self, order_id: str, *, now: float | None = None) -> bool:
        grant = self.by_order(order_id)
        if grant is None:
            return False
        grant.revoked_at = now if now is not None else time.time()
        activations = grant.activations
        self.put(grant)
        # `put` clears the document's activation list; the set is untouched, so
        # a revocation that is later reversed does not silently free devices.
        grant.activations = activations
        return True

    # -- seats -----------------------------------------------------------

    def activate(
        self, order_id: str, install_id: str, seats: int, *, now: float | None = None
    ) -> Activation:
        grant = self.by_order(order_id)
        if grant is None:
            return Activation(False, seats, 0, "no such order")
        if grant.revoked:
            return Activation(False, seats, len(grant.activations), "this licence was withdrawn")
        if not install_id:
            return Activation(False, seats, len(grant.activations), "no device id sent")

        key = self._key("seats", order_id)
        added = int(self._command(["SADD", key, install_id]) or 0)
        used = int(self._command(["SCARD", key]) or 0)
        if used > seats:
            if added:
                # We are the one over the line; take our own member back out
                # rather than leaving the set permanently oversized.
                self._command(["SREM", key, install_id])
                used -= 1
            return Activation(
                False, seats, used,
                f"this licence covers {seats} device(s) and all of them are in use",
            )
        return Activation(True, seats, used)

    # -- webhook deduplication (the EventStore protocol) -----------------

    def seen(self, event_id: str) -> bool:
        return bool(self._command(["EXISTS", self._key("event", event_id)]))

    def remember(self, event_id: str) -> None:
        self._command(
            ["SET", self._key("event", event_id), "1", "EX", str(EVENT_TTL_SECONDS)]
        )

    # -- plumbing --------------------------------------------------------

    def _activations(self, order_id: str) -> list[str]:
        members = self._command(["SMEMBERS", self._key("seats", order_id)])
        return [str(m) for m in members] if isinstance(members, list) else []

    def _index_email(self, email: str, order_id: str) -> None:
        key = self._key("email", email.strip().lower())
        raw = self._command(["GET", key])
        try:
            orders = json.loads(raw) if raw else []
        except (TypeError, json.JSONDecodeError):
            orders = []
        if order_id not in orders:
            orders.append(order_id)
            self._command(["SET", key], json.dumps(orders))

    def _key(self, kind: str, value: str) -> str:
        return f"{self.namespace}:{kind}:{value}"

    def _command(self, parts: list[str], body: str | None = None) -> Any:
        return self._transport(parts[0], parts[1:], body)

    def _http(self, command: str, args: list[str], body: str | None) -> Any:
        """One Redis command over the REST protocol.

        The value goes in the request body rather than the path so that a
        licence key, an email address or a JSON document cannot be mangled by
        URL length limits or path normalisation.
        """
        path = "/".join(
            [command.lower()] + [urllib.parse.quote(str(a), safe="") for a in args]
        )
        request = urllib.request.Request(
            f"{self.base_url}/{path}",
            data=body.encode("utf-8") if body is not None else None,
            headers={"Authorization": f"Bearer {self.token}"},
            method="POST" if body is not None else "GET",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8") or "{}")
        except urllib.error.URLError as exc:
            raise KVError(f"KV store unreachable: {exc}") from None
        except json.JSONDecodeError as exc:
            raise KVError(f"KV store returned something that is not JSON: {exc}") from None
        if isinstance(payload, dict) and payload.get("error"):
            raise KVError(str(payload["error"]))
        return payload.get("result") if isinstance(payload, dict) else payload


class FakeKV:
    """An in-process stand-in for the REST protocol, for tests.

    Implements only the commands `RestKVGrantStore` sends. It is not a Redis
    emulator; if the store starts using a new command this will fail loudly
    rather than quietly returning None.
    """

    def __init__(self) -> None:
        self.values: dict[str, str] = {}
        self.sets: dict[str, set[str]] = {}
        self.calls: list[tuple[str, list[str]]] = []

    def __call__(self, command: str, args: list[str], body: str | None) -> Any:
        self.calls.append((command, list(args)))
        name = command.upper()
        if name == "SET":
            self.values[args[0]] = body if body is not None else (args[1] if len(args) > 1 else "")
            return "OK"
        if name == "GET":
            return self.values.get(args[0])
        if name == "EXISTS":
            return 1 if args[0] in self.values else 0
        if name == "SADD":
            members = self.sets.setdefault(args[0], set())
            before = len(members)
            members.add(args[1])
            return len(members) - before
        if name == "SREM":
            members = self.sets.setdefault(args[0], set())
            had = args[1] in members
            members.discard(args[1])
            return 1 if had else 0
        if name == "SCARD":
            return len(self.sets.get(args[0], ()))
        if name == "SMEMBERS":
            return sorted(self.sets.get(args[0], ()))
        raise AssertionError(f"FakeKV does not implement {name}")
