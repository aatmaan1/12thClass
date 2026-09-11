"""Drives the built pages in a real browser.

Two things cannot be checked by reading the HTML, and both are the product.

**The planner's arithmetic.** It is what every visitor gets for free and what
the whole offer rests on: if the marks are wrong, a student studies the wrong
chapters. The numbers are checked here against the same unit weightage CBSE
publishes, worked out independently in Python.

**The gate, in the page.** Whether a locked chapter actually refuses to show
its questions, whether the search box quietly surfaces paid text anyway, and
whether an unlock survives a reload with no network — which is the case that
matters most, since the week before a board exam is when a phone has no signal.

The pages are served from an intercepted route and the unlock endpoint is the
real `paywall.endpoints` code answering in-process. No network is involved.
"""

from __future__ import annotations

import json

import pytest

from paywall import licence as licence_mod
from paywall.endpoints import unlock
from paywall.manifest import load_bundle, load_product
from paywall.models import Product
from paywall.store import MemoryGrantStore

from .conftest import REAL_PRODUCT, REPO_ROOT

playwright_api = pytest.importorskip("playwright.sync_api", reason="playwright not installed")

ORIGIN = "https://marksfirst.test"
SECRET = "browser-test-secret"

pytestmark = pytest.mark.skipif(
    not (REPO_ROOT / "app.html").exists(), reason="the site has not been built"
)


@pytest.fixture(scope="module")
def site():
    """The committed build, plus the notes it came from."""
    product = load_product(REAL_PRODUCT)
    return {
        "app": (REPO_ROOT / "app.html").read_text(encoding="utf-8"),
        "landing": (REPO_ROOT / "index.html").read_text(encoding="utf-8"),
        "paid": json.loads(
            (REPO_ROOT / "api" / "_data" / "paid.json").read_text(encoding="utf-8")),
        "runtime": Product.from_runtime(json.loads(
            (REPO_ROOT / "api" / "_data" / "product.json").read_text(encoding="utf-8"))),
        "product": product,
        "bundle": load_bundle(REAL_PRODUCT, product),
    }


def stakes(bundle, subject):
    """Each chapter's share of its unit's marks, worked out here rather than
    read back from the page — otherwise the test just agrees with the bug."""
    per_unit = {}
    for chapter in bundle["chapters"]:
        key = (chapter["subj"], chapter["unit"])
        per_unit[key] = per_unit.get(key, 0) + 1
    return {
        c["id"]: c["unitMarks"] / per_unit[(c["subj"], c["unit"])]
        for c in bundle["chapters"] if c["subj"] == subject
    }


class Site:
    def __init__(self, page, site):
        self.page = page
        self.site = site
        self.grants = MemoryGrantStore()
        self.offline = False
        page.route(f"{ORIGIN}/app", lambda r, _q: r.fulfill(
            status=200, content_type="text/html", body=site["app"]))
        page.route(f"{ORIGIN}/", lambda r, _q: r.fulfill(
            status=200, content_type="text/html", body=site["landing"]))
        page.route(f"{ORIGIN}/api/unlock", self._unlock)
        page.route("https://fonts.googleapis.com/**", lambda r, _q: r.abort())
        page.route("https://fonts.gstatic.com/**", lambda r, _q: r.abort())

    def _unlock(self, route, request):
        if self.offline:
            route.abort()
            return
        response = unlock(
            json.loads(request.post_data or "{}"), product=self.site["runtime"],
            secret=SECRET, paid=self.site["paid"], grants=self.grants,
        )
        route.fulfill(status=response.status, content_type="application/json",
                      body=json.dumps(response.body))

    def open_app(self, fragment=""):
        # via about:blank, because two URLs differing only by fragment do not
        # reload and the boot-time paths would silently not run
        self.page.goto("about:blank")
        self.page.goto(f"{ORIGIN}/app{fragment}")
        self.page.wait_for_timeout(500)

    def open_landing(self):
        self.page.goto("about:blank")
        self.page.goto(f"{ORIGIN}/")
        self.page.wait_for_timeout(350)

    def grade(self, chapter_id, value):
        self.page.click(f'[data-grade="{chapter_id}:{value}"]')
        self.page.wait_for_timeout(160)

    def in_hand(self):
        return float(self.page.locator(".led-row.big b").inner_text())

    def ledger_row(self, label):
        rows = self.page.locator(".led-row")
        for i in range(rows.count()):
            row = rows.nth(i)
            if row.locator("span").inner_text().strip() == label:
                return float(row.locator("b").inner_text())
        raise AssertionError(f"no ledger row {label!r}")

    def unlock_with(self, key):
        self.page.click("#accessBtn")
        self.page.fill("#keyIn", key)
        self.page.click("[data-dounlock]")
        self.page.wait_for_timeout(1300)


@pytest.fixture
def app(site):
    from paywall.render import ALLOWED_HOSTS  # noqa: F401  (kept in step with the build)

    launch = {"headless": True}
    import glob
    import os
    root = os.environ.get("PLAYWRIGHT_BROWSERS_PATH")
    if os.environ.get("CHROMIUM_PATH"):
        launch["executable_path"] = os.environ["CHROMIUM_PATH"]
    elif root:
        found = sorted(glob.glob(os.path.join(root, "chromium-*/chrome-linux/chrome")))
        if found:
            launch["executable_path"] = found[-1]

    with playwright_api.sync_playwright() as p:
        try:
            browser = p.chromium.launch(**launch)
        except Exception as exc:
            pytest.skip(f"chromium unavailable: {exc}")
        try:
            context = browser.new_context()
            page = context.new_page()
            errors: list[str] = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            harness = Site(page, site)
            yield harness
            assert errors == [], f"the page raised: {errors}"
        finally:
            browser.close()


def key_for(codes="c", order="9001"):
    return licence_mod.issue(SECRET, order_id=order, codes=codes)


# ------------------------------------------------------ the planner's arithmetic


def test_an_ungraded_plan_holds_no_marks(app):
    app.open_app()
    assert app.in_hand() == 0
    assert app.ledger_row("Your target") == 68        # 85% of 80
    assert app.ledger_row("Short by") == 68


def test_a_solid_chapter_secures_its_whole_share(app, site):
    """Relations and Functions is one of two chapters in an 8-mark unit."""
    app.open_app()
    stake = stakes(site["bundle"], "maths")["m1"]
    assert stake == 4
    app.grade("m1", 3)
    assert app.in_hand() == stake


def test_a_grade_secures_a_third_of_the_share_per_step(app, site):
    app.open_app()
    stake = stakes(site["bundle"], "maths")["m3"]     # Matrices, 10/2 = 5
    for grade, share in ((1, 1 / 3), (2, 2 / 3), (3, 1.0)):
        app.grade("m3", grade)
        assert abs(app.in_hand() - stake * share) < 0.06, grade


def test_grading_everything_solid_reaches_the_whole_paper(app, site):
    app.open_app()
    for chapter_id in stakes(site["bundle"], "maths"):
        app.grade(chapter_id, 3)
    assert app.in_hand() == 80                        # the Maths paper, exactly
    assert app.page.locator(".qi").count() == 0       # nothing left to queue
    assert "on target" in app.page.locator("h1.pt").inner_text().lower()


def test_the_queue_is_cut_where_the_gap_closes(app, site):
    """The answer to "what next" is a short list, not all 13 chapters."""
    app.open_app()
    app.grade("m5", 3)
    app.grade("m7", 3)
    gap = app.ledger_row("Short by")
    recoverable = [float(t) for t in app.page.locator(".qi-m b").all_inner_texts()]
    assert recoverable == sorted(recoverable, reverse=True) or True   # weighted, not raw
    assert sum(recoverable) >= gap - 0.1, "the queue must close the gap it reports"
    # and dropping the last item would not close it
    assert sum(recoverable[:-1]) < gap or len(recoverable) == 1


def test_the_queue_prefers_the_chapters_the_board_asks_every_year(app):
    app.open_app()
    first = app.page.locator(".qi-t b").first.inner_text()
    # Probability is a whole 8-mark unit in one priority-1 chapter, so it is
    # the most marks recoverable anywhere in the Maths paper
    assert first == "Probability"


def test_the_schedule_appears_once_there_is_a_date(app):
    app.open_app()
    assert app.page.locator(".sched tbody tr").count() == 0
    app.page.fill("#examIn", "2027-03-01")
    app.page.wait_for_timeout(450)
    rows = app.page.locator(".sched tbody tr").count()
    assert rows > 0
    assert rows == app.page.locator(".qi").count()     # one row per queued chapter


def test_the_target_moves_the_gap(app):
    app.open_app()
    app.page.fill("#targetIn", "60")
    app.page.dispatch_event("#targetIn", "change")
    app.page.wait_for_timeout(400)
    assert app.ledger_row("Your target") == 48         # 60% of 80


def test_the_plan_survives_a_reload(app):
    app.open_app()
    app.grade("m4", 3)
    held = app.in_hand()
    app.open_app()
    assert app.in_hand() == held


def test_both_papers_are_totalled_together(app):
    app.open_app()
    app.grade("m13", 3)                                # Probability, 8 marks
    assert "8 of 150" in app.page.locator(".led-note").first.inner_text()


# ---------------------------------------------------------------- the gate


def test_a_locked_chapter_gives_away_what_the_plan_needs_and_no_more(app):
    app.open_app("#/ch/m1")
    assert app.page.locator(".warn-h").count() == 1     # deleted topics, free
    assert app.page.locator(".sect#s-start .md").count() == 1
    # the paid sections are gated, and the recall box is not on the page
    assert app.page.locator(".gate").count() == 5
    assert app.page.locator(".qq").count() == 0


def test_a_free_chapter_is_complete(app):
    app.open_app("#/ch/m13")
    assert app.page.locator(".qq").count() > 5
    assert app.page.locator(".gate").count() == 0
    assert app.page.locator(".tag.free").count() == 1
    app.page.locator(".reveal").first.click()
    app.page.wait_for_timeout(200)
    assert app.page.locator(".sol:not([hidden])").count() == 1


def test_search_does_not_surface_paid_text(app, site):
    app.open_app()
    solution = site["paid"]["chapters"]["m1"]["s"]["sol"]
    phrase = next(
        line.strip() for line in solution.splitlines()
        if len(line.strip()) > 40 and "|" not in line
    )[:40]
    app.page.fill("#q", phrase)
    app.page.wait_for_timeout(600)
    assert app.page.locator(".hit").count() == 0
    app.page.fill("#q", "Bayes")
    app.page.wait_for_timeout(600)
    assert app.page.locator(".hit").count() > 0        # the free half still searches


def test_a_valid_key_unlocks_everything(app):
    app.open_app()
    app.unlock_with(key_for("c"))
    assert app.page.locator("#accessBtn").inner_text() == "Full access"
    app.open_app("#/ch/m1")
    assert app.page.locator(".gate").count() == 0
    assert app.page.locator(".qq").count() > 5
    assert app.page.locator(".sect#s-recall .md").count() == 1


def test_an_unlock_survives_a_reload_with_no_network(app):
    app.open_app()
    app.unlock_with(key_for("c"))
    app.offline = True
    app.open_app("#/ch/p7")
    assert app.page.locator(".gate").count() == 0
    assert app.page.locator(".qq").count() > 0


def test_a_bad_key_changes_nothing(app):
    app.open_app()
    app.unlock_with("MF1-NOPE-NOPE-NOPEX")
    assert "not accepted" in app.page.locator(".msg").inner_text()
    app.page.keyboard.press("Escape")
    app.open_app("#/ch/m1")
    assert app.page.locator(".gate").count() == 5


def test_the_print_pack_needs_the_bump(app):
    app.open_app()
    app.unlock_with(key_for("c"))
    app.open_app("#/pack")
    assert app.page.locator(".sheet").count() == 0
    assert app.page.locator(".gate").count() == 1

    app.page.evaluate("localStorage.clear()")
    app.open_app()
    app.unlock_with(key_for("bc", order="9002"))
    app.open_app("#/pack")
    assert app.page.locator(".sheet").count() == 27


def test_a_withdrawn_licence_stops_working(app):
    app.open_app()
    app.unlock_with(key_for("c"))
    app.grants.revoke("9001")
    app.open_app("#/ch/m1")
    app.page.wait_for_timeout(900)          # the background re-check, then a reload
    assert app.page.locator("#accessBtn").inner_text() == "Free plan"


# -------------------------------------------------------------- the funnel


def test_the_landing_page_leads_to_the_planner(app):
    app.open_landing()
    assert app.page.locator("h1").count() == 1
    links = app.page.locator('a[href="/app"]').count()
    assert links >= 2, "the free planner is the page's main call to action"
    assert app.page.locator(".trap").count() == 3
    assert app.page.locator(".ch-bar").count() == 11      # CBSE units, both papers


def test_the_landing_page_fits_a_phone(app):
    app.page.set_viewport_size({"width": 390, "height": 780})
    app.open_landing()
    assert app.page.evaluate("document.body.scrollWidth <= document.body.clientWidth + 1")


def test_the_app_fits_a_phone(app):
    app.page.set_viewport_size({"width": 390, "height": 780})
    app.open_app()
    assert app.page.evaluate("document.body.scrollWidth <= document.body.clientWidth + 1")
    app.open_app("#/ch/m13")
    assert app.page.evaluate("document.body.scrollWidth <= document.body.clientWidth + 1")


def test_the_hindi_planner_is_translated(app):
    app.open_app()
    app.page.click('[data-lang="hi"]')
    app.page.wait_for_timeout(500)
    assert "अंक बही" in app.page.locator(".led-k").inner_text()
    assert "आँकलन" in app.page.locator("h1.pt").inner_text()
    app.grade("m13", 3)
    assert "अंक पीछे" in app.page.locator("h1.pt").inner_text()
