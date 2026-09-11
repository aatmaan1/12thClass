"""Licence keys: the string a buyer pastes in, and what it may not allow.

Two directions matter. A key must survive being copied out of an email, typed
in lower case and pasted with spaces in it — anything else is a support
ticket. And a key must not survive being edited, re-signed with another
secret, or having an entitlement added to it.
"""

from __future__ import annotations

import pytest

from paywall.licence import (
    SECONDS_PER_DAY,
    LicenceError,
    expiry_date,
    issue,
    verify,
)

SECRET = "a-real-secret"


def test_a_key_round_trips(product):
    key = issue(SECRET, order_id="90210", codes="cb")
    licence = verify(SECRET, key, product=product)
    assert licence.order_id == "90210"
    assert licence.codes == "bc"          # sorted, so the string is canonical
    assert licence.expires == 0


def test_codes_are_deduplicated_and_sorted():
    assert verify(SECRET, issue(SECRET, order_id="1", codes="ccb")).codes == "bc"


def test_a_key_survives_being_pasted_badly(product):
    key = issue(SECRET, order_id="90210", codes="c")
    for mangled in (
        key.lower(),
        key.replace("-", ""),
        key.replace("-", " "),
        f"  {key}\n",
        key.lower().replace("-", "  "),
    ):
        assert verify(SECRET, mangled, product=product).order_id == "90210"


def test_an_edited_key_is_refused(product):
    key = issue(SECRET, order_id="90210", codes="c")
    # flip one character of the payload, keeping the shape intact
    body = key.split("-", 1)[1]
    flipped = "B" if body[6] != "B" else "C"
    edited = key.split("-", 1)[0] + "-" + body[:6] + flipped + body[7:]
    with pytest.raises(LicenceError, match="not valid"):
        verify(SECRET, edited, product=product)


def test_another_secret_cannot_sign_a_key(product):
    key = issue("someone-elses-secret", order_id="90210", codes="c")
    with pytest.raises(LicenceError, match="not valid"):
        verify(SECRET, key, product=product)


def test_rubbish_is_refused(product):
    for rubbish in ("", "hello", "MF1-", "MF1-AAAAA", "MF1-" + "A" * 40, "MF1-!!!!!"):
        with pytest.raises(LicenceError):
            verify(SECRET, rubbish, product=product)


def test_an_expiry_is_honoured(product):
    key = issue(SECRET, order_id="1", codes="c", expires_days=30, now=0)
    assert verify(SECRET, key, product=product, now=29 * SECONDS_PER_DAY).expires == 30
    with pytest.raises(LicenceError, match="expired"):
        verify(SECRET, key, product=product, now=31 * SECONDS_PER_DAY)


def test_no_expiry_by_default(product):
    """A guide bought in October has to still open in March."""
    key = issue(SECRET, order_id="1", codes="c", now=0)
    licence = verify(SECRET, key, product=product, now=400 * SECONDS_PER_DAY)
    assert licence.expires == 0
    assert expiry_date(licence) == ""


def test_the_expiry_date_reads_back():
    key = issue(SECRET, order_id="1", codes="c", expires_days=1, now=0)
    assert expiry_date(verify(SECRET, key, now=0)) == "1970-01-02"


def test_an_unknown_code_is_kept_not_refused(product):
    """A key from a newer build must still open what it can."""
    key = issue(SECRET, order_id="1", codes="cz")
    licence = verify(SECRET, key, product=product)
    assert licence.unknown_codes == "z"
    assert "c" in licence.codes


def test_a_key_that_opens_nothing_here_is_refused(product):
    key = issue(SECRET, order_id="1", codes="z")
    with pytest.raises(LicenceError, match="opens nothing"):
        verify(SECRET, key, product=product)


def test_issuing_needs_a_secret_and_sane_inputs():
    with pytest.raises(LicenceError, match="secret"):
        issue("", order_id="1", codes="c")
    with pytest.raises(LicenceError, match="order id"):
        issue(SECRET, order_id="", codes="c")
    with pytest.raises(LicenceError, match="order id"):
        issue(SECRET, order_id="has|pipe", codes="c")
    with pytest.raises(LicenceError, match="codes"):
        issue(SECRET, order_id="1", codes="")
    with pytest.raises(LicenceError, match="codes"):
        issue(SECRET, order_id="1", codes="c-b")


def test_verifying_needs_a_secret():
    with pytest.raises(LicenceError, match="secret"):
        verify("", issue(SECRET, order_id="1", codes="c"))


def test_a_key_is_short_enough_to_paste():
    key = issue(SECRET, order_id="123456789", codes="cbud")
    assert len(key) < 80
    assert key.startswith("MF1-")


def test_expiry_is_checked_after_the_signature(product):
    """An attacker must not learn anything from which error comes back."""
    expired = issue(SECRET, order_id="1", codes="c", expires_days=1, now=0)
    later = 10 * SECONDS_PER_DAY
    with pytest.raises(LicenceError, match="expired"):
        verify(SECRET, expired, product=product, now=later)
    # the same key against the wrong secret says "not valid", not "expired"
    with pytest.raises(LicenceError, match="not valid"):
        verify("wrong", expired, product=product, now=later)
