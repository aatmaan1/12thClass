# Ch 13 — Probability

**Unit VI (8 marks) · Typical appearance: one Bayes' theorem question worth 4–5 marks (essentially
guaranteed) + one 2/3-mark conditional-probability question + an MCQ.**

---

## 1. Scope

### In the syllabus

- **Conditional probability**
- **Multiplication theorem** on probability
- **Independent events**
- **Theorem of total probability**
- **Bayes' theorem**
- **Random variable** and its **probability distribution**
- **Mean** of a random variable

### Deleted — do not study

- **Variance** and standard deviation of a random variable
- **Bernoulli trials** and the **Binomial distribution** (no ⁿCᵣ pᵣ qⁿ⁻ᵣ)

> **This is the deletion students miss most often.** The Binomial distribution used to be a
> guaranteed question — "find the probability of exactly 3 heads in 5 tosses" — and it is now out of
> syllabus, along with variance. Almost every second-hand note and old question bank still features
> both prominently. The entire 8 marks now comes from the conditional-probability family plus the
> mean of a random variable.

---

## 2. Brief

### Start here — in plain English

Most of this chapter is about one idea, and it is an idea that human intuition gets wrong almost
every time: **how new information should change what you believe.**

Here is the standard illustration, and it is worth sitting with. A disease affects 1 person in 1000.
A test for it is 99% accurate. You test positive. What is the chance you have the disease? Almost
everyone says 99%. The right answer is about 9%. Out of 1000 people, one has the disease and tests
positive; of the 999 healthy ones, 1% — about ten people — test positive anyway. So eleven people
test positive and only one is ill. The test is good; the disease is just rare, and rarity dominates.

That calculation is **Bayes' theorem**, and the chapter builds up to it.

**Conditional probability** is the foundation: P(A|B), read "the probability of A *given* B", is the
probability of A once you know B has happened. Knowing B shrinks the world to just those outcomes
where B is true, so you count A's share of that smaller world: P(A|B) = P(A∩B)/P(B). Drawing a card
and being told it is a face card changes the odds it is a king from 4/52 to 4/12. Nothing has
changed about the card; what changed is what you know.

**Independence** is the special case where the news is useless. A and B are independent if learning
B tells you nothing about A, so P(A|B) = P(A), which rearranges into the test you will use:
**P(A∩B) = P(A)·P(B)**. Two coin tosses are independent. Two cards drawn without replacement are
not, because the first draw changes what is left in the deck. Watch for the phrase "with
replacement" or "without" — it decides the whole question.

The **multiplication theorem** is that same relation used forwards, and the **total probability**
rule is how you handle a situation that could have arisen by several routes: if a ball could have
come from bag A or bag B, the overall chance of it being red is the chance of each bag times the
chance of red from that bag, added up. Then **Bayes' theorem** runs that argument *backwards* —
given the ball is red, which bag did it probably come from? That reversal is the chapter's flagship
5-mark question, and it always arrives dressed as a story: two machines and a defective item, three
bags and a coloured ball, two doctors and a diagnosis. The wording changes; the structure never does.

There is a mechanical way to get these right that is worth adopting: **draw the tree**. Branches for
the possible sources with their prior probabilities, then branches for the observed outcome with its
conditional probabilities, and multiply along each path. Bayes' theorem is then just "the path I care
about, divided by all the paths that produce the observation". Students who draw the tree get these
right; students who reach for the formula mix up which probability is conditioned on which.

The last piece is the **random variable** and its **mean**. A random variable attaches a number to
each outcome — the number of heads in three tosses, say — and its probability distribution lists the
values with their probabilities. The mean, or expectation, is Σx·P(x): each value weighted by how
likely it is. It is the long-run average, and it need not be a value the variable can actually take —
the expected number of heads in three tosses is 1.5. Two checks before you go further: every
probability must be between 0 and 1, and they must sum to exactly 1. If your distribution table
fails either test, stop and find the error.

Note the scope: the binomial distribution and variance have been trimmed in the rationalised
syllabus. Check §1 of this chapter before studying them.

**Learn it from someone else too**

- **Video lecture** — [search: probability class 12 one shot Bayes theorem](https://www.youtube.com/results?search_query=probability+class+12+maths+one+shot+bayes+theorem)
- **Why Bayes' theorem is unintuitive** — [search: Bayes theorem 3Blue1Brown](https://www.youtube.com/results?search_query=bayes+theorem+3blue1brown).
  The clearest visual explanation available, and it makes the disease example obvious.
- **Interactive lessons and practice** — [Khan Academy: conditional probability and Bayes](https://www.khanacademy.org/math/statistics-probability/probability-library)
- **The book the paper is set from** — [NCERT Maths Part II, Chapter 13 (PDF)](https://ncert.nic.in/textbook/pdf/lemh207.pdf)
- **For extra problems** — NCERT exercises, then Exemplar Chapter 13. Do at least ten full Bayes
  word problems with trees drawn; it is the highest-value single question type in the paper.

---

### Conditional probability

The probability of A **given that** B has already occurred:

```
      P(A|B) = P(A ∩ B) / P(B)              provided P(B) ≠ 0
```

Read it as: restrict the sample space to B, and ask what fraction of B is also A.

**Properties:**

```
      P(S|B) = P(B|B) = 1
      P(A′|B) = 1 − P(A|B)
      P((A ∪ C)|B) = P(A|B) + P(C|B) − P((A ∩ C)|B)
```

> **The one thing to keep straight:** P(A|B) and P(B|A) are different numbers. The **denominator is
> whatever is given**. "Given it is defective, find the probability it came from machine C" has
> "defective" in the denominator.

### Multiplication theorem

Rearranging the definition:

```
      P(A ∩ B) = P(B) · P(A|B) = P(A) · P(B|A)
```

For three events:

```
      P(A ∩ B ∩ C) = P(A) · P(B|A) · P(C|A ∩ B)
```

This is what you use for "drawing without replacement": the probability changes at each draw, and
you multiply the conditional probabilities.

### Independent events

A and B are **independent** if the occurrence of one does not affect the other:

```
      P(A ∩ B) = P(A) · P(B)
```

Equivalently, P(A|B) = P(A) and P(B|A) = P(B).

**If A and B are independent, so are:** A′ and B, A and B′, A′ and B′.

**Independent ≠ mutually exclusive.** These are completely different ideas and the distinction is
examined:

| | Mutually exclusive | Independent |
| --- | --- | --- |
| Definition | A ∩ B = ∅, so P(A ∩ B) = 0 | P(A ∩ B) = P(A)P(B) |
| Meaning | they cannot both happen | one happening tells you nothing about the other |
| Can both hold? | Only if P(A) = 0 or P(B) = 0 | |

So two events with non-zero probabilities that are mutually exclusive are **necessarily dependent** —
if you know A happened, you know B did not. That is the standard MCQ.

**Useful:** for independent A, B:

```
      P(A ∪ B) = P(A) + P(B) − P(A)P(B)
      P(neither) = P(A′ ∩ B′) = (1 − P(A))(1 − P(B))
      P(at least one) = 1 − P(neither)
```

### Theorem of total probability

Let E₁, E₂, …, Eₙ be a **partition** of the sample space (mutually exclusive, exhaustive, each with
non-zero probability). Then for any event A:

```
      P(A) = P(E₁)P(A|E₁) + P(E₂)P(A|E₂) + … + P(Eₙ)P(A|Eₙ)
           = Σ P(Eᵢ) P(A|Eᵢ)
```

In words: to find the overall probability of A, go through each way the world could be, and weight
the conditional probability by how likely that way is.

### Bayes' theorem

Same setup. Then

```
                  P(Eᵢ) · P(A|Eᵢ)
      P(Eᵢ|A) = ─────────────────────────
                  Σⱼ P(Eⱼ) · P(A|Eⱼ)
```

The denominator is exactly P(A) from the total probability theorem. So Bayes' theorem is:

```
      P(Eᵢ|A) = (that one term) / (sum of all the terms)
```

**Vocabulary that appears in questions:** P(Eᵢ) are the **prior** probabilities (before you observe
A); P(Eᵢ|A) are the **posterior** probabilities (after).

### The Bayes layout — use it every time

The reason students lose this question is disorganisation, not ignorance. Impose this structure:

**Step 1 — Define the events**, with letters.

```
      E₁ : the item came from machine A
      E₂ : the item came from machine B
      E₃ : the item came from machine C
      D  : the item is defective
```

**Step 2 — Write all the priors** P(E₁), P(E₂), P(E₃).

**Step 3 — Write all the likelihoods** P(D|E₁), P(D|E₂), P(D|E₃).

**Step 4 — Write the formula** with the required index.

**Step 5 — Substitute and simplify.**

Laid out this way it is structurally impossible to invert the conditional or to drop a term from the
denominator — the two ways this question is actually lost.

### Random variables

A **random variable** X is a real-valued function on the sample space of a random experiment.

Its **probability distribution** is the table of values and their probabilities:

| X = xᵢ | x₁ | x₂ | … | xₙ |
| --- | --- | --- | --- | --- |
| P(X = xᵢ) = pᵢ | p₁ | p₂ | … | pₙ |

**The two conditions** every probability distribution must satisfy:

```
      pᵢ ≥ 0 for all i          and          Σ pᵢ = 1
```

Checking Σpᵢ = 1 is both a mark and your own error check. Do it.

**Mean (expectation):**

```
      Mean = E(X) = μ = Σ xᵢ pᵢ
```

The mean is also called the **expected value** or the **expectation** of X.

> Variance is deleted, so you will not be asked for Σxᵢ²pᵢ − μ². If a practice question asks for it,
> it is from an old paper.

### Quick recall box

```
CONDITIONAL:  P(A|B) = P(A∩B)/P(B),  P(B) ≠ 0        ← "given" goes in the DENOMINATOR
              P(A′|B) = 1 − P(A|B)

MULTIPLICATION: P(A∩B) = P(A)P(B|A) = P(B)P(A|B)
                P(A∩B∩C) = P(A)P(B|A)P(C|A∩B)

INDEPENDENT: P(A∩B) = P(A)P(B)  ⟺  P(A|B) = P(A)
             P(at least one) = 1 − (1−P(A))(1−P(B))
             independent ≠ mutually exclusive

TOTAL PROBABILITY:  P(A) = Σ P(Eᵢ) P(A|Eᵢ)

BAYES:  P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ) / Σⱼ P(Eⱼ)P(A|Eⱼ)
        LAYOUT: define events → all priors → all likelihoods → formula → substitute

RANDOM VARIABLE: Σpᵢ = 1 ;  Mean = E(X) = Σ xᵢpᵢ
```

---

## 3. Previous years' questions

**Q1.** *(4 marks — the archetypal Bayes question)*
Bag I contains 3 red and 4 black balls; Bag II contains 5 red and 6 black balls. One ball is drawn
at random from one of the bags, and it is found to be red. Find the probability that it was drawn
from Bag II.

**Q2.** *(5 marks)* A factory has three machines A, B and C, producing 25%, 35% and 40% of the total
output respectively. Of their outputs, 5%, 4% and 2% are defective. An item is drawn at random from
the total output and found to be defective. Find the probability that it was produced by machine C.

**Q3.** *(3 marks)* A die is thrown twice and the sum of the numbers appearing is observed to be 6.
What is the conditional probability that the number 4 has appeared at least once?

**Q4.** *(2 marks)* A and B are independent events with P(A) = 0.3 and P(B) = 0.4. Find P(A ∪ B).

**Q5.** *(4 marks)* Two cards are drawn successively **with replacement** from a well-shuffled deck
of 52 cards. Find the probability distribution of the number of aces, and hence find its mean.

**Q6.** *(3 marks)* An urn contains 5 red and 5 black balls. A ball is drawn at random, its colour
is noted, and it is returned to the urn. Moreover, 2 additional balls of the colour drawn are put
into the urn, and then a ball is drawn at random. What is the probability that the second ball is
red?

**Q7.** *(2 marks)* If P(A) = 6/11, P(B) = 5/11 and P(A ∪ B) = 7/11, find P(A|B).

**Q8.** *(1 mark, MCQ)* If A and B are two events such that P(A) ≠ 0 and P(B|A) = 1, then
(a) A ⊂ B (b) B ⊂ A (c) B = ∅ (d) A = ∅

**Q9.** *(3 marks)* Three cards are drawn successively **without replacement** from a pack of 52
cards. Find the probability that all three are kings.

**Q10.** *(4 marks, case study)* In a school, 40% of the students are girls and 60% are boys. It is
known that 5% of the girls and 8% of the boys are left-handed.
(i) Find the probability that a randomly chosen student is left-handed.
(ii) Given that a randomly chosen student is left-handed, find the probability that the student is a
girl.
(iii) State which theorem you used in each part.

**Q11.** *(2 marks)* A random variable X has the following probability distribution. Find k, and
then the mean of X.

| X | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| P(X) | k | 2k | 3k | 4k |

**Q12.** *(1 mark, Assertion–Reason)*
**A:** If two events are mutually exclusive with non-zero probabilities, they cannot be independent.
**R:** For mutually exclusive events, P(A ∩ B) = 0.

---

## 4. Solutions

### Q1 — two bags, red ball drawn, which bag?

**Step 1 — define events.**

```
      E₁ : the ball is drawn from Bag I
      E₂ : the ball is drawn from Bag II
      R  : the ball drawn is red
```

**Step 2 — priors.** One of the two bags is chosen at random, so

```
      P(E₁) = 1/2          P(E₂) = 1/2
```

**Step 3 — likelihoods.**

```
      Bag I  : 3 red out of (3 + 4) = 7 balls    ⟹   P(R|E₁) = 3/7
      Bag II : 5 red out of (5 + 6) = 11 balls   ⟹   P(R|E₂) = 5/11
```

**Step 4 — Bayes' theorem.**

```
                        P(E₂) P(R|E₂)
      P(E₂|R) = ───────────────────────────────
                 P(E₁)P(R|E₁) + P(E₂)P(R|E₂)
```

**Step 5 — substitute.**

```
                     (1/2)(5/11)
      P(E₂|R) = ──────────────────────────
                 (1/2)(3/7) + (1/2)(5/11)
```

The (1/2) cancels throughout:

```
                    5/11
      P(E₂|R) = ─────────────
                 3/7 + 5/11
```

```
      3/7 + 5/11 = (33 + 35)/77 = 68/77
```

```
      P(E₂|R) = (5/11) × (77/68) = (5 × 7)/68 = 35/68
```

```
P(the ball came from Bag II | it is red) = 35/68          ≈ 0.515
```

*(Sanity check: Bag II's red fraction (5/11 ≈ 0.455) is slightly higher than Bag I's (3/7 ≈ 0.429),
and the two bags were equally likely to start with, so the posterior for Bag II should come out a
little above ½. It does: 35/68 ≈ 0.515 ✓)*

### Q2 — three machines, defective item, which machine?

**Step 1 — define events.**

```
      E₁ : item produced by machine A
      E₂ : item produced by machine B
      E₃ : item produced by machine C
      D  : item is defective
```

**Step 2 — priors.**

```
      P(E₁) = 0.25          P(E₂) = 0.35          P(E₃) = 0.40
```

**Step 3 — likelihoods.**

```
      P(D|E₁) = 0.05        P(D|E₂) = 0.04        P(D|E₃) = 0.02
```

**Step 4 — Bayes' theorem.**

```
                            P(E₃) P(D|E₃)
      P(E₃|D) = ───────────────────────────────────────────
                 P(E₁)P(D|E₁) + P(E₂)P(D|E₂) + P(E₃)P(D|E₃)
```

**Step 5 — substitute.**

```
      P(E₁)P(D|E₁) = 0.25 × 0.05 = 0.0125
      P(E₂)P(D|E₂) = 0.35 × 0.04 = 0.0140
      P(E₃)P(D|E₃) = 0.40 × 0.02 = 0.0080
                                   ────────
      Denominator  =               0.0345
```

*(Note in passing: 0.0345 is P(D), the overall defective rate — that is the total probability
theorem, and it is often asked as a separate part.)*

```
      P(E₃|D) = 0.0080 / 0.0345 = 80/345 = 16/69
```

```
P(machine C | defective) = 16/69          ≈ 0.232
```

### Q3 — die thrown twice, sum is 6, was a 4 shown?

**Define events.**

```
      A : the number 4 appears at least once
      B : the sum of the two numbers is 6
```

**List B.** The outcomes with sum 6:

```
      (1,5), (2,4), (3,3), (4,2), (5,1)          →  n(B) = 5
```

**List A ∩ B.** Which of those contain a 4?

```
      (2,4), (4,2)                                →  n(A ∩ B) = 2
```

**Compute.** All 36 outcomes are equally likely, so

```
      P(B) = 5/36          P(A ∩ B) = 2/36
```

```
      P(A|B) = P(A ∩ B)/P(B) = (2/36)/(5/36) = 2/5
```

```
P(a 4 appeared at least once | the sum is 6) = 2/5
```

> Once you have restricted to the five outcomes with sum 6, the answer is just "2 out of 5". Listing
> the reduced sample space explicitly is the fastest and safest method for this question type.

### Q4 — independent events, P(A ∪ B)

```
      P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
```

Since A and B are **independent**, P(A ∩ B) = P(A)·P(B) = (0.3)(0.4) = 0.12.

```
      P(A ∪ B) = 0.3 + 0.4 − 0.12 = 0.58
```

### Q5 — probability distribution of the number of aces (with replacement)

Let X = the number of aces drawn. Since the draws are **with replacement**, the two draws are
independent, and on each draw

```
      P(ace) = 4/52 = 1/13          P(not ace) = 12/13
```

X can be 0, 1 or 2.

```
      P(X = 0) = (12/13)(12/13) = 144/169

      P(X = 1) = (1/13)(12/13) + (12/13)(1/13) = 24/169      [ace first, or ace second]

      P(X = 2) = (1/13)(1/13) = 1/169
```

**Probability distribution:**

| X | 0 | 1 | 2 |
| --- | --- | --- | --- |
| P(X) | 144/169 | 24/169 | 1/169 |

**Check:** (144 + 24 + 1)/169 = 169/169 = 1 ✓

**Mean:**

```
      E(X) = Σ xᵢ pᵢ = 0(144/169) + 1(24/169) + 2(1/169)
           = (0 + 24 + 2)/169
           = 26/169
           = 2/13
```

```
Mean = 2/13          ≈ 0.154
```

*(Sensible: each draw gives an ace with probability 1/13, and there are two draws, so on average
2/13 aces.)*

### Q6 — urn with balls added

**Define events.**

```
      R₁ : the first ball drawn is red          B₁ : the first ball drawn is black
      R₂ : the second ball drawn is red
```

**Priors.** The urn starts with 5 red and 5 black, so 10 balls:

```
      P(R₁) = 5/10 = 1/2          P(B₁) = 5/10 = 1/2
```

**Likelihoods.** The ball drawn is returned, **and 2 more of the same colour are added**, so the urn
then has 12 balls.

```
      If R₁ occurred: 5 + 2 = 7 red and 5 black    ⟹   P(R₂|R₁) = 7/12
      If B₁ occurred: 5 red and 5 + 2 = 7 black    ⟹   P(R₂|B₁) = 5/12
```

**Apply the total probability theorem:**

```
      P(R₂) = P(R₁)P(R₂|R₁) + P(B₁)P(R₂|B₁)
            = (1/2)(7/12) + (1/2)(5/12)
            = (7 + 5)/24
            = 12/24
```

```
P(the second ball is red) = 1/2
```

> A pleasing result: adding balls of the colour drawn does not change the probability that the next
> ball is red, because the urn started symmetric. Worth stating as a remark — it shows understanding.

### Q7 — find P(A|B)

```
      P(A ∪ B) = P(A) + P(B) − P(A ∩ B)
⟹     7/11 = 6/11 + 5/11 − P(A ∩ B)
⟹     P(A ∩ B) = 11/11 − 7/11 = 4/11
```

```
      P(A|B) = P(A ∩ B)/P(B) = (4/11)/(5/11) = 4/5
```

### Q8 — P(B|A) = 1

```
      P(B|A) = P(A ∩ B)/P(A) = 1     ⟹     P(A ∩ B) = P(A)
```

If the probability of A ∩ B equals the probability of A, then A contributes nothing outside B — i.e.
**A ⊂ B**.

**Answer: (a) A ⊂ B**

*(Interpretation: whenever A happens, B is certain to happen. That means A is contained in B.)*

### Q9 — three kings without replacement

**Define events.**

```
      K₁ : the first card is a king
      K₂ : the second card is a king
      K₃ : the third card is a king
```

Since the draws are **without replacement**, use the multiplication theorem for three events:

```
      P(K₁ ∩ K₂ ∩ K₃) = P(K₁) · P(K₂|K₁) · P(K₃|K₁ ∩ K₂)
```

```
      P(K₁) = 4/52                        [4 kings in 52 cards]
      P(K₂|K₁) = 3/51                     [3 kings left in 51 cards]
      P(K₃|K₁ ∩ K₂) = 2/50                [2 kings left in 50 cards]
```

```
      P = (4/52)(3/51)(2/50) = 24/132600 = 1/5525
```

```
P(all three cards are kings) = 1/5525          ≈ 0.000181
```

### Q10 — case study: left-handed students

**Define events.**

```
      G : the student is a girl          B : the student is a boy
      L : the student is left-handed
```

```
      P(G) = 0.40          P(B) = 0.60
      P(L|G) = 0.05        P(L|B) = 0.08
```

**(i) P(L) — by the theorem of total probability:**

```
      P(L) = P(G)P(L|G) + P(B)P(L|B)
           = (0.40)(0.05) + (0.60)(0.08)
           = 0.020 + 0.048
           = 0.068
```

**P(a student is left-handed) = 0.068 = 17/250**

**(ii) P(G|L) — by Bayes' theorem:**

```
                  P(G)P(L|G)          0.020
      P(G|L) = ──────────────── = ───────────── = 20/68 = 5/17
                     P(L)              0.068
```

**P(the student is a girl | left-handed) = 5/17 ≈ 0.294**

**(iii)** Part (i) uses the **theorem of total probability**; part (ii) uses **Bayes' theorem**.

*(Notice that 5/17 ≈ 0.294 is well below P(G) = 0.40 — knowing the student is left-handed makes
"girl" less likely, because boys are left-handed at a higher rate. Sanity checks like this one are
worth doing.)*

### Q11 — find k and the mean

**Use Σpᵢ = 1:**

```
      k + 2k + 3k + 4k = 1
⟹     10k = 1
⟹     k = 1/10
```

**Distribution:**

| X | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| P(X) | 1/10 | 2/10 | 3/10 | 4/10 |

**Mean:**

```
      E(X) = 0(1/10) + 1(2/10) + 2(3/10) + 3(4/10)
           = (0 + 2 + 6 + 12)/10
           = 20/10
           = 2
```

```
k = 1/10 and Mean = 2
```

### Q12 — Assertion–Reason

**A:** "Mutually exclusive events with non-zero probabilities cannot be independent." **True.**
If mutually exclusive, P(A ∩ B) = 0. If also independent, P(A ∩ B) = P(A)P(B), which would force
P(A)P(B) = 0, contradicting both being non-zero.

**R:** "For mutually exclusive events, P(A ∩ B) = 0." **True** — that is the definition.

**Does R explain A?** Yes — A follows directly from R combined with the independence condition.

**Answer: (a) Both A and R are true, and R is the correct explanation of A.**

---

## 5. Test yourself

Time: 50 minutes. Answers below.

1. *(1)* If P(A) = 0.5, P(B) = 0.4 and P(A ∩ B) = 0.2, then P(A|B) is
   (a) 0.4 (b) 0.5 (c) 0.2 (d) 0.8
2. *(1)* If A and B are independent, P(A) = 1/2, P(B) = 1/3, then P(A ∩ B) is
   (a) 5/6 (b) 1/6 (c) 2/3 (d) 1/5
3. *(1)* For a probability distribution, Σpᵢ must equal
   (a) 0 (b) 1 (c) n (d) any positive number
4. *(2)* A coin is tossed three times. Find the probability of getting at least two heads.
5. *(2)* If P(A) = 0.6, P(B) = 0.3 and A, B are independent, find P(neither A nor B).
6. *(3)* Two dice are thrown. Given that the sum is 8, find the probability that one die shows a 2.
7. *(3)* A bag contains 4 red and 6 white balls. Two balls are drawn without replacement. Find the
   probability that both are red.
8. *(4)* A random variable X has the distribution below. Find c and E(X).

   | X | 1 | 2 | 3 | 4 | 5 |
   | --- | --- | --- | --- | --- | --- |
   | P(X) | c | 2c | 2c | 3c | c |

9. *(5)* Of the students in a college, 60% reside in a hostel and 40% do not. Past records show that
   30% of the hostellers and 20% of the day-scholars attain an A grade. One student is chosen at
   random and has an A grade. What is the probability that the student is a hosteller?
10. *(5)* Two groups are competing for the board positions of a corporation. The probabilities that
    the first and second groups will win are 0.6 and 0.4. Further, if the first group wins, the
    probability of introducing a new product is 0.7, and the corresponding probability if the second
    group wins is 0.3. Find the probability that the new product was introduced by the second group.
11. *(3)* A die is tossed twice. Find the probability distribution of the number of times a number
    greater than 4 appears, and find its mean.
12. *(2)* Three coins are tossed. Let A be "at least two heads" and B "the first coin shows a head".
    Find P(A|B).
13. *(2)* If A and B are events with P(A) = 0.4, P(B) = 0.8 and P(B|A) = 0.6, find P(A|B).

### Answer key

**1. (b) 0.5.** P(A|B) = 0.2/0.4 = 0.5.

**2. (b) 1/6.** (1/2)(1/3).

**3. (b) 1.**

**4. 1/2.** Sample space has 8 outcomes. At least two heads: HHH, HHT, HTH, THH → 4/8 = 1/2.

**5. 0.28.** P(A′ ∩ B′) = (1 − 0.6)(1 − 0.3) = (0.4)(0.7) = 0.28.

**6. 2/5.** Outcomes with sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) → 5 outcomes. Of these, those
containing a 2: (2,6) and (6,2) → 2. So P = 2/5.

**7. 2/15.** (4/10)(3/9) = 12/90 = 2/15.

**8. c = 1/9, E(X) = 3.** Σp = c + 2c + 2c + 3c + c = 9c = 1 ⟹ c = 1/9.
E(X) = [1(1) + 2(2) + 3(2) + 4(3) + 5(1)]/9 = (1 + 4 + 6 + 12 + 5)/9 = 27/9 = 3.

**9. 9/13.** Let H = hosteller, D = day-scholar, A = A grade.
P(H) = 0.6, P(D) = 0.4, P(A|H) = 0.3, P(A|D) = 0.2.
P(A) = (0.6)(0.3) + (0.4)(0.2) = 0.18 + 0.08 = 0.26.
P(H|A) = 0.18/0.26 = 18/26 = **9/13** ≈ 0.692.

**10. 2/9.** Let E₁ = first group wins, E₂ = second group wins, N = new product introduced.
P(E₁) = 0.6, P(E₂) = 0.4, P(N|E₁) = 0.7, P(N|E₂) = 0.3.
P(N) = (0.6)(0.7) + (0.4)(0.3) = 0.42 + 0.12 = 0.54.
P(E₂|N) = 0.12/0.54 = 12/54 = **2/9** ≈ 0.222.

**11.** "Greater than 4" means 5 or 6, so p = 2/6 = 1/3 per throw, and the throws are independent.
X = 0, 1, 2.
P(X = 0) = (2/3)² = 4/9; P(X = 1) = 2(1/3)(2/3) = 4/9; P(X = 2) = (1/3)² = 1/9.
Check: 4/9 + 4/9 + 1/9 = 1 ✓
E(X) = 0(4/9) + 1(4/9) + 2(1/9) = 6/9 = **2/3**.

**12. 3/4.** B = {HHH, HHT, HTH, HTT}, so P(B) = 4/8. A ∩ B = {HHH, HHT, HTH}, so P(A ∩ B) = 3/8.
P(A|B) = (3/8)/(4/8) = 3/4.

**13. 0.3.** P(A ∩ B) = P(A)·P(B|A) = (0.4)(0.6) = 0.24. P(A|B) = 0.24/0.8 = 0.3.

**Scoring.** Out of 34. Below 24 → the loss is almost certainly conditional-probability *direction*.
Redo §3 Q1, Q2 and Q10, writing out the five-step Bayes layout each time even when it feels
unnecessary.

---

## 6. Answering tips

**On Bayes' theorem — the 4/5-mark question**

1. **Define the events with letters, in words, before any arithmetic.** "Let E₁ be the event that the
   item came from machine A; let D be the event that the item is defective." This is a mark, and it
   is the step that prevents the inversion error.

2. **List all the priors, then all the likelihoods, as two separate groups.** Do not mix them. If you
   have three machines you should have exactly three priors and three likelihoods before you write
   the formula.

3. **Write the formula out in full before substituting**, with the whole denominator shown. Dropping
   a term from the denominator is the second-most-common error.

4. **The word "given" tells you the denominator.** "Given that it is defective" → the conditioning
   event is D, so you want P(machine|D), and P(D) is the denominator.

5. **The denominator is P(A) by the total probability theorem — say so.** Many questions ask for P(A)
   as a separate part, and pointing out the connection is good practice and sometimes a mark.

6. **Do a sanity check on the answer.** Posterior probabilities must lie between 0 and 1, and they
   should move in the sensible direction relative to the prior. If a machine makes 40% of output but
   only 2% defectives, its posterior share of defectives must be *below* 40% — 16/69 ≈ 23% ✓.

7. **Leave the answer as a fraction in lowest terms**, and add the decimal in brackets. 16/69 rather
   than 0.2318…

**On conditional probability**

8. **For dice and coin problems, list the reduced sample space explicitly.** Writing out the five
   outcomes with sum 6 is faster and far safer than manipulating formulas, and it shows your method.

9. **State which of P(A|B) and P(B|A) you are computing.** Write it symbolically before substituting.

10. **For "without replacement", the denominators decrease.** 4/52, then 3/51, then 2/50. For "with
    replacement" they do not. Read the question for which it is — this single word changes the whole
    answer.

**On independence**

11. **Never assume independence.** Use P(A ∩ B) = P(A)P(B) **only** when the question says the events
    are independent, or you have verified it. Conversely, when a question asks you to *check*
    independence, compute both P(A ∩ B) and P(A)P(B) and compare.

12. **"At least one" means 1 − P(none).** For independent events, P(at least one) =
    1 − (1 − P(A))(1 − P(B)). This is almost always faster than adding cases.

**On random variables**

13. **Use Σpᵢ = 1 to find the unknown constant**, and show that equation. It is the first mark.

14. **Present the distribution as a table**, then compute the mean underneath it. Do not compute the
    mean inline.

15. **Do not compute variance.** It is out of syllabus, and time spent on it is wasted.
