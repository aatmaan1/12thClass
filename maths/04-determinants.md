# Ch 4 — Determinants

**Unit II (10 marks, shared with Ch 3) · Typical appearance: the unit's 5-mark question lives here
(solving three equations by matrix method) plus 1–2 MCQs. The single most reliable 5-marker in the
paper.**

---

## 1. Scope

### In the syllabus

- Determinant of a square matrix, **up to 3 × 3**
- **Minors** and **cofactors**
- Application of determinants to the **area of a triangle**
- **Adjoint** and **inverse** of a square matrix
- **Consistency, inconsistency** and number of solutions of a system of linear equations
- **Solving a system of linear equations in two or three variables (unique solution) using the
  inverse of a matrix**

### Deleted — do not study

- **Properties of determinants** — the whole "evaluate this determinant using row/column operations
  and prove it equals (a−b)(b−c)(c−a)" family

> **Consequence.** Determinants are now something you *compute*, not something you *manipulate*.
> The long property-based proofs that used to be a guaranteed 5-marker are gone, and their weight
> moved to the matrix method for solving equations. Don't spend time on `R₁ → R₁ + R₂` gymnastics.

---

## 2. Brief

### Start here — in plain English

Every square matrix has one number you can compute from it that tells you something essential, and
that number is the **determinant**. Here is what it actually means, because knowing this makes the
whole chapter cohere.

A 2 × 2 matrix takes the unit square and turns it into a parallelogram. The determinant is the
**area** of that parallelogram. A 3 × 3 matrix turns the unit cube into a slanted box, and the
determinant is its **volume**. So a determinant measures how much a matrix stretches space.

Which immediately explains the one fact everything else hangs on: **det A = 0 means the matrix
squashes space flat.** The parallelogram has collapsed to a line, the box to a plane. And once
something has been flattened you cannot un-flatten it — information is gone for good. That is why a
matrix with zero determinant has no inverse, and why a system of equations whose determinant is zero
does not have a unique solution. Not a rule to memorise: a consequence of collapse.

Practically, you expand a 3 × 3 determinant along a row or column using **cofactors** — each entry
times the smaller 2 × 2 determinant left when you delete its row and column, with signs alternating
+ − + in a checkerboard. Two pieces of advice that pay off immediately: expand along whichever row or
column has the most zeros, since each zero kills a whole term; and remember you are free to add a
multiple of one row to another without changing the value, which lets you manufacture those zeros
before you start. Students who expand blindly along the first row every time do three times the
arithmetic and make three times the slips.

The **adjoint** is the matrix of cofactors, transposed, and its point is the identity
A · adj A = |A| I. Divide through and you have the inverse: **A⁻¹ = adj A / |A|**, which is why the
inverse exists exactly when |A| ≠ 0. In the transpose step lies the most common error in this
chapter — computing the cofactor matrix and forgetting to flip it.

The determinant also gives you **area of a triangle** from its three vertices, as half the
determinant of a 3 × 3 array of their coordinates. And because a triangle with zero area is three
points on a straight line, the same determinant set to zero is the **collinearity** test. That is a
recurring one-marker and it is the area interpretation doing the work again.

The chapter's payoff is solving simultaneous equations. **Cramer's rule** gives each unknown as a
ratio of determinants, and the **matrix method** writes the system as AX = B and solves it as
X = A⁻¹B. The board strongly prefers the matrix method — its 5-mark question is usually "solve these
three equations using matrices", and it wants to see |A| computed, then adj A, then A⁻¹, then the
multiplication. Show all four stages; the marks are distributed across them, so a correct final
answer with the working skipped scores badly.

The consistency analysis is worth getting straight as a decision tree, because it is short and often
asked. If |A| ≠ 0 there is exactly one solution. If |A| = 0, look at (adj A)B: if it is not the zero
matrix the system is **inconsistent** — no solution at all, the planes miss each other. If it is
zero, the system is consistent with **infinitely many** solutions — the planes meet in a line. Two
sentences, three cases, and full marks.

**Learn it from someone else too**

- **Video lecture** — [search: determinants class 12 maths one shot](https://www.youtube.com/results?search_query=determinants+class+12+maths+one+shot)
- **Why a determinant is an area** — [search: essence of linear algebra determinant 3Blue1Brown](https://www.youtube.com/results?search_query=3blue1brown+essence+of+linear+algebra+determinant).
  Fifteen minutes here will make this chapter feel like one idea instead of ten formulae.
- **The book the paper is set from** — [NCERT Maths Part I, Chapter 4 (PDF)](https://ncert.nic.in/textbook/pdf/lemh104.pdf)
- **For extra problems** — NCERT Exemplar Chapter 4; then drill the 5-mark system-of-equations type
  until the four stages are automatic, because it is nearly guaranteed to appear.

---

### Determinant of a 2 × 2

```
        | a  b |
|A| =   | c  d |  =  ad − bc
```

### Determinant of a 3 × 3 — expansion along a row or column

```
        | a₁  b₁  c₁ |
|A| =   | a₂  b₂  c₂ |
        | a₃  b₃  c₃ |

    = a₁ (b₂c₃ − b₃c₂)  −  b₁ (a₂c₃ − a₃c₂)  +  c₁ (a₂b₃ − a₃b₂)
```

Each bracket is the 2 × 2 determinant left after deleting the row and column of the leading element.
The **signs alternate** in the pattern

```
+  −  +
−  +  −
+  −  +
```

You may expand along **any row or column** — the answer is the same. **Choose the row or column with
the most zeros.** If a row has two zeros, that expansion is one term instead of three. This single
habit saves more time in the exam than any other trick in this chapter.

### Minors and cofactors

- **Minor** M_ij = the determinant of the 2 × 2 matrix left after deleting row i and column j
- **Cofactor** A_ij = (−1)^(i+j) · M_ij

So the cofactor is the minor with the sign from the checkerboard above. The distinction matters:
questions ask for one or the other specifically.

**Expansion in cofactor form:** |A| = a₁₁A₁₁ + a₁₂A₁₂ + a₁₃A₁₃ (along row 1), or along any other row
or column.

> **A result that gets asked:** the sum of the products of the elements of any row with the cofactors
> of a **different** row is **zero**. E.g. a₁₁A₂₁ + a₁₂A₂₂ + a₁₃A₂₃ = 0.

### Area of a triangle

For vertices (x₁, y₁), (x₂, y₂), (x₃, y₃):

```
              | x₁  y₁  1 |
Area = ½ | ·  | x₂  y₂  1 | |         (the outer bars are absolute value)
              | x₃  y₃  1 |
```

**Collinearity:** three points are collinear ⟺ the area is zero ⟺ that determinant is 0. This is how
"find k so that the points are collinear" is set.

> Always take the **absolute value** — area cannot be negative. And write the units as "square units".

### Singular and non-singular

- **Singular matrix:** |A| = 0. Has **no** inverse.
- **Non-singular matrix:** |A| ≠ 0. Has an inverse.

### Adjoint

The **adjoint** of A is the **transpose of the matrix of cofactors**:

```
adj A = [A_ij]ᵀ      i.e.      adj A = [ A₁₁  A₂₁  A₃₁ ]
                                       [ A₁₂  A₂₂  A₃₂ ]
                                       [ A₁₃  A₂₃  A₃₃ ]
```

**The transpose step is where most marks are lost in this chapter.** Compute all nine cofactors,
write them in their natural positions, *then transpose*.

**Key identity:**

```
A (adj A) = (adj A) A = |A| · I
```

### Inverse

```
A⁻¹ = (1/|A|) · adj A          provided |A| ≠ 0
```

Properties:

| Result | For a matrix of order n |
| --- | --- |
| \|AB\| = \|A\|\|B\| | |
| \|Aᵀ\| = \|A\| | |
| \|kA\| = kⁿ\|A\| | **n = 3 for a 3 × 3, so \|kA\| = k³\|A\|** |
| \|Aⁿ\| = \|A\|ⁿ | |
| \|A⁻¹\| = 1/\|A\| | |
| \|adj A\| = \|A\|^(n−1) | **= \|A\|² for a 3 × 3** |
| adj(AB) = (adj B)(adj A) | order reverses, like transpose |
| (AB)⁻¹ = B⁻¹A⁻¹ | order reverses |
| (A⁻¹)⁻¹ = A | |
| Determinant of a skew-symmetric matrix of **odd** order | = 0 |

The two most-asked of these are **|kA| = kⁿ|A|** and **|adj A| = |A|^(n−1)**. Learn the exponents:
for a 3 × 3, k³ and |A|².

### Solving a system of linear equations — the matrix method

Write the system

```
a₁x + b₁y + c₁z = d₁
a₂x + b₂y + c₂z = d₂
a₃x + b₃y + c₃z = d₃
```

as **AX = B**, where

```
A = [ a₁  b₁  c₁ ]      X = [ x ]      B = [ d₁ ]
    [ a₂  b₂  c₂ ]          [ y ]          [ d₂ ]
    [ a₃  b₃  c₃ ]          [ z ]          [ d₃ ]
```

If |A| ≠ 0, then **X = A⁻¹B**.

**The five-step procedure** — write it in exactly this order every time:

1. Write AX = B and identify A, X, B.
2. Compute **|A|**. Say explicitly whether it is ≠ 0, and conclude the system has a **unique
   solution**.
3. Compute **all nine cofactors**.
4. Write **adj A** (the transpose of the cofactor matrix), then **A⁻¹ = (1/|A|) adj A**.
5. Compute **X = A⁻¹B** and read off x, y, z.

### Consistency

| Case | Conclusion |
| --- | --- |
| \|A\| ≠ 0 | **Consistent**, with a **unique** solution: X = A⁻¹B |
| \|A\| = 0 and (adj A)B ≠ O | **Inconsistent** — no solution |
| \|A\| = 0 and (adj A)B = O | Either **infinitely many** solutions or **no** solution — must check further |

For the special case of a **homogeneous** system (B = O): x = y = z = 0 is always a solution, so it is
always consistent. If |A| ≠ 0 that trivial solution is the only one; if |A| = 0 there are infinitely
many non-trivial solutions.

### Quick recall box

```
2×2:  |A| = ad − bc
3×3:  expand along the row/column with most zeros; signs  + − + / − + − / + − +

Minor M_ij : delete row i, col j
Cofactor A_ij = (−1)^(i+j) M_ij

adj A = TRANSPOSE of the cofactor matrix
A(adj A) = (adj A)A = |A| I
A⁻¹ = (1/|A|) adj A          (needs |A| ≠ 0)

|AB| = |A||B|      |Aᵀ| = |A|      |kA| = kⁿ|A|      |Aⁿ| = |A|ⁿ
|A⁻¹| = 1/|A|      |adj A| = |A|^(n−1)      adj(AB) = (adj B)(adj A)

Area of triangle = ½ |det[[x₁,y₁,1],[x₂,y₂,1],[x₃,y₃,1]]|
Collinear ⟺ that determinant = 0

AX = B → X = A⁻¹B if |A| ≠ 0 (unique solution)
|A| = 0, (adj A)B ≠ O → inconsistent
|A| = 0, (adj A)B = O → infinitely many, or none
```

---

## 3. Previous years' questions

**Q1.** *(5 marks — the flagship question of this unit)*
Solve the following system of equations by the matrix method:

```
2x + 3y + 3z = 5
 x − 2y +  z = −4
3x −  y − 2z = 3
```

**Q2.** *(5 marks)* If A = [[1, −1, 2], [0, 2, −3], [3, −2, 4]], find A⁻¹.

**Q3.** *(1 mark, MCQ)* If A is a 3 × 3 matrix with |A| = 4, then |2A| equals
(a) 8 (b) 16 (c) 32 (d) 64

**Q4.** *(2 marks)* If A is a 3 × 3 matrix with |A| = 5, find |adj A| and |A⁻¹|.

**Q5.** *(2 marks)* Find the area of the triangle whose vertices are (1, 0), (6, 0) and (4, 3).

**Q6.** *(3 marks)* Find the value(s) of k for which the points (k, 2 − 2k), (1 − k, 2k) and
(−4 − k, 6 − 2k) are collinear.

**Q7.** *(5 marks, word problem — a recurring dressing of Q1)*
The sum of three numbers is 6. If we multiply the third number by 3 and add the second number to it,
we get 11. By adding the first and third numbers we get double the second number. Represent this
algebraically and find the numbers using the matrix method.

**Q8.** *(3 marks)* For A = [[2, 3], [1, −4]], verify that A(adj A) = |A| I.

**Q9.** *(1 mark, MCQ)* If A is a square matrix of order 3 and |A| = −2, then |adj A| is
(a) −2 (b) 2 (c) 4 (d) −4

**Q10.** *(2 marks)* Examine the consistency of the system
x + 2y = 2, 2x + 3y = 3.

**Q11.** *(1 mark)* Write the minor and the cofactor of the element a₂₃ in

```
[ 1  −2   3 ]
[ 4   5  −6 ]
[ 7   8   9 ]
```

**Q12.** *(1 mark, Assertion–Reason)*
**A:** If A is a singular matrix, then A⁻¹ does not exist.
**R:** A⁻¹ = (1/|A|) adj A.

---

## 4. Solutions

### Q1 — solve by the matrix method

**Step 1. Write AX = B.**

```
A = [ 2   3   3 ]      X = [ x ]      B = [  5 ]
    [ 1  −2   1 ]          [ y ]          [ −4 ]
    [ 3  −1  −2 ]          [ z ]          [  3 ]
```

**Step 2. Compute |A|,** expanding along row 1:

```
|A| = 2[(−2)(−2) − (1)(−1)] − 3[(1)(−2) − (1)(3)] + 3[(1)(−1) − (−2)(3)]
    = 2[4 + 1] − 3[−2 − 3] + 3[−1 + 6]
    = 2(5) − 3(−5) + 3(5)
    = 10 + 15 + 15
    = 40
```

Since **|A| = 40 ≠ 0**, A⁻¹ exists and the system has a **unique solution**.

**Step 3. Cofactors.**

```
A₁₁ = +[(−2)(−2) − (1)(−1)]  = 4 + 1   =  5
A₁₂ = −[(1)(−2)  − (1)(3)]   = −(−5)   =  5
A₁₃ = +[(1)(−1)  − (−2)(3)]  = −1 + 6  =  5

A₂₁ = −[(3)(−2)  − (3)(−1)]  = −(−3)   =  3
A₂₂ = +[(2)(−2)  − (3)(3)]   = −4 − 9  = −13
A₂₃ = −[(2)(−1)  − (3)(3)]   = −(−11)  =  11

A₃₁ = +[(3)(1)   − (3)(−2)]  = 3 + 6   =  9
A₃₂ = −[(2)(1)   − (3)(1)]   = −(−1)   =  1
A₃₃ = +[(2)(−2)  − (3)(1)]   = −4 − 3  = −7
```

**Step 4. adj A** = transpose of the cofactor matrix:

```
cofactor matrix = [  5    5    5 ]
                  [  3  −13   11 ]
                  [  9    1   −7 ]
```

Transposing it (rows become columns):

```
adj A = [  5   3   9 ]
        [  5 −13   1 ]
        [  5  11  −7 ]
```

So

```
A⁻¹ = (1/40) [  5   3   9 ]
             [  5 −13   1 ]
             [  5  11  −7 ]
```

**Step 5. X = A⁻¹B.**

```
X = (1/40) [  5   3   9 ] [  5 ]
           [  5 −13   1 ] [ −4 ]
           [  5  11  −7 ] [  3 ]

  = (1/40) [ 5(5) + 3(−4) + 9(3)   ]   = (1/40) [  25 − 12 + 27 ]   = (1/40) [  40 ]
           [ 5(5) − 13(−4) + 1(3)  ]            [  25 + 52 +  3 ]            [  80 ]
           [ 5(5) + 11(−4) − 7(3)  ]            [  25 − 44 − 21 ]            [ −40 ]

  = [  1 ]
    [  2 ]
    [ −1 ]
```

**Hence x = 1, y = 2, z = −1.**

*Verification (always do this — it costs 20 seconds):*
2(1) + 3(2) + 3(−1) = 2 + 6 − 3 = 5 ✓
1 − 2(2) + (−1) = 1 − 4 − 1 = −4 ✓
3(1) − 2 − 2(−1) = 3 − 2 + 2 = 3 ✓

### Q2 — find A⁻¹

```
A = [ 1  −1   2 ]
    [ 0   2  −3 ]
    [ 3  −2   4 ]
```

**|A|**, expanding along row 1:

```
|A| = 1[(2)(4) − (−3)(−2)] − (−1)[(0)(4) − (−3)(3)] + 2[(0)(−2) − (2)(3)]
    = 1[8 − 6] + 1[0 + 9] + 2[0 − 6]
    = 2 + 9 − 12
    = −1
```

|A| = −1 ≠ 0, so A⁻¹ exists.

**Cofactors:**

```
A₁₁ = +[(2)(4)  − (−3)(−2)] = 8 − 6  =  2
A₁₂ = −[(0)(4)  − (−3)(3)]  = −(9)   = −9
A₁₃ = +[(0)(−2) − (2)(3)]   = −6     = −6

A₂₁ = −[(−1)(4) − (2)(−2)]  = −(0)   =  0
A₂₂ = +[(1)(4)  − (2)(3)]   = −2     = −2
A₂₃ = −[(1)(−2) − (−1)(3)]  = −(1)   = −1

A₃₁ = +[(−1)(−3) − (2)(2)]  = 3 − 4  = −1
A₃₂ = −[(1)(−3)  − (2)(0)]  = 3      =  3
A₃₃ = +[(1)(2)   − (−1)(0)] = 2      =  2
```

**adj A** (transpose of the above):

```
adj A = [  2    0   −1 ]
        [ −9   −2    3 ]
        [ −6   −1    2 ]
```

**A⁻¹ = (1/|A|) adj A = (1/−1) adj A = −adj A:**

```
A⁻¹ = [ −2   0   1 ]
      [  9   2  −3 ]
      [  6   1  −2 ]
```

*Verification — first row of A times first column of A⁻¹:*
(1)(−2) + (−1)(9) + (2)(6) = −2 − 9 + 12 = 1 ✓ (the (1,1) entry of I)
*First row of A times second column:* (1)(0) + (−1)(2) + (2)(1) = 0 − 2 + 2 = 0 ✓

### Q3 — |2A| for a 3 × 3 with |A| = 4

|kA| = kⁿ|A| with n = 3:

```
|2A| = 2³ |A| = 8 × 4 = 32
```

**Answer: (c) 32**

*(The trap is (a) 8, from |2A| = 2|A|. The scalar multiplies **every** row, so it comes out n times.)*

### Q4 — |adj A| and |A⁻¹| for a 3 × 3 with |A| = 5

```
|adj A| = |A|^(n−1) = |A|² = 5² = 25
|A⁻¹|  = 1/|A| = 1/5
```

### Q5 — area of the triangle (1,0), (6,0), (4,3)

```
             | 1  0  1 |
Area = ½  |  | 6  0  1 |  |
             | 4  3  1 |
```

Expand along row 1:

```
det = 1[(0)(1) − (1)(3)] − 0[(6)(1) − (1)(4)] + 1[(6)(3) − (0)(4)]
    = 1(−3) − 0 + 1(18)
    = 15
```

```
Area = ½ |15| = 15/2 = 7.5 square units
```

*(Sanity check: the base from (1,0) to (6,0) is 5 units along the x-axis, and the height to (4,3) is
3. Area = ½ × 5 × 3 = 7.5 ✓)*

### Q6 — find k for collinearity

The three points are collinear iff

```
| k       2−2k    1 |
| 1−k     2k      1 |  = 0
| −4−k    6−2k    1 |
```

Expanding along column 3 is tidiest, but let us expand along row 1 to keep it mechanical:

```
det = k[ 2k − (6 − 2k) ] − (2 − 2k)[ (1 − k) − (−4 − k) ] + 1[ (1−k)(6−2k) − 2k(−4−k) ]
```

Term by term:

```
Term 1 = k(2k − 6 + 2k) = k(4k − 6) = 4k² − 6k

Term 2 = −(2 − 2k)(1 − k + 4 + k) = −(2 − 2k)(5) = −10 + 10k

Term 3 = (6 − 2k − 6k + 2k²) − (−8k − 2k²)
       = (6 − 8k + 2k²) + 8k + 2k²
       = 6 + 4k²
```

Adding:

```
det = 4k² − 6k − 10 + 10k + 6 + 4k²
    = 8k² + 4k − 4
```

Set det = 0:

```
      8k² + 4k − 4 = 0
⟹     2k² + k − 1 = 0
⟹     (2k − 1)(k + 1) = 0
⟹     k = 1/2   or   k = −1
```

**k = 1/2 or k = −1**

### Q7 — word problem by the matrix method

**Setting up.** Let the numbers be x, y, z.

- "The sum of three numbers is 6" → x + y + z = 6
- "Multiply the third by 3 and add the second, we get 11" → y + 3z = 11
- "First plus third is double the second" → x + z = 2y ⟹ x − 2y + z = 0

```
A = [ 1   1   1 ]      X = [ x ]      B = [  6 ]
    [ 0   1   3 ]          [ y ]          [ 11 ]
    [ 1  −2   1 ]          [ z ]          [  0 ]
```

**|A|**, expanding along row 1:

```
|A| = 1[(1)(1) − (3)(−2)] − 1[(0)(1) − (3)(1)] + 1[(0)(−2) − (1)(1)]
    = 1[1 + 6] − 1[−3] + 1[−1]
    = 7 + 3 − 1 = 9      ≠ 0, so a unique solution exists
```

**Cofactors:**

```
A₁₁ = +[(1)(1)  − (3)(−2)] =  7        A₂₁ = −[(1)(1)  − (1)(−2)] = −3
A₁₂ = −[(0)(1)  − (3)(1)]  =  3        A₂₂ = +[(1)(1)  − (1)(1)]  =  0
A₁₃ = +[(0)(−2) − (1)(1)]  = −1        A₂₃ = −[(1)(−2) − (1)(1)]  =  3

A₃₁ = +[(1)(3)  − (1)(1)]  =  2
A₃₂ = −[(1)(3)  − (1)(0)]  = −3
A₃₃ = +[(1)(1)  − (1)(0)]  =  1
```

**adj A** (transpose of the cofactor matrix):

```
adj A = [  7  −3   2 ]
        [  3   0  −3 ]
        [ −1   3   1 ]
```

**X = A⁻¹B = (1/9)(adj A)B:**

```
X = (1/9) [  7  −3   2 ] [  6 ]   = (1/9) [ 42 − 33 + 0 ]  = (1/9) [  9 ]  = [ 1 ]
          [  3   0  −3 ] [ 11 ]            [ 18 +  0 − 0 ]           [ 18 ]    [ 2 ]
          [ −1   3   1 ] [  0 ]            [ −6 + 33 + 0 ]           [ 27 ]    [ 3 ]
```

**The numbers are 1, 2 and 3.**

*Verification:* 1 + 2 + 3 = 6 ✓; 2 + 3(3) = 11 ✓; 1 + 3 = 4 = 2(2) ✓

### Q8 — verify A(adj A) = |A| I for A = [[2, 3], [1, −4]]

```
|A| = (2)(−4) − (3)(1) = −8 − 3 = −11
```

For a 2 × 2 matrix [[a, b], [c, d]], adj A = [[d, −b], [−c, a]]. So

```
adj A = [ −4  −3 ]
        [ −1   2 ]
```

```
A(adj A) = [ 2   3 ][ −4  −3 ] = [ 2(−4)+3(−1)    2(−3)+3(2)  ]
           [ 1  −4 ][ −1   2 ]   [ 1(−4)+(−4)(−1) 1(−3)+(−4)(2) ]

         = [ −8 − 3    −6 + 6  ] = [ −11    0  ]
           [ −4 + 4    −3 − 8  ]   [   0  −11  ]

         = −11 [ 1  0 ] = |A| · I ✓
                [ 0  1 ]
```

**Hence A(adj A) = |A| I, verified.**

> The 2 × 2 shortcut `adj [[a,b],[c,d]] = [[d,−b],[−c,a]]` — swap the diagonal, negate the
> off-diagonal — is worth memorising. It saves a full minute whenever a 2 × 2 inverse appears.

### Q9 — |adj A| for a 3 × 3 with |A| = −2

```
|adj A| = |A|^(n−1) = |A|² = (−2)² = 4
```

**Answer: (c) 4**

*(Note the answer is positive even though |A| is negative — the exponent is even. Option (d) −4 is
the trap.)*

### Q10 — consistency of x + 2y = 2, 2x + 3y = 3

```
A = [ 1  2 ]      |A| = (1)(3) − (2)(2) = 3 − 4 = −1
    [ 2  3 ]
```

Since **|A| = −1 ≠ 0**, the system is **consistent** and has a **unique solution**.

*(Finding it, for completeness: adj A = [[3, −2], [−2, 1]], so
A⁻¹ = (1/−1)[[3,−2],[−2,1]] = [[−3, 2], [2, −1]], and
X = A⁻¹B = [[−3,2],[2,−1]]·[2,3]ᵀ = [−6 + 6, 4 − 3]ᵀ = [0, 1]ᵀ, i.e. x = 0, y = 1.
Check: 0 + 2(1) = 2 ✓ and 2(0) + 3(1) = 3 ✓)*

### Q11 — minor and cofactor of a₂₃

a₂₃ = −6 (row 2, column 3). Delete row 2 and column 3:

```
M₂₃ = | 1  −2 |  = (1)(8) − (−2)(7) = 8 + 14 = 22
      | 7   8 |
```

```
A₂₃ = (−1)^(2+3) M₂₃ = (−1)⁵ (22) = −22
```

**Minor M₂₃ = 22; cofactor A₂₃ = −22**

### Q12 — Assertion–Reason

**A:** True. Singular means |A| = 0, and the inverse formula requires division by |A|, so A⁻¹ does
not exist.

**R:** True. That is the correct formula for the inverse.

**Does R explain A?** Yes — it is precisely because A⁻¹ = (1/|A|) adj A that |A| = 0 makes the
inverse undefined.

**Answer: (a) Both A and R are true, and R is the correct explanation of A.**

---

## 5. Test yourself

Time: 45 minutes. Answers below.

1. *(1)* If A is a 2 × 2 matrix with |A| = 3, then |3A| is
   (a) 9 (b) 27 (c) 3 (d) 6
2. *(1)* If A is a 3 × 3 matrix and |adj A| = 16, then |A| is
   (a) ±4 (b) 4 (c) 16 (d) ±2
3. *(1)* The determinant of a skew-symmetric matrix of order 3 is
   (a) 1 (b) 0 (c) −1 (d) cannot be determined
4. *(2)* Evaluate the determinant of [[2, −1, 3], [0, 4, 0], [1, 5, −2]].
5. *(2)* If A = [[3, −2], [4, −2]], find A⁻¹.
6. *(2)* Find the area of the triangle with vertices (2, 7), (1, 1) and (10, 8).
7. *(2)* Find k if the points (3, −2), (k, 2) and (8, 8) are collinear.
8. *(3)* Write the minor and the cofactor of a₃₂ in [[2, −3, 5], [6, 0, 4], [1, 5, −7]].
9. *(3)* If A = [[1, 2], [3, 4]] and B = [[2, 0], [1, 3]], verify |AB| = |A||B|.
10. *(5)* Solve by the matrix method: x + y + z = 4, 2x + y − 3z = −9, 2x − y + z = −1.
11. *(5)* If A = [[2, −3, 5], [3, 2, −4], [1, 1, −2]], find A⁻¹ and hence solve
    2x − 3y + 5z = 11, 3x + 2y − 4z = −5, x + y − 2z = −3.
12. *(2)* Show that the system 2x + 3y = 5, 4x + 6y = 10 does not have a unique solution.
13. *(1)* For a square matrix A of order n, A(adj A) equals
    (a) I (b) |A| (c) |A| I (d) adj A

### Answer key

**1. (b) 27.** n = 2, so |3A| = 3²|A| = 9 × 3 = 27.

**2. (a) ±4.** |adj A| = |A|² = 16 ⟹ |A| = ±4.

**3. (b) 0.** For odd order n, |A| = |Aᵀ| = |−A| = (−1)ⁿ|A| = −|A|, so 2|A| = 0.

**4. −28.** Expand along **row 2**, where only a₂₂ = 4 is non-zero:
det = 4 · A₂₂, and A₂₂ = +|[[2, 3], [1, −2]]| = (2)(−2) − (3)(1) = −7.
So det = 4(−7) = **−28**. *(Choosing row 2 turns three 2 × 2 determinants into one.)*

**5. A⁻¹ = [[−1, 1], [−2, 3/2]].** |A| = 3(−2) − (−2)(4) = −6 + 8 = 2.
adj A = [[−2, 2], [−4, 3]]. A⁻¹ = ½[[−2, 2], [−4, 3]] = [[−1, 1], [−2, 3/2]].
*Check:* A·A⁻¹ = [[3,−2],[4,−2]]·[[−1,1],[−2,3/2]] = [[−3+4, 3−3], [−4+4, 4−3]] = [[1,0],[0,1]] ✓

**6. 47/2 square units.** det[[2,7,1],[1,1,1],[10,8,1]]
= 2(1 − 8) − 7(1 − 10) + 1(8 − 10) = −14 + 63 − 2 = 47. Area = 47/2.

**7. k = 5.** det[[3,−2,1],[k,2,1],[8,8,1]] = 0.
3(2 − 8) + 2(k − 8) + 1(8k − 16) = −18 + 2k − 16 + 8k − 16 = 10k − 50 = 0 ⟹ k = 5.

**8. Minor M₃₂ = −22, cofactor A₃₂ = 22.**
Delete row 3, col 2: M₃₂ = |[[2, 5], [6, 4]]| = 8 − 30 = −22.
A₃₂ = (−1)^(3+2)(−22) = −(−22) = 22.

**9.** |A| = 4 − 6 = −2. |B| = 6 − 0 = 6. AB = [[1,2],[3,4]]·[[2,0],[1,3]] = [[4, 6], [10, 12]].
|AB| = 48 − 60 = −12 = (−2)(6) ✓

**10. x = −1, y = 2, z = 3.**
A = [[1,1,1],[2,1,−3],[2,−1,1]]. |A| = 1(1 − 3) − 1(2 + 6) + 1(−2 − 2) = −2 − 8 − 4 = −14 ≠ 0.
Cofactors: A₁₁ = −2, A₁₂ = −8, A₁₃ = −4; A₂₁ = −2, A₂₂ = −1, A₂₃ = 3; A₃₁ = −4, A₃₂ = 5, A₃₃ = −1.
adj A = [[−2, −2, −4], [−8, −1, 5], [−4, 3, −1]].
X = (1/−14)(adj A)[4, −9, −1]ᵀ
= (1/−14)[(−8 + 18 + 4), (−32 + 9 − 5), (−16 − 27 + 1)]ᵀ = (1/−14)[14, −28, −42]ᵀ = [−1, 2, 3]ᵀ.
*Check:* −1 + 2 + 3 = 4 ✓; −2 + 2 − 9 = −9 ✓; −2 − 2 + 3 = −1 ✓

**11. A⁻¹ = [[0, 1, −2], [−2, 9, −23], [−1, 5, −13]]; x = 1, y = 2, z = 3.**
|A| = 2(−4 + 4) + 3(−6 + 4) + 5(3 − 2) = 0 − 6 + 5 = −1.
Cofactors: A₁₁ = 0, A₁₂ = 2, A₁₃ = 1; A₂₁ = −1, A₂₂ = −9, A₂₃ = −5; A₃₁ = 2, A₃₂ = 23, A₃₃ = 13.
adj A = [[0, −1, 2], [2, −9, 23], [1, −5, 13]] (the transpose of the cofactor matrix), so
A⁻¹ = (1/−1) adj A = [[0, 1, −2], [−2, 9, −23], [−1, 5, −13]].
X = A⁻¹[11, −5, −3]ᵀ = [(0 − 5 + 6), (−22 − 45 + 69), (−11 − 25 + 39)]ᵀ = [1, 2, 3]ᵀ.
*Check:* 2 − 6 + 15 = 11 ✓; 3 + 4 − 12 = −5 ✓; 1 + 2 − 6 = −3 ✓

**12.** A = [[2, 3], [4, 6]], |A| = 12 − 12 = 0, so A⁻¹ does not exist and there is no unique solution.
(adj A)B = [[6, −3], [−4, 2]]·[5, 10]ᵀ = [30 − 30, −20 + 20]ᵀ = [0, 0]ᵀ = O, so the system has
**infinitely many solutions** — indeed the second equation is just twice the first.

**13. (c) |A| I.**

**Scoring.** Out of 30. Below 21 → the loss is almost certainly in cofactor signs or the adjoint
transpose. Redo §3 Q1 and Q7 from scratch without looking.

---

## 6. Answering tips

**On the 5-mark matrix-method question**

1. **Follow the five steps in order, with each labelled.** The marking scheme is essentially those
   five steps. Even a student who makes an arithmetic slip in step 3 scores 3 of 5 if steps 1, 2, 4
   and 5 are visibly present and correctly structured.

2. **State "|A| ≠ 0, therefore A⁻¹ exists and the system has a unique solution."** That sentence is a
   mark. Do not skip it as obvious.

3. **Write out all nine cofactors as a labelled list**, A₁₁ through A₃₃, with the sign shown. Do not
   compute them mentally into a matrix — the examiner cannot award partial credit for arithmetic they
   cannot see, and you cannot check your own work.

4. **The transpose is a separate, visible step.** Write the cofactor matrix, then write "adj A = "
   and the transpose. Every year, a large fraction of students write the cofactor matrix and label
   it adj A. That error propagates and costs the whole question.

5. **Always verify** by substituting x, y, z back into the original equations, and write "Verified"
   or show the substitution. It costs 20 seconds, catches most slips, and reads well.

6. **For word problems, write the three equations first as a clearly labelled system**, before any
   matrices. Translating the words is typically 1 of the 5 marks and is marked separately from the
   matrix work. "By adding the first and third numbers we get double the second" → x + z = 2y →
   x − 2y + z = 0: show that rearrangement.

**On determinants generally**

7. **Expand along the row or column with the most zeros.** State which one you chose
   ("expanding along R₂"). If a row has two zeros, this turns three 2 × 2 determinants into one.

8. **Write the sign of each cofactor explicitly** as +[…] or −[…] before the bracket. The alternating
   sign is the commonest single error in this chapter, and writing it first prevents it.

9. **For area questions: absolute value, and "square units".** Both are marks. And if the area comes
   out zero, say so and conclude the points are collinear rather than reporting "area = 0" alone.

10. **For collinearity questions**, set the determinant equal to zero *first*, as a displayed
    equation, before expanding. It shows the examiner you know why you are computing.

**On the property MCQs**

11. **Memorise the two exponents:** |kA| = kⁿ|A| and |adj A| = |A|^(n−1). For 3 × 3 that is k³ and
    |A|². These two account for most 1-markers in this chapter.

12. **Watch for signs in |adj A|.** Since the exponent n − 1 = 2 for a 3 × 3, the answer is always
    non-negative — a negative option can be eliminated instantly.

13. **The 2 × 2 adjoint shortcut:** adj [[a, b], [c, d]] = [[d, −b], [−c, a]]. Swap the diagonal
    entries, negate the other two. Use it; do not compute four cofactors for a 2 × 2.
