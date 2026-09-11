"""The two pages we own: the offer, and what comes after payment.

The checkout in between belongs to the provider, and so does file delivery —
Lemon Squeezy emails a permanent download link on purchase. Building our own
gated download would mean sessions, tokens and a server to hold them, to
reproduce something the provider already does well. `delivery.py` has signed
URLs for the case where a file is too large to hand the provider, but that is
the exception.

So the thank-you page is not a delivery mechanism. It is where the upsell
lives when the provider cannot do it natively, and where a buyer is told what
to do first — the moment most likely to produce a refund is the one where
someone has paid and cannot tell what they bought.
"""

from __future__ import annotations

import html

from .models import Ladder, Offer, Rung

_CSS = """
:root{color-scheme:light dark;--bg:#fbfaf8;--surface:#fff;--ink:#16150f;--muted:#5c584d;
  --line:#e3ded2;--accent:#1a5c4a;--accent-ink:#fff;--shadow:rgba(22,21,15,.09)}
@media (prefers-color-scheme:dark){:root{--bg:#14140f;--surface:#1d1d17;--ink:#f3f0e7;
  --muted:#a8a294;--line:#33322a;--accent:#4fb397;--accent-ink:#10241d;--shadow:rgba(0,0,0,.4)}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:17px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:680px;margin:0 auto;padding:0 20px 80px}
header{padding-block:64px 32px}
h1{font-size:clamp(1.9rem,5.4vw,2.8rem);line-height:1.12;letter-spacing:-.022em;margin:0 0 12px;font-weight:660}
.sub{color:var(--muted);font-size:1.1rem;margin:0 0 28px}
section{border-top:1px solid var(--line);padding-block:30px}
h2{font-size:.79rem;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);
  font-weight:620;margin:0 0 14px}
p{margin:0 0 14px}
ul{margin:0;padding:0;list-style:none}
li{position:relative;padding-left:26px;margin-bottom:11px}
li::before{content:"";position:absolute;left:6px;top:.62em;width:7px;height:7px;
  border-radius:50%;background:var(--accent)}
.cta{display:inline-block;background:var(--accent);color:var(--accent-ink);padding:15px 30px;
  border-radius:10px;font-size:1.05rem;font-weight:600;text-decoration:none;border:0;
  cursor:pointer;font-family:inherit}
.cta:hover{filter:brightness(1.07)}
.cta:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.cta.quiet{background:none;color:var(--muted);text-decoration:underline;padding:10px 0;font-weight:400;font-size:.95rem}
.price-row{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:20px}
.price{font-size:2.3rem;font-weight:680;letter-spacing:-.02em}
.note{color:var(--muted);font-size:.94rem}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;
  padding:20px 22px;margin-bottom:14px;box-shadow:0 1px 3px var(--shadow)}
.card h3{margin:0 0 6px;font-size:1.1rem;letter-spacing:-.01em}
.card .p{font-weight:640;color:var(--accent)}
.files a{display:block;padding:12px 0;border-bottom:1px solid var(--line);color:var(--ink)}
footer{border-top:1px solid var(--line);padding-top:24px;margin-top:30px;color:var(--muted);font-size:.88rem}
@media (max-width:480px){header{padding-block:44px 26px}.price{font-size:1.9rem}}
"""


def offer_page(
    ladder: Ladder,
    checkout_url: str,
    *,
    headline: str = "",
    problem: str = "",
    deliverables: list[str] | None = None,
    guarantee: str = "",
    bump_is_native: bool = True,
    faq: list[dict[str, str]] | None = None,
    sample_url: str = "",
    sample_label: str = "",
    price_note: str = "one payment, yours to keep",
    footer_note: str = "Tax is calculated at checkout and handled by our payment provider.",
    extra_html: str = "",
) -> str:
    """The page before the checkout.

    When the provider cannot do a native order bump, the bump is shown here
    instead — a worse moment to ask, and labelled as such in the provider
    plan, but better than losing the rung entirely.

    `sample_url` is the one addition that outranks every word of copy on the
    page: a link to a usable part of the product. For anything gated, the
    sample is the only element of an offer that is evidence rather than
    assertion, so it sits next to the buy button rather than below the fold.
    """
    e = html.escape
    core = ladder.core
    bump = ladder.rung(Rung.BUMP)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(ladder.product_name)}</title>
<meta name="description" content="{e(core.description or ladder.product_name)}">
<style>{_CSS}</style>
</head>
<body>
<main class="wrap">
  <header>
    <h1>{e(headline or core.description or ladder.product_name)}</h1>
    <p class="sub">For {e(ladder.audience)}.</p>
    <a class="cta" href="{e(checkout_url)}" data-checkout>Get it — {e(core.display())}</a>
    {_sample(sample_url, sample_label)}
  </header>

  {_problem(problem)}
  {_deliverables(deliverables)}
  {_bump_section(bump) if bump and not bump_is_native else ""}

  <section>
    <h2>Price</h2>
    <div class="price-row">
      <span class="price">{e(core.display())}</span>
      <span class="note">{e(price_note)}</span>
    </div>
    <a class="cta" href="{e(checkout_url)}" data-checkout>Get it — {e(core.display())}</a>
    {f'<p class="note">{e(guarantee)}</p>' if guarantee else ""}
  </section>

  {_faq(faq)}
  {extra_html}

  <footer>
    <p>{e(footer_note)}</p>
  </footer>
</main>
</body>
</html>
"""


def thank_you_page(
    ladder: Ladder,
    *,
    upsell_url: str | None = None,
    downsell_url: str | None = None,
    next_steps: list[str] | None = None,
    support_email: str | None = None,
    upsell_is_native: bool = True,
    headline: str = "That's paid. Check your email.",
    delivery_note: str = (
        "Your download link is on its way to the address you used at "
        "checkout. It doesn't expire — you can come back to it any time."
    ),
    extra_html: str = "",
) -> str:
    """What the buyer sees after paying.

    Delivery itself comes from the provider by email. This page tells them
    that, tells them what to do first, and carries the upsell when the
    provider has no native one.
    """
    e = html.escape
    upsell = ladder.rung(Rung.UPSELL)
    downsell = ladder.rung(Rung.DOWNSELL)
    show_upsell = upsell and upsell_url and not upsell_is_native

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thanks — {e(ladder.product_name)}</title>
<meta name="robots" content="noindex">
<style>{_CSS}</style>
</head>
<body>
<main class="wrap">
  <header>
    <h1>{e(headline)}</h1>
    <p class="sub">{e(delivery_note)}</p>
  </header>

  {extra_html}
  {_next_steps(next_steps)}
  {_upsell_section(upsell, upsell_url, downsell, downsell_url) if show_upsell else ""}

  <footer>
    <p>Nothing arrived within a few minutes? Check spam first{
      f", then email {e(support_email)}" if support_email else ""}.</p>
  </footer>
</main>
</body>
</html>
"""


def _sample(url: str, label: str) -> str:
    if not url:
        return ""
    text = label or "Or read part of it first, free"
    return f'<p><a class="cta quiet" href="{html.escape(url)}" data-sample>{html.escape(text)}</a></p>'


def _faq(items: list[dict[str, str]] | None) -> str:
    if not items:
        return ""
    rows = "".join(
        f"<div class=\"card\"><h3>{html.escape(str(item.get('q', '')))}</h3>"
        f"<p>{html.escape(str(item.get('a', '')))}</p></div>"
        for item in items
    )
    return f'<section><h2>Questions</h2>{rows}</section>'


def _problem(problem: str) -> str:
    if not problem:
        return ""
    return f'<section><h2>The problem</h2><p>{html.escape(problem)}</p></section>'


def _deliverables(items: list[str] | None) -> str:
    if not items:
        return ""
    rows = "".join(f"<li>{html.escape(item)}</li>" for item in items)
    return f'<section><h2>What you get</h2><ul>{rows}</ul></section>'


def _bump_section(bump: Offer) -> str:
    e = html.escape
    return f"""<section>
    <h2>Add on</h2>
    <div class="card">
      <h3>{e(bump.name)}</h3>
      <p>{e(bump.description)}</p>
      <p class="p">+{e(bump.display())}, added at checkout</p>
    </div>
  </section>"""


def _next_steps(items: list[str] | None) -> str:
    if not items:
        return ""
    rows = "".join(f"<li>{html.escape(item)}</li>" for item in items)
    return f'<section><h2>Start here</h2><ul>{rows}</ul></section>'


def _upsell_section(
    upsell: Offer | None, upsell_url: str | None, downsell: Offer | None, downsell_url: str | None
) -> str:
    if not upsell or not upsell_url:
        return ""
    e = html.escape
    alternative = ""
    if downsell and downsell_url:
        alternative = (
            f'<p><a class="cta quiet" href="{e(downsell_url)}" data-downsell>'
            f"Or just {e(downsell.name.lower())} — {e(downsell.display())}</a></p>"
        )
    return f"""<section>
    <h2>One thing before you go</h2>
    <div class="card">
      <h3>{e(upsell.name)}</h3>
      <p>{e(upsell.description)}</p>
      <p class="p">{e(upsell.display())}</p>
    </div>
    <a class="cta" href="{e(upsell_url)}" data-upsell>Add {e(upsell.name)}</a>
    {alternative}
  </section>"""
