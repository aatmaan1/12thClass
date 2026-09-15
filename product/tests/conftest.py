"""Fixtures: a small synthetic product, and the real one.

Most tests run against the synthetic product — three chapters and two
documents, small enough that a failure points at one field. The build tests
run against `products/marks-first` as well, because "the gate holds on the
actual product" is the claim that matters and it is not implied by the claim
holding on a fixture.
"""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

import pytest

from paywall.models import Entitlement, GateRule, Product

REPO_ROOT = Path(__file__).resolve().parents[2]
#: The product is this repository: the notes are at the root, and `product/`
#: holds the things that sell them.
REAL_PRODUCT = REPO_ROOT / "product"

#: Filler long enough for `render.leak_check` to take a distinctive snippet
#: from the middle of a field, which needs about 180 characters.
#:
#: Every sentence names the field it belongs to, so *any* 90-character window
#: of it is unique to that field. That matters: the leak check treats a
#: passage found in both halves as shared wording rather than as an escape,
#: which is right for real boilerplate and would quietly disable the check
#: here if the fixture repeated itself.
def filler(tag: str) -> str:
    return " ".join(
        f"Step {n} of {tag}: write the formula for {tag}, substitute with units, "
        f"then give the answer for {tag} with its unit."
        for n in range(1, 6)
    )


def chapter(identifier: str, number: int) -> dict:
    """One fixture chapter, with every field distinct."""
    return {
        "id": identifier,
        "num": number,
        "title": f"Chapter {number}",
        "intro": f"A plain-English opening for chapter {number}, free to read.",
        "recall": f"Recall box {number}. " + filler(f"{identifier} recall"),
        "s": {
            "scope": f"Scope of chapter {number}, free to read. "
                     + filler(f"{identifier} scope"),
            "pyq": f"**Q1.** *(3 marks)* Question one of chapter {number}. "
                   + filler(f"{identifier} questions"),
            "sol": f"### Q1\nSolution one of chapter {number}. "
                   + filler(f"{identifier} solutions"),
        },
    }


@pytest.fixture
def bundle() -> dict:
    return {
        "chapters": [chapter("a1", 1), chapter("a2", 2), chapter("a3", 3)],
        "docs": [
            {"id": "free-doc", "title": "Blueprint", "blurb": "How the paper works",
             "body": "The blueprint body. " + filler("the blueprint")},
            {"id": "paid-doc", "title": "Formula sheet", "blurb": "Every formula",
             "body": "The formula sheet body. " + filler("the formula sheet")},
        ],
        "langs": {"xx": {"ui": {"a": "b"}}},
    }


@pytest.fixture
def product() -> Product:
    return build_product()


def build_product(**overrides) -> Product:
    base = dict(
        slug="fixture",
        name="Fixture",
        audience="people",
        currency="INR",
        rules=(
            GateRule(
                collection="chapters", key="id", samples=("a3",),
                free_fields=("id", "num", "title", "intro", "s.scope"),
            ),
            GateRule(
                collection="docs", key="id", samples=("free-doc",),
                free_fields=("id", "title", "blurb"),
            ),
            GateRule(collection="langs", free_whole=True),
        ),
        entitlements=(
            Entitlement(offer="core", code="c", grants=("chapters", "docs"), seats=1),
            Entitlement(offer="bump", code="b", grants=("packs.revision",), seats=1,
                        requires=("core",)),
            Entitlement(offer="upsell", code="u", grants=(), seats=5, requires=("core",)),
        ),
        packs=("packs.revision",),
    )
    return Product(**{**base, **overrides})


@pytest.fixture
def product_dir(tmp_path: Path, bundle: dict) -> Path:
    """A complete product directory on disk: manifest, extractor, app."""
    directory = tmp_path / "fixture-product"
    (directory / "app").mkdir(parents=True)

    (directory / "product.yaml").write_text(json.dumps({
        "slug": "fixture",
        "name": "Fixture",
        "tagline": "A fixture product",
        "audience": "people sitting an exam",
        "currency": "INR",
        "extractor": "extract.py",
        "app": "app/app.src.html",
        "support_email": "help@example.test",
        "gate": {
            "free_collections": ["langs"],
            "collections": {
                "chapters": {
                    "key": "id", "samples": ["a3"],
                    "free_fields": ["id", "num", "title", "intro", "s.scope"],
                },
                "docs": {
                    "key": "id", "samples": ["free-doc"],
                    "free_fields": ["id", "title", "blurb"],
                },
            },
        },
        "packs": ["packs.revision"],
        "entitlements": {
            "core": {"code": "c", "grants": ["chapters", "docs"], "seats": 1},
            "bump": {"code": "b", "grants": ["packs.revision"], "seats": 1,
                     "requires": ["core"]},
            "upsell": {"code": "u", "grants": [], "seats": 5, "requires": ["core"]},
        },
    }, indent=2), encoding="utf-8")

    # `product.yaml` is JSON here on purpose: the loader accepts either, and a
    # fixture that needs PyYAML to exist would make these tests skip silently
    # in an environment that has not installed it.
    (directory / "product.json").write_text(
        (directory / "product.yaml").read_text(encoding="utf-8"), encoding="utf-8"
    )
    (directory / "product.yaml").unlink()

    (directory / "extract.py").write_text(textwrap.dedent(f"""
        import json, os
        HERE = os.path.dirname(os.path.abspath(__file__))
        def bundle():
            with open(os.path.join(HERE, "bundle.json"), encoding="utf-8") as fh:
                return json.load(fh)
    """).strip() + "\n", encoding="utf-8")
    (directory / "bundle.json").write_text(
        json.dumps(bundle, ensure_ascii=False), encoding="utf-8"
    )

    (directory / "app" / "app.src.html").write_text(
        "<title>Fixture</title>\n<div id=\"view\"></div>\n"
        "<script>const DATA = /*__DATA__*/;\nconst PAYWALL = /*__PAYWALL__*/;</script>\n",
        encoding="utf-8",
    )
    return directory
