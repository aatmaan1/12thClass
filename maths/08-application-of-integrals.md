# Ch 8 — Application of Integrals

**Unit III Calculus (35 marks) · Typical appearance: usually one full 5-mark question, occasionally
a 3-marker instead. A small chapter with a large per-question payoff.**

---

## 1. Scope

### In the syllabus

- Finding the **area under simple curves**, especially **lines, circles, parabolas and ellipses**,
  **in standard form only**

In practice this covers: area under a curve between two ordinates or between two abscissae, area
bounded by a curve and the coordinate axes, and area of a region bounded by one of these standard
curves together with a line — which is the form CBSE sample papers have used since the syllabus was
rationalised.

### Deleted — do not study

- **Area between two arbitrary curves** (the general "region between y = f(x) and y = g(x)" family)

> **A note on scope, honestly stated.** The syllabus wording ("area under simple curves, especially
> lines, circles/parabolas/ellipses in standard form only") is narrower than the old one, and the
> general two-curve topic is out. But questions bounded by *a standard curve and a line* have
> continued to appear, because a line is one of the named curves. So:
> **prepare the curve-plus-line and curve-plus-axes cases fully; skip the general two-conic case.**
> Check the current year's sample paper to confirm.

---

## 2. Brief

### The two basic formulas

**Strips parallel to the y-axis** (integrate with respect to x):

```
Area = ∫[a,b] y dx          where y = f(x) is the upper boundary
```

**Strips parallel to the x-axis** (integrate with respect to y):

```
Area = ∫[c,d] x dy          where x = g(y) is the right-hand boundary
```

**Which one to choose?** Whichever makes the boundary a single function. If the region's left and
right boundaries are one curve each, integrate w.r.t. y. If the top and bottom are one curve each,
integrate w.r.t. x. Choosing well can turn a two-part integral into one.

### Sign, and why area is never negative

∫[a,b] f(x)dx is negative when the curve lies **below** the x-axis. Area is a positive quantity, so:

- If the curve is below the axis on part of the interval, **split the integral** at the crossing
  point and take the **absolute value** of each piece before adding.
- Writing "Area = |∫…|" and then evaluating is standard and correct.

**Example:** the area between y = sin x and the x-axis from 0 to 2π is

```
∫[0,π] sin x dx  +  | ∫[π,2π] sin x dx |  =  2 + |−2| = 4
```

not ∫[0,2π] sin x dx = 0.

### The standard curves, in standard form

| Curve | Standard form | Facts worth having |
| --- | --- | --- |
| Circle | x² + y² = a² | radius a, centre origin; total area πa²; **quadrant area πa²/4** |
| Parabola (opens right) | y² = 4ax | vertex at origin, symmetric about the x-axis |
| Parabola (opens up) | x² = 4ay | vertex at origin, symmetric about the y-axis |
| Ellipse | x²/a² + y²/b² = 1 | semi-axes a and b; total area **πab**; quadrant area πab/4 |
| Line | y = mx + c, or x/p + y/q = 1 | |

**Standard integral you will use constantly:**

```
∫[0,a] √(a² − x²) dx = πa²/4          (the quadrant of a circle of radius a)
```

and more generally, from Ch 7 form (7):

```
∫ √(a² − x²) dx = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C
```

### Using symmetry

Almost every region in this chapter is symmetric. Exploit it — it halves or quarters the work, and
stating the symmetry is itself a mark.

- Symmetric about the **x-axis** (e.g. y² = 4ax, or a circle): compute the part above the axis and
  **double** it.
- Symmetric about **both** axes (circle, ellipse): compute the first-quadrant part and **multiply
  by 4**.

Write the sentence: "Since the curve is symmetric about the x-axis, the required area = 2 × (area
above the x-axis)."

### The procedure for a curve-and-line region — six steps

This is the 5-mark question. Follow the order every time.

1. **Sketch both curves** on one set of axes, roughly to scale. Mark the axes and label each curve
   with its equation.
2. **Find the points of intersection** by solving the two equations simultaneously. Show the algebra.
3. **Shade the required region** and identify which curve is the upper (or right-hand) boundary on
   each part of it.
4. **Decide whether to integrate w.r.t. x or y**, and **whether the integral must be split** at an
   intersection point.
5. **Write the integral with limits**, and say where the limits came from.
6. **Evaluate**, and state the answer with "square units".

### Two shortcuts that save a lot of algebra

**Shortcut A — the "sector minus triangle" trick.** For a region bounded by a chord and an arc, the
area is often (sector or quadrant area) − (triangle area), both of which are elementary. Example: the
smaller region cut off from an ellipse by the line joining the ends of its semi-axes is

```
(quarter ellipse) − (right triangle) = πab/4 − ½ab
```

**Shortcut B — for a line-through-origin plus circle,** split the region at the intersection point:
the part under the line is a triangle-like integral of x dx, and the part under the circle uses the
√(a² − x²) formula. This is exactly Q3 below.

### Quick recall box

```
Area (w.r.t. x) = ∫[a,b] y dx        Area (w.r.t. y) = ∫[c,d] x dy
Below the axis → split and take |absolute value|

Circle x²+y² = a²  : area πa² ; quadrant πa²/4
Ellipse x²/a²+y²/b² = 1 : area πab ; quadrant πab/4
Parabola y² = 4ax : symmetric about x-axis (double the upper half)

∫[0,a] √(a²−x²) dx = πa²/4
∫ √(a²−x²) dx = (x/2)√(a²−x²) + (a²/2) sin⁻¹(x/a) + C

PROCEDURE: sketch → intersections → shade → choose variable → limits → evaluate → "square units"
```

---

## 3. Previous years' questions

**Q1.** *(3 marks)* Find the area of the region bounded by the curve y² = 9x, the lines x = 2 and
x = 4, and the x-axis, in the first quadrant.

**Q2.** *(3 marks)* Find the area of the region bounded by the ellipse x²/16 + y²/9 = 1.

**Q3.** *(5 marks)* Find the area of the region in the first quadrant enclosed by the x-axis, the
line y = x, and the circle x² + y² = 32.

**Q4.** *(5 marks)* Find the area of the region bounded by the parabola y² = 4x and the line x = 3.

**Q5.** *(5 marks)* Find the area of the smaller region bounded by the ellipse x²/9 + y²/4 = 1 and
the line x/3 + y/2 = 1.

**Q6.** *(2 marks)* Find the area bounded by the curve y = x², the x-axis and the lines x = 1 and
x = 3.

**Q7.** *(3 marks)* Find the area bounded by the curve y = sin x between x = 0 and x = 2π.

**Q8.** *(5 marks)* Find the area of the region bounded by the line y = 3x + 2, the x-axis and the
ordinates x = −1 and x = 1.

**Q9.** *(2 marks)* Find the area of the region bounded by the circle x² + y² = 4 in the first
quadrant.

**Q10.** *(1 mark, MCQ)* The area of the region bounded by y = x², the x-axis and x = 0, x = 2 is
(a) 8/3 (b) 4 (c) 8 (d) 4/3

---

## 4. Solutions

### Q1 — area under y² = 9x from x = 2 to x = 4

In the first quadrant, y² = 9x gives **y = 3√x** (positive root).

```
      Area = ∫[2,4] y dx = ∫[2,4] 3√x dx

           = 3 ∫[2,4] x^(1/2) dx

           = 3 · [ x^(3/2) / (3/2) ]₂⁴

           = 3 · (2/3) [ x^(3/2) ]₂⁴

           = 2 [ 4^(3/2) − 2^(3/2) ]

           = 2 [ 8 − 2√2 ]
```

```
Area = (16 − 4√2) square units          ≈ 10.34 square units
```

### Q2 — area of the ellipse x²/16 + y²/9 = 1

Here a² = 16 and b² = 9, so a = 4 and b = 3.

**By symmetry** (the ellipse is symmetric about both axes), the total area is 4 times the
first-quadrant area:

```
      Area = 4 ∫[0,4] y dx      where  y = 3√(1 − x²/16) = (3/4)√(16 − x²)

           = 4 · (3/4) ∫[0,4] √(16 − x²) dx

           = 3 · (π · 4²/4)                    [using ∫[0,a]√(a²−x²)dx = πa²/4, a = 4]

           = 3 · 4π
```

```
Area = 12π square units
```

*(Consistent with the general result: area of an ellipse = πab = π(4)(3) = 12π.)*

### Q3 — first quadrant, bounded by the x-axis, y = x, and x² + y² = 32

**Sketch.** The circle has radius √32 = 4√2 ≈ 5.66. The line y = x is the 45° line through the
origin. The region sits between the x-axis (below) and the line y = x (above), out to the circle.

**Intersection of y = x and the circle:**

```
      x² + x² = 32   ⟹   2x² = 32   ⟹   x² = 16   ⟹   x = 4      (first quadrant)
```

So they meet at **(4, 4)**.

**Split at x = 4.** For 0 ≤ x ≤ 4 the upper boundary is the **line** y = x; for 4 ≤ x ≤ 4√2 the upper
boundary is the **circle** y = √(32 − x²).

```
      Area = ∫[0,4] x dx  +  ∫[4, 4√2] √(32 − x²) dx
```

**First integral:**

```
      ∫[0,4] x dx = [ x²/2 ]₀⁴ = 8
```

**Second integral**, using ∫√(a² − x²)dx = (x/2)√(a² − x²) + (a²/2)sin⁻¹(x/a) with a² = 32, a = 4√2:

```
      = [ (x/2)√(32 − x²) + 16 sin⁻¹( x/(4√2) ) ]  from 4 to 4√2
```

At x = 4√2:

```
      (4√2/2)√(32 − 32) + 16 sin⁻¹(1) = 0 + 16(π/2) = 8π
```

At x = 4:

```
      (4/2)√(32 − 16) + 16 sin⁻¹(4/(4√2)) = 2√16 + 16 sin⁻¹(1/√2)
                                          = 2(4) + 16(π/4)
                                          = 8 + 4π
```

So the second integral = 8π − (8 + 4π) = **4π − 8**.

**Total:**

```
      Area = 8 + (4π − 8) = 4π
```

```
Area = 4π square units
```

> **Sanity check.** The region is exactly the circular sector between θ = 0 and θ = π/4, whose area
> is (1/8) of the circle = (1/8)π(32) = 4π ✓. Recognising that would have answered the question in
> one line — but the marking scheme wants the integral, so do both: integrate, then check.

### Q4 — area bounded by y² = 4x and x = 3

The parabola y² = 4x is **symmetric about the x-axis**, and the line x = 3 is vertical.

```
      Area = 2 × (area above the x-axis)
           = 2 ∫[0,3] y dx        where y = 2√x
           = 2 ∫[0,3] 2√x dx
           = 4 ∫[0,3] x^(1/2) dx
           = 4 · (2/3) [ x^(3/2) ]₀³
           = (8/3) · 3^(3/2)
           = (8/3) · 3√3
```

```
Area = 8√3 square units          ≈ 13.86 square units
```

*(Alternative, integrating w.r.t. y: the region runs from y = −2√3 to y = 2√3, with x from y²/4 to 3.
Area = ∫[−2√3, 2√3] (3 − y²/4) dy = 2∫[0,2√3](3 − y²/4)dy = 2[3y − y³/12]₀^(2√3)
= 2[6√3 − 24√3/12] = 2[6√3 − 2√3] = 8√3 ✓)*

### Q5 — smaller region between the ellipse x²/9 + y²/4 = 1 and the line x/3 + y/2 = 1

**Recognise the geometry.** The ellipse has a = 3, b = 2. The line x/3 + y/2 = 1 passes through
(3, 0) and (0, 2) — precisely the ends of the semi-major and semi-minor axes in the first quadrant.
So the line is the chord joining those two points, and the **smaller region** is the piece of the
first-quadrant quarter-ellipse lying **above** the line.

```
      Required area = (area of quarter ellipse) − (area of triangle with vertices (0,0), (3,0), (0,2))
```

**Quarter ellipse:**

```
      = πab/4 = π(3)(2)/4 = 3π/2
```

**Triangle:** legs 3 and 2, so area = ½(3)(2) = 3.

```
      Required area = 3π/2 − 3 = (3/2)(π − 2)
```

```
Area = 3(π − 2)/2 square units          ≈ 1.71 square units
```

*(By integration, for full marks if the question demands it:
Area = ∫[0,3] [ (2/3)√(9 − x²) − 2(1 − x/3) ] dx = (2/3)(π·9/4) − 2[x − x²/6]₀³
= 3π/2 − 2(3 − 3/2) = 3π/2 − 3 ✓)*

### Q6 — area under y = x² from x = 1 to x = 3

```
      Area = ∫[1,3] x² dx = [ x³/3 ]₁³ = 27/3 − 1/3 = 26/3
```

```
Area = 26/3 square units
```

### Q7 — area bounded by y = sin x from x = 0 to 2π

The curve is **above** the x-axis on [0, π] and **below** it on [π, 2π]. So split:

```
      Area = ∫[0,π] sin x dx  +  | ∫[π,2π] sin x dx |
```

```
      ∫[0,π] sin x dx = [−cos x]₀^π = −cos π + cos 0 = 1 + 1 = 2

      ∫[π,2π] sin x dx = [−cos x]_π^(2π) = −cos 2π + cos π = −1 − 1 = −2
```

```
      Area = 2 + |−2| = 4
```

```
Area = 4 square units
```

> If you had computed ∫[0,2π] sin x dx you would have got **0**, which is the net signed integral,
> not the area. The split is the whole question.

### Q8 — area bounded by y = 3x + 2, the x-axis, x = −1 and x = 1

**Find where the line crosses the x-axis:**

```
      3x + 2 = 0   ⟹   x = −2/3
```

Since −1 < −2/3 < 1, the line is **below** the axis on [−1, −2/3] and **above** it on [−2/3, 1]. So
split at x = −2/3.

Let F(x) = ∫(3x + 2)dx = 3x²/2 + 2x.

```
      F(−1)   = 3/2 − 2 = −1/2
      F(−2/3) = 3(4/9)/2 + 2(−2/3) = 2/3 − 4/3 = −2/3
      F(1)    = 3/2 + 2 = 7/2
```

**Part 1** (below the axis):

```
      ∫[−1, −2/3] (3x + 2) dx = F(−2/3) − F(−1) = −2/3 + 1/2 = −1/6
      Area₁ = |−1/6| = 1/6
```

**Part 2** (above the axis):

```
      ∫[−2/3, 1] (3x + 2) dx = F(1) − F(−2/3) = 7/2 + 2/3 = 21/6 + 4/6 = 25/6
      Area₂ = 25/6
```

```
      Total area = 1/6 + 25/6 = 26/6 = 13/3
```

```
Area = 13/3 square units
```

*(Geometric check: two triangles. The first has base from −1 to −2/3, i.e. 1/3, and height |3(−1)+2|
= 1, area = ½(1/3)(1) = 1/6 ✓. The second has base from −2/3 to 1, i.e. 5/3, and height 3(1)+2 = 5,
area = ½(5/3)(5) = 25/6 ✓)*

### Q9 — first-quadrant area of x² + y² = 4

This is a **quadrant** of a circle of radius 2:

```
      Area = πa²/4 = π(4)/4 = π
```

*(By integration: ∫[0,2]√(4 − x²)dx = π(2)²/4 = π ✓)*

```
Area = π square units
```

### Q10 — area under y = x² from 0 to 2

```
      ∫[0,2] x² dx = [x³/3]₀² = 8/3
```

**Answer: (a) 8/3**

---

## 5. Test yourself

Time: 50 minutes. Answers below. **Draw a sketch for every question** — that is part of the exercise.

1. *(1)* The area of the region bounded by y = 2x, the x-axis and x = 3 is
   (a) 9 (b) 6 (c) 18 (d) 3
2. *(1)* The area of the circle x² + y² = 16 is
   (a) 4π (b) 8π (c) 16π (d) 32π
3. *(2)* Find the area under y = x³ from x = 1 to x = 2.
4. *(2)* Find the area of the region bounded by y² = 16x, the x-axis and x = 4, in the first
   quadrant.
5. *(2)* Find the area of the ellipse x²/25 + y²/9 = 1.
6. *(3)* Find the area bounded by y = cos x, the x-axis, from x = 0 to x = π.
7. *(3)* Find the area of the region bounded by y = x², the y-axis and the lines y = 1, y = 4.
8. *(5)* Find the area of the region in the first quadrant bounded by the x-axis, the line y = √3 x,
   and the circle x² + y² = 4.
9. *(5)* Find the area of the region bounded by the parabola y = x² and the line y = 4.
10. *(5)* Find the area of the smaller region bounded by the circle x² + y² = 9 and the line x = 2.
11. *(3)* Find the area bounded by the line 2x + y = 4, the x-axis and the y-axis.
12. *(3)* Find the area of the region bounded by y = |x + 1|, the x-axis, x = −3 and x = 1.

### Answer key

**1. (a) 9.** ∫[0,3] 2x dx = [x²]₀³ = 9. *(Or triangle: ½(3)(6) = 9.)*

**2. (c) 16π.** a = 4, area = πa² = 16π.

**3. 15/4.** ∫[1,2]x³dx = [x⁴/4]₁² = 16/4 − 1/4 = 15/4.

**4. 64/3.** In the first quadrant y = 4√x, so
Area = ∫[0,4] 4√x dx = 4(2/3)[x^(3/2)]₀⁴ = (8/3)(8) = **64/3** square units.
*(The question asked for the first quadrant only. Had it asked for the whole region bounded by the
parabola and x = 4, symmetry about the x-axis would double it to 128/3 — read which one is wanted.)*

**5. 15π.** a = 5, b = 3, area = πab = 15π.

**6. 2.** cos x is positive on [0, π/2] and negative on [π/2, π]. Split:
∫[0,π/2]cos x dx = 1; |∫[π/2,π]cos x dx| = |−1| = 1. Total 2.

**7. 14/3.** Integrate w.r.t. y: x = √y. Area = ∫[1,4]√y dy = (2/3)[y^(3/2)]₁⁴ = (2/3)(8 − 1) = 14/3.

**8. 2π/3.** The line y = √3 x meets the circle where x² + 3x² = 4 ⟹ x = 1, y = √3.
Area = ∫[0,1]√3 x dx + ∫[1,2]√(4 − x²)dx = √3/2 + [ (x/2)√(4−x²) + 2sin⁻¹(x/2) ]₁²
= √3/2 + [ (0 + 2·π/2) − (½·√3 + 2·π/6) ] = √3/2 + π − √3/2 − π/3 = **2π/3**.
*(Check: this is the sector from θ = 0 to θ = π/3, area = (1/6)π(4) = 2π/3 ✓)*

**9. 32/3.** y = x² meets y = 4 at x = ±2. By symmetry about the y-axis,
Area = 2∫[0,2](4 − x²)dx = 2[4x − x³/3]₀² = 2(8 − 8/3) = 2(16/3) = 32/3.

**10. 9π/2 − 2√5 − 9 sin⁻¹(2/3) square units.**
The smaller region is to the *right* of x = 2, and is symmetric about the x-axis, so
Area = 2∫[2,3]√(9 − x²)dx
= 2[ (x/2)√(9 − x²) + (9/2)sin⁻¹(x/3) ]₂³
= 2[ (0 + (9/2)(π/2)) − (1·√5 + (9/2)sin⁻¹(2/3)) ]
= 2[ 9π/4 − √5 − (9/2)sin⁻¹(2/3) ]
= 9π/2 − 2√5 − 9 sin⁻¹(2/3)  ≈ 14.14 − 4.47 − 6.56 ≈ **3.11 square units**.

**11. 4.** The line meets the axes at (2, 0) and (0, 4). Area = ∫[0,2](4 − 2x)dx = [4x − x²]₀² = 8 − 4 = 4.
*(Or triangle: ½(2)(4) = 4.)*

**12. 4.** |x + 1| = −(x + 1) for x < −1 and (x + 1) for x ≥ −1. Split at x = −1:
∫[−3,−1] −(x+1)dx = [−x²/2 − x]₋₃⁻¹ = (−½ + 1) − (−9/2 + 3) = ½ + 3/2 = 2.
∫[−1,1](x+1)dx = [x²/2 + x]₋₁¹ = (½ + 1) − (½ − 1) = 2. Total = 4.

**Scoring.** Out of 35. Below 24 → the loss is nearly always in step 1 (no sketch) or step 4 (wrong
choice of variable / not splitting). Redo §3 Q3, Q7 and Q8 with a proper sketch each time.

---

## 6. Answering tips

1. **Draw the sketch. Always.** It carries an independent mark (typically 1 of the 5) and it is how
   you avoid every other error in this chapter. Label the axes, label each curve with its equation,
   mark the intersection points with coordinates, and **shade the required region**.

2. **Show the intersection algebra.** "Solving x² + y² = 32 and y = x gives 2x² = 32, so x = 4" — that
   line is a mark, and it produces your limits.

3. **State where the limits come from.** "The region runs from x = 0 to x = 4, where the line meets
   the circle." Do not let limits appear from nowhere.

4. **State the symmetry you are using.** "The parabola is symmetric about the x-axis, so the required
   area = 2 × (area above the axis)." A mark, and it halves your work.

5. **Split the integral when the boundary changes, and say why.** Two integrals with a clear reason
   score full; one integral over the whole range scores nothing.

6. **Never report a negative area.** If an integral comes out negative, the curve was below the axis
   there — take the modulus, and say so.

7. **Write "square units"** (or cm², if the problem had units). Missing units is a routine ½ mark.

8. **Do the geometric sanity check when you can.** Quarter-circle → πa²/4; triangle → ½bh;
   sector → (θ/2π)πa². If your integral disagrees with the obvious geometry, you have made an
   arithmetic error, and you now know before the examiner does.

9. **Keep the answer exact.** 4π, 8√3, 3(π − 2)/2 — not 12.57, 13.86, 1.71. A decimal in brackets
   afterwards is fine.

10. **When integrating w.r.t. y, rewrite the curve as x = g(y) explicitly** before setting up. Write
    "x = √y" or "x = y²/4" on its own line. Mixing up which variable you are integrating in is a
    complete loss of the question.

11. **Use the ∫√(a² − x²)dx formula rather than a trig substitution.** It is in the syllabus, it is
    faster, and the marking scheme expects it. Write it down before substituting your a.
