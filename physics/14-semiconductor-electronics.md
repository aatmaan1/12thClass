# Ch 14 — Semiconductor Electronics

**Unit IX (7 marks — 10% of the paper) · Typical appearance: 1–2 MCQs + a 2/3-mark question, and
very often one of the two Section-D case studies.**

**Read this even if you read nothing else. After the deletions, this chapter is five topics and
7 marks — the highest marks-per-hour in the paper. Students skip it because it sits last in the book
and because seniors remember it as "the hard transistor chapter". It no longer is.**

---

## 1. Scope

### In the syllabus — the whole of it

- **Energy bands** in conductors, semiconductors and insulators (qualitative ideas only)
- **Intrinsic and extrinsic** semiconductors — **p-type and n-type**
- **p-n junction**
- **Semiconductor diode** — **I–V characteristics** in forward and reverse bias
- Application of the junction diode — **diode as a rectifier**

That is five topics. There is nothing else.

### Deleted — do not study

- **Zener diode** and its use as a **voltage regulator**
- **Optoelectronic devices** — LED, photodiode, solar cell
- **Transistors** — construction, characteristics, transistor as an **amplifier**, as a **switch**, as
  an **oscillator**
- **Logic gates** — OR, AND, NOT, NAND, NOR, and their truth tables
- **Digital electronics** and integrated circuits

> **The deletion here is enormous.** Roughly two thirds of the old chapter is gone, including
> everything students found difficult. The **7 marks did not go anywhere** — they are now concentrated
> on the five surviving topics, which means the questions are more predictable than in any other
> chapter. Two focused days here is worth more than two weeks on
> [Ch 5 Magnetism and Matter](05-magnetism-and-matter.md).
>
> If a practice question mentions a transistor, a logic gate, a Zener diode or an LED, **skip it**.

---

## 2. Brief

### Start here — in plain English

Everything in your phone is in this chapter. It is also the chapter students most often try to
memorise and most often should not, because the whole thing follows from one idea: **you can control
how well a material conducts, and if you can do that you can build a switch with no moving parts.**

Start with why materials differ at all. In an isolated atom electrons sit at sharp energy levels.
Bring 10²³ atoms together in a crystal and those levels smear into continuous **bands**, with gaps
between them where no electron is allowed. Two bands matter: the **valence band**, full of the
electrons holding the crystal together, and the **conduction band** above it, where an electron is
free to roam and carry current. What decides everything is the gap between them.

In a **metal** the bands overlap, or the upper one is half full, so electrons can move with almost
no persuasion — hence good conduction. In an **insulator** the gap is large, several electronvolts,
and at room temperature no electron can cross it. A **semiconductor** is the interesting middle
case: a gap of about one electronvolt, small enough that thermal energy shakes a few electrons
across. So it conducts a little — and, importantly, it conducts *better when heated*, opposite to a
metal, because heat manufactures carriers rather than obstructing them.

When an electron leaves the valence band it leaves behind a vacancy, and a neighbouring electron can
slide into it, which moves the vacancy the other way. It is easier to keep track of the vacancy than
of all the electrons shuffling, so we treat it as a positive particle called a **hole**. Holes are a
bookkeeping convenience that behaves exactly like a real positive carrier.

A pure semiconductor is not much use — too few carriers, and equal numbers of each. The trick is
**doping**: replacing one atom in a million with a deliberate impurity. Silicon has four outer
electrons. Substitute an atom with five (phosphorus) and there is one electron spare, free to
conduct: an **n-type** semiconductor, carrying current mainly by electrons. Substitute one with
three (boron) and there is one electron missing, a ready-made hole: **p-type**, carrying current
mainly by holes. Both are still electrically neutral overall — this is a very common
misunderstanding. You added a neutral atom; you changed which carriers are available, not the total
charge.

Now put a p-type region and an n-type region in contact, and the chapter's one real piece of
machinery appears. Electrons wander across into the p-side, holes into the n-side, and they
annihilate near the boundary — leaving a thin **depletion region** with no free carriers, and
exposed fixed ions on either side. Those ions set up a small built-in voltage, the **barrier
potential**, pointing so as to stop further diffusion. Equilibrium.

Everything a diode does follows from what an external voltage does to that barrier. Connect the
positive terminal to the p-side — **forward bias** — and you oppose the built-in field, the
depletion region narrows, the barrier drops, and beyond about 0.7 V in silicon current flows
freely. Reverse the battery and you *reinforce* the barrier: the depletion region widens and almost
nothing flows. A diode is a one-way valve, and that is the entire content of its I–V graph.

**Rectification** is the application: AC in, DC out. A half-wave rectifier simply blocks the
half-cycles it does not like, wasting half the input. A full-wave rectifier uses two diodes (or four
in a bridge) arranged so that both halves of the cycle are routed through the load in the same
direction — so the output frequency is twice the input, a detail the board likes to ask about.

> **Check your syllabus scope.** Transistors, logic gates and the Zener diode have been trimmed from
> the rationalised syllabus. §1 of this chapter lists exactly what remains examinable; the reliable
> core is bands, doping, the p–n junction, the diode's characteristics and rectification.

**Learn it from someone else too**

- **Video lecture** — [search: semiconductor electronics class 12 one shot](https://www.youtube.com/results?search_query=semiconductor+electronics+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: semiconductors and p-n junction](https://www.khanacademy.org/search?page_search_query=semiconductor%20p-n%20junction%20diode)
- **The book the paper is set from** — [NCERT Physics Part II, Chapter 14 (PDF)](https://ncert.nic.in/textbook/pdf/leph206.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 45 *Semiconductors and Semiconductor Devices*.
  §45.1–45.6 for bands, doping and the junction; §45.7–45.8 for the diode and rectifier. Stop where
  your syllabus does.

---

### Energy bands

In an isolated atom the electron energies are discrete levels. In a solid, the atoms are so close
that these levels broaden into **bands** of closely spaced allowed energies, separated by **forbidden
gaps**.

| Band | What it is |
| --- | --- |
| **Valence band** | The band containing the **valence electrons** — the highest band that is occupied at 0 K |
| **Conduction band** | The next band above it. Electrons here are **free to move** and carry current |
| **Forbidden energy gap (E_g)** | The energy gap between the top of the valence band and the bottom of the conduction band. No electron can have an energy in this gap |

**Conduction requires electrons in the conduction band.** So the size of E_g determines whether a
solid conducts.

**The three cases — draw all three diagrams:**

```
   CONDUCTOR              SEMICONDUCTOR              INSULATOR
                          
 ┌─────────────┐        ┌─────────────┐           ┌─────────────┐
 │ conduction  │        │ conduction  │           │ conduction  │
 │    band     │        │    band     │           │    band     │
 ├─────────────┤        └─────────────┘           └─────────────┘
 │  overlap    │           E_g ≈ 1 eV                            
 │  (E_g = 0)  │        ┌─────────────┐              E_g > 3 eV  
 ├─────────────┤        │  valence    │                          
 │   valence   │        │    band     │           ┌─────────────┐
 │    band     │        │  (full)     │           │  valence    │
 └─────────────┘        └─────────────┘           │    band     │
                                                  │  (full)     │
                                                  └─────────────┘
```

| | **Conductor** | **Semiconductor** | **Insulator** |
| --- | --- | --- | --- |
| Forbidden gap E_g | **zero** — the bands **overlap**, or the valence band is only partly filled | **small**, ≈ 1 eV | **large**, > 3 eV |
| Electrons in the conduction band at room temperature | very many | a few (thermally excited) | essentially none |
| Conductivity | very high | intermediate | very low |
| Effect of raising temperature | conductivity **decreases** | conductivity **increases** | remains an insulator |
| Examples | copper, silver, aluminium | silicon (E_g = 1.1 eV), germanium (E_g = 0.7 eV) | diamond (E_g ≈ 6 eV), glass, wood |

> **The key comparison is E_g.** In a semiconductor E_g ≈ 1 eV is comparable to the thermal energy
> available at room temperature, so a small but useful number of electrons can be excited across the
> gap. In an insulator E_g > 3 eV is far too large for thermal excitation. That one sentence answers
> most questions in this section.

### Intrinsic semiconductors

An **intrinsic semiconductor** is a **pure** semiconductor, with no added impurity.

At absolute zero the valence band is full and the conduction band empty, so it behaves as a perfect
insulator. At room temperature, thermal energy breaks a few covalent bonds, exciting electrons into
the conduction band. Each electron that leaves the valence band leaves behind a vacancy — a
**hole**, which behaves as a **positive** charge carrier.

**So in an intrinsic semiconductor, electrons and holes are always created in pairs:**

```
      n_e = n_h = n_i                       (n_i = intrinsic carrier concentration)
```

**Conduction occurs by both electrons and holes**, moving in opposite directions under an applied
field. The hole current arises from valence electrons hopping into adjacent vacancies, which is
equivalent to the vacancy moving the other way.

**Effect of temperature.** Raising the temperature breaks more bonds, so **n_i increases rapidly**
(roughly exponentially) and the **conductivity increases** — which is why semiconductors have a
**negative temperature coefficient of resistivity** (see
[Ch 3](03-current-electricity.md)).

Intrinsic semiconductors have too low a conductivity to be useful, which is why they are doped.

### Extrinsic semiconductors — doping

**Doping** is the deliberate addition of a small, controlled amount of a suitable impurity to a pure
semiconductor in order to increase its conductivity. Typically about 1 impurity atom per 10⁶ host
atoms.

**n-type semiconductor** — doped with a **pentavalent** impurity (5 valence electrons):

- Dopants: **phosphorus, arsenic, antimony, bismuth**
- Four of the impurity's five valence electrons form covalent bonds with neighbouring Si/Ge atoms;
  the **fifth is loosely bound** and easily becomes a free electron.
- The impurity **donates** an electron, so it is called a **donor**.
- **Majority carriers: electrons.** **Minority carriers: holes.**
- n_e >> n_h

**p-type semiconductor** — doped with a **trivalent** impurity (3 valence electrons):

- Dopants: **boron, aluminium, indium, gallium**
- The impurity's three valence electrons form three bonds, leaving **one bond incomplete** — a
  **hole**, which can accept an electron from a neighbouring bond.
- The impurity **accepts** an electron, so it is called an **acceptor**.
- **Majority carriers: holes.** **Minority carriers: electrons.**
- n_h >> n_e

> **Both n-type and p-type semiconductors are electrically NEUTRAL.** This is asked directly and
> answered wrongly very often. Doping does not add net charge: a donor atom that has given up an
> electron becomes a **fixed positive ion** in the lattice, exactly balancing the free electron. The
> names "n-type" and "p-type" refer only to the **sign of the majority carriers**, not to any net
> charge on the material.

**The mass-action relation** (worth knowing):

```
      n_e × n_h = n_i²
```

so increasing one type of carrier by doping necessarily **decreases** the other.

### The p-n junction

*Diagram:* a bar of semiconductor, p-type on the left and n-type on the right, meeting at a junction.
Show the holes as circles in the p-region and electrons as dots in the n-region; between them, a
narrow **depletion region** containing **immobile negative ions on the p-side** and **immobile
positive ions on the n-side**, with an arrow showing the internal field from n to p and the barrier
potential V_B.

**How the junction forms — the two processes:**

**1. Diffusion.** Because the hole concentration is far higher on the p-side and the electron
concentration far higher on the n-side, **holes diffuse from p to n** and **electrons diffuse from n
to p**. This is a **diffusion current**, from p to n.

**2. Formation of the depletion region.** As an electron leaves the n-region it exposes a **fixed
positive donor ion**; as a hole leaves the p-region it exposes a **fixed negative acceptor ion**.
Near the junction, therefore, a narrow region forms that is **depleted of mobile charge carriers** and
contains only **immobile ions** — negative on the p-side, positive on the n-side. This is the
**depletion region** (or depletion layer), typically a fraction of a micrometre wide.

**3. Barrier potential.** The immobile ions set up an **internal electric field** directed from the
n-side to the p-side. The associated potential difference across the depletion region is the
**barrier potential V_B** (also called the potential barrier or junction potential):

```
      V_B ≈ 0.3 V for germanium                V_B ≈ 0.7 V for silicon
```

**4. Equilibrium.** This field opposes further diffusion, but it **assists** the motion of minority
carriers — driving the few electrons on the p-side across to the n-side and vice versa. That is the
**drift current**, from n to p. At equilibrium the **diffusion current exactly balances the drift
current**, so the **net current is zero** and the junction is stable.

### Forward and reverse bias

**Forward bias** — the **p-side is connected to the positive terminal** of the battery and the n-side
to the negative.

| Effect | |
| --- | --- |
| The applied field **opposes** the internal barrier field | |
| Barrier potential | **decreases** |
| Width of the depletion region | **decreases** |
| Diffusion of majority carriers | greatly **increased** |
| Current | **large**, of the order of **milliamperes**; carried by **majority** carriers |
| Resistance of the junction | **low** (a few ohms to a few hundred ohms) |

Appreciable current begins only once the applied voltage exceeds the barrier potential — the
**knee (threshold or cut-in) voltage**, about **0.3 V for Ge** and **0.7 V for Si**. Beyond the knee,
the current rises very steeply.

**Reverse bias** — the **p-side is connected to the negative terminal** and the n-side to the
positive.

| Effect | |
| --- | --- |
| The applied field **aids** the internal barrier field | |
| Barrier potential | **increases** |
| Width of the depletion region | **increases** |
| Diffusion of majority carriers | essentially **stopped** |
| Current | **very small**, of the order of **microamperes**; carried by **minority** carriers |
| Resistance of the junction | **very high** (of the order of megohms) |

The small reverse current is called the **reverse saturation current**. It is almost **independent of
the applied reverse voltage**, because it is limited by the small number of thermally generated
minority carriers available, not by the voltage. (It does, however, increase with temperature.)

At a sufficiently large reverse voltage the junction suffers **breakdown**, and the reverse current
rises abruptly. That voltage is the **breakdown voltage**.

### I–V characteristics of a p-n junction diode

*Circuit to obtain them:* for the **forward** characteristic, the diode in series with a milliammeter,
a rheostat and a battery, with the p-side to the positive terminal, and a voltmeter across the diode.
For the **reverse** characteristic, the same but with the battery reversed and a **micro**ammeter in
place of the milliammeter.

```
                    I (mA)
                      │        ╱
                      │       │
                      │      ╱     ← FORWARD BIAS
                      │     ╱        current in mA
                      │    │         steep rise after the knee
                      │  ──╯
                      │ ╱  ↑ knee voltage (0.3 V Ge, 0.7 V Si)
    ──────────────────┼────────────────→  V (volts)
   ←── V (reverse)    │
                      │
   breakdown ──►  ────┤   ← REVERSE BIAS: tiny, nearly constant
      │               │      reverse saturation current (µA)
      ▼               │
                    I (µA)
```

**The features to state:**

1. In **forward bias**, the current is negligible until the applied voltage reaches the **knee
   voltage**; beyond it the current rises **very steeply and non-linearly**.
2. In **reverse bias**, only a very small, almost **constant** reverse saturation current flows
   (microamperes), until **breakdown** occurs.
3. **The scales on the two halves are different** — mA for forward, µA for reverse. You must label
   them so, or the graph is wrong.
4. The characteristic is **non-linear**, so a diode is a **non-ohmic** device: V/I is not constant.

**Dynamic (a.c.) resistance:**

```
      r_d = ΔV/ΔI
```

taken from the slope of the characteristic at the operating point. It is small in forward bias and
very large in reverse bias.

**The essential conclusion:** a p-n junction diode conducts **easily in one direction only** —
forward. It is therefore a **one-way valve** for current, and this is precisely what makes it useful
as a **rectifier**.

### Diode as a rectifier

**Rectification** is the conversion of **alternating current into direct (unidirectional) current**.
It works because the diode conducts only when forward biased.

**Half-wave rectifier**

*Circuit:* an AC supply feeding the primary of a transformer; the secondary connected in series with
a single **diode** and a **load resistance R_L**. The output is taken across R_L.

**Working.** During the half-cycle in which the diode is **forward biased**, it conducts and current
flows through R_L, producing an output voltage. During the next half-cycle the diode is **reverse
biased**, so it does not conduct and the output is **zero**.

```
  INPUT (AC)          ╱‾╲       ╱‾╲       ╱‾╲
                     ╱   ╲     ╱   ╲     ╱   ╲
                 ───┴─────┴───┴─────┴───┴─────┴───→ t
                          ╲   ╱     ╲   ╱
                           ╲_╱       ╲_╱

  OUTPUT             ╱‾╲             ╱‾╲             ╱‾╲
  (half-wave)       ╱   ╲           ╱   ╲           ╱   ╲
                 ───┴─────┴─────────┴─────┴─────────┴─────→ t
                         (nothing during the other half-cycle)
```

So the output appears only during **alternate half-cycles**. The output frequency **equals the input
frequency**.

**Full-wave rectifier**

*Circuit:* an AC supply feeding a **centre-tapped transformer**; the two ends of the secondary
connected to the p-sides of **two diodes** D₁ and D₂; the two n-sides joined together and connected
through the **load resistance R_L** back to the **centre tap**.

**Working.** During one half-cycle, the upper end of the secondary is positive, so **D₁ is forward
biased and D₂ reverse biased**; D₁ conducts and current flows through R_L. During the next
half-cycle, the polarity reverses, so **D₂ is forward biased and D₁ reverse biased**; D₂ conducts and
current flows through R_L **in the same direction** as before.

```
  INPUT (AC)          ╱‾╲       ╱‾╲       ╱‾╲
                     ╱   ╲     ╱   ╲     ╱   ╲
                 ───┴─────┴───┴─────┴───┴─────┴───→ t
                          ╲   ╱     ╲   ╱
                           ╲_╱       ╲_╱

  OUTPUT             ╱‾╲ ╱‾╲ ╱‾╲ ╱‾╲ ╱‾╲ ╱‾╲
  (full-wave)       ╱   V   V   V   V   V   ╲
                 ───┴───────────────────────────→ t
                     (output during BOTH half-cycles)
```

So the output appears during **both** half-cycles, always in the same direction through the load. The
output frequency is **twice the input frequency**.

**Comparison:**

| | **Half-wave** | **Full-wave** |
| --- | --- | --- |
| Number of diodes | 1 | 2 (with a centre-tapped transformer) |
| Conduction | alternate half-cycles only | both half-cycles |
| Output frequency | same as the input | **twice** the input |
| Efficiency | lower (~40.6%) | higher (~81.2%) |
| Ripple in the output | larger | smaller |

**Why a filter is used.** The rectified output is unidirectional but still **pulsating**, not steady
DC. A **capacitor connected in parallel with the load** (a filter) smooths it: the capacitor charges
at the peaks and discharges through the load in the gaps, greatly reducing the ripple.

### Quick recall box

```
ENERGY BANDS  (E_g = forbidden gap between valence and conduction bands)
  CONDUCTOR     : E_g = 0, bands overlap ;  conductivity ↓ with T
  SEMICONDUCTOR : E_g ≈ 1 eV (Si 1.1, Ge 0.7) ;  conductivity ↑ with T
  INSULATOR     : E_g > 3 eV (diamond ≈ 6 eV)

INTRINSIC : pure ;  n_e = n_h = n_i ;  conduction by BOTH electrons and holes
  pairs created thermally ;  n_i rises fast with T ;  insulator at 0 K

EXTRINSIC (doping ≈ 1 impurity per 10⁶ atoms)
  n-TYPE : PENTAVALENT dopant (P, As, Sb, Bi) = DONOR
           majority ELECTRONS, minority holes ;  n_e >> n_h
  p-TYPE : TRIVALENT dopant (B, Al, In, Ga) = ACCEPTOR
           majority HOLES, minority electrons ;  n_h >> n_e
  BOTH ARE ELECTRICALLY NEUTRAL       n_e n_h = n_i²

p-n JUNCTION
  diffusion of majority carriers → immobile ions exposed → DEPLETION REGION
  (negative ions on the p-side, positive on the n-side)
  internal field n → p ;  BARRIER POTENTIAL V_B ≈ 0.3 V (Ge), 0.7 V (Si)
  equilibrium: diffusion current = drift current, net current zero

FORWARD BIAS (p to +) : barrier ↓, depletion width ↓, current LARGE (mA),
  majority carriers, resistance LOW ;  knee voltage 0.3 V Ge / 0.7 V Si
REVERSE BIAS (p to −) : barrier ↑, depletion width ↑, current TINY (µA),
  minority carriers, resistance HIGH ;  reverse saturation current is nearly
  independent of voltage ;  breakdown at large reverse V

I–V CHARACTERISTIC: non-linear ⟹ diode is NON-OHMIC
  label the axes: mA for forward, µA for reverse
  dynamic resistance r_d = ΔV/ΔI

RECTIFIER: AC → unidirectional DC (the diode conducts one way only)
  HALF-WAVE : 1 diode ; alternate half-cycles ; output frequency = input
  FULL-WAVE : 2 diodes + CENTRE-TAPPED transformer ; both half-cycles ;
              output frequency = 2 × input ; more efficient, less ripple
  a capacitor in parallel with the load acts as a FILTER, smoothing the ripple
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* With the help of a circuit diagram, explain the working of a **full-wave
rectifier**. Draw the input and output waveforms. How does the output frequency compare with the
input frequency?

**Q2.** *(3 marks)* Draw the energy band diagrams for a conductor, a semiconductor and an insulator,
and distinguish between them on the basis of the forbidden energy gap.

**Q3.** *(3 marks)* Explain, with a diagram, how a **depletion region** and a **barrier potential**
are formed in a p-n junction.

**Q4.** *(3 marks)* Draw the I–V characteristics of a p-n junction diode in forward and reverse bias.
Explain the shape of the curve in each case.

**Q5.** *(3 marks)* Distinguish between n-type and p-type semiconductors. Are they electrically
charged? Explain.

**Q6.** *(2 marks)* What is meant by doping? Name two pentavalent and two trivalent dopants.

**Q7.** *(3 marks)* Explain the working of a **half-wave rectifier** with a circuit diagram and
input/output waveforms.

**Q8.** *(2 marks)* Why does the conductivity of a semiconductor increase with temperature, while that
of a metal decreases?

**Q9.** *(2 marks)* Why is the reverse saturation current of a diode almost independent of the applied
reverse voltage?

**Q10.** *(1 mark, MCQ)* In an n-type semiconductor, the majority carriers are
(a) holes (b) electrons (c) protons (d) positive ions

**Q11.** *(2 marks)* In a p-n junction diode, the forward bias resistance is low and the reverse bias
resistance is high. Explain.

**Q12.** *(4 marks, case study)* A silicon diode is connected in series with a resistance of 200 Ω
and a battery of 5 V, with the p-side towards the positive terminal.
(i) Is the diode forward or reverse biased?
(ii) Taking the voltage drop across a conducting silicon diode as 0.7 V, find the current in the
circuit.
(iii) What would the current be if the battery were reversed?
(iv) Explain why a diode is called a non-ohmic device.

**Q13.** *(2 marks)* Why is a semiconductor an insulator at 0 K?

---

## 4. Solutions

### Q1 — full-wave rectifier

*Circuit diagram (draw and label all of this):* an AC input to the **primary** of a transformer; a
**centre-tapped secondary**; the upper end of the secondary connected to the p-side of diode **D₁**
and the lower end to the p-side of diode **D₂**; the n-sides of both diodes joined and connected
through the **load resistance R_L** back to the **centre tap**. Mark the output across R_L.

**Principle.** A p-n junction diode conducts appreciably only when it is **forward biased**. By
arranging two diodes so that one conducts on each half-cycle, current can be made to flow through the
load in the **same direction** throughout the AC cycle.

**Working.**

**During the first half-cycle**, suppose the **upper end** of the secondary is positive with respect
to the centre tap. Then:
- **D₁ is forward biased** (its p-side is at the positive end) and **conducts**;
- **D₂ is reverse biased** and does not conduct.

Current flows from the upper end of the secondary, through D₁, down through R_L, and back to the
centre tap.

**During the second half-cycle**, the polarity reverses, so the **lower end** is positive. Then:
- **D₂ is forward biased** and **conducts**;
- **D₁ is reverse biased** and does not conduct.

Current now flows from the lower end of the secondary, through D₂, and **down through R_L in the same
direction as before**, back to the centre tap.

So current flows through the load **during both half-cycles**, and always in the **same direction** —
the AC input has been rectified.

**Waveforms:**

```
  INPUT (AC across the whole secondary)
                        ╱‾╲       ╱‾╲       ╱‾╲
                       ╱   ╲     ╱   ╲     ╱   ╲
                   ───┴─────┴───┴─────┴───┴─────┴────→ t
                            ╲   ╱     ╲   ╱
                             ╲_╱       ╲_╱

  OUTPUT (across R_L)
                        ╱‾╲ ╱‾╲ ╱‾╲ ╱‾╲ ╱‾╲ ╱‾╲
                       ╱   V   V   V   V   V   ╲
                   ───┴─────────────────────────────→ t
                       D₁   D₂   D₁   D₂   D₁   D₂
```

*(Align the output pulses under the corresponding input half-cycles, and mark which diode conducts
for each pulse.)*

**Output frequency.** Since one output pulse is produced for **each half-cycle** of the input, there
are **two** output pulses per input cycle. Therefore

```
      output frequency = 2 × input frequency
```

For a 50 Hz mains input, the ripple frequency of the output is **100 Hz**.

*(A half-wave rectifier, by contrast, gives one pulse per input cycle, so its output frequency equals
the input frequency.)*

**Note.** The output is unidirectional but still **pulsating**. A **capacitor in parallel with the
load** acts as a filter, charging at the peaks and discharging through the load between them, and so
smooths the output towards steady DC. ∎

### Q2 — energy band diagrams

```
      CONDUCTOR                SEMICONDUCTOR              INSULATOR

  ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
  │  conduction  │          │  conduction  │          │  conduction  │
  │     band     │          │     band     │          │     band     │
  ├──────────────┤          └──────────────┘          └──────────────┘
  │   OVERLAP    │              ↕ E_g ≈ 1 eV
  │   E_g = 0    │          ┌──────────────┐              ↕ E_g > 3 eV
  ├──────────────┤          │   valence    │
  │   valence    │          │  band (full) │          ┌──────────────┐
  │     band     │          └──────────────┘          │   valence    │
  └──────────────┘                                    │  band (full) │
                                                      └──────────────┘
```

**Distinction on the basis of the forbidden energy gap:**

| | **Conductor** | **Semiconductor** | **Insulator** |
| --- | --- | --- | --- |
| Forbidden gap E_g | **zero** — the valence and conduction bands **overlap** (or the valence band is only partly filled) | **small**, about **1 eV** (Si 1.1 eV, Ge 0.7 eV) | **large**, more than **3 eV** (diamond ≈ 6 eV) |
| Electrons in the conduction band at room temperature | very large number | a small but appreciable number, thermally excited across the gap | practically none |
| Conductivity | very high | intermediate | negligible |
| Examples | copper, silver | silicon, germanium | diamond, glass |

**The essential point.** Conduction requires electrons in the **conduction band**. In a conductor
there are always plenty. In a semiconductor E_g ≈ 1 eV is **comparable with the thermal energy
available at room temperature**, so some electrons can be excited across the gap, leaving holes
behind. In an insulator E_g > 3 eV is **far too large** for thermal excitation at ordinary
temperatures, so the conduction band stays empty.

### Q3 — formation of the depletion region and barrier potential

*Diagram:* a bar with a p-region on the left (holes shown as ○, and after diffusion, fixed negative
acceptor ions ⊖ near the junction) and an n-region on the right (electrons shown as ●, and fixed
positive donor ions ⊕ near the junction). Label the depletion region, the internal field **E**
pointing from n to p, and the barrier potential V_B.

**Step 1 — diffusion.** In the p-region the hole concentration is very high, and in the n-region the
electron concentration is very high. Because of this **concentration gradient**, as soon as the
junction is formed:

- **holes diffuse from the p-side to the n-side**, and
- **electrons diffuse from the n-side to the p-side**.

This constitutes a **diffusion current**, directed from p to n.

**Step 2 — formation of the depletion region.** When an electron diffuses away from the n-side, it
leaves behind a **fixed (immobile) positive donor ion** in the lattice. When a hole diffuses away from
the p-side, it leaves behind a **fixed negative acceptor ion**.

The narrow region on either side of the junction therefore becomes **depleted of mobile charge
carriers** and contains only these **immobile ions** — **negative on the p-side** and **positive on
the n-side**. This region is called the **depletion region** (or depletion layer). Its width is
typically a fraction of a micrometre.

**Step 3 — barrier potential.** These layers of fixed opposite charges set up an **internal electric
field** across the depletion region, directed from the **n-side to the p-side**. The associated
potential difference is called the **barrier potential V_B**, with the n-side at a higher potential
than the p-side:

```
      V_B ≈ 0.3 V for germanium              V_B ≈ 0.7 V for silicon
```

**Step 4 — equilibrium.** The internal field **opposes further diffusion** of majority carriers. It
does, however, **assist** the motion of minority carriers (the few electrons on the p-side and holes
on the n-side), sweeping them across the junction — this is the **drift current**, directed from n
to p.

Diffusion continues until the barrier is large enough that the **diffusion current is exactly
balanced by the drift current**. At that point the **net current across the junction is zero**, and
the junction is in **equilibrium** with a stable depletion region and barrier potential. ∎

### Q4 — I–V characteristics of a p-n junction diode

*Circuits (draw both):* for the forward characteristic — the diode with its p-side to the positive
terminal of a battery, in series with a rheostat and a **milliammeter**, with a voltmeter across the
diode. For the reverse characteristic — the same circuit with the battery reversed and a
**microammeter** in place of the milliammeter.

```
                       I (mA)
                          │           ╱
                          │          │
                          │         ╱
                          │        │      FORWARD BIAS
                          │       ╱       (current in mA)
                          │     ─╯
                          │   ╱ ↑
                          │ ╱   knee voltage
      ────────────────────┼────────────────────→ V (volts)
      ← reverse V         │
                          │
   breakdown ────►   ─────┤   REVERSE BIAS
        │                 │   (current in µA — note the different scale)
        ▼                 │
                       I (µA)
```

**Forward bias — explanation of the shape.**

At small applied voltages the current is **almost zero**, because the applied voltage is not yet
enough to overcome the **barrier potential**. Once the applied voltage exceeds the **knee (threshold)
voltage** — about **0.3 V for germanium** and **0.7 V for silicon** — the barrier is effectively
cancelled, the depletion region becomes very narrow, and the **majority carriers** cross the junction
freely. The current then rises **very steeply and non-linearly** with voltage, and is of the order of
**milliamperes**. The junction resistance is **low**.

**Reverse bias — explanation of the shape.**

The applied field now **aids** the internal barrier field, so the barrier potential increases and the
depletion region widens. The **majority carriers** are therefore prevented from crossing, and the
diffusion current stops.

However, a very small current does flow, carried by the **thermally generated minority carriers** —
the few electrons on the p-side and holes on the n-side — which the field sweeps across the junction.
This is the **reverse saturation current**, of the order of **microamperes**, and it is almost
**independent of the applied voltage** because it is limited by the *number* of minority carriers
available rather than by the voltage. The junction resistance is **very high**.

At a sufficiently large reverse voltage the junction undergoes **breakdown**, and the reverse current
increases abruptly.

**Conclusion.** The characteristic is markedly **non-linear** and quite different in the two
directions: the diode conducts easily in the **forward** direction and hardly at all in the
**reverse** direction. It therefore acts as a **one-way valve** for current — the property that makes
it useful as a rectifier.

### Q5 — n-type vs p-type, and whether they are charged

| | **n-type** | **p-type** |
| --- | --- | --- |
| **Dopant** | **pentavalent** (5 valence electrons) | **trivalent** (3 valence electrons) |
| **Examples of dopant** | phosphorus, arsenic, antimony, bismuth | boron, aluminium, indium, gallium |
| **Name of the dopant** | **donor** — it donates a free electron | **acceptor** — it accepts an electron, creating a hole |
| **Majority carriers** | **electrons** | **holes** |
| **Minority carriers** | holes | electrons |
| **Carrier concentrations** | n_e >> n_h | n_h >> n_e |

**Are they electrically charged?**

**No — both n-type and p-type semiconductors are electrically NEUTRAL.**

**Explanation.** Doping does not add any net charge to the crystal. Consider an n-type semiconductor:
each pentavalent donor atom contributes one **free electron** (negative), but the atom itself, having
lost that electron, becomes a **fixed positive ion** in the lattice. The two charges are equal and
opposite, so they cancel exactly. The same argument applies to p-type material, where each acceptor
atom that accepts an electron becomes a fixed **negative** ion, balancing the mobile positive hole.

The terms "n-type" and "p-type" therefore refer only to the **sign of the majority charge carriers**
— **not** to any net charge on the material as a whole.

### Q6 — doping

**Doping** is the process of deliberately adding a small, carefully controlled amount of a suitable
impurity to a pure (intrinsic) semiconductor in order to **increase its electrical conductivity**.

The doping level is very small — typically about **1 impurity atom per 10⁶ atoms** of the host — so
that the crystal structure is not disturbed.

**Two pentavalent dopants:** **phosphorus (P)** and **arsenic (As)**.
*(Also antimony, bismuth. These produce n-type material.)*

**Two trivalent dopants:** **boron (B)** and **aluminium (Al)**.
*(Also indium, gallium. These produce p-type material.)*

### Q7 — half-wave rectifier

*Circuit diagram:* an AC input to the primary of a transformer; the secondary connected in series
with a **single diode** and the **load resistance R_L**; the output taken across R_L. Label the AC
input, the diode, R_L and the output.

**Principle.** A p-n junction diode conducts appreciably only when it is **forward biased**. So if a
single diode is placed in series with a load and an AC supply, current will flow only during those
half-cycles in which the diode happens to be forward biased.

**Working.**

**During the positive half-cycle** of the input (taking the polarity that makes the diode's p-side
positive), the diode is **forward biased**. It offers low resistance and **conducts**, so current
flows through R_L and an output voltage appears across it.

**During the negative half-cycle**, the polarity reverses and the diode becomes **reverse biased**.
It offers very high resistance and essentially **does not conduct**, so the output across R_L is
practically **zero**.

Thus current flows through the load in **one direction only**, during **alternate half-cycles** —
the AC has been rectified, though only half of each cycle is used.

**Waveforms:**

```
  INPUT (AC)
                        ╱‾╲       ╱‾╲       ╱‾╲
                       ╱   ╲     ╱   ╲     ╱   ╲
                   ───┴─────┴───┴─────┴───┴─────┴────→ t
                            ╲   ╱     ╲   ╱
                             ╲_╱       ╲_╱

  OUTPUT (across R_L)
                        ╱‾╲             ╱‾╲             ╱‾╲
                       ╱   ╲           ╱   ╲           ╱   ╲
                   ───┴─────┴─────────┴─────┴─────────┴─────┴──→ t
                             (no output during the negative half-cycles)
```

**Output frequency = input frequency**, since there is one output pulse per input cycle.

**Limitations** (worth a line): only half of each cycle is used, so the efficiency is low
(about 40.6%) and the output has a large ripple. A full-wave rectifier overcomes both. ∎

### Q8 — temperature dependence of conductivity: semiconductor vs metal

**Semiconductor — conductivity increases with temperature.**

In a semiconductor the forbidden energy gap is small (≈ 1 eV). At low temperature very few electrons
have enough energy to cross it, so there are few charge carriers. As the temperature rises, more
covalent bonds are broken and **many more electron–hole pairs are created**, so the **number density
of charge carriers n increases very rapidly** (roughly exponentially).

Since σ = n e μ, this large increase in n dominates any decrease in the mobility μ, so the
**conductivity increases** — equivalently, the resistivity **falls**, and the temperature coefficient
of resistivity is **negative**.

**Metal — conductivity decreases with temperature.**

In a metal the number density n of free electrons is **essentially fixed** — it is set by the number
of atoms and does not change appreciably with temperature. But as the temperature rises the lattice
ions **vibrate more vigorously**, so the electrons **collide more frequently**, and the relaxation
time τ (and hence the mobility) **decreases**.

With n constant and τ falling, ρ = m/(ne²τ) **increases**, so the **conductivity decreases** and the
temperature coefficient of resistivity is **positive**.

**The essential contrast:** in a semiconductor the dominant effect is the **large increase in the
number of carriers**; in a metal the number of carriers is fixed and the dominant effect is the
**decrease in relaxation time**.

### Q9 — why the reverse saturation current is nearly voltage-independent

In reverse bias, the majority carriers are prevented from crossing the junction by the increased
barrier. The small reverse current is carried entirely by the **minority carriers** — the few
electrons present in the p-region and holes in the n-region, which are produced by **thermal
generation** of electron–hole pairs.

Even a small reverse voltage is enough to sweep **essentially all** of these minority carriers that
reach the junction across it. So the current is limited not by the voltage but by the **rate at which
minority carriers are thermally generated** — that is, by the **number available**, not by the force
driving them.

Increasing the reverse voltage therefore does not increase the current appreciably: the current
**saturates** at a small value, which is why it is called the **reverse saturation current**.

*(It does, however, increase markedly with **temperature**, because the rate of thermal generation of
minority carriers rises with temperature. And at a sufficiently large reverse voltage, breakdown
occurs and the current rises abruptly.)*

### Q10 — majority carriers in n-type material

An n-type semiconductor is doped with a pentavalent (donor) impurity, each atom of which contributes
a free **electron**.

**Answer: (b) electrons**

### Q11 — why the forward resistance is low and the reverse resistance high

**In forward bias** (p-side to the positive terminal), the applied field **opposes** the internal
barrier field. The barrier potential is therefore **reduced** and the **depletion region narrows**.
Once the applied voltage exceeds the knee voltage, the **majority carriers** — which are present in
very large numbers — cross the junction freely. A large current (milliamperes) flows for a small
applied voltage, so by R = V/I the **forward resistance is low** (a few ohms to a few hundred ohms).

**In reverse bias** (p-side to the negative terminal), the applied field **aids** the internal
barrier field. The barrier potential **increases** and the **depletion region widens**, so the
majority carriers cannot cross at all. Only the very few thermally generated **minority carriers**
contribute, giving a current of only microamperes even for a large applied voltage. Hence the
**reverse resistance is very high** (of the order of megohms).

**The ratio** of reverse to forward resistance is typically 10⁵ or more — and it is exactly this
asymmetry that makes the diode useful as a rectifier.

### Q12 — case study: silicon diode in a series circuit

```
      R = 200 Ω          Battery = 5 V          p-side towards the positive terminal
```

**(i) Forward or reverse biased?**

The **p-side is connected towards the positive terminal** of the battery. That is precisely the
condition for **forward bias**.

**The diode is forward biased.**

**(ii) Current in the circuit.**

In forward bias the conducting silicon diode drops a nearly constant **0.7 V** across itself. The
remaining voltage appears across the resistance:

```
      Voltage across R = 5 − 0.7 = 4.3 V
```

```
      I = 4.3/200 = 0.0215 A = 21.5 mA
```

**I = 21.5 mA**

**(iii) Current if the battery were reversed.**

The diode would then be **reverse biased**. Only the tiny **reverse saturation current** would flow —
of the order of **microamperes**, and for most purposes taken as **essentially zero**.

**I ≈ 0** (a few µA at most).

**(iv) Why a diode is a non-ohmic device.**

An **ohmic** device obeys Ohm's law: V ∝ I, so the ratio V/I — the resistance — is **constant**, and
the I–V graph is a straight line through the origin.

For a diode, the I–V characteristic is **markedly non-linear**: the current is nearly zero below the
knee voltage and then rises very steeply, and it is completely different in the reverse direction
from the forward direction. The ratio V/I is therefore **not constant** — it varies with the applied
voltage and even with its sign.

Since the diode does not obey Ohm's law, it is called a **non-ohmic** device.

### Q13 — why a semiconductor is an insulator at 0 K

At **absolute zero** there is no thermal energy available to excite electrons.

In a semiconductor the **valence band is completely full** and the **conduction band is completely
empty**, separated by a forbidden gap of about 1 eV. Conduction requires **electrons in the
conduction band** (and correspondingly holes in the valence band), because electrons in a completely
full band cannot change their state and so cannot carry a net current.

At 0 K, therefore, **no electrons can cross the gap**, the conduction band remains empty, and there
are **no free charge carriers** at all. The semiconductor consequently behaves as a **perfect
insulator**.

As the temperature rises above 0 K, thermal energy begins to break covalent bonds, creating
electron–hole pairs and hence charge carriers — which is why the conductivity of a semiconductor
increases with temperature.

---

## 5. Test yourself

Time: 40 minutes. Answers below.

1. *(1)* The forbidden energy gap of silicon is about
   (a) 0.7 eV (b) 1.1 eV (c) 3 eV (d) 6 eV
2. *(1)* In a p-type semiconductor, the majority carriers are
   (a) electrons (b) holes (c) donor ions (d) acceptor ions
3. *(1)* The output frequency of a full-wave rectifier fed with a 50 Hz input is
   (a) 25 Hz (b) 50 Hz (c) 100 Hz (d) 200 Hz
4. *(1)* Which of the following is a pentavalent dopant?
   (a) boron (b) aluminium (c) arsenic (d) indium
5. *(2)* What is a hole? How does it contribute to conduction?
6. *(2)* Name the majority and minority carriers in an n-type semiconductor. Is it electrically
   neutral?
7. *(2)* What is the barrier potential of a p-n junction? Give its approximate value for silicon and
   germanium.
8. *(2)* How does the width of the depletion region change in (i) forward bias and (ii) reverse bias?
9. *(3)* Draw the I–V characteristic of a p-n junction diode and mark the knee voltage and the
   breakdown voltage.
10. *(5)* Explain, with a circuit diagram and waveforms, the working of a half-wave rectifier. Why is
    a full-wave rectifier preferred?
11. *(3)* Distinguish between intrinsic and extrinsic semiconductors, giving three points of
    difference.
12. *(2)* A germanium diode is connected in series with a 100 Ω resistor and a 3 V battery in forward
    bias. Taking the diode drop as 0.3 V, find the current.
13. *(2)* Why is a filter capacitor used at the output of a rectifier?
14. *(2)* Explain why doping increases the conductivity of a semiconductor so dramatically.

### Answer key

**1. (b) 1.1 eV.** *(Germanium is 0.7 eV; diamond about 6 eV.)*

**2. (b) holes.**

**3. (c) 100 Hz.** The output frequency is twice the input frequency for a full-wave rectifier.

**4. (c) arsenic.** *(Boron, aluminium and indium are trivalent.)*

**5.** A **hole** is the **vacancy left in a covalent bond** when a valence electron is excited into
the conduction band. It behaves as a **positive charge carrier** of magnitude +e. It contributes to
conduction because a valence electron from a neighbouring bond can move into the vacancy, thereby
creating a new vacancy where it came from. This successive movement of valence electrons in one
direction is equivalent to the **motion of the hole in the opposite direction**, and so constitutes a
current. Holes move in the direction of the applied electric field; electrons move against it.

**6.** **Majority carriers: electrons. Minority carriers: holes.** It **is** electrically neutral —
each donor atom contributes one free electron but itself becomes a fixed positive ion, so the charges
cancel exactly. "n-type" refers only to the sign of the majority carriers.

**7.** The **barrier potential** is the potential difference developed across the depletion region of
a p-n junction, due to the layers of immobile ions on either side of the junction; it opposes further
diffusion of majority carriers, with the n-side at the higher potential.
**Si ≈ 0.7 V; Ge ≈ 0.3 V.**

**8.** (i) **Forward bias:** the applied field opposes the internal field, so the barrier is reduced
and the depletion region **narrows**. (ii) **Reverse bias:** the applied field aids the internal
field, so the barrier is increased and the depletion region **widens**.

**9.** Graph as in §4 Q4. Mark the **knee voltage** on the forward branch (0.7 V for Si, 0.3 V for Ge),
where the current starts to rise steeply, and the **breakdown voltage** on the reverse branch, where
the reverse current rises abruptly. **Label the current axis in mA for forward and µA for reverse.**

**10.** Circuit, working and waveforms as in §4 Q7.
**Why full-wave is preferred:** (i) it uses **both** half-cycles, so its **efficiency is about
81.2%** against 40.6% for half-wave; (ii) the output has a **much smaller ripple**, so it is closer
to steady DC and easier to filter; (iii) the **output frequency is twice** the input, which makes
filtering more effective still.

**11.**

| | **Intrinsic** | **Extrinsic** |
| --- | --- | --- |
| Purity | **pure** semiconductor, no added impurity | **doped** with a suitable impurity |
| Carrier concentrations | n_e = n_h = n_i | n_e ≠ n_h — one type dominates |
| Conductivity | very **low**, and depends only on temperature | much **higher**, and controlled by the doping level |

**12. 27 mA.** Voltage across R = 3 − 0.3 = 2.7 V. I = 2.7/100 = 0.027 A = **27 mA**.

**13.** The output of a rectifier is unidirectional but **pulsating**, not steady DC. A capacitor
connected **in parallel with the load** **charges up** to the peak voltage during each pulse and then
**discharges slowly through the load** during the gaps between pulses. This maintains the output
voltage between pulses and so greatly **reduces the ripple**, producing an output much closer to
steady DC.

**14.** In an intrinsic semiconductor the carrier concentration n_i is very small, because an electron
must be excited across a gap of about 1 eV to become free — and only a tiny fraction have that much
thermal energy at room temperature. **Doping supplies charge carriers that need almost no energy to
become free**: a pentavalent donor's fifth electron is only very loosely bound (about 0.01 eV below
the conduction band), and a trivalent acceptor creates a hole directly. So even a doping level of one
part in 10⁶ adds vastly more carriers than thermal excitation provides, and since σ = neμ, the
conductivity rises by orders of magnitude.

**Scoring.** Out of 29. Below 20 → this is the cheapest chapter in the paper to fix. The p-n junction
formation, the I–V characteristic and the two rectifiers cover essentially all 7 marks. Redo §3 Q1,
Q3 and Q4.

---

## 6. Answering tips

**On the rectifier questions (the likely 5-marker)**

1. **Three diagrams, three marks.** The **circuit**, the **input waveform** and the **output
   waveform**. Draw all three, and **align the output under the input** in time so the correspondence
   is visible. This is the bulk of the marks; the verbal explanation is short.

2. **For the full-wave rectifier, the transformer must be shown centre-tapped**, with the two diodes'
   p-sides at the two ends of the secondary and the load returning to the centre tap. A circuit
   without the centre tap is a different (bridge) rectifier and loses the mark.

3. **Explain both half-cycles separately**, naming which diode conducts in each and stating that the
   current through the load is in the **same direction** both times. That last clause is the point of
   the question.

4. **State the output frequency.** Full-wave: twice the input. Half-wave: same as the input. It is
   almost always an explicit sub-part.

5. **Label every diagram**: AC input, transformer, diode(s) D₁ and D₂, load resistance R_L, output.

**On the p-n junction**

6. **Give the three stages in order:** diffusion → immobile ions forming the depletion region →
   barrier potential → equilibrium when diffusion and drift currents balance. Four named steps.

7. **Say which ions are on which side** — negative acceptor ions on the p-side, positive donor ions
   on the n-side — and that the internal field points from **n to p**. These details are marked.

8. **Quote the barrier potentials:** 0.7 V for Si, 0.3 V for Ge. Two numbers, easy marks, asked
   constantly.

9. **For forward/reverse bias, answer in terms of the barrier and the depletion width first**, then
   the current, then the carriers, then the resistance. Four consequences, in that causal order.

**On the I–V characteristic**

10. **Label the two current scales differently — mA for forward, µA for reverse.** An I–V graph with
    the same scale on both halves is wrong, and examiners look for this.

11. **Mark the knee voltage and the breakdown voltage** on the graph.

12. **When explaining the reverse branch, name the minority carriers** and say the current saturates
    because it is limited by the *number* of thermally generated carriers, not by the voltage.

13. **"Non-ohmic" means V/I is not constant** and the graph is not a straight line through the origin.
    Say both.

**On bands and doping**

14. **Draw all three band diagrams side by side** when asked to distinguish conductors,
    semiconductors and insulators, and **mark E_g** on each with its approximate value. The comparison
    is on E_g — say so explicitly.

15. **State that both n-type and p-type materials are electrically neutral**, and give the reason (the
    fixed ion balances the mobile carrier). This is the single most commonly mis-answered point in the
    chapter.

16. **For temperature questions, reason through σ = neμ.** Semiconductor: n rises steeply and
    dominates. Metal: n is fixed and τ (hence μ) falls. Naming which factor dominates is the mark.

**On priorities**

17. **This chapter is 7 marks from five topics.** If you have two days spare anywhere in your
    schedule, spend them here rather than on Magnetism and Matter or EM Waves. It is the best
    marks-per-hour trade available in the Physics syllabus.
