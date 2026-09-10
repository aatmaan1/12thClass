# Ch 1 — Relations and Functions

**Unit I (8 marks, shared with Ch 2) · Typical appearance: one 1-mark MCQ + one 2/3-mark relation
question, occasionally a 5-mark one-one/onto proof**

---

## 1. Scope

### In the syllabus

- Types of relations: **reflexive, symmetric, transitive** and **equivalence** relations
- **One-one (injective)** and **onto (surjective)** functions

That is the whole chapter. It is short.

### Deleted — do not study

- Composition of functions (g∘f)
- Invertible functions and f⁻¹
- Binary operations

> **Why this matters.** Pre-2023 papers and most YouTube playlists spend half this chapter on
> composition and inverses. All of it is out. If you find yourself computing g∘f, you are on an old
> paper.

---

## 2. Brief

### Start here — in plain English

A **relation** is nothing more than a rule that pairs things up. "Is a sibling of" is a relation on
the set of people. "Is less than" is a relation on numbers. That is the whole definition — a
collection of ordered pairs. The chapter's difficulty is not the idea; it is that three particular
properties of relations have names that sound alike, so let us pin them down with the sibling
example.

**Reflexive** means everything is related to itself. Is "is a sibling of" reflexive? Are you your
own sibling? No. So it fails. **Symmetric** means whenever a is related to b, b is related back to a.
If you are my sibling, am I yours? Yes. So it passes. **Transitive** means if a relates to b and b
relates to c, then a relates to c. If Ravi is Sita's sibling and Sita is Meera's sibling, is Ravi
Meera's sibling? Yes. Passes.

Compare with "is the father of": not reflexive, not symmetric (obviously), and not transitive
either — your father's father is your grandfather, not your father. And with "has the same birthday
as": reflexive, symmetric *and* transitive.

That last kind, which passes all three, is an **equivalence relation**, and it is the one worth
understanding properly because it does something useful. An equivalence relation always chops the
set into non-overlapping groups. "Same birthday" splits humanity into 366 groups. "Same remainder
when divided by 3" splits the integers into three. Nobody is left out, nobody is in two groups at
once. Those groups are **equivalence classes**, and being able to say what the classes *are* is the
usual 3-mark question.

Half the marks in this chapter come from checking those three properties on a given relation, and
the reliable method is: for each property, either prove it in general or produce one counterexample.
One counterexample is a complete answer — you do not need to explain further. Most lost marks come
from asserting "not transitive" without naming the offending triple.

Now **functions**. A function is a relation with one extra restriction: every input gets exactly one
output. A vending machine is a function — press B4 and you always get the same thing. Two words
describe how a function fills its target set. **One-one** (injective) means no two different inputs
share an output — nothing is hit twice. **Onto** (surjective) means nothing in the target is missed —
everything is hit at least once. A function that is both is a **bijection**, and a bijection is
exactly a perfect pairing, which is why it is the condition for having an inverse: if two inputs gave
the same output you would not know which to go back to, and if something was never hit you would
have nothing to go back from.

The picture to keep is arrows from a left-hand set to a right-hand set. One-one means no two arrows
land on the same dot. Onto means no dot on the right is left bare. Draw that once and you will never
confuse the two again.

The practical test for one-one on real functions is either algebra — assume f(a) = f(b) and show
a = b — or calculus: a function that is always increasing (f′ > 0 throughout) cannot repeat a value,
so it is one-one. That second route is quick and underused. For onto, compare the actual range with
the stated codomain; a function is onto only if they are equal, which is why f(x) = x² from ℝ to ℝ
is not onto (it never produces a negative) but is onto if you declare the codomain to be [0, ∞).

**Learn it from someone else too**

- **Video lecture** — [search: relations and functions class 12 maths one shot](https://www.youtube.com/results?search_query=relations+and+functions+class+12+maths+one+shot)
- **Interactive lessons and practice** — [Khan Academy: relations and functions](https://www.khanacademy.org/search?page_search_query=relations%20and%20functions%20class%2012)
- **The book the paper is set from** — [NCERT Maths Part I, Chapter 1 (PDF)](https://ncert.nic.in/textbook/pdf/lemh101.pdf)
- **For extra problems** — NCERT Exemplar Chapter 1, and RD Sharma's chapter on relations for drill
  on checking the three properties. The board asks these almost verbatim from the NCERT exercises,
  so finish those first.

---

### Relations

A **relation** R from set A to set B is any subset of A × B. If (a, b) ∈ R we write **a R b**.
A relation **on** A is a subset of A × A.

- **Domain** of R = set of all first elements appearing in R
- **Range** of R = set of all second elements appearing in R
- **Codomain** = B (the whole target set, whether or not everything in it is hit)

Two extreme cases:
- **Empty relation:** R = ∅ (no element related to any element)
- **Universal relation:** R = A × A (every element related to every element)

Both the empty and the universal relation on A are called **trivial relations**.

### The three properties

Let R be a relation on a set A.

| Property | Definition | To prove it | To disprove it |
| --- | --- | --- | --- |
| **Reflexive** | (a, a) ∈ R for **every** a ∈ A | Show it for a general a | One counterexample a with (a,a) ∉ R |
| **Symmetric** | (a, b) ∈ R ⟹ (b, a) ∈ R | Take general (a,b) ∈ R, derive (b,a) ∈ R | One pair (a,b) ∈ R with (b,a) ∉ R |
| **Transitive** | (a, b) ∈ R and (b, c) ∈ R ⟹ (a, c) ∈ R | Take general (a,b), (b,c) ∈ R, derive (a,c) ∈ R | One triple where the first two hold and the third fails |

> **The single most important asymmetry in this chapter:** to *prove* a property you must argue for
> **all** elements; to *disprove* it, **one** counterexample is enough and is fully sufficient for
> full marks. Students routinely try to prove with an example (worth nothing) and disprove with a
> general argument (wasted effort).

**Equivalence relation** = reflexive **and** symmetric **and** transitive. All three, every time.

### Equivalence classes

If R is an equivalence relation on A, then for a ∈ A the **equivalence class** of a is

```
[a] = { x ∈ A : (a, x) ∈ R }
```

The equivalence classes **partition** A: they are non-empty, pairwise disjoint, and their union is A.
So the question "find all elements related to 1" is asking for [1].

### The relations you will actually be asked about

CBSE reuses a small family. Recognise them:

| Relation | Reflexive | Symmetric | Transitive |
| --- | --- | --- | --- |
| a R b ⟺ a = b (identity) | ✓ | ✓ | ✓ |
| a R b ⟺ a ≤ b | ✓ | ✗ | ✓ |
| a R b ⟺ a < b | ✗ | ✗ | ✓ |
| a R b ⟺ a ≤ b³ (on **R**) | ✗ | ✗ | ✗ |
| a R b ⟺ \|a − b\| is even | ✓ | ✓ | ✓ |
| a R b ⟺ (a − b) is divisible by n | ✓ | ✓ | ✓ |
| a R b ⟺ a divides b (on **N**) | ✓ | ✗ | ✓ |
| a R b ⟺ a ⊥ b (lines perpendicular) | ✗ | ✓ | ✗ |
| a R b ⟺ a ∥ b (lines parallel) | ✓ | ✓ | ✓ |
| Triangles: a R b ⟺ a is similar to b | ✓ | ✓ | ✓ |
| Triangles: a R b ⟺ a is congruent to b | ✓ | ✓ | ✓ |

**Note the two traps in that table.** "a ≤ b³" fails *reflexivity* even though "a ≤ b" satisfies it —
because at a = 1/2, a³ < a. And "perpendicular" is symmetric but **not** reflexive (no line is
perpendicular to itself) and **not** transitive (l ⊥ m and m ⊥ n makes l ∥ n, not l ⊥ n).

### Functions

A function f: A → B assigns exactly one element of B to each element of A.

| Type | Definition | How to check |
| --- | --- | --- |
| **One-one (injective)** | f(x₁) = f(x₂) ⟹ x₁ = x₂ | Set f(x₁) = f(x₂) and derive x₁ = x₂. (Equivalently: x₁ ≠ x₂ ⟹ f(x₁) ≠ f(x₂).) |
| **Onto (surjective)** | Range of f = codomain B | Take arbitrary y ∈ B, solve y = f(x) for x, and check that x lies in the domain A |
| **Bijective** | both one-one and onto | do both |

**Alternative check for one-one, when f is differentiable:** if f′(x) > 0 for all x (or f′(x) < 0 for
all x) on the domain, f is strictly monotonic and hence one-one. This is often the fastest route for
polynomial or trig functions, and is fully accepted in the marking scheme.

### Counting formulas (Section A favourites)

Let |A| = m and |B| = n.

| Quantity | Count |
| --- | --- |
| Relations from A to B | 2^(mn) |
| Relations on A (|A| = n) | 2^(n²) |
| Reflexive relations on A | 2^(n² − n) |
| Symmetric relations on A | 2^(n(n+1)/2) |
| Functions from A to B | n^m |
| One-one functions from A to B (needs m ≤ n) | n!/(n − m)! |
| Onto functions from A to B when m = n | n! |
| Bijections from A to A | n! |

If m > n there are **no** one-one functions A → B; if m < n there are **no** onto functions.

### Quick recall box

```
Reflexive   : ∀a,        (a,a) ∈ R
Symmetric   : (a,b) ∈ R  ⟹ (b,a) ∈ R
Transitive  : (a,b),(b,c) ∈ R ⟹ (a,c) ∈ R
Equivalence : all three

One-one : f(x₁) = f(x₂) ⟹ x₁ = x₂     [or f′ of one sign throughout]
Onto    : for every y ∈ codomain, ∃ x ∈ domain with f(x) = y

[a] = { x ∈ A : (a,x) ∈ R }        equivalence classes partition A

Relations on A : 2^(n²)   Reflexive : 2^(n²−n)   Symmetric : 2^(n(n+1)/2)
Functions A→B  : n^m      One-one   : n!/(n−m)!  Bijections A→A : n!
```

---

## 3. Previous years' questions

**Q1.** *(2 marks — recurs constantly, in several disguises)*
Check whether the relation R on **R** defined by R = {(a, b) : a ≤ b³} is reflexive, symmetric or
transitive.

**Q2.** *(3 marks — the standard equivalence-relation question)*
Show that the relation R on the set A = {1, 2, 3, 4, 5} given by R = {(a, b) : |a − b| is even} is an
equivalence relation. Find all elements related to 1.

**Q3.** *(5 marks — the standard bijection proof)*
Show that the function f : **R** − {−4/3} → **R** − {4/3} defined by f(x) = 4x/(3x + 4) is one-one
and onto.

**Q4.** *(3 marks)*
Let R be a relation on **N** × **N** defined by (a, b) R (c, d) if and only if ad = bc. Show that R
is an equivalence relation.

**Q5.** *(1 mark, MCQ)*
The number of equivalence relations on the set {1, 2, 3} that contain (1, 2) and (2, 1) is
(a) 1 (b) 2 (c) 3 (d) 4

**Q6.** *(5 marks)*
Show that f : **R** → **R** defined by f(x) = x/(x² + 1) is neither one-one nor onto.

**Q7.** *(2 marks)*
Check whether f : **N** → **N** given by f(x) = x² is injective and/or surjective. Justify.

**Q8.** *(1 mark)*
Let A = {1, 2, 3}. How many relations on A containing (1, 2) and (1, 3) are reflexive and symmetric
but **not** transitive?

**Q9.** *(2 marks)*
Show that the relation R on the set of all lines in a plane, defined by R = {(l₁, l₂) : l₁ ⊥ l₂}, is
symmetric but neither reflexive nor transitive.

**Q10.** *(4 marks, case-study framing)*
A school has 4 house captains, and the set of students of Class XII is A. A relation R on A is
defined by R = {(x, y) : x and y are in the same house}.
(i) Show that R is an equivalence relation.
(ii) How many equivalence classes does R have?
(iii) If instead R′ = {(x, y) : the roll number of x is less than that of y}, which of the three
properties does R′ satisfy?

---

## 4. Solutions

### Q1 — a ≤ b³ on R

**Reflexive?** We need a ≤ a³ for *every* real a. Take a = 1/2. Then a³ = 1/8, and
1/2 ≤ 1/8 is **false**. So R is **not reflexive**.

**Symmetric?** Take (1, 2): 1 ≤ 2³ = 8 ✓, so (1, 2) ∈ R. Now (2, 1): is 2 ≤ 1³ = 1? **No**.
So (2, 1) ∉ R. Hence R is **not symmetric**.

**Transitive?** Take a = 3, b = 3/2, c = 6/5.
- (3, 3/2): 3 ≤ (3/2)³ = 27/8 = 3.375 ✓
- (3/2, 6/5): 1.5 ≤ (6/5)³ = 216/125 = 1.728 ✓
- (3, 6/5): 3 ≤ 1.728? **No**

So (3, 3/2) ∈ R and (3/2, 6/5) ∈ R but (3, 6/5) ∉ R. Hence R is **not transitive**.

**R is neither reflexive, nor symmetric, nor transitive.**

> Note how every part is settled by a single well-chosen counterexample. Fractions between 0 and 1
> are what break the cube; keep that in your pocket.

### Q2 — |a − b| even, on {1,2,3,4,5}

**Reflexive:** for any a ∈ A, |a − a| = 0, which is even. So (a, a) ∈ R for all a. ✓

**Symmetric:** let (a, b) ∈ R, so |a − b| is even. Since |b − a| = |a − b|, |b − a| is also even, so
(b, a) ∈ R. ✓

**Transitive:** let (a, b) ∈ R and (b, c) ∈ R, so |a − b| and |b − c| are both even.
|a − b| even means a and b have the **same parity** (both odd or both even). Likewise b and c have
the same parity. Hence a and c have the same parity, so |a − c| is even, i.e. (a, c) ∈ R. ✓

All three hold, so **R is an equivalence relation**.

**Elements related to 1:** we need a ∈ A with |1 − a| even, i.e. a odd.

**[1] = {1, 3, 5}**

### Q3 — f(x) = 4x/(3x + 4) is bijective

**One-one.** Let f(x₁) = f(x₂) for x₁, x₂ ∈ **R** − {−4/3}.

```
      4x₁/(3x₁ + 4) = 4x₂/(3x₂ + 4)
⟹     x₁(3x₂ + 4)   = x₂(3x₁ + 4)          [cross-multiply, divide by 4]
⟹     3x₁x₂ + 4x₁   = 3x₁x₂ + 4x₂
⟹     4x₁ = 4x₂
⟹     x₁ = x₂
```

Hence f is **one-one**.

**Onto.** Let y ∈ **R** − {4/3} be arbitrary. Solve y = 4x/(3x + 4) for x:

```
      y(3x + 4) = 4x
⟹     3xy + 4y = 4x
⟹     x(3y − 4) = −4y
⟹     x = −4y/(3y − 4) = 4y/(4 − 3y)
```

This x is well defined because y ≠ 4/3 (so 4 − 3y ≠ 0).

We must also check x lies in the **domain**, i.e. x ≠ −4/3. Suppose it did:

```
      4y/(4 − 3y) = −4/3
⟹     12y = −4(4 − 3y) = −16 + 12y
⟹     0 = −16,  a contradiction
```

So x ≠ −4/3, i.e. x ∈ **R** − {−4/3}, and f(x) = y by construction.

Hence every y in the codomain has a preimage, so f is **onto**.

**f is one-one and onto, hence bijective.**

> The step most students omit is checking x ≠ −4/3. It is worth a mark, because "onto" requires the
> preimage to lie in the **stated domain** — that is exactly why the domain was punctured.

### Q4 — (a, b) R (c, d) ⟺ ad = bc on N × N

**Reflexive:** (a, b) R (a, b) requires ab = ba, which is true for all naturals. ✓

**Symmetric:** suppose (a, b) R (c, d), so ad = bc. Then cb = da (same equation rearranged), which is
exactly the condition for (c, d) R (a, b). ✓

**Transitive:** suppose (a, b) R (c, d) and (c, d) R (e, f), so

```
ad = bc    …(i)
cf = de    …(ii)
```

Multiply (i) by f and (ii) by b:

```
adf = bcf        and        bcf = bde
⟹ adf = bde
⟹ d(af) = d(be)
```

Since d ∈ **N**, d ≠ 0, so we may cancel it: **af = be**, which is the condition for (a, b) R (e, f). ✓

All three hold, so **R is an equivalence relation**.

> Doing transitivity by multiplying rather than by writing a/b = c/d avoids any division and keeps
> the argument valid — cleaner, and it also works if the question is set on **Z** × (**Z** − {0}).

### Q5 — number of equivalence relations on {1,2,3} containing (1,2) and (2,1)

An equivalence relation corresponds exactly to a partition. Since (1, 2) ∈ R, elements 1 and 2 must
be in the same class. That leaves only two possible partitions:

1. {1, 2}, {3} → R = {(1,1),(2,2),(3,3),(1,2),(2,1)}
2. {1, 2, 3} → R = A × A (the universal relation)

**Answer: (b) 2**

### Q6 — f(x) = x/(x² + 1) is neither one-one nor onto

**Not one-one.** f(2) = 2/(4 + 1) = 2/5. And f(1/2) = (1/2)/((1/4) + 1) = (1/2)/(5/4) = 2/5.

So f(2) = f(1/2) but 2 ≠ 1/2. Hence f is **not one-one**.

> In general f(x) = f(1/x) for this function — a useful thing to notice, since it hands you a
> counterexample for any x.

**Not onto.** Find the range. Let y = x/(x² + 1). Then

```
      yx² − x + y = 0
```

Case y = 0: gives x = 0, so 0 is in the range.

Case y ≠ 0: this is a quadratic in x, and x must be real, so the discriminant must be ≥ 0:

```
      (−1)² − 4(y)(y) ≥ 0
⟹     1 − 4y² ≥ 0
⟹     y² ≤ 1/4
⟹     −1/2 ≤ y ≤ 1/2
```

So the range of f is [−1/2, 1/2], which is **not** equal to the codomain **R**. Hence f is
**not onto**.

### Q7 — f : N → N, f(x) = x²

**Injective:** let f(x₁) = f(x₂), so x₁² = x₂², giving x₁ = ±x₂. Since x₁, x₂ ∈ **N** they are
positive, so x₁ = x₂. Hence f **is injective**.

**Surjective:** consider y = 2 in the codomain **N**. We would need x ∈ **N** with x² = 2, i.e.
x = √2 ∉ **N**. So 2 has no preimage, and f is **not surjective**.

*(Contrast: the same rule f(x) = x² on **R** → **R** is neither injective nor surjective, because
f(−1) = f(1) and no negative number is a square. The domain and codomain are part of the question.)*

### Q8 — reflexive and symmetric but not transitive, containing (1,2) and (1,3)

Build R from the constraints:

- Contains (1, 2) and (1, 3) — given.
- **Reflexive** forces (1, 1), (2, 2), (3, 3) ∈ R.
- **Symmetric** forces (2, 1) and (3, 1) ∈ R.

So far R must contain {(1,1),(2,2),(3,3),(1,2),(2,1),(1,3),(3,1)}.

Now, (2, 1) ∈ R and (1, 3) ∈ R. If R were transitive we would need (2, 3) ∈ R. To make R **not**
transitive we must exclude (2, 3) — and by symmetry also exclude (3, 2). Those are the only two
remaining pairs in A × A, so there is exactly one such relation:

```
R = {(1,1), (2,2), (3,3), (1,2), (2,1), (1,3), (3,1)}
```

**Answer: 1**

### Q9 — perpendicularity of lines

**Not reflexive:** a line l is not perpendicular to itself, so (l, l) ∉ R. ✗

**Symmetric:** if l₁ ⊥ l₂ then l₂ ⊥ l₁ (perpendicularity is a mutual relation). ✓

**Not transitive:** take l₁ : y = 0 (the x-axis), l₂ : x = 0 (the y-axis), l₃ : y = 5.
Then l₁ ⊥ l₂ and l₂ ⊥ l₃, but l₁ ∥ l₃, so l₁ is **not** perpendicular to l₃. ✗

Hence R is **symmetric but neither reflexive nor transitive**.

### Q10 — case study

**(i)** R = {(x, y) : x and y are in the same house}.
- *Reflexive:* every student is in the same house as themselves. ✓
- *Symmetric:* if x is in the same house as y, then y is in the same house as x. ✓
- *Transitive:* if x, y are in one house and y, z are in one house, then since y belongs to exactly
  one house, x, y, z are all in that house, so x and z are in the same house. ✓

Hence R is an **equivalence relation**.

**(ii)** The equivalence classes are exactly the houses. There are **4** equivalence classes.

**(iii)** R′ = {(x, y) : roll no. of x < roll no. of y}.
- *Reflexive:* no — a roll number is not less than itself. ✗
- *Symmetric:* no — if x's roll number is less than y's, then y's is not less than x's. ✗
- *Transitive:* yes — if a < b and b < c then a < c. ✓

So R′ is **transitive only**.

---

## 5. Test yourself

Time: 30 minutes. Answers below.

1. *(1)* The number of relations on the set {a, b, c} is
   (a) 8 (b) 64 (c) 512 (d) 9
2. *(1)* If R = {(1,1),(2,2),(1,2)} on A = {1,2}, then R is
   (a) reflexive only (b) reflexive and transitive (c) symmetric (d) an equivalence relation
3. *(1)* The number of one-one functions from a set with 3 elements to a set with 5 elements is
   (a) 125 (b) 243 (c) 60 (d) 15
4. *(2)* Check whether R = {(a, b) : a < b} on **N** is reflexive, symmetric, transitive.
5. *(2)* Show that f : **R** → **R**, f(x) = 3 − 4x is one-one and onto.
6. *(2)* Give an example of a relation on {1,2,3} that is symmetric and transitive but not reflexive.
7. *(3)* Show that the relation R on **Z** defined by R = {(a, b) : (a − b) is divisible by 5} is an
   equivalence relation. Write the equivalence class of 0.
8. *(3)* Let f : **R** → **R** be f(x) = x³ + 5. Prove f is a bijection.
9. *(3)* Check whether R = {(a, b) : a divides b} on the set {1, 2, 3, 4, 5, 6} is reflexive,
   symmetric, transitive.
10. *(5)* Show that f : **R** − {2} → **R** − {1} defined by f(x) = (x − 3)/(x − 2) is one-one and onto.
11. *(2)* Let A = {1,2,3,4}. Write the smallest equivalence relation on A containing (1, 2).
12. *(2)* If f : **R** → **R** is f(x) = x² − 4x + 5, is f one-one? Justify with a counterexample and
    state a domain restriction that makes it one-one.

### Answer key

**1. (c) 512.** |A| = 3, so relations on A number 2^(3²) = 2⁹ = 512.

**2. (b).** Reflexive ✓ (both (1,1),(2,2) present). Symmetric ✗ ((1,2) present, (2,1) absent).
Transitive ✓ (only chain is (1,1),(1,2) → (1,2) ✓).

**3. (c) 60.** 5!/(5 − 3)! = 5 × 4 × 3 = 60.

**4.** Not reflexive (a < a false). Not symmetric (1 < 2 but 2 < 1 false). Transitive ✓
(a < b, b < c ⟹ a < c).

**5.** One-one: 3 − 4x₁ = 3 − 4x₂ ⟹ x₁ = x₂. Onto: for y ∈ **R**, x = (3 − y)/4 ∈ **R** and f(x) = y.

**6.** R = {(1, 1)}. Symmetric ✓ (vacuously, and (1,1) reverses to itself), transitive ✓, but not
reflexive since (2,2), (3,3) ∉ R. *(Any R that omits at least one (a,a) but is otherwise an
equivalence relation on a subset works, e.g. {(1,1),(2,2),(1,2),(2,1)}.)*

**7.** Reflexive: a − a = 0 = 5(0), divisible by 5 ✓. Symmetric: if a − b = 5k then b − a = 5(−k) ✓.
Transitive: a − b = 5k, b − c = 5m ⟹ a − c = 5(k + m) ✓. Equivalence relation.
[0] = {…, −10, −5, 0, 5, 10, …} = all multiples of 5 = {5n : n ∈ **Z**}.

**8.** One-one: x₁³ + 5 = x₂³ + 5 ⟹ x₁³ = x₂³ ⟹ x₁ = x₂ (cube is one-one on **R**).
*(Alternatively f′(x) = 3x² ≥ 0 and = 0 only at x = 0, so f is strictly increasing.)*
Onto: for y ∈ **R**, x = (y − 5)^(1/3) ∈ **R** and f(x) = y.

**9.** Reflexive ✓ (a divides a). Symmetric ✗ (2 divides 4, but 4 does not divide 2).
Transitive ✓ (a | b and b | c ⟹ a | c).

**10.** One-one: (x₁ − 3)/(x₁ − 2) = (x₂ − 3)/(x₂ − 2) ⟹ (x₁ − 3)(x₂ − 2) = (x₂ − 3)(x₁ − 2)
⟹ x₁x₂ − 2x₁ − 3x₂ + 6 = x₁x₂ − 2x₂ − 3x₁ + 6 ⟹ x₁ = x₂.
Onto: y = (x − 3)/(x − 2) ⟹ y(x − 2) = x − 3 ⟹ x(y − 1) = 2y − 3 ⟹ x = (2y − 3)/(y − 1), defined
since y ≠ 1. Check x ≠ 2: (2y − 3)/(y − 1) = 2 ⟹ 2y − 3 = 2y − 2 ⟹ −3 = −2, contradiction. So x is
in the domain and f is onto.

**11.** R = {(1,1),(2,2),(3,3),(4,4),(1,2),(2,1)}. *(Reflexivity forces the four diagonal pairs;
symmetry forces (2,1); nothing more is needed for transitivity.)*

**12.** Not one-one: f(1) = 1 − 4 + 5 = 2 and f(3) = 9 − 12 + 5 = 2, but 1 ≠ 3.
f(x) = (x − 2)² + 1, so restricting the domain to [2, ∞) (or to (−∞, 2]) makes it one-one.

**Scoring.** Out of 27. Below 19 → re-read §2, particularly the prove-vs-disprove asymmetry, and
redo Q1–Q4 of §3.

---

## 6. Answering tips

**On relations**

1. **Answer all three properties, separately and labelled**, even if the question only names one.
   The marking scheme has a mark per property. Write "Reflexive:", "Symmetric:", "Transitive:" as
   headings.

2. **To disprove, give the actual numbers.** "R is not symmetric because a R b does not imply b R a"
   scores **zero**. "Take (1,2) ∈ R since 1 ≤ 8; but (2,1) ∉ R since 2 > 1. So not symmetric" scores
   full. The counterexample *is* the answer.

3. **To prove, use a general element.** Start "Let a ∈ A be arbitrary…" or "Let (a,b) ∈ R…". Never
   verify with specific numbers when proving.

4. **For transitivity, name the pairs.** Write "Let (a,b) ∈ R and (b,c) ∈ R" explicitly before
   deriving. Examiners look for that line.

5. **Conclude explicitly.** End with "Hence R is an equivalence relation." A proof without a
   conclusion loses the last ½ mark.

6. **For equivalence classes**, list the elements in braces, and check your classes partition the set
   (disjoint, and covering everything). If your classes overlap, you have made an error.

**On one-one / onto**

7. **One-one: start from f(x₁) = f(x₂), end at x₁ = x₂.** That direction, not the reverse. If you
   prefer the derivative route, you must state "f′(x) > 0 for all x in the domain, hence f is
   strictly increasing and therefore one-one" — the conclusion sentence is required.

8. **Onto: you must produce x explicitly and check it is in the domain.** Two things, both marked.
   When the domain is punctured (like **R** − {−4/3}), the check that x avoids the removed point is a
   separate mark — it is the reason the point was removed.

9. **Do not confuse range and codomain.** "Onto" means range = codomain. To disprove onto, name a
   specific element of the codomain with no preimage.

10. **State the final verdict in words.** "Hence f is one-one and onto, i.e. bijective."

**On MCQs**

11. For counting questions, write the formula in the margin before computing — 2^(n²) for relations,
    n^m for functions, n!/(n−m)! for one-one. Getting these confused is the whole error mode here.

12. For "which properties does R satisfy" MCQs, test reflexivity first — it is the fastest to
    disprove, and it eliminates "equivalence relation" options immediately.
