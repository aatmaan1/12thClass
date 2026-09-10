# Ch 3 — Current Electricity

**Units I + II (16 marks, shared with Ch 1 and Ch 2) · Typical appearance: 1–2 MCQs + one or two
2/3-mark questions + often the 5-mark drift-velocity or Wheatstone-bridge derivation. Also the
single most likely source of a Section-D case study.**

---

## 1. Scope

### In the syllabus

- Mechanism of the flow of current in conductors
- **Mobility**, **drift velocity** and its relation with electric current
- **Ohm's law**; V–I characteristics (linear and non-linear)
- Electrical **energy and power**
- Electrical **resistivity and conductivity**; **temperature dependence** of resistance
- **Internal resistance** of a cell; potential difference and **emf**
- **Combination of cells** in series and in parallel
- **Kirchhoff's rules** and their applications
- **Wheatstone bridge**

### Deleted — do not study

- **Potentiometer** — theory **and** the practical experiments (comparing emfs of two cells;
  measuring internal resistance)
- **Carbon resistors** and the resistor **colour code**

> **This is one of the biggest deletions in the syllabus.** The potentiometer was a guaranteed
> 3–5 mark question for a decade. Its weight has gone to Kirchhoff's rules, the Wheatstone bridge and
> the drift-velocity derivation. If a practice paper asks you to compare the emfs of two cells with a
> potentiometer, or to read a resistor colour code, it is an old paper.

---

## 2. Brief

### Start here — in plain English

A copper wire is full of electrons that are already moving — fast, in every direction, bouncing off
the atoms like a swarm of flies in a jar. Connect a battery and almost nothing changes about that
chaos. All that happens is that the whole swarm acquires a slight drift in one direction, a crawl of
roughly a millimetre a second on top of speeds of hundreds of kilometres a second. That crawl is the
**current**. It is the single most useful picture in this chapter, and it explains why the light
comes on instantly even though the electrons themselves are so slow: the field that starts them
drifting travels at nearly the speed of light, so every electron in the wire begins its crawl at
once.

So current I = q/t is the number of coulombs strolling past a point each second, and one ampere is
one coulomb per second. Underneath it sits I = neAv_d — number of carriers per cubic metre, times
the charge on each, times the cross-section, times the drift speed. That is just "how many pass per
second", written out.

**Why is there any resistance at all?** Because of the bouncing. An electron is accelerated by the
field, then slams into the lattice and loses what it gained, then accelerates again. The average
time between collisions is called τ, and it fixes everything: a longer τ means a freer run, a
larger drift, a bigger current, a smaller resistance. **Ohm's law**, V = IR, is not a law of nature
so much as a good description of what happens when τ does not itself depend on the voltage — true
for a metal at fixed temperature, false for a diode, false for a filament that heats up.

Distinguish **resistance** from **resistivity** and the chapter gets much easier. Resistivity ρ is
a property of the material — copper has one value, nichrome another, and no amount of cutting or
stretching changes it. Resistance R = ρl/A is a property of the *particular piece*: long and thin
means high resistance, short and fat means low, exactly like water through a pipe. Heat a metal and
ρ rises, because hotter atoms vibrate more and get in the way more often. Heat a semiconductor and ρ
*falls*, because heat shakes loose more carriers than it adds obstruction — the opposite behaviour,
and a favourite one-mark question.

A **real battery** is not a pure voltage source. It has its own internal resistance r, so the
voltage you actually get at the terminals, V = ε − Ir, sags as you draw more current. The **emf** ε
is what it would give if you drew nothing. This is why a torch dims as the cells age: r has crept up.

**Series and parallel** are worth understanding rather than memorising. In series, everything must
pass through each resistor in turn, so resistances add. In parallel, you have added extra routes, so
the total resistance must come *out lower than the smallest branch* — if that is not what your
answer says, you have made an arithmetic slip.

**Kirchhoff's two rules** cover everything the series/parallel shortcuts cannot. The junction rule
says charge does not pile up at a junction, so what flows in flows out. The loop rule says if you
walk all the way round a closed loop and return to where you started, you are back at the same
potential, so the rises and drops must cancel. Every circuit problem in the paper is those two rules
plus careful signs.

The **Wheatstone bridge** is the elegant application: four resistors in a diamond with a
galvanometer across the middle. When P/Q = R/S the two midpoints happen to sit at the same
potential, so no current flows through the galvanometer at all, whatever the battery does. That
lets you measure an unknown resistance by *balancing* rather than by reading a meter — and a null
reading is far more accurate than a deflection, because it does not depend on the meter being
calibrated.

**Learn it from someone else too**

- **Video lecture** — [search: current electricity class 12 one shot](https://www.youtube.com/results?search_query=current+electricity+class+12+physics+one+shot)
- **Interactive lessons and practice** — [Khan Academy: current electricity](https://www.khanacademy.org/search?page_search_query=current%20electricity%20class%2012)
- **The book the paper is set from** — [NCERT Physics Part I, Chapter 3 (PDF)](https://ncert.nic.in/textbook/pdf/leph103.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 32 *Electric Current in Conductors*, all of it.
  §32.2–32.4 on drift speed and the origin of resistance is the clearest short account in print;
  §32.11 onwards does Kirchhoff and the bridge.

---

### Electric current

```
      I = q/t          (steady)              I = dq/dt          (instantaneous)
```

SI unit: **ampere (A)** = C s⁻¹. Current is a **scalar** despite having a direction associated with
it. Conventional current flows from + to −, i.e. **opposite** to the electron drift.

### Drift velocity

In a metal, free electrons move randomly at high speed (~10⁵ m s⁻¹) but with **zero average
velocity**. When a field **E** is applied, they acquire a small **additional** average velocity
opposite to **E** — the **drift velocity**.

```
      v_d = (eE/m) τ
```

where τ is the **relaxation time** — the average time between successive collisions of an electron
with the lattice ions.

**Drift velocity is tiny** — typically of the order of 10⁻⁴ m s⁻¹, i.e. a fraction of a millimetre
per second. (The reason a lamp lights instantly is that the *field* is established through the wire
at nearly the speed of light, not that electrons travel from the switch to the lamp.)

### The current–drift velocity relation, and Ohm's law

**This derivation is asked almost every year. Learn it as one continuous chain.**

Consider a conductor of length l and cross-sectional area A, with n free electrons per unit volume,
each of charge e, drifting with velocity v_d.

In a time Δt, every electron travels a distance v_d Δt, so all the electrons in a volume
(A v_d Δt) cross a given cross-section. The number of such electrons is n(A v_d Δt), carrying charge

```
      Δq = n A v_d Δt · e
```

Therefore

```
      I = Δq/Δt  =  n e A v_d
```

**Now substitute the drift velocity.** With v_d = eEτ/m and E = V/l:

```
      I = n e A (eEτ/m)
        = n e A (e τ/m)(V/l)
        = ( n e² A τ / (m l) ) V
```

So

```
      V = [ m l / (n e² A τ) ] I
```

which is **Ohm's law, V = IR**, with

```
      R = m l / (n e² A τ)
```

Comparing with R = ρl/A gives the **resistivity**:

```
      ρ = m / (n e² τ)
```

> **This last step is the one students omit.** The question usually says "…and hence deduce Ohm's
> law" or "…hence obtain an expression for resistivity". Stopping at I = neAv_d loses most of the
> marks.

### Resistance, resistivity, conductivity

```
      R = ρ l / A                   ρ = resistivity, unit Ω m
      σ = 1/ρ                       conductivity, unit S m⁻¹ (or Ω⁻¹ m⁻¹)
```

**R depends on** the material (ρ), the length, the area, and the temperature.
**ρ depends on** the material and the temperature **only** — not on the dimensions. That distinction
gets asked.

**Stretching a wire.** If a wire is stretched so its length becomes n times, the volume is unchanged,
so A becomes A/n, and

```
      R′ = ρ(nl)/(A/n) = n² R
```

Resistance becomes **n² times** — a favourite MCQ.

**Current density and the microscopic Ohm's law:**

```
      J = I/A = n e v_d                       unit A m⁻²  (J is a VECTOR)
      J = σ E                                 (microscopic form of Ohm's law)
```

**Mobility** — drift velocity per unit field:

```
      μ = v_d/E = eτ/m                        unit m² V⁻¹ s⁻¹
```

and then σ = neμ.

### Temperature dependence

```
      ρ_T = ρ₀ [ 1 + α (T − T₀) ]
```

α is the **temperature coefficient of resistivity**, unit K⁻¹ (or °C⁻¹).

| Material | α | Behaviour as T increases | Reason |
| --- | --- | --- | --- |
| **Metals / conductors** | positive | ρ **increases** | n is essentially constant, but τ decreases (more vigorous lattice vibrations ⟹ more frequent collisions) |
| **Semiconductors** | negative | ρ **decreases** sharply | n increases rapidly (more electrons are thermally excited across the gap), which outweighs the fall in τ |
| **Alloys** (nichrome, manganin) | small positive | ρ nearly constant | useful for standard resistors |

**Graph — resistivity vs temperature:**

```
  ρ │           metal                       ρ │
    │          ╱                              │╲
    │        ╱                                │ ╲
    │      ╱   (nearly linear, ρ ↑)           │  ╲___     semiconductor (ρ ↓ sharply)
    │    ╱                                    │      ‾‾‾───────
    └──────────────── T                       └──────────────── T
```

Being able to draw and *explain* both curves via ρ = m/(ne²τ) is a reliable 2–3 mark question.

### V–I characteristics

- **Ohmic (linear):** a metallic conductor at constant temperature — a straight line through the
  origin, slope 1/R.
- **Non-ohmic (non-linear):** a semiconductor diode, a filament lamp (R rises with temperature), an
  electrolyte. The graph is curved, and R is not constant.

### emf, terminal potential difference and internal resistance

The **emf ε** of a cell is the potential difference across its terminals when **no current** is drawn
(the open-circuit voltage). Its **internal resistance r** is the resistance of its electrolyte.

When the cell drives a current I through an external resistance R:

```
      ε = I(R + r)                            I = ε/(R + r)
```

The **terminal potential difference** is

```
      V = ε − I r                             (discharging)
      V = ε + I r                             (while being charged)
```

So V < ε whenever current is drawn, and V = ε only when I = 0.

**From a V–I graph** of a cell: the **intercept on the V-axis is ε**, and the **magnitude of the
slope is r**. That reading is a standard 2-mark question.

### Combination of cells

**In series** (n cells, emfs εᵢ, internal resistances rᵢ):

```
      ε_eq = ε₁ + ε₂ + … + εₙ                 r_eq = r₁ + r₂ + … + rₙ
```

*(If a cell is connected with reversed polarity, its emf enters with a minus sign.)*

**In parallel** (two cells):

```
      ε_eq = (ε₁r₂ + ε₂r₁)/(r₁ + r₂)          1/r_eq = 1/r₁ + 1/r₂
```

**Which combination to use.** Series when the external resistance is **large** compared with r
(you gain voltage); parallel when the external resistance is **small** compared with r (you reduce
the total internal resistance and so can draw more current).

### Kirchhoff's rules

**Rule 1 — the junction (or current) rule.** The algebraic sum of the currents meeting at any
junction is zero: the total current entering equals the total current leaving.

```
      Σ I = 0                       — a statement of CONSERVATION OF CHARGE
```

**Rule 2 — the loop (or voltage) rule.** The algebraic sum of the changes in potential around any
closed loop is zero.

```
      Σ ΔV = 0                      — a statement of CONSERVATION OF ENERGY
```

> **Always name the conservation law each rule expresses.** "Junction rule — conservation of charge;
> loop rule — conservation of energy." That is a full mark and it is asked explicitly.

**Sign conventions for the loop rule** (fix one and use it consistently):
- Traversing a resistor **in the direction of the current**: potential change = −IR.
- Traversing a resistor **against the current**: +IR.
- Traversing a cell from **− to +**: +ε. From **+ to −**: −ε.

### Wheatstone bridge

*Circuit:* four resistances P, Q, R, S forming a quadrilateral ABCD; a galvanometer between B and D;
a cell between A and C.

The bridge is **balanced** when no current flows through the galvanometer. The balance condition is

```
      P/Q = R/S
```

**Derivation (using Kirchhoff's rules).** At balance, I_g = 0, so the current I₁ flows through P and
then Q, while I₂ flows through R and then S.

Applying the loop rule to loop ABDA (with no galvanometer current):

```
      I₁ P − I₂ R = 0          ⟹     I₁ P = I₂ R          …(i)
```

Applying the loop rule to loop BCDB:

```
      I₁ Q − I₂ S = 0          ⟹     I₁ Q = I₂ S          …(ii)
```

Dividing (i) by (ii):

```
      P/Q = R/S
```

**Why the bridge is useful:** at balance the result does not involve the emf of the cell or the
galvanometer's resistance, so an unknown resistance can be found very accurately from three known
ones. This is a **null method** — its accuracy does not depend on the sensitivity of the meter
reading, only on detecting zero.

### Metre bridge

A practical Wheatstone bridge in which two arms are replaced by a uniform 1 m resistance wire.

With the unknown R in one gap, a known resistance S in the other, and the balance point at length l
cm from one end:

```
      R/S = l/(100 − l)              ⟹     R = S · l/(100 − l)
```

**Precautions/notes that get asked:** the balance point should be near the middle of the wire (that
is where the bridge is most sensitive); the jockey should be pressed gently and briefly to avoid
altering the wire.

### Electrical power and energy

```
      P = VI = I²R = V²/R                     unit watt (W)
      Energy = Pt                             unit joule; commercially kWh (1 kWh = 3.6 × 10⁶ J)
```

**Which form to use:** I²R when the current is common (series); V²/R when the voltage is common
(parallel).

**Maximum power transfer.** The power delivered to an external resistance R by a cell of emf ε and
internal resistance r is maximum when **R = r**.

### Quick recall box

```
I = q/t = dq/dt (ampere) ;  conventional current opposite to electron drift

DRIFT:  v_d = eEτ/m  (~10⁻⁴ m s⁻¹) ;  I = n e A v_d
        Ohm's law: R = ml/(ne²Aτ)  and  ρ = m/(ne²τ)
J = I/A = n e v_d = σE  (VECTOR) ;  μ = v_d/E = eτ/m ;  σ = neμ = 1/ρ

R = ρl/A  ;  wire stretched to n times its length → R becomes n²R

ρ_T = ρ₀[1 + α(T − T₀)]
  metals: α > 0, ρ↑ (τ falls) ;  semiconductors: α < 0, ρ↓ (n rises sharply)

CELL:  ε = I(R + r) ;  V = ε − Ir  (discharging) ;  V = ε when I = 0
  V–I graph of a cell: intercept = ε, |slope| = r
  series   : ε_eq = Σεᵢ , r_eq = Σrᵢ
  parallel : ε_eq = (ε₁r₂+ε₂r₁)/(r₁+r₂) , 1/r_eq = 1/r₁+1/r₂

KIRCHHOFF: junction rule ΣI = 0  → conservation of CHARGE
           loop rule ΣΔV = 0     → conservation of ENERGY

WHEATSTONE (balanced, I_g = 0): P/Q = R/S       — a null method
METRE BRIDGE: R = S·l/(100 − l)

P = VI = I²R = V²/R ;  max power to external R when R = r
1 kWh = 3.6 × 10⁶ J
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* Define drift velocity. Derive the relation I = neAv_d for a metallic conductor,
and hence deduce Ohm's law. Obtain an expression for the resistivity of the conductor in terms of
the relaxation time.

**Q2.** *(3 marks)* State Kirchhoff's rules and name the conservation law each one expresses. Using
them, derive the balance condition of a Wheatstone bridge.

**Q3.** *(3 marks)* Explain, using ρ = m/(ne²τ), why the resistivity of a metal increases while that
of a semiconductor decreases with rising temperature. Draw both graphs.

**Q4.** *(3 marks)* Two cells of emfs ε₁ and ε₂ and internal resistances r₁ and r₂ are connected in
parallel. Derive expressions for the equivalent emf and equivalent internal resistance.

**Q5.** *(2 marks)* A cell of emf 2 V and internal resistance 0.5 Ω is connected across a 4.5 Ω
resistor. Find the current and the terminal potential difference.

**Q6.** *(2 marks)* Define mobility of a charge carrier and write its SI unit. How does it depend on
the relaxation time?

**Q7.** *(3 marks)* In a metre bridge, the balance point is found at 40 cm from the left end when a
resistance of 6 Ω is in the right gap. Find the unknown resistance in the left gap. Why is the
balance point best kept near the middle of the wire?

**Q8.** *(3 marks)* A wire of resistance R is stretched until its length is doubled. What is its new
resistance? Explain.

**Q9.** *(2 marks)* Draw the V–I graph for (i) an ohmic conductor and (ii) a semiconductor diode.
State one difference.

**Q10.** *(1 mark, MCQ)* When the temperature of a metallic conductor is increased, its resistance
(a) increases (b) decreases (c) remains the same (d) first decreases then increases

**Q11.** *(4 marks, case study)* A student measures the terminal potential difference V across a cell
for different currents I, and plots V against I. The graph is a straight line with a V-axis intercept
of 1.5 V and a slope of magnitude 0.4 V A⁻¹.
(i) What does the intercept represent?
(ii) What does the slope represent?
(iii) Write the equation of the line.
(iv) Find the current when the cell is short-circuited.

**Q12.** *(3 marks)* Using Kirchhoff's rules, find the current in each branch of the circuit below: a
10 V cell (negligible internal resistance) in series with a 2 Ω resistor feeds two parallel
resistors of 4 Ω and 6 Ω.

---

## 4. Solutions

### Q1 — drift velocity, I = neAv_d, Ohm's law and resistivity

*Diagram:* a cylindrical conductor of length l and area A, with a battery across it, an arrow showing
**E** inside, and electrons drifting opposite to **E**.

**Definition of drift velocity.** When a potential difference is applied across a conductor, the free
electrons acquire, in addition to their random thermal motion, a small **average velocity in the
direction opposite to the applied field**. This average velocity is called the **drift velocity**.

```
      v_d = (eE/m) τ
```

where τ is the relaxation time (the average time between two successive collisions).

**Derivation of I = neAv_d.**

Let the conductor have cross-sectional area A and n free electrons per unit volume, each of charge e,
drifting with speed v_d.

In a small time Δt, each electron covers a distance v_d Δt. Hence **all** the electrons contained in
a cylinder of length v_d Δt and cross-section A will cross a given plane in that time.

```
      Volume of that cylinder = A v_d Δt
      Number of electrons in it = n A v_d Δt
      Charge crossing the plane, Δq = (n A v_d Δt) e
```

Therefore

```
      I = Δq/Δt = n e A v_d
```

**Hence Ohm's law.** Substituting v_d = eEτ/m, and E = V/l for a uniform conductor:

```
      I = n e A · (eτ/m) · (V/l)
        = ( n e² A τ / m l ) V
```

Rearranging,

```
      V = [ m l / (n e² A τ) ] I
```

The bracket is a constant for a given conductor at a given temperature. So

```
      V ∝ I,     i.e.     V = I R          — Ohm's law
```

with

```
      R = m l / (n e² A τ)
```

**Resistivity.** Comparing with R = ρ l/A:

```
      ρ l/A = m l/(n e² A τ)
⟹     ρ = m / (n e² τ)
```

∎

*(Note what this expression tells you: ρ depends only on the material properties n and τ, and on
temperature through τ and n — not on the dimensions of the conductor. That is why ρ is a material
constant while R is not.)*

### Q2 — Kirchhoff's rules and the Wheatstone bridge

**Kirchhoff's rules.**

**1. Junction rule.** The algebraic sum of the currents at any junction in a circuit is zero — the
total current entering a junction equals the total current leaving it.

```
      Σ I = 0
```

This expresses the **conservation of electric charge** (charge cannot accumulate at a junction).

**2. Loop rule.** The algebraic sum of the changes in potential around any closed loop of a circuit
is zero.

```
      Σ ΔV = 0
```

This expresses the **conservation of energy** (a charge returning to its starting point must have no
net change in potential energy).

**Wheatstone bridge — balance condition.**

*Circuit:* draw the quadrilateral ABCD with P in AB, Q in BC, R in AD, S in DC; a galvanometer G
between B and D; a cell with a key between A and C.

At balance, **no current flows through the galvanometer** (I_g = 0). Hence the current I₁ entering at
A through P continues through Q, and the current I₂ through R continues through S.

**Loop ABDA** (traversing A → B → D → A). With I_g = 0 the galvanometer branch contributes nothing,
so the potential drop across P must equal that across R:

```
      I₁ P − I₂ R = 0
⟹     I₁ P = I₂ R                    …(i)
```

**Loop BCDB** (traversing B → C → D → B):

```
      I₁ Q − I₂ S = 0
⟹     I₁ Q = I₂ S                    …(ii)
```

**Dividing (i) by (ii):**

```
      (I₁ P)/(I₁ Q) = (I₂ R)/(I₂ S)
⟹     P/Q = R/S
```

This is the **balance condition of the Wheatstone bridge**. ∎

**Why it is useful.** The condition does not contain the emf of the cell or the resistance of the
galvanometer, so an unknown resistance can be determined accurately from three known ones. Being a
**null method**, its accuracy depends only on detecting zero deflection, not on the calibration of
the meter.

### Q3 — temperature dependence of resistivity, explained via ρ = m/(ne²τ)

```
      ρ = m / (n e² τ)
```

so ρ depends on the temperature only through **n** (number density of free charge carriers) and **τ**
(relaxation time).

**Metals.** The number density n of free electrons is essentially **fixed** — it is set by the number
of atoms and does not change appreciably with temperature. As T rises, the lattice ions vibrate more
vigorously, so electrons collide **more frequently**, and **τ decreases**. With n constant and τ
falling, ρ = m/(ne²τ) **increases**. Hence α > 0 for metals.

**Semiconductors.** Here n is small at low temperature, because electrons must be thermally excited
across an energy gap to become free. As T rises, **n increases very rapidly** (roughly
exponentially). τ still decreases, as in a metal, but the **increase in n dominates by far**.
Therefore ρ = m/(ne²τ) **decreases** sharply. Hence α < 0 for semiconductors.

**Graphs:**

```
   ρ │        METAL                      ρ │  SEMICONDUCTOR
     │       ╱                             │╲
     │      ╱                              │ ╲
     │     ╱     ρ increases,              │  ╲
     │    ╱      nearly linearly           │   ╲___   ρ decreases sharply
     │   ╱                                 │       ‾‾‾───────
   ρ₀●──                                   │
     └────────────────── T                 └────────────────── T
```

*(Label both axes, and mark ρ₀ on the metal graph.)*

### Q4 — two cells in parallel

*Diagram:* two cells (ε₁, r₁) and (ε₂, r₂) connected between the same two points A and B, with a
total current I leaving at B.

Let the two cells be connected between points A and B, with currents I₁ and I₂ through them, and let
the terminal potential difference between A and B be V.

**For each cell** (both discharging, driving current from A to B):

```
      V = ε₁ − I₁ r₁          ⟹     I₁ = (ε₁ − V)/r₁
      V = ε₂ − I₂ r₂          ⟹     I₂ = (ε₂ − V)/r₂
```

**By the junction rule**, the total current is

```
      I = I₁ + I₂
        = (ε₁ − V)/r₁ + (ε₂ − V)/r₂
        = (ε₁/r₁ + ε₂/r₂) − V(1/r₁ + 1/r₂)
```

Rearranging for V:

```
      V (1/r₁ + 1/r₂) = (ε₁/r₁ + ε₂/r₂) − I
```

```
      V = (ε₁/r₁ + ε₂/r₂)/(1/r₁ + 1/r₂)  −  I · 1/(1/r₁ + 1/r₂)
```

```
      V = (ε₁r₂ + ε₂r₁)/(r₁ + r₂)  −  I · [ r₁r₂/(r₁ + r₂) ]
```

Comparing with the standard single-cell form V = ε_eq − I r_eq:

```
      ε_eq = (ε₁r₂ + ε₂r₁)/(r₁ + r₂)

      r_eq = r₁r₂/(r₁ + r₂)          i.e.     1/r_eq = 1/r₁ + 1/r₂
```

∎

*(Sanity check: if the two cells are identical, ε₁ = ε₂ = ε and r₁ = r₂ = r, then ε_eq = ε and
r_eq = r/2 — the emf is unchanged but the internal resistance is halved, which is exactly why cells
are put in parallel.)*

### Q5 — current and terminal PD

```
      ε = 2 V          r = 0.5 Ω          R = 4.5 Ω
```

```
      I = ε/(R + r) = 2/(4.5 + 0.5) = 2/5 = 0.4 A
```

```
      V = ε − I r = 2 − (0.4)(0.5) = 2 − 0.2 = 1.8 V
```

**I = 0.4 A and V = 1.8 V.**

*(Check: V = IR = (0.4)(4.5) = 1.8 V ✓ — the terminal PD equals the drop across the external
resistance.)*

### Q6 — mobility

**Definition.** The **mobility** of a charge carrier is the magnitude of its drift velocity per unit
applied electric field:

```
      μ = v_d / E
```

**SI unit:** m² V⁻¹ s⁻¹.

**Dependence on relaxation time.** Since v_d = eEτ/m,

```
      μ = (eEτ/m)/E = e τ / m
```

so **mobility is directly proportional to the relaxation time τ** (and inversely proportional to the
mass of the carrier). A longer average time between collisions means a carrier can be accelerated
for longer, giving a greater drift velocity for the same field.

### Q7 — metre bridge

*Circuit:* a 1 m uniform wire AC, unknown R in the left gap, S = 6 Ω in the right gap, jockey at B
with a galvanometer.

```
      R/S = l/(100 − l)
```

with l = 40 cm and S = 6 Ω:

```
      R = S · l/(100 − l)
        = 6 × 40/(100 − 40)
        = 6 × 40/60
        = 4 Ω
```

**R = 4 Ω**

**Why the balance point should be near the middle.** The bridge is **most sensitive** when the four
resistances are of comparable magnitude, which corresponds to a balance point near the mid-point of
the wire. Near the ends, a small change in the jockey position produces only a very small change in
the ratio l/(100 − l), so the null point is hard to locate precisely and the error in R is large.
Working near the middle also minimises the effect of the **end resistances** of the wire and the
connecting strips.

### Q8 — wire stretched to double its length

*(Given: original resistance R.)*

When a wire is stretched, its **volume remains constant** (the material is conserved). Let the
original length and area be l and A; after stretching, the length is 2l and the new area is A′.

```
      Volume constant:   l A = (2l) A′
⟹     A′ = A/2
```

New resistance:

```
      R′ = ρ (2l)/(A/2) = 4 · (ρ l/A) = 4R
```

**The new resistance is 4R.**

**Explanation.** Resistance rises for **two** reasons acting together: the length doubles (R ∝ l), and
the cross-sectional area halves (R ∝ 1/A). The two effects multiply, giving a factor of 4.

*(In general, stretching to n times the length gives **n²R**.)*

### Q9 — V–I graphs

```
  (i) OHMIC CONDUCTOR              (ii) SEMICONDUCTOR DIODE
   I │        ╱                     I │              ╱
     │      ╱                         │             │
     │    ╱   straight line           │            ╱   forward bias:
     │  ╱     through origin          │        ___╱    sharp rise after
     │╱       slope = 1/R             │  ─────╯        the knee voltage
  ───●────────── V              ──────●────────────── V
     │╱                          reverse│  (tiny, almost
     │                            bias  │   constant current)
```

**One difference:** for an ohmic conductor the graph is a **straight line through the origin**, so
the ratio V/I — the resistance — is **constant**. For a diode the graph is **non-linear** and
different in forward and reverse bias, so the resistance is **not constant**; it also conducts
appreciably in only one direction.

### Q10 — resistance of a metal on heating

**Answer: (a) increases**

For a metal, n is essentially constant and τ decreases with temperature, so ρ = m/(ne²τ) increases,
and hence so does R = ρl/A.

### Q11 — case study: V–I graph of a cell

The relation between terminal potential difference and current is

```
      V = ε − I r
```

which is a straight line in V against I.

**(i) The V-axis intercept** is the value of V when I = 0, which is the **emf of the cell**.

```
      ε = 1.5 V
```

**(ii) The magnitude of the slope** is r, the **internal resistance of the cell**.

```
      r = 0.4 Ω
```

*(The slope is negative, since V falls as I rises; the magnitude is r.)*

**(iii) Equation of the line:**

```
      V = 1.5 − 0.4 I
```

**(iv) Short circuit** means the external resistance is zero, so V = 0:

```
      0 = 1.5 − 0.4 I
⟹     I = 1.5/0.4 = 3.75 A
```

**The short-circuit current is 3.75 A** — which is also just ε/r, as expected.

### Q12 — Kirchhoff's rules on a series–parallel circuit

*Circuit:* a 10 V cell (negligible internal resistance), then a 2 Ω resistor, then a parallel pair
of 4 Ω and 6 Ω, back to the cell.

**Step 1 — the parallel combination.**

```
      1/R_p = 1/4 + 1/6 = 3/12 + 2/12 = 5/12
⟹     R_p = 12/5 = 2.4 Ω
```

**Step 2 — total resistance and main current.**

```
      R_total = 2 + 2.4 = 4.4 Ω
      I = ε/R_total = 10/4.4 = 2.27 A
```

**Step 3 — potential difference across the parallel section.**

```
      V_p = I R_p = (2.27)(2.4) = 5.45 V
```

*(Equivalently, the drop across the 2 Ω resistor is (2.27)(2) = 4.55 V, and 10 − 4.55 = 5.45 V ✓ —
this is Kirchhoff's loop rule.)*

**Step 4 — branch currents** (each branch has the full 5.45 V across it, since they are in parallel):

```
      I₄ = 5.45/4 = 1.36 A
      I₆ = 5.45/6 = 0.91 A
```

*Check with the junction rule:* I₄ + I₆ = 1.36 + 0.91 = 2.27 A = I ✓

**Currents: 2.27 A through the 2 Ω resistor, 1.36 A through the 4 Ω, and 0.91 A through the 6 Ω.**

*(Note that the smaller resistance carries the larger current — in parallel, I ∝ 1/R.)*

---

## 5. Test yourself

Time: 50 minutes. Answers below.

1. *(1)* The SI unit of current density is
   (a) A (b) A m⁻² (c) A m² (d) A m⁻¹
2. *(1)* The drift velocity of electrons in a copper wire carrying a normal current is of the order of
   (a) 10⁵ m s⁻¹ (b) 10⁻⁴ m s⁻¹ (c) 10⁸ m s⁻¹ (d) 1 m s⁻¹
3. *(1)* Kirchhoff's junction rule is a statement of the conservation of
   (a) energy (b) charge (c) momentum (d) mass
4. *(2)* Define resistivity and write its SI unit. On what factors does it depend?
5. *(2)* A cell of emf 1.5 V has an internal resistance of 0.2 Ω. Find the current when it is
   short-circuited.
6. *(2)* Two resistors of 4 Ω and 6 Ω are connected (i) in series and (ii) in parallel. Find the
   equivalent resistance in each case.
7. *(3)* Derive the relation J = σE from I = neAv_d.
8. *(3)* A 100 W, 220 V bulb is connected to a 110 V supply. What power does it consume?
9. *(3)* Three cells of emf 2 V and internal resistance 0.5 Ω each are connected in series across an
   external resistance of 4.5 Ω. Find the current and the terminal PD across the combination.
10. *(5)* State Kirchhoff's rules. Apply them to find the currents in a circuit where a 6 V cell
    (r = 1 Ω) and a 4 V cell (r = 1 Ω) are connected in parallel (both driving current the same way)
    across a 5 Ω external resistance.
11. *(2)* Why is manganin used for making standard resistors?
12. *(2)* A wire of resistance 10 Ω is drawn out so that its length becomes three times. Find the new
    resistance.
13. *(3)* Explain why the terminal potential difference of a cell is less than its emf when a current
    is drawn from it, and equal to it when no current is drawn.

### Answer key

**1. (b) A m⁻².**

**2. (b) 10⁻⁴ m s⁻¹.**

**3. (b) charge.**

**4.** Resistivity is the resistance of a conductor of **unit length and unit cross-sectional area**:
ρ = RA/l. SI unit **Ω m**. It depends on the **nature of the material** and on the **temperature** —
but **not** on the dimensions of the conductor.

**5. 7.5 A.** Short circuit means R = 0, so I = ε/r = 1.5/0.2 = 7.5 A.

**6.** (i) Series: 4 + 6 = **10 Ω**. (ii) Parallel: 1/R = 1/4 + 1/6 = 5/12, R = **2.4 Ω**.

**7.** From I = neAv_d, current density J = I/A = nev_d. Substituting v_d = eEτ/m:
J = ne(eEτ/m) = (ne²τ/m)E. Since ρ = m/(ne²τ), the bracket is 1/ρ = σ. Hence **J = σE**. ∎

**8. 25 W.** The bulb's resistance R = V²/P = (220)²/100 = 484 Ω. At 110 V,
P′ = V′²/R = (110)²/484 = 12100/484 = **25 W**. *(Halving the voltage quarters the power, since
P ∝ V² at constant R.)*

**9. I = 1 A, V = 4.5 V.** Series: ε_eq = 3(2) = 6 V, r_eq = 3(0.5) = 1.5 Ω.
I = 6/(4.5 + 1.5) = 6/6 = 1 A. Terminal PD across the combination = ε_eq − I r_eq = 6 − 1.5 = **4.5 V**
(= IR ✓).

**10. I = 0.909 A through the 5 Ω; the 6 V cell supplies 1.455 A and the 4 V cell is charged at
0.545 A.**
Two cells in parallel: ε_eq = (ε₁r₂ + ε₂r₁)/(r₁ + r₂) = (6·1 + 4·1)/2 = 5 V;
r_eq = r₁r₂/(r₁ + r₂) = 1/2 = 0.5 Ω.
Total current I = 5/(5 + 0.5) = 5/5.5 = **0.909 A**.
Terminal PD V = 5 − (0.909)(0.5) = 4.545 V.
Branch currents: I₁ = (6 − 4.545)/1 = **1.455 A**; I₂ = (4 − 4.545)/1 = **−0.545 A** — negative, so the
4 V cell is actually being **charged** by the 6 V cell.
*Check:* 1.455 − 0.545 = 0.909 A ✓

**11.** Manganin has a **very small temperature coefficient of resistivity**, so its resistance stays
almost constant as it warms up during use. It also has a fairly **high resistivity**, so a compact
coil gives a usefully large resistance. Both properties are needed for a standard resistor.

**12. 90 Ω.** Stretching to n = 3 times the length gives R′ = n²R = 9(10) = 90 Ω.

**13.** When a current I is drawn, the current must also flow **through the cell's own internal
resistance r**, and this causes a potential drop Ir inside the cell. The terminal potential
difference is therefore V = ε − Ir, which is **less than ε**. When no current is drawn (I = 0), there
is no internal drop, so V = ε. This is why the emf of a cell is defined as its open-circuit terminal
potential difference.

**Scoring.** Out of 32. Below 22 → the drift-velocity chain (I = neAv_d → Ohm's law → ρ) is the
priority. Write it out from memory, in full, three times.

---

## 6. Answering tips

**On the drift-velocity derivation (the 5-marker)**

1. **Define drift velocity in words first**, then give v_d = eEτ/m. The definition is a separate mark.

2. **Show the volume-and-count argument** for I = neAv_d: the volume Av_dΔt, the number nAv_dΔt, the
   charge, then divide by Δt. Four visible steps.

3. **Do not stop at I = neAv_d.** The question always continues to Ohm's law and usually to
   resistivity. Substitute v_d and E = V/l, and finish with **R = ml/(ne²Aτ)** and **ρ = m/(ne²τ)**.
   Those last two expressions are typically 2 of the 5 marks.

4. **Define τ when you first use it** — "the relaxation time, the average time between successive
   collisions of an electron with the lattice ions".

**On Kirchhoff and Wheatstone**

5. **Name the conservation law for each rule.** Junction → charge; loop → energy. This is an explicit
   mark and takes one line.

6. **Draw the labelled circuit** with the four resistances, the galvanometer and the cell. Label the
   vertices A, B, C, D and mark the currents I₁, I₂ with arrows. It is worth a mark on its own.

7. **State "at balance, I_g = 0"** before writing the loop equations. Everything follows from it.

8. **Say why the null method is accurate:** the balance condition contains neither the emf nor the
   galvanometer resistance, so the result depends only on detecting zero deflection.

**On temperature dependence**

9. **Reason through ρ = m/(ne²τ), naming which of n and τ changes.** Metals: n constant, τ falls.
   Semiconductors: n rises sharply, dominating the fall in τ. Simply saying "metals' resistance
   increases" without the mechanism gets about half the marks.

10. **Draw both graphs with labelled axes**, and mark ρ₀ on the metal graph. Two graphs, two marks.

**On cells and circuits**

11. **Distinguish ε from V explicitly.** ε is the open-circuit value; V = ε − Ir when current flows.
    Questions are set specifically to test whether you conflate them.

12. **For a V–I graph of a cell, the intercept is ε and the slope magnitude is r.** Memorise this
    pairing — it is one of the most reliable 2-markers in the chapter, and it recurs in case studies.

13. **Check circuit answers with the junction rule.** Branch currents must add to the main current.
    Twenty seconds, and it catches most arithmetic slips.

14. **A negative branch current is a real answer, not an error** — it means you assumed the wrong
    direction, and physically that cell is being charged. Say so.

**On numericals**

15. **Choose the right power formula.** I²R when the current is common (series); V²/R when the voltage
    is common (parallel). And for a bulb operated at the wrong voltage, first find R = V_rated²/P_rated,
    then use the actual voltage.

16. **Units:** A for current, Ω for resistance, Ω m for resistivity, S m⁻¹ for conductivity,
    A m⁻² for current density, m² V⁻¹ s⁻¹ for mobility, W for power.
