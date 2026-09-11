"""Licence keys: signed, self-verifying, offline-checkable.

A key is a short string a buyer pastes into the app. It carries the order it
came from, the entitlement codes it opens and when it expires, and it is
signed with a secret only the seller has. Verification needs the secret and
nothing else — no database, no provider round-trip — which keeps the unlock
endpoint a pure function plus one revocation check.

Why sign rather than store random keys and look them up:

* **The endpoint stays cheap and stateless.** A stolen key cannot be brute
  forced into existence, and a lost database cannot lock out paying buyers.
* **The key says what it opens.** The bump, the batch licence and the core are
  different products, and the string itself distinguishes them.
* **It fails closed on tampering.** Editing a key to add an entitlement or
  push out the expiry invalidates the signature.

The trade-off is that a signed key cannot be un-issued by forgetting it, so
refunds and chargebacks need an explicit revocation list. That lives in
`store.py`, is checked on every unlock, and is the reason the endpoint is not
purely offline after all.

Format:

    MF1-<base32 payload>-<base32 signature>       grouped in fives for typing

The payload is `order|codes|issued|expires`, days since the epoch for both
dates. Base32 rather than base64: no case sensitivity to lose over a phone
call, and no characters that look like each other in the alphabet.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import re
import time

from .models import Licence, Product

PREFIX = "MF1"
#: Bytes of HMAC-SHA256 kept as the signature. 12 bytes is 96 bits: far past
#: forgeable, and short enough to keep the key pasteable.
SIG_BYTES = 12
SECONDS_PER_DAY = 86400
_CLEAN = re.compile(r"[^A-Z2-7]")


class LicenceError(ValueError):
    """A key that must not be honoured."""


def issue(
    secret: str,
    *,
    order_id: str,
    codes: str,
    expires_days: int = 0,
    now: float | None = None,
) -> str:
    """Sign a licence key.

    `expires_days` of 0 means it never expires, which is the right default for
    a one-payment product: a study guide bought in October must still open in
    March, and an expiry that lapses mid-exam-season is a refund and a
    grievance rather than a renewal.
    """
    if not secret:
        raise LicenceError("a signing secret is required to issue licences")
    if not order_id or "|" in order_id:
        raise LicenceError(f"bad order id for a licence: {order_id!r}")
    codes = "".join(sorted(set(codes)))
    if not codes or not codes.isalnum():
        raise LicenceError(f"bad entitlement codes for a licence: {codes!r}")

    issued = _today(now)
    expires = issued + expires_days if expires_days else 0
    payload = f"{order_id}|{codes}|{issued}|{expires}".encode()
    return _format(payload, _sign(secret, payload))


def verify(
    secret: str,
    key: str,
    *,
    product: Product | None = None,
    now: float | None = None,
) -> Licence:
    """Check a key and return what it opens, or raise.

    The signature is checked before the expiry, so a forged key and a stale
    one are indistinguishable from outside: telling them apart would let
    someone probe for the shape of a valid key.

    An entitlement code this build does not recognise is kept on the licence
    rather than rejected. Codes are permanent by contract, but a key issued by
    a newer build than the one serving it is a deployment ordering problem,
    and locking out a paying buyer is the worst available response to it.
    """
    if not secret:
        raise LicenceError("a signing secret is required to verify licences")

    payload, signature = _parse(key)
    expected = _sign(secret, payload)
    if not hmac.compare_digest(expected, signature):
        raise LicenceError("this key is not valid")

    try:
        order_id, codes, issued_raw, expires_raw = payload.decode().split("|")
        issued, expires = int(issued_raw), int(expires_raw)
    except (UnicodeDecodeError, ValueError):
        raise LicenceError("this key is not valid") from None

    if expires and _today(now) > expires:
        raise LicenceError("this key has expired")

    unknown = ""
    if product is not None:
        unknown = "".join(c for c in codes if product.by_code(c) is None)
        if unknown == codes:
            raise LicenceError("this key opens nothing in this product")

    return Licence(
        order_id=order_id, codes=codes, issued=issued, expires=expires,
        unknown_codes=unknown,
    )


def expiry_date(licence: Licence) -> str:
    """The expiry as an ISO date, or an empty string when it never expires."""
    if not licence.expires:
        return ""
    return time.strftime("%Y-%m-%d", time.gmtime(licence.expires * SECONDS_PER_DAY))


def _sign(secret: str, payload: bytes) -> bytes:
    return hmac.new(secret.encode(), PREFIX.encode() + b"\x00" + payload,
                    hashlib.sha256).digest()[:SIG_BYTES]


def _format(payload: bytes, signature: bytes) -> str:
    # Encoded as one byte string, not two encodings concatenated: base32 packs
    # five bytes into eight characters, so joining two separately-encoded
    # halves would only decode back cleanly when the payload happened to be a
    # multiple of five bytes long.
    body = _b32(payload + signature)
    groups = [body[i:i + 5] for i in range(0, len(body), 5)]
    return "-".join([PREFIX] + groups)


def _parse(key: str) -> tuple[bytes, bytes]:
    """Read a key back, tolerating however the buyer pasted it.

    Case, dashes, spaces and a duplicated prefix all get normalised: the key
    arrives from an email client, a screenshot or a WhatsApp message, and
    refusing a lower-case paste is a support ticket, not security.
    """
    if not key:
        raise LicenceError("no key given")
    # The prefix goes before cleaning: it contains a digit the base32 alphabet
    # has no room for, so cleaning first would leave "MF" glued to the body.
    text = key.strip().upper()
    for candidate in (PREFIX, _CLEAN.sub("", PREFIX)):
        if candidate and text.startswith(candidate):
            text = text[len(candidate):]
            break
    cleaned = _CLEAN.sub("", text)
    if len(cleaned) < 16:
        raise LicenceError("this key is too short to be valid")

    raw = _unb32(cleaned)
    if len(raw) <= SIG_BYTES:
        raise LicenceError("this key is not valid")
    return raw[:-SIG_BYTES], raw[-SIG_BYTES:]


def _b32(raw: bytes) -> str:
    return base64.b32encode(raw).decode().rstrip("=")


def _unb32(text: str) -> bytes:
    padded = text + "=" * (-len(text) % 8)
    try:
        return base64.b32decode(padded)
    except Exception:
        raise LicenceError("this key is not valid") from None


def _today(now: float | None) -> int:
    return int((now if now is not None else time.time()) // SECONDS_PER_DAY)
