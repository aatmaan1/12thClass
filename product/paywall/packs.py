"""Artefacts built out of the content bundle, and one report about it.

Two different things live here on purpose.

**The revision pack** is a product: one printable page per chapter, carrying
the quick-recall box, the deleted-topics warning and how often the chapter has
appeared. It is the same content the core already contains, in a form the core
cannot give you — paper, on a desk, in the week when a phone is the enemy. It
is sold as exactly that and the copy says so; a bump that pretends to be new
material is a refund waiting to happen.

**The paper-feasibility report** is not a product. It counts the question bank
against the board's own paper design and says which sections could be filled.
It exists because the obvious upsell for a study product is "six full mock
papers", and this bank cannot honestly produce one: CBSE Maths Section A needs
eighteen MCQs and the bank holds twelve. So the report says so, the ladder
sells access instead of invented papers, and the gap is a content decision
someone can act on rather than a promise someone has to keep.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

#: `**Q7.** *(3 marks, case study — an aside)*` then the body.
_QUESTION = re.compile(r"^\*\*Q(\d+)\.\*\*\s*(?:\*\(([^)]*)\)\*)?\s*([\s\S]*)$")
_SOLUTION = re.compile(r"^### Q(\d+)\b[^\n]*\n?([\s\S]*)$")

#: The board's paper design, from docs/00-exam-blueprint.md. Slots are
#: (section, kind, marks each, how many).
PAPER_DESIGN: dict[str, dict[str, Any]] = {
    "maths": {
        "marks": 80, "minutes": 180,
        "slots": [
            ("A", "mcq", 1, 18), ("A", "assertion", 1, 2), ("B", "plain", 2, 5),
            ("C", "plain", 3, 6), ("D", "plain", 5, 4), ("E", "case", 4, 3),
        ],
    },
    "physics": {
        "marks": 70, "minutes": 180,
        "slots": [
            ("A", "mcq", 1, 12), ("A", "assertion", 1, 4), ("B", "plain", 2, 5),
            ("C", "plain", 3, 7), ("D", "case", 4, 2), ("E", "plain", 5, 3),
        ],
    },
}


@dataclass(frozen=True)
class Question:
    """One board question, as parsed out of a chapter."""

    chapter: str
    subject: str
    number: str
    marks: int
    kind: str
    annotation: str
    body: str
    solution: str


def questions(bundle: dict[str, Any]) -> list[Question]:
    """Every board question in the bundle, with its solution attached."""
    out: list[Question] = []
    for chapter in bundle.get("chapters") or []:
        sections = chapter.get("s") or {}
        solutions = _solutions(sections.get("sol") or "")
        for block in re.split(r"\n(?=\*\*Q\d+\.\*\*)", sections.get("pyq") or ""):
            match = _QUESTION.match(block.strip())
            if not match:
                continue
            number, annotation, body = match.group(1), match.group(2) or "", match.group(3)
            out.append(Question(
                chapter=str(chapter.get("id")),
                subject=str(chapter.get("subj")),
                number=number,
                marks=_marks(annotation),
                kind=_kind(annotation),
                annotation=annotation.strip(),
                body=body.strip(),
                solution=solutions.get(number, ""),
            ))
    return out


# ------------------------------------------------------------- the pack


def revision_pack(bundle: dict[str, Any]) -> dict[str, Any]:
    """One printable sheet per chapter.

    Ordered as the app orders chapters — Maths then Physics, by number —
    because a pack printed in a different order to the app it came from is a
    small, constant irritation.
    """
    sheets = []
    for chapter in bundle.get("chapters") or []:
        recall = (chapter.get("recall") or "").strip()
        if not recall:
            # A sheet with no recall box is a page with a title on it.
            continue
        sheets.append({
            "id": chapter.get("id"),
            "subj": chapter.get("subj"),
            "num": chapter.get("num"),
            "title": chapter.get("title"),
            "unit": chapter.get("unit"),
            "unitMarks": chapter.get("unitMarks"),
            "appear": chapter.get("appear") or "",
            "deleted": (chapter.get("deleted") or "").strip(),
            "recall": recall,
        })
    return {
        "sheets": sheets,
        "note": (
            "One page per chapter: the quick-recall box, what the board has "
            "deleted, and how often the chapter has appeared. Nothing here is "
            "new material — it is the recall boxes you already have, laid out "
            "to print and revise from on paper."
        ),
    }


# --------------------------------------------------- the feasibility report


@dataclass
class SlotReport:
    section: str
    kind: str
    marks: int
    needed: int
    available: int

    @property
    def papers(self) -> int:
        return self.available // self.needed if self.needed else 0

    @property
    def short_by(self) -> int:
        return max(self.needed - self.available, 0)


@dataclass
class SubjectFeasibility:
    subject: str
    paper_marks: int
    slots: list[SlotReport] = field(default_factory=list)
    total_questions: int = 0

    @property
    def complete_papers(self) -> int:
        return min((slot.papers for slot in self.slots), default=0)

    @property
    def blocking(self) -> list[SlotReport]:
        """Slots that cannot be filled even once, worst shortfall first."""
        return sorted(
            (s for s in self.slots if s.short_by), key=lambda s: -s.short_by
        )


def paper_feasibility(bundle: dict[str, Any]) -> list[SubjectFeasibility]:
    """How many complete board-format papers the question bank supports."""
    bank = questions(bundle)
    out: list[SubjectFeasibility] = []
    for subject, design in PAPER_DESIGN.items():
        subject_bank = [q for q in bank if q.subject == subject]
        report = SubjectFeasibility(
            subject=subject, paper_marks=int(design["marks"]),
            total_questions=len(subject_bank),
        )
        for section, kind, marks, needed in design["slots"]:
            available = len([
                q for q in subject_bank if q.kind == kind and q.marks == marks
            ])
            report.slots.append(SlotReport(section, kind, marks, needed, available))
        out.append(report)
    return out


def format_feasibility(reports: list[SubjectFeasibility]) -> str:
    """The report as text, for the build log and the notes."""
    lines: list[str] = []
    for report in reports:
        lines.append(
            f"\n{report.subject} — {report.total_questions} questions in the bank, "
            f"against a {report.paper_marks}-mark paper"
        )
        header = f"  {'section':<8} {'type':<10} {'marks':>5} {'needed':>7} {'have':>5} {'papers':>7}"
        lines.append(header)
        lines.append("  " + "-" * (len(header) - 2))
        for slot in report.slots:
            lines.append(
                f"  {slot.section:<8} {slot.kind:<10} {slot.marks:>5} {slot.needed:>7}"
                f" {slot.available:>5} {slot.papers:>7}"
            )
        if report.complete_papers:
            lines.append(f"  complete papers possible: {report.complete_papers}")
        else:
            short = ", ".join(
                f"{s.section}/{s.kind} short by {s.short_by}" for s in report.blocking
            )
            lines.append(f"  no complete paper: {short}")
    return "\n".join(lines)


# ----------------------------------------------------------------- parsing


def _solutions(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for block in text.split("\n### Q"):
        match = _SOLUTION.match("### Q" + block if not block.startswith("### Q") else block)
        if match:
            out[match.group(1)] = (match.group(2) or "").strip()
    return out


def _marks(annotation: str) -> int:
    match = re.search(r"(\d+)\s*marks?", annotation)
    return int(match.group(1)) if match else 0


def _kind(annotation: str) -> str:
    lowered = annotation.lower()
    if "assertion" in lowered:
        return "assertion"
    if "mcq" in lowered:
        return "mcq"
    if "case" in lowered:
        return "case"
    return "plain"
