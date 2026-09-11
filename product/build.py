#!/usr/bin/env python3
"""Build the deployable site into the repository root.

    python3 product/build.py

    index.html    the landing page — the front door of the funnel
    app.html      the planner and the guide, with only the free half inside it
    thanks.html   what a buyer lands on, which hands over their key
    api/          unlock / claim / webhook, and the paid half they serve

Everything it writes is generated and committed, because the host builds
nothing: Vercel serves this repository root as a static site with the Python
functions under `api/` picked up automatically. Re-run it after editing a
chapter, the app, the ladder or the copy, and commit what changes.

Two properties are worth stating, because they are what make this a product
rather than a demo:

* **Nothing paid reaches index.html or app.html.** The paid half is written
  under `api/_data/`, which a static host does not serve, and the build is
  refused outright if any of it turns up in either page.
* **It builds before there is a payment provider.** With no store configured,
  every buy button points at the offer page and the build says so.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import landing as landing_mod             # noqa: E402
from paywall import packs as packs_mod         # noqa: E402
from paywall import render as render_mod       # noqa: E402
from paywall.build import paywall_config, runtime_manifest   # noqa: E402
from paywall.deploy import write_deployable    # noqa: E402
from paywall.manifest import load_bundle, load_product       # noqa: E402
from paywall.split import split_bundle         # noqa: E402
from storefront.config import load_copy, load_ladder         # noqa: E402
from storefront.models import Rung             # noqa: E402
from storefront.pages import thank_you_page    # noqa: E402
from tokens import TOKENS                      # noqa: E402

#: The app is written as parts and assembled here, so each one stays a file a
#: person can read. It still ships as one self-contained page.
APP_PARTS = ["i18n", "model", "planner", "chapter", "paywall", "shell"]

#: Three real marking-scheme lines for the landing page, named by where they
#: come from: (chapter id, which numbered tip). Quoted verbatim — a page that
#: argued "marks are awarded for steps" with an invented example would be
#: arguing against itself. If one cannot be found the build says so and drops
#: it rather than substituting anything.
TRAPS = [("m7", 1), ("p6", 1), ("m10", 1)]


def app_template() -> str:
    """The app source, assembled from its parts."""
    shell = io.open(os.path.join(HERE, "app", "app.src.html"), encoding="utf-8").read()
    shell = shell.replace("/*__TOKENS__*/", TOKENS.strip())
    for part in APP_PARTS:
        path = os.path.join(HERE, "app", "js", part + ".js")
        marker = "/*__" + {"i18n": "I18N", "model": "MODEL", "planner": "PLANNER",
                           "chapter": "CHAPTER", "paywall": "PAYWALL_JS",
                           "shell": "SHELL"}[part] + "__*/"
        if marker not in shell:
            raise SystemExit(f"app.src.html has no {marker} placeholder")
        shell = shell.replace(marker, io.open(path, encoding="utf-8").read())
    left = re.findall(r"/\*__[A-Z_]+__\*/", shell)
    stray = [m for m in left if m not in ("/*__DATA__*/", "/*__PAYWALL__*/")]
    if stray:
        raise SystemExit(f"unfilled placeholders in the app: {stray}")
    return shell


def unit_rows(bundle: dict) -> list[dict]:
    """CBSE unit weightage, in paper order, for the landing page's chart."""
    labels = {"maths": ("Mathematics", "041", 80), "physics": ("Physics", "042", 70)}
    rows, seen = [], set()
    for chapter in bundle["chapters"]:
        key = (chapter["subj"], chapter["unit"])
        if key in seen:
            continue
        seen.add(key)
        label, code, total = labels[chapter["subj"]]
        rows.append({
            "subject": chapter["subj"], "subject_label": label,
            "code": code, "subject_total": total,
            # "Unit III · Calculus" reads better here without the numbering,
            # which the marks column makes redundant
            "label": chapter["unit"].split("·")[-1].strip(),
            "marks": chapter["unitMarks"],
        })
    return rows


def marking_traps(bundle: dict) -> tuple[list[dict], list[str]]:
    """Pull the named tips out of the notes, verbatim."""
    by_id = {c["id"]: c for c in bundle["chapters"]}
    out, notes = [], []
    for chapter_id, which in TRAPS:
        chapter = by_id.get(chapter_id)
        tips = (chapter or {}).get("s", {}).get("tips", "")
        if not tips:
            notes.append(f"no tips for {chapter_id}, so that landing-page trap is omitted")
            continue
        found = re.search(
            r"^%d\.\s+((?:.|\n(?!\s*\n|\s*\d+\.))+)" % which, tips, re.M
        )
        if not found:
            notes.append(f"tip {which} not found in {chapter_id}; omitted")
            continue
        text = re.sub(r"\s+", " ", found.group(1)).strip()
        text = text.replace("**", "").replace("*", "")
        subject = "Mathematics" if chapter["subj"] == "maths" else "Physics"
        out.append({"where": f"{subject} · {chapter['title']}", "text": text})
    return out, notes


def main() -> None:
    product = load_product(HERE)
    bundle = load_bundle(HERE, product)
    split = split_bundle(bundle, product)
    ladder = load_ladder(os.path.join(HERE, product.ladder))
    copy = load_copy(os.path.join(HERE, product.funnel))

    store = str((copy.get("store") or {}).get("name", ""))
    product_ids = dict((copy.get("store") or {}).get("product_ids") or {})
    site_url = str(copy.get("site_url", ""))
    warnings = list(split.warnings)

    # the pack the order bump sells
    for name in product.packs:
        if name != "packs.revision":
            raise SystemExit(f"the build cannot make pack {name!r}")
        split.paid.setdefault(name, {})["pack"] = packs_mod.revision_pack(bundle)

    # checkout links, or honest placeholders
    checkout, nonce_param = {}, ""
    if store and product_ids:
        from storefront.providers import get_provider
        provider = get_provider("lemonsqueezy", store, product_ids=product_ids)
        nonce_param = provider.custom_param("nonce")
        for offer in ladder.offers:
            try:
                checkout[offer.slug] = provider.checkout_url(
                    offer, custom={"offers": offer.slug, "ladder": ladder.slug}
                )
            except KeyError as exc:
                warnings.append(str(exc).strip('"'))
    else:
        warnings.append(
            "no store or product ids configured, so every buy button points at "
            "the landing page instead of a checkout. Create the products in the "
            "provider's dashboard, then fill in store.product_ids in copy.yaml."
        )

    questions = packs_mod.questions(bundle)
    counts = {
        "chapters": len(bundle["chapters"]),
        "questions": len(questions),
        "docs": len(bundle["docs"]),
        "total_marks": 150,
        "free_chapters": len(product.rule("chapters").samples),
    }

    # ---- the app -------------------------------------------------------
    config = paywall_config(
        product, ladder, bundle, checkout,
        site_url=site_url, nonce_param=nonce_param,
        note=os.environ.get("PAYWALL_NOTE", ""),
    )
    config["offerUrl"] = "/"
    app = render_mod.render_app(
        app_template(), split.free, config,
        title=f"{product.name} · CBSE Class 12 Maths & Physics",
        tagline=landing_mod._meta(counts),
    )
    problems = render_mod.check_render(app)
    if problems:
        raise SystemExit("the rendered app is broken: " + "; ".join(problems))

    # ---- the landing page ----------------------------------------------
    traps, trap_notes = marking_traps(bundle)
    warnings.extend(trap_notes)
    page = landing_mod.render_landing(
        product=product, ladder=ladder, copy=copy,
        units=unit_rows(bundle), traps=traps, counts=counts, app_url="/app",
    )

    # ---- the gate holds, or nothing ships ------------------------------
    report = render_mod.leak_check(app + "\n" + page, split.paid, split.free)
    if report.leaks:
        raise SystemExit(
            "paid content is present in a public page — the build is refused.\n  "
            + "\n  ".join(report.leaks[:12])
        )
    if report.shared:
        warnings.append(
            f"{len(report.shared)} paid passage(s) also appear in the free half, so "
            f"they are public legitimately: {', '.join(report.shared[:4])}"
        )

    # ---- the page after payment ----------------------------------------
    upsell, downsell = ladder.rung(Rung.UPSELL), ladder.rung(Rung.DOWNSELL)
    thanks = thank_you_page(
        ladder,
        upsell_url=checkout.get(upsell.slug) if upsell else None,
        downsell_url=checkout.get(downsell.slug) if downsell else None,
        next_steps=copy.get("next_steps"),
        support_email=product.support_email,
        upsell_is_native=True,
        headline="That's paid. Your guide is unlocking now.",
        delivery_note=(
            "Nothing to download and no account to create: the key below opens "
            "the guide in this browser and it keeps working offline afterwards. "
            "It is also in your receipt, so it is not lost if this page is."
        ),
        extra_html=_claim_widget(),
    )

    # ---- write -----------------------------------------------------------
    written = []
    for name, text in (("index.html", page), ("app.html", app), ("thanks.html", thanks)):
        path = os.path.join(ROOT, name)
        io.open(path, "w", encoding="utf-8").write(text)
        written.append(name)

    data = os.path.join(ROOT, "api", "_data")
    os.makedirs(data, exist_ok=True)
    io.open(os.path.join(data, "paid.json"), "w", encoding="utf-8").write(
        json.dumps(split.paid, ensure_ascii=False, separators=(",", ":")))
    io.open(os.path.join(data, "product.json"), "w", encoding="utf-8").write(
        json.dumps(runtime_manifest(product), indent=2))
    written += ["api/_data/paid.json", "api/_data/product.json"]

    from pathlib import Path
    for path in write_deployable(
        Path(ROOT), Path(HERE), product_path="product",
        config=False, readme=False,     # both already belong to the repository
    ):
        written.append(os.path.relpath(str(path), ROOT))

    io.open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8").write(
        json.dumps(VERCEL, indent=2) + "\n")
    written.append("vercel.json")

    # ---- say what happened ----------------------------------------------
    print(f"\n{product.name} — built into the repository root\n")
    header = f"{'collection':<12} {'items':>6} {'free':>6} {'gated':>6} {'public KB':>10} {'sold KB':>9}"
    print(header)
    print("-" * len(header))
    for collection in split.collections:
        print(f"{collection.collection:<12} {collection.items:>6} {collection.samples:>6}"
              f" {collection.gated:>6} {collection.free_bytes / 1024:>10.0f}"
              f" {collection.paid_bytes / 1024:>9.0f}")
    print(
        f"\nlanding      {len(page.encode('utf-8')) / 1024:.0f} KB"
        f"\napp          {len(app.encode('utf-8')) / 1048576:.2f} MB"
        f"\nsold bundle  {split.paid_bytes / 1048576:.2f} MB"
        f"\nfree share   {split.free_share:.1%} of the product, by bytes"
        f"\nleak check   {report.checked_snippets} paid passages searched for in both "
        f"public pages, {len(report.leaks)} found"
        f"\ncontent      {counts['chapters']} chapters · {counts['questions']} questions"
        f" · {counts['docs']} documents · {counts['free_chapters']} chapters free"
    )
    for name in written:
        print(f"  wrote {name}")
    if checkout:
        print("\ncheckout links:")
        for slug, url in checkout.items():
            print(f"  {slug:<10} {url}")
    hosts = render_mod.stray_hosts(app + page)
    if hosts:
        print(f"\nnote  external hosts referenced: {', '.join(hosts)}")
    for warning in warnings:
        print(f"\nwarn  {warning}")


def _claim_widget() -> str:
    """The bit of the thank-you page that hands the buyer their key.

    The nonce was generated by the browser before it left for the checkout and
    comes back through the provider's custom data, so the key goes to the
    browser that made the purchase rather than to anyone who guesses an order
    number.
    """
    return """<section>
    <h2>Your key</h2>
    <div class="card">
      <p id="claim-state">Looking up your purchase…</p>
      <p><code id="claim-key" style="font-size:1.05rem;word-break:break-all"></code></p>
    </div>
    <p><a class="cta" id="claim-open" href="/app">Open the guide</a></p>
    <p class="note">A payment can take a few seconds to reach us. If the key has not
      appeared, reload this page — nothing is lost, and it is in your receipt too.</p>
  </section>
  <script>
  (function(){
    var nonce = "";
    try { nonce = localStorage.getItem("mf.nonce") || ""; } catch(e){}
    var state = document.getElementById("claim-state");
    var out = document.getElementById("claim-key");
    var open = document.getElementById("claim-open");
    var fallback = "Your key is in the receipt email. Paste it into the guide under Access.";
    if (!nonce){ state.textContent = fallback; return; }
    open.href = "/app?claim=" + encodeURIComponent(nonce);
    fetch("/api/claim", {
      method: "POST", headers: {"Content-Type": "application/json"},
      body: JSON.stringify({nonce: nonce, peek: true})
    }).then(function(r){ return r.json(); }).then(function(j){
      if (j && j.key){
        state.textContent = "Here it is. Opening the guide will apply it automatically.";
        out.textContent = j.key;
      } else { state.textContent = fallback; }
    }).catch(function(){ state.textContent = fallback; });
  })();
  </script>"""


VERCEL = {
    "$schema": "https://openapi.vercel.sh/vercel.json",
    # Clean URLs, and no rewrites. An earlier version of this site served the
    # page through a vercel.json rewrite and 404'd on the live deployment,
    # because cleanUrls strips the .html from a rewrite *destination*. Plain
    # files plus cleanUrls has no such interaction: /app serves app.html.
    "cleanUrls": True,
    "trailingSlash": False,
    "headers": [
        {
            "source": "/(.*)",
            "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
            ],
        }
    ],
}


if __name__ == "__main__":
    main()
