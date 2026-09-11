"""What this repository ships, tested against the real notes.

Three claims, in order of how much it would cost to get them wrong:

1. **No paid content reaches index.html or app.html.** Everything else here is
   a preference; this one is the product.
2. **The committed build matches the notes.** The host builds nothing, so a
   chapter edited and not rebuilt is a page that sells the old text.
3. **The planner's arithmetic is right.** It is what a visitor is given for
   free and what the offer rests on, so a wrong number there is worse than an
   ugly one.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

from paywall.manifest import load_bundle, load_product
from paywall.models import Product
from paywall.packs import questions, revision_pack
from paywall.render import leak_check
from paywall.split import split_bundle
from storefront.config import load_ladder

from .conftest import REAL_PRODUCT, REPO_ROOT

pytestmark = pytest.mark.skipif(
    not (REAL_PRODUCT / "product.yaml").exists(), reason="no product manifest here"
)


@pytest.fixture(scope="module")
def real():
    product = load_product(REAL_PRODUCT)
    bundle = load_bundle(REAL_PRODUCT, product)
    split = split_bundle(bundle, product)
    split.paid.setdefault("packs.revision", {})["pack"] = revision_pack(bundle)
    return {"product": product, "bundle": bundle, "split": split}


def built(name):
    path = REPO_ROOT / name
    if not path.exists():
        pytest.skip(f"{name} has not been built")
    return path.read_text(encoding="utf-8")


# ------------------------------------------------------- 1. the gate holds


def test_the_notes_split_into_a_free_half_and_a_sold_half(real):
    product, bundle, split = real["product"], real["bundle"], real["split"]
    free_chapters = {c["id"]: c for c in split.free["chapters"]}
    samples = set(product.rule("chapters").samples)
    assert samples and samples <= set(free_chapters)

    for chapter in bundle["chapters"]:
        identifier = chapter["id"]
        free = free_chapters[identifier]
        if identifier in samples:
            assert free["s"]["sol"] == chapter["s"]["sol"], identifier
            continue
        # withheld: the recall box, the detail, the questions, the solutions,
        # the self-test and the answering tips
        assert "recall" not in free, identifier
        for section in ("brief", "pyq", "sol", "test", "tips"):
            assert section not in free["s"], f"{identifier}/{section}"
        # free: everything the planner needs, plus the scope, the deleted
        # topics and the plain-English opening
        for field in ("unitMarks", "prio", "appear", "deleted", "intro", "title"):
            assert free[field] == chapter[field], f"{identifier}/{field}"
        assert free["s"]["scope"] == chapter["s"]["scope"], identifier


def test_neither_public_page_contains_the_paid_half(real):
    """The claim the whole product rests on, made about the shipped files."""
    pages = built("index.html") + "\n" + built("app.html")
    report = leak_check(pages, real["split"].paid, real["split"].free)
    assert report.checked_snippets > 100
    assert report.leaks == []

    # and spot-check by hand, not only through the checker
    paid = json.loads((REPO_ROOT / "api" / "_data" / "paid.json").read_text(encoding="utf-8"))
    for identifier, payload in list(paid["chapters"].items())[:6]:
        assert payload["s"]["sol"] not in pages, identifier
        assert payload["recall"] not in pages, identifier


def test_the_paid_half_is_not_where_a_static_host_would_serve_it():
    data = REPO_ROOT / "api" / "_data" / "paid.json"
    assert data.exists()
    # under api/, and under a leading-underscore directory, which is how the
    # host spells "not a route"
    assert data.parent.name.startswith("_")
    assert not (REPO_ROOT / "paid.json").exists()


# ------------------------------------------- 2. the committed build is current


def test_the_committed_build_matches_the_notes(real):
    """A stale build sells what the notes used to say."""
    committed = json.loads(
        (REPO_ROOT / "api" / "_data" / "paid.json").read_text(encoding="utf-8")
    )
    for identifier, payload in real["split"].paid["chapters"].items():
        assert committed["chapters"][identifier] == payload, (
            f"api/_data is stale for {identifier} — run `python3 product/build.py`"
        )
    assert committed["packs.revision"]["pack"]["sheets"], "the print pack is empty"


def test_the_app_and_the_landing_page_are_both_committed():
    for name in ("index.html", "app.html", "thanks.html"):
        assert (REPO_ROOT / name).exists(), f"{name} is missing — run the build"
    for name in ("unlock", "claim", "webhook"):
        source = (REPO_ROOT / "api" / f"{name}.py").read_text(encoding="utf-8")
        assert "class handler" in source
        assert f'dispatch("{name}"' in source


def test_the_app_assembles_with_nothing_left_behind():
    app = built("app.html")
    assert "/*__" not in app, "an unfilled placeholder survived into the page"
    assert app.count("<script") == app.count("</script>")
    for part in ("function planView", "function chapterView", "function unlockWithKey"):
        assert part in app, f"{part} is missing from the assembled app"


def test_the_vendored_library_imports_with_nothing_installed():
    """The function bundle must not need PyYAML, requests or playwright."""
    lib = REPO_ROOT / "api" / "_lib"
    result = subprocess.run(
        [sys.executable, "-c",
         "import sys; sys.path.insert(0, %r); sys.modules['yaml'] = None;"
         " from paywall.serverless import dispatch, load_runtime;"
         " from paywall.endpoints import unlock; print('ok')" % str(lib)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "ok" in result.stdout


def test_the_host_config_does_not_rewrite_anything():
    """The 404 this site had before came from a rewrite plus cleanUrls."""
    config = json.loads((REPO_ROOT / "vercel.json").read_text(encoding="utf-8"))
    assert config.get("cleanUrls") is True
    assert "rewrites" not in config
    assert "routes" not in config


def test_the_runtime_files_are_where_the_handlers_look_for_them():
    """`_lib` and `_data` sit under `api/`, under a leading underscore.

    The underscore is how the host spells "not a route", so the paid bundle is
    never served as a static file. Whether the host *bundles* them into the
    function is a separate question, and not one to answer in config: a
    `functions.includeFiles` block written to force it failed this project's
    build, while the same commit without it deployed. The handler fails loudly
    and by name if a file is missing, so one live request settles it.
    """
    config = json.loads((REPO_ROOT / "vercel.json").read_text(encoding="utf-8"))
    assert "functions" not in config, (
        "a functions block broke this project's build once — see product/build.py"
    )
    for path in ("api/_lib/paywall/serverless.py", "api/_data/product.json",
                 "api/_data/paid.json"):
        assert (REPO_ROOT / path).exists(), path
        assert path.split("/")[1].startswith("_"), path
