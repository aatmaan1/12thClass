"""Rendering, and the leak check that decides whether a build may ship.

The leak check is the test that tests the paywall. If it can be fooled, every
other guarantee here is a comment.
"""

from __future__ import annotations

import json

import pytest

from paywall.render import (
    LeakError,
    check_render,
    leak_check,
    render_app,
    stray_hosts,
)

TEMPLATE = (
    "<title>Fixture</title>\n"
    "<script>const DATA = /*__DATA__*/;\nconst PAYWALL = /*__PAYWALL__*/;</script>\n"
)

PAID = {
    "chapters": {
        "a1": {"s": {"sol": (
            "Take moments about the pivot, then substitute the numerical values "
            "with their units before simplifying, because the marking scheme "
            "awards a mark for the substitution line itself and not for the "
            "final number alone."
        )}}
    }
}


def test_the_page_carries_the_free_bundle_and_the_config():
    page = render_app(
        TEMPLATE, {"chapters": [{"id": "a1", "title": "Chapter 1"}]},
        {"product": "fixture", "prices": {"core": "₹499"}},
        title="Fixture", tagline="A fixture",
    )
    assert "Chapter 1" in page
    assert '"product":"fixture"' in page
    assert "₹499" in page
    assert check_render(page) == []
    assert page.startswith("<!doctype html>")
    assert page.rstrip().endswith("</html>")


def test_a_template_without_the_placeholders_is_refused():
    with pytest.raises(RuntimeError, match="__DATA__"):
        render_app("<p>nothing here</p>", {}, {}, title="t", tagline="t")
    with pytest.raises(RuntimeError, match="__PAYWALL__"):
        render_app("<script>/*__DATA__*/</script>", {}, {}, title="t", tagline="t")


def test_the_renderer_keeps_one_title():
    page = render_app(TEMPLATE, {}, {}, title="The Only Title", tagline="t")
    assert page.count("<title>") == 1
    assert "The Only Title" in page


def test_broken_output_is_recognised():
    assert "placeholder" in " ".join(check_render("<!doctype html>/*__DATA__*/</body>"))
    assert "unbalanced" in " ".join(check_render("<!doctype html><script></body>"))
    assert "not complete" in " ".join(check_render("<p>fragment</p>"))


def test_the_leak_check_finds_paid_text_in_the_page():
    leaked = render_app(
        TEMPLATE, {"everything": PAID}, {}, title="t", tagline="t"
    )
    report = leak_check(leaked, PAID)
    assert report.leaks == ["chapters/a1/s.sol"]
    assert report.checked_snippets == 1


def test_the_leak_check_passes_a_properly_split_page():
    page = render_app(
        TEMPLATE, {"chapters": [{"id": "a1", "title": "Chapter 1", "lock": ["s.sol"]}]},
        {}, title="t", tagline="t",
    )
    report = leak_check(page, PAID)
    assert report.leaks == []
    assert report.checked_snippets == 1


def test_the_leak_check_is_not_fooled_by_reformatting():
    """A leak that got reflowed on the way in is still a leak."""
    reflowed = PAID["chapters"]["a1"]["s"]["sol"].replace(" ", "\n   ")
    page = render_app(TEMPLATE, {"leak": reflowed}, {}, title="t", tagline="t")
    assert leak_check(page, PAID).leaks == ["chapters/a1/s.sol"]


def test_short_fields_are_not_snippet_checked():
    """Too short to be distinctive: a false alarm teaches people to force builds."""
    page = render_app(TEMPLATE, {}, {}, title="t", tagline="t")
    report = leak_check(page, {"docs": {"d1": {"body": "Q1. (a)"}}})
    assert report.checked_snippets == 0
    assert report.leaks == []


def test_the_leak_check_walks_nested_payloads():
    paid = {"g": {"i": {"a": {"b": {"c": PAID["chapters"]["a1"]["s"]["sol"]}}}}}
    page = render_app(TEMPLATE, {}, {}, title="t", tagline="t")
    assert leak_check(page, paid).checked_snippets == 1


def test_external_hosts_are_reported():
    page = render_app(
        TEMPLATE, {"link": "see https://tracker.example.com/x and "
                           "https://fonts.googleapis.com/css2"},
        {}, title="t", tagline="t",
    )
    assert stray_hosts(page) == ["tracker.example.com"]


def test_the_favicon_is_the_products_own():
    page = render_app(TEMPLATE, {}, {}, title="t", tagline="t", icon="\U0001f4d0")
    assert "%F0%9F%93%90" in page


def test_the_leak_error_exists_for_the_build_to_raise():
    with pytest.raises(LeakError):
        raise LeakError("refused")


def test_control_characters_in_the_template_are_refused():
    """They survive into the file and the browser silently drops them."""
    with pytest.raises(RuntimeError, match="control characters"):
        render_app(TEMPLATE + "\x01raw sentinel", {}, {}, title="t", tagline="t")


def test_the_renderer_escapes_the_title_and_tagline():
    page = render_app(TEMPLATE, {}, {}, title='Cheap "Guide" & Co',
                      tagline="<script>alert(1)</script>")
    assert "&amp; Co" in page
    assert "<script>alert(1)</script>" not in page.split("<body>")[0]


def test_the_bundle_is_json_the_page_can_parse():
    page = render_app(TEMPLATE, {"chapters": [{"id": "a1"}]}, {"k": "v"},
                      title="t", tagline="t")
    body = page.split("const DATA = ", 1)[1].split(";\n", 1)[0]
    assert json.loads(body) == {"chapters": [{"id": "a1"}]}
