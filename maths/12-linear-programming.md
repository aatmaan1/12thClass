# Ch 12 — Linear Programming

**Unit V (5 marks) · Typical appearance: one 4- or 5-mark graphical question, plus sometimes a
1-mark corner-point MCQ. Completely templated — there is no excuse for losing marks here.**

---

## 1. Scope

### In the syllabus

- Introduction and related **terminology**: constraints, objective function, optimisation
- **Graphical method** of solution for problems in **two variables**
- **Feasible and infeasible regions** (bounded or unbounded)
- Feasible and infeasible solutions; **optimal feasible solutions**
- Restricted to **up to three non-trivial constraints**

### Deleted — do not study

- The named **problem types** as separate categories: diet problems, manufacturing problems,
  transportation problems
- Problems with **more than three** non-trivial constraints

> **What "three non-trivial constraints" means for you.** Beyond x ≥ 0 and y ≥ 0 (the trivial ones),
> you will never face more than three inequalities. That caps the feasible region at a small polygon
> with at most five corner points. There is a hard ceiling on how difficult this question can be.

---

## 2. Brief

### Terminology — know these words, they get asked directly

| Term | Meaning |
| --- | --- |
| **Decision variables** | The quantities you are solving for, usually x and y |
| **Objective function** | The linear expression Z = ax + by to be maximised or minimised |
| **Constraints** | The linear inequalities the variables must satisfy |
| **Non-negative constraints** | x ≥ 0, y ≥ 0 (the "trivial" constraints) |
| **Feasible region** | The set of all points satisfying *all* the constraints simultaneously |
| **Feasible solution** | Any point in the feasible region |
| **Infeasible solution** | Any point outside it |
| **Optimal (feasible) solution** | A feasible point at which Z attains its required maximum or minimum |
| **Bounded region** | The feasible region can be enclosed in a circle |
| **Unbounded region** | It cannot — it extends indefinitely |

### The two theorems that make the method work

**Theorem 1.** If the feasible region R is non-empty and Z = ax + by has an optimal value there, then
that optimal value occurs at a **corner point (vertex)** of R.

**Theorem 2.**
- If R is **bounded**, then Z has **both** a maximum and a minimum on R, and each occurs at a corner
  point.
- If R is **unbounded**, a maximum or minimum **may not exist**. If it does, it occurs at a corner
  point — but you must **verify** it exists.

This pair is why the method is just "check the corners".

### The corner-point method — the fixed procedure

Follow this order exactly. Each step is a mark.

1. **Write all the constraints as inequalities**, including x ≥ 0 and y ≥ 0. If the question is a word
   problem, tabulate the data first and then translate.

2. **Convert each inequality to its boundary line** (replace ≤ or ≥ with =) and find two points on
   each line — usually the axis intercepts.

3. **Draw the graph on graph paper.** State the scale. Label each line with its equation.

4. **Shade the feasible region.** For each inequality, test the origin (0, 0): if it satisfies the
   inequality, shade the side containing the origin; if not, shade the other side. The feasible
   region is the intersection of all shaded regions.

5. **Find every corner point exactly**, by solving the relevant pair of simultaneous equations. Do
   **not** read coordinates off the graph — the grid will lie to you and the marking scheme wants the
   algebra.

6. **Tabulate Z at each corner point.**

| Corner point | Z = ax + by |
| --- | --- |
| … | … |

7. **State the optimum**: the value, the point at which it occurs, and whether it is a maximum or
   minimum.

8. **If the region is unbounded, do the existence check** (next section). This is the mark most
   students drop.

### The unbounded-region check

Suppose the region is unbounded and M is the largest value of Z at the corner points.

```
M is the MAXIMUM  ⟺  the open half-plane  ax + by > M  has NO point in common with the feasible region.
```

Similarly, if m is the smallest corner value:

```
m is the MINIMUM  ⟺  the open half-plane  ax + by < m  has NO point in common with the feasible region.
```

**How to do the check in practice.** Sketch the line ax + by = M (or = m). If the feasible region
lies entirely on one side of it, the optimum exists. If the region pokes through to the other side,
no optimum exists in that direction.

**The rule of thumb** (state the check anyway, but this tells you what to expect): if the feasible
region is unbounded "upwards and to the right" (typical of ≥ constraints), and a, b > 0, then Z has a
**minimum** but **no maximum**.

**Write the check as a sentence**, e.g.: "Since the feasible region is unbounded, we check whether
3x + 5y < 7 has any point in common with it. It does not, so the minimum value of Z is 7."

### Two special outcomes

**Multiple optimal solutions.** If Z takes the same optimal value at **two** corner points, then it
takes that value at **every point on the line segment joining them**, so there are infinitely many
optimal solutions. Say so explicitly.

**No feasible solution.** If the constraints are mutually contradictory, the feasible region is
empty and the LPP has **no solution**. For example x − y ≤ −1 (i.e. y ≥ x + 1) together with
−x + y ≤ 0 (i.e. y ≤ x) cannot both hold. State: "The feasible region is empty, hence the problem
has no feasible solution."

### Quick recall box

```
Z = ax + by  is the objective function; the inequalities are the constraints.

CORNER-POINT METHOD:
  1. list constraints (incl. x ≥ 0, y ≥ 0)
  2. boundary lines + intercepts
  3. graph on graph paper, state scale, label lines
  4. shade feasible region (test the origin for each inequality)
  5. find corner points by SOLVING SIMULTANEOUS EQUATIONS (not by reading the graph)
  6. table of Z at each corner
  7. state optimum: value, point, max/min
  8. if UNBOUNDED: check whether ax+by > M (or < m) meets the region

Bounded region  → max AND min both exist, at corners
Unbounded region → may not exist; must check
Equal Z at two corners → infinitely many optima, all along that segment
Contradictory constraints → empty feasible region → no feasible solution
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* Maximise Z = 4x + y subject to
x + y ≤ 50, 3x + y ≤ 90, x ≥ 0, y ≥ 0.

**Q2.** *(5 marks)* Minimise Z = 3x + 5y subject to
x + 3y ≥ 3, x + y ≥ 2, x ≥ 0, y ≥ 0.

**Q3.** *(5 marks)* Minimise **and** maximise Z = 5x + 10y subject to
x + 2y ≤ 120, x + y ≥ 60, x − 2y ≥ 0, x ≥ 0, y ≥ 0.

**Q4.** *(2 marks)* Show that the LPP "Maximise Z = x + y subject to x − y ≤ −1, −x + y ≤ 0,
x ≥ 0, y ≥ 0" has no feasible solution.

**Q5.** *(3 marks)* The corner points of the feasible region of an LPP are (0, 3), (1, 1) and (3, 0).
If Z = px + qy with p, q > 0, and the minimum of Z occurs at **both** (3, 0) and (1, 1), find the
relation between p and q.

**Q6.** *(1 mark, MCQ)* The corner points of a bounded feasible region are (0, 0), (4, 0), (2, 4)
and (0, 5). The maximum of Z = 3x + 2y is
(a) 12 (b) 14 (c) 10 (d) 22

**Q7.** *(4 marks)* Maximise Z = 3x + 4y subject to x + y ≤ 4, x ≥ 0, y ≥ 0.

**Q8.** *(4 marks, case study)* A manufacturer produces two products, A and B. Each unit of A
requires 2 hours on machine M₁ and 1 hour on M₂; each unit of B requires 1 hour on M₁ and 2 hours on
M₂. M₁ is available for 10 hours and M₂ for 8 hours per day. The profit is ₹5 per unit of A and ₹3
per unit of B.
(i) Formulate this as an LPP.
(ii) Find the corner points of the feasible region.
(iii) Find the maximum profit and the production plan that achieves it.

---

## 4. Solutions

### Q1 — Maximise Z = 4x + y

**Constraints:**

```
      x + y ≤ 50            …(i)
      3x + y ≤ 90           …(ii)
      x ≥ 0, y ≥ 0
```

**Boundary lines and intercepts:**

```
      x + y = 50    →  (50, 0) and (0, 50)
      3x + y = 90   →  (30, 0) and (0, 90)
```

**Origin test.** (0, 0) satisfies both (i) and (ii) (0 ≤ 50 ✓, 0 ≤ 90 ✓), so shade the side
containing the origin for each. With x, y ≥ 0 the feasible region is a **bounded** quadrilateral in
the first quadrant.

**Corner points.**

- **(0, 0)** — the origin
- **(30, 0)** — where 3x + y = 90 meets the x-axis (note x + y = 50 meets it at (50,0), which is
  outside (ii) since 3(50) = 150 > 90, so (30,0) is the binding one)
- **(0, 50)** — where x + y = 50 meets the y-axis (the point (0,90) violates (i))
- **Intersection of (i) and (ii):**

```
      x + y = 50
      3x + y = 90
```

Subtracting: 2x = 40 ⟹ **x = 20**, and then y = 30. So the point is **(20, 30)**.

**Table of Z = 4x + y:**

| Corner point | Z = 4x + y |
| --- | --- |
| (0, 0) | 0 |
| (30, 0) | 120 + 0 = **120** |
| (20, 30) | 80 + 30 = 110 |
| (0, 50) | 0 + 50 = 50 |

Since the feasible region is **bounded**, the maximum exists and occurs at a corner point.

```
Maximum Z = 120, at the point (30, 0)
```

### Q2 — Minimise Z = 3x + 5y

**Constraints:**

```
      x + 3y ≥ 3            …(i)
      x + y ≥ 2             …(ii)
      x ≥ 0, y ≥ 0
```

**Boundary lines:**

```
      x + 3y = 3   →  (3, 0) and (0, 1)
      x + y = 2    →  (2, 0) and (0, 2)
```

**Origin test.** (0, 0) gives 0 ≥ 3 ✗ and 0 ≥ 2 ✗, so shade **away** from the origin for both. The
feasible region is therefore **unbounded** (it extends up and to the right).

**Corner points.**

- **(3, 0)** — where x + 3y = 3 meets the x-axis (and (2,0) fails (i): 2 ≥ 3 ✗)
- **(0, 2)** — where x + y = 2 meets the y-axis (and (0,1) fails (ii): 1 ≥ 2 ✗)
- **Intersection of (i) and (ii):**

```
      x + 3y = 3
      x +  y = 2
```

Subtracting: 2y = 1 ⟹ **y = 1/2**, and then x = 3/2. So the point is **(3/2, 1/2)**.

**Table of Z = 3x + 5y:**

| Corner point | Z = 3x + 5y |
| --- | --- |
| (3, 0) | 9 + 0 = 9 |
| (3/2, 1/2) | 4.5 + 2.5 = **7** |
| (0, 2) | 0 + 10 = 10 |

The smallest corner value is 7. **But the region is unbounded, so we must check.**

**The unbounded check.** Consider the open half-plane 3x + 5y < 7. The line 3x + 5y = 7 passes
through (7/3, 0) ≈ (2.33, 0) and (0, 7/5) = (0, 1.4). Every point of the feasible region lies on or
above this line — the feasible region has **no point in common** with 3x + 5y < 7.

Hence 7 is genuinely the minimum.

```
Minimum Z = 7, at the point (3/2, 1/2)
```

*(Note that Z has **no maximum** here: the region is unbounded upwards and both coefficients are
positive, so Z can be made arbitrarily large.)*

### Q3 — Minimise and maximise Z = 5x + 10y

**Constraints:**

```
      x + 2y ≤ 120          …(i)
      x + y ≥ 60            …(ii)
      x − 2y ≥ 0            …(iii)
      x ≥ 0, y ≥ 0
```

**Boundary lines:**

```
      x + 2y = 120  →  (120, 0) and (0, 60)
      x + y = 60    →  (60, 0) and (0, 60)
      x − 2y = 0    →  passes through (0, 0) and (40, 20)
```

**Corner points.** The feasible region is a **bounded** quadrilateral. Its vertices:

- **(60, 0)** — where x + y = 60 meets the x-axis; check (i): 60 ≤ 120 ✓, (iii): 60 ≥ 0 ✓
- **(120, 0)** — where x + 2y = 120 meets the x-axis; check (ii): 120 ≥ 60 ✓, (iii): 120 ≥ 0 ✓
- **Intersection of (i) and (iii):**

```
      x + 2y = 120
      x − 2y = 0
```

Adding: 2x = 120 ⟹ x = 60, y = 30. Point **(60, 30)**. Check (ii): 90 ≥ 60 ✓

- **Intersection of (ii) and (iii):**

```
      x +  y = 60
      x − 2y = 0     ⟹  x = 2y
```

So 2y + y = 60 ⟹ y = 20, x = 40. Point **(40, 20)**. Check (i): 40 + 40 = 80 ≤ 120 ✓

**Table of Z = 5x + 10y:**

| Corner point | Z = 5x + 10y |
| --- | --- |
| (60, 0) | 300 + 0 = **300** |
| (120, 0) | 600 + 0 = **600** |
| (60, 30) | 300 + 300 = **600** |
| (40, 20) | 200 + 200 = 400 |

```
Minimum Z = 300, at (60, 0)

Maximum Z = 600, attained at BOTH (120, 0) and (60, 30)
```

Since the maximum occurs at two corner points, **it occurs at every point on the line segment
joining (120, 0) and (60, 30)** — there are infinitely many optimal solutions.

### Q4 — no feasible solution

**Rewrite the constraints:**

```
      x − y ≤ −1     ⟹     y ≥ x + 1          …(i)
      −x + y ≤ 0     ⟹     y ≤ x              …(ii)
```

From (i), y ≥ x + 1; from (ii), y ≤ x. Combining:

```
      x + 1 ≤ y ≤ x
⟹     x + 1 ≤ x
⟹     1 ≤ 0,   which is impossible
```

So no point (x, y) satisfies both constraints. **The feasible region is empty**, and the LPP has
**no feasible solution**.

*(Graphically: the half-plane above the line y = x + 1 and the half-plane below y = x are disjoint,
since those two lines are parallel and distinct.)*

### Q5 — relation between p and q

Z = px + qy, and the **minimum** occurs at both (3, 0) and (1, 1). Equal Z values at those points:

```
      Z(3, 0) = 3p + 0 = 3p
      Z(1, 1) = p + q
```

```
      3p = p + q
⟹     2p = q
```

```
q = 2p          (equivalently p = q/2)
```

*(Check the third corner is not lower: Z(0, 3) = 3q = 6p, which exceeds 3p since p > 0 ✓ — so the
minimum really is at those two points, and hence along the segment joining them.)*

### Q6 — maximum of Z = 3x + 2y at given corners

| Corner point | Z = 3x + 2y |
| --- | --- |
| (0, 0) | 0 |
| (4, 0) | 12 |
| (2, 4) | 6 + 8 = **14** |
| (0, 5) | 0 + 10 = 10 |

**Answer: (b) 14**

### Q7 — Maximise Z = 3x + 4y subject to x + y ≤ 4

**Constraints:** x + y ≤ 4, x ≥ 0, y ≥ 0.

**Boundary line:** x + y = 4 → (4, 0) and (0, 4).

**Origin test:** (0, 0) gives 0 ≤ 4 ✓, so shade towards the origin. The feasible region is the
**bounded** triangle with vertices (0, 0), (4, 0), (0, 4).

| Corner point | Z = 3x + 4y |
| --- | --- |
| (0, 0) | 0 |
| (4, 0) | 12 |
| (0, 4) | **16** |

```
Maximum Z = 16, at the point (0, 4)
```

### Q8 — case study: manufacturer

**(i) Formulation.**

Let x = number of units of A produced per day, y = number of units of B.

Tabulating the data:

| | Machine M₁ (hours) | Machine M₂ (hours) | Profit (₹) |
| --- | --- | --- | --- |
| Product A (x units) | 2 | 1 | 5 |
| Product B (y units) | 1 | 2 | 3 |
| **Available / total** | 10 | 8 | maximise |

```
Maximise    Z = 5x + 3y                (profit in ₹)

subject to  2x + y ≤ 10                (machine M₁ time)
            x + 2y ≤ 8                 (machine M₂ time)
            x ≥ 0,  y ≥ 0
```

**(ii) Corner points.**

Boundary lines: 2x + y = 10 → (5, 0) and (0, 10); x + 2y = 8 → (8, 0) and (0, 4).

- **(0, 0)**
- **(5, 0)** — where 2x + y = 10 meets the x-axis; check x + 2y ≤ 8: 5 ≤ 8 ✓
- **(0, 4)** — where x + 2y = 8 meets the y-axis; check 2x + y ≤ 10: 4 ≤ 10 ✓
- **Intersection:**

```
      2x + y = 10          …multiply by 2:  4x + 2y = 20
      x + 2y = 8
```

Subtracting: 3x = 12 ⟹ **x = 4**, then y = 10 − 8 = **2**. Point **(4, 2)**.

**Corner points: (0, 0), (5, 0), (4, 2), (0, 4).**

**(iii) Maximum profit.**

| Corner point | Z = 5x + 3y |
| --- | --- |
| (0, 0) | 0 |
| (5, 0) | 25 |
| (4, 2) | 20 + 6 = **26** |
| (0, 4) | 12 |

```
Maximum profit = ₹26, by producing 4 units of A and 2 units of B per day.
```

*(Check both machine constraints at (4, 2): M₁ uses 2(4) + 2 = 10 hours ✓ exactly available;
M₂ uses 4 + 2(2) = 8 hours ✓ exactly available. Both machines are fully utilised — a good sign that
the optimum is at the intersection.)*

---

## 5. Test yourself

Time: 45 minutes. Answers below. **Draw the graph for every question** — it is part of the marks.

1. *(1)* The optimal value of the objective function of an LPP is attained at
   (a) any point of the feasible region (b) a corner point of the feasible region
   (c) the origin only (d) the centre of the feasible region
2. *(1)* If the feasible region of an LPP is unbounded, then
   (a) both max and min always exist (b) neither exists
   (c) max or min may not exist (d) only the max exists
3. *(1)* The corner points of a feasible region are (0, 0), (3, 0), (2, 2), (0, 4). The minimum of
   Z = 4x + 6y is
   (a) 0 (b) 12 (c) 20 (d) 24
4. *(4)* Maximise Z = 5x + 3y subject to 3x + 5y ≤ 15, 5x + 2y ≤ 10, x ≥ 0, y ≥ 0.
5. *(4)* Minimise Z = −3x + 4y subject to x + 2y ≤ 8, 3x + 2y ≤ 12, x ≥ 0, y ≥ 0.
6. *(4)* Maximise Z = 3x + 2y subject to x + 2y ≤ 10, 3x + y ≤ 15, x ≥ 0, y ≥ 0.
7. *(5)* Minimise Z = 200x + 500y subject to x + 2y ≥ 10, 3x + 4y ≤ 24, x ≥ 0, y ≥ 0.
8. *(5)* Maximise Z = x + y subject to x + 4y ≤ 8, 2x + 3y ≤ 12, 3x + y ≤ 9, x ≥ 0, y ≥ 0.
9. *(3)* The corner points of the feasible region are (0, 4), (2, 2) and (6, 0). If
   Z = ax + by (a, b > 0) has the same minimum at (2, 2) and (6, 0), find a relation between a and b.
10. *(2)* Show that the constraints x + y ≤ 2, x + y ≥ 5, x ≥ 0, y ≥ 0 give an infeasible LPP.

### Answer key

**1. (b) a corner point of the feasible region.**

**2. (c) max or min may not exist.**

**3. (a) 0.** Z at (0,0) = 0; (3,0) = 12; (2,2) = 8 + 12 = 20; (0,4) = 24. Minimum is 0.

**4. Maximum Z = 235/19 at (20/19, 45/19).**
Corners: (0, 0), (2, 0), (0, 3), and the intersection of 3x + 5y = 15 with 5x + 2y = 10.
Solving: multiply first by 2, second by 5 → 6x + 10y = 30 and 25x + 10y = 50; subtract: 19x = 20,
x = 20/19, then y = (15 − 3(20/19))/5 = (285/19 − 60/19)/5 = (225/19)/5 = 45/19.
Z: (0,0) = 0; (2,0) = 10; (0,3) = 9; (20/19, 45/19) = 100/19 + 135/19 = 235/19 ≈ 12.37.
**Maximum = 235/19 ≈ 12.37 at (20/19, 45/19).**

**5. Minimum Z = −12 at (4, 0).**
Corners: (0, 0), (4, 0), (2, 3), (0, 4).
*(Intersection of x + 2y = 8 and 3x + 2y = 12: subtract → 2x = 4, x = 2, y = 3.)*
Z = −3x + 4y: (0,0) = 0; (4,0) = −12; (2,3) = −6 + 12 = 6; (0,4) = 16. **Minimum = −12 at (4, 0).**

**6. Maximum Z = 18 at (4, 3).**
Corners: (0, 0), (5, 0), (4, 3), (0, 5).
*(Intersection of x + 2y = 10 and 3x + y = 15: from the second y = 15 − 3x; substituting,
x + 30 − 6x = 10 ⟹ −5x = −20 ⟹ x = 4, y = 3.)*
Z: 0; 15; 12 + 6 = 18; 10. **Maximum = 18 at (4, 3).**

**7. Minimum Z = 2300 at (4, 3).**
Constraints x + 2y ≥ 10 and 3x + 4y ≤ 24 with x, y ≥ 0 give a **bounded** region.
Corners: (0, 5), (0, 6), and the intersection of x + 2y = 10 with 3x + 4y = 24.
Solving: multiply the first by 2 → 2x + 4y = 20; subtract from the second: x = 4, then y = 3.
Z = 200x + 500y: (0, 5) = 2500; (0, 6) = 3000; (4, 3) = 800 + 1500 = 2300.
**Minimum = 2300 at (4, 3).**

**8. Maximum Z = 43/11 ≈ 3.91 at (28/11, 15/11).**
The binding constraints are x + 4y ≤ 8 and 3x + y ≤ 9. Their intersection: from the second
y = 9 − 3x; substituting,
x + 36 − 12x = 8 ⟹ −11x = −28 ⟹ x = 28/11, y = 9 − 84/11 = 15/11.
Check 2x + 3y = 56/11 + 45/11 = 101/11 ≈ 9.18 ≤ 12 ✓
Corners: (0, 0), (3, 0), (28/11, 15/11), (0, 2).
Z = x + y: 0; 3; 43/11 ≈ 3.91; 2. **Maximum = 43/11 ≈ 3.91 at (28/11, 15/11).**

**9. b = 2a.** Z(2, 2) = 2a + 2b and Z(6, 0) = 6a. Equal ⟹ 2a + 2b = 6a ⟹ 2b = 4a ⟹ **b = 2a**.

**10. Infeasible.** x + y ≤ 2 and x + y ≥ 5 require 5 ≤ x + y ≤ 2, i.e. 5 ≤ 2, which is impossible.
The feasible region is empty, so the LPP has no feasible solution.

**Scoring.** Out of 30. Below 22 → the loss is almost certainly corner points read off the graph
instead of solved for, or the unbounded check omitted. Redo §3 Q2 and Q3.

---

## 6. Answering tips

1. **Use graph paper, and state the scale.** "Scale: 1 cm = 10 units on both axes." A freehand sketch
   loses the graph mark.

2. **Label every line with its equation** on the graph, and mark the axis intercepts with their
   coordinates.

3. **Shade the feasible region and label it** (write "feasible region" with an arrow, or hatch it).
   The examiner must be able to see which region you mean.

4. **Find corner points by solving simultaneous equations, and show that algebra.** Reading (20, 30)
   off a graph earns nothing; deriving it from x + y = 50 and 3x + y = 90 earns the mark. This is the
   single most common way marks are lost in this chapter.

5. **Present Z in a table**, one row per corner point, with the arithmetic shown. Not prose.

6. **Say whether the region is bounded or unbounded**, in words, before concluding.

7. **Do the unbounded check and write it as a sentence.** "Since the region is unbounded, we check
   whether 3x + 5y < 7 has a point in common with the feasible region. It does not, so the minimum
   is 7." Omitting this is a routine 1-mark loss on every unbounded question.

8. **State the answer completely:** the optimal value of Z, the point where it occurs, and whether it
   is a maximum or a minimum. "Maximum Z = 120 at (30, 0)" — all three parts.

9. **When two corners tie, say there are infinitely many optimal solutions** along the segment
   joining them. That sentence is a mark, and CBSE sets this case deliberately.

10. **For word problems, tabulate the data before writing the constraints.** A three-row table
    (resource, product A requirement, product B requirement, availability) makes the constraints
    write themselves and is worth a mark on its own.

11. **Define your variables in words.** "Let x be the number of units of A produced per day." Then
    the answer can be stated meaningfully: "Produce 4 units of A and 2 units of B for a maximum
    profit of ₹26."

12. **Check the optimal point satisfies every constraint.** Twenty seconds, and it catches a wrongly
    identified corner point.
