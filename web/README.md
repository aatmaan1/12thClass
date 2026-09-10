# Marks First — the study site

A single-page study app built from the markdown notes in this repository. It is a **static site**:
one HTML file, no framework, no build step on the server, no dependencies to install.

- **`../index.html`** — the deployable site, at the **repository root**. Generated; do not edit by
  hand. It sits at the root because Vercel serves a repository root as a static site with no
  configuration at all — no rewrites to misfire.
- **`app.src.html`** — the app template (markup, CSS, JS). Edit this. English UI strings live in
  the `EN` object near the top of its script.
- **`build_data.py`** — extracts the chapters and reference docs from the markdown into `data.json`,
  and folds in every translation under `../i18n/`.
- **`build.py`** — runs the extractor, bundles the data into the template, writes `index.html`.
- **`data.json`** — generated content bundle.

---

## Deploy to Vercel

Vercel's Git integration deploys this automatically. You need to do the import once; after that
every push to `main` redeploys on its own.

> **Import it into your personal account**, not into a team.
> Vercel's importer remembers the last scope you used, so it may pre-select a team such as
> `chair-talks`. Change the scope to **`aatmaan108-gmailcoms-projects`** before you click Deploy.

1. Go to **[vercel.com/new](https://vercel.com/new)**.
2. At the top of the page, set the **Vercel Scope** to your personal account —
   **`aatmaan108-gmailcoms-projects`**. Check this before anything else.
3. Under *Import Git Repository*, choose **`aatmaan1/12thClass`**. If it isn't listed, click
   *Adjust GitHub App Permissions* and grant access to the repository.
4. Leave every build setting at its default:
   - Framework Preset — **Other**
   - Root Directory — **`./`** (the repository root)
   - Build Command — **empty**
   - Output Directory — **empty**
   - Install Command — **empty**

   `index.html` is at the repository root, so Vercel serves it at `/` with no routing
   configuration. The `vercel.json` at the root only sets a few response headers.
5. Click **Deploy**. It takes well under a minute — there is nothing to compile.

You will get a URL like `https://12thclass.vercel.app`. Add a custom domain from the project's
*Settings → Domains* if you want one.

### If the deployed page shows a 404

Check, in order:

1. **Is `index.html` on the branch Vercel is deploying?** Vercel deploys `main` as production.
   Confirm `index.html` exists at the root of `main`.
2. **Is Root Directory set to `./`?** If it points at `web`, Vercel looks for `web/index.html`,
   which no longer exists.
3. **Do not add `rewrites` to `vercel.json`.** An earlier version served the page from
   `web/index.html` via a rewrite and 404'd on the live deployment — `cleanUrls` strips the `.html`
   from the rewrite *destination*, so it resolved to nothing. Serving from the root avoids the whole
   problem.

---

## Rebuild after editing the notes

The content is compiled into `index.html` at build time, so editing a chapter's markdown does not
change the site until you rebuild:

```bash
python3 web/build.py
git add index.html web/data.json
git commit -m "Rebuild study site"
git push
```

Vercel redeploys on the push. `build.py` needs only Python 3 — no packages.

It also fails loudly rather than shipping a broken page: it checks that the content placeholder was
replaced, that no stray control characters survive, that the `<script>` tags balance, and it prints
the chapter, document and question counts so you can see the content actually made it in.

### Editing the app itself

Edit `app.src.html`, then run `python3 web/build.py`. To preview locally:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

Open it as a `file://` URL and it works too — there is nothing that needs a server.

---

## What the site does

| Feature | Why |
| --- | --- |
| Six tabs per chapter — Scope, Brief, Questions, Solutions, Self-test, Tips | The notes' six-part structure *is* the navigation |
| Brief opens with **Start here** — plain English, no prior knowledge assumed, plus links out to a video lecture, Khan Academy, the NCERT chapter and the matching HC Verma sections | Formulae are useless to someone who does not yet know what the thing *is* |
| The quick-recall box is **collapsed** by default | It is a revision aid; on a first read it is noise |
| 332 board questions, each with the solution behind a **Show solution** toggle | Lets you attempt on paper first. Reading a solution you did not attempt teaches nothing |
| Answer keys hidden behind a reveal | Makes the self-tests work as tests |
| Progress counted in **marks**, not chapters | Marks are the only unit the board pays in |
| Three-pass tracking per chapter (Learn / Apply / Test) plus a score box | The revision method from `docs/study-plan.md`, built in |
| "Study these next", ranked by priority then marks at stake | Removes the daily decision about what to open |
| Deleted topics as a red banner at the top of every chapter | The highest-value warning in the whole guide |
| Search across all 27 chapters and 9 reference documents | Press `/` to focus it |
| Light and dark themes, both designed | Follows the OS, with a manual override |
| **English / हिन्दी** switch at the top right | Hindi-medium candidates sit the same paper |

---

## Languages

The switch at the top right offers **English** and **हिन्दी**. The choice is remembered per device
(`localStorage`), and sets `<html lang>` so the right font and line-height apply.

**Hindi is a partial translation, on purpose.** Translated:

- the whole interface — tabs, labels, buttons, the dashboard, the search results
- every chapter and unit name, and every reference document's title and blurb, using the
  terminology of the **NCERT Hindi-medium textbooks** (`lhph*`, `lhmh*`) rather than literal
  translation — so आव्यूह, सारणिक, विभव, धारिता, अपवाह वेग, ह्रासी क्षेत्र
- the **Start here** plain-English introduction for all 27 chapters, with the Hindi NCERT chapter
  PDFs linked in place of the English ones

Still English: the exam-language detail under *The full detail*, the board questions, the solutions,
the self-tests, the answering tips, and the nine reference documents. Wherever that happens the app
shows a notice in Hindi saying so, rather than pretending otherwise. Anything with no translation
falls back to English silently.

### Adding to the Hindi translation, or adding a language

Everything lives under `i18n/<code>/`:

```
i18n/hi/ui.json            every UI string, plus chapter names, unit names, document names
i18n/hi/chapters/p01.md    the "Start here" text for Physics ch 1 — same shape as the English
i18n/hi/chapters/m13.md    ... and Maths ch 13
```

Add a directory with the same two pieces and it appears in the switch on the next build, named by
its own `lang.name`. `build_data.py` **fails the build** if a language is missing a chapter name, a
unit name or a document name, so a half-wired language cannot ship; a missing chapter intro is
allowed and falls back to English.

---

**Progress is stored in the browser** (`localStorage`), per device. It is not sent anywhere and
there is no account. Clearing site data clears it. On a phone and a laptop you will have two
separate records — that is the trade-off for having no login.

---

## Caveats that travel with the content

These are stated in the app itself as well, and they are not softened by the nicer packaging:

- The PYQ frequency bands ("every year", "8–9/10") are **well-informed pattern estimates, not a
  machine count** of past papers.
- Two scope points are **flagged rather than asserted**: polarisation in Wave Optics, and the
  magnetic-materials block in Physics Ch 5.
- Check the deletion lists against the current CBSE syllabus PDF at
  [cbseacademic.nic.in](https://cbseacademic.nic.in/) at the start of the session. Notes go stale;
  the board circular does not.
