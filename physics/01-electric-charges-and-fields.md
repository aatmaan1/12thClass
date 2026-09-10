# Ch 1 — Electric Charges and Fields

**Units I + II (16 marks, shared with Ch 2 and Ch 3) · Typical appearance: 1–2 MCQs + a 2-mark flux
or dipole question, and often the 5-mark Gauss's law derivation-plus-application.**

---

## 1. Scope

### In the syllabus

- Electric charges; **conservation of charge**
- **Coulomb's law** — force between two point charges; forces between multiple charges;
  **superposition principle**; continuous charge distribution
- **Electric field**; field due to a point charge; **electric field lines**
- **Electric dipole**; field due to a dipole; **torque** on a dipole in a uniform field
- **Electric flux**; statement of **Gauss's theorem** and its applications to find the field due to
  - an infinitely long straight **wire**
  - a uniformly charged infinite plane **sheet**
  - a uniformly charged thin **spherical shell** (field inside and outside)

### Deleted

Nothing substantial was removed from this chapter beyond what was already out of the
senior-secondary course. (The Van de Graaff generator, sometimes taught alongside, belongs to Ch 2
and **is** deleted.)

---

## 2. Brief

### Properties of electric charge

| Property | Statement |
| --- | --- |
| **Quantisation** | q = ne, where n is an integer and e = 1.6 × 10⁻¹⁹ C |
| **Conservation** | The total charge of an isolated system is constant |
| **Additivity** | Charge is a scalar and adds algebraically |

### Coulomb's law

The force between two point charges q₁ and q₂ separated by r, in vacuum:

```
      F = (1/4πε₀) · q₁q₂/r²  =  k q₁q₂/r²
```

```
      k = 1/4πε₀ = 9 × 10⁹ N m² C⁻²          ε₀ = 8.854 × 10⁻¹² C² N⁻¹ m⁻²
```

**Vector form** (force on charge 2 due to charge 1):

```
      F₂₁ = (1/4πε₀) (q₁q₂/r²) r̂₂₁
```

**In a medium** of dielectric constant (relative permittivity) K:

```
      F_medium = F_vacuum / K
```

so the force is always **reduced** in a medium.

**Superposition principle.** The force on a charge due to several others is the **vector sum** of the
forces due to each one taken separately, each computed as if the others were absent.

### Electric field

```
      E = F/q₀                      (force per unit positive test charge)
      E = (1/4πε₀) q/r²             (due to a point charge q, at distance r)
```

**E is a vector**, with SI unit N C⁻¹ (equivalently V m⁻¹).

**Properties of electric field lines** (a standard 2-mark question):

1. They start on **positive** charges and end on **negative** charges.
2. They are **continuous** curves without breaks in a charge-free region.
3. **Two field lines never intersect** — if they did, there would be two directions of E at that
   point, which is impossible.
4. They do not form **closed loops** (a consequence of the electrostatic field being conservative).
5. The **tangent** at any point gives the direction of E there; the **density** of lines gives the
   magnitude.
6. They are always **perpendicular to the surface of a conductor** in electrostatics.
7. **Equidistant parallel lines** represent a uniform field.

### Electric dipole

Two equal and opposite charges +q and −q separated by 2a.

```
      Dipole moment  p = q(2a)              direction: from −q towards +q
```

SI unit: C m. Note the direction convention — it is asked.

**Field on the axial line** (on the line joining the charges, at distance r from the centre):

```
      Exact:            E = (1/4πε₀) · 2pr/(r² − a²)²
      For r >> a:       E = (1/4πε₀) · 2p/r³
```

Direction: **along p** (parallel to the dipole moment).

**Field on the equatorial line** (perpendicular bisector, at distance r from the centre):

```
      Exact:            E = (1/4πε₀) · p/(r² + a²)^(3/2)
      For r >> a:       E = (1/4πε₀) · p/r³
```

Direction: **antiparallel to p**.

> **Two facts that get asked directly.** (i) The axial field is **twice** the equatorial field at the
> same distance, for a short dipole. (ii) A dipole field falls off as **1/r³**, faster than the 1/r²
> of a point charge — because the two opposite charges partly cancel at large distances.

**Torque on a dipole in a uniform field E:**

```
      τ = pE sin θ                  vector form:  τ = p × E
```

where θ is the angle between **p** and **E**.

- **Net force** on a dipole in a **uniform** field is **zero** (the two forces are equal and
  opposite) — but the net torque is not, so the dipole rotates without translating.
- τ is **maximum** (= pE) when θ = 90°, and **zero** when θ = 0° or 180°.
- **Stable equilibrium** at θ = 0° (p parallel to E); **unstable** at θ = 180°.

### Electric flux

```
      dφ = E · dA = E dA cos θ                φ = ∮ E · dA
```

θ is the angle between **E** and the **area vector** (the outward normal to the surface).

SI unit: N m² C⁻¹ (equivalently V m).

Flux is a **scalar**. It is positive for outward field, negative for inward.

### Gauss's theorem

**Statement.** The total electric flux through any **closed** surface equals 1/ε₀ times the total
charge **enclosed** by that surface.

```
      φ = ∮ E · dA = q_enclosed / ε₀
```

**Key consequences that get asked:**

- The flux depends **only on the enclosed charge** — not on the shape or size of the surface, and
  not on charges **outside** it (those contribute zero net flux).
- A closed surface with no charge inside has **zero net flux**, even if there is a field passing
  through it.

**Choosing the Gaussian surface.** The whole art is picking a surface on which E has constant
magnitude and a simple angle to the normal — which means matching the symmetry of the charge
distribution. **You must state this choice and its justification** — it is a mark.

### The three Gauss's law applications

These three derivations are the backbone of the chapter. Learn all three.

**(a) Infinitely long straight charged wire**, linear charge density λ (C m⁻¹).

*Gaussian surface:* a **coaxial cylinder** of radius r and length l.
*Symmetry:* E is radial and has the same magnitude everywhere on the curved surface; the flux
through the two flat ends is zero because E is parallel to those surfaces.

```
      φ = E × (2πrl)          and         q_enclosed = λl

      E (2πrl) = λl/ε₀
⟹     E = λ/(2πε₀ r)          i.e.  E ∝ 1/r
```

**(b) Uniformly charged infinite plane sheet**, surface charge density σ (C m⁻²).

*Gaussian surface:* a **cylinder (or cuboid) with its flat faces parallel to the sheet**, one on each
side.
*Symmetry:* E is perpendicular to the sheet and the same magnitude on both faces; the curved surface
contributes no flux.

```
      φ = E A + E A = 2EA          and         q_enclosed = σA

      2EA = σA/ε₀
⟹     E = σ/(2ε₀)
```

**E is independent of the distance from the sheet** — a uniform field. That independence is the
asked fact.

*(For a charged conducting plate with charge on both surfaces, the field just outside is
E = σ/ε₀ — twice as large. Read the question for which case is meant.)*

**(c) Uniformly charged thin spherical shell** of radius R with total charge q.

*Gaussian surface:* a **concentric sphere** of radius r.

**Outside (r > R):**

```
      E (4πr²) = q/ε₀
⟹     E = (1/4πε₀) q/r²
```

— identical to the field of a point charge q at the centre.

**Inside (r < R):**

```
      q_enclosed = 0
⟹     E = 0
```

**The field inside a uniformly charged spherical shell is zero.** This appears as an MCQ or
Assertion–Reason almost every year on its own.

**On the surface (r = R):** E = (1/4πε₀) q/R² = σ/ε₀.

### Conductors in electrostatic equilibrium

- The electric field **inside** a conductor is **zero**.
- All excess charge resides on the **outer surface**.
- The field just outside is **perpendicular** to the surface, of magnitude σ/ε₀.
- The whole conductor (including its surface) is at the **same potential**.

### Quick recall box

```
q = ne,  e = 1.6 × 10⁻¹⁹ C          k = 1/4πε₀ = 9 × 10⁹ N m² C⁻²
ε₀ = 8.854 × 10⁻¹² C² N⁻¹ m⁻²

Coulomb :  F = k q₁q₂/r²      F_medium = F_vacuum/K
Field   :  E = F/q₀ = k q/r²          unit N C⁻¹ = V m⁻¹

DIPOLE :  p = q(2a), directed from −q to +q
  axial      (r >> a) : E = 2kp/r³        along p
  equatorial (r >> a) : E = kp/r³         antiparallel to p
  axial = 2 × equatorial ;  dipole field ∝ 1/r³
  torque τ = pE sin θ = p × E ;  net force in a uniform field = 0
  stable at θ = 0°, unstable at θ = 180°

FLUX :  φ = ∮E·dA = EA cos θ            unit N m² C⁻¹
GAUSS:  φ = q_enclosed/ε₀               (independent of surface shape; outside charges give 0)

  infinite wire  :  E = λ/(2πε₀ r)          ∝ 1/r
  infinite sheet :  E = σ/(2ε₀)             independent of distance
  spherical shell:  outside E = kq/r² ;  INSIDE E = 0 ;  surface E = σ/ε₀

CONDUCTOR: E = 0 inside ; charge on outer surface ; E ⊥ surface, magnitude σ/ε₀
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* State Gauss's theorem. Using it, derive an expression for the electric field due
to a uniformly charged infinite plane sheet of surface charge density σ.

**Q2.** *(5 marks)* Using Gauss's law, obtain the electric field due to a uniformly charged thin
spherical shell of radius R and charge q at a point (i) outside and (ii) inside the shell. Sketch a
graph of E against r.

**Q3.** *(3 marks)* Derive an expression for the electric field at a point on the axial line of an
electric dipole. Hence write the expression for a short dipole.

**Q4.** *(3 marks)* Derive an expression for the torque acting on an electric dipole placed in a
uniform electric field. When is it maximum?

**Q5.** *(3 marks)* Using Gauss's law, derive an expression for the electric field due to an
infinitely long straight uniformly charged wire.

**Q6.** *(2 marks)* State any three properties of electric field lines. Why can two field lines
never intersect?

**Q7.** *(2 marks)* A charge q is placed at the centre of a cube of side a. What is the electric flux
through (i) the whole cube and (ii) one face of the cube?

**Q8.** *(2 marks)* Two point charges of +4 μC and −2 μC are 10 cm apart in air. Find the force
between them. What happens to this force if the space between them is filled with a medium of
dielectric constant 5?

**Q9.** *(1 mark, MCQ)* The electric field inside a uniformly charged thin spherical shell is
(a) kq/r² (b) kq/R² (c) zero (d) σ/ε₀

**Q10.** *(4 marks, case study)* A thin spherical shell of radius 10 cm carries a uniformly
distributed charge of 5 × 10⁻⁸ C.
(i) Find the electric field at a point 5 cm from the centre.
(ii) Find the electric field at a point 20 cm from the centre.
(iii) Find the surface charge density.
(iv) What is the total flux through a concentric sphere of radius 15 cm?

**Q11.** *(2 marks)* An electric dipole of dipole moment 4 × 10⁻⁹ C m is placed at 30° to a uniform
electric field of 5 × 10⁴ N C⁻¹. Find the torque acting on it.

**Q12.** *(1 mark, Assertion–Reason)*
**A:** The electric flux through a closed surface enclosing no charge is zero.
**R:** Charges outside a closed surface contribute no net flux through it.

---

## 4. Solutions

### Q1 — Gauss's theorem and the infinite plane sheet

**Statement of Gauss's theorem.** The total electric flux through any closed surface is equal to
1/ε₀ times the total charge enclosed by that surface:

```
      ∮ E · dA = q_enclosed / ε₀
```

**Derivation for an infinite plane sheet.**

*Diagram:* draw the sheet, the outward field arrows perpendicular to it on both sides, and a
cylindrical Gaussian surface pierced through it, with its flat faces of area A parallel to the sheet
on either side.

**Choice of Gaussian surface, with justification.** Take a cylinder of cross-sectional area A with
its axis perpendicular to the sheet and its two flat faces equidistant on either side. By symmetry:

- **E** is directed perpendicularly away from the sheet (for positive σ) and has the same magnitude
  at both faces.
- On the **curved** surface, **E** is parallel to the surface, so **E**·d**A** = 0 there and it
  contributes **no flux**.

**Compute the flux.**

```
      φ = (flux through face 1) + (flux through face 2) + (flux through curved surface)
        = EA + EA + 0
        = 2EA
```

**Compute the enclosed charge.** The cylinder cuts out an area A of the sheet, so

```
      q_enclosed = σA
```

**Apply Gauss's theorem.**

```
      2EA = σA/ε₀
⟹     E = σ/(2ε₀)
```

In vector form, **E** = (σ/2ε₀) n̂, where n̂ is the unit vector normal to the sheet pointing away from
it.

**Note:** E is **independent of the distance** from the sheet — the field of an infinite charged
sheet is uniform. ∎

### Q2 — spherical shell, inside and outside, plus the graph

*Diagram:* draw the shell of radius R with charge q spread over it, and two concentric spherical
Gaussian surfaces — one of radius r > R and one of radius r < R.

**Choice of Gaussian surface.** By the spherical symmetry of the charge distribution, **E** must be
radial and must have the same magnitude at every point of a concentric sphere. So on such a sphere
**E** is parallel to d**A** everywhere, and

```
      φ = ∮ E · dA = E ∮ dA = E (4πr²)
```

**(i) Outside the shell (r > R).**

The whole charge q is enclosed:

```
      E (4πr²) = q/ε₀
⟹     E = (1/4πε₀) · q/r²
```

This is exactly the field of a **point charge q placed at the centre**. So for external points, a
uniformly charged shell behaves as though all its charge were concentrated at its centre.

**(ii) Inside the shell (r < R).**

The Gaussian sphere lies entirely inside the shell, and since all the charge is on the shell's
surface, it encloses **no charge**:

```
      q_enclosed = 0
⟹     E (4πr²) = 0
⟹     E = 0
```

**The electric field everywhere inside a uniformly charged thin spherical shell is zero.**

**On the surface (r = R):** E = (1/4πε₀)q/R² = σ/ε₀, where σ = q/4πR².

**Graph of E against r:**

```
  E │
    │                    ← discontinuous jump at r = R
    │        ●
    │        │╲
    │        │ ╲___                    E ∝ 1/r² for r > R
    │        │     ╲______
    │        │            ‾‾‾‾‾‾‾‾───────
  0 ●────────┘
    └────────┴──────────────────────────── r
    0        R
        E = 0 inside
```

E is zero from 0 to R, jumps to a maximum value σ/ε₀ at r = R, and then falls off as 1/r². ∎

### Q3 — field on the axial line of a dipole

*Diagram:* draw −q at A and +q at B, separated by 2a, with centre O. Mark the point P on the axis at
distance r from O, on the +q side.

Let the dipole consist of −q at A and +q at B, with AB = 2a and midpoint O. Let P be a point on the
axis at distance r from O, beyond B.

**Distance from +q to P:** r − a. **Distance from −q to P:** r + a.

**Field due to +q at P** — directed **away** from B, i.e. along OP:

```
      E₊ = (1/4πε₀) · q/(r − a)²
```

**Field due to −q at P** — directed **towards** A, i.e. opposite to OP:

```
      E₋ = (1/4πε₀) · q/(r + a)²
```

**Net field**, taking the direction along OP as positive:

```
      E = E₊ − E₋
        = (q/4πε₀) [ 1/(r − a)² − 1/(r + a)² ]

        = (q/4πε₀) [ ( (r + a)² − (r − a)² ) / ( (r − a)²(r + a)² ) ]

        = (q/4πε₀) [ 4ar / (r² − a²)² ]
```

Since p = q(2a), we have q(4a) = 2p, so

```
      E_axial = (1/4πε₀) · 2pr/(r² − a²)²          directed along p
```

**For a short dipole (r >> a)**, we may neglect a² compared with r², giving (r² − a²)² ≈ r⁴:

```
      E_axial = (1/4πε₀) · 2p/r³
```

∎

### Q4 — torque on a dipole in a uniform field

*Diagram:* draw a uniform field **E** as parallel horizontal lines, and a dipole (−q at A, +q at B,
length 2a) inclined at angle θ to **E**. Mark the force qE on +q along **E** and qE on −q opposite to
**E**, and mark the perpendicular distance between their lines of action.

Let a dipole of moment p = q(2a) be placed in a uniform field **E** at angle θ to it.

**Forces.**

```
      Force on +q :  qE, along E
      Force on −q :  qE, opposite to E
```

These are equal in magnitude and opposite in direction, so the **net force is zero** — the dipole
does not translate.

**Torque.** The two forces do not act along the same line; they form a couple. The torque of a
couple is (magnitude of either force) × (perpendicular distance between their lines of action).

From the geometry, the perpendicular distance between the two lines of action is 2a sin θ.

```
      τ = (qE)(2a sin θ)
        = (q · 2a) E sin θ
        = pE sin θ
```

**In vector form:**

```
      τ = p × E
```

with the torque perpendicular to the plane containing **p** and **E**.

**Maximum torque.** τ = pE sin θ is maximum when sin θ = 1, i.e. **θ = 90°** — when the dipole is
perpendicular to the field. Then

```
      τ_max = pE
```

**Zero torque** when θ = 0° (stable equilibrium) or θ = 180° (unstable equilibrium). ∎

### Q5 — infinitely long charged wire

*Diagram:* draw the wire, radial field arrows perpendicular to it, and a coaxial cylindrical
Gaussian surface of radius r and length l.

Let the wire have uniform linear charge density λ (charge per unit length).

**Choice of Gaussian surface, with justification.** Take a cylinder of radius r and length l,
coaxial with the wire. By the cylindrical symmetry of the charge distribution:

- **E** is **radial** (perpendicular to the wire) and has the same magnitude at every point of the
  curved surface.
- On the two **flat end faces**, **E** is parallel to the surface, so those contribute **no flux**.

**Flux.**

```
      φ = E × (area of curved surface) = E (2πrl)
```

**Enclosed charge.**

```
      q_enclosed = λl
```

**Gauss's theorem.**

```
      E (2πrl) = λl/ε₀
⟹     E = λ/(2πε₀ r)
```

So **E ∝ 1/r** — the field of a long line charge falls off as the inverse *first* power of the
distance, not the inverse square. ∎

### Q6 — properties of electric field lines

Any three of:

1. Field lines **start from positive charges and end on negative charges**.
2. They are **continuous curves** with no breaks in a charge-free region.
3. **Two field lines can never intersect.**
4. They **never form closed loops**, because the electrostatic field is conservative.
5. The **tangent** at any point gives the direction of **E**; the **closeness** of the lines
   indicates the magnitude.
6. Field lines are always **perpendicular to the surface of a conductor**.

**Why two field lines can never intersect.** If two lines crossed at a point, then drawing tangents
at that point would give **two different directions for the electric field at the same point**. But
the electric field at a point has a single, unique direction. Hence field lines cannot intersect.

### Q7 — flux through a cube with a charge at its centre

**(i) Through the whole cube.** The cube is a closed surface enclosing the charge q, so by Gauss's
theorem:

```
      φ_total = q/ε₀
```

**(ii) Through one face.** By symmetry, the charge sits at the centre and the six faces are
equivalent, so each receives an equal share of the total flux:

```
      φ_one face = (1/6)(q/ε₀) = q/(6ε₀)
```

*(Note that the answer does not involve the side a at all — flux depends only on the enclosed
charge. That independence is what the question is testing.)*

### Q8 — Coulomb force, and the effect of a medium

```
      q₁ = +4 μC = 4 × 10⁻⁶ C
      q₂ = −2 μC = 2 × 10⁻⁶ C  (magnitude)
      r  = 10 cm = 0.1 m
```

**In air:**

```
      F = k q₁q₂/r²
        = (9 × 10⁹)(4 × 10⁻⁶)(2 × 10⁻⁶) / (0.1)²
        = (9 × 10⁹)(8 × 10⁻¹²) / (0.01)
        = (7.2 × 10⁻²) / (0.01)
        = 7.2 N
```

**F = 7.2 N**, and since the charges are of opposite sign the force is **attractive**.

**In a medium of dielectric constant K = 5:**

```
      F′ = F/K = 7.2/5 = 1.44 N
```

**The force is reduced to 1.44 N** — introducing a dielectric always reduces the electrostatic force,
by the factor K.

### Q9 — field inside a shell

**Answer: (c) zero**

By Gauss's law, a concentric spherical surface inside the shell encloses no charge, so the flux
through it — and hence the field on it — is zero.

### Q10 — case study: charged spherical shell

```
      R = 10 cm = 0.1 m          q = 5 × 10⁻⁸ C
```

**(i) At r = 5 cm — this is INSIDE the shell (r < R):**

```
      E = 0
```

*(No charge is enclosed by a concentric sphere of radius 5 cm.)*

**(ii) At r = 20 cm = 0.2 m — OUTSIDE the shell:**

```
      E = k q/r²
        = (9 × 10⁹)(5 × 10⁻⁸)/(0.2)²
        = (450)/(0.04)
        = 1.125 × 10⁴ N C⁻¹
```

**E ≈ 1.13 × 10⁴ N C⁻¹**, directed radially outward.

**(iii) Surface charge density:**

```
      σ = q/(4πR²)
        = (5 × 10⁻⁸)/(4π(0.1)²)
        = (5 × 10⁻⁸)/(4π × 0.01)
        = (5 × 10⁻⁸)/(0.1257)
        = 3.98 × 10⁻⁷ C m⁻²
```

**σ ≈ 4.0 × 10⁻⁷ C m⁻²**

**(iv) Flux through a concentric sphere of radius 15 cm.** This sphere encloses the whole charge, so
by Gauss's theorem:

```
      φ = q/ε₀ = (5 × 10⁻⁸)/(8.854 × 10⁻¹²) = 5.65 × 10³ N m² C⁻¹
```

**φ ≈ 5.6 × 10³ N m² C⁻¹**

*(The radius 15 cm is irrelevant to the answer, as long as it exceeds R — that is the point of the
sub-question.)*

### Q11 — torque on a dipole

```
      p = 4 × 10⁻⁹ C m          E = 5 × 10⁴ N C⁻¹          θ = 30°
```

```
      τ = pE sin θ
        = (4 × 10⁻⁹)(5 × 10⁴)(sin 30°)
        = (2 × 10⁻⁴)(0.5)
        = 1 × 10⁻⁴ N m
```

**τ = 1 × 10⁻⁴ N m**

### Q12 — Assertion–Reason

**A:** "The flux through a closed surface enclosing no charge is zero." **True** — by Gauss's law,
φ = q_enclosed/ε₀ = 0.

**R:** "Charges outside a closed surface contribute no net flux through it." **True** — field lines
from an external charge that enter the surface also leave it, so their contributions cancel.

**Does R explain A?** Yes. It is precisely because external charges contribute nothing that a surface
with no charge inside has zero net flux, even when a field is present.

**Answer: (a) Both A and R are true, and R is the correct explanation of A.**

---

## 5. Test yourself

Time: 45 minutes. Answers below.

1. *(1)* The SI unit of electric flux is
   (a) N C⁻¹ (b) N m² C⁻¹ (c) C m (d) N m C⁻¹
2. *(1)* The electric field due to a short dipole at a distance r on its axis varies as
   (a) 1/r (b) 1/r² (c) 1/r³ (d) 1/r⁴
3. *(1)* The net force on an electric dipole placed in a uniform electric field is
   (a) pE (b) pE sin θ (c) zero (d) 2pE
4. *(2)* Two charges of 2 μC and 3 μC are 30 cm apart. Find the force between them.
5. *(2)* Define electric field intensity and write its SI unit. Is it a scalar or a vector?
6. *(2)* A charge of 8 μC is enclosed by a closed surface. Find the total flux through it.
7. *(3)* Derive the expression for the electric field on the equatorial line of a short electric
   dipole.
8. *(3)* Using Gauss's law, find the electric field just outside a charged conductor of surface
   charge density σ.
9. *(3)* Two point charges +q and −q are placed 2a apart. Find the electric field at a point on the
   perpendicular bisector at distance r from the centre, for r >> a. State its direction.
10. *(5)* State Gauss's theorem and use it to derive the field due to an infinitely long straight
    charged wire. A wire carries a linear charge density of 2 × 10⁻⁶ C m⁻¹. Find the field 4 cm from
    it.
11. *(2)* Sketch the electric field lines for (i) two equal positive point charges and (ii) an
    electric dipole.
12. *(2)* Why must the electric field inside a conductor be zero in electrostatic equilibrium?
13. *(2)* An electric dipole of moment 2 × 10⁻⁸ C m experiences a maximum torque of 4 × 10⁻⁴ N m in
    a uniform field. Find the field strength.

### Answer key

**1. (b) N m² C⁻¹** (equivalently V m).

**2. (c) 1/r³.**

**3. (c) zero.** The two forces are equal and opposite; only the torque is non-zero.

**4. 0.6 N.** F = (9 × 10⁹)(2 × 10⁻⁶)(3 × 10⁻⁶)/(0.3)² = (9 × 10⁹)(6 × 10⁻¹²)/0.09
= (5.4 × 10⁻²)/0.09 = 0.6 N, repulsive.

**5.** Electric field intensity at a point is the **force per unit positive test charge** placed at
that point: **E** = **F**/q₀. SI unit: **N C⁻¹** (= V m⁻¹). It is a **vector**.

**6. 9.04 × 10⁵ N m² C⁻¹.** φ = q/ε₀ = (8 × 10⁻⁶)/(8.854 × 10⁻¹²) ≈ 9.0 × 10⁵ N m² C⁻¹.
*(The shape of the surface is irrelevant.)*

**7.** Let P be on the perpendicular bisector at distance r from the centre O. Each charge is at
distance √(r² + a²) from P.
E₊ = kq/(r² + a²), directed away from +q; E₋ = kq/(r² + a²), directed towards −q.
The components perpendicular to the dipole axis cancel; the components **along the axis** (each
E cos θ, with cos θ = a/√(r² + a²)) add:
E = 2 · [kq/(r² + a²)] · a/√(r² + a²) = k(2qa)/(r² + a²)^(3/2) = kp/(r² + a²)^(3/2).
For r >> a: **E = kp/r³ = p/(4πε₀r³)**, directed **antiparallel to p**.

**8. E = σ/ε₀.** Take a small cylindrical Gaussian surface ("pillbox") with one flat face of area A
just outside the conductor and the other just inside. The field inside a conductor is zero, so the
inner face contributes no flux; the curved surface contributes none (E is normal to the surface).
So φ = EA, and q_enclosed = σA, giving EA = σA/ε₀, i.e. **E = σ/ε₀**.

**9. E = kp/r³ = p/(4πε₀r³)**, directed from +q towards −q, i.e. **antiparallel to p**. (Same as
Q7.)

**10.** Statement and derivation as in §3 Q5, giving E = λ/(2πε₀r).
Numerically, with λ = 2 × 10⁻⁶ C m⁻¹ and r = 0.04 m, using 1/(2πε₀) = 2k = 1.8 × 10¹⁰:
E = (1.8 × 10¹⁰)(2 × 10⁻⁶)/(0.04) = (3.6 × 10⁴)/(0.04) = **9 × 10⁵ N C⁻¹**, radially outward.

**11.** (i) Two equal positive charges: lines radiate outward from each and curve away from one
another, with a **neutral point midway** between them where the field is zero; no line joins them.
(ii) Dipole: lines leave +q and curve round to enter −q, densest along the axis between the charges,
symmetric about the perpendicular bisector.

**12.** If the field inside were non-zero, it would exert a force **F** = q**E** on the free
electrons, which would keep moving — so the situation would not be static. Charges therefore
redistribute on the surface until the internal field is exactly cancelled everywhere inside. Hence
in electrostatic equilibrium E = 0 inside a conductor.

**13. E = 2 × 10⁴ N C⁻¹.** τ_max = pE, so E = τ_max/p = (4 × 10⁻⁴)/(2 × 10⁻⁸) = 2 × 10⁴ N C⁻¹.

**Scoring.** Out of 29. Below 20 → the three Gauss's law derivations are the gap. Write all three
from memory, with diagrams, before moving on.

---

## 6. Answering tips

**On the Gauss's law derivations (the 5-markers)**

1. **State the theorem in words first**, then in symbols. Both are marked, and the statement is
   typically 1 mark before any derivation begins.

2. **Draw the Gaussian surface on the diagram** and label it. Cylinder for wire and sheet, sphere for
   shell. The diagram is worth ½–1 mark, marked independently.

3. **Justify the choice of surface.** Write the two sentences: "By symmetry, E is radial and constant
   in magnitude on the curved surface" and "On the flat end faces, E is parallel to the surface, so
   they contribute no flux." That justification is a mark, and it is what separates a full answer
   from a formula.

4. **Show φ and q_enclosed as separate labelled steps** before equating them. Three lines: flux,
   enclosed charge, then Gauss's law.

5. **State the physical conclusion at the end.** "E ∝ 1/r" for the wire; "E is independent of
   distance" for the sheet; "E = 0 inside" for the shell. That closing observation is often an
   explicit sub-part.

6. **For the shell, draw the E-vs-r graph** with E = 0 up to r = R, the jump at r = R, and the 1/r²
   tail. Label both axes and mark R. It is a routine sub-part.

**On dipoles**

7. **State the direction of p** — from −q to +q. It gets asked, and it is required for the direction
   of the field.

8. **In the axial derivation, be careful with (r − a) and (r + a).** The near charge is at r − a. Get
   these the wrong way round and the sign of the answer flips.

9. **Do the r >> a approximation as an explicit final step**, with the words "for a short dipole,
   a² << r², so". Do not silently drop the a².

10. **For torque, state that the net force is zero** before deriving the torque. It is a mark and it
    is often a separate sub-part.

**On flux**

11. **Flux depends only on the enclosed charge.** For "flux through one face of a cube", use symmetry
    (divide by 6). For "flux when the surface is enlarged", the answer does not change. For "flux due
    to a charge outside", the answer is zero. These three are the whole flux question set.

12. **Watch the units:** N m² C⁻¹ for flux, N C⁻¹ or V m⁻¹ for field, C m for dipole moment,
    C m⁻¹ for λ, C m⁻² for σ.

**On numericals**

13. **Convert to SI first, on its own line.** μC → 10⁻⁶ C, cm → 10⁻² m. Most numerical errors in this
    chapter are unit-conversion errors, especially forgetting to square the metres.

14. **Use k = 9 × 10⁹ rather than 1/4πε₀**, and 1/(2πε₀) = 1.8 × 10¹⁰ for the wire. Faster, and less
    error-prone.

15. **State the direction of a field or force answer**, not just the magnitude — "radially outward",
    "attractive", "along p".
