# Ch 9 — Differential Equations

**Unit III Calculus (35 marks) · Typical appearance: one 1-mark order/degree MCQ + one 3- or 5-mark
solving question, nearly every year. Highly templated — three methods cover the whole chapter.**

---

## 1. Scope

### In the syllabus

- **Definition, order and degree**, general and particular solutions of a differential equation
- Solution by the **method of separation of variables**
- Solutions of **homogeneous** differential equations of first order and first degree
- Solutions of **linear** differential equations of the type **dy/dx + Py = Q**, where P and Q are
  functions of x or constants

### Deleted — do not study

- **Formation** of a differential equation whose general solution is given
- Differential equations **reducible to homogeneous** form
- Order and degree questions built on the deleted formation topic

> **Consequence.** The chapter is now exactly three solving methods plus one definition question.
> There is nothing to "form" and nothing to reduce. If a practice question says "form the
> differential equation of the family of circles touching the y-axis", it is out of syllabus.

---

## 2. Brief

### Definitions

A **differential equation** is an equation involving derivatives of a dependent variable with
respect to an independent variable.

- **Order** = the order of the **highest** derivative appearing in the equation.
- **Degree** = the **power** of that highest-order derivative, *after the equation has been made free
  of radicals and fractions in the derivatives*, and provided it is a polynomial in the derivatives.

**Degree is not defined** when the equation is not polynomial in its derivatives — for example if it
contains sin(dy/dx), log(dy/dx), or e^(dy/dx).

| Equation | Order | Degree |
| --- | --- | --- |
| dy/dx + y = x | 1 | 1 |
| (d²y/dx²)³ + (dy/dx)⁵ = 0 | 2 | 3 |
| d³y/dx³ + x(dy/dx)⁴ = 0 | 3 | 1 |
| √(1 + (dy/dx)²) = x | 1 | 2 (square both sides first) |
| d²y/dx² + sin(dy/dx) = 0 | 2 | **not defined** |
| (dy/dx)² + 1/(dy/dx) = 3 | 1 | 3 (multiply through by dy/dx first) |

> **The two traps.** (i) Degree is the power of the **highest-order** derivative, not the highest
> power anywhere in the equation. (ii) Clear radicals and fractions *before* reading off the degree.

### General and particular solutions

- **General solution:** contains arbitrary constants (as many as the order).
- **Particular solution:** the arbitrary constants have been fixed using given initial conditions
  (e.g. "y = 1 when x = 0").

To verify a given function is a solution, substitute it and its derivatives into the equation and
show both sides agree.

### Method 1 — Variables separable

**Trigger:** the equation can be written as f(y)dy = g(x)dx, i.e. the y-stuff separates cleanly from
the x-stuff. Often it starts as dy/dx = g(x)·h(y).

**Procedure:**

1. Separate: get all y-terms with dy on one side, all x-terms with dx on the other.
2. Integrate both sides.
3. Add a **single** arbitrary constant C (on one side only).
4. If an initial condition is given, substitute to find C.

```
dy/dx = (1 + y²)/(1 + x²)
⟹  dy/(1 + y²) = dx/(1 + x²)
⟹  tan⁻¹y = tan⁻¹x + C
```

### Method 2 — Homogeneous equations

**Trigger:** dy/dx can be written entirely in terms of y/x. Formally, dy/dx = F(y/x). Test: if you
replace x → λx and y → λy and the right-hand side is unchanged, it is homogeneous.

**Procedure:**

1. Write the equation as dy/dx = F(y/x).
2. **Substitute y = vx**, so that **dy/dx = v + x(dv/dx)** (product rule — do not forget the v).
3. The equation becomes separable in v and x. Separate and integrate.
4. **Substitute back v = y/x** at the end.

```
x² dy/dx = x² + xy + y²
⟹  dy/dx = 1 + y/x + (y/x)²                 [divide by x² — now visibly homogeneous]

Put y = vx,  dy/dx = v + x dv/dx :

      v + x dv/dx = 1 + v + v²
⟹     x dv/dx = 1 + v²
⟹     dv/(1 + v²) = dx/x
⟹     tan⁻¹v = log|x| + C
⟹     tan⁻¹(y/x) = log|x| + C
```

> If the equation is homogeneous but easier in terms of x/y (i.e. it is naturally
> dx/dy = F(x/y)), substitute **x = vy** instead. Same method, mirrored.

### Method 3 — Linear differential equations

**Trigger:** the equation can be written in the standard form

```
      dy/dx + P(x)·y = Q(x)
```

— that is, dy/dx appears to the first power with coefficient 1, y appears to the first power, and
their coefficients depend on x only.

**Procedure:**

1. **Write it in standard form.** Divide through if the coefficient of dy/dx is not 1. Identify P
   and Q explicitly.
2. **Compute the integrating factor:**

```
      I.F. = e^(∫P dx)
```

3. **Write the solution template:**

```
      y · (I.F.) = ∫ Q · (I.F.) dx  +  C
```

4. Evaluate the integral on the right, then solve for y if asked.
5. Apply the initial condition if given.

**The one thing to get right:** the right-hand integrand is **Q times the I.F.**, not Q alone. Write
the template line down *before* substituting — that habit alone prevents the standard error.

**Common integrating factors:**

| P(x) | I.F. = e^(∫P dx) |
| --- | --- |
| a constant k | e^(kx) |
| 1/x | x |
| 2/x | x² |
| −1/x | 1/x |
| n/x | xⁿ |
| tan x | sec x |
| cot x | sin x |
| −tan x | cos x |

**The y-variable version.** If the equation is linear in x rather than y — i.e.
dx/dy + P(y)·x = Q(y) — the same method applies with the roles swapped: I.F. = e^(∫P dy) and
x·(I.F.) = ∫Q·(I.F.)dy + C. This form appears occasionally, so recognise it.

### How to choose the method — 10 seconds

```
Can I get all y's with dy on one side?          →  SEPARABLE
Is the RHS a function of (y/x) only?            →  HOMOGENEOUS, put y = vx
Is it dy/dx + P(x)y = Q(x)?                     →  LINEAR, integrating factor
```

Try them in that order. Separable is fastest; check for it first.

### Quick recall box

```
ORDER  = order of the highest derivative
DEGREE = power of the highest-order derivative, after clearing radicals/fractions
         NOT DEFINED if the equation is not polynomial in the derivatives
         (sin(dy/dx), log(dy/dx), e^(dy/dx))

SEPARABLE   : f(y)dy = g(x)dx → integrate both sides, one +C

HOMOGENEOUS : dy/dx = F(y/x)
              put y = vx,  dy/dx = v + x dv/dx      ← the "+v" is essential
              separate in v and x, integrate, then put v = y/x back

LINEAR      : dy/dx + Py = Q
              I.F. = e^(∫P dx)
              y·(I.F.) = ∫ Q·(I.F.) dx + C          ← Q TIMES I.F.

I.F. shortcuts: P = 1/x → x ;  P = n/x → xⁿ ;  P = tan x → sec x ;  P = cot x → sin x
```

---

## 3. Previous years' questions

**Q1.** *(1 mark, MCQ)* The order and degree of the differential equation
d²y/dx² + (dy/dx)³ + 6y⁵ = 0 are
(a) 2, 3 (b) 2, 1 (c) 3, 2 (d) 2, 5

**Q2.** *(1 mark)* Write the degree of the differential equation
d²y/dx² + sin(dy/dx) + 1 = 0.

**Q3.** *(3 marks)* Solve: dy/dx = (1 + y²)/(1 + x²).

**Q4.** *(3 marks)* Find the particular solution of dy/dx = y tan x, given that y = 1 when x = 0.

**Q5.** *(3 marks)* Find the general solution of sec²x · tan y dx + sec²y · tan x dy = 0.

**Q6.** *(5 marks)* Solve the differential equation x dy/dx − y = x².

**Q7.** *(5 marks)* Solve: x dy/dx + 2y = x² log x.

**Q8.** *(5 marks)* Solve: dy/dx + y cot x = 2 cos x.

**Q9.** *(5 marks)* Solve the homogeneous differential equation x² dy/dx = x² + xy + y².

**Q10.** *(5 marks)* Solve: (x − y) dy/dx = x + 2y.

**Q11.** *(2 marks)* Find the integrating factor of the differential equation
(1 + x²) dy/dx + 2xy = 4x².

**Q12.** *(4 marks, case study)* The rate of growth of a bacterial population is proportional to the
population present. A culture has 1000 bacteria initially, and 2000 after 2 hours.
(i) Write the differential equation modelling this.
(ii) Solve it to express the population N at time t.
(iii) Find the population after 6 hours.

---

## 4. Solutions

### Q1 — order and degree

The **highest-order** derivative is d²y/dx², so the **order is 2**.

Its power is 1 (it appears as d²y/dx², not squared or cubed), so the **degree is 1**.

*(The (dy/dx)³ term has power 3, but that is a lower-order derivative and is irrelevant to the
degree. Likewise 6y⁵ has nothing to do with it.)*

**Answer: (b) 2, 1**

### Q2 — degree of an equation containing sin(dy/dx)

The equation contains **sin(dy/dx)**, so it is not a polynomial in the derivatives.

**The degree is not defined.**

*(The order is 2.)*

### Q3 — dy/dx = (1 + y²)/(1 + x²)

**Separable.**

```
      dy/(1 + y²) = dx/(1 + x²)
```

Integrating both sides:

```
      ∫ dy/(1 + y²) = ∫ dx/(1 + x²)
⟹     tan⁻¹y = tan⁻¹x + C
```

```
General solution:  tan⁻¹y − tan⁻¹x = C
```

### Q4 — particular solution of dy/dx = y tan x, with y(0) = 1

**Separable.**

```
      dy/y = tan x dx
```

Integrating:

```
      log|y| = log|sec x| + log C          [writing the constant as log C for convenience]
⟹     log|y| = log|C sec x|
⟹     y = C sec x
```

**Apply the initial condition** y = 1 when x = 0. Since sec 0 = 1:

```
      1 = C(1)   ⟹   C = 1
```

```
Particular solution:  y = sec x
```

> Writing the arbitrary constant as **log C** rather than C, when both sides are logs, avoids an
> extra exponentiation step. This is standard and expected.

### Q5 — sec²x tan y dx + sec²y tan x dy = 0

**Separable.** Divide throughout by (tan x)(tan y):

```
      (sec²x / tan x) dx  +  (sec²y / tan y) dy = 0
```

Integrating each term (substituting t = tan x in the first, t = tan y in the second, so that
dt = sec²x dx and sec²y dy respectively):

```
      log|tan x| + log|tan y| = log C
⟹     log|tan x · tan y| = log C
```

```
General solution:  tan x · tan y = C
```

### Q6 — x dy/dx − y = x²

**Step 1 — standard form.** Divide throughout by x:

```
      dy/dx − y/x = x
```

So this is **linear**, with

```
      P = −1/x          Q = x
```

**Step 2 — integrating factor.**

```
      I.F. = e^(∫P dx) = e^(∫ −dx/x) = e^(−log x) = e^(log(1/x)) = 1/x
```

**Step 3 — solution template.**

```
      y · (I.F.) = ∫ Q · (I.F.) dx + C
⟹     y · (1/x) = ∫ x · (1/x) dx + C
⟹     y/x = ∫ 1 dx + C
⟹     y/x = x + C
```

**Step 4 — solve for y.**

```
General solution:  y = x² + Cx
```

*(Check: y′ = 2x + C, so x y′ − y = 2x² + Cx − x² − Cx = x² ✓)*

### Q7 — x dy/dx + 2y = x² log x

**Step 1 — standard form.** Divide by x:

```
      dy/dx + (2/x) y = x log x
```

```
      P = 2/x          Q = x log x
```

**Step 2 — integrating factor.**

```
      I.F. = e^(∫ 2dx/x) = e^(2 log x) = e^(log x²) = x²
```

**Step 3 — solution template.**

```
      y · x² = ∫ (x log x)(x²) dx + C = ∫ x³ log x dx + C
```

**Evaluate ∫x³ log x dx by parts** (ILATE: take u = log x):

```
      ∫ x³ log x dx = log x · (x⁴/4) − ∫ (1/x)(x⁴/4) dx
                    = (x⁴/4) log x − (1/4) ∫ x³ dx
                    = (x⁴/4) log x − x⁴/16
```

So

```
      y x² = (x⁴/4) log x − x⁴/16 + C
```

**Step 4 — solve for y** (divide by x²):

```
General solution:  y = (x²/4) log x − x²/16 + C/x²
```

### Q8 — dy/dx + y cot x = 2 cos x

Already in standard form, with

```
      P = cot x          Q = 2 cos x
```

**Integrating factor:**

```
      I.F. = e^(∫cot x dx) = e^(log|sin x|) = sin x
```

**Solution template:**

```
      y sin x = ∫ (2 cos x)(sin x) dx + C
```

Use 2 sin x cos x = sin 2x:

```
      y sin x = ∫ sin 2x dx + C
              = −(cos 2x)/2 + C
```

```
General solution:  y sin x = −(cos 2x)/2 + C          i.e.  y = [C − ½cos 2x] / sin x
```

### Q9 — x² dy/dx = x² + xy + y²

**Recognise it as homogeneous.** Divide throughout by x²:

```
      dy/dx = 1 + y/x + (y/x)²
```

The right-hand side depends only on y/x, so the equation is homogeneous.

**Substitute y = vx**, so dy/dx = v + x(dv/dx):

```
      v + x dv/dx = 1 + v + v²
⟹     x dv/dx = 1 + v²
```

**Separate:**

```
      dv/(1 + v²) = dx/x
```

**Integrate:**

```
      tan⁻¹v = log|x| + C
```

**Substitute back v = y/x:**

```
General solution:  tan⁻¹(y/x) = log|x| + C
```

### Q10 — (x − y) dy/dx = x + 2y

Write it as

```
      dy/dx = (x + 2y)/(x − y)
```

**Check homogeneity:** dividing numerator and denominator by x,

```
      dy/dx = (1 + 2y/x)/(1 − y/x)
```

which depends only on y/x. **Homogeneous.**

**Substitute y = vx, dy/dx = v + x dv/dx:**

```
      v + x dv/dx = (1 + 2v)/(1 − v)
```

```
      x dv/dx = (1 + 2v)/(1 − v) − v
              = [ (1 + 2v) − v(1 − v) ] / (1 − v)
              = [ 1 + 2v − v + v² ] / (1 − v)
              = (1 + v + v²)/(1 − v)
```

**Separate:**

```
      (1 − v)/(1 + v + v²) dv = dx/x
```

**Integrate the left side.** Note d/dv(1 + v + v²) = 1 + 2v, so write

```
      1 − v = −½(1 + 2v) + 3/2
```

*(Check: −½ − v + 3/2 = 1 − v ✓)*

```
      ∫ (1 − v)/(1 + v + v²) dv = −½ ∫ (1 + 2v)/(1 + v + v²) dv  +  (3/2) ∫ dv/(1 + v + v²)
```

**First part** (substituting t = 1 + v + v²):

```
      = −½ log|1 + v + v²|
```

**Second part:** complete the square, 1 + v + v² = (v + ½)² + 3/4 = (v + ½)² + (√3/2)²

```
      = (3/2) · (1/(√3/2)) tan⁻¹( (v + ½)/(√3/2) )
      = (3/2)(2/√3) tan⁻¹( (2v + 1)/√3 )
      = √3 tan⁻¹( (2v + 1)/√3 )
```

So

```
      −½ log|1 + v + v²| + √3 tan⁻¹( (2v + 1)/√3 ) = log|x| + C
```

**Substitute back v = y/x.** Since 1 + y/x + y²/x² = (x² + xy + y²)/x²:

```
      −½ log| (x² + xy + y²)/x² |  +  √3 tan⁻¹( (2y + x)/(√3 x) )  =  log|x| + C
```

Expanding the log: −½log|x² + xy + y²| + log|x| = log|x| + C rearranges to

```
General solution:  √3 tan⁻¹( (x + 2y)/(√3 x) )  −  ½ log|x² + xy + y²|  =  C
```

*(Different textbooks present this with the constant absorbed differently; any equivalent form is
acceptable, provided the working is shown.)*

> This is at the hard end of what CBSE sets. The technique to take away is the numerator split —
> writing (1 − v) as a multiple of the denominator's derivative plus a constant. That is the same
> "split the numerator" move from [Ch 7](07-integrals.md).

### Q11 — integrating factor of (1 + x²)dy/dx + 2xy = 4x²

**Standard form:** divide by (1 + x²):

```
      dy/dx + [2x/(1 + x²)] y = 4x²/(1 + x²)
```

```
      P = 2x/(1 + x²)
```

```
      I.F. = e^(∫ 2x dx/(1 + x²)) = e^(log(1 + x²)) = 1 + x²
```

**I.F. = 1 + x²**

> Notice the shortcut: whenever the equation is already written as (coefficient)·dy/dx + (derivative
> of that coefficient)·y = …, the coefficient itself **is** the integrating factor. Here
> d/dx(1 + x²) = 2x, which is exactly the coefficient of y.

### Q12 — case study: bacterial growth

**(i) The differential equation.**

"The rate of growth is proportional to the population present" translates directly:

```
      dN/dt = kN                    where k > 0 is the constant of proportionality
```

**(ii) Solve it.**

Separable:

```
      dN/N = k dt
⟹     log N = kt + C₁
⟹     N = e^(kt + C₁) = A e^(kt)          where A = e^(C₁)
```

**Apply N = 1000 at t = 0:**

```
      1000 = A e⁰ = A     ⟹   A = 1000
⟹     N = 1000 e^(kt)
```

**Apply N = 2000 at t = 2:**

```
      2000 = 1000 e^(2k)
⟹     e^(2k) = 2
⟹     2k = log 2
⟹     k = (log 2)/2
```

```
      N(t) = 1000 e^( (t log 2)/2 )  =  1000 · 2^(t/2)
```

**(iii) Population after 6 hours.**

```
      N(6) = 1000 · 2^(6/2) = 1000 · 2³ = 8000
```

**The population after 6 hours is 8000 bacteria.**

*(The doubling time is 2 hours, so in 6 hours the population doubles three times: 1000 → 2000 →
4000 → 8000 ✓ — a useful sanity check.)*

---

## 5. Test yourself

Time: 50 minutes. Answers below.

1. *(1)* The order of the differential equation 2x²(d²y/dx²) − 3(dy/dx) + y = 0 is
   (a) 2 (b) 1 (c) 0 (d) not defined
2. *(1)* The degree of the differential equation [1 + (dy/dx)²]^(3/2) = d²y/dx² is
   (a) 1 (b) 2 (c) 3 (d) 4
3. *(1)* The integrating factor of dy/dx + y/x = x² is
   (a) x (b) 1/x (c) x² (d) log x
4. *(2)* Solve: dy/dx = e^(x + y).
5. *(2)* Find the general solution of dy/dx + 2y = e^(3x).
6. *(2)* Write the order and degree of (d³y/dx³)² + (d²y/dx²)⁴ + dy/dx = 0.
7. *(3)* Solve: x dy/dx + y = x³.
8. *(3)* Find the particular solution of dy/dx = 2xy given y = 1 at x = 0.
9. *(3)* Solve: (1 + y²)dx = (tan⁻¹y − x)dy.
10. *(5)* Solve the homogeneous equation (x² + y²)dx − 2xy dy = 0.
11. *(5)* Solve: dy/dx + 2y tan x = sin x, given y = 0 when x = π/3.
12. *(3)* Solve: sec²y dy/dx + x = 0.
13. *(3)* Solve the homogeneous equation dy/dx = (y − x)/(y + x).

### Answer key

**1. (a) 2.**

**2. (b) 2.** Square both sides to clear the fractional power:
[1 + (dy/dx)²]³ = (d²y/dx²)². The highest-order derivative is d²y/dx², appearing to the power 2.

**3. (a) x.** P = 1/x, I.F. = e^(∫dx/x) = e^(log x) = x.

**4. e^(−y) + eˣ = C.** Separable: dy/e^y = eˣ dx ⟹ ∫e^(−y)dy = ∫eˣdx ⟹ −e^(−y) = eˣ + C₁,
i.e. eˣ + e^(−y) = C.

**5. y = e^(3x)/5 + Ce^(−2x).** Linear with P = 2, Q = e^(3x); I.F. = e^(2x).
y e^(2x) = ∫e^(3x)e^(2x)dx = ∫e^(5x)dx = e^(5x)/5 + C.

**6. Order 3, degree 2.** Highest derivative is d³y/dx³, appearing squared.
*(The (d²y/dx²)⁴ term is a red herring.)*

**7. y = x³/4 + C/x.** Standard form: dy/dx + y/x = x². I.F. = x.
yx = ∫x²·x dx = ∫x³dx = x⁴/4 + C ⟹ y = x³/4 + C/x.

**8. y = e^(x²).** Separable: dy/y = 2x dx ⟹ log y = x² + C. At x = 0, y = 1 ⟹ log 1 = 0 = C.
So log y = x², y = e^(x²).

**9. x = (tan⁻¹y − 1) + C e^(−tan⁻¹y).** Rewrite as
dx/dy + x/(1 + y²) = tan⁻¹y/(1 + y²) — linear **in x**, with P = 1/(1 + y²).
I.F. = e^(∫dy/(1+y²)) = e^(tan⁻¹y).
x·e^(tan⁻¹y) = ∫ [tan⁻¹y/(1 + y²)] e^(tan⁻¹y) dy. Put t = tan⁻¹y, dt = dy/(1 + y²):
= ∫ t e^t dt = e^t(t − 1) = e^(tan⁻¹y)(tan⁻¹y − 1).
So **x = (tan⁻¹y − 1) + C e^(−tan⁻¹y)**.

**10. x² − y² = Cx.** Write it as dy/dx = (x² + y²)/(2xy), which is homogeneous. Put y = vx:
v + x dv/dx = (1 + v²)/(2v) ⟹ x dv/dx = (1 + v² − 2v²)/(2v) = (1 − v²)/(2v).
⟹ 2v dv/(1 − v²) = dx/x. Put t = 1 − v², dt = −2v dv: −∫dt/t = ∫dx/x
⟹ −log|1 − v²| = log|x| + C₁ ⟹ log|x(1 − v²)| = −C₁, so x(1 − v²) = C.
With v = y/x: x(1 − y²/x²) = C ⟹ **(x² − y²)/x = C**, i.e. x² − y² = Cx.

**11. y = cos x − 2cos²x.** Linear: P = 2 tan x, Q = sin x. I.F. = e^(∫2tan x dx) = e^(2 log sec x) = sec²x.
y sec²x = ∫ sin x sec²x dx = ∫ (sin x/cos²x) dx = sec x + C  *(put t = cos x)*.
So y = cos x + C cos²x. At x = π/3: 0 = ½ + C(¼) ⟹ C = −2.
**y = cos x − 2cos²x.**

**12. tan y + x²/2 = C.** Separable: sec²y dy = −x dx ⟹ tan y = −x²/2 + C.

**13. Homogeneous.** dy/dx = (y − x)/(y + x). Put y = vx:
v + x dv/dx = (v − 1)/(v + 1) ⟹ x dv/dx = (v − 1)/(v + 1) − v = (v − 1 − v² − v)/(v + 1)
= −(v² + 1)/(v + 1).
⟹ (v + 1)dv/(v² + 1) = −dx/x ⟹ ½log(v² + 1) + tan⁻¹v = −log|x| + C.
With v = y/x: ½log((x² + y²)/x²) + tan⁻¹(y/x) + log|x| = C, which simplifies to
**½ log(x² + y²) + tan⁻¹(y/x) = C**.

**Scoring.** Out of 34. Below 24 → the failure is almost always method *identification*. Write out
the three triggers from §2 and re-classify all thirteen questions before re-attempting.

---

## 6. Answering tips

**On order and degree**

1. **Identify the highest-order derivative first, and say so.** Then read its power. Do not scan for
   the biggest exponent anywhere in the equation.

2. **Clear radicals and fractions before reading the degree.** If you see a square root or a
   derivative in a denominator, square or multiply through first, and show that step.

3. **"Not defined" is a real answer.** If the equation contains sin, cos, log or exp *of* a
   derivative, the degree is not defined. Write exactly that phrase.

**On solving**

4. **Name the method in the first line.** "This is a linear differential equation" or "This is
   homogeneous, so put y = vx". One line, and it earns the method mark before any algebra.

5. **For linear equations, write P and Q explicitly on their own line** before computing the I.F. It
   prevents the commonest error, which is mis-identifying Q after dividing through.

6. **Write the solution template before substituting:** `y·(I.F.) = ∫Q·(I.F.)dx + C`. This is the
   single most useful habit in the chapter, and it makes the "forgot to multiply Q by the I.F."
   error impossible.

7. **For homogeneous equations, write `dy/dx = v + x dv/dx` as its own line.** Forgetting the `v` is
   the standard slip and it destroys the rest of the question.

8. **Substitute back.** A homogeneous solution left in terms of v is incomplete. Replace v = y/x and
   simplify. The final substitution is a mark.

9. **One arbitrary constant, on one side.** Do not write +C₁ on the left and +C₂ on the right. When
   both sides are logarithms, use **log C** as the constant to keep the algebra clean, and say you
   are doing so.

10. **For a particular solution, apply the condition at the end and state the value of C.** Then
    write the particular solution out in full as a separate final line.

11. **Simplify logarithmic answers using log rules.** log|tan x| + log|tan y| = log C should become
    tan x · tan y = C. The marking scheme gives the simplified form.

12. **Check by differentiating** when the answer is explicit in y. For Q6, verifying
    y = x² + Cx satisfies x y′ − y = x² takes fifteen seconds and confirms 5 marks.

**On case-study / word problems**

13. **Translate the words into the equation as an explicit first step.** "Rate of change of N is
    proportional to N" → dN/dt = kN. That translation is typically 1 of the 4 marks, marked
    separately.

14. **Use the given data points in order** to fix the two constants (A then k), and show each
    substitution. And do the plausibility check at the end — a doubling time of 2 hours must give
    8000 at 6 hours.
