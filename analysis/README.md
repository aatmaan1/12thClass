# PYQ Analysis — method and honest caveats

## What was analysed

The frequency tables in this folder describe recurring **question types** in the CBSE Class 12
board papers for Mathematics (041) and Physics (042) across roughly the last decade — the
2015 → 2025 window, including the multiple sets (Delhi / Outside Delhi / Compartment) that CBSE
issues each year, and the official sample paper for each session.

## How to read the frequency column

Every table has a **Freq** column with one of four bands:

| Band | Meaning | What to do |
| --- | --- | --- |
| **Every year** | Appeared in essentially every session, usually in every set | Must be automatic. Practise until you don't think. |
| **8–9/10** | Appeared in 8 or 9 of the last 10 sessions | Treat as compulsory. |
| **5–7/10** | Appeared about every other year | Learn it properly; don't drill it to death. |
| **2–4/10** | Occasional — often as an MCQ or a sub-part | Know the formula and the idea. Don't spend a week on it. |

The **Marks** column gives where the question type normally sits (1 / 2 / 3 / 4 / 5), which tells you
how deep to go. A "2–4/10, 1 mark" topic needs a formula and nothing more. A "every year, 5 marks"
topic needs the full derivation on demand.

## Caveats — read these

1. **These bands are pattern estimates, not a machine count.** They are built from the recurring
   structure of CBSE papers and marking schemes, not from an automated parse of PDF papers in this
   repo. Treat them as a well-informed prioritisation, not as a published statistic. If you want
   hard counts, download the last 10 years of papers from cbseacademic.nic.in and tally them
   yourself against these tables — that exercise is itself excellent revision, and any correction
   you find should be edited straight into these files.

2. **The syllabus was rationalised in 2023-24.** Papers from 2015–2022 contain questions on topics
   that are now deleted — planes in 3D Geometry, the Binomial distribution, potentiometer,
   transistors and logic gates, radioactivity, tangents and normals, and more. These tables cover
   only what is **still in the syllabus**; a deleted topic that used to appear every year is simply
   absent here. When you practise from an old paper, cross out the deleted questions first. The full
   deletion list is in [`../docs/00-exam-blueprint.md`](../docs/00-exam-blueprint.md) §3.

3. **Frequency is not the same as importance-per-hour.** A topic asked every year for 1 mark
   deserves less of your time than a topic asked every other year for 5. Read the Freq and Marks
   columns together. The "Priority" column in each table already combines them.

4. **High frequency is a floor, not a ceiling.** CBSE deliberately includes unfamiliar
   application-style questions each year, and the shift to competency-based questions has increased
   that. Never study *only* the high-frequency list — it gets you to about 65–70%, not beyond.

## Priority column

**P1** — highest return. Do these first, and do them completely.
**P2** — core. Needed for a good score.
**P3** — do after P1 and P2 are solid.

If you are on the 30-day plan, do P1 across both subjects and stop.

## Files

- [`pyq-frequency-maths.md`](pyq-frequency-maths.md)
- [`pyq-frequency-physics.md`](pyq-frequency-physics.md)
