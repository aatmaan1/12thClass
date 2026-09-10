# Ch 3 — Matrices

**Unit II (10 marks, shared with Ch 4) · Typical appearance: 1–2 MCQs + one 2- or 3-mark question.
The heavy 5-marker for this unit lives in Ch 4.**

---

## 1. Scope

### In the syllabus

- Concept, notation, **order**, equality of matrices
- **Types**: row, column, square, diagonal, scalar, identity, zero
- **Transpose**; **symmetric** and **skew-symmetric** matrices
- **Operations**: addition, scalar multiplication, matrix multiplication
- Properties of these operations; **non-commutativity** of matrix multiplication

### Deleted — do not study

- Concept of **elementary row and column operations**
- **Inverse of a matrix by elementary operations**
- Existence of non-zero matrices whose product is the zero matrix (as a stated topic)
- Invertible matrices and the **proof of uniqueness of the inverse**

> **Consequence.** Finding A⁻¹ now happens **only** via the adjoint method, which lives in
> [Ch 4 Determinants](04-determinants.md). If a practice question says "find the inverse using
> elementary row transformations", skip it — it is out of syllabus.

---

## 2. Brief

### Definition and order

A **matrix** is a rectangular array of numbers. A matrix with m rows and n columns has **order
m × n**, written A = [a_ij]_(m×n), where a_ij is the element in the **iᵗʰ row and jᵗʰ column**.

Row index first, always. a₂₃ is row 2, column 3.

An m × n matrix has **mn elements**.

> **Standard MCQ:** "A matrix has 12 elements. How many possible orders are there?" Answer: count
> factor pairs of 12 — (1,12), (2,6), (3,4), (4,3), (6,2), (12,1) → **6 orders**. If the question adds
> "and it is a square matrix", the answer is 0 (12 is not a perfect square).

> **Standard MCQ:** "How many 3 × 3 matrices are possible with each entry 0 or 1?" There are 9
> entries, 2 choices each → **2⁹ = 512**.

### Types of matrices

| Type | Condition |
| --- | --- |
| Row matrix | order 1 × n |
| Column matrix | order m × 1 |
| Square matrix | m = n |
| Diagonal matrix | square, and a_ij = 0 for all i ≠ j |
| Scalar matrix | diagonal, and all diagonal entries equal |
| Identity matrix I | scalar, with all diagonal entries = 1 |
| Zero (null) matrix O | every entry 0 |
| Upper triangular | square, a_ij = 0 for i > j |
| Lower triangular | square, a_ij = 0 for i < j |

Note the nesting: **identity ⊂ scalar ⊂ diagonal ⊂ square**. Every scalar matrix is diagonal; not
every diagonal matrix is scalar.

### Equality

A = B requires (i) **same order**, and (ii) **a_ij = b_ij for every i, j**.

Both conditions. A 2 × 3 matrix can never equal a 3 × 2 matrix, whatever the entries.

This is the basis of the "find x and y" question: equate corresponding elements to get simultaneous
equations.

### Addition and scalar multiplication

Defined **only for matrices of the same order**; done entry by entry.

| Property | Statement |
| --- | --- |
| Commutative | A + B = B + A |
| Associative | (A + B) + C = A + (B + C) |
| Additive identity | A + O = A |
| Additive inverse | A + (−A) = O |
| Distributive over scalars | k(A + B) = kA + kB; (k + l)A = kA + lA |

### Matrix multiplication — where the rules change

For AB to be defined, the **number of columns of A must equal the number of rows of B**:

```
A(m × n) × B(n × p)  =  AB(m × p)
```

The element (AB)_ij = (iᵗʰ row of A) · (jᵗʰ column of B) = Σₖ a_ik b_kj.

**Properties — note carefully what is and is not true:**

| Property | Holds? |
| --- | --- |
| Associative: (AB)C = A(BC) | ✓ |
| Distributive: A(B + C) = AB + AC | ✓ |
| Multiplicative identity: AI = IA = A | ✓ |
| **Commutative: AB = BA** | ✗ **in general** |
| AB = O ⟹ A = O or B = O | ✗ **false** |
| AB = AC ⟹ B = C (cancellation) | ✗ **false** |

The last three are the ones examined. A concrete counterexample worth memorising:

```
A = [ 0  1 ]      B = [ 0  0 ]      AB = [ 0  0 ]  = O
    [ 0  0 ]          [ 0  1 ]           [ 0  0 ]
```

but neither A nor B is the zero matrix. (And BA = [[0,1],[0,0]] ≠ O, so AB ≠ BA too.)

### Transpose

A′ (also written Aᵀ) is obtained by interchanging rows and columns. If A is m × n, then A′ is n × m,
and (A′)_ij = a_ji.

| Property | Statement |
| --- | --- |
| Double transpose | (A′)′ = A |
| Scalar | (kA)′ = kA′ |
| Sum | (A + B)′ = A′ + B′ |
| **Product (order reverses)** | **(AB)′ = B′A′** |

The reversal in (AB)′ = B′A′ is examined constantly, both as a proof-for-given-matrices question and
as an MCQ. Remember it as "the transpose turns the product inside out".

### Symmetric and skew-symmetric

| | Condition | Consequence for diagonal |
| --- | --- | --- |
| **Symmetric** | A′ = A, i.e. a_ij = a_ji | no restriction |
| **Skew-symmetric** | A′ = −A, i.e. a_ij = −a_ji | **all diagonal elements are 0** |

*Why the diagonal is zero for skew-symmetric:* put i = j in a_ij = −a_ji to get a_ii = −a_ii, so
2a_ii = 0, so a_ii = 0. That two-line argument is itself a 1- or 2-mark question.

**Both must be square matrices** — A′ = ±A forces the order to be n × n.

### The decomposition theorem

**Every square matrix A can be written uniquely as the sum of a symmetric matrix and a
skew-symmetric matrix:**

```
A = P + Q       where     P = ½(A + A′)   is symmetric
                          Q = ½(A − A′)   is skew-symmetric
```

*Proof sketch (worth knowing, it is sometimes asked):*
P′ = ½(A + A′)′ = ½(A′ + A) = P, so P is symmetric.
Q′ = ½(A − A′)′ = ½(A′ − A) = −½(A − A′) = −Q, so Q is skew-symmetric.
And P + Q = ½(A + A′) + ½(A − A′) = A. ∎

### Results worth memorising

For square matrices A and B:

- A + A′ is always **symmetric**
- A − A′ is always **skew-symmetric**
- AA′ and A′A are always **symmetric**
- If A is symmetric, then kA and Aⁿ are symmetric
- If A and B are symmetric, then **AB + BA is symmetric** and **AB − BA is skew-symmetric**
- If A and B are symmetric, AB is symmetric **only if** AB = BA
- If A is skew-symmetric, A² is **symmetric**

### Quick recall box

```
Order m×n → mn elements.   a_ij = row i, column j.
Number of orders for k elements = number of factor pairs of k.
Number of m×n matrices with entries from a set of size s = s^(mn).

AB defined iff cols(A) = rows(B);  A(m×n)B(n×p) = AB(m×p)

(A′)′ = A      (kA)′ = kA′      (A+B)′ = A′+B′      (AB)′ = B′A′

Symmetric      : A′ = A
Skew-symmetric : A′ = −A  ⟹ all diagonal entries are 0
A = ½(A+A′) + ½(A−A′)          [symmetric + skew-symmetric]

AB ≠ BA in general.  AB = O does NOT imply A = O or B = O.
```

---

## 3. Previous years' questions

**Q1.** *(2 marks)* Find x and y if

```
2 [ 1  3 ] + [ y   0 ] = [ 5  6 ]
  [ 0  x ]   [ 1   2 ]   [ 1  8 ]
```

**Q2.** *(1 mark)* If a matrix has 24 elements, what are the possible orders it can have? What if it
has 13 elements?

**Q3.** *(3 marks)* Express the matrix

```
A = [  2   4  −6 ]
    [  7   3   5 ]
    [  1  −2   4 ]
```

as the sum of a symmetric and a skew-symmetric matrix.

**Q4.** *(2 marks)* If

```
A = [ 0   a   3 ]
    [ 2   b  −1 ]
    [ c   1   0 ]
```

is a skew-symmetric matrix, find the values of a, b and c.

**Q5.** *(3 marks)* If A = [[1, 2], [3, 4]], show that A² − 5A − 2I = O.

**Q6.** *(1 mark, MCQ)* The number of all possible matrices of order 3 × 3 with each entry 0, 1 or 2 is
(a) 27 (b) 18 (c) 81 (d) 3⁹

**Q7.** *(3 marks)* If A and B are symmetric matrices of the same order, prove that AB − BA is
skew-symmetric.

**Q8.** *(2 marks)* If A = [[3, 1], [−1, 2]], find A² and verify (A′)² = (A²)′.

**Q9.** *(2 marks)* Give an example of two non-zero 2 × 2 matrices A and B such that AB = O.

**Q10.** *(1 mark, Assertion–Reason)*
**A:** If A is a skew-symmetric matrix, then all its diagonal elements are zero.
**R:** For a skew-symmetric matrix, a_ij = −a_ji for all i, j.

**Q11.** *(2 marks)* If A = [[cos α, sin α], [−sin α, cos α]], find A + A′ and state whether it is
symmetric.

**Q12.** *(3 marks)* Find a 2 × 2 matrix X such that

```
X [ 1  2 ] = [ 3  4 ]
  [ 3  4 ]   [ 7  10 ]
```

---

## 4. Solutions

### Q1 — find x and y

```
2 [ 1  3 ] = [ 2  6 ]
  [ 0  x ]   [ 0  2x ]
```

Adding:

```
[ 2 + y   6 + 0 ] = [ 5  6 ]
[ 0 + 1   2x + 2 ]   [ 1  8 ]
```

Equating corresponding elements:

- (1,1): 2 + y = 5 ⟹ **y = 3**
- (2,2): 2x + 2 = 8 ⟹ 2x = 6 ⟹ **x = 3**

*(Check the other two entries as a verification: (1,2) gives 6 = 6 ✓, (2,1) gives 1 = 1 ✓.)*

**x = 3, y = 3**

### Q2 — possible orders

**24 elements.** We need ordered pairs (m, n) with mn = 24:

(1,24), (2,12), (3,8), (4,6), (6,4), (8,3), (12,2), (24,1) → **8 possible orders**.

**13 elements.** 13 is prime, so only (1,13) and (13,1) → **2 possible orders**.

> The trick in this question is that (m, n) is *ordered* — a 3 × 8 matrix and an 8 × 3 matrix are
> different. Count divisors, not factor pairs: the number of orders equals the **number of divisors**
> of the element count. 24 has 8 divisors; 13 has 2.

### Q3 — decompose into symmetric + skew-symmetric

First find A′ (swap rows and columns):

```
A′ = [  2   7   1 ]
     [  4   3  −2 ]
     [ −6   5   4 ]
```

**Symmetric part P = ½(A + A′):**

```
A + A′ = [ 2+2    4+7    −6+1 ]   = [  4   11  −5 ]
         [ 7+4    3+3     5−2 ]     [ 11    6   3 ]
         [ 1−6   −2+5     4+4 ]     [ −5    3   8 ]

P = ½(A + A′) = [   2    11/2   −5/2 ]
                [ 11/2    3      3/2 ]
                [ −5/2   3/2      4  ]
```

Check: P′ = P ✓ (it is visibly symmetric about the diagonal).

**Skew-symmetric part Q = ½(A − A′):**

```
A − A′ = [ 2−2    4−7    −6−1 ]   = [  0   −3   −7 ]
         [ 7−4    3−3     5+2 ]     [  3    0    7 ]
         [ 1+6   −2−5     4−4 ]     [  7   −7    0 ]

Q = ½(A − A′) = [   0    −3/2   −7/2 ]
                [  3/2     0     7/2 ]
                [  7/2   −7/2     0  ]
```

Check: diagonal is all zeros ✓ and Q′ = −Q ✓.

**Hence A = P + Q** with P symmetric and Q skew-symmetric.

*(Verify by adding P + Q: the (1,2) entry is 11/2 − 3/2 = 4 ✓, matching A.)*

### Q4 — skew-symmetric, find a, b, c

For a skew-symmetric matrix, a_ij = −a_ji.

**Diagonal:** all diagonal entries must be 0. The (2,2) entry is b, so **b = 0**.

**Off-diagonal:**
- a₁₂ = −a₂₁ : a = −2 ⟹ **a = −2**
- a₁₃ = −a₃₁ : 3 = −c ⟹ **c = −3**
- a₂₃ = −a₃₂ : −1 = −(1) = −1 ✓ (consistent, no new information)

**a = −2, b = 0, c = −3**

Verification — the matrix becomes

```
[  0  −2   3 ]              [  0   2  −3 ]
[  2   0  −1 ]   and A′ =   [ −2   0   1 ]  = −A ✓
[ −3   1   0 ]              [  3  −1   0 ]
```

### Q5 — show A² − 5A − 2I = O for A = [[1,2],[3,4]]

```
A² = [ 1  2 ][ 1  2 ] = [ 1·1+2·3   1·2+2·4 ] = [  7  10 ]
     [ 3  4 ][ 3  4 ]   [ 3·1+4·3   3·2+4·4 ]   [ 15  22 ]

5A = [  5  10 ]        2I = [ 2  0 ]
     [ 15  20 ]             [ 0  2 ]
```

Therefore

```
A² − 5A − 2I = [  7−5−2    10−10−0 ] = [ 0  0 ] = O
               [ 15−15−0   22−20−2 ]   [ 0  0 ]
```

**Hence A² − 5A − 2I = O.** ∎

> **Where this comes from.** For any 2 × 2 matrix, A² − (trace A)·A + (det A)·I = O. Here
> trace = 1 + 4 = 5 and det = 1·4 − 2·3 = −2, giving A² − 5A − 2I = O. Knowing this lets you *predict*
> the relation, which is useful when the question says "find k such that A² = kA + mI".

### Q6 — number of 3 × 3 matrices with entries from {0, 1, 2}

9 positions, 3 choices each → 3⁹.

**Answer: (d) 3⁹** (= 19683)

*(Option (c) 81 = 3⁴ is a distractor; (a) 27 = 3³ counts only one row.)*

### Q7 — if A, B symmetric then AB − BA is skew-symmetric

Given: A′ = A and B′ = B.

We must show (AB − BA)′ = −(AB − BA).

```
(AB − BA)′ = (AB)′ − (BA)′              [transpose of a difference]
           = B′A′ − A′B′                 [(XY)′ = Y′X′]
           = BA − AB                     [since A′ = A, B′ = B]
           = −(AB − BA)
```

Hence AB − BA is **skew-symmetric**. ∎

> Note where each property is used: the transpose-reverses-products rule, then the given symmetry.
> The marking scheme awards a mark for each of those two lines.

### Q8 — A² and verifying (A′)² = (A²)′

```
A = [  3  1 ]
    [ −1  2 ]

A² = [  3  1 ][  3  1 ] = [ 3·3+1·(−1)    3·1+1·2  ] = [  8   5 ]
     [ −1  2 ][ −1  2 ]   [ (−1)·3+2·(−1) (−1)·1+2·2 ]   [ −5   3 ]
```

Now

```
A′ = [ 3  −1 ]
     [ 1   2 ]

(A′)² = [ 3  −1 ][ 3  −1 ] = [ 9−1    −3−2 ] = [  8  −5 ]
        [ 1   2 ][ 1   2 ]   [ 3+2    −1+4 ]   [  5   3 ]

(A²)′ = transpose of [  8  5 ]  = [  8  −5 ]
                     [ −5  3 ]    [  5   3 ]
```

**(A′)² = (A²)′ ✓ verified.**

*(This is a special case of (Aⁿ)′ = (A′)ⁿ, which follows from (AB)′ = B′A′.)*

### Q9 — non-zero A, B with AB = O

```
A = [ 1  0 ]        B = [ 0  0 ]
    [ 0  0 ]            [ 0  1 ]

AB = [ 1·0+0·0   1·0+0·1 ] = [ 0  0 ] = O
     [ 0·0+0·0   0·0+0·1 ]   [ 0  0 ]
```

Both A ≠ O and B ≠ O, yet AB = O.

**This shows the cancellation law fails for matrices:** AB = O does *not* imply A = O or B = O.

*(Also note BA = [[0,0],[0,0]] here — but that is a coincidence of this example. With
A = [[0,1],[0,0]], B = [[0,0],[0,1]] you get AB = O while BA = [[0,1],[0,0]] ≠ O, which additionally
demonstrates non-commutativity.)*

### Q10 — Assertion–Reason

**A:** True. Setting i = j in a_ij = −a_ji gives a_ii = −a_ii ⟹ 2a_ii = 0 ⟹ a_ii = 0.

**R:** True. That is the definition of skew-symmetric, written element-wise.

**Does R explain A?** Yes — A is derived from R by putting i = j.

**Answer: (a) Both A and R are true, and R is the correct explanation of A.**

### Q11 — A + A′ for the rotation matrix

```
A = [  cos α   sin α ]        A′ = [ cos α   −sin α ]
    [ −sin α   cos α ]             [ sin α    cos α ]

A + A′ = [ 2cos α      0    ] = 2cos α · I
         [    0     2cos α  ]
```

This is a **scalar matrix**, hence certainly **symmetric** — consistent with the general result that
A + A′ is symmetric for any square A.

### Q12 — find X

Let X = [[a, b], [c, d]]. Then

```
X [ 1  2 ] = [ a  b ][ 1  2 ] = [ a + 3b    2a + 4b ] = [ 3   4 ]
  [ 3  4 ]   [ c  d ][ 3  4 ]   [ c + 3d    2c + 4d ]   [ 7  10 ]
```

**Row 1:**
```
a + 3b = 3       …(i)
2a + 4b = 4  ⟹  a + 2b = 2   …(ii)
```
(i) − (ii): b = 1. Then from (ii): a = 2 − 2 = 0.

**Row 2:**
```
c + 3d = 7       …(iii)
2c + 4d = 10 ⟹  c + 2d = 5   …(iv)
```
(iii) − (iv): d = 2. Then from (iv): c = 5 − 4 = 1.

```
X = [ 0  1 ]
    [ 1  2 ]
```

*Check:* [[0,1],[1,2]]·[[1,2],[3,4]] = [[3, 4], [1+6, 2+8]] = [[3,4],[7,10]] ✓

---

## 5. Test yourself

Time: 35 minutes. Answers below.

1. *(1)* If A is a 3 × 4 matrix and B is a 4 × 2 matrix, the order of AB is
   (a) 3 × 2 (b) 2 × 3 (c) 4 × 4 (d) not defined
2. *(1)* A matrix has 18 elements. The number of possible orders is
   (a) 3 (b) 5 (c) 6 (d) 9
3. *(1)* If A is a square matrix such that A² = I, then A⁻¹ equals
   (a) I (b) A (c) O (d) 2A
4. *(2)* Find x and y if [[x + y, 2], [5, xy]] = [[6, 2], [5, 8]].
5. *(2)* If A = [[2, 3], [−1, 0]], find A² − 2A.
6. *(2)* If [[0, 2b, −2], [3, 1, 3], [3a, 3, −1]] is symmetric, find a and b.
7. *(2)* Show that for any square matrix A, A − A′ is skew-symmetric.
8. *(3)* Express A = [[3, 5], [1, −1]] as the sum of a symmetric and a skew-symmetric matrix.
9. *(3)* If A = [[2, −1], [3, 4]] and B = [[1, 0], [−2, 5]], verify that (AB)′ = B′A′.
10. *(3)* If A = [[1, 0, 2], [0, 2, 1], [2, 0, 3]], and A³ − 6A² + 7A + kI = O, find k.
11. *(2)* If A is a skew-symmetric matrix of order 3, what can you say about the trace of A?
12. *(3)* Find a matrix A such that 2A + 3B = [[8, 0], [−1, 5]] where B = [[2, 0], [1, 1]].
13. *(1)* If A and B are matrices such that both AB and BA are defined, and A is of order 2 × 3, then
    the order of B is
    (a) 2 × 3 (b) 3 × 2 (c) 2 × 2 (d) 3 × 3

### Answer key

**1. (a) 3 × 2.** cols(A) = 4 = rows(B) ✓, so AB has order rows(A) × cols(B) = 3 × 2.

**2. (c) 6.** 18 has divisors 1, 2, 3, 6, 9, 18 → six divisors → six orders.

**3. (b) A.** A² = I means A·A = I, so A is its own inverse.

**4. x = 2, y = 4 or x = 4, y = 2.** x + y = 6 and xy = 8 ⟹ x, y are roots of t² − 6t + 8 = 0
⟹ t = 2, 4.

**5.** A² = [[2,3],[−1,0]]·[[2,3],[−1,0]] = [[4−3, 6+0], [−2+0, −3+0]] = [[1, 6], [−2, −3]].
2A = [[4, 6], [−2, 0]]. A² − 2A = [[−3, 0], [0, −3]] = −3I.

**6. a = −2/3, b = 3/2.** Symmetric requires a_ij = a_ji: 2b = 3 ⟹ b = 3/2; and −2 = 3a ⟹ a = −2/3.
*(The (2,3) and (3,2) entries are both 3 ✓.)*

**7.** (A − A′)′ = A′ − (A′)′ = A′ − A = −(A − A′). Hence skew-symmetric. ∎

**8.** A′ = [[3, 1], [5, −1]].
P = ½(A + A′) = ½[[6, 6], [6, −2]] = [[3, 3], [3, −1]].
Q = ½(A − A′) = ½[[0, 4], [−4, 0]] = [[0, 2], [−2, 0]].
A = P + Q, with P symmetric and Q skew-symmetric. ✓

**9.** AB = [[2,−1],[3,4]]·[[1,0],[−2,5]] = [[2+2, 0−5], [3−8, 0+20]] = [[4, −5], [−5, 20]].
(AB)′ = [[4, −5], [−5, 20]] (it happens to be symmetric).
B′ = [[1,−2],[0,5]], A′ = [[2,3],[−1,4]].
B′A′ = [[1,−2],[0,5]]·[[2,3],[−1,4]] = [[2+2, 3−8], [0−5, 0+20]] = [[4, −5], [−5, 20]]. ✓ Equal.

**10. k = 2.**
A² = [[5, 0, 8], [2, 4, 5], [8, 0, 13]]
&nbsp;&nbsp;(e.g. the (1,1) entry is 1·1 + 0·0 + 2·2 = 5; the (3,3) entry is 2·2 + 0·1 + 3·3 = 13)
A³ = A²·A = [[21, 0, 34], [12, 8, 23], [34, 0, 55]]
&nbsp;&nbsp;(e.g. the (2,3) entry is 2·2 + 4·1 + 5·3 = 23)
A³ − 6A² + 7A = [[21−30+7, 0, 34−48+14], [12−12+0, 8−24+14, 23−30+7], [34−48+14, 0, 55−78+21]]
= [[−2, 0, 0], [0, −2, 0], [0, 0, −2]] = −2I.
So A³ − 6A² + 7A + kI = O becomes −2I + kI = O, i.e. (k − 2)I = O, giving **k = 2**.

**11. Trace = 0.** All diagonal entries of a skew-symmetric matrix are zero, so their sum is zero.

**12.** 3B = [[6, 0], [3, 3]]. 2A = [[8,0],[−1,5]] − [[6,0],[3,3]] = [[2, 0], [−4, 2]].
A = [[1, 0], [−2, 1]].

**13. (b) 3 × 2.** For AB to be defined, B must have 3 rows. For BA to be defined, cols(B) must
equal rows(A) = 2. So B is 3 × 2.

**Scoring.** Out of 26. Below 18 → redo §3 Q3, Q4, Q7 and the multiplication-property table.

---

## 6. Answering tips

1. **Write the order under every matrix as you go**, e.g. A(2×3), B(3×4). Half the errors in this
   chapter are attempts to add matrices of different orders or multiply in the wrong order. Writing
   the orders makes the mistake impossible to make.

2. **For "find x, y" questions, equate corresponding elements and label your equations (i), (ii).**
   Then verify the entries you did *not* use — that check is free and catches arithmetic slips.

3. **In the symmetric/skew decomposition, always show A′ explicitly as a separate step**, then A + A′,
   then the ½. Three visible steps, three marks. And **state the conclusion**: "where P is symmetric
   and Q is skew-symmetric, hence A = P + Q."

4. **Keep fractions as fractions.** The decomposition of an integer matrix almost always produces
   halves. Write 11/2, not 5.5.

5. **For skew-symmetric questions, do the diagonal first.** Setting diagonal entries to zero is
   usually one full mark and takes five seconds.

6. **For proofs like "AB − BA is skew-symmetric", state the given conditions first** ("Given A′ = A,
   B′ = B"), then transform the transpose step by step, then conclude. Do not skip from
   (AB − BA)′ to −(AB − BA) in one line — the intermediate B′A′ − A′B′ line is a mark.

7. **Never assume AB = BA.** If a question asks you to verify something involving both AB and BA,
   compute both. And when squaring a sum, (A + B)² = A² + AB + BA + B², **not** A² + 2AB + B².

8. **For matrix multiplication, write out the dot-product arithmetic** for at least the first entry:
   "(1,1) entry = 1·1 + 2·3 = 7". It shows method and lets the examiner follow a slip.

9. **Multiplication questions in MCQs:** check whether the product is even *defined* before computing.
   "Not defined" is a real option and is often the answer.

10. **A² − 5A − 2I type questions:** if the question asks you to *find* k rather than verify, use
    A² = (trace)A − (det)I for 2 × 2 matrices to predict it, then verify by direct multiplication.
    Show the multiplication — the prediction alone will not score.
