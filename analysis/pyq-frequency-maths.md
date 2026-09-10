# Mathematics (041) — What Actually Gets Asked

Read [`README.md`](README.md) in this folder for how the Freq and Priority bands are defined and what
they are and are not.

Only **current-syllabus** topics appear here. Deleted topics (composite/invertible functions, inverse
trig identities, tangents & normals, area between two curves, planes in 3D, Binomial distribution,
and the rest) are listed in [`../docs/00-exam-blueprint.md`](../docs/00-exam-blueprint.md) §3.

---

## The 60-mark core

If you learn nothing else, learn these fourteen question types. Together they have historically
covered around 60 of 80 marks.

| # | Question type | Chapter | Marks | Freq |
| --- | --- | --- | --- | --- |
| 1 | Solve 3 linear equations by matrix method (X = A⁻¹B) | 4 | 5 | Every year |
| 2 | Integration by partial fractions | 7 | 3–5 | Every year |
| 3 | Bayes' theorem word problem | 13 | 4–5 | Every year |
| 4 | Linear differential equation, dy/dx + Py = Q | 9 | 3–5 | Every year |
| 5 | Maxima–minima word problem | 6 | 4–5 | Every year |
| 6 | Shortest distance between two skew lines | 11 | 3–5 | 9/10 |
| 7 | Continuity at a point — find k | 5 | 2–3 | Every year |
| 8 | Definite integral using the f(x) → f(a−x) property | 7 | 3 | 9/10 |
| 9 | Linear programming, graphical, corner-point | 12 | 4–5 | Every year |
| 10 | Area bounded by a line and a circle/parabola | 8 | 5 | 8/10 |
| 11 | Prove a relation is an equivalence relation | 1 | 2–3 | 8/10 |
| 12 | Projection / angle / area using dot and cross product | 10 | 2–3 | Every year |
| 13 | Logarithmic or implicit differentiation | 5 | 3 | Every year |
| 14 | Integration by parts (ILATE) | 7 | 3 | Every year |

---

## Unit I — Relations and Functions (8 marks)

### Ch 1. Relations and Functions

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Check reflexive / symmetric / transitive for a given relation | 2–3 | Every year | **P1** |
| Prove a relation is an equivalence relation; find an equivalence class | 3–5 | 8/10 | **P1** |
| Prove a function is one-one and onto (bijective) | 3–5 | 7/10 | **P1** |
| Counting: number of relations / functions / one-one functions on a small set | 1 | 7/10 | P2 |
| Identify from a graph or arrow diagram whether a function is injective/surjective | 1 | 5/10 | P2 |
| Modify domain/codomain to make a function bijective | 1–2 | 4/10 | P3 |

**Pattern note.** After the deletion of composition and invertible functions, this chapter shrank
sharply. What remains is highly stereotyped: a relation defined by "a − b is divisible by n", or
"|a − b| is even", or on a set of triangles/lines, and you must classify it. And a function like
f(x) = (4x+3)/(6x−4) or f(x) = x² on a restricted domain, to be shown bijective.

**The trap.** For *transitive*, students test one example and declare it transitive. Transitivity
must be argued in general — take arbitrary (a,b) and (b,c) in R and show (a,c) ∈ R. For a *counter*
example, one concrete pair is enough and that asymmetry is exactly what CBSE tests.

### Ch 2. Inverse Trigonometric Functions

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Principal value of sin⁻¹ / cos⁻¹ / tan⁻¹ of a given number | 1–2 | Every year | **P1** |
| Domain and range (principal value branch) of an inverse trig function | 1 | Every year | **P1** |
| Evaluate a composite like sin(cos⁻¹ x), tan(sin⁻¹ x) | 1–2 | 7/10 | P2 |
| Evaluate sin⁻¹(sin θ) / cos⁻¹(cos θ) where θ is *outside* the principal branch | 1–2 | 8/10 | **P1** |
| Sum/simplify two inverse trig terms | 2 | 4/10 | P3 |

**Pattern note.** Now almost entirely a Section-A chapter. The single most-asked idea is
sin⁻¹(sin θ) for θ outside [−π/2, π/2] — e.g. sin⁻¹(sin(3π/4)) = π/4, not 3π/4. It appears as an
MCQ nearly every year because it separates students who memorised "they cancel" from students who
know the range.

---

## Unit II — Algebra (10 marks)

### Ch 3. Matrices

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Find unknowns from a matrix equation (equate corresponding elements) | 1–2 | Every year | **P1** |
| Symmetric / skew-symmetric: identify, or express A as sum of both | 2–3 | 8/10 | **P1** |
| Compute AB, verify (AB)ᵀ = BᵀAᵀ | 2 | 7/10 | P2 |
| Order of a matrix / number of elements / number of possible matrices | 1 | 8/10 | P2 |
| A² = A or A² = I type: find the matrix or a scalar | 2–3 | 6/10 | P2 |
| Diagonal elements of a skew-symmetric matrix are zero (as MCQ/AR) | 1 | 6/10 | P2 |
| Transpose and its properties | 1–2 | 6/10 | P2 |

**Pattern note.** With elementary row operations deleted, matrix inversion moved fully into
Determinants (via adjoint). What is left in Ch 3 is arithmetic and the symmetric/skew-symmetric
structure — quick marks, and often in Section A or B.

### Ch 4. Determinants

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Solve a system of 3 equations by matrix method | 5 | Every year | **P1** |
| Find A⁻¹ using adj A for a 3×3 matrix | 3–5 | Every year | **P1** |
| Verify A(adj A) = |A|I | 2–3 | 6/10 | P2 |
| |kA| = kⁿ|A|, |adj A| = |A|ⁿ⁻¹, |A⁻¹| = 1/|A| | 1 | Every year | **P1** |
| Area of a triangle / collinearity of three points by determinant | 1–2 | 7/10 | P2 |
| Value of x from a given determinant equation | 1–2 | 7/10 | P2 |
| Consistency / inconsistency of a system from |A| and (adj A)B | 1–3 | 5/10 | P2 |
| Cofactor / minor of a specific element | 1 | 6/10 | P2 |

**Pattern note.** This is the most reliable 5-mark question in the entire paper. The system-of-three-
equations question has appeared in essentially every session for a decade, sometimes dressed as a
word problem (three people buying three items; award money split three ways). The dressing changes;
the method never does.

**The trap.** Students compute adj A but forget it is the transpose of the cofactor matrix, and skip
the transpose step. Also: the sign pattern `+ − + / − + − / + − +` for cofactors. Both cost the whole
question.

---

## Unit III — Calculus (35 marks) — the half of the paper

### Ch 5. Continuity and Differentiability

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Find k / a / b so a piecewise function is continuous at a point | 2–3 | Every year | **P1** |
| Logarithmic differentiation — y = xˣ, xʸ = yˣ, y = (f)^(g) | 3 | Every year | **P1** |
| Implicit differentiation | 2–3 | Every year | **P1** |
| Parametric differentiation (x = f(t), y = g(t)) | 2–3 | 8/10 | **P1** |
| Second-order derivative; prove a relation like (1−x²)y″ − xy′ − a²y = 0 | 3–5 | 8/10 | **P1** |
| Differentiability at a point / continuity ⇏ differentiability | 1–2 | 7/10 | P2 |
| Chain rule on a composite of 3 functions | 2 | Every year | **P1** |
| Continuity of |x|, [x] (greatest integer), and similar | 1 | 6/10 | P2 |
| Derivative of inverse trig composites, e.g. d/dx tan⁻¹((1−x)/(1+x)) | 3 | 6/10 | P2 |

**Pattern note.** Rolle's and Mean Value Theorem are deleted, which removed the one "theory" question
from this chapter. It is now purely mechanical — and therefore fully learnable. The
`prove (1−x²)y″ − xy′ = a²y` family (from y = (sin⁻¹x)² or y = e^(a sin⁻¹x)) recurs constantly as a
5- or 3-marker.

### Ch 6. Application of Derivatives

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Maxima/minima word problem (volume, area, cost, distance, cone in sphere) | 4–5 | Every year | **P1** |
| Find intervals where f is strictly increasing / decreasing | 3 | Every year | **P1** |
| Show f is increasing/decreasing on a given interval | 2–3 | 8/10 | **P1** |
| Absolute maximum and minimum on a closed interval | 3 | 6/10 | P2 |
| Local maxima/minima by first or second derivative test | 2–3 | 8/10 | **P1** |
| Simple rate of change (radius, area, volume w.r.t. time) | 2 | 6/10 | P2 |
| Case-study framed optimisation | 4 | 7/10 | **P1** |

**Pattern note.** With tangents/normals and approximations deleted, this chapter is now *only*
monotonicity and optimisation. That concentration makes it very high-return: two question types
covering the whole chapter.

The recurring optimisation problems, almost verbatim across years: largest cone inscribed in a
sphere; cylinder of maximum volume in a sphere/cone; open box from a square sheet with corners cut;
window as rectangle + semicircle with fixed perimeter; wire of given length cut into a square and a
circle; shortest distance from a point to a curve; two posts and a wire. Learn these seven and you
have seen the question.

**The trap.** Not verifying it is a maximum. Write the second-derivative test (or a sign table)
explicitly — that is a full mark. Also: answering with the *variable* value when the question asked
for the maximum *volume*.

### Ch 7. Integrals — the single biggest chapter in the paper

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Partial fractions | 3–5 | Every year | **P1** |
| Integration by parts (ILATE), incl. ∫eˣ(f + f′)dx | 3 | Every year | **P1** |
| Substitution | 2–3 | Every year | **P1** |
| Definite integral via ∫[0,a] f(x)dx = ∫[0,a] f(a−x)dx | 3 | 9/10 | **P1** |
| 1/(ax²+bx+c) or 1/√(ax²+bx+c) — complete the square | 3 | 9/10 | **P1** |
| ∫ with modulus, e.g. ∫[−1,2]\|x\|dx or \|x−1\| | 2–3 | 7/10 | P2 |
| Odd/even property on symmetric limits | 1–2 | 7/10 | P2 |
| Trig integrals: sin/cos powers, 1/(a + b sin x) type | 3 | 7/10 | P2 |
| (px+q)/√(quadratic) type | 3 | 6/10 | P2 |
| ∫[0,π/2] with the sin↔cos symmetry | 3 | 6/10 | P2 |
| Standard forms straight from the table | 1 | Every year | **P1** |

**Pattern note.** Integrals typically supplies **8–12 marks** of the paper on its own, spread across
one 5-marker, one or two 3-markers, and 1–2 MCQs. It is the highest-return chapter in Mathematics.
Definite-integral-as-a-limit-of-a-sum is deleted, which removed the one genuinely unpleasant topic.

**The trap.** Forgetting `+ C`. Forgetting to change limits after substituting in a *definite*
integral (either change them, or back-substitute — pick one and be consistent). Both are routinely
worth a mark each.

### Ch 8. Application of Integrals

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Area bounded by a line and a circle | 5 | 7/10 | **P1** |
| Area bounded by a line and a parabola | 5 | 7/10 | **P1** |
| Area under a simple curve between two ordinates | 3 | 6/10 | P2 |
| Area of a region of an ellipse | 5 | 4/10 | P2 |
| Area using symmetry (multiply a quadrant by 4) | 3–5 | 6/10 | P2 |
| Area bounded by \|x\| or \|y\| type | 3 | 4/10 | P3 |

**Pattern note.** "Area between two curves" in general is deleted; what remains is area under a
simple curve, and area between a **line** and a circle/parabola/ellipse. That is a much smaller and
more predictable target than the old syllabus, but the question is still usually a full 5-marker —
so per-mark it is worth real time.

**The trap.** Not sketching the region. The sketch carries a mark, and without it students routinely
integrate over the wrong interval or forget to split the integral at the intersection point.

### Ch 9. Differential Equations

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Linear DE: dy/dx + Py = Q, integrating factor | 3–5 | Every year | **P1** |
| Homogeneous DE of first order and degree (substitute y = vx) | 3–5 | 8/10 | **P1** |
| Variable separable, with a particular solution from an initial condition | 3 | 9/10 | **P1** |
| Order and degree of a given DE | 1 | Every year | **P1** |
| Verify a given function is a solution | 1–2 | 5/10 | P2 |
| Growth/decay or word-problem framing (case study) | 4 | 4/10 | P2 |
| General solution of a simple dy/dx = f(x) | 1–2 | 6/10 | P2 |

**Pattern note.** Formation of a DE from a general solution, and equations reducible to homogeneous
form, are both deleted. So the chapter is now exactly three solving methods. Identify which of the
three you are looking at in the first 10 seconds and this chapter becomes free marks.

**The trap.** Writing the integrating factor as e^∫P dx but then integrating Q instead of Q·(I.F.).
The solution is y·(I.F.) = ∫Q·(I.F.)dx + C. Write that line down as a template before substituting.

---

## Unit IV — Vectors and Three-Dimensional Geometry (14 marks)

### Ch 10. Vector Algebra

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Unit vector in the direction of a given vector / along a+b | 1–2 | Every year | **P1** |
| Angle between two vectors using the dot product | 2 | Every year | **P1** |
| Projection of a on b | 1–2 | Every year | **P1** |
| Area of a triangle / parallelogram using the cross product | 2–3 | 9/10 | **P1** |
| Find λ so that two vectors are perpendicular or parallel | 1–2 | 9/10 | **P1** |
| Direction cosines / direction ratios of a vector | 1–2 | 8/10 | **P1** |
| Show \|a+b\| = \|a−b\| ⟺ a ⊥ b, and similar identities | 2–3 | 6/10 | P2 |
| Section formula / position vector of a dividing point | 2 | 6/10 | P2 |
| a·b and a×b of î ĵ k̂ combinations (MCQ) | 1 | Every year | **P1** |
| \|a×b\|² + (a·b)² = \|a\|²\|b\|² | 2 | 4/10 | P3 |

**Pattern note.** Scalar triple product is deleted. What remains is a small, dense formula set that
generates 1- and 2-mark questions in volume — probably the best marks-per-minute in the paper if the
formula box is genuinely memorised.

### Ch 11. Three Dimensional Geometry — **lines only**

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Shortest distance between two skew lines | 3–5 | 9/10 | **P1** |
| Angle between two lines (vector or Cartesian form) | 2–3 | 9/10 | **P1** |
| Vector and Cartesian equation of a line through two points | 2–3 | Every year | **P1** |
| Equation of a line through a point, parallel to a given line | 1–2 | 8/10 | **P1** |
| Foot of the perpendicular from a point to a line | 3–5 | 7/10 | **P1** |
| Image (reflection) of a point in a line | 5 | 6/10 | P2 |
| Show two lines intersect; find the point of intersection | 3–5 | 6/10 | P2 |
| Direction cosines of a line; check perpendicularity/parallelism | 1–2 | Every year | **P1** |
| Distance between two parallel lines | 3 | 4/10 | P3 |

**Pattern note.** This is the chapter most distorted by old material. **Every plane topic is deleted**
— no equation of a plane, no angle between planes, no distance of a point from a plane, no
coplanarity. Roughly half of every pre-2023 3D question is therefore out of syllabus. If your
practice source asks for a plane, it is stale.

What replaced that weight is more questions on lines: skew-line distance, foot of perpendicular, and
image of a point are now the standard 5-mark candidates.

---

## Unit V — Linear Programming (5 marks)

### Ch 12. Linear Programming

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Graphical solution: maximise/minimise Z, corner-point method | 4–5 | Every year | **P1** |
| Identify the feasible region / corner points from a given graph | 1–2 | 8/10 | **P1** |
| Unbounded feasible region — does max/min exist? | 2–5 | 6/10 | P2 |
| Formulate an LPP from a word problem | 2–3 | 5/10 | P2 |
| Max/min of Z given the corner points (MCQ) | 1 | 8/10 | **P1** |
| Feasible region has no common point → no solution | 1–2 | 4/10 | P3 |

**Pattern note.** Five marks for one completely templated question. Named problem *types* (diet,
transportation, manufacturing) are deleted as categories, and problems are limited to two variables
with at most three non-trivial constraints — which caps how hard this can get. There is no excuse
for losing marks here.

**The trap.** Reading corner points off the graph instead of solving the pair of equations. And, for
an unbounded region, not doing the existence check. Both are single marks that most students drop.

---

## Unit VI — Probability (8 marks)

### Ch 13. Probability

| Topic | Marks | Freq | Priority |
| --- | --- | --- | --- |
| Bayes' theorem word problem | 4–5 | Every year | **P1** |
| Conditional probability P(A\|B) from given data or a table | 2–3 | Every year | **P1** |
| Theorem of total probability | 3–4 | 9/10 | **P1** |
| Independent events — test independence, or compute with it | 2–3 | 9/10 | **P1** |
| Multiplication theorem; drawing without replacement | 2–3 | 8/10 | **P1** |
| Probability distribution of a random variable, and its mean | 3–4 | 7/10 | **P1** |
| At-least / at-most phrasing on two or three trials | 2 | 6/10 | P2 |
| Odds in favour / against, complement | 1 | 5/10 | P2 |

**Pattern note.** **Variance and the Binomial distribution are deleted.** This is the deletion
students most often miss, because the Binomial distribution used to be a guaranteed question. What
survives — and now absorbs the whole 8 marks — is the conditional-probability family: conditional,
multiplication, independence, total probability, Bayes, plus the mean of a random variable.

Bayes is the closest thing to a guaranteed 4- or 5-marker in the paper, and it recurs in a small
number of costumes: two or three machines/factories with different defect rates; two or three bags
with different ball compositions; a diagnostic test with false positives; students from different
sections; a coin chosen from a set of biased coins.

**The trap.** Mixing up P(A|B) and P(B|A). The layout fix in
[`../docs/how-to-answer.md`](../docs/how-to-answer.md) — define events, list all priors, list all
likelihoods, then write the formula — makes this error structurally hard to commit.

---

## Putting it together: a 30-day Maths triage list

Every **P1** row above, and nothing else. That is:

- Matrix method for 3 equations, and A⁻¹ via adjoint
- Integrals: partial fractions, by parts, substitution, complete-the-square, the f(a−x) property
- Linear and variable-separable and homogeneous differential equations
- Maxima–minima word problems, and increasing/decreasing intervals
- Continuity at a point; logarithmic, implicit, parametric and second-order differentiation
- Vectors: unit vector, angle, projection, cross-product area, perpendicularity
- 3D lines: equation through two points, angle between lines, shortest distance, foot of perpendicular
- LP: graphical corner-point method
- Probability: conditional, total probability, Bayes, mean of a random variable
- Relations: equivalence relations; functions: one-one and onto
- Inverse trig: principal values, and sin⁻¹(sin θ) outside the branch
- Area between a line and a circle/parabola

That list is about 60 of 80 marks, and it is genuinely coverable in 30 days.
