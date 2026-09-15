"""Loading a product manifest, and pulling its content bundle in.

The manifest is the only file that knows this particular product. Everything
else in `paywall/` works from what it declares, so a second product — another
board, another class, another subject pair — is a directory with a manifest
and a content extractor, not a fork of the build.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any

from .models import Entitlement, GateError, GateRule, Product


def load_product(path: str | Path) -> Product:
    """Load `product.yaml` from a product directory, or the file itself."""
    manifest = _manifest_path(Path(path))
    data = _load(manifest)

    missing = [k for k in ("slug", "name", "audience") if not data.get(k)]
    if missing:
        raise GateError(f"{manifest}: missing {', '.join(missing)}")

    gate = data.get("gate") or {}
    rules = tuple(
        _rule(name, raw) for name, raw in (gate.get("collections") or {}).items()
    )
    for name in gate.get("free_collections") or []:
        rules += (GateRule(collection=str(name), free_whole=True),)

    entitlements = tuple(
        _entitlement(offer, raw) for offer, raw in (data.get("entitlements") or {}).items()
    )

    return Product(
        slug=str(data["slug"]),
        name=str(data["name"]),
        audience=str(data["audience"]),
        tagline=str(data.get("tagline", "")),
        currency=str(data.get("currency", "USD")),
        extractor=str(data.get("extractor", "extract")),
        app=str(data.get("app", "app/app.src.html")),
        ladder=str(data.get("ladder", "")),
        funnel=str(data.get("funnel", "")),
        rules=rules,
        entitlements=entitlements,
        packs=tuple(str(p) for p in data.get("packs") or ()),
        deploy=str(data.get("deploy", "deploy")),
        support_email=str(data.get("support_email", "")),
        site_url=str(data.get("site_url", "")),
        sample_note=str(data.get("sample_note", "")),
    )


def product_dir(path: str | Path) -> Path:
    """The directory a manifest path refers to."""
    path = Path(path)
    return path if path.is_dir() else path.parent


def load_bundle(path: str | Path, product: Product) -> dict[str, Any]:
    """Import the product's extractor and call its `bundle()`.

    Loaded by file path rather than by package name: a product directory is
    content plus one script, not an installed package, and requiring it to be
    importable would make every product a packaging problem.
    """
    directory = product_dir(path)
    script = directory / product.extractor
    if script.suffix != ".py":
        script = script.with_suffix(".py")
    if not script.exists():
        raise GateError(f"{script}: no content extractor for product {product.slug!r}")

    spec = importlib.util.spec_from_file_location(f"_product_{product.slug}", script)
    if spec is None or spec.loader is None:
        raise GateError(f"{script}: cannot be imported")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "bundle"):
        raise GateError(f"{script}: defines no bundle() function")
    data = module.bundle()
    if not isinstance(data, dict):
        raise GateError(f"{script}: bundle() must return a dict, got {type(data).__name__}")
    return data


def _manifest_path(path: Path) -> Path:
    if path.is_dir():
        for name in ("product.yaml", "product.yml", "product.json"):
            candidate = path / name
            if candidate.exists():
                return candidate
        raise GateError(f"{path}: no product.yaml here")
    if not path.exists():
        raise GateError(f"{path}: no such manifest")
    return path


def _rule(collection: str, raw: dict[str, Any]) -> GateRule:
    raw = raw or {}
    return GateRule(
        collection=str(collection),
        key=str(raw.get("key", "id")),
        samples=tuple(str(s) for s in raw.get("samples") or ()),
        free_fields=tuple(str(f) for f in raw.get("free_fields") or ()),
        free_whole=bool(raw.get("free_whole", False)),
    )


def _entitlement(offer: str, raw: dict[str, Any]) -> Entitlement:
    raw = raw or {}
    if "code" not in raw:
        raise GateError(
            f"entitlement {offer!r} has no code. It is written into every "
            "licence key, so it has to be chosen explicitly and never changed."
        )
    return Entitlement(
        offer=str(offer),
        code=str(raw["code"]),
        grants=tuple(str(g) for g in raw.get("grants") or ()),
        seats=int(raw.get("seats", 1)),
        requires=tuple(str(r) for r in raw.get("requires") or ()),
        name=str(raw.get("name", "")),
    )


def _load(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in (".yaml", ".yml"):
        try:
            import yaml
        except ImportError as exc:  # pragma: no cover - environment problem
            raise ImportError("YAML manifests need PyYAML, or use JSON.") from exc
        return yaml.safe_load(text) or {}
    return json.loads(text)
