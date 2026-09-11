"""Wiring the endpoints up to a serverless host, and the request dispatcher.

The endpoint logic in `endpoints.py` takes its dependencies as arguments. This
is where those dependencies actually come from on a deployed host: environment
variables for the secrets, JSON files written by the build for the product and
the paid content, and a key-value store for the small amount of state that has
to outlive one request.

Kept as ordinary, importable, testable code rather than being inlined into the
platform's handler file, because the interesting failures live here: a missing
secret, a store that cannot be reached, a body that is not JSON. Each one has
a right answer, and none of them should be discovered in production.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

from . import endpoints
from .models import Product

#: Where the build puts what the endpoints read.
DATA_DIR = "_data"

#: Environment variables. The two secrets have no defaults on purpose.
ENV_SECRET = "PAYWALL_SECRET"
ENV_WEBHOOK_SECRET = "PAYWALL_WEBHOOK_SECRET"
ENV_PROVIDER = "PAYWALL_PROVIDER"
ENV_PRODUCT_IDS = "PAYWALL_PRODUCT_IDS"
ENV_STORE_FILE = "PAYWALL_STORE_FILE"
#: Opt-in, for looking at the funnel before there is anywhere to keep state.
ENV_DEMO = "PAYWALL_DEMO"
#: Vercel KV and Upstash set different names for the same REST endpoint.
ENV_KV_URLS = ("KV_REST_API_URL", "UPSTASH_REDIS_REST_URL")
ENV_KV_TOKENS = ("KV_REST_API_TOKEN", "UPSTASH_REDIS_REST_TOKEN")


class ConfigError(RuntimeError):
    """The endpoint cannot run as configured."""


@dataclass
class Runtime:
    product: Product
    paid: dict[str, Any]
    secret: str
    webhook_secret: str = ""
    provider: str = "lemonsqueezy"
    product_ids: dict[str, str] = field(default_factory=dict)
    grants: Any = None
    events: Any = None


def load_runtime(
    base: str | Path,
    env: Mapping[str, str] | None = None,
    *,
    grants: Any = None,
    events: Any = None,
) -> Runtime:
    """Assemble everything an endpoint needs, or say exactly what is missing."""
    env = env if env is not None else os.environ
    directory = Path(base)
    data = directory / DATA_DIR if (directory / DATA_DIR).is_dir() else directory

    product_file, paid_file = data / "product.json", data / "paid.json"
    for path in (product_file, paid_file):
        if not path.exists():
            raise ConfigError(
                f"{path.name} is missing from {data} — run `python -m paywall.cli "
                "build` and deploy what it writes"
            )

    secret = env.get(ENV_SECRET, "")
    if not secret:
        raise ConfigError(
            f"{ENV_SECRET} is not set. It signs and verifies every licence key; "
            "without it no purchase can be opened."
        )

    store = grants if grants is not None else open_store(env)
    # An injected store means the caller is doing the wiring, so an event store
    # is not demanded here — the webhook resolves one when it needs it, and
    # says so if there is none.
    if events is None and grants is None:
        events = open_events(env, store)
    return Runtime(
        product=Product.from_runtime(json.loads(product_file.read_text(encoding="utf-8"))),
        paid=json.loads(paid_file.read_text(encoding="utf-8")),
        secret=secret,
        webhook_secret=env.get(ENV_WEBHOOK_SECRET, ""),
        provider=env.get(ENV_PROVIDER, "lemonsqueezy"),
        product_ids=_product_ids(env.get(ENV_PRODUCT_IDS, "")),
        grants=store,
        events=events,
    )


def demo_mode(env: Mapping[str, str] | None = None) -> bool:
    """Whether this deployment is a look at the funnel rather than a shop.

    Opt-in and explicit, because everything it changes is a thing that must
    not be true of a deployment taking money.
    """
    env = env if env is not None else os.environ
    return str(env.get(ENV_DEMO, "")).strip().lower() in ("1", "true", "yes", "on")


def open_store(env: Mapping[str, str] | None = None) -> Any:
    """The grant store this host can actually keep state in.

    A key-value store if one is configured, a file if a path is given, and
    otherwise a refusal. There is deliberately no *silent* in-memory fallback:
    it would appear to work, count devices per instance, and lose every claim
    between the checkout and the thank-you page.

    `PAYWALL_DEMO=1` asks for that in-memory store on purpose, so the funnel
    can be walked through before there is anywhere to keep state. It changes
    nothing about who is let in — signatures are still verified, the webhook
    still needs its secret — only how long the little state there is survives.
    What it cannot do is sell anything: seats reset whenever the host recycles
    the instance, and a buyer cannot be handed their key on the thank-you page
    because the webhook that recorded it landed on a different instance.
    """
    env = env if env is not None else os.environ
    url = next((env[name] for name in ENV_KV_URLS if env.get(name)), "")
    token = next((env[name] for name in ENV_KV_TOKENS if env.get(name)), "")
    if url and token:
        from .kv import RestKVGrantStore
        return RestKVGrantStore(url, token, namespace=env.get("PAYWALL_NAMESPACE", "paywall"))

    path = env.get(ENV_STORE_FILE, "")
    if path:
        from .store import FileGrantStore
        return FileGrantStore(path)

    if demo_mode(env):
        from .store import MemoryGrantStore
        return MemoryGrantStore()

    raise ConfigError(
        "no grant store configured. Set KV_REST_API_URL and KV_REST_API_TOKEN "
        f"(any Redis-compatible REST store), or {ENV_STORE_FILE} on a host with "
        "a filesystem that persists. Without one, devices cannot be counted and "
        f"a buyer cannot be handed their key. To look at the funnel without "
        f"selling through it, set {ENV_DEMO}=1 instead."
    )


def open_events(env: Mapping[str, str] | None, grants: Any) -> Any:
    """Where handled webhook ids are remembered.

    The key-value store can do this itself, so it does. A file-backed grant
    store cannot — it holds grants, not events — and the webhook needs
    somewhere to record what it has already delivered, or a provider's retries
    deliver twice. So that case gets a `FileEventStore` beside the grants file.

    Passing the grant store as its own event store when it cannot do the job
    would fail at the worst possible moment: inside a live webhook, after the
    money had been taken.
    """
    env = env if env is not None else os.environ
    if hasattr(grants, "seen") and hasattr(grants, "remember"):
        return grants

    from storefront.fulfil import FileEventStore, MemoryEventStore

    path = env.get(ENV_STORE_FILE, "")
    if path:
        return FileEventStore(Path(path).with_name("handled-events.log"))
    if demo_mode(env):
        # Per-instance, so a retried webhook can deliver twice. Acceptable
        # only because a demo deployment is not taking money.
        return MemoryEventStore()
    raise ConfigError(
        "the configured grant store cannot deduplicate webhooks and there is "
        f"no {ENV_STORE_FILE} to keep an event log beside. Providers retry "
        "hard; without this, one sale is delivered several times."
    )


def demo_warning(env: Mapping[str, str] | None = None) -> str:
    """What to log on a demo deployment, once per cold start."""
    if not demo_mode(env):
        return ""
    return (
        f"{ENV_DEMO} is set: state is per-instance. Device counts reset when "
        "the host recycles, and the thank-you page cannot hand over a key. "
        "Do not take real payments through this deployment."
    )


def dispatch(
    name: str,
    raw_body: bytes,
    headers: Mapping[str, str],
    runtime: Runtime,
    *,
    now: float | None = None,
) -> endpoints.Response:
    """Route one request to its endpoint. Never raises for bad input."""
    if name == "webhook":
        if not runtime.webhook_secret:
            return endpoints.Response(
                500, {"error": f"{ENV_WEBHOOK_SECRET} is not set on this deployment"}
            )
        # Raises ConfigError when nothing here can deduplicate retries. That
        # reaches the platform handler as a 500 and a log line, which is the
        # right outcome: delivering one sale several times is worse than the
        # provider retrying a request that is failing loudly.
        events = runtime.events if runtime.events is not None else open_events(None, runtime.grants)
        return endpoints.webhook(
            raw_body, headers,
            provider=runtime.provider, product=runtime.product,
            webhook_secret=runtime.webhook_secret, licence_secret=runtime.secret,
            events=events,
            grants=runtime.grants, product_ids=runtime.product_ids, now=now,
        )

    try:
        payload = json.loads(raw_body or b"{}")
    except json.JSONDecodeError:
        return endpoints.Response(400, {"error": "the request body is not JSON"})
    if not isinstance(payload, dict):
        return endpoints.Response(400, {"error": "the request body is not a JSON object"})

    if name == "unlock":
        return endpoints.unlock(
            payload, product=runtime.product, secret=runtime.secret,
            paid=runtime.paid, grants=runtime.grants, now=now,
        )
    if name == "claim":
        return endpoints.claim(
            payload, product=runtime.product, secret=runtime.secret,
            paid=runtime.paid, grants=runtime.grants, now=now,
        )
    return endpoints.Response(404, {"error": f"no endpoint named {name!r}"})


def _product_ids(raw: str) -> dict[str, str]:
    if not raw.strip():
        return {}
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        # `core=aaa,bump=bbb` is easier to paste into a dashboard than JSON.
        return dict(
            pair.split("=", 1) for pair in raw.split(",") if "=" in pair
        )
    return {str(k): str(v) for k, v in parsed.items()} if isinstance(parsed, dict) else {}
