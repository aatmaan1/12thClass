#!/usr/bin/env python3
"""Turn the markdown notes in this repository into one content bundle.

This is the product-specific half of the build: it knows that this product is
27 CBSE chapters with a six-part shape, which unit each belongs to and how
many marks that unit carries. Everything downstream — the free/paid split, the
packs, the paywalled app — is generic and lives in `paywall/`.

The notes are the repository, so the content paths are the repository root.
Nothing here writes to them: the build only reads.

The bundle it returns is the shape the study app consumes:

    {"chapters": [ ... ], "docs": [ ... ], "langs": { ... }}

One deliberate difference from the upstream 12thClass extractor: `s.brief`
here holds *only* the exam-language detail. The quick-recall box and the
plain-English "Start here" intro are lifted out into `recall` and `intro`, and
the brief keeps what is left. Upstream the app re-stripped them at render
time, which meant the three lived in one field and could not be priced apart.
The free tier gives away the intro and withholds the recall box, so they have
to be separate fields for the gate to reach them.
"""

from __future__ import annotations

import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
#: The notes live at the repository root — `maths/`, `physics/`, `docs/`,
#: `analysis/`, `i18n/` — and are the source of truth for every word of the
#: product. This directory holds only the things that sell them.
CONTENT = os.path.dirname(HERE)
#: Translations that belong to the product rather than to the notes — the
#: paywall, the funnel, the planner. Merged over the notes' own UI strings and
#: kept here, so the notes stay a study guide rather than half a shopfront.
OVERLAY = os.path.join(HERE, "i18n")

M, P = "maths", "physics"

#: (subject, number, file slug, title, unit label, unit marks, priority)
CH = [
    (M, 1, "01-relations-and-functions", "Relations and Functions", "Unit I · Relations & Functions", 8, 2),
    (M, 2, "02-inverse-trigonometric-functions", "Inverse Trigonometric Functions", "Unit I · Relations & Functions", 8, 3),
    (M, 3, "03-matrices", "Matrices", "Unit II · Algebra", 10, 2),
    (M, 4, "04-determinants", "Determinants", "Unit II · Algebra", 10, 1),
    (M, 5, "05-continuity-and-differentiability", "Continuity and Differentiability", "Unit III · Calculus", 35, 1),
    (M, 6, "06-application-of-derivatives", "Application of Derivatives", "Unit III · Calculus", 35, 1),
    (M, 7, "07-integrals", "Integrals", "Unit III · Calculus", 35, 1),
    (M, 8, "08-application-of-integrals", "Application of Integrals", "Unit III · Calculus", 35, 2),
    (M, 9, "09-differential-equations", "Differential Equations", "Unit III · Calculus", 35, 1),
    (M, 10, "10-vector-algebra", "Vector Algebra", "Unit IV · Vectors & 3D", 14, 1),
    (M, 11, "11-three-dimensional-geometry", "Three Dimensional Geometry", "Unit IV · Vectors & 3D", 14, 1),
    (M, 12, "12-linear-programming", "Linear Programming", "Unit V · Linear Programming", 5, 1),
    (M, 13, "13-probability", "Probability", "Unit VI · Probability", 8, 1),
    (P, 1, "01-electric-charges-and-fields", "Electric Charges and Fields", "Units I+II · Electrostatics & Current", 16, 1),
    (P, 2, "02-electrostatic-potential-and-capacitance", "Electrostatic Potential and Capacitance", "Units I+II · Electrostatics & Current", 16, 1),
    (P, 3, "03-current-electricity", "Current Electricity", "Units I+II · Electrostatics & Current", 16, 1),
    (P, 4, "04-moving-charges-and-magnetism", "Moving Charges and Magnetism", "Units III+IV · Magnetism, EMI & AC", 17, 1),
    (P, 5, "05-magnetism-and-matter", "Magnetism and Matter", "Units III+IV · Magnetism, EMI & AC", 17, 3),
    (P, 6, "06-electromagnetic-induction", "Electromagnetic Induction", "Units III+IV · Magnetism, EMI & AC", 17, 1),
    (P, 7, "07-alternating-current", "Alternating Current", "Units III+IV · Magnetism, EMI & AC", 17, 1),
    (P, 8, "08-electromagnetic-waves", "Electromagnetic Waves", "Units V+VI · EM Waves & Optics", 18, 2),
    (P, 9, "09-ray-optics-and-optical-instruments", "Ray Optics and Optical Instruments", "Units V+VI · EM Waves & Optics", 18, 1),
    (P, 10, "10-wave-optics", "Wave Optics", "Units V+VI · EM Waves & Optics", 18, 1),
    (P, 11, "11-dual-nature-of-radiation-and-matter", "Dual Nature of Radiation and Matter", "Units VII+VIII · Modern Physics", 12, 1),
    (P, 12, "12-atoms", "Atoms", "Units VII+VIII · Modern Physics", 12, 1),
    (P, 13, "13-nuclei", "Nuclei", "Units VII+VIII · Modern Physics", 12, 1),
    (P, 14, "14-semiconductor-electronics", "Semiconductor Electronics", "Unit IX · Electronic Devices", 7, 1),
]

SEC_KEYS = ["scope", "brief", "pyq", "sol", "test", "tips"]

DOCS = [
    ("blueprint", "Exam Blueprint", "docs/00-exam-blueprint.md",
     "Paper design, unit weightage, the full deletion list, and how CBSE marking schemes award marks"),
    ("plan", "Study Plans", "docs/study-plan.md",
     "Three plans by time remaining, plus the error-log habit"),
    ("answer", "How to Answer", "docs/how-to-answer.md",
     "Answer templates for every question type in the paper"),
    ("pyqm", "What Repeats · Maths", "analysis/pyq-frequency-maths.md",
     "Topic-by-topic frequency and P1/P2/P3 priorities"),
    ("pyqp", "What Repeats · Physics", "analysis/pyq-frequency-physics.md",
     "Topic-by-topic frequency and P1/P2/P3 priorities"),
    ("pyqi", "Reading the Frequency Tables", "analysis/README.md",
     "What the frequency bands mean, and the caveats"),
    ("fsm", "Formula Sheet · Maths", "maths/formula-sheet.md",
     "Every in-syllabus formula, all 13 chapters"),
    ("fsp", "Formula Sheet · Physics", "physics/formula-sheet.md",
     "Every in-syllabus formula, all 14 chapters, plus constants"),
    ("deriv", "The 30 Derivations", "physics/derivations-list.md",
     "Ranked in tiers, with the step people miss, plus the 14 examinable graphs"),
]


def split_sections(text: str) -> tuple[str, list[str]]:
    """Split a chapter on its `## N. ` headings into preamble + six bodies."""
    parts = re.split(r"\n## [1-6]\. [^\n]*\n", "\n" + text)
    return parts[0], parts[1:7]


def sub(body: str, heading: str) -> str:
    """Pull one `### heading` block out of a section body."""
    match = re.search(
        r"\n### " + heading + r"[^\n]*\n(.*?)(?=\n### |\n## |\Z)", "\n" + body, re.S
    )
    if not match:
        return ""
    return re.sub(r"\n*(?:-{3,}|\*{3,})\s*$", "", match.group(1).strip()).strip()


def drop(body: str, heading: str) -> str:
    """Remove one `### heading` block from a section body."""
    return re.sub(r"### " + heading + r"[\s\S]*?(?=\n### |$)", "", body)


def read(*parts: str) -> str:
    return io.open(os.path.join(CONTENT, *parts), encoding="utf-8").read()


def chapters() -> list[dict]:
    out = []
    for subj, num, slug, title, unit, unit_marks, prio in CH:
        raw = read(subj, slug + ".md")
        pre, secs = split_sections(raw)
        if len(secs) != 6:
            raise SystemExit(f"{slug}: expected 6 sections, found {len(secs)}")

        appear = ""
        line = re.search(r"^\*\*(.+?)\*\*\s*$", pre, re.M | re.S)
        if line:
            appear = re.sub(r"\s+", " ", line.group(1)).strip()

        # The brief keeps only the exam-language detail; the recall box and the
        # plain-English intro become fields of their own so the gate can price
        # them apart (the intro is free, the recall box is not).
        detail = drop(drop(secs[1], "Quick recall box"), "Start here")
        detail = re.sub(r"^\s*-{3,}\s*$", "", detail, flags=re.M).strip()

        sections = {key: secs[i].strip() for i, key in enumerate(SEC_KEYS)}
        sections["scope"] = re.sub(
            r"### Deleted[\s\S]*?(?=\n### |$)", "", sections["scope"]
        ).strip()
        sections["brief"] = detail

        out.append({
            "id": subj[0] + str(num), "subj": subj, "num": num, "title": title,
            "unit": unit, "unitMarks": unit_marks, "prio": prio, "appear": appear,
            "deleted": sub(secs[0], "Deleted"),
            "recall": sub(secs[1], "Quick recall box"),
            "intro": sub(secs[1], "Start here"),
            "s": sections,
        })
    return out


def docs() -> list[dict]:
    out = []
    for doc_id, title, path, blurb in DOCS:
        body = read(*path.split("/"))
        body = re.sub(r"^# [^\n]*\n", "", body, count=1)  # the UI supplies the title
        out.append({"id": doc_id, "title": title, "blurb": blurb, "body": body.strip()})
    return out


def translated_qa(directory: str, lang: str, chapter_list: list[dict]) -> list[str]:
    """Attach a language's board questions and solutions to their chapters.

    One file per chapter, split by two machine markers so the headings never
    reach a reader. The question numbering must survive translation, because
    each question is paired with its solution by that number — a mismatch is a
    build failure rather than a page that quietly shows the wrong working.

    These are attached to the **chapter**, not to the language pack, and that
    is the whole point: questions and solutions are the paid half of this
    product in any language. On the chapter they pass through the same gate as
    the English, so a locked chapter withholds its Hindi solutions and a free
    sample hands them over. In the language pack — which ships whole, because
    an interface is not the product — they would be a straight leak.
    """
    missing = []
    for chapter in chapter_list:
        path = os.path.join(directory, "qa", "%s%02d.md" % (chapter["id"][0], chapter["num"]))
        if not os.path.exists(path):
            missing.append(chapter["id"])
            continue
        text = io.open(path, encoding="utf-8").read()
        split = re.search(r"<!--\s*QUESTIONS\s*-->(.*?)<!--\s*SOLUTIONS\s*-->(.*)$", text, re.S)
        if not split:
            raise SystemExit(
                f"{path}: needs both <!-- QUESTIONS --> and <!-- SOLUTIONS --> markers"
            )
        pyq, sol = split.group(1).strip(), split.group(2).strip()

        want = re.findall(r"^\*\*Q(\d+)\.\*\*", chapter["s"]["pyq"], re.M)
        got = re.findall(r"^\*\*Q(\d+)\.\*\*", pyq, re.M)
        if got != want:
            raise SystemExit(
                f"{path}: question numbers {got} do not match the English {want}"
            )
        got_sol = re.findall(r"^### Q(\d+)\b", sol, re.M)
        if got_sol != want:
            raise SystemExit(
                f"{path}: solution numbers {got_sol} do not match the questions {want}"
            )
        chapter.setdefault("tr", {})[lang] = {"pyq": pyq, "sol": sol}
    return missing


def langs(chapter_list: list[dict], doc_list: list[dict]) -> dict:
    """Fold in every translation under `content/i18n/`.

    A language missing a chapter name, a unit name or a document name fails the
    build: a half-wired language would ship as English with a Hindi shell. A
    missing chapter intro is allowed and falls back to English.
    """
    root = os.path.join(CONTENT, "i18n")
    out: dict[str, dict] = {}
    if not os.path.isdir(root):
        return out

    for lang in sorted(os.listdir(root)):
        directory = os.path.join(root, lang)
        if not os.path.isdir(directory):
            continue
        ui = json.load(io.open(os.path.join(directory, "ui.json"), encoding="utf-8"))
        overlay_file = os.path.join(OVERLAY, lang, "ui.json")
        overlaid = 0
        if os.path.exists(overlay_file):
            extra = json.load(io.open(overlay_file, encoding="utf-8"))
            extra.pop("_note", None)
            # The overlay wins: where both define a string, the product's
            # wording is the one that was written against this funnel.
            ui.update(extra)
            overlaid = len(extra)
        ui.pop("_note", None)
        titles = ui.pop("chapters", {})
        units = ui.pop("units", {})
        docnames = ui.pop("docs", {})

        intros, missing = {}, []
        for chapter in chapter_list:
            path = os.path.join(
                directory, "chapters", "%s%02d.md" % (chapter["id"][0], chapter["num"])
            )
            if os.path.exists(path):
                text = io.open(path, encoding="utf-8").read()
                intros[chapter["id"]] = re.sub(r"^\s*###[^\n]*\n", "", text).strip()
            else:
                missing.append(chapter["id"])

        for chapter in chapter_list:
            if chapter["id"] not in titles:
                raise SystemExit(f"{lang}: no chapter name for {chapter['id']}")
            if chapter["unit"] not in units:
                raise SystemExit(f"{lang}: no unit name for {chapter['unit']}")
        for doc in doc_list:
            if doc["id"] not in docnames:
                raise SystemExit(f"{lang}: no document name for {doc['id']}")

        no_qa = translated_qa(directory, lang, chapter_list)
        out[lang] = {"ui": ui, "titles": titles, "units": units, "docs": docnames,
                     "intros": intros}
        print("  %s: %d ui strings (%d of them the product's own), %d chapter "
              "names, %d intros, %d Q&A sets%s%s"
              % (lang, len(ui), overlaid, len(titles), len(intros),
                 len(chapter_list) - len(no_qa),
                 ("  no intro for: " + ",".join(missing)) if missing else "",
                 ("  no Q&A for: " + ",".join(no_qa)) if no_qa else ""))
    return out


def bundle() -> dict:
    """The whole content bundle, before any gating."""
    chapter_list = chapters()
    doc_list = docs()
    return {
        "chapters": chapter_list,
        "docs": doc_list,
        "langs": langs(chapter_list, doc_list),
    }


if __name__ == "__main__":
    data = bundle()
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    print("chapters %d  docs %d  languages %d  %.2f MB"
          % (len(data["chapters"]), len(data["docs"]), len(data["langs"]),
             len(blob.encode("utf-8")) / 1048576))
    for field in ("recall", "intro", "deleted", "appear"):
        blank = [c["id"] for c in data["chapters"] if not c[field]]
        if blank:
            print(f"  chapters with no {field}: {blank}")
