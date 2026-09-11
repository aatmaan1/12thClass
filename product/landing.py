"""The landing page: the front door of the funnel.

Funnel-hacked rather than invented, in the order the sources agree on —
outcome-first headline, the problem in the buyer's words, the mechanism, the
deliverable, the evidence, then the price. Two departures from that template,
both deliberate:

**The evidence comes before the price and it is the product itself.** The
planner is free and needs no account, so the strongest thing this page can do
is get out of the way and send people to it. A sample is the only part of an
offer that is evidence rather than copy, and here the sample is a working tool
rather than a chapter to skim.

**The weightage chart is real.** It is the actual CBSE unit weightage for both
papers, drawn to scale from the same numbers the planner computes with. A
page about marks that drew an illustrative chart would be arguing against
itself.

No JavaScript: the page is complete in its first frame, which is what a shared
link and a search crawler both get.
"""

from __future__ import annotations

import html
from typing import Any

from tokens import FONTS, TOKENS

CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--body);
  font:400 16px/1.66 var(--sans);font-variant-numeric:tabular-nums}
:focus-visible{outline:2.5px solid var(--accent);outline-offset:3px;border-radius:3px}
.wrap{max-width:760px;margin:0 auto;padding:0 24px}
a{color:var(--accent-ink)}

/* the masthead: a question paper's own header block */
header.top{border-bottom:1px solid var(--line);background:var(--card)}
header.top .wrap{display:flex;align-items:baseline;gap:12px;padding-block:16px}
header.top b{font:700 19px/1 var(--serif);color:var(--ink)}
header.top span{font:400 10.5px/1 var(--mono);color:var(--faint);letter-spacing:.05em}
header.top a{margin-left:auto;font:500 13px/1 var(--sans);text-decoration:none}

.hero{padding-block:66px 10px}
h1{font:600 clamp(30px,5.2vw,46px)/1.1 var(--serif);color:var(--ink);
  letter-spacing:-.022em;margin:0;text-wrap:balance;max-width:22ch}
.sub{font:400 clamp(17px,2vw,19px)/1.58 var(--sans);color:var(--muted);
  margin:20px 0 0;max-width:58ch}
.cta-row{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-top:32px}
.cta{display:inline-block;background:var(--accent);color:var(--on-accent);
  padding:15px 24px;border-radius:9px;font:600 15px/1 var(--sans);text-decoration:none}
.cta:hover{filter:brightness(1.08)}
.cta.ghost{background:none;color:var(--accent-ink);border:1px solid var(--accent);
  padding:14px 23px}
.cta.ghost:hover{background:var(--accent-soft);filter:none}
.mini{font:400 12px/1.5 var(--mono);color:var(--faint);margin:14px 0 0}

section{padding-block:44px;border-top:1px solid var(--line)}
section:first-of-type{border-top:0}
h2{font:600 clamp(22px,3vw,27px)/1.22 var(--serif);color:var(--ink);
  letter-spacing:-.015em;margin:0 0 14px;text-wrap:balance}
.kicker{font:400 10.5px/1 var(--mono);letter-spacing:.15em;text-transform:uppercase;
  color:var(--accent-ink);margin:0 0 13px}
p{margin:0 0 15px;max-width:62ch}
p:last-child{margin-bottom:0}
.lead{font-size:17px;color:var(--body)}

/* the weightage chart: real CBSE unit marks, to scale */
.chart{margin-top:8px}
.ch-row{display:grid;grid-template-columns:minmax(120px,1.4fr) minmax(0,3fr) 46px;
  gap:14px;align-items:center;padding:7px 0}
.ch-row span{font:400 12.5px/1.35 var(--sans);color:var(--muted)}
.ch-bar{height:13px;border-radius:3px;background:var(--accent);opacity:.88}
.ch-row b{font:500 13px/1 var(--mono);color:var(--ink);text-align:right}
.ch-h{display:flex;align-items:baseline;justify-content:space-between;gap:12px;
  margin:26px 0 8px;padding-bottom:7px;border-bottom:1px solid var(--hair)}
.ch-h i{font:400 11px/1 var(--mono);font-style:normal;color:var(--faint);
  letter-spacing:.08em;text-transform:uppercase}
.ch-h em{font:500 13px/1 var(--mono);font-style:normal;color:var(--ink)}

/* the traps: three real marking-scheme lines from the notes */
.traps{display:flex;flex-direction:column;gap:12px;margin-top:6px}
.trap{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--mark);
  border-radius:0 10px 10px 0;padding:15px 18px}
.trap b{display:block;font:500 11px/1 var(--mono);letter-spacing:.08em;
  text-transform:uppercase;color:var(--mark);margin-bottom:8px}
.trap p{margin:0;font-size:14.5px}

ul.what{list-style:none;margin:0;padding:0}
ul.what li{position:relative;padding-left:27px;margin-bottom:12px;max-width:62ch}
ul.what li::before{content:"";position:absolute;left:7px;top:.66em;width:7px;height:7px;
  border-radius:50%;background:var(--accent)}

/* the ladder */
.rungs{display:flex;flex-direction:column;gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:11px;overflow:hidden;margin-top:6px}
.rung{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:16px;align-items:baseline;
  background:var(--card);padding:17px 19px}
.rung.core{background:var(--accent-soft)}
.rung b{font:600 15.5px/1.3 var(--sans);color:var(--ink)}
.rung p{margin:5px 0 0;font-size:13.5px;color:var(--muted);max-width:52ch}
.rung em{font:500 17px/1 var(--mono);font-style:normal;color:var(--ink);white-space:nowrap}
.rung i{display:block;font:400 10px/1 var(--mono);font-style:normal;color:var(--faint);
  letter-spacing:.1em;text-transform:uppercase;margin-top:6px;text-align:right}
.guarantee{margin-top:18px;font-size:14.5px;color:var(--muted)}

.faq{display:flex;flex-direction:column;gap:2px;margin-top:6px}
details{background:var(--card);border:1px solid var(--line);border-radius:10px;
  padding:14px 18px}
details+details{margin-top:9px}
summary{font:500 15px/1.4 var(--sans);color:var(--ink);cursor:pointer;list-style:none;
  display:flex;justify-content:space-between;gap:14px;align-items:center}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font:400 17px/1 var(--mono);color:var(--faint);flex:none}
details[open] summary::after{content:"\\2212"}
details p{margin:13px 0 0;font-size:14.5px}

footer{border-top:1px solid var(--line);padding-block:32px 60px;
  font:400 12.5px/1.68 var(--sans);color:var(--faint)}
footer p{max-width:68ch;margin:0 0 11px}
footer strong{color:var(--muted);font-weight:600}
footer a{color:var(--muted)}

@media (max-width:560px){
  .hero{padding-block:44px 6px}
  .wrap{padding:0 18px}
  .ch-row{grid-template-columns:minmax(96px,1.3fr) minmax(0,2fr) 38px;gap:10px}
  .rung{grid-template-columns:minmax(0,1fr)}
  .rung em{margin-top:10px}
  .rung i{text-align:left}
}
"""


def render_landing(
    *,
    product: Any,
    ladder: Any,
    copy: dict[str, Any],
    units: list[dict[str, Any]],
    traps: list[dict[str, str]],
    counts: dict[str, int],
    app_url: str = "/app",
) -> str:
    """The whole page, as one self-contained file."""
    e = html.escape
    core = ladder.core if ladder is not None else None

    headline = str(copy.get("headline") or product.tagline or product.name).strip()
    problem = str(copy.get("problem") or "").strip()
    guarantee = str(copy.get("guarantee") or "").strip()

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(product.name)} · CBSE Class 12 Maths &amp; Physics</title>
<meta name="description" content="{e(_meta(counts))}">
<meta name="theme-color" content="#F1F4F1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1211" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{_FAVICON}">
<link rel="apple-touch-icon" href="{_FAVICON}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(product.name)} · {e(headline)}">
<meta property="og:description" content="{e(_meta(counts))}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>{TOKENS}{CSS}</style>
</head>
<body>

<header class="top">
  <div class="wrap">
    <b>{e(product.name)}</b>
    <span>CBSE 2025-26 · 041 · 042</span>
    <a href="{e(app_url)}">Open the planner &rarr;</a>
  </div>
</header>

<main>
  <div class="wrap hero">
    <h1>{e(headline)}</h1>
    <p class="sub">{e(_hero_sub(counts))}</p>
    <div class="cta-row">
      <a class="cta" href="{e(app_url)}">Work out my marks — free</a>
      <a class="cta ghost" href="#inside">See what is inside</a>
    </div>
    <p class="mini">No account. Nothing to install. Saved on your device, sent nowhere.</p>
  </div>

  <div class="wrap">
    <section>
      <p class="kicker">The problem</p>
      <h2>Everyone tells you to work hard. Nobody tells you where the marks are.</h2>
      <p class="lead">{e(problem)}</p>
    </section>

    <section>
      <p class="kicker">What it does</p>
      <h2>It starts from the marks, not the syllabus</h2>
      <p>CBSE publishes marks per unit. {counts['chapters']} chapters carry
      {counts['total_marks']} of them between two papers, and they do not carry
      them evenly &mdash; Calculus alone is 35 marks of the Maths paper, and
      Linear Programming is 5.</p>
      <p>So the planner asks you one thing per chapter &mdash; how solid are you,
      0 to 3 &mdash; and works out the rest: how many marks you already have in
      hand, how many are still at risk, and which chapters hold the ones you are
      short of. Then it puts them in order and spreads them over the days you
      have left.</p>
      <div class="chart">{_chart(units)}</div>
      <p class="mini">Unit weightage as published by CBSE for 2025-26. A
      chapter's share is its unit's marks split between the chapters in that
      unit &mdash; an even split, because the board does not publish a finer one.</p>
    </section>

    <section>
      <p class="kicker">Why it is different</p>
      <h2>Marks are awarded for steps, and the steps are written down</h2>
      <p>A marking scheme does not pay for the right answer. It pays for named
      steps &mdash; the substitution line, the unit, the vector arrow, the
      statement of the theorem you used. Almost every mark lost in these two
      papers is lost by a candidate who knew the material and skipped a step.</p>
      <p>Every chapter here opens with what the examiner pays for, taken from
      the marking schemes rather than from a textbook. Three of them, verbatim:</p>
      <div class="traps">{_traps(traps)}</div>
    </section>

    <section id="inside">
      <p class="kicker">What you get</p>
      <h2>{counts['questions']} board questions, and the plan that tells you which to do first</h2>
      <ul class="what">{_deliverables(copy.get('deliverables') or [])}</ul>
    </section>

    <section>
      <p class="kicker">Free, and not a trial</p>
      <h2>The diagnosis is free. Always.</h2>
      <p>The planner, the syllabus scope for all {counts['chapters']} chapters,
      the deleted-topics warning on every one of them and the plain-English
      opening to each cost nothing and need no account. Neither does the exam
      blueprint, or {counts['free_chapters']} chapters end to end.</p>
      <p>That is not a teaser. Knowing which chapters hold your missing marks is
      genuinely useful on its own, and the deleted-topics list is the single
      most valuable line in the whole guide &mdash; charging for
      &ldquo;this is no longer in your syllabus&rdquo; would be the wrong side of
      a line worth having.</p>
      <div class="cta-row">
        <a class="cta" href="{e(app_url)}">Open the free planner</a>
      </div>
    </section>

    <section>
      <p class="kicker">Price</p>
      <h2>One payment. It still works after the exam.</h2>
      <div class="rungs">{_rungs(ladder)}</div>
      <p class="guarantee">{e(guarantee)}</p>
    </section>

    <section>
      <p class="kicker">Questions</p>
      <h2>Before you buy</h2>
      <div class="faq">{_faq(copy.get('faq') or [])}</div>
    </section>
  </div>
</main>

<footer>
  <div class="wrap">
    <p><strong>Not affiliated with CBSE.</strong> This is an independent study
    guide written against the published CBSE curriculum documents and the
    2025-26 sample papers. Download the syllabus and sample paper for each
    subject from
    <a href="https://cbseacademic.nic.in/" target="_blank" rel="noopener">cbseacademic.nic.in</a>
    and re-check the deleted-topics list at the start of your session. Notes go
    stale; the board circular does not.</p>
    <p>The frequency bands (&ldquo;every year&rdquo;, &ldquo;8&ndash;9/10&rdquo;)
    are well-informed pattern estimates, not a machine count of past papers.
    Two scope points are flagged rather than asserted: polarisation in Wave
    Optics, and the magnetic-materials block in Physics chapter 5.</p>
    <p>{e(product.support_email or "")} &middot;
    <a href="{e(app_url)}">Open the planner</a></p>
  </div>
</footer>
</body>
</html>
"""


_FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'"
    "%3E%3Ctext y='.92em' font-size='88'%3E%F0%9F%93%90%3C/text%3E%3C/svg%3E"
)


def _meta(counts: dict[str, int]) -> str:
    return (
        f"Work out how many marks you are missing in CBSE Class 12 Maths and "
        f"Physics, which of the {counts['chapters']} chapters hold them, and what "
        f"to do in the days you have left. {counts['questions']} board questions "
        f"with full solutions. The planner is free."
    )


def _hero_sub(counts: dict[str, int]) -> str:
    return (
        f"Grade each chapter 0 to 3. This works out how many of the "
        f"{counts['total_marks']} marks you already have, which chapters hold the "
        f"ones you are short of, and what to study in the days you have left — "
        f"then gives you the {counts['questions']} board questions to do it with."
    )


def _chart(units: list[dict[str, Any]]) -> str:
    """Unit weightage, to scale, with every bar labelled by its real marks."""
    if not units:
        return ""
    widest = max(u["marks"] for u in units) or 1
    out, subject = [], None
    for unit in units:
        if unit["subject"] != subject:
            subject = unit["subject"]
            out.append(
                f'<div class="ch-h"><i>{html.escape(unit["subject_label"])} '
                f'&middot; {html.escape(unit["code"])}</i>'
                f'<em>{unit["subject_total"]} marks</em></div>'
            )
        width = 100 * unit["marks"] / widest
        out.append(
            f'<div class="ch-row"><span>{html.escape(unit["label"])}</span>'
            f'<span class="ch-bar" style="width:{width:.1f}%" role="img" '
            f'aria-label="{unit["marks"]} marks"></span>'
            f'<b>{unit["marks"]}</b></div>'
        )
    return "".join(out)


def _traps(traps: list[dict[str, str]]) -> str:
    return "".join(
        f'<div class="trap"><b>{html.escape(t["where"])}</b>'
        f"<p>{html.escape(t['text'])}</p></div>"
        for t in traps
    )


def _deliverables(items: list[Any]) -> str:
    return "".join(f"<li>{html.escape(str(item).strip())}</li>" for item in items)


def _rungs(ladder: Any) -> str:
    if ladder is None:
        return ""
    labels = {"core": "the product", "bump": "added at checkout",
              "upsell": "offered after", "downsell": "offered after"}
    out = []
    for offer in ladder.ordered:
        rung = offer.rung.value
        out.append(
            f'<div class="rung{" core" if rung == "core" else ""}">'
            f'<div><b>{html.escape(offer.name)}</b>'
            f"<p>{html.escape(offer.description.strip())}</p></div>"
            f'<div><em>{html.escape(offer.display())}</em>'
            f'<i>{html.escape(labels.get(rung, rung))}</i></div></div>'
        )
    return "".join(out)


def _faq(items: list[dict[str, str]]) -> str:
    return "".join(
        f"<details><summary>{html.escape(str(item.get('q', '')).strip())}</summary>"
        f"<p>{html.escape(str(item.get('a', '')).strip())}</p></details>"
        for item in items
    )
