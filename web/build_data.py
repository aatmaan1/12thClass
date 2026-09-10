import json, os, re, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chapter metadata: (subject, num, slug, title, unit label, unit marks, priority)
M = "maths"; P = "physics"
CH = [
 (M, 1,"01-relations-and-functions","Relations and Functions","Unit I · Relations & Functions",8,2),
 (M, 2,"02-inverse-trigonometric-functions","Inverse Trigonometric Functions","Unit I · Relations & Functions",8,3),
 (M, 3,"03-matrices","Matrices","Unit II · Algebra",10,2),
 (M, 4,"04-determinants","Determinants","Unit II · Algebra",10,1),
 (M, 5,"05-continuity-and-differentiability","Continuity and Differentiability","Unit III · Calculus",35,1),
 (M, 6,"06-application-of-derivatives","Application of Derivatives","Unit III · Calculus",35,1),
 (M, 7,"07-integrals","Integrals","Unit III · Calculus",35,1),
 (M, 8,"08-application-of-integrals","Application of Integrals","Unit III · Calculus",35,2),
 (M, 9,"09-differential-equations","Differential Equations","Unit III · Calculus",35,1),
 (M,10,"10-vector-algebra","Vector Algebra","Unit IV · Vectors & 3D",14,1),
 (M,11,"11-three-dimensional-geometry","Three Dimensional Geometry","Unit IV · Vectors & 3D",14,1),
 (M,12,"12-linear-programming","Linear Programming","Unit V · Linear Programming",5,1),
 (M,13,"13-probability","Probability","Unit VI · Probability",8,1),
 (P, 1,"01-electric-charges-and-fields","Electric Charges and Fields","Units I+II · Electrostatics & Current",16,1),
 (P, 2,"02-electrostatic-potential-and-capacitance","Electrostatic Potential and Capacitance","Units I+II · Electrostatics & Current",16,1),
 (P, 3,"03-current-electricity","Current Electricity","Units I+II · Electrostatics & Current",16,1),
 (P, 4,"04-moving-charges-and-magnetism","Moving Charges and Magnetism","Units III+IV · Magnetism, EMI & AC",17,1),
 (P, 5,"05-magnetism-and-matter","Magnetism and Matter","Units III+IV · Magnetism, EMI & AC",17,3),
 (P, 6,"06-electromagnetic-induction","Electromagnetic Induction","Units III+IV · Magnetism, EMI & AC",17,1),
 (P, 7,"07-alternating-current","Alternating Current","Units III+IV · Magnetism, EMI & AC",17,1),
 (P, 8,"08-electromagnetic-waves","Electromagnetic Waves","Units V+VI · EM Waves & Optics",18,2),
 (P, 9,"09-ray-optics-and-optical-instruments","Ray Optics and Optical Instruments","Units V+VI · EM Waves & Optics",18,1),
 (P,10,"10-wave-optics","Wave Optics","Units V+VI · EM Waves & Optics",18,1),
 (P,11,"11-dual-nature-of-radiation-and-matter","Dual Nature of Radiation and Matter","Units VII+VIII · Modern Physics",12,1),
 (P,12,"12-atoms","Atoms","Units VII+VIII · Modern Physics",12,1),
 (P,13,"13-nuclei","Nuclei","Units VII+VIII · Modern Physics",12,1),
 (P,14,"14-semiconductor-electronics","Semiconductor Electronics","Unit IX · Electronic Devices",7,1),
]

SEC_KEYS = ["scope","brief","pyq","sol","test","tips"]

def split_sections(txt):
    """Split on '## N. ' headings, return list of 6 bodies."""
    parts = re.split(r'\n## [1-6]\. [^\n]*\n', "\n" + txt)
    # parts[0] is the preamble (title + weightage line)
    return parts[0], parts[1:7]

def sub(body, heading):
    """Extract a '### heading' block from a section body."""
    m = re.search(r'\n### ' + heading + r'[^\n]*\n(.*?)(?=\n### |\n## |\Z)', "\n" + body, re.S)
    if not m: return ""
    t = m.group(1).strip()
    return re.sub(r"\n*(?:-{3,}|\*{3,})\s*$", "", t).strip()

chapters = []
for subj, num, slug, title, unit, umarks, prio in CH:
    raw = io.open(os.path.join(ROOT, subj, slug + ".md"), encoding="utf-8").read()
    pre, secs = split_sections(raw)
    assert len(secs) == 6, (slug, len(secs))
    # weightage/appearance line = the bold line in the preamble
    ap = ""
    mm = re.search(r'^\*\*(.+?)\*\*\s*$', pre, re.M | re.S)
    if mm: ap = re.sub(r'\s+', ' ', mm.group(1)).strip()
    chapters.append({
        "id": subj[0] + str(num), "subj": subj, "num": num, "title": title,
        "unit": unit, "unitMarks": umarks, "prio": prio, "appear": ap,
        "deleted": sub(secs[0], "Deleted"),
        "recall": sub(secs[1], "Quick recall box"),
        "intro": sub(secs[1], "Start here"),
        "s": {k: secs[i].strip() for i, k in enumerate(SEC_KEYS)},
    })

DOCS = [
 ("blueprint","Exam Blueprint","docs/00-exam-blueprint.md","Paper design, unit weightage, the full deletion list, and how CBSE marking schemes award marks"),
 ("plan","Study Plans","docs/study-plan.md","Three plans by time remaining, plus the error-log habit"),
 ("answer","How to Answer","docs/how-to-answer.md","Answer templates for every question type in the paper"),
 ("pyqm","What Repeats · Maths","analysis/pyq-frequency-maths.md","Topic-by-topic frequency and P1/P2/P3 priorities"),
 ("pyqp","What Repeats · Physics","analysis/pyq-frequency-physics.md","Topic-by-topic frequency and P1/P2/P3 priorities"),
 ("pyqi","Reading the Frequency Tables","analysis/README.md","What the frequency bands mean, and the caveats"),
 ("fsm","Formula Sheet · Maths","maths/formula-sheet.md","Every in-syllabus formula, all 13 chapters"),
 ("fsp","Formula Sheet · Physics","physics/formula-sheet.md","Every in-syllabus formula, all 14 chapters, plus constants"),
 ("deriv","The 30 Derivations","physics/derivations-list.md","Ranked in tiers, with the step people miss, plus the 14 examinable graphs"),
]
docs = []
for did, dtitle, path, blurb in DOCS:
    body = io.open(os.path.join(ROOT, path), encoding="utf-8").read()
    body = re.sub(r'^# [^\n]*\n', '', body, count=1)  # drop the H1, the UI shows the title
    docs.append({"id": did, "title": dtitle, "blurb": blurb, "body": body.strip()})

out = {"chapters": chapters, "docs": docs}
js = json.dumps(out, ensure_ascii=False, separators=(",", ":"))
io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json"), "w", encoding="utf-8").write(js)

print("chapters:", len(chapters), " docs:", len(docs))
print("bundle bytes: %.2f MB" % (len(js.encode('utf-8'))/1048576))
print("chapters missing a recall box:", [c["id"] for c in chapters if not c["recall"]])
print("chapters missing a plain-English intro:", [c["id"] for c in chapters if not c["intro"]])
print("chapters missing a deleted block:", [c["id"] for c in chapters if not c["deleted"]])
print("chapters missing an appearance line:", [c["id"] for c in chapters if not c["appear"]])
print("total marks  maths:", sum({c['unit']:c['unitMarks'] for c in chapters if c['subj']=='maths'}.values()),
      " physics:", sum({c['unit']:c['unitMarks'] for c in chapters if c['subj']=='physics'}.values()))
