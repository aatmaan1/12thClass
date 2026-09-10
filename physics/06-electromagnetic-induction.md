# Ch 6 — Electromagnetic Induction

**Units III + IV (17 marks, shared with Ch 4, 5, 7) · Typical appearance: 1–2 MCQs + a 2/3-mark
Lenz's-law or inductance question, and often a 5-marker on the AC generator or self/mutual
inductance.**

---

## 1. Scope

### In the syllabus

- **Electromagnetic induction**
- **Faraday's laws**; induced emf and current
- **Lenz's law**; **eddy currents**
- **Self and mutual induction**
- **AC generator** — *(the CBSE syllabus lists this under Chapter 7, while NCERT places it in
  Chapter 6. It is the same unit either way; it is covered here because the physics is Faraday's
  law.)*

### Deleted

Nothing substantial was removed from this chapter.

---

## 2. Brief

### Magnetic flux

```
      φ = B · A = B A cos θ
```

θ is the angle between **B** and the **area vector** (the normal to the surface).

SI unit: **weber (Wb)** = T m². For a coil of N turns, the **flux linkage** is Nφ.

Flux is a **scalar**. It changes if B changes, if A changes, or if the orientation θ changes — and
**all three** are used to set questions.

### Faraday's laws of electromagnetic induction

**First law.** Whenever the magnetic flux linked with a closed circuit changes, an **emf is induced**
in the circuit. The emf lasts only as long as the change continues.

**Second law.** The magnitude of the induced emf is equal to the **rate of change** of magnetic flux
linked with the circuit.

```
      ε = − dφ/dt                   and for N turns:      ε = − N dφ/dt
```

**Induced current** (if the circuit is closed, of total resistance R):

```
      I = ε/R = −(N/R) dφ/dt
```

**Charge** that flows in time Δt:

```
      q = ∫I dt = NΔφ/R
```

— note that the charge depends only on the **total change in flux**, not on how fast it happened.
That is a favourite MCQ.

### Lenz's law

**Statement.** The direction of the induced emf (and hence of the induced current) is such that it
**opposes the change** in magnetic flux that produced it.

That is the meaning of the **minus sign** in Faraday's law.

**Lenz's law is a consequence of the conservation of energy.** If the induced current *aided* the
change instead of opposing it, the change would grow without limit and produce energy from nothing —
a perpetual-motion machine. So work must be done against the opposing force, and it is this
mechanical work that appears as the electrical energy of the induced current.

**Applying it — the standard cases:**

| Situation | Induced current direction | Reason |
| --- | --- | --- |
| N pole of a magnet approaching a coil | such that the near face becomes a **north** pole | to **repel** the approaching magnet |
| N pole of a magnet receding from a coil | such that the near face becomes a **south** pole | to **attract** and oppose the receding |
| Coil moving into a field region | opposes the **increase** in flux | |
| Coil moving out of a field region | opposes the **decrease** in flux | |
| A magnet falling through a metal ring | opposes the motion | the magnet falls **slower** than free fall |

> **In an exam, always give the reason, not just the direction.** "The induced current flows
> anticlockwise so that the face towards the magnet becomes a north pole, repelling the approaching
> north pole and thereby opposing the increase in flux." That sentence is the mark.

### Motional emf

*Set-up:* a conducting rod of length l slides with velocity v along two parallel rails, in a uniform
field B perpendicular to the plane of the rails.

**Derivation.** Let the rod be at distance x from the closed end. The area of the circuit is lx, so
the flux is

```
      φ = B l x
```

As the rod moves, x changes, so

```
      ε = −dφ/dt = −B l (dx/dt) = −B l v
```

**Magnitude:**

```
      ε = B l v
```

**Alternative derivation (via the Lorentz force).** Each free charge q in the rod moves with the rod
at velocity v, and so experiences a magnetic force qvB along the rod. The work done per unit charge
in moving it along the length l is therefore

```
      ε = (force per unit charge) × (length) = (vB)(l) = Blv
```

**Associated quantities** (often asked as follow-up parts):

```
      Induced current      I = Blv/R
      Force needed to keep the rod moving at constant v:   F = BIl = B²l²v/R
      Mechanical power supplied:   P = Fv = B²l²v²/R
      Electrical power dissipated: P = I²R = B²l²v²/R           — the two are EQUAL
```

The equality of mechanical input and electrical output is a nice demonstration of energy
conservation, and it is asked.

### Eddy currents

When the magnetic flux through the **body** of a conductor changes, induced currents circulate in
closed loops within the bulk of the metal. These are **eddy currents** (also called Foucault
currents).

**Disadvantages:**
- They dissipate energy as **heat** in transformer and motor cores, reducing efficiency.
- They can cause overheating of the core.

**How they are minimised:** by using a **laminated core** — thin sheets of metal separated by
insulating varnish. The laminations break the large eddy-current loops into many small ones of
higher resistance, so the induced currents (and hence the I²R losses) are much smaller.

**Applications (each worth knowing by name):**
- **Electromagnetic braking** in trains
- **Induction furnace** — melting metals by eddy-current heating
- **Induction motor**
- **Electric power (energy) meters** — the rotating aluminium disc
- **Metal detectors**
- Damping in moving-coil galvanometers (via the metal frame)

### Self-induction

When the current in a coil changes, the flux it produces through itself changes, inducing an emf in
the **same** coil that opposes the change. This is **self-induction**, and it is why a coil resists
changes in its own current — an electrical "inertia".

```
      φ = L I                       ⟹      ε = − L dI/dt
```

**L is the self-inductance** (or coefficient of self-induction), SI unit the **henry (H)**.

**Definitions of the henry**, either of which is acceptable:
- L = 1 H if a flux linkage of 1 Wb is produced by a current of 1 A.
- L = 1 H if an emf of 1 V is induced by a current changing at 1 A s⁻¹.

**Self-inductance of a long solenoid** (N turns, length l, area A, n = N/l turns per unit length):

*Derivation.* The field inside is B = μ₀nI. The flux through one turn is BA = μ₀nIA, so the total
flux linkage through N turns is

```
      Nφ = N μ₀ n I A = (n l)(μ₀ n I A) = μ₀ n² A l I
```

Comparing with Nφ = LI:

```
      L = μ₀ n² A l  =  μ₀ N² A / l
```

(With a magnetic material of relative permeability μ_r inside, multiply by μ_r.)

**Energy stored in an inductor:**

```
      U = ½ L I²
```

*Derivation:* the work done against the back emf in raising the current from 0 to I is
W = ∫εI dt = ∫(L dI/dt) I dt = L∫I dI = ½LI².

### Mutual induction

When the current in one coil (the **primary**) changes, the changing flux links a nearby coil (the
**secondary**) and induces an emf in it.

```
      φ₂ = M I₁                     ⟹      ε₂ = − M dI₁/dt
```

**M is the mutual inductance**, also in **henry**. Note M is the same whichever coil is treated as
primary (M₁₂ = M₂₁) — the **reciprocity** property.

**Mutual inductance of two long coaxial solenoids** (both of length l and area A, with N₁ and N₂
turns):

```
      M = μ₀ n₁ n₂ A l  =  μ₀ N₁ N₂ A / l
```

**M depends on:** the number of turns of each coil, their areas, their separation and relative
orientation, and the permeability of the medium between them. It is maximum when the coils are
**coaxial and close together** and zero when their axes are **perpendicular**.

**Coupling relation** (worth knowing): M = k√(L₁L₂), where k ≤ 1 is the coupling coefficient; k = 1
for perfect coupling.

### AC generator (dynamo)

**Principle.** Electromagnetic induction — when a coil rotates in a uniform magnetic field, the flux
through it changes continuously, inducing an alternating emf.

*Diagram (label all of these):* a rectangular armature coil ABCD between the poles N and S of a
magnet; the two ends of the coil connected to two **slip rings**, which press against two
**carbon brushes** connected to the external circuit.

**Construction.**
- **Armature coil** — a coil of many turns of insulated wire wound on a soft-iron core
- **Field magnet** — provides a strong uniform magnetic field
- **Slip rings** — two rings attached to the ends of the coil, rotating with it
- **Brushes** — stationary carbon contacts pressing on the slip rings, carrying current to the
  external circuit

**Working and derivation.** Let the coil of N turns and area A rotate with uniform angular velocity ω
in a uniform field B. At time t, the normal to the coil makes an angle θ = ωt with **B**, so the flux
linkage is

```
      Nφ = N B A cos ωt
```

By Faraday's law,

```
      ε = −d(Nφ)/dt
        = −N B A d(cos ωt)/dt
        = N B A ω sin ωt
```

So

```
      ε = ε₀ sin ωt                 where     ε₀ = N B A ω
```

The emf is **sinusoidal**, i.e. alternating. Its **peak value** is ε₀ = NBAω, and it reverses
direction every half rotation.

**When is the emf maximum and zero?**
- ε is **maximum** when sin ωt = 1, i.e. when the **plane of the coil is parallel to B** (the coil is
  moving perpendicular to the field, cutting field lines fastest).
- ε is **zero** when the **plane of the coil is perpendicular to B** (the coil is momentarily moving
  parallel to the field lines).

**Why slip rings and not a commutator?** Slip rings keep each end of the coil permanently connected
to the same brush, so the output reverses with the coil and is **alternating**. (A split-ring
commutator, as in a DC generator, reverses the connections each half turn to give a unidirectional
output.)

### Quick recall box

```
FLUX : φ = BA cos θ (weber) ;  flux linkage = Nφ
FARADAY : ε = −N dφ/dt ;  I = ε/R ;  charge q = NΔφ/R  (independent of the time taken)

LENZ : the induced current OPPOSES the change in flux
  — the minus sign in Faraday's law
  — a consequence of CONSERVATION OF ENERGY

MOTIONAL EMF : ε = Blv
  I = Blv/R ;  F = B²l²v/R ;  P_mech = P_elec = B²l²v²/R

EDDY CURRENTS : induced loops in the bulk of a conductor
  minimised by LAMINATED cores
  uses: electromagnetic braking, induction furnace, induction motor, energy meters

SELF-INDUCTANCE : φ = LI ;  ε = −L dI/dt ;  unit HENRY
  solenoid : L = μ₀n²Al = μ₀N²A/l
  energy   : U = ½LI²

MUTUAL INDUCTANCE : φ₂ = MI₁ ;  ε₂ = −M dI₁/dt ;  M₁₂ = M₂₁
  two coaxial solenoids : M = μ₀n₁n₂Al = μ₀N₁N₂A/l
  M = k√(L₁L₂) ;  max when coaxial and close, ZERO when axes are perpendicular

AC GENERATOR : ε = NBAω sin ωt = ε₀ sin ωt ;  ε₀ = NBAω
  max emf when the coil's PLANE is PARALLEL to B ;  zero when perpendicular
  slip rings (not a commutator) → alternating output
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* Draw a labelled diagram of an AC generator. State its principle, explain its
working, and derive an expression for the instantaneous emf induced in the coil.

**Q2.** *(3 marks)* State Faraday's laws of electromagnetic induction. Derive an expression for the
motional emf induced in a conducting rod moving in a uniform magnetic field.

**Q3.** *(3 marks)* State Lenz's law. Show that it is a consequence of the conservation of energy.

**Q4.** *(3 marks)* Derive an expression for the self-inductance of a long solenoid. On what factors
does it depend?

**Q5.** *(3 marks)* Define mutual inductance and write its SI unit. Derive an expression for the
mutual inductance of two long coaxial solenoids.

**Q6.** *(2 marks)* What are eddy currents? State two applications and one way of minimising them.

**Q7.** *(2 marks)* A magnet is dropped through a long vertical copper tube. Will it fall with the
acceleration due to gravity? Explain.

**Q8.** *(2 marks)* The current in a coil of self-inductance 5 H changes from 2 A to 6 A in 0.2 s.
Find the magnitude of the induced emf.

**Q9.** *(2 marks)* A coil of area 0.05 m² with 100 turns is placed perpendicular to a field of
0.2 T. The field is reduced to zero in 0.1 s. Find the induced emf.

**Q10.** *(1 mark, MCQ)* The SI unit of self-inductance is
(a) weber (b) tesla (c) henry (d) volt

**Q11.** *(2 marks)* A conducting rod of length 0.5 m moves with a velocity of 4 m s⁻¹ perpendicular
to a magnetic field of 0.3 T. Find the emf induced across its ends.

**Q12.** *(4 marks, case study)* A coil of 500 turns and area 100 cm² is placed with its plane
perpendicular to a magnetic field of 0.4 T. The coil has a resistance of 20 Ω. The field is reduced
uniformly to zero in 0.2 s.
(i) Find the initial magnetic flux linkage.
(ii) Find the induced emf.
(iii) Find the induced current.
(iv) Find the total charge that flows.

**Q13.** *(2 marks)* Why is the core of a transformer laminated?

---

## 4. Solutions

### Q1 — AC generator

*Diagram:* a rectangular coil ABCD mounted on an axle between the poles N and S of a permanent
magnet, with the ends of the coil connected to two slip rings S₁ and S₂, which press against carbon
brushes B₁ and B₂ leading to an external resistance R. Label all of: armature coil, field magnet,
slip rings, brushes, external circuit.

**Principle.** The AC generator works on the principle of **electromagnetic induction**: when a coil
is rotated in a uniform magnetic field, the magnetic flux linked with it changes continuously, and by
Faraday's law an emf is induced. Because the flux varies sinusoidally, the induced emf is
**alternating**.

**Construction.**
- **Armature coil:** a rectangular coil of a large number of turns of insulated copper wire wound on
  a soft-iron core (the core increases the flux linkage).
- **Field magnet:** a strong permanent magnet (or electromagnet) providing a uniform field between
  its concave poles.
- **Slip rings:** two metal rings, each connected to one end of the coil and rotating with it.
- **Brushes:** two stationary carbon brushes pressing against the slip rings, transferring the
  current to the external circuit.

**Working.** As the coil rotates, the angle between its normal and the field changes continuously, so
the flux through it changes and an emf is induced. During one half-rotation the flux decreases and
the emf drives current one way; during the next half it increases and the current reverses. The
output is therefore **alternating**, completing one cycle per rotation.

**Derivation.** Let the coil have N turns and area A, and rotate with constant angular velocity ω in
a uniform field B. At time t the normal to the coil makes an angle θ = ωt with **B**, so the flux
linkage is

```
      N φ = N B A cos θ = N B A cos ωt
```

By Faraday's law,

```
      ε = − d(Nφ)/dt
        = − N B A · d(cos ωt)/dt
        = − N B A (−ω sin ωt)
```

```
      ε = N B A ω sin ωt  =  ε₀ sin ωt              where  ε₀ = N B A ω
```

The induced emf varies sinusoidally with time, with peak value ε₀ = NBAω. ∎

**Maximum and zero emf.** ε is maximum when sin ωt = 1, i.e. when the **plane of the coil is parallel
to the field** (the coil sides are then moving perpendicular to **B**, cutting field lines at the
greatest rate). ε is zero when the **plane of the coil is perpendicular to the field**.

### Q2 — Faraday's laws and motional emf

**Faraday's first law.** Whenever the magnetic flux linked with a closed circuit changes, an emf is
induced in the circuit; it persists only as long as the flux is changing.

**Faraday's second law.** The magnitude of the induced emf equals the rate of change of the magnetic
flux linkage:

```
      ε = − N dφ/dt
```

(The minus sign expresses Lenz's law — the induced emf opposes the change.)

**Motional emf — derivation.**

*Diagram:* two long parallel horizontal rails joined at the left end by a resistance R, in a uniform
field **B** directed into the page. A conducting rod PQ of length l rests across the rails and slides
to the right with velocity v.

Let the rod be at distance x from the closed end. The area enclosed by the circuit is

```
      A = l x
```

so the magnetic flux through it is

```
      φ = B A = B l x
```

As the rod slides, x increases with time. By Faraday's law,

```
      ε = − dφ/dt = − B l (dx/dt)
```

and since dx/dt = v,

```
      |ε| = B l v
```

∎

**Alternative (Lorentz-force) derivation, if asked.** Each free charge q in the rod shares the rod's
velocity v and so experiences a magnetic force qvB directed along the rod. The work done by this
force in carrying unit charge from one end of the rod to the other, a distance l, is

```
      ε = (vB)(l) = Blv
```

which is the induced emf. ∎

### Q3 — Lenz's law and energy conservation

**Statement of Lenz's law.** The direction of the induced emf, and hence of the induced current, is
always such as to **oppose the change in magnetic flux** that produces it.

**Showing it is a consequence of energy conservation.**

*Diagram:* the north pole of a bar magnet being pushed towards a coil connected to a galvanometer,
with the induced current shown flowing so that the near face of the coil becomes a north pole.

Suppose the north pole of a magnet is pushed towards a closed coil. The flux through the coil
increases, so a current is induced.

**By Lenz's law**, the induced current flows in the sense that makes the **near face of the coil a
north pole**, which **repels** the approaching magnet. To keep pushing the magnet in, an external
agent must therefore do **work against this repulsion**. That mechanical work is what appears as the
electrical energy dissipated in the coil. Energy is conserved.

**Now suppose Lenz's law were violated** — that the induced current instead made the near face a
**south** pole. It would then **attract** the magnet, pulling it in faster. The magnet would
accelerate on its own, increasing the rate of change of flux, increasing the induced current,
increasing the attraction — and so on. We would obtain both increasing kinetic energy and increasing
electrical energy from nothing. This violates the **conservation of energy**, and is therefore
impossible.

Hence Lenz's law is required by, and is a consequence of, the conservation of energy. ∎

### Q4 — self-inductance of a long solenoid

*Diagram:* a long solenoid of length l, cross-sectional area A, with N closely wound turns carrying
current I, and the uniform axial field B inside.

Consider a long solenoid of length l, cross-sectional area A, with N turns, so that the number of
turns per unit length is n = N/l. Let it carry a current I.

**Field inside** the solenoid (from [Ch 4](04-moving-charges-and-magnetism.md)):

```
      B = μ₀ n I
```

**Flux through one turn:**

```
      φ = B A = μ₀ n I A
```

**Total flux linkage** through all N turns:

```
      N φ = N μ₀ n I A
```

Substituting N = nl:

```
      N φ = (n l)(μ₀ n I A) = μ₀ n² A l I
```

**By definition** of self-inductance, Nφ = L I, so

```
      L = μ₀ n² A l  =  μ₀ N² A / l
```

∎

**Factors on which L depends:**

1. The **number of turns** — L ∝ N² (so doubling the turns quadruples L).
2. The **cross-sectional area** A — L ∝ A.
3. The **length** l — L ∝ 1/l for a fixed N.
4. The **permeability of the core material** — with a core of relative permeability μ_r,
   L = μ_r μ₀ N²A/l, so an iron core greatly increases L.

Note that L does **not** depend on the current — it is a purely geometric and material property.

### Q5 — mutual inductance of two coaxial solenoids

**Definition.** The **mutual inductance** of two coils is the flux linkage produced in one coil per
unit current in the other:

```
      φ₂ = M I₁                     ⟹      M = φ₂/I₁
```

Equivalently, M = 1 H if a rate of change of current of 1 A s⁻¹ in the primary induces an emf of 1 V
in the secondary.

**SI unit:** the **henry (H)**.

**Derivation for two long coaxial solenoids.**

*Diagram:* an inner solenoid S₂ of N₂ turns wound over a longer outer solenoid S₁ of N₁ turns, both
of length l and cross-sectional area A, on the same axis.

Let solenoid 1 have N₁ turns and solenoid 2 have N₂ turns, both of length l and cross-sectional area
A, wound coaxially. Let n₁ = N₁/l and n₂ = N₂/l.

Suppose a current I₁ flows in solenoid 1. The field it produces inside is

```
      B₁ = μ₀ n₁ I₁
```

Since the solenoids are coaxial and of the same area, this whole field links solenoid 2. The flux
through one turn of solenoid 2 is B₁A, so the total flux linkage of solenoid 2 is

```
      N₂ φ₂ = N₂ B₁ A = N₂ μ₀ n₁ I₁ A
```

Substituting N₂ = n₂ l:

```
      N₂ φ₂ = (n₂ l)(μ₀ n₁ I₁ A) = μ₀ n₁ n₂ A l I₁
```

By definition N₂φ₂ = M I₁, hence

```
      M = μ₀ n₁ n₂ A l  =  μ₀ N₁ N₂ A / l
```

∎

Note the result is **symmetric** in the two coils, consistent with the reciprocity property
M₁₂ = M₂₁.

**M depends on:** the number of turns of each coil, their cross-sectional area, their length,
their relative orientation and separation, and the permeability of the medium between them.

### Q6 — eddy currents

**Definition.** When the magnetic flux through the **body** of a conductor changes, induced currents
are set up which circulate in closed loops within the bulk of the metal. These are called **eddy
currents** (or Foucault currents).

**Two applications:**
1. **Electromagnetic braking** — in electric trains, an electromagnet near the rotating rails or
   drum induces eddy currents that oppose the motion, providing smooth braking with no mechanical
   wear.
2. **Induction furnace** — a metal placed in a rapidly changing magnetic field develops large eddy
   currents, whose I²R heating melts the metal. Used to produce alloys.

*(Other acceptable answers: induction motor, electric power meters, metal detectors, damping in
galvanometers.)*

**How they are minimised.** By using a **laminated core** — the core is made of thin sheets of metal
stuck together with insulating varnish between them, with the planes of the laminations parallel to
the field. This confines the eddy-current loops to individual thin sheets, greatly increasing the
resistance of each loop and so reducing the currents and the associated I²R heating.

### Q7 — a magnet dropped through a copper tube

**No — the magnet falls with an acceleration much less than g**, and in fact often reaches a nearly
constant (terminal) velocity.

**Explanation.** As the magnet falls, the magnetic flux through each section of the copper tube
changes. This induces **eddy currents** in the walls of the tube. By **Lenz's law**, these currents
flow in the sense that opposes the change in flux, so they exert a **retarding force** on the falling
magnet — opposing its motion.

The magnet therefore experiences an upward magnetic force in addition to its weight, so its net
downward acceleration is less than g. As it speeds up, the induced currents and the retarding force
grow, until the retarding force balances the weight and the magnet descends at a steady speed.

*(If the tube were made of an insulator, or were slit lengthwise so no circulating current could
flow, the magnet would fall freely with acceleration g. That is the standard follow-up question.)*

### Q8 — induced emf from a changing current

```
      L = 5 H          dI = 6 − 2 = 4 A          dt = 0.2 s
```

```
      |ε| = L |dI/dt| = 5 × (4/0.2) = 5 × 20 = 100 V
```

**|ε| = 100 V**

*(The induced emf opposes the increase in current, hence the minus sign in ε = −L dI/dt; the question
asks for the magnitude.)*

### Q9 — induced emf from a changing field

```
      N = 100          A = 0.05 m²          B changes from 0.2 T to 0
      dt = 0.1 s       coil ⊥ to B, so θ = 0 and φ = BA
```

```
      Initial flux linkage  = N B A = (100)(0.2)(0.05) = 1 Wb
      Final flux linkage    = 0

      |ε| = |N dφ/dt| = |Δ(Nφ)|/Δt = (1 − 0)/0.1 = 10 V
```

**|ε| = 10 V**

### Q10 — SI unit of self-inductance

**Answer: (c) henry**

### Q11 — motional emf

```
      l = 0.5 m          v = 4 m s⁻¹          B = 0.3 T          (all mutually perpendicular)
```

```
      ε = B l v = (0.3)(0.5)(4) = 0.6 V
```

**ε = 0.6 V**

### Q12 — case study: coil in a changing field

```
      N = 500          A = 100 cm² = 100 × 10⁻⁴ m² = 1 × 10⁻² m²
      B = 0.4 T (initially), reduced to 0          R = 20 Ω          Δt = 0.2 s
```

The plane of the coil is perpendicular to **B**, so the normal is **parallel** to **B** and θ = 0,
giving φ = BA.

**(i) Initial flux linkage:**

```
      N φ = N B A = (500)(0.4)(1 × 10⁻²) = 2 Wb
```

**Initial flux linkage = 2 Wb**

**(ii) Induced emf:**

```
      |ε| = |Δ(Nφ)|/Δt = (2 − 0)/0.2 = 10 V
```

**|ε| = 10 V**

**(iii) Induced current:**

```
      I = ε/R = 10/20 = 0.5 A
```

**I = 0.5 A**

**(iv) Total charge:**

```
      q = I Δt = (0.5)(0.2) = 0.1 C
```

**q = 0.1 C**

*(Cross-check with q = NΔφ/R = 2/20 = 0.1 C ✓ — and note this form shows the charge depends only on
the total flux change and the resistance, **not** on how quickly the change happened. Halving Δt
would double the emf and the current but leave q unchanged.)*

### Q13 — why a transformer core is laminated

The alternating current in a transformer's windings produces a continuously changing magnetic flux in
the core. Since the core is a conductor, this changing flux induces **eddy currents** in the body of
the core, which dissipate energy as **heat** (I²R loss) and reduce the transformer's efficiency.

The core is therefore built from **thin laminations** — sheets of soft iron separated by insulating
varnish, with their planes **parallel to the magnetic field**. This restricts each eddy-current loop
to a single thin sheet, greatly **increasing the resistance** of the path available to the eddy
currents. The currents, and hence the power dissipated, are therefore much smaller.

---

## 5. Test yourself

Time: 45 minutes. Answers below.

1. *(1)* The SI unit of magnetic flux is
   (a) tesla (b) weber (c) henry (d) volt
2. *(1)* Lenz's law is a consequence of the conservation of
   (a) charge (b) momentum (c) energy (d) mass
3. *(1)* The self-inductance of a solenoid is proportional to
   (a) N (b) N² (c) 1/N (d) 1/N²
4. *(2)* Define magnetic flux and write its SI unit. When is the flux through a coil maximum?
5. *(2)* State Lenz's law and use it to find the direction of the induced current when the south pole
   of a magnet is moved towards a coil.
6. *(2)* A rod of length 1 m rotates about one end in a plane perpendicular to a field of 0.5 T with
   angular velocity 20 rad s⁻¹. Find the emf between its ends.
7. *(3)* Derive an expression for the energy stored in an inductor carrying a current I.
8. *(3)* A coil of 200 turns and area 0.02 m² is rotated at 50 rad s⁻¹ in a field of 0.1 T. Find the
   peak emf.
9. *(3)* Two coils have a mutual inductance of 0.5 H. Find the emf induced in the second coil when
   the current in the first changes from 0 to 4 A in 0.1 s.
10. *(5)* Draw a labelled diagram of an AC generator and derive the expression for the emf induced.
    A coil of 100 turns and area 0.05 m² rotates at 60 rad s⁻¹ in a field of 0.2 T; find the peak emf.
11. *(2)* Why does an aeroplane flying over the Earth's magnetic field develop a potential difference
    across its wing tips?
12. *(2)* On what factors does the mutual inductance of two coils depend? When is it zero?
13. *(2)* A coil of resistance 10 Ω experiences a flux change of 5 Wb. Find the charge that flows.

### Answer key

**1. (b) weber.**

**2. (c) energy.**

**3. (b) N².**

**4.** Magnetic flux through a surface is the product of the magnetic field and the area projected
perpendicular to it: φ = **B**·**A** = BA cos θ. SI unit **weber (Wb)**. It is **maximum** when θ = 0,
i.e. when **B** is **perpendicular to the plane of the coil** (parallel to its normal), giving
φ = BA.

**5.** **Lenz's law:** the induced current flows in the direction that opposes the change in flux
producing it. With the **south** pole approaching, the flux through the coil increases (in the sense
towards the magnet), so the induced current flows such that the **near face of the coil becomes a
south pole**, which **repels** the approaching south pole and so opposes the increase in flux. Seen
from the magnet's side, this means the current flows **clockwise**.

**6. 5 V.** For a rod rotating about one end, ε = ½Bωl² = ½(0.5)(20)(1)² = 5 V.
*(Derivation: the rod sweeps area ½l²θ, so φ = ½Bl²θ and ε = dφ/dt = ½Bl²ω.)*

**7.** When the current in an inductor is i and increasing at rate di/dt, the back emf is L(di/dt),
and the work done against it per unit time is P = εi = L i (di/dt). So the total work in raising the
current from 0 to I is
W = ∫P dt = ∫L i (di/dt) dt = L∫[0,I] i di = **½ L I²**, which is stored as magnetic energy. ∎

**8. 20 V.** ε₀ = NBAω = (200)(0.1)(0.02)(50) = 20 V.

**9. 20 V.** |ε₂| = M|dI₁/dt| = (0.5)(4/0.1) = (0.5)(40) = 20 V.

**10.** Diagram and derivation as in §3 Q1, giving ε = NBAω sin ωt.
Numerically: ε₀ = NBAω = (100)(0.2)(0.05)(60) = **60 V**.

**11.** The metal wings of the aeroplane act as a **conductor moving through the Earth's magnetic
field**. As the wings cut across the field's lines, a **motional emf** ε = B_V l v is induced across
them (it is the **vertical** component of the Earth's field that matters for horizontal flight, with
l the wingspan and v the speed). Hence a potential difference appears between the wing tips.

**12.** Mutual inductance depends on: the **number of turns** of each coil; their **cross-sectional
areas**; their **lengths**; the **distance between them** and their **relative orientation**; and the
**permeability of the medium** between them. It is **zero** when the axes of the two coils are
**perpendicular** to each other, because then none of the flux from one links the other.

**13. 0.5 C.** q = Δφ/R = 5/10 = 0.5 C. *(For N turns, q = NΔφ/R.)*

**Scoring.** Out of 29. Below 20 → the AC generator derivation and the two inductance derivations are
where the marks are. Write all three from memory, with diagrams.

---

## 6. Answering tips

**On the AC generator (the 5-marker)**

1. **The labelled diagram is worth 1–2 marks on its own.** You must show and label: armature coil,
   field magnet with poles, **slip rings**, **brushes**, external circuit. Omitting the slip rings and
   brushes is the standard loss.

2. **State the principle in one line** ("electromagnetic induction") before the construction.

3. **In the derivation, write the flux linkage first**: Nφ = NBA cos ωt. Then differentiate. Do not
   start from ε = NBAω sin ωt.

4. **Answer the "when is emf maximum" sub-part**, and phrase it in terms of the **plane** of the coil
   relative to **B**. It appears almost every time this question is set.

5. **If asked why slip rings rather than a commutator:** slip rings keep each coil end tied to the
   same brush, so the output alternates; a split-ring commutator would reverse the connection each
   half-cycle and give DC.

**On Lenz's law**

6. **Give the reason, not just the direction.** The mark is for "so that the near face becomes a north
   pole, repelling the approaching magnet and thereby opposing the increase in flux".

7. **For the energy-conservation question, argue by contradiction.** Suppose the induced current
   aided the change → the magnet accelerates → more current → more acceleration → energy from
   nothing. State that explicitly; it is the whole answer.

8. **Name the law you are invoking.** "By Lenz's law…" — examiners look for it.

**On the inductance derivations**

9. **Start from B = μ₀nI, then flux through one turn, then flux linkage through N turns, then compare
   with LI.** Four steps, and each is marked. Do not jump to L = μ₀N²A/l.

10. **Substitute N = nl explicitly** — it is the algebraic step that converts μ₀n²Al into μ₀N²A/l, and
    it is easy to show.

11. **Answer the "on what factors does it depend" part with a numbered list**, and include the core
    material. And note that L is **independent of the current** — that is often the intended catch.

12. **For mutual inductance, state the reciprocity property** M₁₂ = M₂₁, and note M is zero for
    perpendicular axes.

**On numericals**

13. **Convert cm² to m² by 10⁻⁴, not 10⁻².** 100 cm² = 10⁻² m². This is the single most common unit
    slip in this chapter.

14. **Watch what "plane perpendicular to the field" means.** If the *plane* of the coil is
    perpendicular to **B**, then the *normal* is **parallel** to **B**, so θ = 0 and φ = BA (maximum).
    State which you are using.

15. **For charge questions, use q = NΔφ/R**, and point out that it is independent of the time taken.
    That observation is often the marked part of the question.

16. **Units:** Wb for flux, V for emf, H for inductance, C for charge, J for stored energy.
