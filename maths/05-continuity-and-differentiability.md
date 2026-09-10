# Ch 5 — Continuity and Differentiability

**Unit III Calculus (35 marks) · Typical appearance: 1–2 MCQs + a 2-mark continuity question + a
3-mark differentiation question, and often a 5-mark second-order-derivative relation. Expect 6–9
marks from this chapter alone.**

---

## 1. Scope

### In the syllabus

- **Continuity** and **differentiability**
- **Chain rule**
- Derivatives of **inverse trigonometric functions** — sin⁻¹x, cos⁻¹x, tan⁻¹x
- Derivatives of **implicit functions**
- Concept of exponential and logarithmic functions; derivatives of **log and exponential** functions
- **Logarithmic differentiation**
- Derivatives of functions in **parametric form**
- **Second-order derivatives**

### Deleted — do not study

- **Rolle's theorem** and **Lagrange's Mean Value Theorem**, and their geometric interpretation

> **Consequence.** This chapter is now purely mechanical. There is no theorem to state, no
> hypothesis to verify — only procedures to execute correctly. That makes it one of the most
> completely learnable chapters in the paper: every question is a technique, and there are only
> seven techniques.

---

## 2. Brief

### Start here — in plain English

**Continuity** is the mathematical version of "you can draw it without lifting your pen." That is
genuinely all it means. A function is continuous at a point if there is no jump, no hole and no
sudden flight off to infinity there.

To make that precise you check three things at the point in question: what value the function
actually takes there, and what it *approaches* from the left, and from the right. If all three agree,
the graph passes through smoothly and the function is continuous. If the left and right approaches
disagree, there is a jump. If they agree with each other but not with the function's value, there is
a hole with a stray dot beside it. That is the whole test, and it is why every continuity question in
the paper looks the same: compute the left-hand limit, the right-hand limit and the value, then set
them equal. When a question says "find k such that f is continuous", it is asking you to do exactly
that and solve for k.

**Differentiability** is a stronger demand: not just no break, but no **corner**. The derivative is
the slope of the graph, so for it to exist at a point the graph must have one definite slope there.
Think of |x| at zero: perfectly continuous — you can draw it without lifting the pen — but it
arrives at a sharp V. Coming from the left the slope is −1, from the right it is +1, so there is no
single slope and the function is not differentiable there. This gives the chapter's most important
one-way street: **differentiable implies continuous, but continuous does not imply
differentiable**, and |x| at x = 0 is the counterexample to quote. Every year, some form of this is
asked.

The rest of the chapter is machinery for computing derivatives, and it is worth seeing what each
rule is *for* rather than as a separate spell.

The **chain rule** handles a function inside a function. Differentiate the outside, then multiply by
the derivative of the inside. sin(x²) becomes cos(x²) × 2x. If you are ever unsure whether you have
finished differentiating, ask whether anything is still nested; the commonest error in the whole
chapter is stopping one layer early.

**Implicit differentiation** is for equations you cannot untangle, like x² + y³ = xy. You do not
need to solve for y. Differentiate every term with respect to x, remembering that y is secretly a
function of x, so anything with a y in it produces a dy/dx by the chain rule. Then collect the dy/dx
terms and divide. That is the entire technique.

**Logarithmic differentiation** is the tool for towers and products — x^x, or (sin x)^(cos x), or a
long product of factors. Take the log of both sides first, which turns powers into multipliers and
products into sums, and only then differentiate. Without it, x^x is essentially intractable; with
it, three lines.

**Parametric** differentiation is for curves given as x = f(t), y = g(t): find dy/dt and dx/dt
separately, then divide. And for a **second** derivative of a parametric curve, remember you must
differentiate dy/dx with respect to t and then divide by dx/dt again — forgetting that last division
is the single most frequent slip in this chapter's 3-markers.

**Rolle's** and the **Mean Value Theorem** are the odd ones out — existence statements rather than
computations. The MVT says that over any interval, at some point in between, the instantaneous slope
must equal the average slope. If you averaged 60 km/h over an hour, then at some instant your
speedometer read exactly 60. Rolle's theorem is the special case where you finish where you started,
so the average slope is zero, so somewhere the tangent is flat. Both questions are marked mostly on
whether you *verified the conditions* — continuity on the closed interval, differentiability on the
open one — before applying the conclusion. State them explicitly.

**Learn it from someone else too**

- **Video lecture** — [search: continuity and differentiability class 12 one shot](https://www.youtube.com/results?search_query=continuity+and+differentiability+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: limits and continuity](https://www.khanacademy.org/math/differential-calculus/dc-limits)
- **The book the paper is set from** — [NCERT Maths Part I, Chapter 5 (PDF)](https://ncert.nic.in/textbook/pdf/lemh105.pdf)
- **For extra problems** — NCERT Exemplar Chapter 5 for the piecewise-continuity type, and RD Sharma
  for volume on logarithmic and parametric differentiation, which reward sheer repetition.

---

### Continuity at a point

f is **continuous at x = a** if all three exist and are equal:

```
lim f(x)  =  lim f(x)  =  f(a)
x→a⁻         x→a⁺

  LHL          RHL        value at the point
```

So there are three things to check, and the question is almost always set so that one of them
differs. Write all three separately.

**Computing LHL and RHL.** Substitute x = a − h for the LHL and x = a + h for the RHL, then take
h → 0 with h > 0. This substitution is the standard method and is what the marking scheme expects.

```
LHL = lim f(a − h)          RHL = lim f(a + h)
      h→0⁺                        h→0⁺
```

**Discontinuity** at a means one of the three fails: LHL ≠ RHL, or the limit exists but ≠ f(a), or
f(a) is not defined.

### Continuity on an interval, and algebra of continuous functions

f is continuous on (a, b) if it is continuous at every point of (a, b).

If f and g are continuous at a, then so are f + g, f − g, f·g, cf, and f/g **provided g(a) ≠ 0**.
Composites of continuous functions are continuous.

**Functions continuous everywhere on their domain** (safe to assert without proof):
polynomials, sin x, cos x, eˣ, |x|, and log x on (0, ∞).

**Functions with known discontinuities:** tan x (at odd multiples of π/2), the greatest integer
function [x] (at every integer), 1/x (at 0).

### Differentiability

f is **differentiable at a** if the limit

```
f′(a) = lim  [ f(a + h) − f(a) ] / h
        h→0
```

exists. Equivalently, **LHD = RHD**:

```
LHD = lim [f(a − h) − f(a)] / (−h)          RHD = lim [f(a + h) − f(a)] / h
      h→0⁺                                        h→0⁺
```

### The one-way implication

```
differentiable at a   ⟹   continuous at a
continuous at a       ⟹̸   differentiable at a
```

**The standard counterexample: f(x) = |x| at x = 0.** It is continuous there (LHL = RHL = 0 = f(0))
but not differentiable: LHD = −1 and RHD = +1.

More generally, |x − c| is continuous but not differentiable at x = c. This appears every other year
as an MCQ or Assertion–Reason.

**Corollary that gets asked:** if a function is *not* continuous at a point, it is certainly not
differentiable there. So for a piecewise function, check continuity first — if it fails, you are done.

### Standard derivatives — the table

| f(x) | f′(x) | | f(x) | f′(x) |
| --- | --- | --- | --- | --- |
| xⁿ | n x^(n−1) | | sin⁻¹x | 1/√(1 − x²) |
| sin x | cos x | | cos⁻¹x | −1/√(1 − x²) |
| cos x | −sin x | | tan⁻¹x | 1/(1 + x²) |
| tan x | sec²x | | cot⁻¹x | −1/(1 + x²) |
| cot x | −cosec²x | | sec⁻¹x | 1/(\|x\|√(x² − 1)) |
| sec x | sec x tan x | | cosec⁻¹x | −1/(\|x\|√(x² − 1)) |
| cosec x | −cosec x cot x | | eˣ | eˣ |
| log x | 1/x | | aˣ | aˣ log a |
| log_a x | 1/(x log a) | | constant | 0 |

Note the pattern: each **co-** function's derivative is the negative of its partner's. Learn six, get
twelve.

### The seven techniques

**1. Chain rule.** For y = f(g(x)): dy/dx = f′(g(x)) · g′(x). Work outside-in, and write each layer.

For y = sin(cos(x²)):
```
dy/dx = cos(cos(x²)) · (−sin(x²)) · 2x = −2x sin(x²) cos(cos(x²))
```

**2. Product rule.** (uv)′ = u′v + uv′
**3. Quotient rule.** (u/v)′ = (u′v − uv′)/v²

**4. Implicit differentiation.** When y is not isolated (e.g. x³ + y³ = 3axy), differentiate **both
sides with respect to x**, treating y as a function of x — so every y-term picks up a factor dy/dx by
the chain rule. Then collect dy/dx terms and solve.

```
d/dx (y²) = 2y · dy/dx          d/dx (xy) = y + x · dy/dx
d/dx (sin y) = cos y · dy/dx    d/dx (y³) = 3y² · dy/dx
```

**5. Logarithmic differentiation.** Use it when the variable appears in **both** the base and the
exponent (y = xˣ, y = x^(sin x)), or when y is a long product/quotient of powers.

Method: take log of both sides, simplify using log rules, then differentiate implicitly.

For y = xˣ:
```
      log y = x log x
⟹     (1/y) dy/dx = log x + x·(1/x) = log x + 1
⟹     dy/dx = y(1 + log x) = xˣ (1 + log x)
```

> **Why you cannot just use the power rule.** d/dx(xⁿ) = nx^(n−1) requires n constant, and
> d/dx(aˣ) = aˣ log a requires a constant. In xˣ neither is constant, so neither rule applies. That
> is the whole reason logarithmic differentiation exists, and it is worth being able to say in one
> line if asked.

**6. Parametric differentiation.** If x = f(t) and y = g(t), then

```
dy/dx = (dy/dt) / (dx/dt)          provided dx/dt ≠ 0
```

Never try to eliminate the parameter — it is almost always harder.

**7. Second-order derivatives.** d²y/dx² = d/dx (dy/dx). Differentiate the first derivative again.

**For parametric functions, be careful:**

```
d²y/dx² = d/dx (dy/dx) = [ d/dt (dy/dx) ] / (dx/dt)
```

You must divide by dx/dt again. Forgetting this is the standard error.

### The "prove a relation" family — the 5-mark question

Questions like "if y = (sin⁻¹x)², prove (1 − x²)y″ − xy′ − 2 = 0" all yield to the same three moves:

1. Differentiate once, and **clear the radical** by multiplying up: get √(1 − x²)·y′ = (something in y).
2. **Square both sides** to remove the radical entirely: (1 − x²)(y′)² = (something in y).
3. **Differentiate again**, then divide the whole equation by 2y′.

Step 2 is the one students miss. Squaring before differentiating a second time is what makes the
algebra collapse into the required form.

### Quick recall box

```
CONTINUOUS at a  :  LHL = RHL = f(a)        (three things, check all three)
   LHL = lim f(a−h),  RHL = lim f(a+h),  h→0⁺

DIFFERENTIABLE at a : LHD = RHD (both finite)
   differentiable ⟹ continuous;  continuous ⇏ differentiable   (|x| at 0)

Chain    : dy/dx = f′(g(x))·g′(x)
Product  : (uv)′ = u′v + uv′
Quotient : (u/v)′ = (u′v − uv′)/v²
Implicit : differentiate both sides; every y gives a dy/dx
Log diff : variable in base AND exponent → take log first
Parametric: dy/dx = (dy/dt)/(dx/dt)
           d²y/dx² = [d/dt(dy/dx)] / (dx/dt)      ← divide AGAIN

"Prove a relation": differentiate → clear radical → SQUARE → differentiate → ÷ 2y′
```

---

## 3. Previous years' questions

**Q1.** *(2 marks)* Find the value of k for which

```
f(x) = { kx²,   x ≤ 2
       { 3,     x > 2
```

is continuous at x = 2.

**Q2.** *(3 marks)* Find the value of k so that the function

```
f(x) = { (k cos x)/(π − 2x),   x ≠ π/2
       { 3,                     x = π/2
```

is continuous at x = π/2.

**Q3.** *(3 marks)* Differentiate y = xˣ with respect to x.

**Q4.** *(3 marks)* If xʸ = yˣ, find dy/dx.

**Q5.** *(5 marks)* If y = (sin⁻¹x)², prove that (1 − x²) d²y/dx² − x dy/dx − 2 = 0.

**Q6.** *(5 marks)* If y = e^(a cos⁻¹x), −1 ≤ x ≤ 1, show that
(1 − x²) d²y/dx² − x dy/dx − a²y = 0.

**Q7.** *(3 marks)* If x = a(θ − sin θ) and y = a(1 − cos θ), find dy/dx.

**Q8.** *(3 marks)* If sin y = x sin(a + y), prove that dy/dx = sin²(a + y)/sin a.

**Q9.** *(3 marks)* Differentiate tan⁻¹((1 − x)/(1 + x)) with respect to x.

**Q10.** *(2 marks)* Show that f(x) = |x − 1| is continuous but not differentiable at x = 1.

**Q11.** *(2 marks)* If y = x³ log x, find d²y/dx².

**Q12.** *(2 marks)* Examine the continuity of

```
f(x) = { (x² − 9)/(x − 3),   x ≠ 3
       { 6,                   x = 3
```

at x = 3.

**Q13.** *(1 mark, Assertion–Reason)*
**A:** f(x) = |x| is differentiable at x = 0.
**R:** Every continuous function is differentiable.

**Q14.** *(2 marks)* Find dy/dx if y = sin(cos(x²)).

---

## 4. Solutions

### Q1 — find k for continuity at x = 2

For continuity at x = 2 we need LHL = RHL = f(2).

```
f(2) = k(2)² = 4k          [using the x ≤ 2 branch]

LHL = lim  f(2 − h) = lim  k(2 − h)² = 4k
      h→0⁺              h→0⁺

RHL = lim  f(2 + h) = lim  3 = 3
      h→0⁺              h→0⁺
```

Setting LHL = RHL:

```
      4k = 3
⟹     k = 3/4
```

**k = 3/4** (and then f(2) = 4(3/4) = 3, so all three agree ✓).

### Q2 — find k for continuity at x = π/2

```
f(π/2) = 3
```

For the limit, substitute **x = π/2 + h**, so that h → 0 as x → π/2:

```
cos x = cos(π/2 + h) = −sin h
π − 2x = π − 2(π/2 + h) = π − π − 2h = −2h
```

Therefore

```
lim f(x) = lim  [ k(−sin h) ] / (−2h)
x→π/2      h→0

         = lim  (k/2) · (sin h / h)
           h→0

         = (k/2) · 1                 [since lim (sin h)/h = 1]
         = k/2
```

For continuity, this limit must equal f(π/2) = 3:

```
      k/2 = 3
⟹     k = 6
```

**k = 6**

> The substitution x = π/2 + h is the whole trick. Trying to evaluate the limit directly gives 0/0
> and goes nowhere.

### Q3 — differentiate y = xˣ

Neither the power rule nor the exponential rule applies, since the variable occurs in both the base
and the exponent. Use **logarithmic differentiation**.

```
      y = xˣ
⟹     log y = x log x
```

Differentiate both sides with respect to x:

```
      (1/y) (dy/dx) = (1)(log x) + x(1/x)          [product rule on the right]
⟹     (1/y) (dy/dx) = log x + 1
⟹     dy/dx = y (1 + log x)
```

**dy/dx = xˣ (1 + log x)**

### Q4 — if xʸ = yˣ, find dy/dx

Take log of both sides:

```
      y log x = x log y
```

Differentiate both sides with respect to x (product rule on each side, chain rule on log y):

```
      (dy/dx) log x + y·(1/x)  =  (1) log y + x·(1/y)(dy/dx)
```

Collect the dy/dx terms on the left:

```
      (dy/dx) log x − (x/y)(dy/dx)  =  log y − y/x
⟹     (dy/dx) [ log x − x/y ]  =  log y − y/x
```

Combine each bracket over a common denominator:

```
      log x − x/y = (y log x − x)/y
      log y − y/x = (x log y − y)/x
```

Hence

```
      dy/dx = [ (x log y − y)/x ] × [ y/(y log x − x) ]
```

```
dy/dx = y (x log y − y) / [ x (y log x − x) ]
```

### Q5 — y = (sin⁻¹x)² ⟹ (1 − x²)y″ − xy′ − 2 = 0

**Differentiate once:**

```
      y = (sin⁻¹x)²
⟹     dy/dx = 2 sin⁻¹x · 1/√(1 − x²)
```

**Clear the radical:**

```
      √(1 − x²) · dy/dx = 2 sin⁻¹x
```

**Square both sides** (this is the key move — it eliminates sin⁻¹x in favour of y):

```
      (1 − x²) (dy/dx)² = 4 (sin⁻¹x)² = 4y
```

**Differentiate again** with respect to x, using the product rule on the left:

```
      (1 − x²) · 2 (dy/dx)(d²y/dx²)  +  (dy/dx)² · (−2x)  =  4 (dy/dx)
```

**Divide throughout by 2(dy/dx)** (valid since dy/dx ≠ 0 in general):

```
      (1 − x²) (d²y/dx²) − x (dy/dx) = 2
⟹     (1 − x²) (d²y/dx²) − x (dy/dx) − 2 = 0
```

**Hence proved.** ∎

### Q6 — y = e^(a cos⁻¹x) ⟹ (1 − x²)y″ − xy′ − a²y = 0

**Differentiate once:**

```
      dy/dx = e^(a cos⁻¹x) · a · ( −1/√(1 − x²) )
            = −a y / √(1 − x²)                       [since e^(a cos⁻¹x) = y]
```

**Clear the radical:**

```
      √(1 − x²) · dy/dx = −a y
```

**Square both sides:**

```
      (1 − x²) (dy/dx)² = a² y²
```

**Differentiate again:**

```
      (1 − x²) · 2 (dy/dx)(d²y/dx²)  +  (dy/dx)² (−2x)  =  a² · 2y (dy/dx)
```

**Divide throughout by 2(dy/dx):**

```
      (1 − x²)(d²y/dx²) − x (dy/dx) = a² y
⟹     (1 − x²)(d²y/dx²) − x (dy/dx) − a² y = 0
```

**Hence proved.** ∎

> Q5 and Q6 are the *same* question with a different outer function. Recognise the shape — inverse
> trig inside, then differentiate/clear/square/differentiate/divide — and this whole family becomes
> one method. Other members: y = (tan⁻¹x)², y = e^(m sin⁻¹x), y = (log(x + √(1+x²)))².

### Q7 — parametric: x = a(θ − sin θ), y = a(1 − cos θ)

```
dx/dθ = a(1 − cos θ)
dy/dθ = a(0 + sin θ) = a sin θ
```

```
dy/dx = (dy/dθ) / (dx/dθ) = a sin θ / [ a(1 − cos θ) ] = sin θ / (1 − cos θ)
```

Simplify using the half-angle identities sin θ = 2 sin(θ/2) cos(θ/2) and 1 − cos θ = 2 sin²(θ/2):

```
dy/dx = [ 2 sin(θ/2) cos(θ/2) ] / [ 2 sin²(θ/2) ] = cos(θ/2)/sin(θ/2)
```

**dy/dx = cot(θ/2)**

### Q8 — sin y = x sin(a + y) ⟹ dy/dx = sin²(a + y)/sin a

From the given relation, first isolate x:

```
      x = sin y / sin(a + y)
```

Differentiate **x with respect to y** (easier than the other way round here), using the quotient
rule:

```
dx/dy = [ cos y · sin(a + y)  −  sin y · cos(a + y) ] / sin²(a + y)
```

The numerator is the sine subtraction formula, sin(A − B) = sin A cos B − cos A sin B, with
A = a + y and B = y:

```
      cos y sin(a + y) − sin y cos(a + y) = sin((a + y) − y) = sin a
```

So

```
      dx/dy = sin a / sin²(a + y)
```

Therefore

```
      dy/dx = 1 / (dx/dy) = sin²(a + y) / sin a
```

**Hence proved.** ∎

> Choosing to differentiate x with respect to y, then reciprocating, avoids implicit differentiation
> entirely. Whenever a relation gives x cleanly in terms of y, this is the faster route.

### Q9 — differentiate tan⁻¹((1 − x)/(1 + x))

Let u = (1 − x)/(1 + x), so y = tan⁻¹u.

**Step 1 — du/dx**, by the quotient rule:

```
du/dx = [ (−1)(1 + x) − (1 − x)(1) ] / (1 + x)²
      = [ −1 − x − 1 + x ] / (1 + x)²
      = −2 / (1 + x)²
```

**Step 2 — simplify 1 + u²:**

```
1 + u² = 1 + (1 − x)²/(1 + x)²
       = [ (1 + x)² + (1 − x)² ] / (1 + x)²
       = [ (1 + 2x + x²) + (1 − 2x + x²) ] / (1 + x)²
       = (2 + 2x²) / (1 + x)²
       = 2(1 + x²) / (1 + x)²
```

**Step 3 — chain rule:**

```
dy/dx = (1/(1 + u²)) · du/dx
      = [ (1 + x)² / (2(1 + x²)) ] · [ −2/(1 + x)² ]
      = −1/(1 + x²)
```

**dy/dx = −1/(1 + x²)**

### Q10 — f(x) = |x − 1| at x = 1

Write f piecewise:

```
f(x) = { 1 − x,   x < 1
       { x − 1,   x ≥ 1
```

**Continuity at x = 1:**

```
f(1) = 0
LHL = lim (1 − (1 − h)) = lim h = 0
      h→0⁺                 h→0⁺
RHL = lim ((1 + h) − 1) = lim h = 0
      h→0⁺                 h→0⁺
```

All three equal 0, so f is **continuous at x = 1**. ✓

**Differentiability at x = 1:**

```
LHD = lim  [ f(1 − h) − f(1) ] / (−h) = lim  [ h − 0 ] / (−h) = −1
      h→0⁺                                h→0⁺

RHD = lim  [ f(1 + h) − f(1) ] / h    = lim  [ h − 0 ] / h    = +1
      h→0⁺                                h→0⁺
```

Since LHD = −1 ≠ +1 = RHD, f is **not differentiable at x = 1**.

**Hence f is continuous but not differentiable at x = 1** — which shows continuity does not imply
differentiability.

### Q11 — y = x³ log x, find d²y/dx²

**First derivative** (product rule):

```
dy/dx = 3x² log x + x³ · (1/x) = 3x² log x + x²
```

**Second derivative** (product rule on the first term):

```
d²y/dx² = [ 6x log x + 3x² · (1/x) ] + 2x
        = 6x log x + 3x + 2x
```

**d²y/dx² = 6x log x + 5x = x(6 log x + 5)**

### Q12 — continuity of (x² − 9)/(x − 3) at x = 3

```
f(3) = 6                     [given]

lim  f(x) = lim  (x² − 9)/(x − 3)
x→3          x→3

          = lim  (x − 3)(x + 3)/(x − 3)
            x→3

          = lim  (x + 3)               [cancelling, valid since x ≠ 3 in the limit]
            x→3

          = 6
```

Since lim f(x) = 6 = f(3), **f is continuous at x = 3**.

### Q13 — Assertion–Reason

**A:** "f(x) = |x| is differentiable at x = 0." **False** — LHD = −1, RHD = +1.

**R:** "Every continuous function is differentiable." **False** — the implication runs the other way;
|x| at 0 is the counterexample.

**Answer: A is false and R is false.**

*(The true statement is the converse: every differentiable function is continuous.)*

### Q14 — y = sin(cos(x²))

Three layers, so chain rule twice. Work outside-in:

```
dy/dx = cos(cos(x²)) · d/dx[cos(x²)]
      = cos(cos(x²)) · (−sin(x²)) · d/dx[x²]
      = cos(cos(x²)) · (−sin(x²)) · 2x
```

**dy/dx = −2x sin(x²) cos(cos(x²))**

---

## 5. Test yourself

Time: 50 minutes. Answers below.

1. *(1)* The function f(x) = [x] (greatest integer function) is
   (a) continuous everywhere (b) continuous only at integers (c) discontinuous at every integer
   (d) differentiable everywhere
2. *(1)* d/dx (sec⁻¹x) equals
   (a) 1/√(1 − x²) (b) 1/(1 + x²) (c) 1/(|x|√(x² − 1)) (d) −1/(x√(x² − 1))
3. *(1)* If y = log(log x), then dy/dx is
   (a) 1/(x log x) (b) 1/log x (c) log x/x (d) 1/x
4. *(2)* Find a if f(x) = { ax + 1, x ≤ 3 ; bx + 3, x > 3 } is continuous at x = 3, given b = 2.
5. *(2)* Find dy/dx if y = (log x)^(cos x).
6. *(2)* If y = tan⁻¹(x²), find dy/dx.
7. *(3)* If x = a cos³θ, y = a sin³θ, find dy/dx.
8. *(3)* If y = eˣ sin x, prove that d²y/dx² − 2 dy/dx + 2y = 0.
9. *(3)* Find dy/dx if x² + xy + y² = 100.
10. *(3)* Differentiate y = x^(sin x) with respect to x.
11. *(2)* Show that f(x) = { (sin 3x)/x, x ≠ 0 ; 3, x = 0 } is continuous at x = 0.
12. *(5)* If y = (tan⁻¹x)², show that (1 + x²)² d²y/dx² + 2x(1 + x²) dy/dx − 2 = 0.
13. *(2)* Find d²y/dx² if y = x sin x.
14. *(2)* For what value of k is f(x) = { (x² − 25)/(x − 5), x ≠ 5 ; k, x = 5 } continuous at x = 5?

### Answer key

**1. (c) discontinuous at every integer.** At an integer n, LHL = n − 1 and RHL = n.

**2. (c) 1/(|x|√(x² − 1)).**

**3. (a) 1/(x log x).** Chain rule: (1/log x)·(1/x).

**4. a = 8/3.** f(3) = 3a + 1 (from the x ≤ 3 branch). RHL = 2(3) + 3 = 9. So 3a + 1 = 9 ⟹ a = 8/3.

**5.** Take logs: log y = cos x · log(log x). Then
(1/y)y′ = −sin x · log(log x) + cos x · 1/(x log x).
y′ = (log x)^(cos x) [ cos x/(x log x) − sin x · log(log x) ].

**6.** dy/dx = (1/(1 + x⁴)) · 2x = **2x/(1 + x⁴)**.

**7.** dx/dθ = −3a cos²θ sin θ; dy/dθ = 3a sin²θ cos θ.
dy/dx = (3a sin²θ cos θ)/(−3a cos²θ sin θ) = −sin θ/cos θ = **−tan θ**.

**8.** y′ = eˣ sin x + eˣ cos x = eˣ(sin x + cos x).
y″ = eˣ(sin x + cos x) + eˣ(cos x − sin x) = 2eˣ cos x.
y″ − 2y′ + 2y = 2eˣcos x − 2eˣ(sin x + cos x) + 2eˣ sin x = 0 ✓

**9.** Differentiate implicitly: 2x + (y + x·dy/dx) + 2y·dy/dx = 0
⟹ dy/dx (x + 2y) = −(2x + y) ⟹ **dy/dx = −(2x + y)/(x + 2y)**.

**10.** log y = sin x · log x. (1/y)y′ = cos x · log x + sin x/x.
**y′ = x^(sin x) [ cos x · log x + (sin x)/x ]**.

**11.** f(0) = 3. lim (sin 3x)/x = lim 3·(sin 3x)/(3x) = 3(1) = 3. Since the limit equals f(0),
f is continuous at 0. ✓

**12.** y′ = 2 tan⁻¹x · 1/(1 + x²), so (1 + x²)y′ = 2 tan⁻¹x.
Differentiate: (1 + x²)y″ + 2x y′ = 2/(1 + x²).
Multiply through by (1 + x²): **(1 + x²)²y″ + 2x(1 + x²)y′ − 2 = 0** ✓
*(Note this one does not need the squaring step — the radical never appears, because tan⁻¹ has a
rational derivative. Recognise which family you are in.)*

**13.** y′ = sin x + x cos x. y″ = cos x + (cos x − x sin x) = **2 cos x − x sin x**.

**14. k = 10.** lim (x² − 25)/(x − 5) = lim (x + 5) = 10, so k must be 10.

**Scoring.** Out of 32. Below 22 → identify whether you are losing marks on *continuity* (redo Q1,
Q2, Q12 of §3) or on *differentiation technique* (redo Q3–Q9). They need different fixes.

---

## 6. Answering tips

**On continuity questions**

1. **Write all three quantities separately and label them**: f(a), LHL, RHL. Three lines. The
   marking scheme has a mark for the LHL, a mark for the RHL, and a mark for equating them.

2. **Use the h-substitution explicitly.** Write "Put x = a − h, h → 0⁺". Do not compute limits
   mentally — the substitution line is marked.

3. **State the conclusion in the language of the definition:** "Since LHL = RHL = f(2), f is
   continuous at x = 2." Not just "k = 3/4".

4. **Use the correct branch for f(a).** If the definition says x ≤ 2 for one branch, then f(2) comes
   from *that* branch. Reading the inequality wrongly is a common and expensive slip.

5. **When the limit is 0/0, look for the standard limits:** lim (sin x)/x = 1, lim (tan x)/x = 1,
   lim (eˣ − 1)/x = 1, lim (1 + x)^(1/x) = e, and factorisation for polynomial quotients.

**On differentiation questions**

6. **Name the method before starting.** Write "Using logarithmic differentiation" or "Differentiating
   implicitly w.r.t. x". It costs one line and reads as competence.

7. **For logarithmic differentiation, the log step is a mark.** Show `log y = …` on its own line
   before differentiating.

8. **When to use log differentiation:** variable in the base *and* exponent, or a product/quotient
   of three or more factors. If it is just aˣ or xⁿ, use the standard rule instead — using logs
   there is not wrong but wastes time.

9. **Express the answer in terms of x where possible**, or substitute y back. dy/dx = y(1 + log x) is
   incomplete; dy/dx = xˣ(1 + log x) is the answer.

10. **For parametric second derivatives, do not forget the second division by dx/dt.** Write the
    formula d²y/dx² = [d/dt(dy/dx)]/(dx/dt) down before substituting; that prevents the error.

11. **For "prove the relation" questions, the squaring step must be visible.** Write
    √(1 − x²)·y′ = … on its own line, then the squared version on the next. Those two lines are
    typically 2 of the 5 marks.

12. **Simplify with half-angle identities when a parametric answer looks ugly.**
    sin θ/(1 − cos θ) = cot(θ/2) is expected, not optional — the marking scheme gives the simplified
    form.

**On MCQs**

13. **Learn the derivative table cold.** Roughly half the 1-markers from this chapter are a single
    table lookup plus one chain-rule step. There is no faster marks-per-minute in the paper.

14. **For Assertion–Reason on continuity/differentiability, the direction of the implication is
    almost always the trap.** Differentiable ⟹ continuous. Never the reverse.
