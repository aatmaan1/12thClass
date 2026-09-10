# Ch 5 — Magnetism and Matter

**Units III + IV (17 marks, shared with Ch 4, 6, 7) · Typical appearance: one 1-mark MCQ, sometimes a
2-mark question on Earth's magnetic elements or material types. Rarely more.**

**This is the smallest and lowest-yield chapter in Physics. Budget two days, not two weeks.**

---

## 1. Scope

### In the syllabus

The official CBSE line for this chapter is short:

- **Bar magnet as an equivalent solenoid**; **magnetic field lines**
- **Earth's magnetic field and magnetic elements**

Alongside these, two things are routinely examined at 1–2 mark level and cost almost nothing to
learn, so they are included below:

- **Torque on a magnetic dipole**, τ = **m** × **B** — this is the same physics as *torque on a
  current loop*, which is explicitly in [Ch 4](04-moving-charges-and-magnetism.md)
- The **qualitative** comparison of **para-, dia- and ferromagnetic** substances

### Deleted — do not study

- **Magnetic susceptibility** (χ) and **permeability** (μ, μ_r), and the relations between them
- **Magnetisation** M and magnetic intensity H, and the relation B = μ₀(H + M)
- **Hysteresis** loops, retentivity, coercivity
- **Electromagnets**, the factors affecting their strength, and **permanent magnets**
- **Magnetic dipole moment of a revolving electron**
- Magnetic field of a **bar magnet** along its **axial** and **equatorial** lines (the analogue of the
  electric dipole formulas)
- Tangent galvanometer; oscillation-of-a-magnet timing experiments

> **A note on scope, honestly stated.** This chapter's syllabus line has been trimmed more than once,
> and different publishers disagree about exactly what survived. What is certain: the whole
> **quantitative magnetic-materials** block (χ, μ_r, M, H, hysteresis, electromagnets) is out, and
> so are the bar-magnet axial/equatorial field formulas. What is certain to *stay*: bar magnet as an
> equivalent solenoid, field lines, and Earth's magnetism.
>
> **Practical advice:** learn the short retained list properly, know τ = **m** × **B** and the
> qualitative material table, and do **not** invest time in χ, μ_r or hysteresis. Then check the
> current year's CBSE syllabus PDF to confirm. Given the chapter is worth roughly 1–3 marks, this is
> not a place to spend more effort than that.

---

## 2. Brief

### Start here — in plain English

A compass has worked for a thousand years and the reason is that the Earth is, roughly, a very large
bar magnet with its south pole buried under the northern hemisphere. This chapter is about magnets
as objects — what they are made of, what they do in a field, and why some materials become magnets
and others refuse.

The first thing to be clear about: **there is no such thing as a single magnetic pole.** Snap a bar
magnet in half and you do not get a loose north and a loose south; you get two smaller magnets, each
with both. Cut again and again, and you never separate them. This is the deep difference from
electricity, where isolated positive and negative charges are everywhere. In field-line language it
means magnetic field lines never start or stop anywhere — they always close on themselves, passing
through the magnet and back around outside.

So a magnet's basic unit is not a pole but a **dipole**, described by its magnetic moment m. And if
you compare a bar magnet's field pattern with a current loop's, they are identical. That is the
chapter's central insight and it is not a coincidence: **a magnet's magnetism comes from currents**
— electrons circulating inside atoms. There is no magnetic "stuff", only moving charge.

Because a magnet is a dipole, everything you learned about an electric dipole in Chapter 1 carries
across unchanged. In a uniform field the forces on the two ends are equal and opposite, so the
magnet does not move; it **twists** until it lines up, with torque τ = mB sin θ. Its potential
energy is U = −mB cos θ, lowest when aligned and highest when reversed, which is why a compass
settles pointing north and stays there.

**Earth's magnetism** is described by three numbers, and they are all just "how is the field
oriented here?" The **declination** is how far magnetic north is from true north as you look down at
a map. The **dip** (or inclination) is how far the field tilts down into the ground — nearly zero at
the equator, nearly vertical at the poles. The **horizontal component** is the part of the field
lying flat, which is the only part a compass needle floating on a pivot can respond to. The relation
B_H = B cos δ is trigonometry, nothing more.

Then the materials. Every atom is a tiny current loop, so every material responds to a field
somehow; the question is how. **Diamagnetic** materials (water, copper, bismuth) have atoms whose
internal currents cancel, so they have no moment of their own; an applied field induces a weak
opposing one, and they are pushed feebly *out* of the field. **Paramagnetic** materials (aluminium,
oxygen) have atoms with a small permanent moment each, but thermal jostling keeps them randomly
pointed; a field lines up a few of them and they are pulled weakly *in*. **Ferromagnetic** materials
(iron, cobalt, nickel) are the dramatic case: neighbouring atoms lock their moments parallel over
whole regions called domains, so a modest field can align enormous numbers at once and the material
becomes strongly magnetised — and stays that way. Heat any ferromagnet past its Curie temperature
and the locking breaks; it turns paramagnetic and forgets it was ever a magnet.

> **Check the scope before you invest time here.** In the rationalised syllabus much of the
> magnetic-materials treatment — and the hysteresis loop in particular — has been trimmed. This
> chapter's §1 lists what is in and what is out; read it first. The examinable core is the bar
> magnet as a dipole, torque and energy, and Earth's magnetic elements.

**Learn it from someone else too**

- **Video lecture** — [search: magnetism and matter class 12 one shot](https://www.youtube.com/results?search_query=magnetism+and+matter+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: magnetism and matter](https://www.khanacademy.org/search?page_search_query=magnetism%20and%20matter%20class%2012)
- **The book the paper is set from** — [NCERT Physics Part I, Chapter 5 (PDF)](https://ncert.nic.in/textbook/pdf/leph105.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 36 *Permanent Magnets* §36.1–36.6 for poles,
  dipole moment and Earth's field; Ch 37 *Magnetic Properties of Matter* for the three classes of
  material. Read only as far as your syllabus scope goes.

---

### Magnetic field lines — properties

1. They form **continuous closed loops** — unlike electric field lines, which start and end on
   charges.
2. Outside a magnet they run from the **north pole to the south pole**; **inside** the magnet they run
   from **south to north**, completing the loop.
3. The **tangent** at any point gives the direction of **B** there.
4. **Two field lines never intersect** (otherwise **B** would have two directions at one point).
5. Their **density** indicates the field strength.

**Gauss's law for magnetism:**

```
      ∮ B · dA = 0
```

The net magnetic flux through any closed surface is **always zero**. Physically: **isolated magnetic
poles (magnetic monopoles) do not exist** — every field line that enters a closed surface also leaves
it. This is the fundamental contrast with electrostatics, where ∮**E**·d**A** = q/ε₀ can be non-zero.

### Bar magnet as an equivalent solenoid

A **current-carrying solenoid** and a **bar magnet** produce essentially identical external field
patterns. This is the basis for treating a bar magnet as a magnetic dipole.

**The argument:** each turn of a solenoid is a small current loop, and a current loop is a magnetic
dipole of moment m = IA. A solenoid is therefore a stack of such dipoles, giving a net dipole moment
along its axis — exactly like a bar magnet, whose atomic current loops (electron orbits and spins)
align to give a net moment.

For a solenoid of N turns, length 2l, radius a, carrying current I, the field at an axial point far
away (r >> l) is

```
      B = (μ₀/4π) · 2m/r³               where  m = N I A = N I (πa²)
```

which is identical in form to the axial field of a bar magnet of moment m. Hence a bar magnet
behaves as an **equivalent solenoid**.

**Consequences that get asked:**

- A bar magnet's poles are not isolated points; **cutting a bar magnet in two gives two complete
  magnets**, each with a north and a south pole. You can never obtain an isolated pole.
- The **magnetic dipole moment** of a bar magnet is m = q_m × 2l (pole strength × length), directed
  from S to N inside the magnet.

### Torque on a magnetic dipole in a uniform field

```
      τ = m B sin θ                 vector form:  τ = m × B
```

- **Net force** on the dipole in a **uniform** field is **zero**; only a torque acts.
- τ is **maximum** (= mB) at θ = 90°, and **zero** at θ = 0° and 180°.
- **Potential energy:** U = −mB cos θ = −**m**·**B**.
  Stable equilibrium at θ = 0° (aligned with the field); unstable at θ = 180°.
- **Work done in rotating** from θ₁ to θ₂: W = mB(cos θ₁ − cos θ₂).

*(Note this is exactly the electric-dipole result of
[Ch 2](02-electrostatic-potential-and-capacitance.md) with p → m and E → B. Learn one, get both.)*

### Earth's magnetic field and magnetic elements

The Earth behaves approximately as a giant **magnetic dipole** whose axis is tilted about 11° to its
rotational axis. Its **magnetic south pole** lies near the **geographic north** — which is why a
compass needle's north pole points north.

The Earth's field at a place is specified by **three magnetic elements**:

**1. Declination (θ or D).** The angle between the **geographic meridian** (the vertical plane
containing the geographic north–south line) and the **magnetic meridian** (the vertical plane
containing the magnetic field direction).

**2. Dip / inclination (δ or I).** The angle that the Earth's total field **B** makes with the
**horizontal** at that place.

**3. Horizontal component (B_H).** The horizontal component of the Earth's field, i.e. the component
along the magnetic meridian.

**The relations — this is the examinable content:**

```
      B_H = B cos δ
      B_V = B sin δ
      tan δ = B_V/B_H
      B = √(B_H² + B_V²)
```

**Special values:**

| Place | Dip δ | Notes |
| --- | --- | --- |
| **Magnetic equator** | 0° | B_V = 0, so B = B_H — the field is entirely horizontal; a dip needle stays horizontal |
| **Magnetic poles** | 90° | B_H = 0, so B = B_V — the field is entirely vertical; a compass needle is useless |
| Intermediate latitudes | 0° < δ < 90° | both components present |

> **The standard question** is "at a place the dip is 30° and the horizontal component is
> 0.34 × 10⁻⁴ T; find the total field and the vertical component." It is one line each from the
> relations above.

### Para-, dia- and ferromagnetic substances (qualitative)

| | **Diamagnetic** | **Paramagnetic** | **Ferromagnetic** |
| --- | --- | --- | --- |
| Behaviour in a field | **weakly repelled** | **weakly attracted** | **strongly attracted** |
| Net atomic dipole moment | **zero** | small, non-zero, randomly oriented | non-zero, aligned in domains |
| In a non-uniform field | moves from strong to **weak** field | moves from weak to **strong** field | moves strongly to the **strong** field |
| Field lines | tend to be **expelled** from the material | slightly **concentrated** in it | strongly **concentrated** in it |
| Effect of temperature | almost none | magnetisation decreases as T rises | loses ferromagnetism above the **Curie temperature** |
| Examples | bismuth, copper, water, gold, mercury | aluminium, sodium, oxygen, platinum | iron, cobalt, nickel, gadolinium |

**The mechanism, in one line each:**
- **Diamagnetic:** atoms have no net moment; an applied field *induces* a moment that **opposes** it
  (Lenz's law at the atomic level), so the substance is repelled.
- **Paramagnetic:** atoms have permanent moments that are randomly oriented; an applied field
  **partially aligns** them, so the substance is weakly attracted. Thermal agitation opposes this
  alignment, hence the temperature dependence.
- **Ferromagnetic:** atomic moments are already aligned within **domains**; an applied field aligns
  whole domains, giving a very strong effect.

### Quick recall box

```
FIELD LINES: continuous CLOSED loops ; N→S outside, S→N inside ; never intersect
∮B·dA = 0  ⟹  no magnetic monopoles exist        (contrast: ∮E·dA = q/ε₀)

BAR MAGNET ≡ SOLENOID
  m = NIA for a solenoid ;  m = q_m × 2l for a bar magnet, directed S → N inside
  cutting a magnet gives TWO complete magnets — an isolated pole is impossible

DIPOLE IN A FIELD: τ = mB sin θ = m × B ;  net force = 0 in a uniform field
  U = −mB cos θ = −m·B ;  stable at θ = 0°, unstable at 180°
  W(θ₁ → θ₂) = mB(cos θ₁ − cos θ₂)

EARTH'S MAGNETIC ELEMENTS: declination, dip (δ), horizontal component (B_H)
  B_H = B cos δ        B_V = B sin δ
  tan δ = B_V/B_H      B = √(B_H² + B_V²)
  magnetic equator: δ = 0°, B = B_H     magnetic poles: δ = 90°, B = B_V
  Earth's magnetic SOUTH pole is near the geographic NORTH

MATERIALS: dia — weakly REPELLED, no net atomic moment
           para — weakly ATTRACTED, random permanent moments, T-dependent
           ferro — STRONGLY attracted, domains, loses it above the Curie temperature
```

---

## 3. Previous years' questions

**Q1.** *(2 marks)* Define the magnetic elements of the Earth at a place. Write the relation between
the dip, the horizontal component and the total field.

**Q2.** *(2 marks)* At a certain place the horizontal component of the Earth's magnetic field is
0.34 × 10⁻⁴ T and the angle of dip is 30°. Find the total intensity of the Earth's field and its
vertical component.

**Q3.** *(3 marks)* Explain why a bar magnet may be regarded as an equivalent solenoid. What does
this imply about isolated magnetic poles?

**Q4.** *(2 marks)* State any three properties of magnetic field lines. How do they differ from
electric field lines?

**Q5.** *(2 marks)* Write Gauss's law for magnetism and state its physical significance.

**Q6.** *(3 marks)* Distinguish between diamagnetic, paramagnetic and ferromagnetic substances,
giving one example of each.

**Q7.** *(2 marks)* A bar magnet of magnetic moment 0.5 A m² is placed at 60° to a uniform field of
0.2 T. Find the torque acting on it.

**Q8.** *(2 marks)* What is the angle of dip at the magnetic equator and at the magnetic poles?
Justify.

**Q9.** *(1 mark, MCQ)* The net magnetic flux through any closed surface is
(a) q/ε₀ (b) μ₀I (c) zero (d) BA

**Q10.** *(2 marks)* A bar magnet is cut into two equal halves perpendicular to its length. What
happens to its magnetic dipole moment? Explain.

**Q11.** *(1 mark, Assertion–Reason)*
**A:** A ferromagnetic substance loses its ferromagnetic properties above a certain temperature.
**R:** Thermal agitation destroys the alignment of domains above the Curie temperature.

**Q12.** *(2 marks)* Find the work done in rotating a magnet of dipole moment 2 A m² from a position
parallel to a field of 0.5 T to a position antiparallel to it.

---

## 4. Solutions

### Q1 — magnetic elements of the Earth

The Earth's magnetic field at a place is completely specified by three quantities, the **magnetic
elements**:

**1. Magnetic declination** — the angle between the **geographic meridian** and the **magnetic
meridian** at that place. (Equivalently, the angle by which a compass needle deviates from the true
geographic north–south direction.)

**2. Angle of dip (inclination)** — the angle δ that the Earth's total magnetic field **B** makes
with the **horizontal direction** at that place.

**3. Horizontal component** B_H — the component of the Earth's total field in the horizontal
direction, along the magnetic meridian.

**Relations:**

```
      B_H = B cos δ                 B_V = B sin δ

      tan δ = B_V/B_H               B = √(B_H² + B_V²)
```

### Q2 — total field and vertical component

```
      B_H = 0.34 × 10⁻⁴ T           δ = 30°
```

**Total field:**

```
      B_H = B cos δ
⟹     B = B_H/cos δ = (0.34 × 10⁻⁴)/cos 30°
        = (0.34 × 10⁻⁴)/(0.866)
        = 3.93 × 10⁻⁵ T
```

**B ≈ 3.93 × 10⁻⁵ T = 0.393 × 10⁻⁴ T**

**Vertical component:**

```
      B_V = B sin δ = (3.93 × 10⁻⁵)(0.5) = 1.96 × 10⁻⁵ T
```

**B_V ≈ 1.96 × 10⁻⁵ T = 0.196 × 10⁻⁴ T**

*(Check with tan δ = B_V/B_H: (1.96 × 10⁻⁵)/(3.4 × 10⁻⁵) = 0.577 = tan 30° ✓)*

*(Alternatively and more directly: B_V = B_H tan δ = (0.34 × 10⁻⁴)(0.577) = 1.96 × 10⁻⁵ T.)*

### Q3 — bar magnet as an equivalent solenoid

*Diagram:* draw a bar magnet with its external field lines, and beside it a current-carrying solenoid
with its external field lines — showing that the two patterns are identical, with one end of the
solenoid behaving as a north pole and the other as a south pole.

**The reasoning.**

A **single current loop** is a magnetic dipole, of moment m = IA directed along its normal.

A **solenoid** is a stack of many such closely-wound loops, all carrying the same current in the same
sense. Their dipole moments therefore all point the same way, along the solenoid's axis, and add to
give a net moment

```
      m = N I A
```

for N turns of area A. The **external field pattern** of a solenoid is found experimentally — and
can be shown by calculation — to be identical in form to that of a bar magnet: field lines emerge
from one end (behaving as a **north pole**) and re-enter at the other (a **south pole**).

Quantitatively, for a solenoid of N turns and half-length l, at an axial point far away (r >> l):

```
      B = (μ₀/4π) · 2m/r³
```

which has **exactly the same form** as the axial field of a magnetic dipole of moment m. Hence a bar
magnet can be regarded as an equivalent solenoid.

**Physical basis.** In a bar magnet, the magnetism arises from the **atomic current loops** — the
orbital motion and spin of electrons — each of which is a tiny magnetic dipole. When these align, as
they do in a ferromagnet, their combined effect is that of a solenoid.

**Implication for isolated poles.** Since a magnet's magnetism arises from **current loops**, and a
current loop has no isolated poles, **an isolated magnetic pole cannot exist**. Cutting a bar magnet
in two does not separate a north pole from a south pole — it simply produces **two complete magnets**,
each with its own north and south pole. This is consistent with Gauss's law for magnetism,
∮**B**·d**A** = 0.

### Q4 — properties of magnetic field lines, and the contrast with electric

**Properties (any three):**

1. Magnetic field lines form **continuous closed loops**.
2. Outside a magnet they run from the **north pole to the south pole**; **inside** the magnet, from
   **south to north**.
3. **Two field lines never intersect** — otherwise the field would have two directions at one point.
4. The **tangent** at any point gives the direction of **B**; the **density** of lines indicates its
   magnitude.

**Difference from electric field lines.**

| Magnetic field lines | Electric field lines |
| --- | --- |
| Form **closed loops** | **Start** on positive charges and **end** on negative charges — they are not closed |
| ∮**B**·d**A** = 0 always — no monopoles | ∮**E**·d**A** = q/ε₀ — isolated charges exist |

### Q5 — Gauss's law for magnetism

```
      ∮ B · dA = 0
```

**Statement:** the net magnetic flux through any **closed** surface is always **zero**.

**Physical significance:** it expresses the fact that **isolated magnetic poles (magnetic monopoles)
do not exist**. Because magnetic field lines are closed loops, every line that enters a closed
surface must also leave it, so the inward and outward fluxes cancel exactly.

This is the fundamental difference from electrostatics: there, ∮**E**·d**A** = q_enclosed/ε₀ can be
non-zero, because isolated electric charges do exist.

### Q6 — distinguishing the three types of magnetic substance

| Property | Diamagnetic | Paramagnetic | Ferromagnetic |
| --- | --- | --- | --- |
| **Behaviour in a magnetic field** | weakly **repelled** | weakly **attracted** | **strongly attracted** |
| **Net atomic magnetic moment** | **zero** | small and non-zero, but randomly oriented | non-zero and aligned within domains |
| **Effect of temperature** | essentially none | magnetisation falls as temperature rises | loses ferromagnetism above the **Curie temperature** |
| **Example** | bismuth (also copper, water) | aluminium (also sodium, oxygen) | iron (also cobalt, nickel) |

*(Note the table compares the **same** property on each row — that is what the marking scheme wants.
Three properly parallel rows plus examples is a full 3-mark answer.)*

### Q7 — torque on a bar magnet

```
      m = 0.5 A m²          B = 0.2 T          θ = 60°
```

```
      τ = m B sin θ
        = (0.5)(0.2)(sin 60°)
        = (0.1)(0.866)
        = 0.0866 N m
```

**τ ≈ 8.66 × 10⁻² N m**, directed perpendicular to the plane containing **m** and **B**.

### Q8 — dip at the equator and at the poles

**At the magnetic equator, δ = 0°.**

The Earth's field there is entirely **horizontal**, so the vertical component B_V = 0. Since
tan δ = B_V/B_H = 0, we get δ = 0°. A dip needle placed at the magnetic equator therefore rests
**horizontally**, and B = B_H.

**At the magnetic poles, δ = 90°.**

There the field is entirely **vertical**, so the horizontal component B_H = 0. Since
tan δ = B_V/B_H → ∞, we get δ = 90°. A dip needle at a magnetic pole stands **vertically**, and
B = B_V. (This is also why an ordinary compass, which relies on B_H, is useless near the magnetic
poles.)

### Q9 — net magnetic flux through a closed surface

**Answer: (c) zero**

This is Gauss's law for magnetism, and it reflects the non-existence of magnetic monopoles.

### Q10 — bar magnet cut in half perpendicular to its length

*(Cut perpendicular to the length, i.e. across the magnet, halving its length.)*

The pole strength q_m depends on the **cross-sectional area**, which is **unchanged** by this cut. The
length, however, is **halved**: 2l → l.

Since m = q_m × (length),

```
      m′ = q_m × l = m/2
```

**The magnetic dipole moment of each half is halved.**

Each piece is still a **complete magnet**, with its own north and south pole — you do not obtain
isolated poles.

*(Contrast: if the magnet were cut **along** its length instead, the length would be unchanged but
the cross-sectional area would be halved, so the pole strength — and hence the moment — would also
be halved. Both cuts halve m, but for different reasons; read which cut the question specifies.)*

### Q11 — Assertion–Reason

**A:** "A ferromagnetic substance loses its ferromagnetic properties above a certain temperature."
**True** — above the **Curie temperature** a ferromagnet becomes paramagnetic.

**R:** "Thermal agitation destroys the alignment of domains above the Curie temperature." **True** —
that is the mechanism.

**Does R explain A?** Yes. Ferromagnetism depends on the alignment of magnetic domains; when thermal
energy exceeds the energy holding the domains aligned, the alignment is destroyed and the strong
magnetism disappears.

**Answer: (a) Both A and R are true, and R is the correct explanation of A.**

### Q12 — work done in rotating a magnet from parallel to antiparallel

```
      m = 2 A m²          B = 0.5 T          θ₁ = 0°          θ₂ = 180°
```

```
      W = m B (cos θ₁ − cos θ₂)
        = (2)(0.5)(cos 0° − cos 180°)
        = (1)(1 − (−1))
        = 2 J
```

**W = 2 J**

*(This is the maximum possible work for this magnet and field — it takes the dipole from stable
equilibrium, U = −mB = −1 J, to unstable equilibrium, U = +mB = +1 J, a change of 2 J ✓)*

---

## 5. Test yourself

Time: 25 minutes. Answers below.

1. *(1)* The angle of dip at the magnetic equator is
   (a) 0° (b) 45° (c) 90° (d) 11°
2. *(1)* Which of the following is diamagnetic?
   (a) iron (b) aluminium (c) bismuth (d) nickel
3. *(1)* The SI unit of magnetic dipole moment is
   (a) A m (b) A m² (c) T (d) Wb
4. *(2)* Write two properties in which magnetic field lines differ from electric field lines.
5. *(2)* At a place the vertical and horizontal components of the Earth's field are equal. Find the
   angle of dip.
6. *(2)* Why does a compass needle fail to work near the magnetic poles of the Earth?
7. *(2)* A magnet of moment 1.5 A m² is held at 90° to a field of 0.4 T. Find the torque, and the work
   done in bringing it to the aligned position.
8. *(3)* Explain, in terms of atomic magnetic moments, why a diamagnetic substance is repelled and a
   paramagnetic substance is attracted by a magnetic field.
9. *(2)* State Gauss's law for magnetism and explain what it implies.
10. *(2)* The horizontal component of the Earth's field at a place is 0.3 × 10⁻⁴ T and the dip is 60°.
    Find the total field.
11. *(2)* A bar magnet is cut into three equal pieces perpendicular to its length. What is the dipole
    moment of each piece, in terms of the original m?

### Answer key

**1. (a) 0°.**

**2. (c) bismuth.**

**3. (b) A m².**

**4.** (i) Magnetic field lines form **closed loops**, whereas electric field lines **begin and end on
charges**. (ii) The net magnetic flux through any closed surface is always **zero** (no monopoles),
whereas the net electric flux equals q_enclosed/ε₀ and can be non-zero.

**5. 45°.** tan δ = B_V/B_H = 1, so δ = 45°.

**6.** A compass needle aligns with the **horizontal component** B_H of the Earth's field. At the
magnetic poles the field is entirely vertical, so **B_H = 0** and there is no horizontal component to
align with — the needle has no preferred horizontal direction and the compass is useless.

**7. τ = 0.6 N m; W = −0.6 J (i.e. 0.6 J is released).**
τ = mB sin 90° = (1.5)(0.4)(1) = 0.6 N m.
W = mB(cos θ₁ − cos θ₂) = (0.6)(cos 90° − cos 0°) = (0.6)(0 − 1) = −0.6 J.
The negative sign means the field does the work — the magnet moves *towards* stable equilibrium
spontaneously, releasing 0.6 J.

**8.** **Diamagnetic:** the atoms have **no net magnetic moment**. When an external field is applied,
it induces a moment in each atom that **opposes** the applied field (an atomic-scale expression of
Lenz's law). The induced moments therefore experience a force pushing the material towards the
**weaker** part of the field — the substance is **repelled**.
**Paramagnetic:** the atoms have **permanent** magnetic moments, but these are **randomly oriented**
by thermal agitation, so the net moment is normally zero. An applied field **partially aligns** them
with itself, giving a net moment **along** the field, so the substance is pulled towards the
**stronger** part of the field — it is **attracted**.

**9.** ∮**B**·d**A** = 0: the net magnetic flux through any closed surface is zero. It implies that
**isolated magnetic poles do not exist** — magnetic field lines are closed, so every line entering a
closed surface also leaves it.

**10. 0.6 × 10⁻⁴ T.** B = B_H/cos δ = (0.3 × 10⁻⁴)/cos 60° = (0.3 × 10⁻⁴)/0.5 = 0.6 × 10⁻⁴ T.

**11. m/3 each.** Cutting perpendicular to the length leaves the cross-sectional area (and hence the
pole strength q_m) unchanged, but divides the length by 3. Since m = q_m × length, each piece has
moment **m/3**. Each is a complete magnet with both poles.

**Scoring.** Out of 20. Below 14 → the only things worth going back for are the Earth's-magnetism
relations and the three-material table. That is genuinely all this chapter owes you.

---

## 6. Answering tips

1. **Do not over-invest in this chapter.** It carries roughly 1–3 marks. Learn the Earth's-magnetism
   triangle, the material table, and the field-line properties, and put the rest of your time into
   [Ch 9 Ray Optics](09-ray-optics-and-optical-instruments.md) and
   [Ch 14](14-semiconductor-electronics.md), which carry 17 marks between them.

2. **For Earth's magnetism, draw the right triangle.** B as the hypotenuse, B_H horizontal, B_V
   vertical, angle δ between B and B_H. Every question here is one trigonometric step from that
   triangle, and drawing it prevents mixing up sin and cos.

3. **Use B_V = B_H tan δ when both B_H and δ are given** — it is one step rather than two.

4. **For "distinguish between" questions, use a table** and compare the **same** property on each
   row. Three parallel rows plus one example each is a full 3-mark answer. Comparing different
   attributes on the two sides scores badly.

5. **Always give examples** when asked to distinguish materials — bismuth/copper for diamagnetic,
   aluminium/sodium for paramagnetic, iron/cobalt/nickel for ferromagnetic. The examples are worth a
   mark.

6. **For the bar-magnet-as-solenoid question, the diagram is the answer.** Draw both field patterns
   side by side and label the effective poles of the solenoid.

7. **On cutting a magnet, say what happens to the pole strength and what happens to the length**
   separately, then combine. And always add the sentence "each piece is a complete magnet with both
   poles" — it is the conceptual mark.

8. **When contrasting with electrostatics, name the contrast explicitly:** closed loops vs
   start-and-end on charges, and ∮**B**·d**A** = 0 vs ∮**E**·d**A** = q/ε₀. Those two pairings answer
   most comparison questions in this chapter.

9. **Do not use χ, μ_r, M or H in your answers.** They are out of syllabus, and an answer framed in
   terms of them may not match the marking scheme even if it is physically correct.
