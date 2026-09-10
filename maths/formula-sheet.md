# Mathematics (041) — Complete Formula Sheet

Everything in the current syllabus, on one page. **Deleted topics are not here** — if a formula you
half-remember is missing, check [`../docs/00-exam-blueprint.md`](../docs/00-exam-blueprint.md) §3
before hunting for it; it is probably out of syllabus.

Use this for the daily 20-minute revision in February, and read it once on the morning of the exam.

---

## Ch 1 — Relations and Functions

```
Reflexive    : (a, a) ∈ R for every a ∈ A
Symmetric    : (a, b) ∈ R ⟹ (b, a) ∈ R
Transitive   : (a, b), (b, c) ∈ R ⟹ (a, c) ∈ R
Equivalence  : all three

One-one (injective) : f(x₁) = f(x₂) ⟹ x₁ = x₂       [or f′ of one sign throughout]
Onto (surjective)   : range = codomain
Bijective           : both

Equivalence class  [a] = { x ∈ A : (a, x) ∈ R };  classes partition A

|A| = m, |B| = n :
  relations A→B     = 2^(mn)          relations on A (|A| = n) = 2^(n²)
  reflexive on A    = 2^(n² − n)      symmetric on A           = 2^(n(n+1)/2)
  functions A→B     = n^m             one-one A→B (m ≤ n)      = n!/(n − m)!
  bijections A→A    = n!
```

## Ch 2 — Inverse Trigonometric Functions

```
              DOMAIN            RANGE (principal value branch)
sin⁻¹ x      [−1, 1]           [−π/2, π/2]
cos⁻¹ x      [−1, 1]           [0, π]
tan⁻¹ x      R                 (−π/2, π/2)
cot⁻¹ x      R                 (0, π)
sec⁻¹ x      |x| ≥ 1           [0, π] − {π/2}
cosec⁻¹ x    |x| ≥ 1           [−π/2, π/2] − {0}

Family A (sin⁻¹, tan⁻¹, cosec⁻¹) : f(−x) = −f(x)
Family B (cos⁻¹, cot⁻¹, sec⁻¹)   : f(−x) = π − f(x)      ← never negative

sin⁻¹(sin θ) = θ  ONLY if θ ∈ [−π/2, π/2] ;  else reduce
cos⁻¹(cos θ) = θ  ONLY if θ ∈ [0, π]      ;  else reduce
tan⁻¹(tan θ) = θ  ONLY if θ ∈ (−π/2, π/2) ;  else reduce

sin⁻¹x + cos⁻¹x = π/2

sin(cos⁻¹x) = √(1 − x²)      tan(sin⁻¹x) = x/√(1 − x²)      sec(tan⁻¹x) = √(1 + x²)
```

## Ch 3 — Matrices

```
Order m × n → mn elements ;  a_ij = row i, column j
Number of possible orders for k elements = number of divisors of k
Number of m × n matrices with entries from a set of size s = s^(mn)

AB defined iff cols(A) = rows(B) ;  A(m×n) B(n×p) = AB(m×p)

(A′)′ = A      (kA)′ = kA′      (A + B)′ = A′ + B′      (AB)′ = B′A′

Symmetric      : A′ = A
Skew-symmetric : A′ = −A  ⟹  all diagonal entries = 0  ⟹  trace = 0
A = ½(A + A′) + ½(A − A′)                [symmetric + skew-symmetric]

A + A′, AA′, A′A are symmetric ;  A − A′ is skew-symmetric
A, B symmetric ⟹ AB + BA symmetric, AB − BA skew-symmetric

AB ≠ BA in general ;  AB = O does NOT imply A = O or B = O
(A + B)² = A² + AB + BA + B²             [NOT A² + 2AB + B²]

For 2 × 2 :  A² − (trace A)·A + (det A)·I = O
```

## Ch 4 — Determinants

```
2 × 2 :  |A| = ad − bc

3 × 3 :  expand along the row/column with the most zeros
         signs :   + − +
                   − + −
                   + − +

Minor M_ij    : delete row i, column j
Cofactor A_ij = (−1)^(i+j) M_ij

adj A = TRANSPOSE of the cofactor matrix
A (adj A) = (adj A) A = |A| I
A⁻¹ = (1/|A|) adj A                      (requires |A| ≠ 0)

2 × 2 shortcut : adj [[a, b], [c, d]] = [[d, −b], [−c, a]]

|AB| = |A||B|        |Aᵀ| = |A|          |kA| = kⁿ|A|        |Aⁿ| = |A|ⁿ
|A⁻¹| = 1/|A|        |adj A| = |A|^(n−1)
adj(AB) = (adj B)(adj A)                 (AB)⁻¹ = B⁻¹A⁻¹
det of a skew-symmetric matrix of ODD order = 0

Area of triangle = ½ | det [[x₁,y₁,1],[x₂,y₂,1],[x₃,y₃,1]] |
Collinear ⟺ that determinant = 0

AX = B → X = A⁻¹B if |A| ≠ 0                      (unique solution, consistent)
|A| = 0 and (adj A)B ≠ O  → inconsistent, no solution
|A| = 0 and (adj A)B = O  → infinitely many, or none
```

## Ch 5 — Continuity and Differentiability

```
CONTINUOUS at a  : LHL = RHL = f(a)
   LHL = lim f(a − h),  RHL = lim f(a + h),  h → 0⁺

DIFFERENTIABLE at a : LHD = RHD, both finite
   differentiable ⟹ continuous ;  continuous ⇏ differentiable  (|x| at 0)

DERIVATIVES
  xⁿ → n x^(n−1)          log x → 1/x            log_a x → 1/(x log a)
  eˣ → eˣ                 aˣ → aˣ log a          constant → 0

  sin x → cos x            cos x → −sin x
  tan x → sec²x            cot x → −cosec²x
  sec x → sec x tan x      cosec x → −cosec x cot x

  sin⁻¹x → 1/√(1 − x²)     cos⁻¹x → −1/√(1 − x²)
  tan⁻¹x → 1/(1 + x²)      cot⁻¹x → −1/(1 + x²)
  sec⁻¹x → 1/(|x|√(x²−1))  cosec⁻¹x → −1/(|x|√(x²−1))

RULES
  Chain    : dy/dx = f′(g(x)) · g′(x)
  Product  : (uv)′ = u′v + uv′
  Quotient : (u/v)′ = (u′v − uv′)/v²
  Implicit : differentiate both sides; every y term gains a dy/dx
  Log diff : variable in base AND exponent → take log first
  Parametric : dy/dx = (dy/dt)/(dx/dt)
               d²y/dx² = [ d/dt (dy/dx) ] / (dx/dt)     ← divide AGAIN

STANDARD LIMITS
  lim (sin x)/x = 1     lim (tan x)/x = 1     lim (eˣ − 1)/x = 1     lim (1+x)^(1/x) = e
  x→0                   x→0                    x→0                    x→0

"PROVE A RELATION" METHOD
  differentiate → clear the radical → SQUARE both sides → differentiate → divide by 2y′
```

## Ch 6 — Application of Derivatives

```
RATES : dy/dt = (dy/dx)(dx/dt).  Always state units.

  Circle   A = πr² → dA/dt = 2πr dr/dt      C = 2πr → dC/dt = 2π dr/dt
  Sphere   V = (4/3)πr³ → dV/dt = 4πr² dr/dt    S = 4πr² → dS/dt = 8πr dr/dt
  Cube     V = x³ → dV/dt = 3x² dx/dt       S = 6x² → dS/dt = 12x dx/dt

MONOTONICITY
  f′(x) > 0 on I ⟹ strictly increasing        f′(x) < 0 on I ⟹ strictly decreasing
  Method: f′ → factorise → critical points → sign table → state intervals

EXTREMA
  Critical point : f′(c) = 0 or f′(c) undefined
  1st derivative test : f′ goes + → − ⟹ MAX ;  − → + ⟹ MIN ;  no change ⟹ inflection
  2nd derivative test : f′(c) = 0 and f″(c) < 0 ⟹ MAX ;  f″(c) > 0 ⟹ MIN ;  = 0 ⟹ test fails
  Absolute extrema on [a, b] : compare f at critical points AND at both endpoints

STANDARD OPTIMISATION RESULTS
  Open box from square sheet of side a, corners x cut  →  x = a/6
  Max-area rectangle in a circle                       →  a SQUARE
  Max-volume cylinder in a sphere of radius R          →  h = 2R/√3
  Max-volume cone in a sphere of radius R              →  h = 4R/3
  Window (rectangle + semicircle), perimeter P         →  height = radius = P/(4 + π)
  Wire length L cut into square + circle, min area     →  circle piece = Lπ/(π + 4)
  Fixed sum, min sum of squares/cubes                  →  the numbers are EQUAL
```

## Ch 7 — Integrals

```
STANDARD
  ∫ xⁿ dx = x^(n+1)/(n+1) + C   (n ≠ −1)      ∫ dx/x = log|x| + C
  ∫ eˣ dx = eˣ + C                            ∫ aˣ dx = aˣ/log a + C

  ∫ sin x dx = −cos x + C                     ∫ cos x dx = sin x + C
  ∫ sec²x dx = tan x + C                      ∫ cosec²x dx = −cot x + C
  ∫ sec x tan x dx = sec x + C                ∫ cosec x cot x dx = −cosec x + C
  ∫ tan x dx = log|sec x| + C                 ∫ cot x dx = log|sin x| + C
  ∫ sec x dx = log|sec x + tan x| + C         ∫ cosec x dx = log|cosec x − cot x| + C
  ∫ dx/√(1 − x²) = sin⁻¹x + C                 ∫ dx/(1 + x²) = tan⁻¹x + C

THE NINE SPECIAL FORMS
  ∫ dx/(x² − a²)  = (1/2a) log|(x − a)/(x + a)| + C
  ∫ dx/(a² − x²)  = (1/2a) log|(a + x)/(a − x)| + C
  ∫ dx/(x² + a²)  = (1/a) tan⁻¹(x/a) + C

  ∫ dx/√(x² − a²) = log|x + √(x² − a²)| + C
  ∫ dx/√(x² + a²) = log|x + √(x² + a²)| + C
  ∫ dx/√(a² − x²) = sin⁻¹(x/a) + C

  ∫ √(a² − x²) dx = (x/2)√(a² − x²) + (a²/2) sin⁻¹(x/a) + C
  ∫ √(x² + a²) dx = (x/2)√(x² + a²) + (a²/2) log|x + √(x² + a²)| + C
  ∫ √(x² − a²) dx = (x/2)√(x² − a²) − (a²/2) log|x + √(x² − a²)| + C     ← MINUS

BY PARTS
  ∫ u v dx = u ∫v dx − ∫ (du/dx)(∫v dx) dx
  ILATE : Inverse, Log, Algebraic, Trig, Exponential   (choose u = the earlier one)
  ∫ log x dx = x log x − x + C
  ∫ eˣ [ f(x) + f′(x) ] dx = eˣ f(x) + C

PARTIAL FRACTIONS (numerator degree < denominator degree; else divide first)
  (x−a)(x−b)              → A/(x−a) + B/(x−b)
  (x−a)²                  → A/(x−a) + B/(x−a)²
  (x−a)(x−b)(x−c)         → A/(x−a) + B/(x−b) + C/(x−c)
  (x−a)²(x−b)             → A/(x−a) + B/(x−a)² + C/(x−b)
  (x−a)(x²+bx+c) irred.   → A/(x−a) + (Bx + C)/(x²+bx+c)

TRIG REDUCTION
  sin²x = (1 − cos 2x)/2        cos²x = (1 + cos 2x)/2
  sin 2x = 2 sin x cos x        cos 2x = 1 − 2sin²x = 2cos²x − 1
  2 sin A cos B = sin(A+B) + sin(A−B)
  2 cos A cos B = cos(A+B) + cos(A−B)
  2 sin A sin B = cos(A−B) − cos(A+B)

DEFINITE INTEGRAL PROPERTIES
  ∫[a,b] f = −∫[b,a] f  ;  ∫[a,a] f = 0
  ∫[a,b] f = ∫[a,c] f + ∫[c,b] f
  ∫[a,b] f(x)dx = ∫[a,b] f(a + b − x)dx
  ∫[0,a] f(x)dx = ∫[0,a] f(a − x)dx                        ← the workhorse
  ∫[0,2a] f = ∫[0,a] f(x)dx + ∫[0,a] f(2a − x)dx
  ∫[0,2a] f = 2∫[0,a] f  if f(2a − x) = f(x) ;  = 0 if f(2a − x) = −f(x)
  ∫[−a,a] f = 2∫[0,a] f  if f EVEN ;  = 0 if f ODD

  NO +C in a definite integral.  Change the limits when you substitute.
```

## Ch 8 — Application of Integrals

```
Area (strips ∥ y-axis) = ∫[a,b] y dx
Area (strips ∥ x-axis) = ∫[c,d] x dy

Below the axis → split at the crossing point and take |absolute value| of each piece

Circle  x² + y² = a²          area = πa²  ;  quadrant = πa²/4
Ellipse x²/a² + y²/b² = 1     area = πab  ;  quadrant = πab/4
Parabola y² = 4ax             symmetric about the x-axis (double the upper half)
Parabola x² = 4ay             symmetric about the y-axis

∫[0,a] √(a² − x²) dx = πa²/4

Sector of a circle, angle θ (radians) = (θ/2π) πa² = ½a²θ

PROCEDURE: sketch → intersections → shade → choose variable → limits → evaluate → "square units"
```

## Ch 9 — Differential Equations

```
ORDER  = order of the highest derivative
DEGREE = power of the highest-order derivative, after clearing radicals and fractions
         NOT DEFINED if the equation is not polynomial in its derivatives
         (contains sin(dy/dx), log(dy/dx), e^(dy/dx))

VARIABLES SEPARABLE : f(y)dy = g(x)dx  → integrate both sides, one +C

HOMOGENEOUS : dy/dx = F(y/x)
  put y = vx  and  dy/dx = v + x dv/dx     ← the "+v" is essential
  separate in v and x, integrate, then substitute v = y/x back
  (if naturally dx/dy = F(x/y), put x = vy instead)

LINEAR : dy/dx + P(x)y = Q(x)
  I.F. = e^(∫P dx)
  y · (I.F.) = ∫ Q · (I.F.) dx + C          ← Q TIMES the I.F.

  y-version : dx/dy + P(y)x = Q(y),  I.F. = e^(∫P dy),  x·(I.F.) = ∫Q·(I.F.)dy + C

I.F. SHORTCUTS
  P = k      → e^(kx)        P = 1/x   → x         P = n/x   → xⁿ
  P = −1/x   → 1/x           P = tan x → sec x     P = cot x → sin x
  P = −tan x → cos x

GROWTH/DECAY : dN/dt = kN  →  N = N₀ e^(kt)
```

## Ch 10 — Vector Algebra

```
|a| = √(a₁² + a₂² + a₃²)          â = a/|a|
AB = b − a                        (head minus tail)

Section formula (A(a), B(b), ratio m : n)
  internal : r = (mb + na)/(m + n)      external : r = (mb − na)/(m − n)
  midpoint : r = (a + b)/2

Direction cosines : l = a₁/|a|, m = a₂/|a|, n = a₃/|a| ;   l² + m² + n² = 1

DOT (scalar)
  a·b = |a||b| cos θ = a₁b₁ + a₂b₂ + a₃b₃           a·a = |a|²
  cos θ = a·b / (|a||b|)
  perpendicular ⟺ a·b = 0
  projection of a on b = a·b/|b|                    (a SCALAR, may be negative)
  vector projection of a on b = [ (a·b)/|b|² ] b
  î·î = ĵ·ĵ = k̂·k̂ = 1 ;  î·ĵ = ĵ·k̂ = k̂·î = 0

CROSS (vector)
  a × b = determinant with rows  î ĵ k̂ / a₁ a₂ a₃ / b₁ b₂ b₃
        = î(a₂b₃ − a₃b₂) − ĵ(a₁b₃ − a₃b₁) + k̂(a₁b₂ − a₂b₁)    ← middle term MINUS
  |a × b| = |a||b| sin θ           a × b = −(b × a)          a × a = 0
  parallel ⟺ a × b = 0
  î×ĵ = k̂,  ĵ×k̂ = î,  k̂×î = ĵ

  area of parallelogram (adjacent sides a, b) = |a × b|
  area of parallelogram (diagonals d₁, d₂)    = ½ |d₁ × d₂|
  area of triangle (two sides a, b)           = ½ |a × b|
  unit vector ⊥ to both a and b               = (a × b)/|a × b|

|a × b|² + (a·b)² = |a|² |b|²
|a + b| = |a − b|  ⟺  a ⊥ b
a, b, c unit with a + b + c = 0  ⟹  a·b + b·c + c·a = −3/2
```

## Ch 11 — Three Dimensional Geometry (lines only)

```
DRs of AB = (x₂ − x₁, y₂ − y₁, z₂ − z₁) ;  divide by |AB| for direction cosines

LINE through A(a) with direction b :
  vector    : r = a + λb
  Cartesian : (x − x₁)/a₁ = (y − y₁)/a₂ = (z − z₁)/a₃
  general point : (a₁λ + x₁, a₂λ + y₁, a₃λ + z₁)

LINE through A(a) and B(b) : r = a + λ(b − a)
  Cartesian : (x − x₁)/(x₂ − x₁) = (y − y₁)/(y₂ − y₁) = (z − z₁)/(z₂ − z₁)

ANGLE between two lines : cos θ = |b₁·b₂| / (|b₁||b₂|)          ← MODULUS
  perpendicular : a₁a₂ + b₁b₂ + c₁c₂ = 0
  parallel      : a₁/a₂ = b₁/b₂ = c₁/c₂

SKEW LINES : neither parallel nor intersecting

SHORTEST DISTANCE
  skew     : d = | (b₁ × b₂) · (a₂ − a₁) | / | b₁ × b₂ |
  parallel : d = | b × (a₂ − a₁) | / | b |
  d = 0 ⟹ the lines intersect

FOOT OF PERPENDICULAR from P : general point Q(λ) → PQ·b = 0 → solve λ → Q
IMAGE of P in the line        : P′ = 2Q − P

Before reading DRs, normalise so the coefficient of x, y, z inside each bracket is 1:
  (2y − 1)/4 = (y − ½)/2
```

## Ch 12 — Linear Programming

```
Z = ax + by  (objective function) ;  inequalities are the constraints

CORNER-POINT METHOD
  1. all constraints, including x ≥ 0, y ≥ 0
  2. boundary lines and their intercepts
  3. graph on graph paper, scale stated, lines labelled
  4. shade the feasible region (test the origin in each inequality)
  5. corner points by SOLVING SIMULTANEOUS EQUATIONS — not by reading the graph
  6. table of Z at each corner point
  7. state the optimum: value, point, and max/min

BOUNDED region   → both max and min exist, at corner points
UNBOUNDED region → may not exist; CHECK:
  M is the max ⟺ ax + by > M has no point in common with the feasible region
  m is the min ⟺ ax + by < m has no point in common with the feasible region

Equal Z at two corner points → infinitely many optima, all along that segment
Contradictory constraints     → empty feasible region → no feasible solution
```

## Ch 13 — Probability

```
CONDITIONAL : P(A|B) = P(A ∩ B)/P(B),  P(B) ≠ 0        ← "given" is the DENOMINATOR
  P(A′|B) = 1 − P(A|B)
  P((A ∪ C)|B) = P(A|B) + P(C|B) − P((A ∩ C)|B)

MULTIPLICATION : P(A ∩ B) = P(A)P(B|A) = P(B)P(A|B)
  P(A ∩ B ∩ C) = P(A) P(B|A) P(C|A ∩ B)               ← "without replacement"

INDEPENDENT : P(A ∩ B) = P(A)P(B)  ⟺  P(A|B) = P(A)
  P(A ∪ B) = P(A) + P(B) − P(A)P(B)
  P(neither) = (1 − P(A))(1 − P(B))
  P(at least one) = 1 − P(neither)
  independent ≠ mutually exclusive
  mutually exclusive with non-zero probabilities ⟹ NOT independent

ADDITION : P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

TOTAL PROBABILITY : P(A) = Σᵢ P(Eᵢ) P(A|Eᵢ)          (E₁…Eₙ a partition)

BAYES : P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ) / Σⱼ P(Eⱼ)P(A|Eⱼ)
  LAYOUT: define events → all priors → all likelihoods → formula → substitute
  P(Eᵢ) are PRIORS ; P(Eᵢ|A) are POSTERIORS

RANDOM VARIABLE
  Σ pᵢ = 1  and  pᵢ ≥ 0                               ← use this to find an unknown constant
  Mean = E(X) = Σ xᵢ pᵢ
  (Variance and the Binomial distribution are OUT of syllabus)
```

---

## The last-page checklist, for the exam hall

Before you hand the paper in:

1. `+ C` on every indefinite integral; **no** `+ C` on any definite integral.
2. Every vector answer written with î ĵ k̂ or an arrow.
3. Every area answered in "square units"; every rate with its unit.
4. Every graph: axes labelled, scale stated, region shaded, corner points named.
5. Every "prove" ended with an explicit concluding line.
6. Abandoned internal-choice attempts crossed out.
7. Question numbers matching the paper.
8. Modulus signs present in log answers, and in the angle-between-lines formula.
