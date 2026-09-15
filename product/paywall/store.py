"""Where purchases, seat activations and revocations are remembered.

A signed licence key proves what was bought. Three things it cannot do on its
own, and this is the small amount of state they need:

* **Hand the key to the buyer.** The checkout redirect arrives back at our
  thank-you page carrying a nonce the browser generated before leaving. The
  webhook stores the grant against that nonce; the page claims it. So the key
  reaches the buyer without an email provider in the path, and without putting
  a guessable order number in a URL that hands out products.
* **Count seats.** A five-seat batch licence is a real product only if the
  sixth device is refused.
* **Undo a sale.** Refunds and chargebacks have to be able to take access
  back, and a self-verifying key cannot be un-signed.

Append-only JSON lines: it survives a restart, needs no database, and the
whole history of a sale stays readable afterwards. Like `storefront`'s event
store it is not atomic across processes — fine for one worker, and worth
replacing with something real before there are several.
"""

from __future__ import annotations

import json
import os
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Protocol

from .models import Grant


@dataclass(frozen=True)
class Activation:
    """The outcome of one device asking to use a licence."""

    allowed: bool
    seats: int
    used: int
    reason: str = ""

    @property
    def remaining(self) -> int:
        return max(self.seats - self.used, 0)


class GrantStore(Protocol):
    def put(self, grant: Grant) -> None: ...
    def by_order(self, order_id: str) -> Grant | None: ...
    def by_nonce(self, nonce: str) -> Grant | None: ...
    def by_email(self, email: str) -> list[Grant]: ...
    def revoke(self, order_id: str, *, now: float | None = None) -> bool: ...
    def activate(
        self, order_id: str, install_id: str, seats: int, *, now: float | None = None
    ) -> Activation: ...


class MemoryGrantStore:
    """For tests, and for a build that only wants to check the wiring."""

    def __init__(self) -> None:
        self._by_order: dict[str, Grant] = {}

    # -- writes ----------------------------------------------------------

    def put(self, grant: Grant) -> None:
        if not grant.order_id:
            raise ValueError("a grant needs an order id")
        grant.created = grant.created or time.time()
        existing = self._by_order.get(grant.order_id)
        if existing is not None:
            # A second webhook for the same order — another rung of the ladder
            # bought, or a retry after a rename. Keep the activations already
            # spent; a buyer must not lose a seat by buying more.
            grant.activations = list(existing.activations)
            grant.revoked_at = grant.revoked_at or existing.revoked_at
        self._by_order[grant.order_id] = grant

    def revoke(self, order_id: str, *, now: float | None = None) -> bool:
        grant = self._by_order.get(order_id)
        if grant is None:
            return False
        grant.revoked_at = now if now is not None else time.time()
        return True

    def activate(
        self, order_id: str, install_id: str, seats: int, *, now: float | None = None
    ) -> Activation:
        """Claim a seat for `install_id`, idempotently.

        Keyed on the device's install id, not on a request: unlocking twice in
        the same browser must not burn a second seat. Clearing site data does
        lose the id and does spend one — that is a support case, not something
        to solve by not counting.
        """
        grant = self._by_order.get(order_id)
        if grant is None:
            return Activation(False, seats, 0, "no such order")
        if grant.revoked:
            return Activation(False, seats, len(grant.activations), "this licence was withdrawn")
        if install_id and install_id in grant.activations:
            return Activation(True, seats, len(grant.activations))
        if not install_id:
            return Activation(False, seats, len(grant.activations), "no device id sent")
        if len(grant.activations) >= seats:
            return Activation(
                False, seats, len(grant.activations),
                f"this licence covers {seats} device(s) and all of them are in use",
            )
        grant.activations.append(install_id)
        self._on_activate(grant, install_id, now)
        return Activation(True, seats, len(grant.activations))

    def _on_activate(self, grant: Grant, install_id: str, now: float | None) -> None:
        """Hook for subclasses that persist."""

    # -- reads -----------------------------------------------------------

    def by_order(self, order_id: str) -> Grant | None:
        return self._by_order.get(order_id)

    def by_nonce(self, nonce: str) -> Grant | None:
        if not nonce:
            return None
        found = [g for g in self._by_order.values() if g.nonce == nonce]
        return max(found, key=lambda g: g.created) if found else None

    def by_email(self, email: str) -> list[Grant]:
        wanted = (email or "").strip().lower()
        if not wanted:
            return []
        return sorted(
            (g for g in self._by_order.values() if g.email.strip().lower() == wanted),
            key=lambda g: g.created,
        )

    def all(self) -> list[Grant]:
        return sorted(self._by_order.values(), key=lambda g: g.created)


class FileGrantStore(MemoryGrantStore):
    """The same store, appended to a JSON-lines file as it goes."""

    def __init__(self, path: str | Path) -> None:
        super().__init__()
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._replay()

    def put(self, grant: Grant) -> None:
        super().put(grant)
        self._append({"t": "grant", **asdict(self._by_order[grant.order_id])})

    def revoke(self, order_id: str, *, now: float | None = None) -> bool:
        if not super().revoke(order_id, now=now):
            return False
        self._append({
            "t": "revoke", "order_id": order_id,
            "at": self._by_order[order_id].revoked_at,
        })
        return True

    def _on_activate(self, grant: Grant, install_id: str, now: float | None) -> None:
        self._append({
            "t": "activate", "order_id": grant.order_id, "install": install_id,
            "at": now if now is not None else time.time(),
        })

    def compact(self) -> int:
        """Rewrite the log as one record per grant. Returns the count.

        Written to a temporary file and moved into place, so an interrupted
        compaction leaves the old log intact rather than half a new one.
        """
        grants = self.all()
        handle = tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", delete=False, dir=str(self.path.parent)
        )
        try:
            for grant in grants:
                handle.write(json.dumps({"t": "grant", **asdict(grant)}, ensure_ascii=False) + "\n")
            handle.close()
            os.replace(handle.name, self.path)
        except BaseException:
            handle.close()
            Path(handle.name).unlink(missing_ok=True)
            raise
        return len(grants)

    def _append(self, record: dict) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    def _replay(self) -> None:
        if not self.path.exists():
            return
        for line in self.path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                # One corrupt line must not lose every sale after it.
                continue
            kind = record.pop("t", "grant")
            if kind == "grant":
                self._by_order[str(record.get("order_id"))] = grant_from_record(record)
            elif kind == "revoke":
                grant = self._by_order.get(str(record.get("order_id")))
                if grant is not None:
                    grant.revoked_at = float(record.get("at") or time.time())
            elif kind == "activate":
                grant = self._by_order.get(str(record.get("order_id")))
                install = str(record.get("install") or "")
                if grant is not None and install and install not in grant.activations:
                    grant.activations.append(install)


def grant_from_record(record: dict) -> Grant:
    """Rebuild a Grant from a stored record. Shared with the KV store."""
    return Grant(
        order_id=str(record.get("order_id") or ""),
        provider=str(record.get("provider") or ""),
        email=str(record.get("email") or ""),
        codes=str(record.get("codes") or ""),
        key=str(record.get("key") or ""),
        nonce=str(record.get("nonce") or ""),
        created=float(record.get("created") or 0.0),
        total=float(record.get("total") or 0.0),
        currency=str(record.get("currency") or "USD"),
        test_mode=bool(record.get("test_mode")),
        revoked_at=float(record.get("revoked_at") or 0.0),
        activations=[str(a) for a in record.get("activations") or []],
    )
