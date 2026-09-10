# Ch 7 — Integrals

**Unit III Calculus (35 marks) · The single largest source of marks in the paper: typically 8–12
marks across one 5-marker, one or two 3-markers and 1–2 MCQs. Give this chapter more time than any
other in Mathematics.**

---

## 1. Scope

### In the syllabus

- Integration as the **inverse process of differentiation**
- Integration by **substitution**, by **partial fractions**, by **parts**
- Evaluation of integrals of these standard types:

```
∫ dx/(x² ± a²)          ∫ dx/√(x² ± a²)          ∫ dx/√(a² − x²)
∫ dx/(ax² + bx + c)     ∫ dx/√(ax² + bx + c)
∫ (px + q)dx/(ax² + bx + c)      ∫ (px + q)dx/√(ax² + bx + c)
∫ √(a² ± x²) dx         ∫ √(x² − a²) dx
```

- **Fundamental Theorem of Calculus** (without proof)
- **Properties of definite integrals** and their use in evaluation

### Deleted — do not study

- **Definite integral as a limit of a sum** (the Σ-with-limits definition and its problems)
- ∫√(ax² + bx + c) dx and ∫(px + q)√(ax² + bx + c) dx

> **Good news.** The limit-of-a-sum questions were the most unpleasant thing in this chapter and they
> are gone. What remains is a set of techniques, each with a clear trigger.

---

## 2. Brief

### Start here — in plain English

Integration is differentiation run backwards, and it is worth being blunt about the consequence:
differentiation is a procedure, integration is a search. To differentiate x⁵ you apply a rule and
you are done. To integrate something you have to *recognise* what it could be the derivative of.
That is why this chapter is the biggest in the book, why it carries the most marks, and why the only
route through it is doing problems rather than reading them.

There are two distinct things called integration, and confusing them causes a lot of unnecessary
suffering.

The **indefinite integral** is the antiderivative: ∫2x dx = x² + C. The answer is a *function*. The
+C is there because differentiating x² + 7 also gives 2x, so there is a whole family of answers
differing by a constant. Dropping the +C is the most common single mark lost in the entire paper.

The **definite integral** ∫ₐᵇ f(x) dx is a *number*, and it means the area under the graph between
a and b. The astonishing fact linking the two — the Fundamental Theorem of Calculus — is that you
can find that area by antidifferentiating and subtracting: F(b) − F(a). Areas and slopes look
unrelated, and the discovery that they are inverse operations is what made calculus the most
powerful tool in mathematics.

The rest of the chapter is a toolkit, and knowing *which tool a problem calls for* matters more than
knowing any one of them. Here is how to tell.

**Substitution** is the chain rule reversed. Look for a chunk whose derivative is also sitting in
the integrand — if you can see f(g(x)) and g′(x) together, put u = g(x) and the integral collapses.
∫2x·cos(x²) dx works because 2x is the derivative of x². This is the first thing to try, always.

**Integration by parts** is for a *product* of two unlike things — a polynomial times a
trigonometric function, or anything times a logarithm. ∫u dv = uv − ∫v du. The whole art is choosing
which factor to call u, and the guide is **ILATE**: Inverse trig, Logarithm, Algebraic,
Trigonometric, Exponential — whichever appears first in that list becomes u. The reason is that u
gets differentiated, and you want the factor that gets *simpler* when differentiated. A logarithm
becomes 1/x; a polynomial loses a degree; an exponential never simplifies, so it should be the other
one.

**Partial fractions** is for a ratio of polynomials. Split the fraction into simpler pieces whose
denominators are the factors, and integrate each — usually into logarithms. Mechanical once set up;
the setup depends on the factors being linear, repeated or quadratic, and it is worth learning the
three shapes.

**Special forms** are the ones to recognise on sight, because they will not yield to anything else:
anything with 1/(x² + a²), 1/(x² − a²), 1/√(a² − x²) and their relatives. There are about eight of
them, they are in the formula sheet, and they are non-negotiable memorisation. A trigonometric
substitution derives them, but in an exam you want them instantly.

Finally, the **properties of definite integrals** are the chapter's hidden shortcut, and strong
candidates are separated from average ones by whether they use them. The most valuable is
∫₀ᵃ f(x) dx = ∫₀ᵃ f(a − x) dx: replacing x by a − x often turns an impossible integrand into one
that cancels against the original, and a whole class of 3- and 5-markers is designed around it. The
even/odd property — ∫₋ₐᵃ of an odd function is zero — can reduce a page of work to one line. Learn to
*look* for these before you start grinding.

Do not try to shortcut this chapter. Thirty problems a week for a month is the honest cost, and it
is repaid: Integrals plus Application of Integrals plus Differential Equations is around a quarter
of the paper.

**Learn it from someone else too**

- **Video lecture** — [search: integrals class 12 maths one shot](https://www.youtube.com/results?search_query=integrals+class+12+maths+one+shot)
- **Interactive lessons and practice** — [Khan Academy: integrals](https://www.khanacademy.org/math/integral-calculus/ic-integration)
- **Why area and slope are inverse** — [search: essence of calculus integration fundamental theorem 3Blue1Brown](https://www.youtube.com/results?search_query=3blue1brown+essence+of+calculus+integration+fundamental+theorem)
- **The book the paper is set from** — [NCERT Maths Part II, Chapter 7 (PDF)](https://ncert.nic.in/textbook/pdf/lemh201.pdf)
- **For extra problems** — NCERT first, all exercises, then RD Sharma for volume. This is the one
  chapter where sheer number of problems attempted is the single best predictor of your mark.

---

### The 15-second classification

Before writing anything, decide which method applies. This decision is the whole skill.

| The integrand looks like | Use |
| --- | --- |
| f(g(x)) · g′(x) — a function and (a multiple of) its own derivative | **substitution** |
| a product of two unrelated functions (x·eˣ, x·log x, x·sin x) | **by parts**, ILATE |
| a rational function whose denominator factorises | **partial fractions** |
| 1/(quadratic) or 1/√(quadratic) | **complete the square**, then a standard form |
| (linear)/(quadratic) or (linear)/√(quadratic) | **split the numerator**: linear = k(derivative of denominator) + m |
| √(a² − x²), √(a² + x²), √(x² − a²) | **standard formula** (or the trig substitution) |
| even powers of sin/cos | **double-angle identities** to reduce the power |
| definite, limits symmetric about 0 | check **odd/even** first |
| definite over [0, a] or [a, b] with an awkward integrand | try **f(x) → f(a − x)** or **f(a + b − x)** |
| definite with a modulus or [x] | **split the interval** at the breakpoints |

### Standard integrals — memorise this table

```
∫ xⁿ dx = x^(n+1)/(n+1) + C        (n ≠ −1)
∫ dx/x = log|x| + C
∫ eˣ dx = eˣ + C
∫ aˣ dx = aˣ/log a + C

∫ sin x dx = −cos x + C            ∫ cos x dx = sin x + C
∫ sec²x dx = tan x + C             ∫ cosec²x dx = −cot x + C
∫ sec x tan x dx = sec x + C       ∫ cosec x cot x dx = −cosec x + C

∫ tan x dx = log|sec x| + C        ∫ cot x dx = log|sin x| + C
∫ sec x dx = log|sec x + tan x| + C
∫ cosec x dx = log|cosec x − cot x| + C

∫ dx/√(1 − x²) = sin⁻¹x + C        ∫ dx/(1 + x²) = tan⁻¹x + C
```

### The special forms — the nine that are named in the syllabus

```
(1)  ∫ dx/(x² − a²)   = (1/2a) log |(x − a)/(x + a)| + C
(2)  ∫ dx/(a² − x²)   = (1/2a) log |(a + x)/(a − x)| + C
(3)  ∫ dx/(x² + a²)   = (1/a) tan⁻¹(x/a) + C

(4)  ∫ dx/√(x² − a²)  = log |x + √(x² − a²)| + C
(5)  ∫ dx/√(x² + a²)  = log |x + √(x² + a²)| + C
(6)  ∫ dx/√(a² − x²)  = sin⁻¹(x/a) + C

(7)  ∫ √(a² − x²) dx  = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C
(8)  ∫ √(x² + a²) dx  = (x/2)√(x² + a²) + (a²/2) log|x + √(x² + a²)| + C
(9)  ∫ √(x² − a²) dx  = (x/2)√(x² − a²) − (a²/2) log|x + √(x² − a²)| + C
```

**How to remember the pattern.** Forms (1)–(3): denominator is a quadratic without a root sign → the
answer is a **log** if the quadratic factorises as a difference of squares, and a **tan⁻¹** if it is
a sum. Forms (4)–(6): with a root sign → **log** for x² ± a², **sin⁻¹** for a² − x². Forms (7)–(9):
the √ integrated gives "half of x times the root, plus half of a² times the corresponding form from
(4)–(6)" — and note (9) alone has a **minus** before the a²/2 term.

### Method 1 — Substitution

Put t = the inner function, so that dt = g′(x)dx, and the integral becomes one in t.

```
∫ 2x/(1 + x²) dx        put t = 1 + x², dt = 2x dx  →  ∫ dt/t = log|t| = log(1 + x²) + C
∫ sin(log x)/x dx       put t = log x, dt = dx/x     →  ∫ sin t dt = −cos(log x) + C
∫ (tan⁻¹x)/(1 + x²) dx  put t = tan⁻¹x, dt = dx/(1+x²) →  ∫ t dt = (tan⁻¹x)²/2 + C
```

**In a definite integral, when you substitute you must either change the limits to the new variable,
or back-substitute before evaluating.** Pick one and be consistent. Changing the limits is safer and
faster — and it is where a mark is routinely lost.

### Method 2 — By parts

```
∫ u · v dx = u ∫v dx − ∫ (du/dx) (∫v dx) dx
```

**Choosing u** — the **ILATE** order. Take as u (the function to be differentiated) whichever comes
**first** in:

```
I  — Inverse trigonometric  (sin⁻¹x, tan⁻¹x)
L  — Logarithmic            (log x)
A  — Algebraic              (x, x², polynomials)
T  — Trigonometric          (sin x, cos x)
E  — Exponential            (eˣ)
```

So in ∫ x log x dx, "L" beats "A": take u = log x. In ∫ x eˣ dx, "A" beats "E": take u = x.

**Two special cases worth memorising:**

```
∫ log x dx = x log x − x + C

∫ eˣ [ f(x) + f′(x) ] dx = eˣ f(x) + C
```

The second one is a gift. Whenever you see eˣ times a bracket, check whether the bracket is a
function plus its own derivative. E.g. ∫eˣ(sin x + cos x)dx = eˣ sin x + C, and
∫eˣ(1/x + log x)dx = eˣ log x + C.

### Method 3 — Partial fractions

For a **proper** rational function (degree of numerator < degree of denominator). If it is improper,
**divide first**.

| Denominator form | Decomposition |
| --- | --- |
| (x − a)(x − b) | A/(x − a) + B/(x − b) |
| (x − a)² | A/(x − a) + B/(x − a)² |
| (x − a)(x − b)(x − c) | A/(x − a) + B/(x − b) + C/(x − c) |
| (x − a)²(x − b) | A/(x − a) + B/(x − a)² + C/(x − b) |
| (x − a)(x² + bx + c), with x² + bx + c irreducible | A/(x − a) + (Bx + C)/(x² + bx + c) |

**Finding the constants — two ways, use both:**
- *Substitution:* put x equal to each root of the denominator; this kills all but one term.
- *Comparing coefficients:* for the irreducible-quadratic case, where substitution alone is not enough.

**Improper example:** ∫ x²/(x² + 1) dx. Degree top = degree bottom, so divide:
x²/(x² + 1) = 1 − 1/(x² + 1), giving ∫ = x − tan⁻¹x + C.

### Method 4 — Complete the square

For ∫dx/(ax² + bx + c) or ∫dx/√(ax² + bx + c):

1. Take out the coefficient of x² if it is not 1.
2. Complete the square: x² + px + q = (x + p/2)² + (q − p²/4).
3. Substitute t = x + p/2, and apply the matching standard form.

```
∫ dx/(x² − 6x + 13) :   x² − 6x + 13 = (x − 3)² + 4 = (x − 3)² + 2²
                        →  (1/2) tan⁻¹((x − 3)/2) + C
```

### Method 5 — Splitting the numerator

For ∫(px + q)/(ax² + bx + c) dx or with a root sign: write the numerator as

```
px + q  =  k · (derivative of the quadratic)  +  m
```

Find k and m by comparing coefficients. The first part integrates to a log (or a root); the second
part reduces to Method 4.

```
∫ (x + 2)/√(x² + 2x + 3) dx :   d/dx(x² + 2x + 3) = 2x + 2
                                x + 2 = ½(2x + 2) + 1
```

### Trigonometric integrals

Reduce powers with these:

```
sin²x = (1 − cos 2x)/2            cos²x = (1 + cos 2x)/2
sin 2x = 2 sin x cos x            cos 2x = 1 − 2sin²x = 2cos²x − 1
sin³x = sin x (1 − cos²x)         cos³x = cos x (1 − sin²x)

2 sin A cos B = sin(A + B) + sin(A − B)
2 cos A cos B = cos(A + B) + cos(A − B)
2 sin A sin B = cos(A − B) − cos(A + B)
```

For odd powers, peel off one factor and substitute. For even powers, use the double-angle identities.

### Definite integrals — the Fundamental Theorem

```
∫[a,b] f(x) dx = F(b) − F(a)          where F′ = f
```

**No constant of integration in a definite integral.**

### Properties of definite integrals — the workhorses

```
P1.  ∫[a,b] f(x)dx = −∫[b,a] f(x)dx  ;  ∫[a,a] f(x)dx = 0

P2.  ∫[a,b] f(x)dx = ∫[a,c] f(x)dx + ∫[c,b] f(x)dx           (splitting)

P3.  ∫[a,b] f(x)dx = ∫[a,b] f(a + b − x)dx

P4.  ∫[0,a] f(x)dx = ∫[0,a] f(a − x)dx                        ← the most used

P5.  ∫[0,2a] f(x)dx = ∫[0,a] f(x)dx + ∫[0,a] f(2a − x)dx

P6.  ∫[0,2a] f(x)dx = 2∫[0,a] f(x)dx   if f(2a − x) = f(x)
                    = 0                if f(2a − x) = −f(x)

P7.  ∫[−a,a] f(x)dx = 2∫[0,a] f(x)dx   if f is EVEN, f(−x) = f(x)
                    = 0                if f is ODD,  f(−x) = −f(x)
```

**How P4 is used.** When the integrand is horrible but symmetric-looking, write the integral as I,
apply P4 to get a second expression for I, and **add the two**. The sum usually simplifies to
something trivial, and then I is half of it. This "add and halve" trick is the single most-tested
idea in definite integrals.

**Check odd/even first, always.** ∫[−1,1] x¹⁷cos⁴x dx = 0 in one line, because x¹⁷ is odd and cos⁴x
is even, so the product is odd. Students who do not check spend ten minutes on it.

### Quick recall box

```
CLASSIFY FIRST (15 seconds):
  f(g)·g′ → substitution   |  product → by parts (ILATE)  |  rational → partial fractions
  1/quadratic → complete square  |  linear/quadratic → split numerator
  even trig powers → double angle  |  symmetric limits → odd/even  |  [0,a] → P4

∫eˣ[f + f′]dx = eˣ f + C          ∫log x dx = x log x − x + C
∫u v dx = u∫v − ∫(u′)(∫v)         ILATE: Inverse, Log, Algebraic, Trig, Exponential

P4: ∫[0,a] f(x)dx = ∫[0,a] f(a−x)dx      →  write I twice, ADD, then halve
P7: odd on [−a,a] → 0 ;  even on [−a,a] → 2∫[0,a]

Definite integral: NO +C.  After substituting, CHANGE THE LIMITS.
Indefinite integral: ALWAYS +C.
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* Evaluate ∫ (x² + x + 1)/[(x + 2)(x² + 1)] dx.

**Q2.** *(3 marks)* Evaluate ∫ 2x/[(x² + 1)(x² + 3)] dx.

**Q3.** *(3 marks)* Evaluate ∫ x/[(x + 1)(x + 2)] dx.

**Q4.** *(3 marks)* Evaluate ∫ dx/(x² − 6x + 13).

**Q5.** *(3 marks)* Evaluate ∫ (x + 2)/√(x² + 2x + 3) dx.

**Q6.** *(3 marks)* Evaluate ∫ x² log x dx.

**Q7.** *(2 marks)* Evaluate ∫ eˣ (sin x + cos x) dx.

**Q8.** *(3 marks)* Evaluate ∫[0, π/2] √(tan x) / [√(tan x) + √(cot x)] dx.

**Q9.** *(3 marks)* Evaluate ∫[1, 4] |x − 2| dx.

**Q10.** *(1 mark)* Evaluate ∫[−1, 1] x¹⁷ cos⁴x dx.

**Q11.** *(3 marks)* Evaluate ∫[2, 3] dx/(x² − 1).

**Q12.** *(3 marks)* Evaluate ∫ sin³x dx.

**Q13.** *(3 marks)* Evaluate ∫ √(4 − x²) dx.

**Q14.** *(2 marks)* Evaluate ∫[0, π/2] sin²x dx.

**Q15.** *(1 mark, MCQ)* ∫ dx/(x² + 4) equals
(a) (1/2) tan⁻¹(x/2) + C (b) tan⁻¹(x/2) + C (c) (1/4) tan⁻¹(x/2) + C (d) 2 tan⁻¹(2x) + C

---

## 4. Solutions

### Q1 — ∫ (x² + x + 1)/[(x + 2)(x² + 1)] dx

The denominator has a linear factor and an **irreducible** quadratic factor (x² + 1 has no real
roots). So the decomposition is

```
      (x² + x + 1)/[(x + 2)(x² + 1)]  =  A/(x + 2)  +  (Bx + C)/(x² + 1)
```

Multiply through by (x + 2)(x² + 1):

```
      x² + x + 1 = A(x² + 1) + (Bx + C)(x + 2)          …(∗)
```

**Find A** by putting x = −2:

```
      4 − 2 + 1 = A(4 + 1) + 0
⟹     3 = 5A
⟹     A = 3/5
```

**Find B** by comparing coefficients of x² in (∗):

```
      1 = A + B   ⟹   B = 1 − 3/5 = 2/5
```

**Find C** by comparing constant terms in (∗):

```
      1 = A + 2C   ⟹   1 = 3/5 + 2C   ⟹   2C = 2/5   ⟹   C = 1/5
```

So

```
      ∫ = (3/5) ∫ dx/(x + 2)  +  ∫ [ (2/5)x + 1/5 ] / (x² + 1) dx

        = (3/5) log|x + 2|  +  (1/5) ∫ (2x + 1)/(x² + 1) dx
```

Split the remaining integral:

```
      (1/5) ∫ 2x/(x² + 1) dx  +  (1/5) ∫ dx/(x² + 1)
    = (1/5) log(x² + 1)  +  (1/5) tan⁻¹x
```

*(the first by substituting t = x² + 1, dt = 2x dx)*

```
∫ (x² + x + 1)/[(x + 2)(x² + 1)] dx = (3/5) log|x + 2| + (1/5) log(x² + 1) + (1/5) tan⁻¹x + C
```

### Q2 — ∫ 2x/[(x² + 1)(x² + 3)] dx

Notice the numerator 2x is the derivative of x². **Substitute t = x², dt = 2x dx:**

```
      ∫ = ∫ dt / [(t + 1)(t + 3)]
```

Partial fractions:

```
      1/[(t + 1)(t + 3)] = A/(t + 1) + B/(t + 3)
⟹     1 = A(t + 3) + B(t + 1)
```

t = −1: 1 = 2A ⟹ A = 1/2. t = −3: 1 = −2B ⟹ B = −1/2.

```
      ∫ = ½ ∫ dt/(t + 1)  −  ½ ∫ dt/(t + 3)
        = ½ log|t + 1| − ½ log|t + 3| + C
        = ½ log |(t + 1)/(t + 3)| + C
```

Substituting back t = x²:

```
∫ 2x/[(x² + 1)(x² + 3)] dx = ½ log [ (x² + 1)/(x² + 3) ] + C
```

*(No modulus needed since both x² + 1 and x² + 3 are positive.)*

### Q3 — ∫ x/[(x + 1)(x + 2)] dx

```
      x/[(x + 1)(x + 2)] = A/(x + 1) + B/(x + 2)
⟹     x = A(x + 2) + B(x + 1)
```

x = −1: −1 = A(1) ⟹ **A = −1**
x = −2: −2 = B(−1) ⟹ **B = 2**

```
      ∫ = −∫ dx/(x + 1) + 2∫ dx/(x + 2)
```

```
∫ x/[(x + 1)(x + 2)] dx = −log|x + 1| + 2 log|x + 2| + C
```

*(Equivalently log|(x + 2)²/(x + 1)| + C.)*

### Q4 — ∫ dx/(x² − 6x + 13)

**Complete the square:**

```
      x² − 6x + 13 = (x² − 6x + 9) + 4 = (x − 3)² + 2²
```

So, using ∫dt/(t² + a²) = (1/a)tan⁻¹(t/a) with t = x − 3 and a = 2:

```
∫ dx/(x² − 6x + 13) = ½ tan⁻¹( (x − 3)/2 ) + C
```

### Q5 — ∫ (x + 2)/√(x² + 2x + 3) dx

**Split the numerator.** The derivative of x² + 2x + 3 is 2x + 2, so write

```
      x + 2 = ½(2x + 2) + 1
```

*(Check: ½(2x + 2) + 1 = x + 1 + 1 = x + 2 ✓)*

```
      ∫ = ½ ∫ (2x + 2)/√(x² + 2x + 3) dx  +  ∫ dx/√(x² + 2x + 3)
          \_________ I₁ _________/            \______ I₂ ______/
```

**I₁:** substitute t = x² + 2x + 3, dt = (2x + 2)dx:

```
      I₁ = ½ ∫ dt/√t = ½ · 2√t = √(x² + 2x + 3)
```

**I₂:** complete the square: x² + 2x + 3 = (x + 1)² + 2 = (x + 1)² + (√2)²

```
      I₂ = ∫ dx/√((x + 1)² + (√2)²) = log | (x + 1) + √(x² + 2x + 3) |
```

*(using ∫dt/√(t² + a²) = log|t + √(t² + a²)|)*

```
∫ (x + 2)/√(x² + 2x + 3) dx = √(x² + 2x + 3) + log | (x + 1) + √(x² + 2x + 3) | + C
```

### Q6 — ∫ x² log x dx

Product of an algebraic and a logarithmic function → **by parts**, and by ILATE, "L" comes before
"A", so take **u = log x** and v = x².

```
      ∫ x² log x dx = log x · ∫x² dx  −  ∫ (1/x) (∫x² dx) dx

                    = log x · (x³/3)  −  ∫ (1/x)(x³/3) dx

                    = (x³/3) log x  −  (1/3) ∫ x² dx

                    = (x³/3) log x  −  (1/3)(x³/3)
```

```
∫ x² log x dx = (x³/3) log x − x³/9 + C
```

*(Check by differentiating: (3x²/3)log x + (x³/3)(1/x) − 3x²/9 = x² log x + x²/3 − x²/3 = x² log x ✓)*

### Q7 — ∫ eˣ (sin x + cos x) dx

Recognise the form ∫eˣ[f(x) + f′(x)]dx with **f(x) = sin x**, since f′(x) = cos x.

```
∫ eˣ (sin x + cos x) dx = eˣ sin x + C
```

*(If you did not spot it, by parts twice also works — but that is four lines instead of one.)*

### Q8 — ∫[0, π/2] √(tan x) / [√(tan x) + √(cot x)] dx

Let

```
      I = ∫[0, π/2] √(tan x) / [√(tan x) + √(cot x)] dx          …(i)
```

**Apply P4** with a = π/2, i.e. replace x by (π/2 − x). Since tan(π/2 − x) = cot x and
cot(π/2 − x) = tan x:

```
      I = ∫[0, π/2] √(cot x) / [√(cot x) + √(tan x)] dx          …(ii)
```

**Add (i) and (ii):**

```
      2I = ∫[0, π/2] [ √(tan x) + √(cot x) ] / [ √(tan x) + √(cot x) ] dx

         = ∫[0, π/2] 1 dx

         = [x]₀^(π/2) = π/2
```

```
I = π/4
```

> This is the canonical "write it twice and add" question. Once you recognise the shape, it is three
> lines. Any question whose integrand is A/(A + B) over [0, a], with A and B swapping under
> x → a − x, is this question.

### Q9 — ∫[1, 4] |x − 2| dx

The modulus changes sign at x = 2, which lies inside [1, 4]. So **split the interval** at 2:

```
      |x − 2| = 2 − x   for x < 2          (since x − 2 < 0)
              = x − 2   for x ≥ 2
```

```
      I = ∫[1,2] (2 − x) dx  +  ∫[2,4] (x − 2) dx
```

**First part:**

```
      ∫[1,2] (2 − x) dx = [ 2x − x²/2 ]₁²
                        = (4 − 2) − (2 − ½)
                        = 2 − 3/2 = 1/2
```

**Second part:**

```
      ∫[2,4] (x − 2) dx = [ x²/2 − 2x ]₂⁴
                        = (8 − 8) − (2 − 4)
                        = 0 − (−2) = 2
```

```
I = 1/2 + 2 = 5/2
```

*(Sanity check by geometry: the graph of |x − 2| over [1, 4] is two triangles, one with base 1 and
height 1 (area ½) and one with base 2 and height 2 (area 2). Total 5/2 ✓)*

### Q10 — ∫[−1, 1] x¹⁷ cos⁴x dx

Let f(x) = x¹⁷ cos⁴x. Then

```
      f(−x) = (−x)¹⁷ cos⁴(−x) = −x¹⁷ cos⁴x = −f(x)
```

*(x¹⁷ is odd since 17 is odd; cos⁴x is even since cos(−x) = cos x.)*

So f is an **odd** function, and the limits are symmetric about 0. By **P7**:

```
∫[−1, 1] x¹⁷ cos⁴x dx = 0
```

### Q11 — ∫[2, 3] dx/(x² − 1)

Use standard form (1) with a = 1, or partial fractions — same thing:

```
      ∫ dx/(x² − 1) = ½ log |(x − 1)/(x + 1)|
```

Evaluate from 2 to 3:

```
      I = ½ [ log|(x − 1)/(x + 1)| ]₂³

        = ½ [ log(2/4) − log(1/3) ]

        = ½ [ log(1/2) + log 3 ]

        = ½ log(3/2)
```

```
I = ½ log(3/2)
```

### Q12 — ∫ sin³x dx

Odd power of sine → peel off one factor of sin x and convert the rest to cosine:

```
      ∫ sin³x dx = ∫ sin²x · sin x dx = ∫ (1 − cos²x) sin x dx
```

Substitute t = cos x, dt = −sin x dx:

```
      = ∫ (1 − t²)(−dt)
      = ∫ (t² − 1) dt
      = t³/3 − t
```

```
∫ sin³x dx = cos³x/3 − cos x + C
```

*(Check: d/dx[cos³x/3 − cos x] = cos²x(−sin x) + sin x = sin x(1 − cos²x) = sin³x ✓)*

### Q13 — ∫ √(4 − x²) dx

This is standard form (7) with a = 2:

```
      ∫ √(a² − x²) dx = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C
```

```
∫ √(4 − x²) dx = (x/2)√(4 − x²) + 2 sin⁻¹(x/2) + C
```

*(Since a² /2 = 4/2 = 2.)*

### Q14 — ∫[0, π/2] sin²x dx

Even power → use the double-angle identity:

```
      sin²x = (1 − cos 2x)/2
```

```
      I = ∫[0, π/2] (1 − cos 2x)/2 dx

        = ½ [ x − (sin 2x)/2 ]₀^(π/2)

        = ½ [ (π/2 − (sin π)/2) − (0 − 0) ]

        = ½ (π/2 − 0)
```

```
I = π/4
```

### Q15 — ∫ dx/(x² + 4)

Standard form (3) with a = 2: ∫dx/(x² + a²) = (1/a)tan⁻¹(x/a).

**Answer: (a) (1/2) tan⁻¹(x/2) + C**

*(The trap is (b), forgetting the 1/a factor.)*

---

## 5. Test yourself

Time: 75 minutes. Answers below.

1. *(1)* ∫ dx/(9 + x²) equals
   (a) (1/3)tan⁻¹(x/3) + C (b) tan⁻¹(x/3) + C (c) (1/9)tan⁻¹(x/3) + C (d) 3tan⁻¹(3x) + C
2. *(1)* ∫[−π/2, π/2] sin⁷x dx equals
   (a) 2 (b) 1 (c) 0 (d) π
3. *(1)* ∫ eˣ (1/x + log x) dx equals
   (a) eˣ log x + C (b) eˣ/x + C (c) eˣ(1 + log x) + C (d) log x + C
4. *(2)* Evaluate ∫ dx/(x² + 2x + 5).
5. *(2)* Evaluate ∫ (2x + 3)/(x² + 3x + 2) dx.
6. *(2)* Evaluate ∫ x eˣ dx.
7. *(3)* Evaluate ∫ 1/[(x + 1)(x + 3)] dx.
8. *(3)* Evaluate ∫ (2x + 1)/√(x² + x + 1) dx.
9. *(3)* Evaluate ∫ cos³x dx.
10. *(3)* Evaluate ∫[0, π/2] dx/(1 + tan x).
11. *(3)* Evaluate ∫ √(x² + 9) dx.
12. *(3)* Evaluate ∫[0, 2] |x − 1| dx.
13. *(3)* Evaluate ∫ x sin⁻¹x / √(1 − x²) dx.
14. *(5)* Evaluate ∫ (3x − 1)/[(x − 1)(x − 2)(x − 3)] dx.
15. *(5)* Evaluate ∫[0, π] x sin x / (1 + cos²x) dx.
16. *(2)* Evaluate ∫ sec²(7 − 4x) dx.
17. *(3)* Evaluate ∫ x²/(x² + 1) dx.

### Answer key

**1. (a) (1/3)tan⁻¹(x/3) + C.**

**2. (c) 0.** sin⁷x is odd and the limits are symmetric.

**3. (a) eˣ log x + C.** Form ∫eˣ[f + f′] with f = log x, f′ = 1/x.

**4. ½ tan⁻¹((x + 1)/2) + C.** x² + 2x + 5 = (x + 1)² + 4.

**5. log|x² + 3x + 2| + C.** The numerator is exactly the derivative of the denominator; substitute
t = x² + 3x + 2.

**6. eˣ(x − 1) + C.** By parts with u = x, v = eˣ: x eˣ − ∫eˣ dx = x eˣ − eˣ.

**7. ½ log|(x + 1)/(x + 3)| + C.** Partial fractions: A = ½ at x = −1, B = −½ at x = −3.
*(Or directly by form (1) after substituting t = x + 2, since (x+1)(x+3) = (x+2)² − 1.)*

**8. 2√(x² + x + 1) + C.** The numerator is the derivative of the quadratic; substitute
t = x² + x + 1 to get ∫dt/√t = 2√t.

**9. sin x − sin³x/3 + C.** ∫cos³x dx = ∫(1 − sin²x)cos x dx; put t = sin x.

**10. π/4.** Note 1/(1 + tan x) = cos x/(cos x + sin x). Call it I; apply P4 (x → π/2 − x) to get
I = ∫ sin x/(sin x + cos x)dx. Adding, 2I = ∫[0,π/2] 1 dx = π/2, so I = π/4.

**11. (x/2)√(x² + 9) + (9/2) log|x + √(x² + 9)| + C.** Standard form (8) with a = 3.

**12. 1.** Split at x = 1: ∫[0,1](1 − x)dx + ∫[1,2](x − 1)dx = ½ + ½ = 1.

**13. −√(1 − x²) · sin⁻¹x + x + C.** By parts with u = sin⁻¹x and v = x/√(1 − x²).
∫v dx = −√(1 − x²). So the integral = sin⁻¹x·(−√(1 − x²)) − ∫[1/√(1 − x²)]·(−√(1 − x²))dx
= −√(1 − x²) sin⁻¹x + ∫1 dx = −√(1 − x²) sin⁻¹x + x + C.

**14. log|x − 1| − 5log|x − 2| + 4log|x − 3| + C.**
(3x − 1) = A(x−2)(x−3) + B(x−1)(x−3) + C(x−1)(x−2).
x = 1: 2 = A(−1)(−2) = 2A ⟹ A = 1.
x = 2: 5 = B(1)(−1) = −B ⟹ B = −5.
x = 3: 8 = C(2)(1) = 2C ⟹ C = 4.

**15. π²/4.** Let I = ∫[0,π] x sin x/(1 + cos²x)dx. Apply P3 (x → π − x); sin(π−x) = sin x and
cos²(π−x) = cos²x, so I = ∫[0,π](π − x)sin x/(1 + cos²x)dx.
Adding: 2I = π∫[0,π] sin x/(1 + cos²x)dx.
Put t = cos x, dt = −sin x dx; limits x = 0 → t = 1, x = π → t = −1:
∫[0,π] sin x/(1 + cos²x)dx = ∫[1,−1] −dt/(1 + t²) = ∫[−1,1] dt/(1 + t²) = [tan⁻¹t]₋₁¹ = π/4 + π/4 = π/2.
So 2I = π(π/2) ⟹ **I = π²/4**.

**16. −¼ tan(7 − 4x) + C.** Substitute t = 7 − 4x, dt = −4dx.

**17. x − tan⁻¹x + C.** Improper, so divide first: x²/(x² + 1) = 1 − 1/(x² + 1).

**Scoring.** Out of 44. Below 31 → do not move on. This chapter is worth 8–12 marks; the return on
another week here beats a week anywhere else in the syllabus. Redo the classification table in §2
and re-attempt every question you missed.

---

## 6. Answering tips

**Universal**

1. **`+ C` on every indefinite integral. No `+ C` on any definite integral.** This is worth a mark in
   both directions and is lost every single year by a large number of students.

2. **Name the method in one line before starting.** "Using partial fractions", "By parts with
   u = log x", "Put t = x² + 1". The examiner is looking for method, and this line earns it before
   you have done any algebra.

3. **Show the substitution and its differential explicitly:** "Let t = x² + 1, so dt = 2x dx". Both
   halves. Not "let t = x² + 1" alone.

4. **Verify by differentiating when you have time.** For a 5-mark integral, thirty seconds of
   differentiation confirms the answer completely. Do this on the two or three biggest questions.

**Substitution**

5. **In a definite integral, change the limits when you substitute** — and write the new limits
   explicitly ("when x = 0, t = 1; when x = π, t = −1"). The alternative is to back-substitute to x
   before evaluating; either is fine, but *mixing* them (new variable, old limits) is a guaranteed
   wrong answer.

6. **Watch the sign when dt = −(something)dx.** Substituting t = cos x gives dt = −sin x dx, and the
   minus sign flips the limits. This is the commonest single error in definite integrals.

**Partial fractions**

7. **Check the fraction is proper first.** If deg(numerator) ≥ deg(denominator), divide. Skipping
   this produces an unsolvable system for A, B, C.

8. **Use the substitution method for linear factors** (put x = each root) — it is much faster than
   comparing coefficients. Use coefficient comparison only for the irreducible-quadratic case.

9. **Do not forget the modulus in the log.** log|x + 2|, not log(x + 2). Marking schemes include it.

**By parts**

10. **State ILATE and your choice of u.** "By ILATE, take u = log x." One line, one mark's worth of
    method credit.

11. **Look for the ∫eˣ[f + f′] form before starting by parts.** If the integrand is eˣ times a
    bracket, check the bracket: is the second term the derivative of the first? If so, the answer is
    one line.

**Definite integrals**

12. **Check odd/even first whenever the limits are ±a.** It takes five seconds and sometimes finishes
    the question.

13. **For a P4 question, lay it out as (i), add (ii), get 2I.** Label the two expressions for I and
    write "Adding (i) and (ii)". That structure is what the marking scheme follows.

14. **For a modulus or greatest-integer integrand, split the interval and state where you split and
    why.** "Since x − 2 < 0 on [1, 2) and ≥ 0 on [2, 4], split at x = 2."

15. **Evaluate in square brackets with limits shown**: [x − (sin 2x)/2]₀^(π/2). Then substitute. Do
    not jump to the number.

**Time management**

16. **If you cannot classify an integral in 30 seconds, move on and come back.** Integrals are the
    biggest time sink in the paper precisely because a wrong method choice can burn ten minutes with
    nothing to show. Bank the questions you recognise first.
