# Ch 2 — Electrostatic Potential and Capacitance

**Units I + II (16 marks, shared with Ch 1 and Ch 3) · Typical appearance: 1–2 MCQs + a 2/3-mark
question on equipotentials or energy, and frequently the 5-mark capacitor-with-dielectric
derivation.**

---

## 1. Scope

### In the syllabus

- **Electric potential** and potential difference; potential due to a **point charge**, a **dipole**,
  and a **system of charges**
- **Equipotential surfaces**
- **Electric potential energy** of a system of two point charges, and of an electric **dipole** in an
  electrostatic field
- **Conductors and insulators**; free and bound charges inside a conductor
- **Dielectrics** and electric **polarisation**
- **Capacitors and capacitance**; combination in **series and parallel**
- **Capacitance of a parallel-plate capacitor**, with and without a dielectric medium
- **Energy stored** in a capacitor

### Deleted — do not study

- **Van de Graaff generator**

---

## 2. Brief

### Start here — in plain English

Lifting a bucket up a staircase takes work, and the higher you take it the more work it took. You do
not need to know the shape of the staircase — only the height. Gravity is like that, and so is
electricity. This chapter is the electrical version of "height".

Push a positive charge towards another positive charge and you have to work at it, because it fights
you the whole way. That work does not vanish; it is stored, and released the instant you let go —
the charge flies apart. **Potential energy** is the name for the stored amount. Divide it by the
charge you were pushing and you get a property of the *place* rather than of the charge:
**potential**, V, measured in volts. One volt means one joule of work per coulomb brought in from
far away. Potential is a single number at each point, not an arrow — which is exactly why it is
easier to work with than the field, and why the chapter leans on it so heavily.

The link between the two is worth memorising as a picture, not a formula: **the field points
downhill on the potential**, and the steeper the hill the stronger the field. E = −dV/dr is just
that sentence in symbols. The minus sign is the word "downhill".

An **equipotential surface** is a contour line on that hill — every point on it at the same
potential. Walk along a contour and you climb nothing, so no work is done, so the field can have no
component along it: **equipotentials and field lines always cross at right angles**. That single
fact answers a surprising number of board questions.

Now conductors. In a metal, charges are free to move, and they will keep moving as long as any
field pushes them. So once things have settled, the field *inside* must be exactly zero — otherwise
the charges would still be shuffling. Everything follows from that: all the excess charge sits on
the outer surface, the whole body is at one potential, and the field just outside meets the surface
perpendicularly. This is why a car is a safe place in a lightning storm.

**Capacitance** is the chapter's second big idea, and it is a much humbler one than it looks. Take
any two conductors, put +Q on one and −Q on the other, and a voltage V appears between them. The
ratio C = Q/V turns out to depend only on their shape and spacing, never on how much charge you
used. So C is a fixed property of the arrangement — a measure of how much charge it will swallow
per volt. A capacitor is a bucket for charge, and C is the size of the bucket.

Why does bringing the plates closer, or making them bigger, increase C? Because both make it easier
to hold the charge: more area gives the charge more room to spread out, and a smaller gap means the
opposite charge is nearby pulling it in, so less voltage builds up for the same Q. Hence
C = ε₀A/d.

Slide a slab of glass or plastic — a **dielectric** — into the gap and C goes up by a factor K. The
reason is pretty: the slab's own molecules are dipoles, and they all swing round to point against
the applied field, producing a weak field of their own that partly cancels it. Less net field means
less voltage for the same charge, which means more capacitance.

Charging a capacitor stores energy, U = ½CV², and the ½ trips people up. It is there because the
first bit of charge goes on for free while the capacitor is still empty, and the last bit has to be
forced in against everything already there. You are paying an increasing price, so the total is the
*average* price times the amount — hence one half.

**Learn it from someone else too**

- **Video lecture** — [search: electrostatic potential and capacitance class 12 one shot](https://www.youtube.com/results?search_query=electrostatic+potential+and+capacitance+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: electrostatic potential and capacitance](https://www.khanacademy.org/science/in-in-class-12th-physics-india/in-in-electrostatic-potential-and-capacitance)
- **The book the paper is set from** — [NCERT Physics Part I, Chapter 2 (PDF)](https://ncert.nic.in/textbook/pdf/leph102.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 29 §29.9–29.14 for potential, then Ch 31
  *Capacitors* entire. HC Verma's treatment of the energy stored and of the dielectric slab is
  clearer than the NCERT's; do his in-chapter examples.

---

### Electric potential

The **electric potential** at a point is the work done per unit positive charge in bringing a test
charge from infinity to that point, without acceleration.

```
      V = W/q                       SI unit: volt (V) = J C⁻¹
```

Potential is a **scalar** — this is why potential problems are easier than field problems: you add
numbers, not vectors.

**Potential difference** between A and B:

```
      V_B − V_A = W_(A→B)/q
```

**Due to a point charge q at distance r:**

```
      V = (1/4πε₀) · q/r  =  kq/r
```

Note V ∝ 1/r, whereas E ∝ 1/r². And V is **positive** for a positive charge, **negative** for a
negative one — the sign is carried, unlike with field magnitudes.

**Due to a system of charges:** the **algebraic sum** of the individual potentials:

```
      V = k ( q₁/r₁ + q₂/r₂ + q₃/r₃ + … )
```

### Potential due to a dipole

At a point at distance r from the centre, making angle θ with the dipole axis (for r >> a):

```
      V = (1/4πε₀) · p cos θ / r²
```

**Special cases:**

| Position | θ | V |
| --- | --- | --- |
| Axial (on the +q side) | 0° | kp/r² |
| Axial (on the −q side) | 180° | −kp/r² |
| **Equatorial** | 90° | **0** |

> **The equatorial potential of a dipole is zero.** This is asked directly, and it is worth
> understanding why: the two charges are equidistant from any equatorial point, so their equal and
> opposite potentials cancel exactly. (Their *fields* do not cancel, because fields are vectors and
> point in different directions.)

Note also that a dipole's potential falls as **1/r²**, faster than a point charge's 1/r.

### Relation between E and V

```
      E = −dV/dr
```

The electric field is the **negative gradient of potential** — it points in the direction of
**steepest decrease** of V. For a uniform field between plates separated by d:

```
      E = V/d
```

### Equipotential surfaces

An **equipotential surface** is a surface on which the potential is the same at every point.

**Properties (a standard 2/3-mark question):**

1. **No work is done** in moving a charge along an equipotential surface.
2. The **electric field is always perpendicular** to the equipotential surface at every point.
3. Two equipotential surfaces **never intersect** (a point cannot have two potentials).
4. They are **closer together where the field is stronger** (since E = −dV/dr, a large E means V
   changes rapidly over a short distance).
5. For a **point charge**, they are concentric spheres. For a **uniform field**, parallel planes
   perpendicular to the field. For a conductor, its **surface** is an equipotential.

**Why is no work done along an equipotential?** Because W = qΔV, and ΔV = 0 along the surface.
Equivalently, **E** is perpendicular to the displacement, so **F**·d**s** = 0.

### Potential energy

**Of two point charges** q₁ and q₂ separated by r:

```
      U = (1/4πε₀) · q₁q₂/r  =  k q₁q₂/r
```

The sign is carried: U is **positive** for like charges (work must be done to assemble them) and
**negative** for unlike charges.

**Of a system of three charges:** add the contributions of each **pair**:

```
      U = k [ q₁q₂/r₁₂ + q₂q₃/r₂₃ + q₁q₃/r₁₃ ]
```

**Of a dipole in a uniform field E:**

```
      U = −pE cos θ  =  −p · E
```

| θ | U | State |
| --- | --- | --- |
| 0° | −pE (minimum) | **stable** equilibrium |
| 90° | 0 | |
| 180° | +pE (maximum) | **unstable** equilibrium |

**Work done in rotating a dipole** from θ₁ to θ₂:

```
      W = U₂ − U₁ = pE (cos θ₁ − cos θ₂)
```

### Conductors, dielectrics and polarisation

**In a conductor** in electrostatic equilibrium: E = 0 inside, all excess charge on the outer
surface, the whole conductor at one potential, and E perpendicular to the surface just outside.
Conductors have **free charges** (mobile electrons).

**In a dielectric** the charges are **bound** — they cannot move freely, but they can be displaced
slightly. When an external field is applied:

- **Non-polar** molecules (no permanent dipole moment) develop an **induced** dipole moment.
- **Polar** molecules (with a permanent moment) **align** with the field.

Either way, the dielectric develops a net dipole moment per unit volume — the **polarisation P** —
which produces an **internal field opposing** the applied field. So the net field inside the
dielectric is reduced:

```
      E_net = E₀/K
```

where **K** is the **dielectric constant** (relative permittivity), K = ε/ε₀. K > 1 always, and
K = 1 for vacuum.

### Capacitance

A **capacitor** stores charge; its **capacitance** is

```
      C = Q/V                       SI unit: farad (F) = C V⁻¹
```

1 F is very large; practical values are μF (10⁻⁶ F) and pF (10⁻¹² F).

Capacitance depends only on the **geometry** of the conductors and the **medium** between them — not
on the charge or the voltage.

**Parallel-plate capacitor**, plate area A, separation d:

```
      C = ε₀A/d                            (vacuum or air between the plates)
      C = K ε₀A/d                          (a dielectric of constant K filling the gap)
```

**With a dielectric slab of thickness t (t < d) partly filling the gap:**

```
      C = ε₀A / ( d − t + t/K )
```

*(Check the limits: t = 0 gives ε₀A/d ✓; t = d gives Kε₀A/d ✓.)*

### Combinations of capacitors

**In series** — the same charge Q on each, and the voltages add:

```
      1/C_eq = 1/C₁ + 1/C₂ + 1/C₃ + …
```

C_eq is **smaller** than the smallest individual capacitance.

**In parallel** — the same voltage V across each, and the charges add:

```
      C_eq = C₁ + C₂ + C₃ + …
```

C_eq is **larger** than the largest individual capacitance.

> **Note the contrast with resistors:** capacitors add in *parallel* the way resistors add in
> *series*. Getting this the wrong way round is the standard error in circuit questions.

### Energy stored in a capacitor

```
      U = ½ CV²  =  ½ QV  =  Q²/(2C)
```

All three forms are equivalent by Q = CV. **Which one to use depends on what is held constant** —
see below.

**Energy density** (energy per unit volume) in the field between the plates:

```
      u = ½ ε₀ E²
```

### The dielectric-insertion table — learn this as a table

Insert a dielectric of constant K into a charged parallel-plate capacitor. There are **two cases**,
and CBSE asks them interchangeably.

**Case A — battery remains connected (V constant):**

| Quantity | Change |
| --- | --- |
| C | **increases** to KC |
| V | unchanged |
| Q = CV | **increases** to KQ |
| E = V/d | unchanged |
| U = ½CV² | **increases** to KU |

Extra charge flows from the battery, and the battery does work.

**Case B — battery disconnected (Q constant):**

| Quantity | Change |
| --- | --- |
| C | **increases** to KC |
| Q | unchanged |
| V = Q/C | **decreases** to V/K |
| E = V/d | **decreases** to E/K |
| U = Q²/2C | **decreases** to U/K |

The energy decreases because the dielectric is pulled into the gap, so the field does work on it.

> **The examiner's trick** is to give you one case and see whether you answer for the other. Read the
> question for the words "battery is disconnected" or "still connected". If the question does not
> say, state your assumption.

### Two charged capacitors connected together

When capacitors C₁ (at V₁) and C₂ (at V₂) are joined by a wire, charge redistributes until they
reach a **common potential**:

```
      V = (C₁V₁ + C₂V₂)/(C₁ + C₂)              (total charge / total capacitance)
```

There is always a **loss of energy** (dissipated as heat in the connecting wire and as radiation):

```
      ΔU = C₁C₂ (V₁ − V₂)² / [ 2(C₁ + C₂) ]
```

Note ΔU ≥ 0 always, and it is zero only if V₁ = V₂ — so energy is *always* lost unless the
potentials were already equal. That is a favourite conceptual question.

### Quick recall box

```
V = W/q  (volt = J C⁻¹) ;  V = kq/r  (SCALAR, sign carried) ;  V ∝ 1/r
System of charges : V = Σ kqᵢ/rᵢ           (algebraic sum)
Dipole : V = kp cos θ/r² ;  axial kp/r² ;  EQUATORIAL V = 0 ;  V ∝ 1/r²

E = −dV/dr ;  uniform field E = V/d

EQUIPOTENTIAL : no work done along it ; E ⊥ to it ; never intersect ;
                closer where E is stronger ; spheres for a point charge

U (two charges)   = k q₁q₂/r                (sign carried)
U (three charges) = k[q₁q₂/r₁₂ + q₂q₃/r₂₃ + q₁q₃/r₁₃]
U (dipole in E)   = −pE cos θ = −p·E
   θ = 0° : U = −pE, STABLE ;  θ = 180° : U = +pE, unstable
W (rotate θ₁→θ₂)  = pE(cos θ₁ − cos θ₂)

C = Q/V (farad)
Parallel plate : C = ε₀A/d ;  with dielectric C = Kε₀A/d
   slab of thickness t : C = ε₀A/(d − t + t/K)
Series   : 1/C = Σ1/Cᵢ    (C smaller than the smallest)
Parallel : C = ΣCᵢ        (C larger than the largest)
   — the OPPOSITE way round from resistors

U = ½CV² = ½QV = Q²/2C ;   energy density u = ½ε₀E²

DIELECTRIC INSERTED:
  battery CONNECTED    (V fixed): C↑K, Q↑K, E same, U↑K
  battery DISCONNECTED (Q fixed): C↑K, V↓K, E↓K,  U↓K

Two capacitors joined : V = (C₁V₁+C₂V₂)/(C₁+C₂)
   energy lost ΔU = C₁C₂(V₁−V₂)²/[2(C₁+C₂)]   ≥ 0 always
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* Derive an expression for the capacitance of a parallel-plate capacitor when a
dielectric slab of thickness t and dielectric constant K is inserted between the plates, which are
separated by a distance d.

**Q2.** *(3 marks)* Derive an expression for the energy stored in a parallel-plate capacitor. Hence
obtain the expression for the energy density of the electric field.

**Q3.** *(3 marks)* Define an equipotential surface. State any three of its properties. Why is no
work done in moving a charge along an equipotential surface?

**Q4.** *(3 marks)* Derive an expression for the electric potential at a point due to an electric
dipole. Hence show that the potential at any point on the equatorial line of a dipole is zero.

**Q5.** *(3 marks)* Two capacitors of capacitance 2 μF and 3 μF are connected in series across a 6 V
battery. Find (i) the equivalent capacitance, (ii) the charge on each capacitor, and (iii) the
potential difference across each.

**Q6.** *(5 marks)* A parallel-plate capacitor is charged by a battery. The battery is then
disconnected and a dielectric slab is inserted between the plates. Explain, with reasons, what
happens to (i) the capacitance, (ii) the charge, (iii) the potential difference, (iv) the electric
field, and (v) the energy stored. How would your answers change if the battery had remained
connected?

**Q7.** *(3 marks)* Two capacitors of 4 μF and 6 μF are charged to potentials of 100 V and 50 V
respectively and then connected together. Find the common potential and the loss of energy.

**Q8.** *(2 marks)* Derive an expression for the potential energy of an electric dipole placed in a
uniform electric field. When is it minimum?

**Q9.** *(2 marks)* Three charges of +2 μC, −3 μC and +4 μC are placed at the vertices of an
equilateral triangle of side 10 cm. Find the electric potential energy of the system.

**Q10.** *(1 mark, MCQ)* The capacitance of a parallel-plate capacitor is doubled if
(a) the plate separation is doubled (b) the plate area is doubled
(c) the charge is doubled (d) the voltage is doubled

**Q11.** *(4 marks, case study)* A parallel-plate capacitor has plates of area 100 cm² separated by
1 mm of air, and is connected to a 100 V supply.
(i) Find its capacitance.
(ii) Find the charge stored.
(iii) Find the energy stored.
(iv) If a dielectric of K = 5 now fills the gap while the supply remains connected, find the new
energy stored.

**Q12.** *(1 mark, Assertion–Reason)*
**A:** When two charged capacitors at different potentials are connected, energy is always lost.
**R:** Charge is conserved when capacitors are connected together.

---

## 4. Solutions

### Q1 — parallel-plate capacitor with a partial dielectric slab

*Diagram:* draw two parallel plates separated by d, with a slab of thickness t (t < d) of dielectric
constant K between them, leaving air gaps totalling (d − t).

Let the plates carry surface charge density σ = Q/A.

**The field in the air gaps.** In the region between the plates where there is no dielectric:

```
      E₀ = σ/ε₀
```

**The field inside the dielectric.** The polarised dielectric produces an opposing field, reducing
the net field by the factor K:

```
      E = E₀/K = σ/(Kε₀)
```

**The potential difference** across the plates is the sum of the potential drops across the air gaps
and the slab. The total air path has thickness (d − t) and the slab has thickness t:

```
      V = E₀ (d − t)  +  E t
        = (σ/ε₀)(d − t)  +  (σ/Kε₀) t
        = (σ/ε₀) [ (d − t) + t/K ]
```

**Substitute σ = Q/A:**

```
      V = (Q/Aε₀) [ (d − t) + t/K ]
```

**Capacitance:**

```
      C = Q/V = Q / { (Q/Aε₀)[(d − t) + t/K] }
```

```
      C = ε₀A / [ d − t + t/K ]
```

**Check the limiting cases** (worth writing — it demonstrates understanding):

- t = 0 (no slab): C = ε₀A/d ✓ — the ordinary air capacitor.
- t = d (slab fills the gap): C = ε₀A/(d/K) = **Kε₀A/d** ✓ — the fully dielectric-filled capacitor.

Since K > 1, we have t/K < t, so the denominator is smaller than d — hence **inserting a dielectric
always increases the capacitance**. ∎

### Q2 — energy stored in a capacitor, and energy density

**Derivation.** Charging a capacitor means transferring charge from one plate to the other against
the potential difference that builds up as you go. Suppose at some instant the charge is q, so the
potential difference is

```
      V′ = q/C
```

The work needed to move a further small charge dq is

```
      dW = V′ dq = (q/C) dq
```

Total work to charge the capacitor from 0 to Q:

```
      W = ∫[0,Q] (q/C) dq = (1/C) [ q²/2 ]₀^Q = Q²/(2C)
```

This work is stored as electrostatic potential energy:

```
      U = Q²/(2C)  =  ½ CV²  =  ½ QV                (using Q = CV)
```

**Energy density.** For a parallel-plate capacitor, C = ε₀A/d and V = Ed. Substituting into
U = ½CV²:

```
      U = ½ (ε₀A/d)(Ed)² = ½ ε₀ A d E²
```

The volume between the plates is (A d), so the energy per unit volume is

```
      u = U/(Ad) = ½ ε₀ E²
```

```
      Energy density  u = ½ ε₀ E²
```

This result is general — it holds for the electrostatic field anywhere, not just in a capacitor. ∎

### Q3 — equipotential surfaces

**Definition.** An equipotential surface is a surface on which the electric potential has the **same
value at every point**.

**Properties (any three):**

1. **No work** is done in moving a charge from one point to another **along** an equipotential
   surface.
2. The **electric field is always perpendicular** to the equipotential surface at every point.
3. Two equipotential surfaces **can never intersect**, since a point cannot have two different
   potentials.
4. Equipotential surfaces are **crowded together where the field is strong** and widely spaced where
   it is weak.
5. For an isolated point charge they are **concentric spheres**; for a uniform field they are
   **parallel planes** perpendicular to the field.

**Why no work is done along an equipotential surface.**

The work done in moving a charge q through a potential difference ΔV is

```
      W = q ΔV
```

Along an equipotential surface, all points have the same potential, so ΔV = 0, and therefore
**W = 0**.

Equivalently: since **E** is perpendicular to the surface, and the displacement d**s** lies *in* the
surface, the force q**E** is perpendicular to the displacement, so

```
      dW = qE · ds = qE ds cos 90° = 0
```

### Q4 — potential due to a dipole, and the equatorial case

*Diagram:* draw −q at A and +q at B, separated by 2a with centre O. Mark point P at distance r from
O, with OP making angle θ with the dipole axis OB. Drop perpendiculars from A and B onto OP.

Let the dipole have charges −q at A and +q at B, with AB = 2a and centre O. Let P be at distance r
from O, with ∠POB = θ.

**Distances.** For r >> a, dropping perpendiculars from A and B onto the line OP gives, to a good
approximation,

```
      BP ≈ r − a cos θ                AP ≈ r + a cos θ
```

**Potential at P** — the algebraic sum of the two contributions (potential is a scalar):

```
      V = k [ q/BP  +  (−q)/AP ]
        = kq [ 1/(r − a cos θ)  −  1/(r + a cos θ) ]

        = kq [ ( (r + a cos θ) − (r − a cos θ) ) / ( r² − a² cos²θ ) ]

        = kq [ 2a cos θ / (r² − a² cos²θ) ]
```

For r >> a we may neglect a²cos²θ compared with r²:

```
      V = kq (2a cos θ)/r²
```

Since p = q(2a),

```
      V = (1/4πε₀) · p cos θ / r²
```

**On the equatorial line, θ = 90°**, so cos θ = 0:

```
      V_equatorial = 0
```

**Hence the potential at every point on the equatorial line of a dipole is zero.** ∎

*(Physical reason: any equatorial point is **equidistant** from +q and −q, so their potentials — equal
in magnitude, opposite in sign — cancel exactly. Note that the *field* there is **not** zero, because
fields are vectors and the two contributions do not cancel.)*

### Q5 — two capacitors in series

```
      C₁ = 2 μF          C₂ = 3 μF          V = 6 V
```

**(i) Equivalent capacitance (series):**

```
      1/C = 1/C₁ + 1/C₂ = 1/2 + 1/3 = 5/6
⟹     C = 6/5 = 1.2 μF
```

**(ii) Charge.** In series the **same charge** flows onto each capacitor:

```
      Q = C V = (1.2 × 10⁻⁶)(6) = 7.2 × 10⁻⁶ C = 7.2 μC
```

**Both capacitors carry 7.2 μC.**

**(iii) Potential differences:**

```
      V₁ = Q/C₁ = 7.2/2 = 3.6 V
      V₂ = Q/C₂ = 7.2/3 = 2.4 V
```

*Check:* V₁ + V₂ = 3.6 + 2.4 = 6 V ✓ — equal to the supply, as it must be in series.

*(Note the smaller capacitor takes the larger share of the voltage — in series, V ∝ 1/C.)*

### Q6 — dielectric inserted, battery disconnected then connected

**Case B: battery DISCONNECTED before insertion — so Q is constant.**

**(i) Capacitance:** C′ = KC. **Increases** by the factor K, because the polarised dielectric reduces
the field for the same charge, so more charge can be held per volt.

**(ii) Charge:** **unchanged**, Q′ = Q. The capacitor is isolated — there is no path for charge to
enter or leave.

**(iii) Potential difference:** V′ = Q/C′ = Q/(KC) = **V/K**. **Decreases** by the factor K.

**(iv) Electric field:** E′ = V′/d = **E/K**. **Decreases** by the factor K, because the induced
polarisation field opposes the applied field.

**(v) Energy stored:** using the form with Q constant,

```
      U′ = Q²/(2C′) = Q²/(2KC) = U/K
```

**Decreases** by the factor K. The lost energy is accounted for by the work done by the capacitor in
**pulling the dielectric slab into** the gap.

**If the battery had remained CONNECTED — so V is constant:**

| Quantity | Battery disconnected (Q fixed) | Battery connected (V fixed) |
| --- | --- | --- |
| C | increases to KC | increases to KC |
| Q | unchanged | **increases to KQ** |
| V | decreases to V/K | **unchanged** |
| E | decreases to E/K | **unchanged** (E = V/d) |
| U | decreases to U/K | **increases to KU** (U = ½CV²) |

With the battery connected, the extra charge KQ − Q is supplied by the battery, which does work; so
the stored energy increases rather than decreasing.

> Note that the *same* physical action produces opposite changes in U depending on whether the
> battery is attached. That contrast is the whole point of the question.

### Q7 — two charged capacitors connected together

```
      C₁ = 4 μF at V₁ = 100 V          C₂ = 6 μF at V₂ = 50 V
```

**Common potential:**

```
      V = (C₁V₁ + C₂V₂)/(C₁ + C₂)
        = (4 × 100 + 6 × 50)/(4 + 6)              [in μF and volts]
        = (400 + 300)/10
        = 700/10
        = 70 V
```

**Loss of energy:**

```
      ΔU = C₁C₂ (V₁ − V₂)² / [ 2(C₁ + C₂) ]
         = (4 × 10⁻⁶)(6 × 10⁻⁶)(100 − 50)² / [ 2(10 × 10⁻⁶) ]
         = (24 × 10⁻¹²)(2500) / (20 × 10⁻⁶)
         = (6 × 10⁻⁸)/(2 × 10⁻⁵)
         = 3 × 10⁻³ J
```

**Common potential = 70 V; energy lost = 3 × 10⁻³ J = 3 mJ.**

*(Cross-check by direct computation: initial energy = ½(4μ)(100)² + ½(6μ)(50)² = 20 mJ + 7.5 mJ
= 27.5 mJ. Final energy = ½(10μ)(70)² = 24.5 mJ. Loss = 3 mJ ✓)*

This energy is dissipated as **heat in the connecting wires** (and a little as electromagnetic
radiation).

### Q8 — potential energy of a dipole in a uniform field

The potential energy of the dipole equals the work done in rotating it from a reference orientation
to the angle θ.

From [Ch 1](01-electric-charges-and-fields.md), the torque needed to hold the dipole at angle θ is
τ = pE sin θ. The small work done in rotating it through dθ against the field is

```
      dW = τ dθ = pE sin θ dθ
```

Taking the reference position as θ = 90° (where U is conventionally zero), the work done in rotating
from 90° to θ is

```
      W = ∫[90°, θ] pE sin θ′ dθ′
        = pE [ −cos θ′ ]₉₀°^θ
        = pE ( −cos θ + cos 90° )
        = −pE cos θ
```

So

```
      U = −pE cos θ  =  −p · E
```

**U is minimum** when cos θ = 1, i.e. **θ = 0°** — the dipole aligned **parallel** to the field. Then

```
      U_min = −pE
```

This is the position of **stable equilibrium**. (At θ = 180°, U = +pE is a maximum — unstable
equilibrium.) ∎

### Q9 — potential energy of three charges

*Diagram:* an equilateral triangle of side 10 cm with q₁ = +2 μC, q₂ = −3 μC, q₃ = +4 μC at the
vertices.

All three pairwise separations are equal: r = 10 cm = 0.1 m.

```
      U = k [ q₁q₂/r + q₂q₃/r + q₁q₃/r ]
        = (k/r) [ q₁q₂ + q₂q₃ + q₁q₃ ]
```

```
      q₁q₂ = (2 × 10⁻⁶)(−3 × 10⁻⁶) = −6 × 10⁻¹²
      q₂q₃ = (−3 × 10⁻⁶)(4 × 10⁻⁶) = −12 × 10⁻¹²
      q₁q₃ = (2 × 10⁻⁶)(4 × 10⁻⁶)  = +8 × 10⁻¹²
                                     ─────────────
      Sum                          = −10 × 10⁻¹² = −1 × 10⁻¹¹
```

```
      U = (9 × 10⁹/0.1)(−1 × 10⁻¹¹)
        = (9 × 10¹⁰)(−1 × 10⁻¹¹)
        = −0.9 J
```

**U = −0.9 J**

The negative sign means the system is **bound** — external work of 0.9 J would be needed to separate
the three charges to infinity.

### Q10 — when is C doubled?

C = ε₀A/d depends only on the geometry and the medium.

- Doubling d **halves** C — not (a).
- Doubling A **doubles** C ✓
- C does not depend on Q or V at all — not (c) or (d).

**Answer: (b) the plate area is doubled**

### Q11 — case study: parallel-plate capacitor

```
      A = 100 cm² = 100 × 10⁻⁴ m² = 1 × 10⁻² m²
      d = 1 mm = 1 × 10⁻³ m
      V = 100 V
```

**(i) Capacitance:**

```
      C = ε₀A/d = (8.854 × 10⁻¹²)(1 × 10⁻²)/(1 × 10⁻³)
        = (8.854 × 10⁻¹⁴)/(10⁻³)
        = 8.854 × 10⁻¹¹ F
```

**C ≈ 8.85 × 10⁻¹¹ F = 88.5 pF**

**(ii) Charge stored:**

```
      Q = CV = (8.854 × 10⁻¹¹)(100) = 8.854 × 10⁻⁹ C
```

**Q ≈ 8.85 × 10⁻⁹ C = 8.85 nC**

**(iii) Energy stored:**

```
      U = ½ CV² = ½ (8.854 × 10⁻¹¹)(100)²
        = ½ (8.854 × 10⁻¹¹)(10⁴)
        = ½ (8.854 × 10⁻⁷)
        = 4.43 × 10⁻⁷ J
```

**U ≈ 4.43 × 10⁻⁷ J**

**(iv) With K = 5 and the supply still connected.** V is constant, so C increases to KC and

```
      U′ = ½ (KC) V² = K × U = 5 × 4.43 × 10⁻⁷
```

**U′ ≈ 2.21 × 10⁻⁶ J** — five times the original energy, the extra energy being supplied by the
battery.

### Q12 — Assertion–Reason

**A:** "When two charged capacitors at different potentials are connected, energy is always lost."
**True** — the loss is ΔU = C₁C₂(V₁ − V₂)²/[2(C₁ + C₂)], which is strictly positive whenever
V₁ ≠ V₂.

**R:** "Charge is conserved when capacitors are connected together." **True** — the total charge
before and after redistribution is the same.

**Does R explain A?** **No.** Charge conservation is what lets you *calculate* the common potential,
but it is not the reason energy is lost. The energy is lost because charge flows through the
connecting wire's resistance and is dissipated as heat. Conservation of charge, on its own, does not
imply any energy loss.

**Answer: (b) Both A and R are true, but R is not the correct explanation of A.**

> This is a good example of the classic Assertion–Reason trap: two true statements, where the second
> is relevant-sounding but explains something else.

---

## 5. Test yourself

Time: 50 minutes. Answers below.

1. *(1)* The SI unit of capacitance is
   (a) volt (b) coulomb (c) farad (d) joule
2. *(1)* The potential at a point on the equatorial line of a short dipole is
   (a) kp/r² (b) 2kp/r² (c) zero (d) kp/r³
3. *(1)* Three capacitors each of 3 μF are connected in series. The equivalent capacitance is
   (a) 9 μF (b) 1 μF (c) 3 μF (d) 1/9 μF
4. *(2)* Define electric potential and write its SI unit. Is it a scalar or a vector?
5. *(2)* A 10 μF capacitor is charged to 50 V. Find the charge and the energy stored.
6. *(2)* Why does the capacitance of a parallel-plate capacitor increase when a dielectric is
   inserted?
7. *(3)* Two capacitors of 3 μF and 6 μF are connected in parallel across a 12 V battery. Find the
   equivalent capacitance, the total charge, and the charge on each.
8. *(3)* Derive the expression for the equivalent capacitance of three capacitors connected in
   series.
9. *(3)* A dipole of moment 3 × 10⁻⁸ C m is placed in a uniform field of 2 × 10⁴ N C⁻¹. Find the work
   done in rotating it from 0° to 90°, and from 0° to 180°.
10. *(5)* Derive the expression for the capacitance of a parallel-plate capacitor with air between
    the plates. A capacitor of 200 pF is charged to 200 V; the battery is then disconnected and a
    slab of K = 4 is inserted. Find the new capacitance, voltage and energy.
11. *(2)* Two charges of +q and −q are placed 2a apart. Find the potential at the midpoint of the
    line joining them, and at a point on the perpendicular bisector.
12. *(2)* Sketch equipotential surfaces for (i) a single positive point charge and (ii) a uniform
    electric field.
13. *(3)* Find the work done in bringing a charge of 2 μC from infinity to a point 30 cm from a
    charge of 5 μC.

### Answer key

**1. (c) farad.**

**2. (c) zero.**

**3. (b) 1 μF.** 1/C = 1/3 + 1/3 + 1/3 = 1, so C = 1 μF.

**4.** The electric potential at a point is the **work done per unit positive charge** in bringing a
test charge from infinity to that point without acceleration: V = W/q. SI unit **volt (V) = J C⁻¹**.
It is a **scalar**.

**5. Q = 5 × 10⁻⁴ C, U = 1.25 × 10⁻² J.** Q = CV = (10 × 10⁻⁶)(50) = 5 × 10⁻⁴ C.
U = ½CV² = ½(10 × 10⁻⁶)(2500) = 1.25 × 10⁻² J = 12.5 mJ.

**6.** The dielectric becomes **polarised**, developing an internal field that **opposes** the applied
field. The net field, and hence the potential difference V = Ed, is reduced by the factor K for the
same charge Q. Since C = Q/V, a smaller V for the same Q means a **larger C** — specifically K times
larger.

**7. C = 9 μF, Q_total = 108 μC, Q₁ = 36 μC, Q₂ = 72 μC.**
Parallel: C = 3 + 6 = 9 μF. Q_total = CV = 9 × 12 = 108 μC.
Each has the full 12 V across it: Q₁ = 3 × 12 = 36 μC; Q₂ = 6 × 12 = 72 μC. *(Sum = 108 ✓)*

**8.** In series, the same charge Q appears on each capacitor, and the applied voltage divides:
V = V₁ + V₂ + V₃. Since Vᵢ = Q/Cᵢ and V = Q/C,
Q/C = Q/C₁ + Q/C₂ + Q/C₃, and dividing by Q gives **1/C = 1/C₁ + 1/C₂ + 1/C₃**. ∎

**9. W(0°→90°) = 6 × 10⁻⁴ J; W(0°→180°) = 1.2 × 10⁻³ J.**
W = pE(cos θ₁ − cos θ₂), with pE = (3 × 10⁻⁸)(2 × 10⁴) = 6 × 10⁻⁴ J.
0° → 90°: W = 6 × 10⁻⁴(1 − 0) = 6 × 10⁻⁴ J.
0° → 180°: W = 6 × 10⁻⁴(1 − (−1)) = 1.2 × 10⁻³ J.

**10.** Derivation: for plates of area A separated by d, E = σ/ε₀ = Q/(Aε₀), and V = Ed = Qd/(Aε₀),
so **C = Q/V = ε₀A/d**.
Numerically, with the battery **disconnected** (Q constant):
C′ = KC = 4 × 200 pF = **800 pF**.
V′ = V/K = 200/4 = **50 V**.
U′ = ½C′V′² = ½(800 × 10⁻¹²)(50)² = ½(800 × 10⁻¹²)(2500) = **1 × 10⁻⁶ J**.
*(Check: U = ½(200 × 10⁻¹²)(200)² = 4 × 10⁻⁶ J, and U′ = U/K = 1 × 10⁻⁶ J ✓)*

**11. At the midpoint: V = 0. On the perpendicular bisector: V = 0.**
Midpoint: V = kq/a + k(−q)/a = 0. Perpendicular bisector: both charges are equidistant, so again the
equal and opposite potentials cancel, giving V = 0 everywhere on it.

**12.** (i) Point charge: **concentric spheres** centred on the charge, more widely spaced further
out (since V ∝ 1/r). (ii) Uniform field: **parallel planes perpendicular to the field**, equally
spaced.

**13. 0.3 J.** W = qV where V is the potential at that point due to the 5 μC charge:
V = kq/r = (9 × 10⁹)(5 × 10⁻⁶)/(0.3) = 1.5 × 10⁵ V.
W = (2 × 10⁻⁶)(1.5 × 10⁵) = 0.3 J.

**Scoring.** Out of 30. Below 21 → the two weak points are almost always (a) the dielectric-insertion
table, and (b) series-vs-parallel for capacitors. Rewrite both from memory before continuing.

---

## 6. Answering tips

**On the derivations**

1. **For the capacitor-with-slab derivation, split V into two parts explicitly:** the drop across the
   air path (d − t) and the drop across the slab t. That splitting line is the key mark.

2. **State the limiting checks** (t = 0 and t = d) at the end. It costs two lines and demonstrates
   the result is right — examiners reward it and it protects you if you made an algebra slip.

3. **For the energy derivation, show the integration.** dW = (q/C)dq, then integrate from 0 to Q.
   Writing U = ½CV² without deriving it scores only the final mark.

4. **For the dipole potential, state that potential is a scalar and therefore adds algebraically.**
   That is why you can write V = kq/BP − kq/AP directly without resolving components — it is the
   conceptual mark.

5. **Do the "for r >> a" approximation explicitly**, and say what you are neglecting.

**On the dielectric question**

6. **Identify which case you are in, in the first line:** "Since the battery is disconnected, the
   charge Q remains constant." Everything else follows from that sentence, and it is the mark the
   question is really testing.

7. **Choose the energy formula that holds the constant quantity:** U = Q²/2C when Q is fixed;
   U = ½CV² when V is fixed. Using the wrong one gives the wrong direction of change.

8. **Give a reason for each change, not just the direction.** "V decreases because Q is unchanged
   while C has increased by K" earns the mark; "V decreases" alone often does not.

9. **Present it as a table when both cases are asked.** Faster to write and easier to mark.

**On circuits**

10. **In series: same charge, voltages add. In parallel: same voltage, charges add.** Write whichever
    applies as your first line — it structures the whole answer.

11. **Check your answer adds up.** In series, V₁ + V₂ must equal the supply. In parallel,
    Q₁ + Q₂ must equal Q_total. Twenty seconds, and it catches most slips.

12. **Capacitors combine the opposite way from resistors.** If you catch yourself adding capacitances
    in series, stop.

**On numericals**

13. **Convert μF, pF, nC, cm² and mm to SI on their own line** before substituting. Note
    100 cm² = 10⁻² m², **not** 1 m² — the factor is 10⁻⁴ per cm².

14. **Keep the sign of charges in potential and potential-energy calculations.** Unlike field
    magnitudes, V and U carry signs, and the sign is part of the answer — a negative U means a bound
    system, and saying so earns the mark.

15. **Units:** F for capacitance, V for potential, J for energy, C m for dipole moment, J m⁻³ for
    energy density.
