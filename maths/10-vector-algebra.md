# Ch 10 — Vector Algebra

**Unit IV Vectors and 3D Geometry (14 marks, shared with Ch 11) · Typical appearance: 2–3 MCQs +
one or two 2/3-mark questions. Small, dense, formula-driven — probably the best marks-per-hour
chapter in Mathematics.**

---

## 1. Scope

### In the syllabus

- Vectors and scalars; **magnitude and direction** of a vector
- **Direction cosines** and **direction ratios**
- Types of vectors: equal, unit, zero, parallel and collinear
- **Position vector** of a point; negative of a vector; components of a vector
- **Addition** of vectors; multiplication of a vector by a **scalar**
- Position vector of a point **dividing a line segment** in a given ratio
- **Scalar (dot) product**: definition, geometrical interpretation, properties, applications
- **Vector (cross) product**: definition, geometrical interpretation, properties, applications

### Deleted — do not study

- **Scalar triple product** [a b c] and its applications (volume of a parallelepiped, coplanarity)

> **Consequence.** No triple products means no volume questions and no coplanarity-of-three-vectors
> questions. Everything left is dot product, cross product, and basic vector arithmetic.

---

## 2. Brief

### Basics

A **vector** has magnitude and direction; a **scalar** has magnitude only.

For **a** = a₁î + a₂ĵ + a₃k̂:

```
Magnitude       |a| = √(a₁² + a₂² + a₃²)
Unit vector     â  = a / |a|                       (magnitude 1, same direction)
```

**Types of vectors:**

| Type | Meaning |
| --- | --- |
| Zero (null) vector **0** | magnitude 0; direction indeterminate |
| Unit vector | magnitude 1 |
| Equal vectors | same magnitude **and** same direction |
| Collinear / parallel | along the same or parallel lines; **a** = λ**b** for some scalar λ |
| Negative of **a** | same magnitude, opposite direction, written −**a** |
| Coinitial vectors | same initial point |

### Position vectors and the vector joining two points

If A and B have position vectors **a** and **b** (measured from the origin O), then

```
      AB  =  OB − OA  =  b − a
```

("head minus tail" — the terminal point minus the initial point.) This is the single most-used
formula in this chapter and the next.

For points A(x₁, y₁, z₁) and B(x₂, y₂, z₂):

```
      AB = (x₂ − x₁)î + (y₂ − y₁)ĵ + (z₂ − z₁)k̂
      |AB| = √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²]
```

### Section formula

Point R divides the join of A(**a**) and B(**b**) in the ratio m : n.

```
Internally:   r = (m b + n a)/(m + n)
Externally:   r = (m b − n a)/(m − n)
Midpoint:     r = (a + b)/2
```

> **Memory hook for the internal formula:** the coefficient of **b** is m (the part *nearer* B). Get
> that right and the formula assembles itself.

### Direction cosines and direction ratios

If **a** = a₁î + a₂ĵ + a₃k̂ makes angles α, β, γ with the positive x-, y-, z-axes, then the
**direction cosines** are

```
      l = cos α = a₁/|a|          m = cos β = a₂/|a|          n = cos γ = a₃/|a|
```

and always

```
      l² + m² + n² = 1
```

**Direction ratios** are any triple proportional to (l, m, n) — so (a₁, a₂, a₃) themselves are
direction ratios. Direction ratios are not unique (any scalar multiple works); direction cosines are
(up to overall sign).

To convert direction ratios (a, b, c) to direction cosines, divide by √(a² + b² + c²).

### Scalar (dot) product

```
      a · b = |a| |b| cos θ                    (θ is the angle between them, 0 ≤ θ ≤ π)
      a · b = a₁b₁ + a₂b₂ + a₃b₃               (component form)
```

The dot product is a **scalar**.

**Properties:**

| | |
| --- | --- |
| Commutative | **a**·**b** = **b**·**a** |
| Distributive | **a**·(**b** + **c**) = **a**·**b** + **a**·**c** |
| **a**·**a** = \|**a**\|² | |
| Perpendicular ⟺ **a**·**b** = 0 | (for non-zero vectors) |
| î·î = ĵ·ĵ = k̂·k̂ = 1 | î·ĵ = ĵ·k̂ = k̂·î = 0 |

**Applications:**

```
Angle between vectors:      cos θ = (a · b) / (|a| |b|)

Projection of a on b   =    (a · b) / |b|          (a SCALAR)

Vector projection of a on b = [ (a · b) / |b|² ] b
```

> **Projection is a scalar and can be negative** (when the angle is obtuse). Do not take a modulus
> unless asked for the *length* of the projection.

### Vector (cross) product

```
      a × b = |a| |b| sin θ n̂
```

where n̂ is the unit vector perpendicular to both **a** and **b**, in the direction given by the
right-hand rule. The cross product is a **vector**.

**Component form — always compute it as a determinant:**

```
              | î    ĵ    k̂  |
      a × b = | a₁   a₂   a₃ |
              | b₁   b₂   b₃ |

            = î(a₂b₃ − a₃b₂) − ĵ(a₁b₃ − a₃b₁) + k̂(a₁b₂ − a₂b₁)
```

**Properties:**

| | |
| --- | --- |
| **Not** commutative | **a** × **b** = −(**b** × **a**) |
| Distributive | **a** × (**b** + **c**) = **a**×**b** + **a**×**c** |
| **a** × **a** = **0** | |
| Parallel ⟺ **a** × **b** = **0** | (for non-zero vectors) |
| î×ĵ = k̂, ĵ×k̂ = î, k̂×î = ĵ | and each reverses sign if the order swaps |

**Applications:**

```
sin θ = |a × b| / (|a| |b|)

Area of a parallelogram with adjacent sides a, b   =  |a × b|
Area of a parallelogram with diagonals d₁, d₂      =  ½ |d₁ × d₂|
Area of a triangle with two sides a, b             =  ½ |a × b|

Unit vector perpendicular to both a and b          =  (a × b) / |a × b|
```

### The identity worth memorising

```
      |a × b|² + (a · b)² = |a|² |b|²
```

This follows from sin²θ + cos²θ = 1, and it converts a dot-product question into a cross-product
answer (or vice versa) in one line. It appears as a 2-marker.

### Two classic results

**1. |a + b| = |a − b| ⟺ a ⊥ b.**

```
      |a + b|² = |a|² + 2a·b + |b|²
      |a − b|² = |a|² − 2a·b + |b|²
```

Equality forces 4(**a**·**b**) = 0, i.e. **a**·**b** = 0.

**2. If a, b, c are unit vectors with a + b + c = 0, then a·b + b·c + c·a = −3/2.**

```
      |a + b + c|² = 0
⟹     |a|² + |b|² + |c|² + 2(a·b + b·c + c·a) = 0
⟹     1 + 1 + 1 + 2(a·b + b·c + c·a) = 0
⟹     a·b + b·c + c·a = −3/2
```

### Quick recall box

```
|a| = √(a₁²+a₂²+a₃²)          â = a/|a|
AB = b − a                     (head minus tail)

Section (internal, m:n) : r = (mb + na)/(m+n)     Midpoint: (a+b)/2
Direction cosines: l,m,n = a₁/|a|, a₂/|a|, a₃/|a| ;  l²+m²+n² = 1

DOT:   a·b = |a||b|cos θ = a₁b₁+a₂b₂+a₃b₃        (SCALAR)
       cos θ = a·b/(|a||b|)
       ⊥  ⟺  a·b = 0
       projection of a on b = a·b/|b|

CROSS: a×b = determinant with rows î ĵ k̂ / a / b  (VECTOR)
       |a×b| = |a||b| sin θ
       ∥  ⟺  a×b = 0
       area of parallelogram = |a×b| ;  triangle = ½|a×b|
       unit ⊥ to both = (a×b)/|a×b|

|a×b|² + (a·b)² = |a|²|b|²
|a+b| = |a−b|  ⟺  a ⊥ b
```

---

## 3. Previous years' questions

**Q1.** *(1 mark)* Find the unit vector in the direction of **a** = 2î + ĵ − 2k̂.

**Q2.** *(2 marks)* Find the angle between the vectors **a** = î + ĵ − k̂ and **b** = î − ĵ + k̂.

**Q3.** *(2 marks)* Find the projection of **a** = 2î + 3ĵ + 2k̂ on **b** = î + 2ĵ + k̂.

**Q4.** *(2 marks)* Find λ so that the vectors **a** = 2î + λĵ + k̂ and **b** = î − 2ĵ + 3k̂ are
perpendicular.

**Q5.** *(3 marks)* Find the area of the triangle with vertices A(1, 1, 2), B(2, 3, 5) and
C(1, 5, 5).

**Q6.** *(2 marks)* If |**a**| = 3, |**b**| = 4 and **a**·**b** = 6, find |**a** × **b**|.

**Q7.** *(2 marks)* Show that if |**a** + **b**| = |**a** − **b**|, then **a** and **b** are
perpendicular.

**Q8.** *(2 marks)* Find the direction cosines of the vector î + 2ĵ + 3k̂.

**Q9.** *(3 marks)* Find a unit vector perpendicular to both **a** = î + ĵ + k̂ and
**b** = î + 2ĵ + 3k̂.

**Q10.** *(2 marks)* Find the position vector of the point which divides the join of the points with
position vectors **a** and **b** in the ratio 2 : 1 internally.

**Q11.** *(3 marks)* If **a**, **b**, **c** are unit vectors such that **a** + **b** + **c** = **0**,
find the value of **a**·**b** + **b**·**c** + **c**·**a**.

**Q12.** *(1 mark, MCQ)* If **a** and **b** are non-zero vectors with **a** × **b** = **0**, then
(a) **a** ⊥ **b** (b) **a** ∥ **b** (c) **a** = **b** (d) **a**·**b** = 0

**Q13.** *(2 marks)* Find the area of the parallelogram whose diagonals are
**d₁** = 3î + ĵ − 2k̂ and **d₂** = î − 3ĵ + 4k̂.

---

## 4. Solutions

### Q1 — unit vector in the direction of 2î + ĵ − 2k̂

```
      |a| = √(2² + 1² + (−2)²) = √(4 + 1 + 4) = √9 = 3
```

```
      â = a/|a| = (2î + ĵ − 2k̂)/3 = (2/3)î + (1/3)ĵ − (2/3)k̂
```

### Q2 — angle between î + ĵ − k̂ and î − ĵ + k̂

```
      a · b = (1)(1) + (1)(−1) + (−1)(1) = 1 − 1 − 1 = −1

      |a| = √(1 + 1 + 1) = √3          |b| = √(1 + 1 + 1) = √3
```

```
      cos θ = (a · b)/(|a||b|) = −1/(√3 · √3) = −1/3
```

```
θ = cos⁻¹(−1/3)          ≈ 109.5°
```

*(The angle is obtuse, consistent with the negative dot product.)*

### Q3 — projection of a on b

```
      a · b = (2)(1) + (3)(2) + (2)(1) = 2 + 6 + 2 = 10

      |b| = √(1 + 4 + 1) = √6
```

```
      Projection of a on b = (a · b)/|b| = 10/√6 = 10√6/6 = (5√6)/3
```

*(Note the projection formula divides by |**b**| — the vector you are projecting *onto*. Dividing by
|**a**| is the standard error.)*

### Q4 — find λ for perpendicularity

Perpendicular ⟺ **a**·**b** = 0:

```
      (2)(1) + (λ)(−2) + (1)(3) = 0
⟹     2 − 2λ + 3 = 0
⟹     5 = 2λ
⟹     λ = 5/2
```

### Q5 — area of triangle A(1,1,2), B(2,3,5), C(1,5,5)

**Form two side vectors from the same vertex:**

```
      AB = (2−1)î + (3−1)ĵ + (5−2)k̂ = î + 2ĵ + 3k̂
      AC = (1−1)î + (5−1)ĵ + (5−2)k̂ = 0î + 4ĵ + 3k̂
```

**Cross product:**

```
                | î   ĵ   k̂ |
      AB × AC = | 1   2   3 |
                | 0   4   3 |

              = î(2·3 − 3·4) − ĵ(1·3 − 3·0) + k̂(1·4 − 2·0)
              = î(6 − 12) − ĵ(3) + k̂(4)
              = −6î − 3ĵ + 4k̂
```

**Magnitude:**

```
      |AB × AC| = √(36 + 9 + 16) = √61
```

```
      Area of triangle = ½ |AB × AC| = √61/2 square units
```

### Q6 — |a × b| given |a|, |b| and a·b

Use the identity |**a** × **b**|² + (**a**·**b**)² = |**a**|²|**b**|²:

```
      |a × b|² = |a|²|b|² − (a·b)²
               = (3)²(4)² − (6)²
               = 144 − 36
               = 108
```

```
      |a × b| = √108 = 6√3
```

> The alternative route — find cos θ = 6/12 = ½ so θ = 60°, then |**a**×**b**| = 3·4·sin 60° = 12(√3/2)
> = 6√3 — gives the same answer and is equally acceptable.

### Q7 — |a + b| = |a − b| ⟹ a ⊥ b

Square both sides (both are non-negative, so this is valid):

```
      |a + b|² = |a − b|²
```

Expanding each using |**v**|² = **v**·**v**:

```
      (a + b)·(a + b) = (a − b)·(a − b)
⟹     a·a + 2 a·b + b·b = a·a − 2 a·b + b·b
⟹     2 a·b = −2 a·b
⟹     4 a·b = 0
⟹     a·b = 0
```

Since **a** and **b** are non-zero and their dot product is zero, **a** ⊥ **b**. ∎

### Q8 — direction cosines of î + 2ĵ + 3k̂

```
      |a| = √(1 + 4 + 9) = √14
```

```
      l = 1/√14          m = 2/√14          n = 3/√14
```

*Check:* l² + m² + n² = (1 + 4 + 9)/14 = 14/14 = 1 ✓

### Q9 — unit vector perpendicular to both a and b

A vector perpendicular to both is **a** × **b**:

```
               | î   ĵ   k̂ |
      a × b =  | 1   1   1 |
               | 1   2   3 |

            = î(1·3 − 1·2) − ĵ(1·3 − 1·1) + k̂(1·2 − 1·1)
            = î(3 − 2) − ĵ(3 − 1) + k̂(2 − 1)
            = î − 2ĵ + k̂
```

```
      |a × b| = √(1 + 4 + 1) = √6
```

```
      Required unit vector = (î − 2ĵ + k̂)/√6
```

*(The vector −(î − 2ĵ + k̂)/√6 is also perpendicular to both — it points the opposite way. Mention
this if the question says "find a unit vector"; either is acceptable, but note there are two.)*

### Q10 — section formula

R divides AB internally in the ratio m : n = 2 : 1, so

```
      r = (m b + n a)/(m + n) = (2b + 1·a)/(2 + 1)
```

```
      r = (2b + a)/3
```

### Q11 — unit vectors with a + b + c = 0

Take the square of the magnitude of both sides:

```
      |a + b + c|² = |0|² = 0
```

Expanding:

```
      |a|² + |b|² + |c|² + 2(a·b + b·c + c·a) = 0
```

Since **a**, **b**, **c** are **unit** vectors, |**a**|² = |**b**|² = |**c**|² = 1:

```
      1 + 1 + 1 + 2(a·b + b·c + c·a) = 0
⟹     3 + 2(a·b + b·c + c·a) = 0
⟹     a·b + b·c + c·a = −3/2
```

### Q12 — a × b = 0 for non-zero vectors

|**a** × **b**| = |**a**||**b**| sin θ = 0 with |**a**|, |**b**| ≠ 0 forces sin θ = 0, so θ = 0 or π —
i.e. the vectors are **parallel** (or antiparallel, which still counts as parallel/collinear).

**Answer: (b) a ∥ b**

### Q13 — area of parallelogram from its diagonals

```
      Area = ½ |d₁ × d₂|
```

```
                | î   ĵ   k̂ |
      d₁ × d₂ = | 3   1  −2 |
                | 1  −3   4 |

              = î(1·4 − (−2)(−3)) − ĵ(3·4 − (−2)(1)) + k̂(3(−3) − 1(1))
              = î(4 − 6) − ĵ(12 + 2) + k̂(−9 − 1)
              = −2î − 14ĵ − 10k̂
```

```
      |d₁ × d₂| = √(4 + 196 + 100) = √300 = 10√3
```

```
      Area = ½ (10√3) = 5√3 square units
```

> **Note the ½.** For *adjacent sides* the area is |**a** × **b**|; for *diagonals* it is
> ½|**d₁** × **d₂**|. Reading which one the question gives you is the whole question.

---

## 5. Test yourself

Time: 40 minutes. Answers below.

1. *(1)* The magnitude of the vector 3î − 2ĵ + 6k̂ is
   (a) 7 (b) 5 (c) √41 (d) 11
2. *(1)* If **a**·**b** = 0 for non-zero **a**, **b**, then the angle between them is
   (a) 0 (b) π/4 (c) π/2 (d) π
3. *(1)* î × ĵ equals
   (a) 0 (b) k̂ (c) −k̂ (d) 1
4. *(2)* Find a unit vector in the direction of **a** + **b** where **a** = î + 2ĵ − k̂ and
   **b** = 2î + ĵ + k̂.
5. *(2)* Find the angle between **a** = î + ĵ and **b** = ĵ + k̂.
6. *(2)* Find the projection of **a** = î − ĵ on **b** = î + ĵ.
7. *(2)* Find p if **a** = 3î + 2ĵ + 9k̂ and **b** = î + pĵ + 3k̂ are parallel.
8. *(3)* Find the area of the parallelogram whose adjacent sides are **a** = î − ĵ + 3k̂ and
   **b** = 2î − 7ĵ + k̂.
9. *(3)* Find the area of the triangle with vertices A(1, 2, 3), B(2, −1, 4) and C(4, 5, −1).
10. *(2)* If |**a**| = 5, |**b**| = 13 and |**a** × **b**| = 25, find **a**·**b**.
11. *(2)* Find the direction cosines of the line joining A(1, 2, −3) and B(−1, −2, 1).
12. *(2)* Find the position vector of the midpoint of the segment joining the points with position
    vectors 2î + 3ĵ − k̂ and 4î − ĵ + 3k̂.
13. *(3)* If **a** = î + ĵ + k̂ and **b** = ĵ − k̂, find a vector **c** such that
    **a** × **c** = **b** and **a**·**c** = 3.

### Answer key

**1. (a) 7.** √(9 + 4 + 36) = √49 = 7.

**2. (c) π/2.**

**3. (b) k̂.**

**4. (3î + 3ĵ)/(3√2) = (î + ĵ)/√2.** **a** + **b** = 3î + 3ĵ + 0k̂, magnitude √18 = 3√2.

**5. π/3.** **a**·**b** = 0 + 1 + 0 = 1; |**a**| = |**b**| = √2. cos θ = 1/2, θ = π/3.

**6. 0.** **a**·**b** = 1 − 1 = 0, so the projection is 0 (they are perpendicular).

**7. p = 2/3.** Parallel ⟹ components proportional: 3/1 = 2/p = 9/3 = 3, so 2/p = 3 ⟹ p = 2/3.

**8. 15√2.** **a** × **b** = î((−1)(1) − 3(−7)) − ĵ((1)(1) − 3(2)) + k̂((1)(−7) − (−1)(2))
= î(−1 + 21) − ĵ(1 − 6) + k̂(−7 + 2) = 20î + 5ĵ − 5k̂.
|**a** × **b**| = √(400 + 25 + 25) = √450 = 15√2.

**9. √274/2 square units.**
AB = î − 3ĵ + k̂; AC = 3î + 3ĵ − 4k̂.
AB × AC = î((−3)(−4) − (1)(3)) − ĵ((1)(−4) − (1)(3)) + k̂((1)(3) − (−3)(3))
= î(12 − 3) − ĵ(−4 − 3) + k̂(3 + 9) = 9î + 7ĵ + 12k̂.
|AB × AC| = √(81 + 49 + 144) = √274. **Area = √274/2 square units.**

**10. ±60.** (**a**·**b**)² = |**a**|²|**b**|² − |**a**×**b**|² = 25(169) − 625 = 4225 − 625 = 3600,
so **a**·**b** = ±60.

**11. (−1/3, −2/3, 2/3).** AB = −2î − 4ĵ + 4k̂, |AB| = √(4 + 16 + 16) = 6.
Direction cosines = (−2/6, −4/6, 4/6) = (−1/3, −2/3, 2/3). *Check: 1/9 + 4/9 + 4/9 = 1 ✓*

**12. 3î + ĵ + k̂.** Midpoint = ((2+4)/2)î + ((3−1)/2)ĵ + ((−1+3)/2)k̂ = 3î + ĵ + k̂.

**13. c = (5/3)î + (2/3)ĵ + (2/3)k̂.**
Let **c** = c₁î + c₂ĵ + c₃k̂.
**a**·**c** = c₁ + c₂ + c₃ = 3   …(i)
**a** × **c** = î(c₃ − c₂) − ĵ(c₃ − c₁) + k̂(c₂ − c₁) = 0î + ĵ − k̂
⟹ c₃ − c₂ = 0 …(ii);  −(c₃ − c₁) = 1 ⟹ c₁ − c₃ = 1 …(iii);  c₂ − c₁ = −1 …(iv)
From (ii): c₂ = c₃. From (iv): c₁ = c₂ + 1 = c₃ + 1, consistent with (iii).
Substituting into (i): (c₃ + 1) + c₃ + c₃ = 3 ⟹ 3c₃ = 2 ⟹ c₃ = 2/3, c₂ = 2/3, c₁ = 5/3.

**Scoring.** Out of 26. Below 19 → the loss is almost certainly the cross-product determinant sign
pattern (the middle term is **minus**). Redo §3 Q5, Q9 and Q13.

---

## 6. Answering tips

1. **Write vectors with the arrow or in î ĵ k̂ form in your final answer.** A vector answer written as
   a bare triple, or without the hats, loses the last mark. The marking scheme distinguishes vector
   answers from scalar ones.

2. **State whether your answer is a scalar or a vector.** Dot product → scalar. Cross product →
   vector. Projection → scalar. Area → scalar. Unit vector → vector. If your "area" has an î in it,
   you forgot to take the magnitude.

3. **Compute the cross product as a determinant, written out.** Do not attempt it component by
   component from memory. And **the middle term carries a minus sign** — write −ĵ(…) explicitly. This
   is the single commonest error in the chapter.

4. **Projection divides by the magnitude of the vector you project *onto*.** Projection of **a** on
   **b** is **a**·**b**/|**b**|. Write the formula down before substituting.

5. **For "find a unit vector perpendicular to both", the answer is (a × b)/|a × b|** — two steps, and
   both are marked. Note that the negative is also valid, and saying so shows understanding.

6. **Area: know which of the two formulas applies.** Adjacent sides → |**a**×**b**|. Diagonals →
   ½|**d₁**×**d₂**|. Triangle from two sides → ½|**a**×**b**|. Read the question for which is given.

7. **For a triangle from three vertices, form both side vectors from the *same* vertex.** AB and AC,
   not AB and BC (which also works but is easier to get wrong).

8. **For perpendicularity/parallelism questions, state the condition first.** "Since the vectors are
   perpendicular, **a**·**b** = 0" and then substitute. The condition line is a mark.

9. **Verify direction cosines with l² + m² + n² = 1.** Five seconds, and it catches any arithmetic
   error in |**a**|.

10. **Rationalise or leave surds tidily.** 10/√6 is acceptable; (5√6)/3 is tidier. Both score. Do
    not convert to a decimal.

11. **Use the identity |a×b|² + (a·b)² = |a|²|b|² whenever a question gives you three of the four
    quantities.** It turns a two-step trigonometric argument into one line, and it is exactly why
    CBSE sets those 2-markers.

12. **For "find c such that a × c = b and a·c = k", set up c = c₁î + c₂ĵ + c₃k̂ and get three
    simultaneous equations.** Label them (i)–(iv) and solve systematically. Trying to guess **c**
    wastes the question.
