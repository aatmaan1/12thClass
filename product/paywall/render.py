"""Rendering the gated app into one deployable file, and proving it is gated.

The page is a single self-contained HTML file with the free bundle compiled
into it: no build step on the server, no CDN, no framework. That is the same
choice `reskin/render.py` makes and for the same reason — it works offline, on
a cheap phone, on a train.

The important function here is not the renderer. It is `leak_check`, which
takes distinctive snippets of the paid content and refuses the build if any of
them appear in the public file. Everything else in this project's paywall
rests on the claim that the paid half is absent, and a claim like that has to
be a test rather than an intention: one careless template change is all it
takes to inline the whole bundle again.
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field
from typing import Any

#: How much of a paid field to look for in the public page. Long enough that a
#: coincidental match is not credible, short enough to survive the field being
#: reformatted between build and check.
SNIPPET = 90

#: External hosts the page is allowed to reference. Anything else is reported:
#: a study app that quietly gained a tracker or a CDN dependency is a different
#: product from the one that was reviewed.
ALLOWED_HOSTS = {
    "fonts.googleapis.com", "fonts.gstatic.com", "www.w3.org",
    "cbseacademic.nic.in", "ncert.nic.in", "www.khanacademy.org",
    "www.youtube.com", "github.com",
}

_RESET = """
*,*::before,*::after{box-sizing:border-box}
html{color-scheme:light dark}
body{margin:0}
img,svg,video{max-width:100%}
[hidden]{display:none!important}
"""


class LeakError(RuntimeError):
    """Paid content found in the public page. The build must not ship."""


@dataclass
class RenderReport:
    path: str = ""
    bytes: int = 0
    checked_snippets: int = 0
    leaks: list[str] = field(default_factory=list)
    #: Passages that are in the page *and* in the free half — the same words
    #: on both sides of the gate, not content escaping through it.
    shared: list[str] = field(default_factory=list)
    stray_hosts: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def megabytes(self) -> float:
        return self.bytes / 1048576


def render_app(
    template: str,
    free_bundle: dict[str, Any],
    config: dict[str, Any],
    *,
    title: str,
    tagline: str,
    icon: str = "\U0001f4d0",
    lang: str = "en",
) -> str:
    """Bundle the free content and the paywall config into the app template."""
    if "/*__DATA__*/" not in template:
        raise RuntimeError("app template has no /*__DATA__*/ placeholder")
    if "/*__PAYWALL__*/" not in template:
        raise RuntimeError("app template has no /*__PAYWALL__*/ placeholder")

    # The markdown renderer marks search hits with two control characters. In
    # the template they are literal; a standalone file needs them escaped, or
    # the browser strips them and highlighting silently stops working.
    body = template.replace('"\u0001"', '"\\u0001"').replace('"\u0002"', '"\\u0002"')
    if any(ord(ch) < 9 for ch in body):
        raise RuntimeError("stray control characters in the app template")

    body = body.replace(
        "/*__DATA__*/", json.dumps(free_bundle, ensure_ascii=False, separators=(",", ":"))
    )
    body = body.replace(
        "/*__PAYWALL__*/", json.dumps(config, ensure_ascii=False, separators=(",", ":"))
    )
    body = re.sub(r"^<title>.*?</title>\s*", "", body, count=1, flags=re.S)

    favicon = (
        "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'"
        "%3E%3Ctext y='.92em' font-size='88'%3E" + _uri(icon) + "%3C/text%3E%3C/svg%3E"
    )
    escaped_title, escaped_tagline = html.escape(title), html.escape(tagline)
    head = f"""<!doctype html>
<html lang="{html.escape(lang)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escaped_title}</title>
<meta name="description" content="{escaped_tagline}">
<meta name="theme-color" content="#F6F7FA" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F141E" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{favicon}">
<link rel="apple-touch-icon" href="{favicon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escaped_title}">
<meta property="og:description" content="{escaped_tagline}">
<meta name="twitter:card" content="summary">
<style>{_RESET}</style>
</head>
<body>
"""
    return head + body + "\n</body>\n</html>\n"


def check_render(page: str) -> list[str]:
    """The failures that would ship a broken page rather than no page."""
    problems: list[str] = []
    if "/*__DATA__*/" in page or "/*__PAYWALL__*/" in page:
        problems.append("a placeholder survived into the output")
    if page.count("<script") != page.count("</script>"):
        problems.append("unbalanced <script> tags")
    if "</body>" not in page or "<!doctype html>" not in page:
        problems.append("the document is not complete")
    return problems


def stray_hosts(page: str) -> list[str]:
    found = {host for host in re.findall(r"https?://([a-z0-9.-]+)", page)}
    return sorted(found - ALLOWED_HOSTS)


def leak_check(
    page: str, paid: dict[str, Any], free: dict[str, Any] | None = None
) -> RenderReport:
    """Look for the paid content in the public page.

    Snippets come from the middle of each withheld field rather than its
    start: the start of a section is often a heading that legitimately appears
    in free copy too, and a false alarm that blocks a build teaches people to
    pass --force.

    `free` is the other half of the same split, and it is what stops the check
    crying wolf over shared wording. A line that appears in a paid chapter and
    in the free sample — a standard instruction, a repeated caveat, a
    boilerplate footer — is in the page legitimately, and blocking the build
    over it would be wrong: withholding it was never possible in the first
    place. Such passages are reported as `shared` instead, so they are visible
    without being fatal.

    The gate's own guarantee, that no withheld field survives into the free
    projection, is a separate claim proved in `split`. Both are needed: this
    check cannot see a gate that leaked into `free`, and that one cannot see a
    template that inlined the paid bundle.
    """
    report = RenderReport()
    haystack = _normalise(page)
    free_text = _normalise(json.dumps(free, ensure_ascii=False)) if free else ""
    for grant, items in (paid or {}).items():
        for identifier, payload in (items or {}).items():
            for path, snippet in _snippets(payload):
                report.checked_snippets += 1
                if not snippet or snippet not in haystack:
                    continue
                where = f"{grant}/{identifier}/{path}"
                if free_text and snippet in free_text:
                    report.shared.append(where)
                else:
                    report.leaks.append(where)
    return report


def _snippets(payload: Any, prefix: str = "") -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if isinstance(payload, dict):
        for key, value in payload.items():
            out.extend(_snippets(value, f"{prefix}.{key}" if prefix else str(key)))
        return out
    if isinstance(payload, str) and len(payload) >= SNIPPET * 2:
        middle = len(payload) // 2
        window = payload[middle - SNIPPET // 2: middle + SNIPPET // 2]
        out.append((prefix or "value", _normalise(window)))
    return out


def _normalise(text: str) -> str:
    r"""Whitespace-insensitive, so a reflowed copy still counts as a leak.

    JSON escape sequences are flattened too. Content inlined into the page
    goes through `json.dumps`, which turns a newline into the two characters
    `\` and `n` — not whitespace, so collapsing whitespace alone would let a
    leak past whenever the paid copy happened to be wrapped differently to the
    snippet being looked for.
    """
    flattened = re.sub(r"\\[nrt]", " ", text)
    return re.sub(r"\s+", " ", flattened)


def _uri(icon: str) -> str:
    return "".join(f"%{byte:02X}" for byte in icon.encode("utf-8"))
