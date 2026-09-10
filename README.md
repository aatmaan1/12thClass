# Class 12 CBSE — Mathematics & Physics Study Guide

A complete, exam-first study system for **CBSE Class 12 Mathematics (Code 041)** and
**Physics (Code 042)**, built around what the board actually asks.

The notes in this repository are in English. The study site built from them
([`web/`](web/README.md)) also offers **हिन्दी** — the whole interface, all 27 chapter and unit
names in NCERT Hindi-medium terminology, and the plain-English *Start here* introduction for every
chapter. Hindi text lives under [`i18n/hi/`](i18n/hi/); the site says so wherever a section is
still English only.

Every chapter note follows the same six-part shape:

1. **Scope** — exactly what is in the syllabus, and what has been deleted (so no time is wasted).
2. **Brief** — opens with *Start here*, a plain-English explanation that assumes no prior
   knowledge, with links to a video lecture, Khan Academy, the NCERT chapter and (for Physics) the
   matching HC Verma sections. Then the concept compressed to what you need to answer questions.
3. **Previous years' questions** — real board question types, with the year(s) they appeared.
4. **Solutions** — full working, in the form an examiner expects.
5. **Test yourself** — a short diagnostic set with an answer key, to check understanding.
6. **Answering tips** — marking-scheme traps, per question type.

---

## Start here

| If you want to… | Read |
| --- | --- |
| Understand the exam before studying | [`docs/00-exam-blueprint.md`](docs/00-exam-blueprint.md) |
| Know what to study when | [`docs/study-plan.md`](docs/study-plan.md) |
| See which topics repeat most in Maths | [`analysis/pyq-frequency-maths.md`](analysis/pyq-frequency-maths.md) |
| See which topics repeat most in Physics | [`analysis/pyq-frequency-physics.md`](analysis/pyq-frequency-physics.md) |
| Learn how to write answers that score | [`docs/how-to-answer.md`](docs/how-to-answer.md) |
| Revise formulas the night before | [`maths/formula-sheet.md`](maths/formula-sheet.md) · [`physics/formula-sheet.md`](physics/formula-sheet.md) |

---

## Mathematics — 13 chapters, 80 marks

Full index and unit weightage: [`maths/README.md`](maths/README.md)

| # | Chapter | Unit (marks) |
| --- | --- | --- |
| 1 | [Relations and Functions](maths/01-relations-and-functions.md) | Relations & Functions (8) |
| 2 | [Inverse Trigonometric Functions](maths/02-inverse-trigonometric-functions.md) | Relations & Functions (8) |
| 3 | [Matrices](maths/03-matrices.md) | Algebra (10) |
| 4 | [Determinants](maths/04-determinants.md) | Algebra (10) |
| 5 | [Continuity and Differentiability](maths/05-continuity-and-differentiability.md) | Calculus (35) |
| 6 | [Application of Derivatives](maths/06-application-of-derivatives.md) | Calculus (35) |
| 7 | [Integrals](maths/07-integrals.md) | Calculus (35) |
| 8 | [Application of Integrals](maths/08-application-of-integrals.md) | Calculus (35) |
| 9 | [Differential Equations](maths/09-differential-equations.md) | Calculus (35) |
| 10 | [Vector Algebra](maths/10-vector-algebra.md) | Vectors & 3D (14) |
| 11 | [Three Dimensional Geometry](maths/11-three-dimensional-geometry.md) | Vectors & 3D (14) |
| 12 | [Linear Programming](maths/12-linear-programming.md) | LP (5) |
| 13 | [Probability](maths/13-probability.md) | Probability (8) |

## Physics — 14 chapters, 70 marks

Full index and unit weightage: [`physics/README.md`](physics/README.md)

| # | Chapter | Unit (marks) |
| --- | --- | --- |
| 1 | [Electric Charges and Fields](physics/01-electric-charges-and-fields.md) | I + II (16) |
| 2 | [Electrostatic Potential and Capacitance](physics/02-electrostatic-potential-and-capacitance.md) | I + II (16) |
| 3 | [Current Electricity](physics/03-current-electricity.md) | I + II (16) |
| 4 | [Moving Charges and Magnetism](physics/04-moving-charges-and-magnetism.md) | III + IV (17) |
| 5 | [Magnetism and Matter](physics/05-magnetism-and-matter.md) | III + IV (17) |
| 6 | [Electromagnetic Induction](physics/06-electromagnetic-induction.md) | III + IV (17) |
| 7 | [Alternating Current](physics/07-alternating-current.md) | III + IV (17) |
| 8 | [Electromagnetic Waves](physics/08-electromagnetic-waves.md) | V + VI (18) |
| 9 | [Ray Optics and Optical Instruments](physics/09-ray-optics-and-optical-instruments.md) | V + VI (18) |
| 10 | [Wave Optics](physics/10-wave-optics.md) | V + VI (18) |
| 11 | [Dual Nature of Radiation and Matter](physics/11-dual-nature-of-radiation-and-matter.md) | VII + VIII (12) |
| 12 | [Atoms](physics/12-atoms.md) | VII + VIII (12) |
| 13 | [Nuclei](physics/13-nuclei.md) | VII + VIII (12) |
| 14 | [Semiconductor Electronics](physics/14-semiconductor-electronics.md) | IX (7) |

Physics extras: [`physics/derivations-list.md`](physics/derivations-list.md) — the 30 derivations that
cover almost every 3- and 5-mark question, ranked by how often they are asked.

---

## How to use this repo with a student

**The 3-pass method.** Do not read a chapter once and move on.

- **Pass 1 (learn):** Read *Scope*, then *Brief* — the *Start here* part first, and the full detail
  only once that makes sense. Close the note. Reproduce the formula box on blank
  paper from memory. Anything you cannot reproduce, you have not learnt.
- **Pass 2 (apply):** Work the *Previous years' questions* with the solutions covered. Compare
  against the solution — not for the answer, but for the *steps*. CBSE pays for steps.
- **Pass 3 (test):** Do the *Test yourself* set under time (roughly 2 minutes per mark). Score it
  with the key. Below 70%? Go back to Pass 1 for the sub-topics you dropped.

**Track it.** Keep a one-line log per chapter: date of each pass, and the Pass 3 score. Chapters
whose score never crossed 80% are your revision list in February — nothing else is.

**Rule for numericals.** Every numerical gets written as: *formula → substitution with units →
answer with unit*. Three lines, always. Most numerical marks are lost by skipping the middle line.

---

## Notation used in these notes

Written in plain text so it reads correctly in any editor, on GitHub, and on a phone.

| Symbol | Means |
| --- | --- |
| `∫ f dx`, `∫[a,b] f dx` | indefinite / definite integral from a to b |
| `dy/dx`, `d²y/dx²` | first / second derivative |
| `a·b`, `a×b` | dot (scalar) product, cross (vector) product |
| `|a|` | magnitude of vector a, or modulus |
| `x^n`, `√x` | x to the power n, square root |
| `A⁻¹`, `Aᵀ`, `adj A` | inverse, transpose, adjoint of matrix A |
| `î, ĵ, k̂` | unit vectors along x, y, z |
| `→` | "implies" / "therefore" in working |
| `P(A|B)` | probability of A given B |

Vectors are written **bold** or with a hat for unit vectors; in your answer sheet always put the
arrow over the letter, since the marking scheme distinguishes vector from scalar answers.

---

## The paid edition

There is a commercial build of this guide, in the private `aatmaan1/sidehussle`
repository under `products/marks-first/`. It takes the notes here and adds a paywall, a
licence layer and a checkout funnel: the free site gives away the syllabus scope, the
deleted-topics warning and the plain-English introduction for all 27 chapters plus two
chapters in full, and the questions, solutions, self-tests, tips and reference documents are
sold as one payment.

**These notes remain the source of truth for the content.** The paid build holds a copy under
`products/marks-first/content/` and is regenerated from it, so a chapter edited here has to be
copied across and the build re-run before it reaches anyone who paid:

```bash
# from the sidehussle checkout, with 12thClass beside it
rsync -a --delete ../12thClass/{maths,physics,docs,analysis,i18n} products/marks-first/content/
python -m paywall.cli build products/marks-first
```

Editing an existing chapter needs nothing more than that. *Adding* one also means adding a row
to the chapter table in `products/marks-first/extract.py`, which is where the unit, the
weightage and the priority live on that side.

Nothing has been deployed and no payment has been processed. `Marks First` at the repository
root here stays free and complete, and is not affected by any of it.

---

## Sources for syllabus and pattern

Syllabus scope, unit weightage, deleted topics and question-paper design in these notes were checked
against the CBSE senior-secondary curriculum documents and 2025-26 sample papers:

- [CBSE Academic — curriculum & syllabus (cbseacademic.nic.in)](https://cbseacademic.nic.in/)
- [CBSE Class 12 Physics syllabus & unit weightage](https://testbook.com/cbse-class-12/physics-syllabus)
- [CBSE Class 12 Maths syllabus & unit weightage](https://testbook.com/cbse-class-12/maths-syllabus)
- [CBSE Class 12 Physics deleted topics](https://www.collegedekho.com/cbse-class-12-physics-deleted-syllabus-brd)
- [CBSE Class 12 Maths deleted topics](https://collegedunia.com/articles/e-704-cbse-class-12-maths-deleted-syllabus)
- [Physics sample paper 2025-26 structure](https://www.pw.live/school-prep/exams/cbse-sample-papers-class-12-physics)
- [Maths sample paper 2025-26 structure](https://www.pw.live/school-prep/exams/cbse-sample-papers-class-12-maths)

> **Verify before the exam.** CBSE republishes the syllabus and one sample paper per subject each
> year, usually around April and again with the sample papers. Download both from
> cbseacademic.nic.in at the start of the session and re-check the deleted-topics list against
> [`docs/00-exam-blueprint.md`](docs/00-exam-blueprint.md). Notes go stale; the board circular does not.
