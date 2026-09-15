"""The whole build: content in, deployable funnel out.

    content/*.md ──► extract ──► split ──┬─► free bundle ──► public/index.html
                                         │
                                         ├─► packs ────────► api/_data/paid.json
                                         └─► paid bundle ──┘

    ladders/*.yaml + funnel/*.yaml ─────────► public/get.html, public/thanks.html

Two properties are worth stating because they are what make this deployable
rather than a demo:

* **Nothing paid reaches `public/`.** The paid bundle is written under `api/`,
  which a static host does not serve, and `render.leak_check` refuses the
  build if any of it turns up in the page anyway.
* **It builds before there is a payment provider.** With no store or product
  ids configured, the checkout links become the offer page and the build says
  so. A funnel you cannot look at until you have finished the paperwork is a
  funnel nobody reviews.
"""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from storefront.config import load_copy, load_ladder
from storefront.models import Ladder, Rung
from storefront.pages import offer_page, thank_you_page
from storefront.providers import RECOMMENDED, get_provider

from . import packs as packs_mod
from . import render as render_mod
from .deploy import write_deployable
from .manifest import load_bundle, load_product, product_dir
from .models import Product
from .split import Split, split_bundle


@dataclass
class BuildResult:
    product: Product
    split: Split
    deploy: Path
    written: list[Path] = field(default_factory=list)
    render: render_mod.RenderReport = field(default_factory=render_mod.RenderReport)
    feasibility: list[packs_mod.SubjectFeasibility] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checkout: dict[str, str] = field(default_factory=dict)


def build(
    path: str | Path,
    *,
    provider: str = RECOMMENDED,
    store: str = "",
    product_ids: dict[str, str] | None = None,
    site_url: str = "",
    note: str = "",
    clean: bool = False,
) -> BuildResult:
    """Build the product at `path` into its deploy directory."""
    directory = product_dir(path)
    product = load_product(path)
    bundle = load_bundle(path, product)
    split = split_bundle(bundle, product)

    ladder = _ladder(directory, product)
    copy = load_copy(_resolve(directory, product.funnel)) if product.funnel else {}
    store = store or str((copy.get("store") or {}).get("name", ""))
    product_ids = product_ids or dict((copy.get("store") or {}).get("product_ids") or {})
    site_url = site_url or product.site_url or str(copy.get("site_url", ""))

    result = BuildResult(product=product, split=split, deploy=directory / product.deploy)
    result.warnings.extend(split.warnings)

    _add_packs(bundle, product, split, result)
    checkout = _checkout_urls(ladder, provider, store, product_ids, result)
    result.checkout = checkout
    nonce_param = get_provider(provider, store or "example").custom_param("nonce")
    if not nonce_param:
        result.warnings.append(
            f"{provider} cannot carry our data through its checkout, so a buyer "
            "cannot be handed their key on the thank-you page — it has to reach "
            "them by email instead."
        )

    public = result.deploy / "public"
    data = result.deploy / "api" / "_data"
    if clean:
        shutil.rmtree(public, ignore_errors=True)
        shutil.rmtree(data, ignore_errors=True)
    public.mkdir(parents=True, exist_ok=True)
    data.mkdir(parents=True, exist_ok=True)

    # 1. the app, with the free half compiled in
    template = (directory / product.app).read_text(encoding="utf-8")
    config = paywall_config(
        product, ladder, bundle, checkout, site_url=site_url,
        nonce_param=nonce_param, note=note,
    )
    page = render_mod.render_app(
        template, split.free, config,
        title=f"{product.name} · {_subtitle(product)}",
        tagline=product.tagline or product.name,
        icon=str(config.get("icon") or "\U0001f4d0"),
    )
    problems = render_mod.check_render(page)
    if problems:
        raise RuntimeError("the rendered app is broken: " + "; ".join(problems))

    result.render = render_mod.leak_check(page, split.paid, split.free)
    result.render.stray_hosts = render_mod.stray_hosts(page)
    if result.render.shared:
        result.warnings.append(
            f"{len(result.render.shared)} paid passage(s) also appear in the free "
            "half, so they are in the public page legitimately: "
            f"{', '.join(result.render.shared[:5])}. Shared boilerplate is fine; "
            "shared substance means the gate is not dividing what you think."
        )
    if result.render.leaks:
        raise render_mod.LeakError(
            "paid content is present in the public page — the build is refused.\n  "
            + "\n  ".join(result.render.leaks[:12])
        )
    _write(public / "index.html", page, result)
    result.render.path = str(public / "index.html")
    result.render.bytes = len(page.encode("utf-8"))

    # 2. the paid half, where only a function can read it
    _write(
        data / "paid.json",
        json.dumps(split.paid, ensure_ascii=False, separators=(",", ":")),
        result,
    )
    # 3. what the endpoints need to know about the product, without PyYAML
    _write(data / "product.json", json.dumps(runtime_manifest(product), indent=2), result)

    # 4. the funnel pages
    if ladder is not None:
        _write(
            public / "get.html",
            _offer(ladder, copy, checkout, provider, site_url, nonce_param),
            result,
        )
        _write(
            public / "thanks.html",
            _thanks(ladder, copy, checkout, provider, product, site_url),
            result,
        )

    # 5. the handlers, the modules they import, and the host config
    for path in write_deployable(
        result.deploy, Path(__file__).resolve().parent.parent,
        product_path=_relative(directory),
    ):
        result.written.append(path)

    result.feasibility = packs_mod.paper_feasibility(bundle)
    return result


def paywall_config(
    product: Product,
    ladder: Ladder | None,
    bundle: dict[str, Any],
    checkout: dict[str, str],
    *,
    site_url: str = "",
    nonce_param: str = "",
    note: str = "",
) -> dict[str, Any]:
    """What the page needs to know about its own paywall.

    Prices and offer names are in here, which means they are public. That is
    correct: a padlock that will not say what it costs is worse than no
    padlock. Nothing here is a secret — the secret is the licence signing key,
    and it never leaves the server.
    """
    questions = packs_mod.questions(bundle)
    by_subject: dict[str, int] = {}
    for question in questions:
        by_subject[question.subject] = by_subject.get(question.subject, 0) + 1

    prices, names = {}, {}
    if ladder is not None:
        for offer in ladder.offers:
            prices[offer.slug] = offer.display()
            names[offer.slug] = offer.name

    return {
        "product": product.slug,
        "name": product.name,
        "icon": "\U0001f4d0",
        "unlockUrl": _api(site_url, "unlock"),
        "claimUrl": _api(site_url, "claim"),
        "offerUrl": f"{site_url.rstrip('/')}/get" if site_url else "/get",
        "checkout": checkout,
        "nonceParam": nonce_param,
        "prices": prices,
        "offerNames": names,
        "support": product.support_email,
        "note": note,
        "sampleNote": product.sample_note,
        "counts": {
            "questions": len(questions),
            "bySubject": by_subject,
            "chapters": len(bundle.get("chapters") or []),
            "docs": len(bundle.get("docs") or []),
        },
    }


def runtime_manifest(product: Product) -> dict[str, Any]:
    """The slice of the manifest the endpoints need, as plain JSON.

    Written out rather than read from `product.yaml` at request time so the
    functions need no YAML parser, and so a manifest edit that has not been
    rebuilt cannot silently change what a live key unlocks.
    """
    return {
        "slug": product.slug,
        "name": product.name,
        "audience": product.audience,
        "support_email": product.support_email,
        "entitlements": [
            {
                "offer": e.offer, "code": e.code, "name": e.name,
                "grants": list(e.grants), "seats": e.seats, "requires": list(e.requires),
            }
            for e in product.entitlements
        ],
    }


# ----------------------------------------------------------------- pieces


def _add_packs(
    bundle: dict[str, Any], product: Product, split: Split, result: BuildResult
) -> None:
    builders = {"packs.revision": packs_mod.revision_pack}
    for name in product.packs:
        builder = builders.get(name)
        if builder is None:
            raise RuntimeError(f"product asks for pack {name!r}, which the build cannot make")
        payload = builder(bundle)
        if not payload.get("sheets"):
            result.warnings.append(f"pack {name!r} came out empty and is not worth selling")
        split.paid.setdefault(name, {})["pack"] = payload


def _ladder(directory: Path, product: Product) -> Ladder | None:
    if not product.ladder:
        return None
    return load_ladder(_resolve(directory, product.ladder))


def _checkout_urls(
    ladder: Ladder | None,
    provider_name: str,
    store: str,
    product_ids: dict[str, str],
    result: BuildResult,
) -> dict[str, str]:
    """A checkout link per rung, or nothing at all — never a broken link."""
    if ladder is None:
        return {}
    if not store or not product_ids:
        result.warnings.append(
            "no store or product ids configured, so every buy button points at "
            "the offer page instead of a checkout. Create the products in the "
            "provider's dashboard, then put their ids under store.product_ids "
            "in the funnel file."
        )
        return {}

    provider = get_provider(provider_name, store, product_ids=product_ids)
    urls: dict[str, str] = {}
    for offer in ladder.offers:
        try:
            urls[offer.slug] = provider.checkout_url(
                offer, custom={"offers": offer.slug, "ladder": ladder.slug}
            )
        except KeyError as exc:
            result.warnings.append(str(exc).strip('"'))
    return urls


def _offer(
    ladder: Ladder, copy: dict[str, Any], checkout: dict[str, str],
    provider_name: str, site_url: str, nonce_param: str = "",
) -> str:
    caps = get_provider(provider_name, "example").capabilities
    fallback = f"{site_url.rstrip('/')}/" if site_url else "/"
    return offer_page(
        ladder,
        checkout.get("core") or fallback,
        bump_is_native=caps.native_order_bump,
        headline=str(copy.get("headline", "")),
        problem=str(copy.get("problem", "")),
        deliverables=copy.get("deliverables"),
        guarantee=str(copy.get("guarantee", "")),
        faq=copy.get("faq"),
        sample_url=str(copy.get("sample_url", "")),
        sample_label=str(copy.get("sample_label", "")),
        **({"price_note": copy["price_note"]} if copy.get("price_note") else {}),
        extra_html=_nonce_script(nonce_param),
    )


def _thanks(
    ladder: Ladder, copy: dict[str, Any], checkout: dict[str, str],
    provider_name: str, product: Product, site_url: str,
) -> str:
    caps = get_provider(provider_name, "example").capabilities
    upsell, downsell = ladder.rung(Rung.UPSELL), ladder.rung(Rung.DOWNSELL)
    return thank_you_page(
        ladder,
        upsell_url=checkout.get(upsell.slug) if upsell else None,
        downsell_url=checkout.get(downsell.slug) if downsell else None,
        next_steps=copy.get("next_steps"),
        support_email=product.support_email or str(copy.get("support_email", "")),
        upsell_is_native=caps.one_click_upsell,
        headline="That's paid. Your guide is unlocking now.",
        delivery_note=(
            "Nothing to download and no account to create: the key below opens "
            "the guide in this browser and it keeps working offline afterwards. "
            "It is also in your receipt, so it is not lost if this page is."
        ),
        extra_html=_claim_widget(site_url),
    )


def _nonce_script(param: str) -> str:
    """Tag every checkout link with a one-time value this browser generated.

    It is stored locally and travels out through the provider's custom data,
    so when the webhook records the sale the thank-you page can prove it was
    the browser that bought it. Without a provider that carries custom data
    there is nothing to add, and the key has to arrive by email.
    """
    if not param:
        return ""
    return f"""<script>
  (function(){{
    var key = "mf.nonce", nonce = "";
    try {{
      nonce = localStorage.getItem(key) || "";
      if (!nonce){{
        nonce = "n" + Math.random().toString(36).slice(2, 12) +
                Math.random().toString(36).slice(2, 12);
        localStorage.setItem(key, nonce);
      }}
    }} catch(e){{ return; }}   // no storage: fall back to the receipt email
    document.querySelectorAll("[data-checkout],[data-upsell],[data-downsell]")
      .forEach(function(a){{
        try {{
          var url = new URL(a.href, location.href);
          url.searchParams.set({param!r}, nonce);
          a.href = url.toString();
        }} catch(e){{}}
      }});
  }})();
  </script>"""


def _claim_widget(site_url: str) -> str:
    """The bit of the thank-you page that hands the buyer their key.

    The nonce is generated by the browser *before* it leaves for the checkout
    and comes back through the provider's custom data, so the key is handed to
    the browser that made the purchase rather than to anyone who guesses an
    order number. Order ids are short and sequential at most providers, which
    makes them a poor thing to hand out products against.
    """
    base = site_url.rstrip("/") if site_url else ""
    return f"""<section>
    <h2>Your key</h2>
    <div class="card">
      <p id="claim-state">Looking up your purchase…</p>
      <p><code id="claim-key" style="font-size:1.05rem;word-break:break-all"></code></p>
    </div>
    <p><a class="cta" id="claim-open" href="{base}/">Open the guide</a></p>
    <p class="note" id="claim-note">A payment can take a few seconds to reach us. If the
      key has not appeared, reload this page — nothing is lost, and it is in your
      receipt too.</p>
  </section>
  <script>
  (function(){{
    var nonce = "";
    try {{ nonce = localStorage.getItem("mf.nonce") || ""; }} catch(e){{}}
    var state = document.getElementById("claim-state");
    var out = document.getElementById("claim-key");
    var open = document.getElementById("claim-open");
    if (!nonce){{
      state.textContent = "Your key is in the receipt email. Paste it into the guide " +
        "under Access.";
      return;
    }}
    open.href = "{base}/?claim=" + encodeURIComponent(nonce);
    fetch("{base}/api/claim", {{
      method: "POST", headers: {{"Content-Type": "application/json"}},
      body: JSON.stringify({{nonce: nonce, peek: true}})
    }}).then(function(r){{ return r.json(); }}).then(function(j){{
      if (j && j.key){{
        state.textContent = "Here it is. Opening the guide will apply it automatically.";
        out.textContent = j.key;
      }} else {{
        state.textContent = "Your key is in the receipt email. Paste it into the guide " +
          "under Access.";
      }}
    }}).catch(function(){{
      state.textContent = "Your key is in the receipt email. Paste it into the guide " +
        "under Access.";
    }});
  }})();
  </script>"""


def _api(site_url: str, name: str) -> str:
    base = site_url.rstrip("/") if site_url else ""
    return f"{base}/api/{name}"


def _subtitle(product: Product) -> str:
    return product.audience.split(" sitting ")[0] if product.audience else product.slug


def _relative(directory: Path) -> Path | str:
    """The product directory as written in a command, where that is possible."""
    try:
        return directory.resolve().relative_to(Path.cwd()).as_posix()
    except ValueError:
        return directory.as_posix()


def _resolve(directory: Path, reference: str) -> Path:
    path = Path(reference)
    return path if path.is_absolute() else (directory / path).resolve()


def _write(path: Path, text: str, result: BuildResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    result.written.append(path)
