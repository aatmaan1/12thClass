"""Parsing the question bank, the print pack, and the feasibility report.

The feasibility report exists to stop a promise being made that the content
cannot keep, so the arithmetic behind it is worth pinning: it is the reason
the ladder sells access and paper rather than mock papers.
"""

from __future__ import annotations

from paywall.packs import (
    PAPER_DESIGN,
    format_feasibility,
    paper_feasibility,
    questions,
    revision_pack,
)


def chapter(identifier="m1", subject="maths", pyq="", sol="", **kw):
    base = {
        "id": identifier, "subj": subject, "num": 1, "title": "Chapter",
        "unit": "Unit I", "unitMarks": 8, "appear": "every year",
        "deleted": "Nothing deleted.", "recall": "Recall box.",
        "s": {"scope": "", "brief": "", "pyq": pyq, "sol": sol, "test": "", "tips": ""},
    }
    base.update(kw)
    return base


def test_a_question_is_parsed_with_its_marks_and_its_solution():
    bundle = {"chapters": [chapter(
        pyq="**Q1.** *(3 marks)* Find the value.\n\n**Q2.** *(5 marks)* Prove it.",
        sol="### Q1\nThe working for one.\n\n### Q2\nThe working for two.",
    )]}
    bank = questions(bundle)
    assert [(q.number, q.marks, q.kind) for q in bank] == [
        ("1", 3, "plain"), ("2", 5, "plain")
    ]
    assert bank[0].solution == "The working for one."
    assert bank[1].solution == "The working for two."


def test_question_types_come_from_the_annotation():
    bundle = {"chapters": [chapter(pyq="\n\n".join([
        "**Q1.** *(1 mark, MCQ)* Which one?",
        "**Q2.** *(1 mark, Assertion–Reason)* Assertion and reason.",
        "**Q3.** *(4 marks, case study)* Read the passage.",
        "**Q4.** *(2 marks)* Straightforward.",
        "**Q5.** *(5 marks — the flagship question of this unit)* Derive it.",
    ]))]}
    assert [(q.marks, q.kind) for q in questions(bundle)] == [
        (1, "mcq"), (1, "assertion"), (4, "case"), (2, "plain"), (5, "plain")
    ]


def test_a_question_with_no_solution_still_parses():
    bundle = {"chapters": [chapter(pyq="**Q1.** *(2 marks)* Unanswered.", sol="")]}
    assert questions(bundle)[0].solution == ""


def test_an_empty_chapter_contributes_nothing():
    assert questions({"chapters": [chapter()]}) == []
    assert questions({}) == []


def test_the_print_pack_is_one_sheet_per_chapter():
    bundle = {"chapters": [chapter("m1"), chapter("p1", subject="physics")]}
    pack = revision_pack(bundle)
    assert [s["id"] for s in pack["sheets"]] == ["m1", "p1"]
    assert pack["sheets"][0]["recall"] == "Recall box."
    assert "new material" in pack["note"]


def test_a_chapter_with_no_recall_box_gets_no_sheet():
    """A sheet with nothing on it is a page with a title on it."""
    bundle = {"chapters": [chapter("m1", recall=""), chapter("m2")]}
    assert [s["id"] for s in revision_pack(bundle)["sheets"]] == ["m2"]


def test_feasibility_counts_the_bank_against_the_paper():
    """Enough two-markers for one Section B, and nothing else."""
    pyq = "\n\n".join(
        f"**Q{n}.** *(2 marks)* Question {n}." for n in range(1, 11)
    )
    bundle = {"chapters": [chapter(pyq=pyq)]}
    maths = next(r for r in paper_feasibility(bundle) if r.subject == "maths")
    section_b = next(s for s in maths.slots if s.section == "B")
    assert (section_b.needed, section_b.available, section_b.papers) == (5, 10, 2)
    assert maths.complete_papers == 0        # every other section is empty
    assert [s.section for s in maths.blocking][0] == "A"


def test_feasibility_is_reported_per_subject():
    reports = paper_feasibility({"chapters": []})
    assert {r.subject for r in reports} == set(PAPER_DESIGN)
    for report in reports:
        assert report.complete_papers == 0
        assert sum(s.needed * s.marks for s in report.slots) == report.paper_marks


def test_a_complete_paper_is_recognised():
    """One paper's worth of every slot, exactly."""
    design = PAPER_DESIGN["physics"]["slots"]
    blocks, number = [], 1
    annotations = {"mcq": "1 mark, MCQ", "assertion": "1 mark, Assertion–Reason",
                   "case": "4 marks, case study"}
    for _section, kind, marks, needed in design:
        for _ in range(needed):
            annotation = annotations.get(kind, f"{marks} marks")
            blocks.append(f"**Q{number}.** *({annotation})* Question {number}.")
            number += 1
    bundle = {"chapters": [chapter("p1", subject="physics", pyq="\n\n".join(blocks))]}
    physics = next(r for r in paper_feasibility(bundle) if r.subject == "physics")
    assert physics.complete_papers == 1
    assert physics.blocking == []


def test_the_report_reads_as_text():
    text = format_feasibility(paper_feasibility({"chapters": [chapter()]}))
    assert "maths" in text and "physics" in text
    assert "no complete paper" in text
