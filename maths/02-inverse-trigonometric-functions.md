# Ch 2 — Inverse Trigonometric Functions

**Unit I (8 marks, shared with Ch 1) · Typical appearance: one or two 1-mark MCQs, occasionally a
2-mark evaluation. Rarely more.**

---

## 1. Scope

### In the syllabus

- **Definition, domain, range** of the six inverse trigonometric functions
- **Principal value branches**

That is all. This is now the smallest chapter in the book.

### Deleted — do not study

- **Graphs** of inverse trigonometric functions
- **Elementary properties** — the identity set: sin⁻¹x + cos⁻¹x = π/2, tan⁻¹x + tan⁻¹y = tan⁻¹((x+y)/(1−xy)),
  2 tan⁻¹x = tan⁻¹(2x/(1−x²)) = sin⁻¹(2x/(1+x²)), and the rest

> **Read this carefully.** Almost everything students think of as "the inverse trig chapter" — the
> long identity-chaining problems — is deleted. Do not spend a week here. Spend two days, learn the
> six domain–range pairs cold, and move to Calculus.
>
> One caveat: the complementary identity **sin⁻¹x + cos⁻¹x = π/2** is one line, occasionally still
> turns up in an MCQ as a shortcut, and costs nothing to remember. Know it. Don't study the rest.

---

## 2. Brief

### Why inverse trig functions need restricted ranges

sin x is not one-one on **R** — sin 0 = sin π = sin 2π = 0 — so it has no inverse on **R**. To invert
it we restrict the domain to an interval where it *is* one-one and where it still attains every
value in [−1, 1]. For sine, the standard choice is [−π/2, π/2]. That restricted inverse is what
sin⁻¹ means, and its output is called the **principal value**.

Every question in this chapter is, at bottom, a question about which interval the answer must lie in.

### The table to memorise

| Function | Domain (input) | Range = principal value branch (output) |
| --- | --- | --- |
| sin⁻¹x | [−1, 1] | [−π/2, π/2] |
| cos⁻¹x | [−1, 1] | [0, π] |
| tan⁻¹x | **R** | (−π/2, π/2) |
| cot⁻¹x | **R** | (0, π) |
| sec⁻¹x | **R** − (−1, 1), i.e. \|x\| ≥ 1 | [0, π] − {π/2} |
| cosec⁻¹x | **R** − (−1, 1), i.e. \|x\| ≥ 1 | [−π/2, π/2] − {0} |

**Learn it as two families, not six rows:**

- **sin⁻¹, tan⁻¹, cosec⁻¹** → range centred on 0, i.e. **[−π/2, π/2]** (open for tan⁻¹, with 0
  removed for cosec⁻¹). These give **negative** answers for negative inputs.
- **cos⁻¹, cot⁻¹, sec⁻¹** → range **[0, π]** (open for cot⁻¹, with π/2 removed for sec⁻¹). These are
  **never negative**; for a negative input they give an obtuse angle.

That one distinction answers most MCQs in this chapter without any computation.

Note also: sec⁻¹ and cosec⁻¹ are **not defined** for −1 < x < 1. So sec⁻¹(1/2) does not exist. This
appears as an MCQ.

### Negative arguments

| | |
| --- | --- |
| sin⁻¹(−x) = −sin⁻¹x | cos⁻¹(−x) = **π −** cos⁻¹x |
| tan⁻¹(−x) = −tan⁻¹x | cot⁻¹(−x) = **π −** cot⁻¹x |
| cosec⁻¹(−x) = −cosec⁻¹x | sec⁻¹(−x) = **π −** sec⁻¹x |

Same split as above: the "centred on 0" family flips sign; the "[0, π]" family subtracts from π.

### Standard values worth having instantly

| x | sin⁻¹x | cos⁻¹x | tan⁻¹x |
| --- | --- | --- | --- |
| 0 | 0 | π/2 | 0 |
| 1/2 | π/6 | π/3 | — |
| 1/√2 | π/4 | π/4 | — |
| √3/2 | π/3 | π/6 | — |
| 1 | π/2 | 0 | π/4 |
| 1/√3 | — | — | π/6 |
| √3 | — | — | π/3 |

And: cot⁻¹(1) = π/4, cot⁻¹(√3) = π/6, cot⁻¹(1/√3) = π/3, sec⁻¹(2) = π/3, sec⁻¹(√2) = π/4,
cosec⁻¹(2) = π/6, cosec⁻¹(√2) = π/4.

### The one question type that carries this chapter

**sin⁻¹(sin θ), cos⁻¹(cos θ), tan⁻¹(tan θ) where θ is outside the principal branch.**

The naive answer "they cancel, so it's θ" is right **only** when θ already lies in the range of the
inverse function. Otherwise you must reduce.

```
sin⁻¹(sin θ) = θ   only if  θ ∈ [−π/2, π/2]
cos⁻¹(cos θ) = θ   only if  θ ∈ [0, π]
tan⁻¹(tan θ) = θ   only if  θ ∈ (−π/2, π/2)
```

**The method — three steps, always:**

1. **Check** whether θ is in the required interval. If yes, the answer is θ. Done.
2. If no, **evaluate the inner function** to get a plain number, using the usual trig
   reduction (sin(π − θ) = sin θ, cos(2π − θ) = cos θ, etc.).
3. **Take the inverse of that number**, and give the answer in the correct branch.

Worked instantly: sin⁻¹(sin(3π/4)). Is 3π/4 ∈ [−π/2, π/2]? No. So sin(3π/4) = sin(π − π/4)
= sin(π/4) = 1/√2, and sin⁻¹(1/√2) = **π/4**.

**Faster, once you trust it — the shortcut identities:**

```
sin⁻¹(sin θ) = π − θ      for θ ∈ [π/2, 3π/2]
cos⁻¹(cos θ) = 2π − θ     for θ ∈ [π, 2π]
tan⁻¹(tan θ) = θ − π      for θ ∈ (π/2, 3π/2)
```

And for θ beyond 2π, first subtract multiples of 2π. Use these only after you can do the three-step
method reliably — if you misremember the shortcut you get no marks and no way to check.

### Composites like sin(cos⁻¹x)

Set the inverse equal to an angle and use a right triangle.

To find sin(cos⁻¹(3/5)): let θ = cos⁻¹(3/5), so cos θ = 3/5 with θ ∈ [0, π]. In that range
sin θ ≥ 0, so sin θ = +√(1 − 9/25) = 4/5. Answer **4/5**.

The sign decision comes from the **range** of the inverse function — that is the whole subtlety, and
it is where the mark is.

Standard results worth recognising:

```
sin(cos⁻¹x) = √(1 − x²)        cos(sin⁻¹x) = √(1 − x²)
tan(sin⁻¹x) = x/√(1 − x²)      sec(tan⁻¹x) = √(1 + x²)
```

### Finding a domain

To find the domain of an expression like sin⁻¹(f(x)), impose −1 ≤ f(x) ≤ 1 and solve.

For sin⁻¹(2x − 1): −1 ≤ 2x − 1 ≤ 1 ⟹ 0 ≤ 2x ≤ 2 ⟹ **x ∈ [0, 1]**.

### Quick recall box

```
                DOMAIN            RANGE (principal branch)
sin⁻¹ x        [−1, 1]           [−π/2, π/2]
cos⁻¹ x        [−1, 1]           [0, π]
tan⁻¹ x        R                 (−π/2, π/2)
cot⁻¹ x        R                 (0, π)
sec⁻¹ x        |x| ≥ 1           [0, π] − {π/2}
cosec⁻¹ x      |x| ≥ 1           [−π/2, π/2] − {0}

Family A (sin⁻¹, tan⁻¹, cosec⁻¹): range around 0;  f(−x) = −f(x)
Family B (cos⁻¹, cot⁻¹, sec⁻¹) : range [0, π];      f(−x) = π − f(x)

sin⁻¹(sin θ) = θ  ONLY if θ ∈ [−π/2, π/2]      else reduce
cos⁻¹(cos θ) = θ  ONLY if θ ∈ [0, π]           else reduce
tan⁻¹(tan θ) = θ  ONLY if θ ∈ (−π/2, π/2)      else reduce

sin⁻¹x + cos⁻¹x = π/2      (one line, worth knowing)
```

---

## 3. Previous years' questions

**Q1.** *(1 mark)* Write the principal value of sin⁻¹(−1/2).

**Q2.** *(1 mark)* Find the principal value of cos⁻¹(−1/2).

**Q3.** *(2 marks)* Find the value of tan⁻¹(√3) − cot⁻¹(−√3).

**Q4.** *(2 marks)* Evaluate sin⁻¹(sin(3π/4)).

**Q5.** *(2 marks)* Evaluate cos⁻¹(cos(7π/6)).

**Q6.** *(1 mark)* Find the value of tan⁻¹(tan(3π/4)).

**Q7.** *(2 marks)* Find the value of sin(cos⁻¹(3/5)).

**Q8.** *(2 marks)* Find the domain of sin⁻¹(2x − 1).

**Q9.** *(1 mark)* The principal value branch of sec⁻¹x is
(a) [−π/2, π/2] (b) [0, π] − {π/2} (c) (0, π) (d) [−π/2, π/2] − {0}

**Q10.** *(2 marks)* Evaluate cos⁻¹(cos(13π/6)).

**Q11.** *(1 mark)* The value of sec⁻¹(−2) is
(a) −π/3 (b) π/3 (c) 2π/3 (d) not defined

**Q12.** *(2 marks)* Find the value of sin⁻¹(1/2) + cos⁻¹(1/2) + tan⁻¹(1).

**Q13.** *(1 mark, Assertion–Reason)*
**Assertion (A):** sin⁻¹(sin(2π/3)) = 2π/3.
**Reason (R):** sin⁻¹(sin x) = x for all x ∈ **R**.

---

## 4. Solutions

### Q1 — sin⁻¹(−1/2)

Let sin⁻¹(−1/2) = θ, so sin θ = −1/2 with θ ∈ [−π/2, π/2].

Since sin(π/6) = 1/2, we have sin(−π/6) = −1/2, and −π/6 ∈ [−π/2, π/2]. ✓

**sin⁻¹(−1/2) = −π/6**

### Q2 — cos⁻¹(−1/2)

cos⁻¹ has range [0, π], so the answer must be in [0, π] — it cannot be negative.

Using cos⁻¹(−x) = π − cos⁻¹x:

```
cos⁻¹(−1/2) = π − cos⁻¹(1/2) = π − π/3 = 2π/3
```

Check: 2π/3 ∈ [0, π] ✓ and cos(2π/3) = −1/2 ✓.

**cos⁻¹(−1/2) = 2π/3**

> The commonest wrong answer here is −π/3. cos⁻¹ is **never negative**.

### Q3 — tan⁻¹(√3) − cot⁻¹(−√3)

```
tan⁻¹(√3) = π/3            since tan(π/3) = √3 and π/3 ∈ (−π/2, π/2)

cot⁻¹(−√3) = π − cot⁻¹(√3)  [Family B rule]
           = π − π/6
           = 5π/6           and 5π/6 ∈ (0, π) ✓
```

Therefore

```
tan⁻¹(√3) − cot⁻¹(−√3) = π/3 − 5π/6 = 2π/6 − 5π/6 = −3π/6 = −π/2
```

**Answer: −π/2**

### Q4 — sin⁻¹(sin(3π/4))

**Step 1.** Is 3π/4 in [−π/2, π/2]? 3π/4 = 135°, and π/2 = 90°. **No.** So the answer is not 3π/4.

**Step 2.** Evaluate the inside:

```
sin(3π/4) = sin(π − π/4) = sin(π/4) = 1/√2
```

**Step 3.** Take the inverse:

```
sin⁻¹(1/√2) = π/4        and π/4 ∈ [−π/2, π/2] ✓
```

**Answer: π/4**

### Q5 — cos⁻¹(cos(7π/6))

**Step 1.** Is 7π/6 in [0, π]? 7π/6 = 210° > 180°. **No.**

**Step 2.**

```
cos(7π/6) = cos(π + π/6) = −cos(π/6) = −√3/2
```

**Step 3.**

```
cos⁻¹(−√3/2) = π − cos⁻¹(√3/2) = π − π/6 = 5π/6      and 5π/6 ∈ [0, π] ✓
```

**Answer: 5π/6**

*(Shortcut check: for θ ∈ [π, 2π], cos⁻¹(cos θ) = 2π − θ = 2π − 7π/6 = 5π/6 ✓)*

### Q6 — tan⁻¹(tan(3π/4))

**Step 1.** Is 3π/4 in (−π/2, π/2)? No.

**Step 2.** tan(3π/4) = tan(π − π/4) = −tan(π/4) = −1.

**Step 3.** tan⁻¹(−1) = −π/4, and −π/4 ∈ (−π/2, π/2) ✓

**Answer: −π/4**

### Q7 — sin(cos⁻¹(3/5))

Let θ = cos⁻¹(3/5). Then cos θ = 3/5 and **θ ∈ [0, π]**.

```
sin²θ = 1 − cos²θ = 1 − 9/25 = 16/25
⟹ sin θ = ± 4/5
```

Since θ ∈ [0, π], sin θ ≥ 0. So we take the **positive** root.

**sin(cos⁻¹(3/5)) = 4/5**

> The line "θ ∈ [0, π], so sin θ ≥ 0" is the mark. Without it you have not justified the sign.

### Q8 — domain of sin⁻¹(2x − 1)

sin⁻¹ requires its argument to lie in [−1, 1]:

```
      −1 ≤ 2x − 1 ≤ 1
⟹     0 ≤ 2x ≤ 2
⟹     0 ≤ x ≤ 1
```

**Domain = [0, 1]**

### Q9 — principal value branch of sec⁻¹

**Answer: (b) [0, π] − {π/2}**

π/2 is excluded because sec(π/2) is undefined.

### Q10 — cos⁻¹(cos(13π/6))

13π/6 > 2π? 2π = 12π/6, so 13π/6 = 2π + π/6. Reduce by 2π first:

```
cos(13π/6) = cos(2π + π/6) = cos(π/6) = √3/2
```

Then

```
cos⁻¹(√3/2) = π/6        and π/6 ∈ [0, π] ✓
```

**Answer: π/6**

### Q11 — sec⁻¹(−2)

|−2| ≥ 1, so it is defined. Range is [0, π] − {π/2}, so the answer is non-negative.

```
sec⁻¹(−2) = π − sec⁻¹(2) = π − π/3 = 2π/3
```

**Answer: (c) 2π/3**

*(Option (a) −π/3 is the trap: sec⁻¹ is never negative.)*

### Q12 — sin⁻¹(1/2) + cos⁻¹(1/2) + tan⁻¹(1)

```
sin⁻¹(1/2) = π/6
cos⁻¹(1/2) = π/3
tan⁻¹(1)   = π/4
```

Sum = π/6 + π/3 + π/4 = 2π/12 + 4π/12 + 3π/12 = **9π/12 = 3π/4**

*(Or note sin⁻¹(1/2) + cos⁻¹(1/2) = π/2 directly, then + π/4 = 3π/4.)*

### Q13 — Assertion–Reason

**Assertion:** sin⁻¹(sin(2π/3)). Is 2π/3 ∈ [−π/2, π/2]? 2π/3 = 120° > 90°, so **no**.
sin(2π/3) = sin(π/3) = √3/2, and sin⁻¹(√3/2) = π/3, **not** 2π/3.
So **A is false**.

**Reason:** "sin⁻¹(sin x) = x for all x ∈ **R**" is **false** — it holds only for x ∈ [−π/2, π/2].
So **R is false**.

Both false. On the standard four-option set (a)–(d), neither (c) "A true, R false" nor (d) "A false,
R true" fits; the correct response is that **both A and R are false**, which in papers using that
fifth option is (e), and in papers using only four options means the question expects you to notice
A is false — check the option list on your paper.

**Answer: A is false and R is false.**

---

## 5. Test yourself

Time: 20 minutes. Answers below.

1. *(1)* The principal value of tan⁻¹(−1) is
   (a) 3π/4 (b) −π/4 (c) π/4 (d) −3π/4
2. *(1)* The range of cot⁻¹x is
   (a) [0, π] (b) (0, π) (c) [−π/2, π/2] (d) **R**
3. *(1)* cosec⁻¹(1/2) is
   (a) π/6 (b) 2 (c) π/3 (d) not defined
4. *(2)* Find sin⁻¹(sin(5π/6)).
5. *(2)* Find cos⁻¹(cos(4π/3)).
6. *(2)* Find tan⁻¹(tan(7π/6)).
7. *(2)* Evaluate cos(sin⁻¹(5/13)).
8. *(2)* Find the domain of cos⁻¹(3x + 1).
9. *(2)* Evaluate cot⁻¹(−1) + sec⁻¹(√2).
10. *(2)* Find the value of tan(sin⁻¹(3/5) ) .
11. *(1)* sin⁻¹x + cos⁻¹x equals
    (a) 0 (b) π (c) π/2 (d) 1
12. *(2)* Find sin⁻¹(sin(−2π/3)).

### Answer key

**1. (b) −π/4.** tan(−π/4) = −1, and −π/4 ∈ (−π/2, π/2).

**2. (b) (0, π).** Open at both ends.

**3. (d) not defined.** cosec⁻¹ requires |x| ≥ 1, and |1/2| < 1.

**4. π/6.** 5π/6 ∉ [−π/2, π/2]. sin(5π/6) = sin(π − π/6) = sin(π/6) = 1/2, so sin⁻¹(1/2) = π/6.

**5. 2π/3.** 4π/3 ∉ [0, π]. cos(4π/3) = cos(π + π/3) = −cos(π/3) = −1/2.
cos⁻¹(−1/2) = π − π/3 = 2π/3.

**6. π/6.** 7π/6 ∉ (−π/2, π/2). tan(7π/6) = tan(π + π/6) = tan(π/6) = 1/√3.
tan⁻¹(1/√3) = π/6. *(Shortcut: θ − π = 7π/6 − π = π/6 ✓)*

**7. 12/13.** Let θ = sin⁻¹(5/13), so sin θ = 5/13 with θ ∈ [−π/2, π/2], where cos θ ≥ 0.
cos θ = +√(1 − 25/169) = 12/13.

**8. [−2/3, 0].** Need −1 ≤ 3x + 1 ≤ 1 ⟹ −2 ≤ 3x ≤ 0 ⟹ −2/3 ≤ x ≤ 0.

**9. π.** cot⁻¹(−1) = π − cot⁻¹(1) = π − π/4 = 3π/4. sec⁻¹(√2) = π/4. Sum = 3π/4 + π/4 = π.

**10. 3/4.** θ = sin⁻¹(3/5) ⟹ sin θ = 3/5, θ ∈ [−π/2, π/2] so cos θ = 4/5 > 0, tan θ = 3/4.

**11. (c) π/2.**

**12. −π/3.** −2π/3 ∉ [−π/2, π/2]. sin(−2π/3) = −sin(2π/3) = −sin(π/3) = −√3/2.
sin⁻¹(−√3/2) = −π/3. *(Sanity check: the answer must be in [−π/2, π/2], and −π/3 is.)*

**Scoring.** Out of 20. Below 15 → the problem is almost certainly the domain–range table. Write it
out from memory five times, then redo.

---

## 6. Answering tips

1. **Every answer in this chapter must be checked against the range.** Before you write the final
   value, ask: "is this in the principal branch?" If cos⁻¹ gave you a negative answer, or sin⁻¹ gave
   you something above π/2, you have made an error. This one check catches almost every mistake
   available here.

2. **cos⁻¹, cot⁻¹ and sec⁻¹ are never negative.** If an MCQ offers a negative option for one of
   these, eliminate it immediately. This single fact resolves a surprising number of 1-markers in
   under five seconds.

3. **Never write sin⁻¹(sin θ) = θ without checking θ.** This is the most-tested trap in the chapter,
   and it is tested *because* students do it automatically.

4. **Show the two-line method even on 1-mark questions.** "sin(3π/4) = 1/√2, so sin⁻¹(1/√2) = π/4"
   is two lines and protects the mark if you slip. For 2-mark questions the two lines *are* the two
   marks.

5. **Answers in radians, in terms of π.** Not degrees, unless the question used degrees. Write π/4,
   not 0.785 or 45°.

6. **State the range you are using when justifying a sign.** For composites like sin(cos⁻¹x), the
   sentence "since θ ∈ [0, π], sin θ ≥ 0" is a mark on its own. Write it.

7. **For "not defined" options, check the domain first.** sec⁻¹ and cosec⁻¹ of anything strictly
   between −1 and 1 does not exist. CBSE sets this MCQ regularly and it is free.

8. **Don't over-invest.** This chapter is worth roughly 1–3 marks in a typical paper and has almost
   no derivation content left. Two solid days, then leave it and revisit only in the formula-sheet
   rounds.
