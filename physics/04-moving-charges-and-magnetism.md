# Ch 4 — Moving Charges and Magnetism

**Units III + IV (17 marks, shared with Ch 5, 6, 7) · Typical appearance: 1–2 MCQs + a 2/3-mark
force or field question, and often a 5-marker on the circular-loop field or the moving-coil
galvanometer.**

---

## 1. Scope

### In the syllabus

- Concept of magnetic field; **Oersted's experiment**
- **Biot–Savart law** and its application to a current-carrying **circular loop**
- **Ampere's law** and its application to an **infinitely long straight wire**
- **Straight solenoid** — *qualitative treatment only*
- **Force on a moving charge** in uniform magnetic and electric fields
- **Force on a current-carrying conductor** in a uniform magnetic field
- **Force between two parallel current-carrying conductors** — definition of the **ampere**
- **Torque** on a current loop in a uniform magnetic field
- **Moving-coil galvanometer** — current sensitivity, and conversion to an **ammeter** and a
  **voltmeter**

### Deleted — do not study

- **Cyclotron** — construction, working, and the resonance-frequency derivation
- **Toroid** — the Ampere's-law application to a toroidal solenoid

> **Two notes on scope.** (i) The cyclotron was a standard 3-mark derivation for years and is now
> fully out. (ii) The solenoid is listed as **qualitative treatment only** — so know the field
> pattern and the result B = μ₀nI, but the marks are in describing and using it rather than in a
> full Ampere's-law derivation. The **long straight wire** is the application that is explicitly
> named for derivation.

---

## 2. Brief

### Start here — in plain English

In 1820 Oersted put a compass needle next to a wire, switched on the current, and the needle swung.
Nobody had expected electricity and magnetism to have anything to do with each other. That accident
is where this chapter starts: **a moving charge makes a magnetic field, and a magnetic field pushes
on a moving charge.** Everything else is detail.

Start with the push. The force on a charge moving through a magnetic field is F = qvB sin θ, and it
behaves unlike any force you have met before in two ways. First, it vanishes if the charge is
sitting still or moving straight along the field — only motion *across* the field counts. Second,
and stranger, **it is always perpendicular to the motion**. A force at right angles to velocity can
never speed anything up or slow it down; it can only bend. So a magnetic field does no work, never
changes a particle's kinetic energy, and turns a free charge into a circle. Set qvB equal to
mv²/r and you get r = mv/qB: heavier or faster particles curve wide, stronger fields curve them
tight. That is the cyclotron in one line, and the reason the time for one lap, T = 2πm/qB, does not
depend on the speed at all — which is the trick that makes a cyclotron possible.

A current-carrying wire is just a lot of moving charges, so it feels the same push, F = BIl sin θ.
This is a motor. Two parallel wires each sit in the other's field, so they attract when their
currents run the same way and repel when they oppose — and that force is how the ampere itself was
defined for over a century.

Now the other direction: what field does a current *make*? The **Biot–Savart law** is the answer,
and it is best read as the magnetic twin of Coulomb's law. A tiny piece of wire of length dl
carrying current I contributes a field that grows with I and dl, falls off as 1/r², and — the new
part — points at right angles to both the wire and the line joining it to your point. Nothing in
electrostatics behaves that way; magnetic fields curl around their source instead of pointing away
from it. Hence the right-hand rule, and hence a straight wire's field circles it, B = μ₀I/2πr, while
a loop's field threads through it, B = μ₀I/2R at the centre.

**Ampere's circuital law** is Gauss's law's counterpart, and it earns its place for the same reason:
where there is symmetry, it replaces a hard integral with a short argument. Walk a closed loop
through the field, adding up B along your path as you go, and the total depends only on how much
current your loop encircles. Choose the loop to run along the field and it collapses to one
multiplication. That gives you the long straight wire in two lines.

The **solenoid** — a long coil — is where this becomes useful. Its fields add up inside and largely
cancel outside, leaving a nearly uniform field down the middle, B = μ₀nI, that depends only on the
turns per metre. It is a bar magnet you can switch off, and it is how you make a strong controlled
field in a lab.

Last, the **moving-coil galvanometer**, which is the chapter's ideas assembled into an instrument.
A coil hangs in a radial field; a current through it feels a torque; a spring resists; the coil
stops where the two balance, so the deflection reads the current. Its two weaknesses are its two
standard questions: it is easily damaged by large currents, and it is a low-resistance device, so
you turn it into an ammeter by hanging a *small* shunt across it and into a voltmeter by putting a
*large* resistance in series. The logic is worth reasoning out each time rather than memorising —
an ammeter goes in the path of the current, so it must barely resist; a voltmeter goes across a
gap, so it must barely steal any current.

**Learn it from someone else too**

- **Video lecture** — [search: moving charges and magnetism class 12 one shot](https://www.youtube.com/results?search_query=moving+charges+and+magnetism+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: moving charges and magnetism](https://www.khanacademy.org/science/in-in-class-12th-physics-india/moving-charges-and-magnetism)
- **The book the paper is set from** — [NCERT Physics Part I, Chapter 4 (PDF)](https://ncert.nic.in/textbook/pdf/leph104.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 34 *Magnetic Field* for the force and circular
  motion, Ch 35 *Magnetic Field due to a Current* for Biot–Savart and Ampere. Do the worked examples
  in §35.4 (straight wire) and §35.6 (solenoid) before attempting the derivations.

---

### Oersted's experiment

A compass needle placed near a straight wire deflects when a current flows through the wire, and
reverses when the current reverses. **Conclusion: a current produces a magnetic field around
itself** — electricity and magnetism are linked.

### Biot–Savart law

The magnetic field d**B** at a point due to a small current element I d**l** at distance r:

```
      dB = (μ₀/4π) · (I dl sin θ)/r²
```

**Vector form:**

```
      dB = (μ₀/4π) · I (dl × r̂)/r²
```

where θ is the angle between d**l** and **r**.

```
      μ₀ = 4π × 10⁻⁷ T m A⁻¹              μ₀/4π = 10⁻⁷ T m A⁻¹
```

**Direction:** d**B** is perpendicular to the plane containing d**l** and **r**, given by the
right-hand rule.

**Note:** dB = 0 when θ = 0° or 180° (i.e. at points along the line of the current element), and is
maximum when θ = 90°.

**Comparison with Coulomb's law** (a 2-mark "compare" question):

| Similarity | Difference |
| --- | --- |
| Both are inverse-square laws | Coulomb's field is along the line joining; Biot–Savart's is perpendicular to it |
| Both obey superposition | Electrostatic field is produced by a scalar (charge); magnetic field by a vector (current element) |
| Both have a 1/4π constant | A current element cannot exist in isolation; a point charge can |

### Field on the axis of a circular current loop

**This derivation is one of the most-asked 5-markers in the chapter.**

For a circular loop of radius R carrying current I, at a point on the axis at distance x from the
centre:

```
      B = μ₀ I R² / [ 2 (R² + x²)^(3/2) ]
```

For N turns, multiply by N.

**At the centre (x = 0):**

```
      B = μ₀ N I / (2R)
```

**Far from the loop (x >> R):**

```
      B ≈ μ₀ I R²/(2x³) = μ₀ (I A)/(2π x³)          — the field of a magnetic dipole
```

**Field due to a circular arc** subtending angle θ (in radians) at the centre:

```
      B = μ₀ I θ / (4π R)
```

*(Check: for a full circle θ = 2π, giving μ₀I/2R ✓; for a semicircle θ = π, giving μ₀I/4R.)*

### Ampere's circuital law

**Statement.** The line integral of the magnetic field around any closed loop equals μ₀ times the
total current threading that loop.

```
      ∮ B · dl = μ₀ I_enclosed
```

**Application — infinitely long straight wire.**

*Amperian loop:* a **circle** of radius r, concentric with the wire and in a plane perpendicular to
it.
*Symmetry:* B is tangential to this circle and has the same magnitude everywhere on it, so
**B**·d**l** = B dl throughout.

```
      ∮ B · dl = B (2πr)          and          I_enclosed = I

      B (2πr) = μ₀ I
⟹     B = μ₀ I / (2π r)
```

So **B ∝ 1/r**, and the field lines are concentric circles around the wire, with direction given by
the **right-hand thumb rule** (thumb along the current, fingers curl in the direction of **B**).

### Solenoid (qualitative)

A long solenoid with n turns per unit length carrying current I has a **uniform** field inside,
parallel to its axis:

```
      B = μ₀ n I                    (well inside a long solenoid)
      B = μ₀ n I / 2                (at either end)
```

The field **outside** a long solenoid is very nearly **zero**. The field pattern inside resembles
that of a bar magnet, with one end acting as a north pole and the other as a south pole.

### Force on a moving charge — the magnetic Lorentz force

```
      F = q (v × B)                 magnitude:  F = q v B sin θ
```

**Key properties (each asked as a 1- or 2-marker):**

- **F = 0** when the charge is at rest (v = 0), or when **v** is **parallel** or antiparallel to **B**
  (θ = 0° or 180°).
- **F is maximum** (= qvB) when **v** ⊥ **B**.
- **F is always perpendicular to v**, so the magnetic force **does no work** on the charge and the
  **speed (and kinetic energy) never changes**. Only the direction changes.

**Circular motion when v ⊥ B.** The force provides the centripetal force:

```
      q v B = m v²/r
⟹     r = m v/(q B)  =  p/(qB)

      Time period  T = 2πm/(qB)                — independent of v and of r
      Frequency    f = qB/(2πm)
```

The independence of T from the speed is the asked fact.

**If v is at an angle θ to B**, the component v cos θ along **B** is unaffected and the component
v sin θ perpendicular to it produces circular motion — so the path is a **helix**.

**The full Lorentz force** (electric plus magnetic):

```
      F = q (E + v × B)
```

**Velocity selector.** With **E** and **B** mutually perpendicular and both perpendicular to **v**,
the electric and magnetic forces can be made to balance:

```
      qE = qvB
⟹     v = E/B
```

Only particles with exactly this speed pass through undeflected, whatever their charge or mass.

### Force on a current-carrying conductor

```
      F = I (l × B)                 magnitude:  F = B I l sin θ
```

Direction by **Fleming's left-hand rule** (forefinger = field, middle finger = current, thumb =
force) or by the cross product.

F = 0 when the conductor is **parallel** to the field; maximum when perpendicular.

### Force between two parallel current-carrying conductors, and the ampere

Two long parallel wires a distance d apart, carrying currents I₁ and I₂.

Wire 1 produces at wire 2 a field B₁ = μ₀I₁/(2πd). The force on a length l of wire 2 is

```
      F = B₁ I₂ l = μ₀ I₁ I₂ l/(2π d)
```

so the **force per unit length** is

```
      F/l = μ₀ I₁ I₂ / (2π d)
```

**Direction:** the wires **attract** when the currents are in the **same** direction, and **repel**
when they are in **opposite** directions. (Note this is the reverse of the electrostatic case for
like charges — worth remembering as a contrast.)

**Definition of the ampere.** One ampere is that current which, flowing in each of two infinitely
long, straight, parallel conductors of negligible cross-section placed 1 m apart in vacuum, produces
a force of **2 × 10⁻⁷ N per metre** of length on each conductor.

*(Check with the formula: F/l = (4π × 10⁻⁷)(1)(1)/(2π × 1) = 2 × 10⁻⁷ N m⁻¹ ✓)*

### Torque on a current loop

A rectangular loop of N turns, area A, carrying current I, in a uniform field B, with its normal at
angle θ to **B**:

```
      τ = N I A B sin θ
```

Defining the **magnetic dipole moment**

```
      m = N I A                     (a vector along the normal to the loop, unit A m²)
```

we can write

```
      τ = m × B
```

- τ is **maximum** (= NIAB) when the **plane of the coil is parallel to B** (i.e. the normal is
  perpendicular to B, θ = 90°).
- τ is **zero** when the **plane of the coil is perpendicular to B** (normal parallel to B, θ = 0°).
- The **net force** on the loop in a uniform field is **zero**.

> **The commonest error here** is confusing the angle with the *plane* of the coil and the angle with
> the *normal*. Read carefully which the question gives, and state which you are using.

### Moving-coil galvanometer

*Construction:* a coil of many turns wound on a soft-iron core, suspended (or pivoted) in a
**radial magnetic field** produced by concave pole pieces, with a phosphor-bronze suspension
providing a restoring torque, and a pointer over a scale.

**Principle.** A current-carrying coil placed in a magnetic field experiences a torque.

**Working.** The deflecting torque on the coil is NIAB. Because the field is **radial**, the plane of
the coil is always parallel to **B**, so sin θ = 1 at all deflections and the torque is NIAB
regardless of the deflection.

The suspension provides a restoring torque kφ, where k is the torsional constant and φ the
deflection. At equilibrium:

```
      N I A B = k φ
⟹     φ = (N A B/k) I
```

So **φ ∝ I** — the deflection is directly proportional to the current, which is why the scale is
linear.

**Why the field must be radial:** so that the coil's plane stays parallel to **B** at all angles,
making the torque independent of the deflection and hence the scale uniform.

**Why a soft-iron core:** it increases the magnetic flux through the coil, and hence the sensitivity;
it also makes the field more radial.

**Current sensitivity:**

```
      I_s = φ/I = N A B/k                     unit: div A⁻¹ (or rad A⁻¹)
```

**Voltage sensitivity:**

```
      V_s = φ/V = φ/(I G) = N A B/(k G)       where G is the galvanometer resistance
```

so

```
      V_s = I_s/G
```

> **A favourite conceptual question:** "Increasing the current sensitivity of a galvanometer does not
> necessarily increase its voltage sensitivity. Why?" Because increasing N increases I_s = NAB/k, but
> it also increases the length of wire and hence the coil resistance G — and V_s = I_s/G. If G rises
> in the same proportion, V_s is unchanged.

### Conversion of a galvanometer

**To an ammeter** — connect a **low resistance (shunt) S in parallel**:

```
      S = I_g G / (I − I_g)
```

where I_g is the full-scale-deflection current of the galvanometer, G its resistance, and I the
current the ammeter is to read at full scale.

An **ideal ammeter has zero resistance**, and is connected in **series** in a circuit.

**To a voltmeter** — connect a **high resistance R in series**:

```
      R = V/I_g − G
```

where V is the voltage the voltmeter is to read at full scale.

An **ideal voltmeter has infinite resistance**, and is connected in **parallel** across the component.

### Quick recall box

```
μ₀ = 4π × 10⁻⁷ T m A⁻¹ ;  μ₀/4π = 10⁻⁷

BIOT–SAVART : dB = (μ₀/4π) I dl sin θ/r² ;  vector (μ₀/4π) I (dl × r̂)/r²
  circular loop, on axis : B = μ₀IR²/[2(R²+x²)^(3/2)]
  at centre (N turns)    : B = μ₀NI/(2R)
  arc of angle θ (rad)   : B = μ₀Iθ/(4πR)

AMPERE : ∮B·dl = μ₀ I_enclosed
  long straight wire : B = μ₀I/(2πr)      B ∝ 1/r, circular field lines
  long solenoid      : B = μ₀nI inside (μ₀nI/2 at an end), ≈ 0 outside

MOVING CHARGE : F = q(v × B) = qvB sin θ
  F ⊥ v always ⟹ NO work done, speed and KE unchanged
  v ⊥ B : r = mv/(qB) ;  T = 2πm/(qB) ;  f = qB/(2πm)     — T independent of v
  v at angle θ to B : helical path
  Lorentz : F = q(E + v × B) ;  velocity selector v = E/B

CONDUCTOR : F = I(l × B) = BIl sin θ      (Fleming's left-hand rule)

PARALLEL WIRES : F/l = μ₀I₁I₂/(2πd)
  same direction → ATTRACT ;  opposite → REPEL
  ampere: 2 × 10⁻⁷ N m⁻¹ between wires 1 m apart carrying 1 A each

CURRENT LOOP : m = NIA (A m²) ;  τ = NIAB sin θ = m × B ;  net force = 0
  τ max when the PLANE of the coil is parallel to B

GALVANOMETER : NIAB = kφ ⟹ φ ∝ I ;  radial field keeps sin θ = 1 (uniform scale)
  current sensitivity I_s = NAB/k ;  voltage sensitivity V_s = NAB/(kG) = I_s/G
  → AMMETER  : shunt in PARALLEL,  S = I_g G/(I − I_g) ;  ideal R = 0, in series
  → VOLTMETER: resistance in SERIES, R = V/I_g − G ;      ideal R = ∞, in parallel
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* State the Biot–Savart law. Using it, derive an expression for the magnetic field
at a point on the axis of a circular current-carrying loop. Hence find the field at the centre.

**Q2.** *(3 marks)* State Ampere's circuital law. Use it to derive an expression for the magnetic
field due to a long straight current-carrying wire.

**Q3.** *(5 marks)* Draw a labelled diagram of a moving-coil galvanometer. State its principle and
working, and derive the relation between the deflection and the current. Why is a radial magnetic
field used?

**Q4.** *(3 marks)* Derive an expression for the force per unit length between two long parallel
current-carrying conductors. Hence define the ampere.

**Q5.** *(3 marks)* Derive an expression for the torque on a current-carrying rectangular loop in a
uniform magnetic field. When is it maximum and when zero?

**Q6.** *(2 marks)* A charged particle enters a uniform magnetic field perpendicular to it. Show that
its path is circular, and that the time period is independent of its speed.

**Q7.** *(3 marks)* How is a galvanometer converted into (i) an ammeter and (ii) a voltmeter? Derive
the required resistance in each case.

**Q8.** *(2 marks)* Why does the magnetic force do no work on a moving charged particle?

**Q9.** *(2 marks)* Two long parallel wires 20 cm apart carry currents of 5 A and 10 A in the same
direction. Find the force per unit length between them, and state whether it is attractive or
repulsive.

**Q10.** *(2 marks)* A circular coil of 50 turns and radius 5 cm carries a current of 2 A. Find the
magnetic field at its centre.

**Q11.** *(1 mark, MCQ)* The magnetic force on a charge moving parallel to a magnetic field is
(a) qvB (b) zero (c) qvB sin θ (d) maximum

**Q12.** *(4 marks, case study)* A galvanometer has a resistance of 60 Ω and gives a full-scale
deflection for a current of 1 mA.
(i) How would you convert it into an ammeter reading up to 1 A?
(ii) How would you convert it into a voltmeter reading up to 5 V?
(iii) What is the resistance of the ammeter so formed?
(iv) Why must an ammeter have a low resistance?

**Q13.** *(2 marks)* Increasing the current sensitivity of a galvanometer does not necessarily
increase its voltage sensitivity. Explain.

---

## 4. Solutions

### Q1 — Biot–Savart law and the field on the axis of a circular loop

**Statement of the Biot–Savart law.** The magnitude of the magnetic field d**B** produced at a point
P by a small current element I d**l** is

- directly proportional to the current I and to the length dl of the element,
- directly proportional to sin θ, where θ is the angle between d**l** and the line joining the
  element to P,
- inversely proportional to the square of the distance r of P from the element.

```
      dB = (μ₀/4π) · I dl sin θ / r²                 vector form:  dB = (μ₀/4π) I (dl × r̂)/r²
```

d**B** is directed perpendicular to the plane containing d**l** and **r**.

**Derivation for a circular loop.**

*Diagram:* a circular loop of radius R in the plane of the page seen edge-on, carrying current I.
P is on the axis at distance x from the centre O. Take two diametrically opposite elements d**l** at
the top and bottom. Draw the d**B** vectors from each, and resolve them into components along the
axis and perpendicular to it.

Consider a current element I d**l** on the loop. Its distance from P is

```
      r = √(R² + x²)
```

For every element on the loop, d**l** is perpendicular to **r** (the element is tangential, **r**
lies in the plane containing the axis), so θ = 90° and sin θ = 1. Hence

```
      dB = (μ₀/4π) · I dl / (R² + x²)
```

**Resolve d**B**.** d**B** is perpendicular to the plane containing d**l** and **r**, so it has:

- a component **along the axis**: dB cos α
- a component **perpendicular to the axis**: dB sin α

where α is the angle between d**B** and the axis, and from the geometry

```
      cos α = R/√(R² + x²)
```

**Now use symmetry.** For the diametrically opposite element, the perpendicular component points the
opposite way. Summing over the whole loop, **all the perpendicular components cancel in pairs**, and
only the axial components survive and add.

```
      B = ∮ dB cos α
        = ∮ (μ₀/4π) · I dl/(R² + x²) · R/√(R² + x²)

        = (μ₀ I R)/(4π (R² + x²)^(3/2)) ∮ dl
```

The integral ∮dl around the loop is its circumference, 2πR:

```
      B = (μ₀ I R)/(4π (R² + x²)^(3/2)) × 2πR
```

```
      B = μ₀ I R² / [ 2 (R² + x²)^(3/2) ]
```

For a coil of **N turns**, multiply by N:

```
      B = μ₀ N I R² / [ 2 (R² + x²)^(3/2) ]
```

**At the centre**, put x = 0:

```
      B = μ₀ N I R²/(2R³)  =  μ₀ N I/(2R)
```

The direction is along the axis, given by the **right-hand rule** (curl the fingers along the current;
the thumb gives **B**). ∎

### Q2 — Ampere's circuital law and the long straight wire

**Statement.** The line integral of the magnetic field **B** around any closed path equals μ₀ times
the total current passing through the area enclosed by that path:

```
      ∮ B · dl = μ₀ I_enclosed
```

**Derivation for a long straight wire.**

*Diagram:* a long straight vertical wire carrying current I upward, with a circle of radius r drawn
around it in a horizontal plane, and **B** shown tangential to the circle.

**Choice of Amperian loop, with justification.** Take a circle of radius r centred on the wire, lying
in a plane perpendicular to it. By the cylindrical symmetry of the problem:

- **B** has the same magnitude at every point of this circle;
- **B** is **tangential** to the circle at every point, so **B** is parallel to d**l** and
  **B**·d**l** = B dl.

Hence

```
      ∮ B · dl = B ∮ dl = B (2πr)
```

The current enclosed by the loop is I. Applying Ampere's law:

```
      B (2πr) = μ₀ I
⟹     B = μ₀ I / (2π r)
```

So **B ∝ 1/r**. The field lines are **concentric circles** around the wire, with the sense given by
the right-hand thumb rule. ∎

### Q3 — moving-coil galvanometer

*Diagram (label all of these):* a rectangular coil PQRS of N turns wound on a soft-iron core;
concave pole pieces N and S of a permanent magnet producing a radial field; a phosphor-bronze strip
suspension at the top carrying a mirror or pointer; a spring at the bottom; the scale.

**Principle.** A current-carrying coil placed in a magnetic field experiences a **torque**.

**Working.** Let the coil have N turns, area A, and carry current I in a radial field of magnitude B.

The **deflecting torque** on the coil is

```
      τ_deflecting = N I A B sin θ
```

Because the field produced by the concave pole pieces is **radial**, the plane of the coil is always
**parallel to B** whatever the deflection, so θ = 90° and sin θ = 1 throughout. Hence

```
      τ_deflecting = N I A B
```

The suspension provides a **restoring torque** proportional to the deflection φ:

```
      τ_restoring = k φ
```

where k is the torsional constant of the suspension.

At equilibrium the two torques balance:

```
      N I A B = k φ
```

```
      φ = (N A B / k) I                    i.e.     φ ∝ I
```

**The deflection is directly proportional to the current**, which is why the galvanometer has a
**uniform (linear) scale**.

**Why a radial magnetic field?** So that the plane of the coil remains parallel to **B** at every
deflection. This keeps sin θ = 1, making the deflecting torque independent of the deflection, and
hence making φ strictly proportional to I — giving a **linear scale**. Without a radial field the
scale would be non-uniform.

**Why a soft-iron core?** It concentrates the magnetic flux through the coil, increasing B and hence
the sensitivity, and it also helps make the field radial. ∎

### Q4 — force between parallel currents, and the ampere

*Diagram:* two long parallel vertical wires a distance d apart, carrying currents I₁ and I₂ in the
same direction, with the field of wire 1 at wire 2 shown into the page and the resulting force on
wire 2 shown pointing towards wire 1.

Let two long parallel straight conductors, a distance d apart, carry currents I₁ and I₂.

**Field of wire 1 at the location of wire 2** (using the long-straight-wire result):

```
      B₁ = μ₀ I₁/(2π d)
```

directed perpendicular to wire 2.

**Force on a length l of wire 2**, which carries current I₂ perpendicular to B₁:

```
      F = B₁ I₂ l sin 90° = B₁ I₂ l
        = [μ₀ I₁/(2π d)] I₂ l
```

**Force per unit length:**

```
      F/l = μ₀ I₁ I₂ / (2π d)
```

By Newton's third law, wire 1 experiences an equal and opposite force.

**Direction.** Applying Fleming's left-hand rule: the wires **attract** each other when the currents
flow in the **same** direction, and **repel** when the currents are in **opposite** directions.

**Definition of the ampere.** Putting I₁ = I₂ = 1 A and d = 1 m:

```
      F/l = (4π × 10⁻⁷)(1)(1)/(2π × 1) = 2 × 10⁻⁷ N m⁻¹
```

**One ampere is that steady current which, when flowing in each of two infinitely long, straight,
parallel conductors of negligible circular cross-section placed 1 metre apart in vacuum, produces a
force of 2 × 10⁻⁷ newton per metre of length on each conductor.** ∎

### Q5 — torque on a current loop

*Diagram:* a rectangular loop PQRS of sides l and b in a uniform field **B**, with the normal to the
loop at angle θ to **B**. Show the forces BIl on the two sides of length l, acting in opposite
directions out of and into the plane.

Consider a rectangular loop PQRS with sides of length l and b, carrying current I, placed in a
uniform field **B**, with the normal to its plane at angle θ to **B**.

**Forces on the sides of length l** (PQ and RS): these sides are perpendicular to **B**, so each
experiences a force

```
      F = B I l
```

These two forces are **equal in magnitude and opposite in direction**, but they act along **different
lines**, so they constitute a **couple**.

**Forces on the sides of length b:** these are equal, opposite, and act along the **same line**, so
they cancel completely and produce no torque.

**Torque of the couple** = (force) × (perpendicular distance between the lines of action). From the
geometry, that perpendicular distance is b sin θ:

```
      τ = (B I l)(b sin θ)
        = B I (l b) sin θ
        = B I A sin θ                        where A = lb is the area of the loop
```

For **N turns:**

```
      τ = N I A B sin θ
```

Defining the **magnetic dipole moment m = N I A** (directed along the normal to the loop):

```
      τ = m × B
```

**Maximum torque:** when sin θ = 1, i.e. θ = 90° — the normal perpendicular to **B**, which means the
**plane of the coil is parallel to B**. Then τ_max = NIAB.

**Zero torque:** when θ = 0°, i.e. the normal parallel to **B**, so the **plane of the coil is
perpendicular to B**. This is the position of stable equilibrium.

**Note:** the **net force** on the loop in a uniform field is **zero** — it experiences a pure couple
and so rotates without translating. ∎

### Q6 — circular path and speed-independent period

A charge q of mass m enters a uniform field **B** with velocity **v** perpendicular to **B**.

**The force.** F = qvB sin 90° = qvB, and by **F** = q(**v** × **B**) it is **perpendicular to v**.

Since the force is always perpendicular to the velocity, it **changes the direction but never the
magnitude** of **v**. A constant-magnitude force always perpendicular to the velocity is exactly a
**centripetal** force, so the particle moves in a **circle** at constant speed.

**Radius.** Equating the magnetic force to the required centripetal force:

```
      q v B = m v²/r
⟹     r = m v/(q B)
```

**Time period.**

```
      T = 2πr/v = 2π [m v/(qB)]/v
⟹     T = 2π m/(q B)
```

**The speed v has cancelled.** So the time period (and hence the frequency f = qB/2πm) depends only
on the charge-to-mass ratio and the field — **not on the speed**, and not on the radius. A faster
particle travels a proportionately larger circle in the same time. ∎

### Q7 — conversion of a galvanometer

*Diagrams:* (i) galvanometer G with a shunt S connected in parallel across it, the pair in series in
the circuit; (ii) galvanometer G with a resistance R in series, the pair connected in parallel across
the component.

**(i) To an ammeter — connect a low resistance (shunt) in parallel.**

Let the galvanometer have resistance G and give full-scale deflection for current I_g. To make it
read up to a current I, connect a shunt S in parallel, so that only I_g passes through G and the
remaining (I − I_g) passes through S.

Since G and S are in parallel, the potential difference across them is the same:

```
      I_g G = (I − I_g) S
```

```
      S = I_g G / (I − I_g)
```

Since I >> I_g in practice, **S is very small**. The resistance of the ammeter so formed is the
parallel combination GS/(G + S), which is smaller than S — hence very small, as required.

**(ii) To a voltmeter — connect a high resistance in series.**

To make the galvanometer read up to a potential difference V, connect a resistance R in series, so
that when V is applied across the combination the current through the galvanometer is exactly I_g:

```
      V = I_g (G + R)
```

```
      R = V/I_g − G
```

Since I_g is very small, **R is very large**. The resistance of the voltmeter so formed is (G + R),
which is very large, as required.

### Q8 — why the magnetic force does no work

The magnetic force on a moving charge is

```
      F = q (v × B)
```

By the definition of the cross product, **F** is **always perpendicular to v**.

The work done by a force over a displacement d**s** = **v** dt is

```
      dW = F · ds = F · v dt
```

Since **F** ⊥ **v**, the dot product **F**·**v** = 0, so

```
      dW = 0
```

Hence the magnetic force does **no work** on the charge. Consequently the **kinetic energy and speed
of the particle remain unchanged** — the magnetic field can change only the **direction** of motion.

### Q9 — force between two parallel wires

```
      I₁ = 5 A          I₂ = 10 A          d = 20 cm = 0.2 m
```

```
      F/l = μ₀ I₁ I₂/(2π d)
          = (4π × 10⁻⁷)(5)(10)/(2π × 0.2)
          = (2 × 10⁻⁷)(50)/(0.2)                    [using μ₀/2π = 2 × 10⁻⁷]
          = (10⁻⁵)/(0.2)
          = 5 × 10⁻⁵ N m⁻¹
```

**F/l = 5 × 10⁻⁵ N m⁻¹**, and since the currents are in the **same direction**, the force is
**attractive**.

### Q10 — field at the centre of a circular coil

```
      N = 50          R = 5 cm = 0.05 m          I = 2 A
```

```
      B = μ₀ N I/(2R)
        = (4π × 10⁻⁷)(50)(2)/(2 × 0.05)
        = (4π × 10⁻⁷)(100)/(0.1)
        = (4π × 10⁻⁵)/(0.1)
        = 4π × 10⁻⁴
        = 1.256 × 10⁻³ T
```

**B ≈ 1.26 × 10⁻³ T** (about 1.26 mT), directed along the axis of the coil.

### Q11 — force on a charge moving parallel to B

F = qvB sin θ with θ = 0°, so sin θ = 0.

**Answer: (b) zero**

### Q12 — case study: galvanometer conversion

```
      G = 60 Ω          I_g = 1 mA = 10⁻³ A
```

**(i) Ammeter reading up to I = 1 A** — connect a shunt S in parallel:

```
      S = I_g G/(I − I_g)
        = (10⁻³)(60)/(1 − 10⁻³)
        = 0.06/0.999
        = 0.06006 Ω
```

**S ≈ 0.06 Ω, connected in parallel with the galvanometer.**

**(ii) Voltmeter reading up to V = 5 V** — connect a resistance R in series:

```
      R = V/I_g − G
        = 5/(10⁻³) − 60
        = 5000 − 60
        = 4940 Ω
```

**R = 4940 Ω, connected in series with the galvanometer.**

**(iii) Resistance of the ammeter** = the parallel combination of G and S:

```
      R_A = GS/(G + S) = (60)(0.06006)/(60.06006) = 3.6036/60.06 ≈ 0.06 Ω
```

**R_A ≈ 0.06 Ω** — essentially equal to the shunt, since S << G.

**(iv) Why an ammeter must have low resistance.** An ammeter is connected **in series** in the
circuit whose current is being measured. If its resistance were appreciable, it would **increase the
total resistance of the circuit and so reduce the current** — the very quantity it is meant to
measure. A low resistance ensures the ammeter disturbs the circuit as little as possible. (Ideally,
an ammeter has zero resistance.)

### Q13 — current sensitivity vs voltage sensitivity

```
      Current sensitivity   I_s = φ/I = N A B/k
      Voltage sensitivity   V_s = φ/V = N A B/(k G)  =  I_s/G
```

The current sensitivity can be increased by increasing the number of turns N. But increasing N also
increases the **length of wire in the coil**, and hence the **galvanometer's resistance G**.

Since V_s = I_s/G, if G increases in the **same proportion** as I_s, the voltage sensitivity is
**unchanged**. So increasing the current sensitivity does **not** necessarily increase the voltage
sensitivity.

*(To increase V_s specifically, one must increase N, A or B, or reduce k, **without** a proportionate
increase in G.)*

---

## 5. Test yourself

Time: 55 minutes. Answers below.

1. *(1)* The SI unit of magnetic dipole moment is
   (a) A m (b) A m² (c) A m⁻² (d) T m²
2. *(1)* The magnetic field at the centre of a circular coil of radius R with N turns carrying
   current I is
   (a) μ₀NI/(2R) (b) μ₀NI/(4πR) (c) μ₀NI/R (d) μ₀I/(2πR)
3. *(1)* Two parallel wires carrying currents in opposite directions
   (a) attract (b) repel (c) exert no force (d) rotate
4. *(2)* A proton moves with speed 2 × 10⁶ m s⁻¹ perpendicular to a field of 0.5 T. Find the force on
   it. (q = 1.6 × 10⁻¹⁹ C)
5. *(2)* State the right-hand thumb rule and use it to give the direction of the field around a
   straight wire.
6. *(2)* An electron moving with velocity **v** enters a magnetic field **B** parallel to **v**. What
   is its path?
7. *(3)* Derive an expression for the radius and time period of a charged particle moving in a
   circular path in a uniform magnetic field.
8. *(3)* A wire of length 20 cm carrying 5 A is placed at 30° to a magnetic field of 0.4 T. Find the
   force on it.
9. *(3)* State and explain the principle of a velocity selector. Derive the condition for a particle
   to pass through undeflected.
10. *(5)* State the Biot–Savart law and use it to find the magnetic field at the centre of a circular
    coil of radius R carrying current I. A coil of 100 turns and radius 10 cm carries 1 A; find B at
    the centre.
11. *(3)* A galvanometer of resistance 40 Ω gives full-scale deflection for 5 mA. Convert it into
    (i) an ammeter of range 2 A and (ii) a voltmeter of range 10 V.
12. *(2)* Why is the magnetic field inside a long solenoid uniform, and what is its value?
13. *(2)* A current loop of area 0.02 m² carrying 3 A is placed in a field of 0.5 T with its plane
    parallel to the field. Find the torque on it.

### Answer key

**1. (b) A m².**

**2. (a) μ₀NI/(2R).**

**3. (b) repel.**

**4. 1.6 × 10⁻¹³ N.** F = qvB sin 90° = (1.6 × 10⁻¹⁹)(2 × 10⁶)(0.5) = 1.6 × 10⁻¹³ N.

**5.** **Right-hand thumb rule:** if the wire is grasped in the right hand with the **thumb pointing
along the direction of the current**, then the **curled fingers give the direction of the magnetic
field lines**, which are concentric circles around the wire.

**6. A straight line** — the force is F = qvB sin 0° = 0, so the electron continues undeflected with
unchanged velocity.

**7.** Since **v** ⊥ **B**, the force qvB is perpendicular to **v** and provides the centripetal
force: qvB = mv²/r, giving **r = mv/(qB)**. Then T = 2πr/v = 2πm/(qB), so **T = 2πm/(qB)** —
independent of the speed. ∎

**8. 0.2 N.** F = BIl sin θ = (0.4)(5)(0.2)(sin 30°) = (0.4)(5)(0.2)(0.5) = 0.2 N.

**9.** A velocity selector has mutually perpendicular electric and magnetic fields, both
perpendicular to the beam, arranged so that the electric force qE and the magnetic force qvB act in
**opposite** directions. A particle passes undeflected when the two balance:
qE = qvB, so **v = E/B**. Only particles with this speed pass through undeflected — and the condition
is independent of the particle's charge and mass, so it selects by **speed** alone.

**10.** Statement and derivation as in §3 Q1, giving B = μ₀NI/(2R).
Numerically: B = (4π × 10⁻⁷)(100)(1)/(2 × 0.1) = (4π × 10⁻⁵)/(0.2) = 2π × 10⁻⁴ ≈
**6.28 × 10⁻⁴ T**.

**11.** (i) S = I_gG/(I − I_g) = (5 × 10⁻³)(40)/(2 − 5 × 10⁻³) = 0.2/1.995 ≈ **0.1003 Ω** in parallel.
(ii) R = V/I_g − G = 10/(5 × 10⁻³) − 40 = 2000 − 40 = **1960 Ω** in series.

**12.** In a long solenoid the fields of the individual closely-wound turns **add** along the axis and
largely **cancel** outside, and away from the ends the contributions from turns on either side make
the axial field the same at all interior points — so **B** is uniform, parallel to the axis, with
magnitude **B = μ₀nI** (n = turns per unit length). The field outside is nearly zero.

**13. 0.03 N m.** With the plane parallel to **B**, the normal is perpendicular to **B**, so θ = 90°
and the torque is maximum: τ = NIAB sin 90° = (1)(3)(0.02)(0.5) = 0.03 N m.

**Scoring.** Out of 30. Below 21 → the circular-loop derivation and the galvanometer are where the
5-marks are. Write both out with diagrams from memory before moving to Ch 5.

---

## 6. Answering tips

**On the circular-loop derivation**

1. **Draw the loop, the axial point P, and a pair of diametrically opposite current elements**, with
   their d**B** vectors resolved into axial and perpendicular components. Without this diagram the
   symmetry argument cannot be followed, and the diagram is a mark in its own right.

2. **State that θ = 90° for every element** (d**l** is always perpendicular to **r**). This is what
   lets you drop sin θ, and it is a mark.

3. **State the symmetry cancellation explicitly:** "the components perpendicular to the axis cancel
   in pairs for diametrically opposite elements, so only the axial components add." This sentence is
   the heart of the derivation.

4. **Show ∮dl = 2πR** as its own step.

5. **Finish with the x = 0 special case** — the question almost always asks for the field at the
   centre as well.

**On Ampere's law**

6. **Choose and justify the Amperian loop.** "By symmetry, B is tangential and constant in magnitude
   on a circle of radius r centred on the wire." That justification is a mark.

7. **State the direction and the field pattern** — concentric circles, right-hand thumb rule.

**On the galvanometer**

8. **The diagram must be labelled**: coil, soft-iron core, concave pole pieces, suspension, pointer,
   scale. It carries 1–2 marks of the 5.

9. **Explain the radial field.** "The field is radial, so the plane of the coil is always parallel to
   B and sin θ = 1, making the torque independent of deflection and the scale uniform." This is the
   most-asked sub-part in the chapter.

10. **For conversions, write the physical arrangement in words as well as the formula.** "A low
    resistance (shunt) is connected in **parallel** with the galvanometer." Both the arrangement and
    the derivation are marked.

11. **Give the reason for low/high resistance.** Ammeter in series, so it must have low resistance to
    avoid changing the circuit current. Voltmeter in parallel, so it must have high resistance to
    avoid drawing appreciable current.

**On force questions**

12. **Say which rule you used for direction** — Fleming's left-hand rule, or the cross product. And
    state the direction in words ("attractive", "into the page", "along the axis").

13. **Watch the angle.** For a current loop, τ = NIAB sin θ where θ is between the **normal** and
    **B**. If the question gives the angle with the **plane**, convert. State which you are using.

14. **For F = qvB sin θ, check the θ = 0 case first.** If the velocity is parallel to the field, the
    answer is zero and there is nothing else to do — that is an entire 1-mark question.

**On numericals**

15. **Use μ₀/4π = 10⁻⁷ and μ₀/2π = 2 × 10⁻⁷.** Much faster than carrying 4π × 10⁻⁷ through the
    arithmetic.

16. **Convert cm to m before substituting**, and note that radius, not diameter, goes into the loop
    formulas. Units: T for field, N for force, N m⁻¹ for force per length, A m² for dipole moment,
    N m for torque.
