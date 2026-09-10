# Ch 11 — Three Dimensional Geometry

**Unit IV Vectors and 3D Geometry (14 marks, shared with Ch 10) · Typical appearance: 1–2 MCQs +
one 3-mark question, and very often a 5-marker (shortest distance between skew lines, or foot of
perpendicular / image of a point).**

---

## 1. Scope

### In the syllabus — **lines only**

- **Direction cosines and direction ratios** of a line joining two points
- **Cartesian and vector equations of a line**
- **Skew lines**
- **Shortest distance between two lines**
- **Angle between two lines**

### Deleted — do not study

**Every plane topic is out.** Specifically:

- Equation of a plane (vector, Cartesian, normal form, intercept form)
- Plane through three points; plane through the intersection of two planes
- **Angle between two planes**
- **Angle between a line and a plane**
- **Distance of a point from a plane**
- **Coplanarity** of two lines
- Distance between parallel planes

> **Read this twice.** Roughly half of every pre-2023 3D Geometry question involved a plane, so
> older question banks, sample papers and video playlists are heavily contaminated. If a practice
> question mentions a plane, an equation like ax + by + cz + d = 0, or a normal vector, **skip it**.
>
> The upside: the surviving topic list is short and every question comes from one of five templates,
> listed below.

---

## 2. Brief

### Start here — in plain English

This chapter is Chapter 10 put to work. It answers geometric questions about lines and planes in
space — the distance between two skew lines, the angle at which a line meets a plane, where a line
pierces a surface — and it answers them with dot and cross products rather than with drawing, which
is fortunate, because drawing in three dimensions is hard.

The one idea to hold on to is that **a line is a point plus a direction**, and **a plane is a point
plus a perpendicular**. Everything else follows.

A **line** is described by saying "start here, then head that way": r = a + λb, where a is the
position vector of a known point on the line, b is its direction, and λ is a dial you turn to slide
along it. Every point of the line is some value of λ. The cartesian form
(x − x₁)/a = (y − y₁)/b = (z − z₁)/c is the same statement — the numerators say how far you have
moved from the known point, the denominators are the direction, and setting the three ratios equal
just says you moved proportionally in all three axes. If a question gives you two points instead of a
direction, subtract them: the direction is the arrow from one to the other.

A **plane** is described differently, and this is the step that repays real thought. You cannot
specify a plane by a direction *in* it — there are infinitely many. What pins a plane down uniquely
is the direction **perpendicular** to it, called the **normal**. So a plane is "all the points whose
displacement from a known point is perpendicular to n", which in dot-product language is
(r − a)·n = 0, and rearranged, r·n = d. In cartesian form ax + by + cz = d, and the numbers a, b, c
*are* the normal's components — read them straight off. That single observation converts most plane
questions into vector arithmetic.

Now every standard question is one of these ideas with a dot or cross product attached, and the
pattern is worth seeing:

- **Angle between two lines** — the angle between their directions, so a dot product of the two b's.
- **Angle between two planes** — the angle between their *normals*, so a dot product of the two n's.
- **Angle between a line and a plane** — here is the trap. Dotting the line's direction with the
  plane's normal gives you the angle from the normal, not from the plane. The angle you want is its
  complement, so use **sin θ** where you would otherwise use cos. Every year someone loses this mark.
- **Perpendicular lines** — directions dot to zero. **Parallel lines** — directions cross to zero.
- **Parallel planes** — same normal (up to a scale factor).

**Distances** are the other family, and there the cross product does the work, because a cross
product measures the perpendicular part. The shortest distance from a point to a line, and the
shortest distance between two **skew** lines — lines that neither meet nor run parallel, which only
exist in three dimensions — both come out of the standard formulae in the formula sheet. For skew
lines the numerator is a scalar triple product and the denominator is |b₁ × b₂|, and the whole thing
is the projection of the gap between the lines onto the one direction perpendicular to both. Worth
knowing as a formula; worth understanding as a shadow.

Practical advice: this chapter is unusually formula-heavy, and the fastest way through it is not
memorising twelve formulae but recognising which of the five or six *situations* you are in. Read
the question and ask: is this a line or a plane, an angle or a distance? The formula follows from
that. And convert between vector and cartesian form fluently — questions often give you one and
expect the other, and that conversion is nothing more than reading off components.

**Learn it from someone else too**

- **Video lecture** — [search: three dimensional geometry class 12 one shot](https://www.youtube.com/results?search_query=three+dimensional+geometry+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: lines and planes in 3D](https://www.khanacademy.org/search?page_search_query=lines%20planes%20three%20dimensional%20geometry)
- **The book the paper is set from** — [NCERT Maths Part II, Chapter 11 (PDF)](https://ncert.nic.in/textbook/pdf/lemh205.pdf)
- **For extra problems** — NCERT exercises are the closest match to the board's phrasing; then
  Exemplar Chapter 11 for the skew-lines and image-of-a-point types.

---

### Direction cosines and direction ratios of a line

For a line through A(x₁, y₁, z₁) and B(x₂, y₂, z₂):

```
Direction ratios (DRs):   (x₂ − x₁, y₂ − y₁, z₂ − z₁)
```

Divide by the magnitude √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²] to get the **direction cosines**
(l, m, n), which satisfy

```
      l² + m² + n² = 1
```

Direction ratios are not unique — any non-zero scalar multiple of (a, b, c) is an equally valid set.
Direction cosines are unique up to overall sign.

### Equations of a line

**Through a point A(position vector a) with direction vector b:**

```
Vector form:      r = a + λ b                      (λ ∈ R, a parameter)

Cartesian form:   (x − x₁)/a₁  =  (y − y₁)/a₂  =  (z − z₁)/a₃
```

where b = a₁î + a₂ĵ + a₃k̂ and A = (x₁, y₁, z₁).

**Through two points A(a) and B(b):**

```
Vector form:      r = a + λ(b − a)

Cartesian form:   (x − x₁)/(x₂ − x₁)  =  (y − y₁)/(y₂ − y₁)  =  (z − z₁)/(z₂ − z₁)
```

**Reading the Cartesian form.** From

```
      (x − 2)/3 = (y + 1)/(−2) = (z − 4)/5
```

you read off: the line passes through **(2, −1, 4)** and has direction ratios **(3, −2, 5)**. Note
the sign flip on the y-coordinate: (y + 1) means y₁ = −1.

**A common trap in the Cartesian form.** If a denominator would be zero, the form is written with a
separate equation. For instance a line through (1, 2, 3) with DRs (0, 1, 2) is written
`x = 1, (y − 2)/1 = (z − 3)/2`. Never write a zero denominator.

**The general point on a line.** From (x − x₁)/a₁ = (y − y₁)/a₂ = (z − z₁)/a₃ = λ, the general point
is

```
      (a₁λ + x₁,  a₂λ + y₁,  a₃λ + z₁)
```

This parametrisation is the engine of half the questions in this chapter — intersections, feet of
perpendiculars, and images all start here.

### Angle between two lines

If the lines have direction vectors **b₁** and **b₂**:

```
      cos θ = | b₁ · b₂ | / ( |b₁| |b₂| )
```

In Cartesian terms, with DRs (a₁, b₁, c₁) and (a₂, b₂, c₂):

```
      cos θ = | a₁a₂ + b₁b₂ + c₁c₂ | / [ √(a₁²+b₁²+c₁²) · √(a₂²+b₂²+c₂²) ]
```

> **The modulus matters.** By convention the angle between two lines is taken as the acute one, so
> we use the absolute value of the dot product. (For the angle between two *vectors*, in Ch 10, you
> do **not** take the modulus — a negative dot product genuinely means an obtuse angle. Know the
> difference.)

**Special cases:**

```
Perpendicular:   a₁a₂ + b₁b₂ + c₁c₂ = 0
Parallel:        a₁/a₂ = b₁/b₂ = c₁/c₂
```

### Skew lines

Two lines in space are **skew** if they are **neither parallel nor intersecting**. Skew lines do not
lie in a common plane. In 2D this cannot happen; it is a genuinely three-dimensional phenomenon.

### Shortest distance — the two formulas

**Between two skew lines** r = a₁ + λb₁ and r = a₂ + μb₂:

```
      d  =  | (b₁ × b₂) · (a₂ − a₁) |  /  | b₁ × b₂ |
```

**Between two parallel lines** r = a₁ + λb and r = a₂ + μb (same direction vector b):

```
      d  =  | b × (a₂ − a₁) |  /  | b |
```

> **Which formula?** Check whether the direction vectors are proportional. If they are, the lines are
> parallel and the skew formula fails (it gives 0/0, since **b₁** × **b₂** = **0**). Making this check
> explicitly, and saying which case you are in, is a mark.

**If d = 0**, the lines **intersect**. So the skew-distance formula doubles as an intersection test.

### The five templates — every question in this chapter

**Template 1 — Equation of a line.** Given a point and either a direction or a second point. Write
both vector and Cartesian forms unless told otherwise.

**Template 2 — Angle between two lines.** Extract the DRs, apply the cos θ formula with a modulus.

**Template 3 — Shortest distance.** Identify a₁, b₁, a₂, b₂; check parallel or skew; apply the
matching formula.

**Template 4 — Foot of the perpendicular from a point P to a line.** Procedure:

1. Write the **general point Q** on the line in terms of λ.
2. Form the vector **PQ** = Q − P.
3. Impose **PQ · b = 0** (since PQ must be perpendicular to the line's direction).
4. Solve for λ, and substitute back to get Q — the foot of the perpendicular.
5. If asked, the perpendicular distance is |**PQ**|.

**Template 5 — Image of a point P in a line.** Find the foot of the perpendicular Q by Template 4;
then Q is the **midpoint** of P and its image P′, so

```
      P′ = 2Q − P
```

component-wise. This is the whole of the extra work — two lines.

**Bonus — show two lines intersect and find the point.** Write the general point of each line (in λ
and μ), equate all three coordinates to get three equations in two unknowns, solve two of them, and
**verify the third**. If the third is satisfied the lines intersect; if not, they are skew. The
verification step is essential and is a mark.

### Quick recall box

```
DRs of AB = (x₂−x₁, y₂−y₁, z₂−z₁);  divide by |AB| for direction cosines;  l²+m²+n² = 1

LINE:  r = a + λb        (x−x₁)/a₁ = (y−y₁)/a₂ = (z−z₁)/a₃
       through two points: r = a + λ(b−a)
       general point: (a₁λ+x₁, a₂λ+y₁, a₃λ+z₁)

ANGLE: cos θ = |b₁·b₂|/(|b₁||b₂|)          ← MODULUS (acute angle convention)
       ⊥ : a₁a₂+b₁b₂+c₁c₂ = 0      ∥ : a₁/a₂ = b₁/b₂ = c₁/c₂

SKEW distance:      d = |(b₁×b₂)·(a₂−a₁)| / |b₁×b₂|
PARALLEL distance:  d = |b×(a₂−a₁)| / |b|
d = 0  ⟹  the lines intersect

FOOT of ⊥ from P: general point Q(λ) → PQ·b = 0 → solve λ → Q
IMAGE of P:       P′ = 2Q − P
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* Find the shortest distance between the lines

```
      r = (î + 2ĵ + k̂) + λ(î − ĵ + k̂)          and          r = (2î − ĵ − k̂) + μ(2î + ĵ + 2k̂)
```

**Q2.** *(3 marks)* Find the angle between the lines

```
      (x − 2)/2 = (y − 1)/5 = (z + 3)/(−3)          and          (x + 2)/(−1) = (y − 4)/8 = (z − 5)/4
```

**Q3.** *(3 marks)* Find the vector and Cartesian equations of the line passing through the points
(−1, 0, 2) and (3, 4, 6).

**Q4.** *(5 marks)* Find the foot of the perpendicular drawn from the point P(1, 6, 3) to the line
x/1 = (y − 1)/2 = (z − 2)/3. Also find the length of the perpendicular.

**Q5.** *(5 marks)* Find the image of the point (1, 6, 3) in the line x/1 = (y − 1)/2 = (z − 2)/3.

**Q6.** *(5 marks)* Show that the lines

```
      (x − 1)/2 = (y − 2)/3 = (z − 3)/4          and          (x − 4)/5 = (y − 1)/2 = z/1
```

intersect, and find their point of intersection.

**Q7.** *(3 marks)* Find the shortest distance between the parallel lines

```
      r = (î + 2ĵ + 3k̂) + λ(2î + 3ĵ + 6k̂)          and          r = (3î + 3ĵ − 5k̂) + μ(2î + 3ĵ + 6k̂)
```

**Q8.** *(2 marks)* Find the direction cosines of the line joining A(2, −1, 3) and B(4, 3, −1).

**Q9.** *(2 marks)* Find the value of p so that the lines

```
      (x − 1)/3 = (y − 2)/(2p) = (z − 3)/2          and          (x − 1)/(3p) = (y − 5)/1 = (z − 6)/(−5)
```

are perpendicular.

**Q10.** *(2 marks)* Find the equation of the line passing through (2, −1, 3) and parallel to the
line r = (î − 2ĵ + k̂) + λ(2î + 3ĵ − k̂).

**Q11.** *(1 mark, MCQ)* The direction ratios of the line (x − 3)/2 = (2y − 1)/4 = z are
(a) (2, 4, 1) (b) (2, 2, 1) (c) (3, 1, 0) (d) (2, 4, 0)

---

## 4. Solutions

### Q1 — shortest distance between two skew lines

**Identify the four ingredients:**

```
      a₁ = î + 2ĵ + k̂          b₁ = î − ĵ + k̂
      a₂ = 2î − ĵ − k̂          b₂ = 2î + ĵ + 2k̂
```

**Check:** are they parallel? (1, −1, 1) and (2, 1, 2) are not proportional, so the lines are **not
parallel** — use the skew formula.

**Compute a₂ − a₁:**

```
      a₂ − a₁ = (2 − 1)î + (−1 − 2)ĵ + (−1 − 1)k̂ = î − 3ĵ − 2k̂
```

**Compute b₁ × b₂:**

```
                | î   ĵ   k̂ |
      b₁ × b₂ = | 1  −1   1 |
                | 2   1   2 |

              = î[(−1)(2) − (1)(1)] − ĵ[(1)(2) − (1)(2)] + k̂[(1)(1) − (−1)(2)]
              = î(−2 − 1) − ĵ(2 − 2) + k̂(1 + 2)
              = −3î + 0ĵ + 3k̂
```

```
      |b₁ × b₂| = √(9 + 0 + 9) = √18 = 3√2
```

**Compute the numerator:**

```
      (b₁ × b₂) · (a₂ − a₁) = (−3)(1) + (0)(−3) + (3)(−2) = −3 + 0 − 6 = −9
```

**Apply the formula:**

```
      d = |−9| / (3√2) = 9/(3√2) = 3/√2 = (3√2)/2
```

```
Shortest distance = 3/√2 = 3√2/2 units          ≈ 2.12 units
```

*(Since d ≠ 0, the lines are indeed skew — they neither meet nor are parallel.)*

### Q2 — angle between two lines

**Extract the direction ratios** from the Cartesian forms:

```
      b₁ = (2, 5, −3)          b₂ = (−1, 8, 4)
```

```
      b₁ · b₂ = (2)(−1) + (5)(8) + (−3)(4) = −2 + 40 − 12 = 26

      |b₁| = √(4 + 25 + 9) = √38
      |b₂| = √(1 + 64 + 16) = √81 = 9
```

```
      cos θ = |26| / (9√38) = 26/(9√38)
```

```
θ = cos⁻¹( 26/(9√38) )          ≈ cos⁻¹(0.469) ≈ 62.0°
```

### Q3 — line through (−1, 0, 2) and (3, 4, 6)

**Direction vector:**

```
      b = (3 − (−1))î + (4 − 0)ĵ + (6 − 2)k̂ = 4î + 4ĵ + 4k̂
```

Divide by 4 (direction ratios are only defined up to a scalar):

```
      b = î + ĵ + k̂
```

**Vector equation**, taking a = −î + 0ĵ + 2k̂:

```
      r = (−î + 2k̂) + λ(î + ĵ + k̂)
```

**Cartesian equation:**

```
      (x + 1)/1 = (y − 0)/1 = (z − 2)/1
```

i.e.

```
      x + 1 = y = z − 2
```

### Q4 — foot of the perpendicular from P(1, 6, 3)

The line is x/1 = (y − 1)/2 = (z − 2)/3, so it passes through (0, 1, 2) with DRs **b** = (1, 2, 3).

**Step 1 — general point Q on the line.** Set each ratio equal to λ:

```
      Q = (λ, 2λ + 1, 3λ + 2)
```

**Step 2 — the vector PQ:**

```
      PQ = Q − P = (λ − 1, 2λ + 1 − 6, 3λ + 2 − 3) = (λ − 1, 2λ − 5, 3λ − 1)
```

**Step 3 — impose PQ ⊥ b, i.e. PQ · b = 0:**

```
      (λ − 1)(1) + (2λ − 5)(2) + (3λ − 1)(3) = 0
⟹     λ − 1 + 4λ − 10 + 9λ − 3 = 0
⟹     14λ − 14 = 0
⟹     λ = 1
```

**Step 4 — substitute back:**

```
      Q = (1, 2(1) + 1, 3(1) + 2) = (1, 3, 5)
```

**The foot of the perpendicular is (1, 3, 5).**

**Step 5 — length of the perpendicular:**

```
      PQ = (1 − 1, 3 − 6, 5 − 3) = (0, −3, 2)

      |PQ| = √(0 + 9 + 4) = √13
```

**The length of the perpendicular is √13 units.**

### Q5 — image of (1, 6, 3) in the same line

From Q4, the foot of the perpendicular is **Q(1, 3, 5)**.

Q is the **midpoint** of P(1, 6, 3) and its image P′(x′, y′, z′). So

```
      (1 + x′)/2 = 1   ⟹   x′ = 1
      (6 + y′)/2 = 3   ⟹   y′ = 0
      (3 + z′)/2 = 5   ⟹   z′ = 7
```

*(Equivalently P′ = 2Q − P = (2 − 1, 6 − 6, 10 − 3) = (1, 0, 7).)*

**The image of (1, 6, 3) in the line is (1, 0, 7).**

*Check:* the midpoint of (1, 6, 3) and (1, 0, 7) is (1, 3, 5) = Q ✓

### Q6 — show the lines intersect, and find the point

**General point on line 1** (setting each ratio equal to λ):

```
      P₁ = (2λ + 1, 3λ + 2, 4λ + 3)
```

**General point on line 2** (setting each ratio equal to μ):

```
      P₂ = (5μ + 4, 2μ + 1, μ)
```

**If the lines intersect, some λ and μ make P₁ = P₂.** Equating coordinates:

```
      2λ + 1 = 5μ + 4          …(i)
      3λ + 2 = 2μ + 1          …(ii)
      4λ + 3 = μ               …(iii)
```

**Solve (ii) and (iii).** Substitute μ from (iii) into (ii):

```
      3λ + 2 = 2(4λ + 3) + 1
⟹     3λ + 2 = 8λ + 7
⟹     −5λ = 5
⟹     λ = −1
```

Then from (iii): μ = 4(−1) + 3 = **−1**.

**Verify in (i)** — this step is essential:

```
      LHS = 2(−1) + 1 = −1
      RHS = 5(−1) + 4 = −1          ✓
```

All three equations are satisfied, so **the lines intersect**.

**Point of intersection** (substituting λ = −1 into P₁):

```
      (2(−1) + 1, 3(−1) + 2, 4(−1) + 3) = (−1, −1, −1)
```

**The lines intersect at (−1, −1, −1).**

*Check with P₂ at μ = −1: (5(−1) + 4, 2(−1) + 1, −1) = (−1, −1, −1) ✓*

### Q7 — shortest distance between parallel lines

**Check they are parallel:** both have direction vector **b** = 2î + 3ĵ + 6k̂. **Parallel.** So use
the parallel-lines formula.

```
      a₁ = î + 2ĵ + 3k̂          a₂ = 3î + 3ĵ − 5k̂

      a₂ − a₁ = 2î + ĵ − 8k̂
```

```
                      | î   ĵ   k̂ |
      b × (a₂ − a₁) = | 2   3   6 |
                      | 2   1  −8 |

                    = î[(3)(−8) − (6)(1)] − ĵ[(2)(−8) − (6)(2)] + k̂[(2)(1) − (3)(2)]
                    = î(−24 − 6) − ĵ(−16 − 12) + k̂(2 − 6)
                    = −30î + 28ĵ − 4k̂
```

```
      |b × (a₂ − a₁)| = √(900 + 784 + 16) = √1700 = 10√17

      |b| = √(4 + 9 + 36) = √49 = 7
```

```
      d = 10√17 / 7
```

```
Shortest distance = 10√17/7 units          ≈ 5.89 units
```

### Q8 — direction cosines of AB, A(2, −1, 3), B(4, 3, −1)

```
      AB = (4 − 2, 3 − (−1), −1 − 3) = (2, 4, −4)

      |AB| = √(4 + 16 + 16) = √36 = 6
```

```
      Direction cosines = (2/6, 4/6, −4/6) = (1/3, 2/3, −2/3)
```

*Check:* 1/9 + 4/9 + 4/9 = 9/9 = 1 ✓

### Q9 — find p for perpendicularity

DRs: **b₁** = (3, 2p, 2) and **b₂** = (3p, 1, −5).

Perpendicular ⟺ **b₁**·**b₂** = 0:

```
      (3)(3p) + (2p)(1) + (2)(−5) = 0
⟹     9p + 2p − 10 = 0
⟹     11p = 10
⟹     p = 10/11
```

### Q10 — line through (2, −1, 3) parallel to a given line

A parallel line has the **same direction vector**, **b** = 2î + 3ĵ − k̂. The position vector of the
given point is **a** = 2î − ĵ + 3k̂.

**Vector form:**

```
      r = (2î − ĵ + 3k̂) + λ(2î + 3ĵ − k̂)
```

**Cartesian form:**

```
      (x − 2)/2 = (y + 1)/3 = (z − 3)/(−1)
```

### Q11 — direction ratios of (x − 3)/2 = (2y − 1)/4 = z

The middle term is not in standard form — the coefficient of y must be 1. Rewrite:

```
      (2y − 1)/4 = 2(y − ½)/4 = (y − ½)/2
```

So the line is

```
      (x − 3)/2 = (y − ½)/2 = (z − 0)/1
```

giving direction ratios **(2, 2, 1)**.

**Answer: (b) (2, 2, 1)**

> This is a favourite trap. Always normalise so that the coefficient of x, y and z inside each
> bracket is 1 before reading off the direction ratios.

---

## 5. Test yourself

Time: 50 minutes. Answers below.

1. *(1)* The direction ratios of the line (x + 1)/3 = (y − 2)/(−1) = (z + 4)/2 are
   (a) (−1, 2, −4) (b) (3, −1, 2) (c) (1, −2, 4) (d) (3, 1, 2)
2. *(1)* Two lines with direction ratios (1, 2, 3) and (−2, 1, 0) are
   (a) parallel (b) perpendicular (c) neither (d) coincident
3. *(1)* If the direction cosines of a line are (1/√3, 1/√3, k), then k is
   (a) 1/√3 (b) ±1/√3 (c) 1/3 (d) 0
4. *(2)* Find the direction cosines of the line joining (1, 0, 0) and (0, 1, 1).
5. *(2)* Find the Cartesian equation of the line r = (2î − ĵ + 4k̂) + λ(î + 2ĵ − k̂).
6. *(2)* Find the vector equation of the line through (1, 2, 3) and (4, 5, 6).
7. *(3)* Find the angle between the lines with direction ratios (2, 2, 1) and (4, 1, 8).
8. *(3)* Find k so that the lines (x − 1)/(−3) = (y − 2)/(2k) = (z − 3)/2 and
   (x − 1)/(3k) = (y − 1)/1 = (z − 6)/(−5) are perpendicular.
9. *(5)* Find the shortest distance between the lines
   r = (î + ĵ) + λ(2î − ĵ + k̂) and r = (2î + ĵ − k̂) + μ(3î − 5ĵ + 2k̂).
10. *(5)* Find the foot of the perpendicular and the perpendicular distance from P(2, 3, 4) to the
    line (x + 3)/3 = (y − 2)/6 = z/2.
11. *(5)* Show that the lines (x + 1)/3 = (y + 3)/5 = (z + 5)/7 and (x − 2)/1 = (y − 4)/3 = (z − 6)/5
    intersect, and find the point.
12. *(3)* Find the shortest distance between the parallel lines
    r = (î + ĵ − k̂) + λ(î − ĵ + k̂) and r = (2î − ĵ + k̂) + μ(î − ĵ + k̂).
13. *(2)* Find the point on the line (x − 1)/2 = (y + 1)/3 = z/1 corresponding to the parameter
    value λ = 2.

### Answer key

**1. (b) (3, −1, 2).**

**2. (b) perpendicular.** Dot product = (1)(−2) + (2)(1) + (3)(0) = −2 + 2 + 0 = 0.
*(Always compute the dot product before choosing — "neither" is the distractor here.)*

**3. (b) ±1/√3.** l² + m² + n² = 1 ⟹ 1/3 + 1/3 + k² = 1 ⟹ k² = 1/3 ⟹ k = ±1/√3.

**4. (−1/√3, 1/√3, 1/√3).** AB = (−1, 1, 1), |AB| = √3.

**5. (x − 2)/1 = (y + 1)/2 = (z − 4)/(−1).**

**6. r = (î + 2ĵ + 3k̂) + λ(3î + 3ĵ + 3k̂), or with b simplified to î + ĵ + k̂.**

**7. cos⁻¹(2/3).** DRs (2, 2, 1) and (4, 1, 8): dot = 8 + 2 + 8 = 18; magnitudes 3 and 9.
cos θ = 18/27 = 2/3. θ = cos⁻¹(2/3) ≈ 48.2°.

**8. k = −10/7.** Dot = (−3)(3k) + (2k)(1) + (2)(−5) = −9k + 2k − 10 = −7k − 10 = 0 ⟹ k = −10/7.

**9. 10/√59.** a₂ − a₁ = î + 0ĵ − k̂. b₁ = (2, −1, 1), b₂ = (3, −5, 2).
b₁ × b₂ = î((−1)(2) − (1)(−5)) − ĵ((2)(2) − (1)(3)) + k̂((2)(−5) − (−1)(3))
= î(−2 + 5) − ĵ(4 − 3) + k̂(−10 + 3) = 3î − ĵ − 7k̂. |b₁ × b₂| = √(9 + 1 + 49) = √59.
(b₁ × b₂)·(a₂ − a₁) = 3(1) + (−1)(0) + (−7)(−1) = 3 + 7 = 10.
**d = 10/√59 ≈ 1.30 units.**

**10. Foot = (−60/49, 272/49, 58/49); distance ≈ 4.98 units.**
General point Q = (3λ − 3, 6λ + 2, 2λ).
PQ = (3λ − 5, 6λ − 1, 2λ − 4). PQ·(3, 6, 2) = 9λ − 15 + 36λ − 6 + 4λ − 8 = 49λ − 29 = 0 ⟹ λ = 29/49.
Q = (3(29/49) − 3, 6(29/49) + 2, 2(29/49)) = (87/49 − 147/49, 174/49 + 98/49, 58/49)
= (−60/49, 272/49, 58/49).
PQ = (−60/49 − 98/49, 272/49 − 147/49, 58/49 − 196/49) = (−158/49, 125/49, −138/49).
|PQ| = (1/49)√(24964 + 15625 + 19044) = (1/49)√59633 ≈ 244.2/49 ≈ 4.98 units.
*(Not every such problem gives whole numbers — do not assume a slip when the answer is fractional.)*

**11. They intersect at (½, −½, −3/2).**
General points: (3λ − 1, 5λ − 3, 7λ − 5) and (μ + 2, 3μ + 4, 5μ + 6).
3λ − 1 = μ + 2 …(i);  5λ − 3 = 3μ + 4 …(ii);  7λ − 5 = 5μ + 6 …(iii).
From (i): μ = 3λ − 3. Into (ii): 5λ − 3 = 3(3λ − 3) + 4 = 9λ − 5 ⟹ −4λ = −2 ⟹ λ = ½, μ = −3/2.
Check (iii): LHS = 7(½) − 5 = −3/2; RHS = 5(−3/2) + 6 = −15/2 + 12/2 = −3/2 ✓
**Point of intersection = (3(½) − 1, 5(½) − 3, 7(½) − 5) = (½, −½, −3/2).**

**12. √(2/3) = √6/3.** b = (1, −1, 1), |b| = √3. a₂ − a₁ = (1, −2, 2).
b × (a₂ − a₁) = î((−1)(2) − (1)(−2)) − ĵ((1)(2) − (1)(1)) + k̂((1)(−2) − (−1)(1))
= î(−2 + 2) − ĵ(2 − 1) + k̂(−2 + 1) = 0î − ĵ − k̂. |·| = √2.
**d = √2/√3 = √6/3 ≈ 0.82 units.**

**13. (5, 5, 2).** General point (2λ + 1, 3λ − 1, λ); at λ = 2 this is (5, 5, 2).

**Scoring.** Out of 34. Below 24 → almost always the cross-product sign pattern or mis-reading DRs
from the Cartesian form. Redo §3 Q1, Q4, Q11.

---

## 6. Answering tips

1. **Write down a₁, b₁, a₂, b₂ as a labelled list before doing anything.** Four lines. Every
   shortest-distance question is lost by mixing up which vector is which, and this prevents it
   entirely.

2. **Check parallel-vs-skew explicitly, and say which formula you are using.** "The direction ratios
   (1, −1, 1) and (2, 1, 2) are not proportional, so the lines are skew; using
   d = |(b₁×b₂)·(a₂−a₁)|/|b₁×b₂| …". That sentence is a mark and it stops you applying the wrong
   formula.

3. **Normalise the Cartesian form before reading direction ratios.** (2y − 1)/4 must become
   (y − ½)/2. Anything with a coefficient on x, y or z inside the numerator needs this step.

4. **Watch the signs when reading the point.** (y + 3)/5 means y₁ = **−3**, not +3.

5. **Take the modulus in the angle formula.** cos θ = |**b₁**·**b₂**|/(|**b₁**||**b₂**|). Without it
   you may report an obtuse angle where the convention wants the acute one.

6. **For intersection questions, verify the third equation and say you are doing so.** Solving two of
   three and stopping is worth about half the marks; the verification is what proves intersection
   rather than skewness.

7. **For foot-of-perpendicular questions, write the general point with a stated parameter.** "Let
   Q = (λ, 2λ + 1, 3λ + 2) be a general point on the line." Then PQ, then PQ·b = 0. Four visible
   steps, four marks.

8. **For the image, state that the foot is the midpoint.** "Since Q is the midpoint of PP′, we have
   P′ = 2Q − P." One line, and it is the mark that distinguishes this question from the previous one.

9. **The cross product's middle term is negative.** Write −ĵ(…) explicitly. In this chapter that
   error costs a full 5-mark question, since everything downstream depends on it.

10. **Give the answer with units** — "units" for a distance, and put it in a final boxed line.

11. **Do the arithmetic check when the answer is a point.** Substituting your intersection point or
    your foot of perpendicular back into the line's equation takes twenty seconds and confirms the
    whole question.

12. **Do not be alarmed by fractional answers.** Feet of perpendiculars often come out as
    thirds or forty-ninths. A messy fraction is not evidence of an error — recheck once, then trust
    your working.
