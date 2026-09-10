# Ch 6 — Application of Derivatives

**Unit III Calculus (35 marks) · Typical appearance: one 3-mark monotonicity question + one 4- or
5-mark optimisation problem (very often the Section-E case study). Expect 6–9 marks.**

---

## 1. Scope

### In the syllabus

- **Rate of change** of quantities
- **Increasing and decreasing** functions
- **Maxima and minima** — first derivative test (motivated geometrically) and second derivative test
- Simple problems illustrating basic principles and real-life situations

### Deleted — do not study

- **Tangents and normals** — equations of tangent/normal, angle between curves
- **Approximations** — using dy to estimate small changes

> **Consequence.** The chapter reduced to exactly **two** question types: *find where the function
> increases/decreases*, and *optimise something*. That concentration makes it very high-return.
> Two techniques, ~7 marks.

---

## 2. Brief

### Rate of change

dy/dx is the rate of change of y with respect to x. When both vary with time, use the chain rule:

```
dy/dt = (dy/dx) · (dx/dt)
```

**Standard set-ups:**

| Quantity | Relation | Differentiated |
| --- | --- | --- |
| Circle | A = πr² | dA/dt = 2πr · dr/dt |
| Circle | C = 2πr | dC/dt = 2π · dr/dt |
| Sphere | V = (4/3)πr³ | dV/dt = 4πr² · dr/dt |
| Sphere | S = 4πr² | dS/dt = 8πr · dr/dt |
| Cube | V = x³ | dV/dt = 3x² · dx/dt |
| Cube | S = 6x² | dS/dt = 12x · dx/dt |
| Cylinder | V = πr²h | product rule if both vary |

A rate is "increasing" if positive and "decreasing" if negative — and the **units** must be stated
(cm²/s, m³/min, and so on).

### Increasing and decreasing functions

Let f be differentiable on an interval I.

| Condition on I | Conclusion |
| --- | --- |
| f′(x) > 0 for all x ∈ I | f is **strictly increasing** on I |
| f′(x) < 0 for all x ∈ I | f is **strictly decreasing** on I |
| f′(x) = 0 for all x ∈ I | f is **constant** on I |
| f′(x) ≥ 0 on I | f is increasing (non-decreasing) on I |

**The procedure — four steps:**

1. Compute f′(x).
2. **Factorise** f′(x) completely.
3. Set f′(x) = 0 to find the **critical points**; these divide the real line (or the given domain)
   into intervals.
4. Test the **sign** of f′ in each interval — pick a convenient test point in each — and state the
   conclusion.

A sign table is the clearest way to present step 4 and is what the marking scheme expects.

> **Watch the domain.** If the question restricts to [0, 2π] or (0, ∞), your intervals must lie inside
> it. And note the difference between "increasing **on**" (an interval) and "increasing **at**" (a
> point) — the question always asks for intervals.

### Maxima and minima — the vocabulary

- **Local (relative) maximum** at c: f(c) ≥ f(x) for all x near c
- **Local minimum** at c: f(c) ≤ f(x) for all x near c
- **Absolute (global) maximum/minimum** on an interval: the largest/smallest value taken anywhere on it
- **Critical point:** a point where f′(c) = 0, or where f′ does not exist

Every local extremum of a differentiable function occurs at a critical point — but not every
critical point is an extremum (f(x) = x³ at 0 is the standard example: f′(0) = 0 but there is no
extremum; it is a point of inflection).

### First derivative test

At a critical point c, look at the **sign change** of f′:

| f′ changes | at c there is a |
| --- | --- |
| + → − | **local maximum** |
| − → + | **local minimum** |
| no change | **point of inflection** (neither) |

### Second derivative test

If f′(c) = 0, then:

| | |
| --- | --- |
| f″(c) < 0 | **local maximum** at c |
| f″(c) > 0 | **local minimum** at c |
| f″(c) = 0 | **test fails** — fall back on the first derivative test |

The second derivative test is usually faster for optimisation word problems, and it is what CBSE
expects there. **You must state it explicitly** — writing "f″(3) = −72 < 0, hence a maximum" is a
mark on its own.

> Memory hook: f″ < 0 means the curve is concave down, i.e. shaped like a hill ⟹ maximum. The
> negative sign and the "max" go together.

### Absolute maximum and minimum on a closed interval [a, b]

Because the interval is closed, the extremes may occur at an endpoint rather than a critical point.
So:

1. Find the critical points inside (a, b).
2. Evaluate f at **all** critical points **and at both endpoints** a and b.
3. The largest of those values is the absolute maximum; the smallest, the absolute minimum.

No derivative test is needed — you are simply comparing a finite list. Forgetting the endpoints is
the standard error here.

### Optimisation word problems — the fixed procedure

This is the 5-mark question, and it has an invariable shape:

1. **Draw and label a diagram.** (Worth a mark. Always.)
2. **Name the variables**, and write the quantity to be optimised (the *objective*).
3. **Write the constraint** given in the problem (fixed perimeter, fixed volume, inscribed in a
   sphere, …).
4. **Use the constraint to eliminate one variable**, so the objective is a function of one variable
   only. State the domain of that variable.
5. **Differentiate**, set = 0, solve for the critical value.
6. **Apply the second derivative test** and state the conclusion.
7. **Answer the question actually asked** — if it asked for the maximum *volume*, give the volume,
   not just the value of x.

### The seven problems that keep coming back

Learn these and you have effectively seen the question:

| Problem | Answer to remember |
| --- | --- |
| Open box from a square sheet of side a, corners of side x cut | x = a/6 |
| Rectangle of maximum area inscribed in a circle | It is a **square** |
| Cylinder of maximum volume inscribed in a sphere of radius R | h = 2R/√3 |
| Cone of maximum volume inscribed in a sphere of radius R | h = 4R/3 |
| Window = rectangle + semicircle, fixed perimeter P | height = radius = P/(4 + π) |
| Wire of length L cut into a square and a circle, minimum total area | circle piece = Lπ/(π + 4) |
| Two positive numbers with fixed sum, minimum sum of cubes/squares | they are **equal** |

### Quick recall box

```
RATES:  dy/dt = (dy/dx)(dx/dt).   Always state units.

MONOTONIC:  f′ > 0 ⟹ strictly increasing;  f′ < 0 ⟹ strictly decreasing
   Method: f′ → factorise → critical points → sign table → state intervals

CRITICAL POINT: f′(c) = 0 or f′(c) undefined

FIRST DERIVATIVE TEST : f′ goes + → −  ⟹ max ;  − → +  ⟹ min ;  no change ⟹ inflection
SECOND DERIVATIVE TEST: f′(c) = 0 and f″(c) < 0 ⟹ MAX ;  f″(c) > 0 ⟹ MIN ; = 0 ⟹ test fails

ABSOLUTE MAX/MIN on [a,b]: compare f at critical points AND at a and b

OPTIMISATION: diagram → objective → constraint → eliminate → f′ = 0 → f″ test → answer asked
```

---

## 3. Previous years' questions

**Q1.** *(3 marks)* Find the intervals in which f(x) = 2x³ − 3x² − 36x + 7 is
(a) strictly increasing, (b) strictly decreasing.

**Q2.** *(3 marks)* Find the intervals in which f(x) = sin x + cos x, 0 ≤ x ≤ 2π, is increasing or
decreasing.

**Q3.** *(5 marks)* Show that the height of a cylinder of maximum volume that can be inscribed in a
sphere of radius R is 2R/√3.

**Q4.** *(5 marks)* A square piece of tin of side 18 cm is to be made into a box without a top by
cutting a square from each corner and folding up the flaps. What should be the side of the square to
be cut off so that the volume of the box is maximum? Find that maximum volume.

**Q5.** *(5 marks)* Find the absolute maximum and minimum values of f(x) = 2x³ − 24x + 107 on the
interval [1, 3], and also on [−3, −1].

**Q6.** *(5 marks)* A wire of length 28 m is to be cut into two pieces. One piece is bent into a
square and the other into a circle. What should be the lengths of the two pieces so that the
combined area is minimum?

**Q7.** *(2 marks)* The radius of a circle is increasing at the rate of 3 cm/s. Find the rate at
which the area of the circle is increasing when the radius is 10 cm.

**Q8.** *(2 marks)* Show that f(x) = x³ − 3x² + 3x − 100 is increasing on **R**.

**Q9.** *(4 marks, case study)* A window is in the form of a rectangle surmounted by a semicircular
opening. The total perimeter of the window is 10 m.
(i) If the radius of the semicircle is r and the height of the rectangular part is h, express the
area A of the window in terms of r alone.
(ii) Find the value of r for which the area is maximum.
(iii) Find the maximum area.

**Q10.** *(3 marks)* Find two positive numbers whose sum is 16 and the sum of whose cubes is minimum.

**Q11.** *(1 mark, MCQ)* The function f(x) = x² − 4x + 6 is strictly decreasing on
(a) (−∞, 2) (b) (2, ∞) (c) **R** (d) (−∞, ∞) − {2}

**Q12.** *(2 marks)* Show that of all rectangles inscribed in a given fixed circle, the square has
the maximum area.

---

## 4. Solutions

### Q1 — intervals of monotonicity for 2x³ − 3x² − 36x + 7

```
f(x)  = 2x³ − 3x² − 36x + 7
f′(x) = 6x² − 6x − 36
      = 6(x² − x − 6)
      = 6(x − 3)(x + 2)
```

Critical points: f′(x) = 0 at **x = −2 and x = 3**. These split **R** into three intervals.

**Sign table:**

| Interval | test point | (x − 3) | (x + 2) | f′(x) | f is |
| --- | --- | --- | --- | --- | --- |
| (−∞, −2) | x = −3 | − | − | **+** | increasing |
| (−2, 3) | x = 0 | − | + | **−** | decreasing |
| (3, ∞) | x = 4 | + | + | **+** | increasing |

**(a) Strictly increasing on (−∞, −2) ∪ (3, ∞)**
**(b) Strictly decreasing on (−2, 3)**

### Q2 — intervals for sin x + cos x on [0, 2π]

```
f′(x) = cos x − sin x
```

Set f′(x) = 0:

```
      cos x = sin x
⟹     tan x = 1
⟹     x = π/4  or  x = 5π/4        (within [0, 2π])
```

**Sign table** on [0, 2π]:

| Interval | test point | f′(x) = cos x − sin x | f is |
| --- | --- | --- | --- |
| (0, π/4) | x = 0 | 1 − 0 = **+** | increasing |
| (π/4, 5π/4) | x = π/2 | 0 − 1 = **−** | decreasing |
| (5π/4, 2π) | x = 3π/2 | 0 − (−1) = **+** | increasing |

**Increasing on [0, π/4) ∪ (5π/4, 2π]; decreasing on (π/4, 5π/4).**

### Q3 — cylinder of maximum volume in a sphere of radius R

**Set-up.** Let the cylinder have base radius r and height h. Inscribed in the sphere, the diagonal
of the axial cross-section is a diameter, so by Pythagoras on the right triangle formed by r, h/2 and R:

```
      r² + (h/2)² = R²
⟹     r² = R² − h²/4                    …(constraint)
```

**Objective.**

```
      V = π r² h
```

**Eliminate r using the constraint:**

```
      V(h) = π (R² − h²/4) h = π R² h − (π/4) h³
```

with 0 < h < 2R.

**Differentiate:**

```
      dV/dh = π R² − (3π/4) h²
```

Set dV/dh = 0:

```
      π R² = (3π/4) h²
⟹     h² = 4R²/3
⟹     h = 2R/√3                          (taking the positive root, since h > 0)
```

**Second derivative test:**

```
      d²V/dh² = −(3π/2) h
```

At h = 2R/√3 > 0, d²V/dh² = −(3π/2)(2R/√3) < 0.

Hence V is **maximum** at h = 2R/√3.

**Therefore the height of the cylinder of maximum volume inscribed in a sphere of radius R is
h = 2R/√3.** ∎

*(For interest: then r² = R² − R²/3 = 2R²/3, and V_max = π(2R²/3)(2R/√3) = 4πR³/(3√3).)*

### Q4 — open box from an 18 cm square sheet

**Set-up.** Let x cm be the side of each square cut from the corners. After folding, the box has

```
base = (18 − 2x) by (18 − 2x)          height = x
```

with 0 < x < 9 (so the base has positive side length).

**Objective.**

```
      V(x) = x (18 − 2x)²
           = x (324 − 72x + 4x²)
           = 324x − 72x² + 4x³
```

**Differentiate:**

```
      V′(x) = 324 − 144x + 12x²
            = 12(x² − 12x + 27)
            = 12(x − 3)(x − 9)
```

Set V′(x) = 0: x = 3 or x = 9. But x = 9 is outside the domain (it gives a base of zero), so

```
      x = 3
```

**Second derivative test:**

```
      V″(x) = −144 + 24x
      V″(3) = −144 + 72 = −72 < 0
```

Hence V is **maximum** at x = 3.

**Maximum volume:**

```
      V(3) = 3(18 − 6)² = 3(12)² = 3(144) = 432 cm³
```

**The side of the square to be cut off is 3 cm, and the maximum volume is 432 cm³.**

### Q5 — absolute extrema of 2x³ − 24x + 107

```
f′(x) = 6x² − 24 = 6(x² − 4) = 6(x − 2)(x + 2)
```

Critical points: x = 2 and x = −2.

**On [1, 3]:** the critical point x = 2 lies inside; x = −2 does not. Evaluate f at x = 1, 2, 3:

```
f(1) = 2 − 24 + 107 = 85
f(2) = 16 − 48 + 107 = 75
f(3) = 54 − 72 + 107 = 89
```

**Absolute maximum = 89 at x = 3; absolute minimum = 75 at x = 2.**

**On [−3, −1]:** the critical point x = −2 lies inside. Evaluate f at x = −3, −2, −1:

```
f(−3) = 2(−27) − 24(−3) + 107 = −54 + 72 + 107 = 125
f(−2) = 2(−8) − 24(−2) + 107 = −16 + 48 + 107 = 139
f(−1) = 2(−1) − 24(−1) + 107 = −2 + 24 + 107 = 129
```

**Absolute maximum = 139 at x = −2; absolute minimum = 125 at x = −3.**

> Note that on [1, 3] the maximum occurred at an **endpoint** and the minimum at the critical point,
> while on [−3, −1] the maximum was at the critical point and the minimum at an endpoint. This is
> exactly why you must evaluate at the endpoints too.

### Q6 — wire of 28 m cut into a square and a circle

**Set-up.** Let x metres be the length used for the **circle**; then (28 − x) metres goes to the
square, with 0 < x < 28.

**Circle:** circumference 2πr = x ⟹ r = x/(2π), so

```
area of circle = πr² = π · x²/(4π²) = x²/(4π)
```

**Square:** perimeter 4a = 28 − x ⟹ a = (28 − x)/4, so

```
area of square = a² = (28 − x)²/16
```

**Objective — total area:**

```
      A(x) = x²/(4π) + (28 − x)²/16
```

**Differentiate:**

```
      A′(x) = 2x/(4π) + 2(28 − x)(−1)/16
            = x/(2π) − (28 − x)/8
```

Set A′(x) = 0:

```
      x/(2π) = (28 − x)/8
⟹     8x = 2π(28 − x)
⟹     8x = 56π − 2πx
⟹     x(8 + 2π) = 56π
⟹     x = 56π/(8 + 2π) = 28π/(4 + π)
```

**Second derivative test:**

```
      A″(x) = 1/(2π) + 1/8 > 0
```

which is positive for all x, so A is **minimum** at this value.

**Lengths:**

```
circle piece  = 28π/(π + 4) m
square piece  = 28 − 28π/(π + 4) = 28[(π + 4) − π]/(π + 4) = 112/(π + 4) m
```

**The wire should be cut into pieces of length 28π/(π + 4) m (for the circle) and 112/(π + 4) m (for
the square).**

*(Numerically, about 12.32 m and 15.68 m.)*

### Q7 — rate of change of area of a circle

```
A = πr²        ⟹     dA/dt = 2πr · dr/dt
```

Given dr/dt = 3 cm/s and r = 10 cm:

```
      dA/dt = 2π(10)(3) = 60π cm²/s
```

**The area is increasing at the rate of 60π cm²/s** (≈ 188.5 cm²/s).

### Q8 — show x³ − 3x² + 3x − 100 is increasing on R

```
f′(x) = 3x² − 6x + 3
      = 3(x² − 2x + 1)
      = 3(x − 1)²
```

Since (x − 1)² ≥ 0 for all real x, we have **f′(x) ≥ 0 for all x ∈ R**, with equality only at the
single point x = 1.

Hence f is **increasing on R**. ∎

> A function whose derivative vanishes at isolated points but is otherwise positive is still
> increasing on the whole interval. If the question says "strictly increasing", note that f′(x) > 0
> for all x ≠ 1 and f′ = 0 only at one point, which is enough for strict increase — say so.

### Q9 — window: rectangle + semicircle, perimeter 10 m

**(i) Express A in terms of r.**

The rectangle's width equals the diameter of the semicircle, so width = 2r. Let its height be h.

**Perimeter** (note: the top of the rectangle is *not* part of the boundary — it is the diameter of
the semicircle, which is interior):

```
      perimeter = 2h + 2r + πr = 10
⟹     h = (10 − 2r − πr)/2                …(constraint)
```

**Area:**

```
      A = (rectangle) + (semicircle)
        = 2rh + ½πr²
```

Substituting h:

```
      A = 2r · (10 − 2r − πr)/2 + ½πr²
        = r(10 − 2r − πr) + ½πr²
        = 10r − 2r² − πr² + ½πr²
```

```
A(r) = 10r − 2r² − (π/2) r²
```

**(ii) Maximise.**

```
      dA/dr = 10 − 4r − πr = 10 − r(4 + π)
```

Set dA/dr = 0:

```
      r = 10/(4 + π)
```

Second derivative test:

```
      d²A/dr² = −4 − π < 0
```

So the area is **maximum** at **r = 10/(4 + π) m** (≈ 1.40 m).

*(Worth noting: substituting back gives h = 20/(4 + π) ÷ 2 = 10/(4 + π) = r. So the maximum-area
window has rectangle height equal to the semicircle radius.)*

**(iii) Maximum area.**

```
      A = 10r − r²(2 + π/2)      with r = 10/(4 + π)

Note 2 + π/2 = (4 + π)/2, so

      A = 10 · 10/(4 + π)  −  [100/(4 + π)²] · (4 + π)/2
        = 100/(4 + π) − 50/(4 + π)
        = 50/(4 + π)
```

**Maximum area = 50/(4 + π) m²** (≈ 7.00 m²).

### Q10 — two positive numbers, sum 16, minimum sum of cubes

Let the numbers be x and 16 − x, with 0 < x < 16.

```
      S(x) = x³ + (16 − x)³
```

```
      S′(x) = 3x² − 3(16 − x)²
            = 3[ x² − (16 − x)² ]
            = 3[ x − (16 − x) ][ x + (16 − x) ]        [difference of squares]
            = 3(2x − 16)(16)
            = 48(2x − 16)
```

Set S′(x) = 0: 2x − 16 = 0 ⟹ **x = 8**.

**Second derivative test:**

```
      S″(x) = 6x + 6(16 − x) = 96 > 0
```

Positive, so S is **minimum** at x = 8.

**The two numbers are 8 and 8**, giving the minimum sum of cubes 8³ + 8³ = 1024.

### Q11 — where is x² − 4x + 6 strictly decreasing?

```
f′(x) = 2x − 4 = 2(x − 2)
```

f′(x) < 0 ⟺ x < 2.

**Answer: (a) (−∞, 2)**

### Q12 — the square is the rectangle of maximum area in a circle

Let the circle have fixed radius a. A rectangle inscribed in it has its diagonal as a diameter, so if
the sides are x and y:

```
      x² + y² = (2a)² = 4a²
⟹     y = √(4a² − x²)
```

**Objective:**

```
      A = xy = x√(4a² − x²)
```

It is easier to maximise A² (a maximum of A² occurs at the same x, since A > 0):

```
      A² = x²(4a² − x²) = 4a²x² − x⁴
```

Let S = A². Then

```
      dS/dx = 8a²x − 4x³ = 4x(2a² − x²)
```

Set dS/dx = 0 (with x > 0):

```
      x² = 2a²   ⟹   x = a√2
```

**Second derivative test:**

```
      d²S/dx² = 8a² − 12x²
      at x² = 2a² :  8a² − 24a² = −16a² < 0
```

So S, and hence A, is **maximum** at x = a√2.

Then

```
      y = √(4a² − 2a²) = √(2a²) = a√2 = x
```

Since x = y, the rectangle of maximum area is a **square**. ∎

> The trick of maximising A² instead of A avoids differentiating a square root, and it is fully
> accepted. State the reason ("since A > 0, A is maximum when A² is maximum") — that sentence is a
> mark.

---

## 5. Test yourself

Time: 55 minutes. Answers below.

1. *(1)* The function f(x) = x³ is
   (a) increasing on **R** (b) decreasing on **R** (c) increasing on (0, ∞) only (d) constant
2. *(1)* If f′(c) = 0 and f″(c) > 0, then at x = c the function has a
   (a) local maximum (b) local minimum (c) point of inflection (d) cannot say
3. *(1)* The maximum value of sin x + cos x is
   (a) 1 (b) 2 (c) √2 (d) 1/√2
4. *(2)* The side of a cube is increasing at 3 cm/s. Find the rate of increase of its volume when the
   side is 10 cm.
5. *(3)* Find the intervals in which f(x) = x³ − 12x² + 36x + 17 is increasing or decreasing.
6. *(3)* Find the intervals in which f(x) = −2x³ − 9x² − 12x + 1 is increasing or decreasing.
7. *(3)* Find the local maximum and local minimum values of f(x) = x³ − 6x² + 9x + 15.
8. *(3)* Find the absolute maximum and minimum values of f(x) = x⁴ − 8x² + 3 on [0, 3].
9. *(5)* Show that the right circular cone of maximum volume that can be inscribed in a sphere of
   radius R has height 4R/3.
10. *(5)* Find the point on the curve y² = 4x which is nearest to the point (2, 1).
11. *(4)* An open cylindrical tank of given volume V is to be made. Show that the material used is
    least when the height equals the radius of the base.
12. *(2)* Prove that f(x) = eˣ is strictly increasing on **R**.
13. *(3)* Find two positive numbers whose product is 100 and whose sum is minimum.

### Answer key

**1. (a) increasing on R.** f′(x) = 3x² ≥ 0, zero only at x = 0.

**2. (b) local minimum.**

**3. (c) √2.** f′ = cos x − sin x = 0 at x = π/4, and f(π/4) = 1/√2 + 1/√2 = √2. f″ = −sin x − cos x,
which is negative at π/4, so it is a maximum.

**4. 900 cm³/s.** V = x³, dV/dt = 3x²(dx/dt) = 3(100)(3) = 900 cm³/s.

**5.** f′ = 3x² − 24x + 36 = 3(x² − 8x + 12) = 3(x − 2)(x − 6).
Increasing on (−∞, 2) ∪ (6, ∞); decreasing on (2, 6).

**6.** f′ = −6x² − 18x − 12 = −6(x² + 3x + 2) = −6(x + 1)(x + 2).
f′ > 0 when (x+1)(x+2) < 0, i.e. −2 < x < −1.
Increasing on (−2, −1); decreasing on (−∞, −2) ∪ (−1, ∞).

**7.** f′ = 3x² − 12x + 9 = 3(x − 1)(x − 3). Critical points x = 1, 3.
f″ = 6x − 12. f″(1) = −6 < 0 ⟹ local **max** at x = 1, value f(1) = 1 − 6 + 9 + 15 = 19.
f″(3) = 6 > 0 ⟹ local **min** at x = 3, value f(3) = 27 − 54 + 27 + 15 = 15.

**8.** f′ = 4x³ − 16x = 4x(x² − 4) = 4x(x − 2)(x + 2). In [0, 3] the critical points are x = 0 and
x = 2. Evaluate: f(0) = 3, f(2) = 16 − 32 + 3 = −13, f(3) = 81 − 72 + 3 = 12.
**Absolute max = 12 at x = 3; absolute min = −13 at x = 2.**

**9.** Let the cone have base radius r and height h. With the sphere's centre at distance (h − R)
from the base, r² = R² − (h − R)² = 2Rh − h².
V = (1/3)πr²h = (1/3)π(2Rh − h²)h = (1/3)π(2Rh² − h³).
dV/dh = (1/3)π(4Rh − 3h²) = (π/3)h(4R − 3h) = 0 ⟹ h = 4R/3 (rejecting h = 0).
d²V/dh² = (1/3)π(4R − 6h); at h = 4R/3 this is (π/3)(4R − 8R) = −4πR/3 < 0 ⟹ maximum. ∎

**10. (1, 2).** Minimise the squared distance from (2, 1) to a point (x, y) on y² = 4x, i.e.
x = y²/4. D² = (y²/4 − 2)² + (y − 1)².
d(D²)/dy = 2(y²/4 − 2)(y/2) + 2(y − 1) = y³/4 − 2y + 2y − 2 = y³/4 − 2.
Setting = 0: y³ = 8 ⟹ y = 2, so x = 4/4 = 1.
d²(D²)/dy² = 3y²/4 > 0 ⟹ minimum. **Nearest point (1, 2).**

**11.** Open cylinder: V = πr²h (fixed), material S = πr² + 2πrh (base + curved surface, no lid).
From the constraint h = V/(πr²), so S = πr² + 2V/r.
dS/dr = 2πr − 2V/r² = 0 ⟹ πr³ = V ⟹ r³ = V/π.
d²S/dr² = 2π + 4V/r³ > 0 ⟹ minimum.
Then h = V/(πr²) = πr³/(πr²) = r. Hence **h = r** at minimum material. ∎

**12.** f′(x) = eˣ > 0 for all x ∈ **R**. Hence f is strictly increasing on **R**. ∎

**13. 10 and 10.** Let the numbers be x and 100/x. S = x + 100/x.
S′ = 1 − 100/x² = 0 ⟹ x² = 100 ⟹ x = 10 (positive).
S″ = 200/x³ > 0 for x > 0 ⟹ minimum. Numbers are 10 and 10, minimum sum 20.

**Scoring.** Out of 36. Below 25 → the failure is almost always at step 4 of the optimisation
procedure (eliminating a variable using the constraint). Redo §3 Q3, Q4, Q6 and write out the
constraint as a separate labelled line each time.

---

## 6. Answering tips

**On monotonicity questions**

1. **Factorise f′(x) completely** before finding critical points. An unfactorised quadratic invites
   sign errors; a factorised one makes the sign table trivial.

2. **Present a sign table.** Interval, test point, sign of each factor, sign of f′, conclusion. It is
   the clearest presentation and the marking scheme follows it.

3. **Use union notation for disjoint intervals:** "(−∞, −2) ∪ (3, ∞)", not "(−∞, −2) and (3, ∞)" and
   certainly not "(−∞, −2) ∩ (3, ∞)".

4. **Respect the given domain.** If the question restricts to [0, 2π], do not report intervals
   outside it, and include the endpoints as the question's notation suggests.

**On maxima and minima**

5. **State the second derivative test explicitly with its value and sign:** "f″(3) = −72 < 0, hence
   f has a local maximum at x = 3." Both the value and the conclusion are marked.

6. **If f″(c) = 0, say the test fails and switch to the first derivative test.** Do not conclude
   "point of inflection" automatically — it might still be an extremum (x⁴ at 0 is a minimum with
   f″(0) = 0).

7. **On a closed interval, evaluate at the endpoints.** Write the three or four values as a short
   list and then pick the largest and smallest. This is one of the highest-frequency dropped marks
   in the chapter.

8. **Answer the question that was asked.** If it asks for the maximum volume, the answer is 432 cm³,
   not x = 3. Many students find x correctly and stop, losing the final mark.

**On optimisation word problems**

9. **Draw the diagram first, and label every variable on it.** It is worth a mark, and it is also
   how you find the constraint.

10. **Write the constraint as its own labelled line**, then the objective, then the substitution.
    Three separate lines. Mixing them is where errors enter.

11. **State the domain of your variable** (0 < x < 9, 0 < h < 2R). Then when a critical point falls
    outside it, you can reject it with a reason — which is itself a mark.

12. **Reject invalid roots explicitly.** "x = 9 is rejected since it gives a base of zero side" is
    better than silently ignoring it.

13. **To avoid differentiating a square root, maximise the square.** For distance and area problems,
    say "since D > 0, D is minimum when D² is minimum" and work with D². This is standard and saves
    time.

14. **Keep π symbolic.** Answers like 28π/(π + 4) and 50/(4 + π) are the expected form. You may add
    the decimal in brackets, but do not replace the exact form with it.
