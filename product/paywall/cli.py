"""CLI for the gated product.

    python -m paywall.cli build   products/marks-first
    python -m paywall.cli check   products/marks-first
    python -m paywall.cli issue   products/marks-first --order 1234 --offers core,bump
    python -m paywall.cli verify  products/marks-first --key MF1-...
    python -m paywall.cli revoke  products/marks-first --order 1234
    python -m paywall.cli grants  products/marks-first

The licence signing secret comes from `PAYWALL_SECRET` and is never written
to a file by anything here. Losing it means every key ever issued stops
verifying, so it belongs in the same place as the payment provider's
credentials, and it must be the same value the deployed endpoint uses.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from storefront.providers import RECOMMENDED

from . import licence as licence_mod
from . import packs as packs_mod
from .build import build
from .manifest import load_bundle, load_product, product_dir
from .models import GateError
from .split import split_bundle
from .store import FileGrantStore

SECRET_ENV = "PAYWALL_SECRET"
DEFAULT_STORE = "data/grants.jsonl"


def main(argv: list[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 2
    try:
        return {
            "build": _build,
            "check": _check,
            "issue": _issue,
            "verify": _verify,
            "revoke": _revoke,
            "grants": _grants,
        }[args.command](args)
    except (GateError, licence_mod.LicenceError) as exc:
        print(f"  {exc}", file=sys.stderr)
        return 1


def _build(args) -> int:
    result = build(
        args.product,
        provider=args.provider,
        store=args.store or "",
        product_ids=_ids(args.product_ids),
        site_url=args.site_url or "",
        note=args.note or "",
        clean=args.clean,
    )
    split = result.split

    print(f"\n{result.product.name} — built into {result.deploy}\n")
    header = f"{'collection':<14} {'items':>6} {'free':>6} {'gated':>6} {'public KB':>10} {'sold KB':>9}"
    print(header)
    print("-" * len(header))
    for collection in split.collections:
        print(
            f"{collection.collection:<14} {collection.items:>6} {collection.samples:>6}"
            f" {collection.gated:>6} {collection.free_bytes / 1024:>10.0f}"
            f" {collection.paid_bytes / 1024:>9.0f}"
        )
    print(
        f"\npublic page  {result.render.megabytes:.2f} MB"
        f"\nsold bundle  {split.paid_bytes / 1048576:.2f} MB"
        f"\nfree share   {split.free_share:.1%} of the product, by bytes"
        f"\nleak check   {result.render.checked_snippets} paid passages searched for in the "
        f"public page, {len(result.render.leaks)} found"
    )
    for path in result.written:
        print(f"  wrote {path}")

    if result.checkout:
        print("\ncheckout links:")
        for slug, url in result.checkout.items():
            print(f"  {slug:<10} {url}")

    if args.feasibility:
        print("\nQuestion bank against the board's paper design:")
        print(packs_mod.format_feasibility(result.feasibility))

    if result.render.stray_hosts:
        print(f"\nnote  external hosts referenced: {', '.join(result.render.stray_hosts)}")
    for warning in result.warnings:
        print(f"\nwarn  {warning}")
    if not os.environ.get(SECRET_ENV):
        print(
            f"\nwarn  {SECRET_ENV} is not set here. The build does not need it, but "
            "the deployed endpoint does, and it must be the same value that "
            "issued the keys."
        )
    return 0


def _check(args) -> int:
    """Apply the gate without writing anything. The pre-flight."""
    product = load_product(args.product)
    bundle = load_bundle(args.product, product)
    split = split_bundle(bundle, product)

    print(f"\n{product.name} — gate check\n")
    for collection in split.collections:
        withheld = ", ".join(collection.withheld_paths) or "nothing"
        print(
            f"  {collection.collection:<12} {collection.items:>3} items, "
            f"{collection.samples} free in full, {collection.gated} gated"
            f"\n               withholds: {withheld}"
        )
    print(f"\n  free share {split.free_share:.1%}")
    print("  entitlements:")
    for entitlement in product.entitlements:
        grants = ", ".join(entitlement.grants) or "no new content"
        print(
            f"    {entitlement.code}  {entitlement.offer:<10} {grants}"
            f"  ·  {entitlement.seats} seat(s)"
        )
    for warning in split.warnings:
        print(f"\nwarn  {warning}")
    return 0


def _issue(args) -> int:
    """Sign a key by hand — for a support case, a comp, or a test."""
    product = load_product(args.product)
    secret = _secret()
    offers = [o.strip() for o in (args.offers or "core").split(",") if o.strip()]
    unknown = [o for o in offers if product.entitlement(o) is None]
    if unknown:
        print(f"  unknown offer(s): {', '.join(unknown)}", file=sys.stderr)
        return 1

    codes = product.codes_for(offers)
    missing = product.missing_requirements(codes)
    if missing:
        print(
            f"  {', '.join(offers)} needs {', '.join(missing)} alongside it — "
            f"add it, or the key opens nothing.",
            file=sys.stderr,
        )
        return 1

    key = licence_mod.issue(
        secret, order_id=args.order, codes=codes, expires_days=args.expires
    )
    print(f"\n{key}\n")
    print(f"  order       {args.order}")
    print(f"  opens       {', '.join(product.grants_for(codes)) or 'no new content'}")
    print(f"  devices     {product.seats_for(codes)}")
    print(f"  expires     {'never' if not args.expires else f'in {args.expires} days'}")
    if args.record:
        store = FileGrantStore(args.record)
        from .models import Grant
        store.put(Grant(
            order_id=args.order, provider="manual", email=args.email or "",
            codes=codes, key=key,
        ))
        print(f"  recorded in {args.record}")
    return 0


def _verify(args) -> int:
    product = load_product(args.product)
    licence = licence_mod.verify(_secret(), args.key, product=product)
    print(f"\n  order       {licence.order_id}")
    print(f"  codes       {licence.codes}")
    print(f"  opens       {', '.join(product.grants_for(licence.codes)) or 'no new content'}")
    print(f"  devices     {product.seats_for(licence.codes)}")
    print(f"  expires     {licence_mod.expiry_date(licence) or 'never'}")
    if licence.unknown_codes:
        print(
            f"  note        this key also carries code(s) "
            f"{licence.unknown_codes!r} that this build does not know"
        )
    store = FileGrantStore(args.record)
    grant = store.by_order(licence.order_id)
    if grant is None:
        print("  grant       not in the store — issued elsewhere, or a different store file")
    else:
        print(f"  grant       {grant.email or 'no email'}, {len(grant.activations)} device(s) used")
        if grant.revoked:
            print("  REVOKED     this licence has been withdrawn")
    return 0


def _revoke(args) -> int:
    store = FileGrantStore(args.record)
    if not store.revoke(args.order):
        print(f"  no grant for order {args.order!r} in {args.record}", file=sys.stderr)
        return 1
    print(f"  order {args.order} revoked. The endpoint refuses its key from now on.")
    return 0


def _grants(args) -> int:
    store = FileGrantStore(args.record)
    rows = store.all()
    if not rows:
        print(f"  no grants recorded in {args.record}")
        return 0
    header = f"{'order':<16} {'codes':<7} {'devices':>7} {'total':>9}  {'email':<28} state"
    print("\n" + header)
    print("-" * len(header))
    for grant in rows:
        state = "revoked" if grant.revoked else ("test" if grant.test_mode else "live")
        print(
            f"{grant.order_id:<16} {grant.codes:<7} {len(grant.activations):>7}"
            f" {grant.total:>9.2f}  {grant.email[:28]:<28} {state}"
        )
    return 0


def _secret() -> str:
    secret = os.environ.get(SECRET_ENV, "")
    if not secret:
        raise licence_mod.LicenceError(
            f"{SECRET_ENV} is not set. It signs every licence key, so the value "
            "here has to be the one the deployed endpoint uses."
        )
    return secret


def _ids(pairs: list[str] | None) -> dict[str, str]:
    if not pairs:
        return {}
    return dict(pair.split("=", 1) for pair in pairs)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build and license a gated product.")
    sub = parser.add_subparsers(dest="command")

    build_cmd = sub.add_parser("build", help="Build the deployable funnel.")
    build_cmd.add_argument("product", help="Product directory (with product.yaml).")
    build_cmd.add_argument("--provider", default=RECOMMENDED)
    build_cmd.add_argument("--store", help="The provider-side store name.")
    build_cmd.add_argument("--product-ids", nargs="*", metavar="SLUG=ID")
    build_cmd.add_argument("--site-url", help="Absolute site URL, for the endpoints.")
    build_cmd.add_argument("--note", help="A line shown in the app's Access dialog, for a "
                                          "deployment that is a preview rather than a shop.")
    build_cmd.add_argument("--clean", action="store_true",
                           help="Empty the deploy directory first.")
    build_cmd.add_argument("--feasibility", action="store_true",
                           help="Also report the question bank against the paper design.")

    check_cmd = sub.add_parser("check", help="Apply the gate without writing anything.")
    check_cmd.add_argument("product")

    issue_cmd = sub.add_parser("issue", help="Sign a licence key by hand.")
    issue_cmd.add_argument("product")
    issue_cmd.add_argument("--order", required=True)
    issue_cmd.add_argument("--offers", default="core", help="Comma-separated offer slugs.")
    issue_cmd.add_argument("--expires", type=int, default=0, help="Days; 0 for never.")
    issue_cmd.add_argument("--email", default="")
    issue_cmd.add_argument("--record", help="Also record the grant in this store file.")

    verify_cmd = sub.add_parser("verify", help="Check a key and say what it opens.")
    verify_cmd.add_argument("product")
    verify_cmd.add_argument("--key", required=True)
    verify_cmd.add_argument("--record", default=DEFAULT_STORE)

    revoke_cmd = sub.add_parser("revoke", help="Withdraw access for an order.")
    revoke_cmd.add_argument("product")
    revoke_cmd.add_argument("--order", required=True)
    revoke_cmd.add_argument("--record", default=DEFAULT_STORE)

    grants_cmd = sub.add_parser("grants", help="List recorded purchases.")
    grants_cmd.add_argument("product")
    grants_cmd.add_argument("--record", default=DEFAULT_STORE)
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
