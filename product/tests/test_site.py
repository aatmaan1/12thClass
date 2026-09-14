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


# ------------------------------------------------- 3. the numbers on the page


def test_the_landing_page_only_claims_what_the_notes_contain(real):
    page = built("index.html")
    bundle = real["bundle"]
    assert str(len(bundle["chapters"])) in page
    assert str(len(questions(bundle))) in page          # 332 board questions

    # the weightage chart is the real CBSE unit weightage, to scale
    marks_on_page = [int(m) for m in re.findall(r"<b>(\d+)</b></div>", page)]
    real_units, seen = [], set()
    for chapter in bundle["chapters"]:
        key = (chapter["subj"], chapter["unit"])
        if key not in seen:
            seen.add(key)
            real_units.append(chapter["unitMarks"])
    assert marks_on_page == real_units
    # and every bar is drawn in proportion to the widest
    widths = [float(w) for w in re.findall(r'ch-bar" style="width:([\d.]+)%', page)]
    assert len(widths) == len(real_units)
    widest = max(real_units)
    for marks, width in zip(real_units, widths):
        assert abs(width - 100 * marks / widest) < 0.11


def test_the_landing_page_quotes_the_marking_scheme_verbatim(real):
    """A page arguing "marks are for steps" with an invented example would be
    arguing against itself."""
    page = built("index.html")
    traps = re.findall(r'<div class="trap"><b>(.*?)</b><p>(.*?)</p>', page, re.S)
    assert len(traps) == 3
    by_title = {c["title"]: c for c in real["bundle"]["chapters"]}
    for where, text in traps:
        chapter = by_title[where.split(" · ", 1)[1]]
        # the quote is a run of words from that chapter's own answering tips,
        # with the markdown emphasis dropped and nothing else changed
        needle = " ".join(html.unescape(text).split()[:8])
        tips = re.sub(r"\s+", " ", chapter["s"]["tips"].replace("**", "").replace("*", ""))
        assert needle in tips, f"{where}: {needle!r} is not in the notes"


def test_every_ladder_rung_is_something_the_gate_can_unlock(real):
    product = real["product"]
    ladder = load_ladder(REAL_PRODUCT / product.ladder)
    assert {o.slug for o in ladder.offers} == {e.offer for e in product.entitlements}
    assert ladder.currency == product.currency
    for offer in ladder.offers:
        entitlement = product.entitlement(offer.slug)
        assert entitlement is not None, offer.slug
        # a rung that grants no content has to be worth buying for its seats
        if not entitlement.grants:
            assert entitlement.seats > 1, offer.slug
    # and the prices on the landing page are the ladder's
    page = built("index.html")
    for offer in ladder.offers:
        assert offer.display() in page, offer.slug


def test_the_products_own_translations_are_not_in_the_notes(real):
    """The notes are a study guide, not half a shopfront.

    The Hindi wording for the paywall and the planner belongs to the product.
    In the notes' `i18n/` it would ship to anyone reading the repository as
    notes, and be edited by people editing chapters.
    """
    overlay = json.loads(
        (REAL_PRODUCT / "i18n" / "hi" / "ui.json").read_text(encoding="utf-8")
    )
    keys = set(overlay) - {"_note"}
    assert {"lock.h", "unlock.go", "plan.queueH", "led.inHand"} <= keys

    notes_ui = json.loads(
        (REPO_ROOT / "i18n" / "hi" / "ui.json").read_text(encoding="utf-8")
    )
    assert not (keys & set(notes_ui)), (
        "these strings are in both the notes and the product overlay"
    )
    assert keys <= set(real["bundle"]["langs"]["hi"]["ui"])


def test_the_runtime_manifest_says_what_each_key_opens(real):
    from paywall.build import runtime_manifest

    rebuilt = Product.from_runtime(runtime_manifest(real["product"]))
    written = Product.from_runtime(
        json.loads((REPO_ROOT / "api" / "_data" / "product.json").read_text(encoding="utf-8"))
    )
    for codes in ("c", "bc", "cu", "cd"):
        assert rebuilt.grants_for(codes) == real["product"].grants_for(codes)
        assert written.grants_for(codes) == real["product"].grants_for(codes)
        assert written.seats_for(codes) == real["product"].seats_for(codes)


# ------------------------------------------- 4. the translated question bank


def test_the_translated_questions_are_gated_like_the_english(real):
    """Questions and solutions are the paid half in *any* language.

    They are attached to the chapter rather than to the language pack, which
    ships whole because an interface is not the product. On the chapter they
    pass through the same gate: a locked chapter withholds its Hindi solutions
    and a free sample hands them over. In the language pack they would have
    been a straight leak, and one the English-only leak check would not see.
    """
    product, bundle, split = real["product"], real["bundle"], real["split"]
    samples = set(product.rule("chapters").samples)
    translated = [c for c in bundle["chapters"] if (c.get("tr") or {}).get("hi")]
    assert len(translated) == len(bundle["chapters"]), "every chapter has a Hindi set"

    free_chapters = {c["id"]: c for c in split.free["chapters"]}
    for chapter in translated:
        free = free_chapters[chapter["id"]]
        if chapter["id"] in samples:
            assert free["tr"]["hi"]["sol"] == chapter["tr"]["hi"]["sol"], chapter["id"]
        else:
            assert "tr" not in free, chapter["id"]
            assert split.paid["chapters"][chapter["id"]]["tr"]["hi"]["sol"]

    # and the language pack itself carries nothing that is sold. It ships
    # whole, to everyone, so this set is the whole of the gate for it.
    free_keys = {"ui", "titles", "units", "docs", "intros", "scopes",
                 "deleteds", "appears"}
    assert set(split.free["langs"]["hi"]) <= free_keys, "a new key in the pack"
    for sold in ("pyq", "sol", "tips", "test", "recall", "brief", "qa"):
        assert sold not in split.free["langs"]["hi"], sold


def test_no_hindi_solution_of_a_locked_chapter_reaches_the_public_page(real):
    """The check the English-only leak scan cannot make."""
    pages = built("index.html") + "\n" + built("app.html")
    samples = set(real["product"].rule("chapters").samples)
    checked = 0
    for chapter in real["bundle"]["chapters"]:
        if chapter["id"] in samples:
            continue
        hindi = (chapter.get("tr") or {}).get("hi") or {}
        for field in ("pyq", "sol"):
            text = hindi.get(field) or ""
            if len(text) < 200:
                continue
            middle = len(text) // 2
            needle = re.sub(r"\s+", " ", text[middle - 60:middle + 60])
            assert needle not in re.sub(r"\s+", " ", pages), f"{chapter['id']}/{field}"
            checked += 1
    assert checked >= 40, "this test should be looking at both fields of 25 chapters"


def test_the_question_numbering_survives_translation(real):
    """Each question is paired with its solution by number, so a mismatch
    would silently show the wrong working."""
    for chapter in real["bundle"]["chapters"]:
        hindi = (chapter.get("tr") or {}).get("hi")
        if not hindi:
            continue
        english = re.findall(r"^\*\*Q(\d+)\.\*\*", chapter["s"]["pyq"], re.M)
        assert re.findall(r"^\*\*Q(\d+)\.\*\*", hindi["pyq"], re.M) == english, chapter["id"]
        assert re.findall(r"^### Q(\d+)\b", hindi["sol"], re.M) == english, chapter["id"]


def test_a_translated_section_is_gated_by_what_it_costs(real):
    """Where a translation lives has to follow the price of what it translates.

    The free sections ride in the language pack, which ships whole to every
    visitor. The sold ones ride on the chapter, where the gate withholds them.
    Put a sold section in the pack and it is published in every language at
    once — invisibly, because a leak check written against English will not
    find a word of it.
    """
    import extract

    assert set(extract.TR_FREE) == {"INTRO", "SCOPE", "DELETED", "APPEAR"}
    assert set(extract.TR_PAID) == {"TIPS", "TEST", "RECALL", "DETAIL"}

    product = real["product"]
    free_fields = set(product.rule("chapters").free_fields)
    # every marker the free half claims is a field the gate also gives away
    for field in extract.TR_FREE.values():
        english = {"intros": "intro", "scopes": "s.scope",
                   "deleteds": "deleted", "appears": "appear"}[field]
        assert english in free_fields, field
    # and none of the sold ones is
    for field in extract.TR_PAID.values():
        for spelling in (field, "s." + field):
            assert spelling not in free_fields, field


def test_a_chapter_file_splits_on_its_markers():
    """The file format, including the one that predates it having sections."""
    import extract

    names = set(extract.TR_FREE) | set(extract.TR_PAID)

    plain = extract.marked("### यहाँ\n\nbody text\n", names)
    assert plain == {"INTRO": "body text"}, "an unmarked file is all intro"

    split = extract.marked(
        "<!-- INTRO -->\nhello\n<!-- TEST -->\nq1\n<!-- SCOPE -->\n\n", names
    )
    assert split == {"INTRO": "hello", "TEST": "q1"}, "an empty section is absent"

    with pytest.raises(SystemExit):
        extract.marked("<!-- SOLUTIONS -->\nx\n", names)


def test_a_chapter_keeps_its_sections_and_its_questions(real):
    """Both attach to `tr[lang]`, and the second used to assign over the first."""
    m13 = [c for c in real["bundle"]["chapters"] if c["id"] == "m13"][0]
    hi = m13["tr"]["hi"]
    assert {"pyq", "sol"} <= set(hi), "the questions survived the sections"
    assert {"tips", "test", "recall", "brief"} <= set(hi), "the sections survived the questions"
