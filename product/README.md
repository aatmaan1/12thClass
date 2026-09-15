# The product

This directory turns the notes at the repository root into a site that can be
sold. The notes are the source of truth and nothing here writes to them.

```bash
python3 product/build.py          # then commit what changed
```

It writes `index.html`, `app.html`, `thanks.html` and `api/` at the repository
root, all generated and all committed, because the host builds nothing: Vercel
serves this repository root as a static site and picks up `api/*.py` as Python
functions on its own.

## The one idea

**Marks First is a planner, not a notes app.**

The old site was 27 chapters behind six tabs. It was a good reference and a bad
product, because it answered the question a textbook answers — *what is in this
chapter* — and not the question a candidate with four months actually has:
**where are my missing marks, and which chapters hold them?**

So the arithmetic is the product now. CBSE publishes marks per unit; each
chapter carries its unit's marks split between the chapters in that unit. You
grade each chapter 0–3, and the page works out:

- **marks in hand** — the stake you have secured, totalled down the margin the
  way an examiner totals a script
- **the gap** — how far that is from your target
- **the queue** — the chapters that hold the gap, ranked by marks recoverable
  and weighted by how reliably the board asks them, cut where the running
  total closes it
- **a schedule** — those chapters spread over the days to your exam, with a
  fifth held back for revision

It is a plan, not a prediction, and the page says so. The even split within a
unit is the honest assumption: the board does not publish a finer one, and
inventing one would be inventing precision.

## Why that changes the funnel

The planner needs only metadata — unit, weightage, priority, frequency — so
**the whole diagnosis can be free** for all 27 chapters, in both languages,
with no account. What is sold is the material that closes the gap it just
showed you.

That is a better offer than a few sample chapters and a more honest one: nobody
is asked to guess whether this would help before seeing exactly what it would
do. It is also the sharpest version of "give away the diagnosis, sell the cure"
that this content supports.

Free, permanently: the planner, the syllabus scope and deleted-topics warning
for every chapter, the plain-English opening to each, the exam blueprint, the
frequency-band explainer, and Probability and Semiconductor Electronics end to
end. Sold: the exam-language detail, the recall boxes, all 332 questions, every
solution, the self-tests and keys, the answering tips, both formula sheets, the
derivations and the frequency analyses.

## The chapter page, reordered

One scrolling page per chapter instead of six tabs, in the order the marks are
in rather than the order a textbook is written in:

1. **Start here** — plain English, free
2. **What the examiner pays for** — the marking-scheme traps
3. **Board questions** — solution hidden until you ask
4. **Self-test** — answer key behind a reveal
5. **Quick recall** — for the third pass
6. **The full detail** — exam language
7. **Scope** — what is in, what has been cut

The old order opened with the syllabus and finished with the marking scheme.
Marks are awarded for named steps, so the marking scheme goes near the top.

## The design

It comes from the thing being sold — a CBSE answer script:

- paper is the cool grey-green of an Indian examination form, not cream
- one deep institutional teal carries every action
- **red is spent only on marks still at risk** — the examiner's pen, not decoration
- green means marks in hand
- a **left margin totals marks** the way an examiner totals a script, and every
  number that is a mark is set in mono, because marks line up in a margin

Faustina for headings (a printed question paper is set in a serif), Archivo for
running text, DM Mono for marks and labels, Noto Devanagari for Hindi. Tokens
live in `tokens.py` because the landing page and the app share them.

## Layout

```
build.py           the whole build: notes in, deployable site out
extract.py         the markdown -> one content bundle (the chapter table lives here)
product.yaml       what is free, what is sold, what each rung unlocks
ladder.yaml        the four prices
copy.yaml          the landing page's words, and the store's ids
landing.py         the landing page
tokens.py          the palette and the type, shared by both pages
i18n/hi/ui.json    the site's own Hindi — every interface string
app/app.src.html   the app's markup and CSS
app/js/*.js        the app, in parts: model, planner, chapter, paywall, shell, i18n
paywall/           the gate, the licence layer and the endpoints
storefront/        the ladder arithmetic, the provider adapters, the webhook
tests/             200 tests, including a browser checking the marks arithmetic
```

`paywall/` and `storefront/` came from the `aatmaan1/sidehussle` framework,
where the reasoning behind them is written down. They are a vendored copy here,
not a dependency: the build has to run from one checkout with nothing
installed, and the functions under `api/` are built the same way.

## Tests

```bash
python3 -m pytest product/tests -q
```

No network. The browser tests drive the committed `app.html` with the real
unlock endpoint answering in-process, and check the marks arithmetic against
the unit weightage worked out independently — a test that read the numbers back
off the page would only agree with a bug.

## Deploying

`api/README.md` (written by the build) has the environment variables. To simply
look at the funnel, two are enough:

```
PAYWALL_SECRET   any long random string
PAYWALL_DEMO     1
```

`PAYWALL_DEMO` relaxes nothing about who is let in — signatures are still
verified. It keeps the little state there is in memory, per instance, which is
why a deployment with it set cannot sell: device counts reset when the host
recycles, and the thank-you page cannot hand over a key.

## Caveats

- **No payment has been processed and nothing is deployed.** The provider
  integrations, the serverless handler shape, the environment variable names
  and the key-value protocol are built from documentation.
- ₹499 is a guess. Price is the real unknown, and the test for it is a pre-sell
  page ranking prices on revenue per visitor, not conversion rate.
- The planner's grade-to-marks mapping is linear and the split within a unit is
  even. Both are assumptions stated on the page rather than findings.
- **This repository is public**, so the paid content is readable on GitHub
  whatever the site does. Make it private before charging, or be explicit that
  the gate only stops casual copying.
