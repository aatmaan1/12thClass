"""The build's mechanics, against a synthetic product.

What this repository actually ships — the planner, the landing page, the gate
holding on the real notes — is in `test_site.py`. These are the pieces
underneath: loading a manifest, applying a gate, refusing a leak.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from paywall.build import build, paywall_config, runtime_manifest
from paywall.manifest import load_bundle, load_product
from paywall.models import GateError, Product
from paywall.render import LeakError
from paywall.split import split_bundle

from .conftest import REPO_ROOT


@pytest.fixture
def built(product_dir: Path):
    return build(product_dir)


# --------------------------------------------------------------- mechanics


def test_the_manifest_loads_from_a_directory(product_dir: Path):
    product = load_product(product_dir)
    assert product.slug == "fixture"
    assert product.currency == "INR"
    assert [e.code for e in product.entitlements] == ["c", "b", "u"]
    assert product.rule("langs").free_whole


def test_a_directory_with_no_manifest_says_so(tmp_path: Path):
    with pytest.raises(GateError, match="no product.yaml"):
        load_product(tmp_path)


def test_an_entitlement_without_a_code_is_refused(product_dir: Path):
    manifest = json.loads((product_dir / "product.json").read_text(encoding="utf-8"))
    del manifest["entitlements"]["core"]["code"]
    (product_dir / "product.json").write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(GateError, match="never changed"):
        load_product(product_dir)


def test_the_extractor_is_loaded_by_path(product_dir: Path):
    product = load_product(product_dir)
    bundle = load_bundle(product_dir, product)
    assert len(bundle["chapters"]) == 3


def test_a_missing_extractor_says_so(product_dir: Path):
    (product_dir / "extract.py").unlink()
    with pytest.raises(GateError, match="no content extractor"):
        load_bundle(product_dir, load_product(product_dir))


def test_the_build_writes_a_public_page_and_a_private_bundle(built):
    public = built.deploy / "public" / "index.html"
    paid = built.deploy / "api" / "_data" / "paid.json"
    assert public.exists() and paid.exists()
    assert "_data" in str(paid.parent)          # under api/, so not served
    assert not (built.deploy / "public" / "paid.json").exists()


def test_the_public_page_does_not_contain_the_paid_half(built):
    page = (built.deploy / "public" / "index.html").read_text(encoding="utf-8")
    paid = json.loads(
        (built.deploy / "api" / "_data" / "paid.json").read_text(encoding="utf-8")
    )
    for identifier, payload in paid["chapters"].items():
        assert payload["s"]["sol"] not in page, identifier
        assert payload["recall"] not in page
    assert built.render.leaks == []
    assert built.render.checked_snippets > 0


def test_a_leak_refuses_the_build(product_dir: Path):
    """The check has to be able to stop a build, not just report on one."""
    template = product_dir / "app" / "app.src.html"
    bundle = json.loads((product_dir / "bundle.json").read_text(encoding="utf-8"))
    leaked = bundle["chapters"][0]["s"]["sol"]
    template.write_text(
        template.read_text(encoding="utf-8") + f"\n<!-- {leaked} -->\n", encoding="utf-8"
    )
    with pytest.raises(LeakError, match="paid content is present"):
        build(product_dir)


def test_the_pack_is_built_and_sold_not_shipped(built):
    paid = json.loads(
        (built.deploy / "api" / "_data" / "paid.json").read_text(encoding="utf-8")
    )
    assert paid["packs.revision"]["pack"]["sheets"]
    page = (built.deploy / "public" / "index.html").read_text(encoding="utf-8")
    assert "Recall box 1." not in page


def test_the_endpoints_and_their_library_are_written(built):
    api = built.deploy / "api"
    for name in ("unlock", "claim", "webhook"):
        source = (api / f"{name}.py").read_text(encoding="utf-8")
        assert "class handler" in source
        assert f'dispatch("{name}"' in source
    assert (api / "_lib" / "paywall" / "licence.py").exists()
    assert (api / "_lib" / "storefront" / "fulfil.py").exists()
    assert (built.deploy / "vercel.json").exists()


def test_the_vendored_library_imports_with_nothing_installed(built):
    """The function bundle must not need PyYAML, requests or playwright."""
    lib = built.deploy / "api" / "_lib"
    result = subprocess.run(
        [sys.executable, "-c",
         "import sys; sys.path.insert(0, %r); sys.modules['yaml'] = None;"
         " from paywall.serverless import dispatch, load_runtime;"
         " from paywall.endpoints import unlock; print('ok')" % str(lib)],
        capture_output=True, text=True, cwd=str(built.deploy),
    )
    assert result.returncode == 0, result.stderr
    assert "ok" in result.stdout


def test_the_host_config_serves_public_and_hides_the_rest(built):
    config = json.loads((built.deploy / "vercel.json").read_text(encoding="utf-8"))
    assert config["outputDirectory"] == "public"
    assert any(r["source"] == "/get" for r in config["rewrites"])


def test_a_deployment_can_carry_a_note_for_the_access_dialog(product_dir: Path):
    """A preview or demo deployment should say so where a key gets pasted."""
    result = build(product_dir, note="This preview has no endpoints.")
    page = (result.deploy / "public" / "index.html").read_text(encoding="utf-8")
    assert "This preview has no endpoints." in page
    # and an ordinary build carries none
    assert '"note":""' in (
        build(product_dir).deploy / "public" / "index.html"
    ).read_text(encoding="utf-8").replace(", ", ",")


def test_the_runtime_manifest_round_trips(product_dir: Path):
    product = load_product(product_dir)
    rebuilt = Product.from_runtime(runtime_manifest(product))
    assert rebuilt.slug == product.slug
    for code in ("c", "b", "u"):
        assert rebuilt.grants_for(code) == product.grants_for(code)
        assert rebuilt.seats_for(code) == product.seats_for(code)


# ------------------------------------------------------ the actual product
