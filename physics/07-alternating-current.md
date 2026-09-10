# Ch 7 — Alternating Current

**Units III + IV (17 marks, shared with Ch 4, 5, 6) · Typical appearance: 1–2 MCQs + a 2/3-mark
question on rms values or reactance, and — very reliably — the 5-mark series-LCR-with-phasor-diagram
question. Along with Ray Optics, this is one of the two most predictable 5-markers in the paper.**

---

## 1. Scope

### In the syllabus

- **Alternating currents**; **peak and RMS values** of alternating current/voltage
- **Reactance** and **impedance**
- **LCR series circuit** — *phasors only*
- **Resonance**
- **Power in AC circuits**; **power factor**; **wattless current**
- **Transformer** *(and the AC generator, which is covered in
  [Ch 6](06-electromagnetic-induction.md))*

### Deleted — do not study

- **LC oscillations** — the charge/current oscillation derivation and the analogy with SHM

> **Note on "phasors only".** The syllabus explicitly restricts the LCR treatment to the **phasor**
> method — you are not expected to solve the differential equation. So learn to *draw* the phasor
> diagram and read the impedance off it. This is good news: the phasor method is much shorter, and it
> is what the marking scheme wants.

---

## 2. Brief

### Start here — in plain English

The electricity in your wall socket does not flow one way. Fifty times a second it reverses, and the
voltage traces a smooth sine wave from +325 V to −325 V and back. We call the "230 V" on the label
the **rms** value, and the first thing this chapter has to explain is why we quote that odd number
instead of the peak.

The average of a sine wave over a full cycle is zero — as much above as below — so an average is
useless for describing AC. But the *heating* is not zero: a bulb does not care which way the current
goes, only how much there is, and heat goes as I². So we square the current, take the average of
that, and square-root it back. That is the root-mean-square, and it is defined precisely so that
I_rms through a resistor produces the same heat as a steady DC current of the same value. Hence
I_rms = I₀/√2, and 230 V rms is a 325 V peak.

Then the chapter's real business: what a resistor, a capacitor and an inductor each do to AC, and
they do three different things.

A **resistor** is dull, and usefully so. Voltage and current rise and fall together, in step. All
the energy delivered is dissipated as heat.

A **capacitor** cannot pass DC at all — charge just piles up on the plates and stops. But with AC
the plates are being charged and discharged fifty times a second, so current sloshes back and forth
in the wires continuously, and the faster you reverse, the easier it gets. So its opposition,
X_C = 1/ωC, *falls* as frequency rises. And the current leads the voltage by a quarter cycle: the
current has to flow first before charge can accumulate to produce a voltage.

An **inductor** is the mirror image. It happily passes DC — it is only a coil of wire — but it fights
change, so the faster you reverse the harder it resists: X_L = ωL *rises* with frequency. Here the
voltage leads the current, because the coil's emf appears in response to the current changing.

Put all three in series and you cannot simply add their oppositions, because their peaks happen at
different moments. This is why the **phasor diagram** exists: draw each voltage as an arrow whose
angle records its timing, and adding arrows handles the timing automatically. The inductor's arrow
points up, the capacitor's down, the resistor's along — so the two reactances partly cancel, and the
total is Z = √(R² + (X_L − X_C)²). That Pythagoras is a picture, not an accident.

**Resonance** is where it gets beautiful. X_L rises with frequency and X_C falls, so at exactly one
frequency they are equal and cancel completely. At that point the circuit behaves as though the
capacitor and inductor were not there — impedance drops to just R, and the current shoots up to its
maximum. That frequency is ω = 1/√(LC). It is how a radio picks one station out of the air: you
adjust C until the circuit resonates with the station you want, and every other frequency stays
small.

**Power** in AC has one trap, and the paper loves it. P = V_rms I_rms cos φ, where cos φ is the
**power factor**. Only the resistor consumes energy; a pure inductor or capacitor gives back
everything it takes, half a cycle later. So in a purely reactive circuit φ = 90°, cos φ = 0, and the
average power is exactly zero despite large currents flowing — the famous **wattless current**.

Finally the **transformer**, which is Chapter 6 put to work. Two coils on a shared iron core: the
first coil's changing current makes a changing flux, the core carries that flux to the second coil,
and the second coil sees an emf. More turns on the output side means more voltage — and,
because energy is conserved, correspondingly less current. This is why power lines run at hundreds
of thousands of volts: for the same power delivered, high voltage means low current, and heating
loss goes as I²R.

**Learn it from someone else too**

- **Video lecture** — [search: alternating current class 12 one shot](https://www.youtube.com/results?search_query=alternating+current+class+12+physics+one+shot)
- **Interactive lessons and practice** — [Khan Academy: alternating current](https://www.khanacademy.org/science/in-in-class-12th-physics-india/x51bd77206da864f3:alternating-current)
- **The book the paper is set from** — [NCERT Physics Part I, Chapter 7 (PDF)](https://ncert.nic.in/textbook/pdf/leph107.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 39 *Alternating Current*. Read §39.2 on rms
  values and §39.5–39.7 on the series circuit and resonance; his phasor treatment is the one that
  makes the √(R² + (X_L − X_C)²) obvious rather than arbitrary.

---

### Alternating current and voltage

```
      i = i₀ sin ωt                 v = v₀ sin ωt
```

where i₀, v₀ are the **peak (amplitude) values**, ω = 2πf is the angular frequency, and f is the
frequency (50 Hz in India).

### Mean and RMS values

**Mean value over a full cycle is zero** — the current spends equal time in each direction. So the
average is useless as a measure of an AC's magnitude, and this is *why* the rms value is needed.

**Mean over a half cycle:**

```
      i_mean = 2i₀/π = 0.637 i₀
```

**Root-mean-square (rms), or virtual, value.** The rms value of an alternating current is that value
of **steady direct current** which would produce the **same heating effect** in a given resistance in
the same time.

```
      i_rms = i₀/√2 = 0.707 i₀                v_rms = v₀/√2 = 0.707 v₀
```

> **Why rms and not mean.** Heating depends on i², which is positive in both half-cycles, so the
> *mean of the square* is non-zero even though the mean of i is zero. That is exactly what makes rms
> the physically meaningful measure — and it is the asked reason.

**In practice:** AC ammeters and voltmeters read **rms** values. The Indian mains "220 V" is an rms
value, so its peak is v₀ = 220√2 ≈ 311 V.

### AC through a single element

| Element | Phase relation | Opposition | Formula |
| --- | --- | --- | --- |
| **Resistor R** | current and voltage **in phase** (φ = 0) | resistance R | i₀ = v₀/R |
| **Inductor L** | current **lags** voltage by **π/2** | inductive reactance X_L | X_L = ωL = 2πfL |
| **Capacitor C** | current **leads** voltage by **π/2** | capacitive reactance X_C | X_C = 1/(ωC) = 1/(2πfC) |

**Memory hook: "CIVIL"** — in a **C**, **I** leads **V**; **V** leads **I** in an **L**.

**Frequency dependence** (asked as MCQs and graph questions):

- **X_L = ωL ∝ f.** An inductor **blocks** high frequencies and passes DC freely (at f = 0, X_L = 0).
- **X_C = 1/ωC ∝ 1/f.** A capacitor **passes** high frequencies and **blocks DC** (at f = 0,
  X_C = ∞ — this is why a capacitor in series stops DC entirely).

**Average power over a cycle in a pure inductor or a pure capacitor is ZERO**, because the phase
difference is 90° and cos 90° = 0. No net energy is consumed — energy is stored and returned each
quarter cycle.

### Series LCR circuit — the phasor method

*Phasor diagram:* draw V_R along the horizontal (in phase with the current I, drawn along the same
direction); V_L vertically **up** (leading I by 90°); V_C vertically **down** (lagging I by 90°). The
net reactive phasor is (V_L − V_C), and the resultant V is the vector sum of V_R and (V_L − V_C).

```
              V_L
               ↑
               │        V
               │      ╱
       V_L−V_C │    ╱
               │  ╱  φ
               │╱________→  V_R   (and I)
               │
               ↓
              V_C
```

Since V_R is along the current and (V_L − V_C) is perpendicular to it, the resultant applied voltage
is

```
      V = √( V_R² + (V_L − V_C)² )
```

Substituting V_R = IR, V_L = IX_L, V_C = IX_C:

```
      V = I √( R² + (X_L − X_C)² )
```

so V = IZ with the **impedance**

```
      Z = √( R² + (X_L − X_C)² )              unit: ohm
```

**Phase angle** between the applied voltage and the current:

```
      tan φ = (X_L − X_C)/R = (V_L − V_C)/V_R                cos φ = R/Z
```

**Three cases:**

| Condition | Circuit behaves as | Phase |
| --- | --- | --- |
| X_L > X_C | mainly **inductive** | voltage **leads** current (φ positive) |
| X_L < X_C | mainly **capacitive** | voltage **lags** current (φ negative) |
| X_L = X_C | purely **resistive** | voltage and current **in phase** — **resonance** |

### Resonance

At **resonance**, X_L = X_C:

```
      ω₀L = 1/(ω₀C)
⟹     ω₀ = 1/√(LC)                 f₀ = 1/(2π√(LC))
```

**At resonance:**
- **Z is minimum**, and equals R (purely resistive)
- **Current is maximum**, I_max = V/R
- **Voltage and current are in phase** (φ = 0)
- **Power factor is unity**
- The voltages across L and C are equal in magnitude and opposite in phase, so they cancel

**Graph — current vs frequency:**

```
   I │        ╱╲     ← small R : SHARP resonance, high Q
     │       ╱  ╲
     │     ╱      ╲
     │   ╱ ╱‾‾╲ ╲     ← large R : BROAD resonance, low Q
     │ ╱  ╱     ╲  ╲
     └──────────┴──────────── f
                f₀
```

A **series LCR circuit at resonance is called an acceptor circuit** — it accepts (passes a large
current at) the resonant frequency, which is the basis of radio tuning.

**Sharpness of resonance — the Q factor:**

```
      Q = ω₀L/R  =  1/(ω₀CR)  =  (1/R)√(L/C)
```

Also Q = ω₀/Δω, where Δω = R/L is the **bandwidth** (the width of the resonance curve at which the
power drops to half its maximum).

**A larger Q means a sharper resonance**, obtained by making R **small**. High Q gives better
selectivity in a tuner.

### Power in AC circuits

**Instantaneous power** varies through the cycle; what matters is the **average over a cycle**:

```
      P_avg = V_rms I_rms cos φ
```

where **cos φ is the power factor**:

```
      power factor  cos φ = R/Z
```

**Values of the power factor:**

| Circuit | cos φ | Average power |
| --- | --- | --- |
| Pure R | 1 | V_rms I_rms — maximum |
| Pure L | 0 | **zero** |
| Pure C | 0 | **zero** |
| Series LCR at resonance | 1 | V_rms I_rms |
| General LCR | R/Z | V_rms I_rms (R/Z) |

**Wattless current.** The component of the current that is **perpendicular** to the voltage phasor,
i.e. i_rms sin φ, consumes **no average power** over a cycle and is called the **wattless
(or idle) current**. In a purely inductive or purely capacitive circuit the *whole* current is
wattless.

*(The in-phase component i_rms cos φ is the part that does deliver power.)*

### Transformer

**Principle: mutual induction.** An alternating current in the primary produces a changing magnetic
flux in the core, which links the secondary and induces an alternating emf in it.

*Diagram:* a closed laminated soft-iron core; primary coil of N_p turns on one limb connected to an
AC source; secondary coil of N_s turns on the other limb connected to a load.

**Construction.** Two coils of insulated copper wire — the **primary** (N_p turns) and the
**secondary** (N_s turns) — wound on a **closed laminated soft-iron core**.

**Working and the turns relation.** The same changing flux φ links both coils, so

```
      ε_p = − N_p dφ/dt                    ε_s = − N_s dφ/dt
```

Dividing:

```
      ε_s/ε_p = N_s/N_p
```

For an **ideal (100% efficient)** transformer, power in = power out:

```
      V_p I_p = V_s I_s
```

Combining, the **transformer equations** are

```
      V_s/V_p = N_s/N_p = I_p/I_s  =  k                (the turns ratio)
```

| Type | Turns | Voltage | Current |
| --- | --- | --- | --- |
| **Step-up** | N_s > N_p | increased | decreased |
| **Step-down** | N_s < N_p | decreased | increased |

> **A transformer never "creates" energy.** Voltage is stepped up only at the cost of a
> proportionately reduced current — the power is (ideally) unchanged. Saying this explicitly is often
> a mark.

**Why a transformer will not work on DC:** a steady current produces a constant flux, and dφ/dt = 0,
so no emf is induced in the secondary. A transformer requires a **changing** flux.

**Energy losses and their remedies** — a standard 3-mark question:

| Loss | Cause | Remedy |
| --- | --- | --- |
| **Copper loss** | I²R heating in the windings | use thick copper wire of low resistance |
| **Eddy-current loss** | induced currents in the core | use a **laminated** core |
| **Hysteresis loss** | repeated magnetisation and demagnetisation of the core | use **soft iron**, which has a narrow hysteresis loop |
| **Flux leakage** | not all the primary flux links the secondary | wind the coils one over the other on a **closed** core |
| **Humming (magnetostriction)** | vibration of the core | tighten the core laminations |

**Why transformers matter — long-distance power transmission.** Power is transmitted at very **high
voltage and low current**, because the line loss is I²R: reducing I by a factor of 100 reduces the
loss by 10 000. Step-up transformers raise the voltage at the generating station, and step-down
transformers reduce it near the consumer.

### Quick recall box

```
i = i₀ sin ωt ;  ω = 2πf
mean over a full cycle = 0 ;  over a half cycle = 2i₀/π
RMS : i_rms = i₀/√2 ;  v_rms = v₀/√2       — the DC that gives the SAME HEATING
  AC meters read rms ;  220 V mains → peak 220√2 ≈ 311 V

SINGLE ELEMENTS
  R : V and I IN PHASE
  L : I LAGS V by π/2 ;  X_L = ωL = 2πfL       ∝ f   (blocks high f, passes DC)
  C : I LEADS V by π/2 ;  X_C = 1/ωC = 1/2πfC  ∝ 1/f (passes high f, BLOCKS DC)
  "CIVIL": in C, I leads V ;  V leads I in L
  average power in a pure L or pure C = ZERO

SERIES LCR (phasors)
  Z = √(R² + (X_L − X_C)²)          tan φ = (X_L − X_C)/R          cos φ = R/Z
  X_L > X_C → inductive, V leads I ;  X_L < X_C → capacitive, V lags I

RESONANCE : X_L = X_C
  ω₀ = 1/√(LC) ;  f₀ = 1/(2π√(LC))
  Z MINIMUM = R ;  I MAXIMUM = V/R ;  φ = 0 ;  power factor = 1
  Q = ω₀L/R = 1/(ω₀CR) = (1/R)√(L/C) = ω₀/Δω ,  Δω = R/L
  small R → sharp resonance, high Q       (an "acceptor" circuit)

POWER : P_avg = V_rms I_rms cos φ ;  power factor cos φ = R/Z
  wattless current = i_rms sin φ  (consumes no average power)

TRANSFORMER (mutual induction)
  V_s/V_p = N_s/N_p = I_p/I_s
  step-up: N_s > N_p, V↑ I↓ ;  step-down: N_s < N_p, V↓ I↑
  losses: copper (thick wire) ; eddy (laminated core) ; hysteresis (soft iron) ;
          flux leakage (closed core, coils wound over each other)
  will NOT work on DC (dφ/dt = 0)
  transmission at high V, low I because line loss = I²R
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* A series LCR circuit is connected to an AC source of voltage
v = v₀ sin ωt. Draw the phasor diagram and hence obtain expressions for the impedance of the circuit
and the phase angle between the voltage and the current. Under what condition is the current maximum?

**Q2.** *(3 marks)* Define the resonant frequency of a series LCR circuit and derive an expression
for it. Draw graphs of current against frequency for two different values of resistance and explain
which corresponds to a sharper resonance.

**Q3.** *(5 marks)* Draw a labelled diagram of a transformer. State its principle and working, and
derive the relation between the voltages and the number of turns. Mention any two sources of energy
loss and how each is minimised.

**Q4.** *(3 marks)* Define the rms value of an alternating current and derive its relation to the
peak value. Why is the rms value, rather than the mean value, used to specify an AC?

**Q5.** *(3 marks)* Define the power factor of an AC circuit. What is meant by wattless current? Show
that the average power consumed in a pure inductor over a complete cycle is zero.

**Q6.** *(2 marks)* An inductor of 200 mH is connected to a 220 V, 50 Hz AC source. Find the
inductive reactance and the rms current.

**Q7.** *(2 marks)* A capacitor of 100 μF is connected to a 220 V, 50 Hz supply. Find the capacitive
reactance and the rms current.

**Q8.** *(3 marks)* A series LCR circuit has R = 3 Ω, L = 25.48 mH and C = 796 μF, connected to a
230 V, 50 Hz supply. Find (i) the impedance, (ii) the current, and (iii) the power factor.

**Q9.** *(2 marks)* Explain why a capacitor blocks DC but allows AC to pass.

**Q10.** *(2 marks)* Why can a transformer not be used with a DC supply?

**Q11.** *(1 mark, MCQ)* At resonance in a series LCR circuit, the impedance is
(a) minimum and equal to R (b) maximum (c) zero (d) equal to X_L

**Q12.** *(4 marks, case study)* A step-down transformer is used to convert 2200 V AC to 220 V AC to
run a 1 kW device. Assume the transformer is 100% efficient.
(i) Find the turns ratio N_s/N_p.
(ii) Find the current in the secondary.
(iii) Find the current in the primary.
(iv) Name one energy loss in a real transformer and how it is reduced.

**Q13.** *(2 marks)* Define the quality factor of a series LCR circuit at resonance. How does it
depend on R?

---

## 4. Solutions

### Q1 — series LCR circuit: phasor diagram, impedance and phase angle

*Circuit diagram:* R, L and C in series across an AC source v = v₀ sin ωt.

*Phasor diagram:*

```
              V_L
               ↑
               │           V
               │         ╱
     (V_L−V_C) │       ╱
               │     ╱  φ
               │   ╱____________→   V_R  ,  I
               │
               ↓
              V_C
```

**Setting up.** In a series circuit the **same current** i = i₀ sin(ωt − φ) flows through all three
elements. Take the current phasor **I** along the reference (horizontal) direction. Then:

- **V_R = IR** is **in phase** with I → drawn along I
- **V_L = IX_L** **leads** I by 90° → drawn perpendicular, **upward**
- **V_C = IX_C** **lags** I by 90° → drawn perpendicular, **downward**

**Combining.** V_L and V_C are antiparallel, so their resultant is a single phasor of magnitude
|V_L − V_C| perpendicular to V_R. The applied voltage V is the vector sum of V_R and (V_L − V_C),
which are at right angles, so by Pythagoras:

```
      V = √( V_R² + (V_L − V_C)² )
```

**Substituting** V_R = IR, V_L = IX_L, V_C = IX_C:

```
      V = √( (IR)² + (IX_L − IX_C)² )
        = I √( R² + (X_L − X_C)² )
```

Comparing with V = I Z, the **impedance** is

```
      Z = √( R² + (X_L − X_C)² )              where X_L = ωL,  X_C = 1/ωC
```

**Phase angle.** From the phasor diagram, the angle φ between V and I satisfies

```
      tan φ = (V_L − V_C)/V_R = (X_L − X_C)/R
```

and

```
      cos φ = V_R/V = R/Z
```

**Condition for maximum current.** Since I = V/Z, the current is maximum when Z is **minimum**. From
Z = √(R² + (X_L − X_C)²), the minimum occurs when the reactive term vanishes:

```
      X_L = X_C
⟹     ωL = 1/(ωC)
⟹     ω = 1/√(LC)
```

This is the condition of **resonance**. At resonance Z = R (its minimum possible value), the current
is maximum at I = V/R, and the voltage and current are **in phase** (φ = 0). ∎

### Q2 — resonant frequency and sharpness of resonance

**Definition.** The **resonant frequency** of a series LCR circuit is the frequency of the applied AC
at which the **inductive and capacitive reactances become equal**, so that the impedance is minimum
and the current maximum.

**Derivation.** At resonance,

```
      X_L = X_C
⟹     ω₀ L = 1/(ω₀ C)
⟹     ω₀² = 1/(LC)
⟹     ω₀ = 1/√(LC)
```

and since ω₀ = 2πf₀,

```
      f₀ = 1/(2π √(LC))
```

**Graphs of current against frequency:**

```
   I │         ╱╲          ← R₁ (SMALL): tall, narrow peak — SHARP resonance
     │        ╱  ╲
     │       ╱    ╲
     │      ╱      ╲
     │    ╱  ╱‾‾╲   ╲      ← R₂ (LARGE): short, broad peak — flat resonance
     │  ╱  ╱      ╲   ╲
     └────────┴────────────── f
              f₀
```

Both curves peak at the **same** frequency f₀ = 1/(2π√(LC)), since f₀ does not depend on R. But:

- For **small R**, the peak current V/R is **large** and the curve is **narrow** — a **sharp**
  resonance.
- For **large R**, the peak current is smaller and the curve is **broad** — a flat resonance.

**Which is sharper, and why.** The curve for the **smaller resistance** is sharper. Quantitatively,
the sharpness is measured by the **quality factor**

```
      Q = ω₀L/R = ω₀/Δω          where Δω = R/L is the bandwidth
```

Since Q ∝ 1/R, a **smaller R gives a larger Q and hence a sharper resonance**. A sharp resonance
means the circuit responds strongly to a narrow band of frequencies, which is what makes it
**selective** — the property used to tune a radio to one station.

### Q3 — transformer

*Diagram:* a closed rectangular laminated soft-iron core; the **primary** coil of N_p turns wound on
the left limb and connected to an AC source; the **secondary** coil of N_s turns wound on the right
limb and connected to a load. Label: laminated soft-iron core, primary, secondary, AC input, output.

**Principle.** A transformer works on the principle of **mutual induction**. An alternating current
in the primary coil produces a continuously changing magnetic flux in the core; this flux links the
secondary coil and, by Faraday's law, induces an alternating emf in it.

**Construction.** Two coils of insulated copper wire — the primary (N_p turns) and the secondary
(N_s turns) — wound on a **closed, laminated, soft-iron core**. The core is closed so that almost all
the flux produced by the primary links the secondary; it is laminated to reduce eddy currents; and it
is soft iron because that has a narrow hysteresis loop.

**Working and derivation.**

Let φ be the flux through each turn of the core (assumed the same for both coils, i.e. no flux
leakage). By Faraday's law, the emf induced in each coil is

```
      ε_p = − N_p (dφ/dt)                    …(i)
      ε_s = − N_s (dφ/dt)                    …(ii)
```

Dividing (ii) by (i):

```
      ε_s/ε_p = N_s/N_p
```

For an ideal transformer with no losses, the terminal voltages equal the emfs, so

```
      V_s/V_p = N_s/N_p
```

Also, for a **100% efficient** transformer, the output power equals the input power:

```
      V_p I_p = V_s I_s
⟹     I_p/I_s = V_s/V_p = N_s/N_p
```

Hence the **transformer equations**:

```
      V_s/V_p = N_s/N_p = I_p/I_s
```

**Step-up transformer:** N_s > N_p, so V_s > V_p and I_s < I_p — the voltage is raised at the cost of
a reduced current.
**Step-down transformer:** N_s < N_p, so V_s < V_p and I_s > I_p.

**Two sources of energy loss and their remedies:**

1. **Eddy-current loss.** The changing flux induces circulating currents in the body of the iron
   core, which dissipate energy as heat. **Remedy:** use a **laminated core** — thin insulated sheets
   of iron, which break the eddy-current loops and greatly increase their resistance.

2. **Copper loss.** The currents in the primary and secondary windings dissipate energy as I²R
   heating in the wires. **Remedy:** use **thick copper wire** of low resistance for the windings.

*(Other acceptable pairs: hysteresis loss → use soft iron with a narrow hysteresis loop; flux
leakage → wind the coils one over the other on a closed core.)* ∎

### Q4 — rms value of an alternating current

**Definition.** The **rms (root-mean-square) value** of an alternating current is that value of
**steady direct current** which, flowing through a given resistance for a given time, produces the
**same amount of heat** as the alternating current does in the same resistance in the same time.

**Derivation.** Let i = i₀ sin ωt. The instantaneous power dissipated in a resistance R is

```
      P = i²R = i₀² R sin²ωt
```

The average over one complete cycle uses the average of sin²ωt, which is **½**:

```
      ⟨sin²ωt⟩ = ½
```

*(Because sin²ωt = (1 − cos 2ωt)/2, and the average of cos 2ωt over a full cycle is zero.)*

So

```
      P_avg = i₀² R × ½ = (i₀²/2) R
```

For an equivalent steady current i_rms producing the same average heating,

```
      i_rms² R = (i₀²/2) R
⟹     i_rms² = i₀²/2
⟹     i_rms = i₀/√2 = 0.707 i₀
```

Similarly v_rms = v₀/√2. ∎

**Why rms rather than mean.**

The **mean value of an alternating current over a complete cycle is zero**, because the current
flows for equal times in opposite directions and the positive and negative halves cancel exactly. So
the mean value carries no information about the magnitude of the current, and an AC meter based on it
would always read zero.

The **heating effect**, however, depends on **i²**, which is positive in **both** half-cycles.
Therefore the average of i² is not zero, and its square root — the rms value — is a genuine measure
of the current's magnitude and of the work it can do. This is why AC ammeters and voltmeters are
calibrated to read rms values, and why "220 V mains" means 220 V rms.

### Q5 — power factor, wattless current, and zero power in an inductor

**Power factor.** The average power in an AC circuit is

```
      P_avg = V_rms I_rms cos φ
```

The factor **cos φ** — where φ is the phase angle between the applied voltage and the current — is
called the **power factor** of the circuit. It equals

```
      cos φ = R/Z
```

It is the ratio of the actual average power consumed to the apparent power V_rms I_rms, and it lies
between 0 and 1.

**Wattless current.** Resolving the current phasor into components parallel and perpendicular to the
voltage phasor:

- the component I_rms cos φ, **in phase** with the voltage, delivers the power;
- the component **I_rms sin φ**, **perpendicular** to the voltage, consumes **no average power** over
  a complete cycle.

This perpendicular component is called the **wattless (or idle) current**.

**Average power in a pure inductor is zero.**

In a purely inductive circuit the current **lags** the voltage by exactly π/2. So with

```
      v = v₀ sin ωt              i = i₀ sin(ωt − π/2) = −i₀ cos ωt
```

the instantaneous power is

```
      P = v i = −v₀ i₀ sin ωt cos ωt = −(v₀ i₀/2) sin 2ωt
```

The average of sin 2ωt over a complete cycle is **zero**, so

```
      P_avg = 0
```

*(Equivalently: P_avg = V_rms I_rms cos φ with φ = 90°, and cos 90° = 0.)*

**Physical meaning.** Energy is drawn from the source and stored in the inductor's magnetic field
during one quarter of the cycle, and returned to the source during the next quarter. Over a complete
cycle there is **no net transfer of energy** — the inductor consumes no power on average. The same
argument applies to a pure capacitor, with energy stored in the electric field. ∎

### Q6 — inductive reactance and current

```
      L = 200 mH = 0.2 H          V_rms = 220 V          f = 50 Hz
```

```
      X_L = 2πfL = 2π(50)(0.2) = 2π(10) = 62.83 Ω
```

```
      I_rms = V_rms/X_L = 220/62.83 = 3.50 A
```

**X_L ≈ 62.8 Ω and I_rms ≈ 3.5 A.**

*(The current lags the voltage by 90°, and the average power consumed is zero.)*

### Q7 — capacitive reactance and current

```
      C = 100 μF = 100 × 10⁻⁶ F = 10⁻⁴ F          V_rms = 220 V          f = 50 Hz
```

```
      X_C = 1/(2πfC) = 1/[2π(50)(10⁻⁴)]
          = 1/(2π × 5 × 10⁻³)
          = 1/(3.1416 × 10⁻²)
          = 31.83 Ω
```

```
      I_rms = V_rms/X_C = 220/31.83 = 6.91 A
```

**X_C ≈ 31.8 Ω and I_rms ≈ 6.9 A.**

*(The current leads the voltage by 90°, and the average power consumed is zero.)*

### Q8 — series LCR numerical

```
      R = 3 Ω          L = 25.48 mH = 25.48 × 10⁻³ H          C = 796 μF = 796 × 10⁻⁶ F
      V_rms = 230 V    f = 50 Hz,  so ω = 2π(50) = 314.16 rad s⁻¹
```

**Reactances:**

```
      X_L = ωL = (314.16)(25.48 × 10⁻³) = 8.0 Ω

      X_C = 1/(ωC) = 1/[(314.16)(796 × 10⁻⁶)]
          = 1/(0.2501)
          = 4.0 Ω
```

**(i) Impedance:**

```
      Z = √( R² + (X_L − X_C)² )
        = √( 3² + (8.0 − 4.0)² )
        = √( 9 + 16 )
        = √25
        = 5 Ω
```

**Z = 5 Ω**

**(ii) Current:**

```
      I_rms = V_rms/Z = 230/5 = 46 A
```

**I_rms = 46 A**

**(iii) Power factor:**

```
      cos φ = R/Z = 3/5 = 0.6
```

**cos φ = 0.6**

*(Since X_L > X_C the circuit is inductive, so the voltage leads the current by
φ = cos⁻¹(0.6) = 53.1°. The average power consumed is
P = V_rms I_rms cos φ = (230)(46)(0.6) = 6348 W ≈ 6.35 kW.)*

### Q9 — why a capacitor blocks DC but passes AC

The capacitive reactance is

```
      X_C = 1/(2π f C)
```

**For DC**, the frequency f = 0, so

```
      X_C = 1/(2π × 0 × C) = ∞
```

The reactance is infinite, so no steady current can flow — the capacitor **blocks DC**. Physically,
the capacitor charges up until the voltage across it equals the applied voltage, after which the
current stops; the dielectric between the plates offers no conducting path.

**For AC**, f is non-zero and X_C = 1/(2πfC) is **finite**, and it becomes **smaller as the frequency
increases**. So the capacitor **allows AC to pass**, and the higher the frequency the more freely it
passes. Physically, the capacitor charges and discharges continuously as the polarity alternates, so
current flows back and forth in the circuit throughout — even though no charge crosses the gap
between the plates.

*(This is why capacitors are used as "blocking capacitors" to stop DC while letting an AC signal
through.)*

### Q10 — why a transformer will not work on DC

A transformer works by **mutual induction**, which requires a **changing** magnetic flux through the
secondary coil. By Faraday's law the emf induced in the secondary is

```
      ε_s = − N_s (dφ/dt)
```

If a **steady DC** is applied to the primary, the current — and hence the magnetic flux in the core —
is **constant**, so

```
      dφ/dt = 0          ⟹          ε_s = 0
```

No emf is induced in the secondary, and there is no output.

*(Worse, in practice: a DC supply would drive a large steady current through the primary, limited only
by its small resistance rather than by its reactance, which could burn out the winding.)*

### Q11 — impedance at resonance

At resonance X_L = X_C, so Z = √(R² + 0) = R, which is the smallest value Z can take.

**Answer: (a) minimum and equal to R**

### Q12 — case study: step-down transformer

```
      V_p = 2200 V          V_s = 220 V          Output power = 1 kW = 1000 W
      100% efficiency
```

**(i) Turns ratio:**

```
      N_s/N_p = V_s/V_p = 220/2200 = 1/10
```

**N_s/N_p = 1 : 10** — a step-down transformer, as expected.

**(ii) Secondary current:**

```
      P = V_s I_s
⟹     I_s = P/V_s = 1000/220 = 4.55 A
```

**I_s ≈ 4.55 A**

**(iii) Primary current.** For a 100% efficient transformer, the input power equals the output power:

```
      V_p I_p = 1000
⟹     I_p = 1000/2200 = 0.455 A
```

**I_p ≈ 0.455 A**

*(Check with the turns relation: I_p/I_s = N_s/N_p = 1/10, so I_p = I_s/10 = 0.455 A ✓ — the voltage
was stepped down by 10, so the current is stepped up by 10.)*

**(iv) One energy loss and its remedy.**

**Eddy-current loss:** the alternating flux in the iron core induces circulating currents in the body
of the core, which dissipate energy as heat. **Remedy:** use a **laminated core** made of thin
insulated iron sheets, which confines each eddy current to a thin sheet of high resistance and so
greatly reduces the loss.

*(Any of copper loss / hysteresis loss / flux leakage with its matching remedy is equally
acceptable.)*

### Q13 — quality factor

**Definition.** The **quality factor (Q factor)** of a series LCR circuit at resonance measures the
**sharpness of the resonance**. It is defined as the ratio of the resonant frequency to the bandwidth:

```
      Q = ω₀/Δω                     where Δω = R/L is the bandwidth
```

Equivalently, it is the ratio of the voltage across the inductor (or the capacitor) at resonance to
the applied voltage:

```
      Q = ω₀L/R  =  1/(ω₀CR)  =  (1/R) √(L/C)
```

**Dependence on R.** Since Q ∝ **1/R**:

- a **smaller resistance** gives a **larger Q** and hence a **sharper** resonance curve;
- a **larger resistance** gives a smaller Q and a broader, flatter resonance.

A high-Q circuit is more **selective** — it responds strongly to a narrow band of frequencies around
f₀, which is what allows a radio receiver to pick out one station from many.

---

## 5. Test yourself

Time: 50 minutes. Answers below.

1. *(1)* The rms value of an alternating current of peak value 10 A is
   (a) 10 A (b) 7.07 A (c) 14.14 A (d) 5 A
2. *(1)* In a purely capacitive AC circuit, the current
   (a) lags the voltage by π/2 (b) leads the voltage by π/2 (c) is in phase (d) is zero
3. *(1)* The average power consumed in a pure inductor over a complete cycle is
   (a) V_rms I_rms (b) ½V_rms I_rms (c) zero (d) V₀I₀
4. *(2)* An AC source of 220 V, 50 Hz is connected to a 100 Ω resistor. Find the rms current and the
   power dissipated.
5. *(2)* Define inductive reactance and capacitive reactance, and state how each depends on frequency.
6. *(2)* Find the resonant frequency of a series LCR circuit with L = 2 H and C = 32 μF.
7. *(3)* A series LCR circuit has R = 40 Ω, X_L = 60 Ω and X_C = 30 Ω. Find the impedance, the phase
   angle and the power factor.
8. *(3)* Show that the average power in an AC circuit is V_rms I_rms cos φ.
9. *(3)* An ideal step-up transformer has 100 turns in the primary and 500 turns in the secondary. If
   the primary is connected to 220 V and draws 5 A, find the secondary voltage and current.
10. *(5)* Draw the phasor diagram for a series LCR circuit and derive the expression for its
    impedance. A series LCR circuit with R = 5 Ω, L = 0.1 H and C = 100 μF is connected to a 200 V,
    50 Hz source; find the impedance and the current.
11. *(2)* Why is power transmitted over long distances at high voltage and low current?
12. *(2)* What is meant by a wattless current? In which circuit is the whole current wattless?
13. *(2)* A 60 W bulb is connected to a 220 V, 50 Hz supply. Find the peak voltage and the rms
    current.

### Answer key

**1. (b) 7.07 A.** i_rms = i₀/√2 = 10/1.414 = 7.07 A.

**2. (b) leads the voltage by π/2.**

**3. (c) zero.**

**4. I_rms = 2.2 A, P = 484 W.** I = V/R = 220/100 = 2.2 A. For a pure resistor cos φ = 1, so
P = VI = (220)(2.2) = 484 W. *(Or P = V²/R = 48400/100 = 484 W.)*

**5.** **Inductive reactance** X_L = ωL = 2πfL is the opposition offered by an inductor to AC; it is
**directly proportional to frequency**. **Capacitive reactance** X_C = 1/ωC = 1/(2πfC) is the
opposition offered by a capacitor; it is **inversely proportional to frequency**. Both are measured in
ohms.

**6. 19.9 Hz.** f₀ = 1/(2π√(LC)) = 1/(2π√(2 × 32 × 10⁻⁶)) = 1/(2π√(6.4 × 10⁻⁵))
= 1/(2π × 8 × 10⁻³) = 1/(0.0503) ≈ 19.9 Hz.

**7. Z = 50 Ω, φ = 36.9°, cos φ = 0.8.**
Z = √(40² + (60 − 30)²) = √(1600 + 900) = √2500 = 50 Ω.
tan φ = 30/40 = 0.75, so φ = 36.9°. cos φ = 40/50 = 0.8. Since X_L > X_C the circuit is inductive and
the voltage **leads** the current.

**8.** Let v = v₀ sin ωt and i = i₀ sin(ωt − φ). Then
P = vi = v₀i₀ sin ωt sin(ωt − φ) = (v₀i₀/2)[cos φ − cos(2ωt − φ)].
Averaging over a full cycle, ⟨cos(2ωt − φ)⟩ = 0, so
P_avg = (v₀i₀/2) cos φ = (v₀/√2)(i₀/√2) cos φ = **V_rms I_rms cos φ**. ∎

**9. V_s = 1100 V, I_s = 1 A.** V_s/V_p = N_s/N_p = 500/100 = 5, so V_s = 5(220) = 1100 V.
I_p/I_s = N_s/N_p = 5, so I_s = I_p/5 = 5/5 = 1 A. *(Check power: 220 × 5 = 1100 W = 1100 × 1 ✓)*

**10.** Phasor diagram and derivation as in §3 Q1, giving Z = √(R² + (X_L − X_C)²).
Numerically, ω = 2π(50) = 314.16 rad s⁻¹:
X_L = ωL = (314.16)(0.1) = 31.4 Ω; X_C = 1/(ωC) = 1/[(314.16)(10⁻⁴)] = 31.8 Ω.
Z = √(5² + (31.4 − 31.8)²) = √(25 + 0.16) = √25.16 ≈ **5.02 Ω**.
I = V/Z = 200/5.02 ≈ **39.8 A**.
*(Note X_L ≈ X_C here, so the circuit is very close to resonance and Z ≈ R — hence the large current.)*

**11.** The power lost in the transmission line is **I²R**, where R is the resistance of the line. For
a given power P = VI, transmitting at a **high voltage** means a proportionately **low current**, and
since the loss goes as I², reducing the current by a factor of 100 reduces the loss by a factor of
**10 000**. Transformers make this practical: step-up at the generating station, step-down near the
consumer.

**12.** The **wattless current** is the component of the AC current that is **perpendicular** to the
voltage phasor, i.e. I_rms sin φ; it consumes **no average power** over a complete cycle. The
**whole** current is wattless in a **purely inductive** or a **purely capacitive** circuit, where
φ = 90° and so the power factor cos φ = 0.

**13. Peak voltage ≈ 311 V; I_rms ≈ 0.27 A.**
v₀ = √2 V_rms = 1.414 × 220 = 311 V.
For a bulb (essentially resistive), P = V_rms I_rms, so I_rms = 60/220 = 0.273 A.

**Scoring.** Out of 29. Below 20 → the phasor diagram is the priority. Draw it and derive Z from
memory five times; that single derivation is worth 5 marks nearly every year.

---

## 6. Answering tips

**On the series-LCR 5-marker**

1. **Draw the phasor diagram, properly labelled.** V_R along the current, V_L up, V_C down, the
   resultant V, and the angle φ. It is worth 1–2 of the 5 marks and is marked **independently** of the
   algebra — so draw it even if you cannot finish the derivation.

2. **State that the same current flows through all three elements**, and that the current is taken as
   the reference phasor. That sentence is why the diagram is drawn the way it is.

3. **Give the phase relation for each element in words:** V_R in phase with I, V_L leads I by 90°,
   V_C lags I by 90°. Three statements, and they are marked.

4. **Show V = √(V_R² + (V_L − V_C)²) before substituting** IR, IX_L, IX_C. Then factor out I to get
   Z. Do not write Z down directly.

5. **Answer the resonance sub-part** — it is asked almost every time: current is maximum when Z is
   minimum, which needs X_L = X_C, giving ω₀ = 1/√(LC).

**On resonance and Q**

6. **Both resonance curves must peak at the same f₀.** A common error is drawing the low-R curve
   shifted sideways. R affects the *height and width*, not the position.

7. **Label the axes and mark f₀.** And label which curve is the smaller R.

8. **Say Q ∝ 1/R and what that means physically** — smaller R, sharper resonance, more selective
   circuit. The physical interpretation is the mark.

**On the transformer**

9. **The diagram must show a closed laminated core** with primary and secondary on it, labelled. A
   sketch with two unconnected coils loses the mark.

10. **Derive from ε = −N dφ/dt for each coil and then divide.** Writing V_s/V_p = N_s/N_p without the
    two Faraday equations is not a derivation.

11. **State the ideal-transformer power assumption explicitly** before using V_p I_p = V_s I_s.

12. **Pair each loss with its remedy.** Eddy → laminated core; copper → thick wire; hysteresis → soft
    iron; leakage → closed core with coils wound over each other. Marks are awarded for the pairs, so
    never list losses without remedies.

13. **Remember: a transformer does not increase power.** If asked "does a step-up transformer violate
    energy conservation?", the answer is no — the current falls in the same proportion as the voltage
    rises.

**On numericals**

14. **Compute ω = 2πf as a separate line** and use it for both reactances. Most numerical errors here
    come from putting f where ω belongs.

15. **Convert mH and μF first.** 200 mH = 0.2 H; 100 μF = 10⁻⁴ F. Note μF → F is 10⁻⁶.

16. **All AC voltages and currents quoted in a question are rms unless stated otherwise.** So a "220 V
    supply" gives I = 220/Z as an rms current. If asked for a peak value, multiply by √2.

17. **Use P = V_rms I_rms cos φ, never V_rms I_rms alone**, unless the circuit is purely resistive or
    at resonance. Omitting cos φ is the most common power-question error.
