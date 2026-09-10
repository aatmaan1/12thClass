# Ch 9 — Ray Optics and Optical Instruments

**Units V + VI (18 marks, shared with Ch 8 and Ch 10) · Ray Optics alone typically carries 8–10
marks, and it is the one chapter that appears in **every** section of the paper — MCQ, 2-mark,
3-mark derivation, case study, and a 5-mark instrument question.**

**This is the highest-priority chapter in Physics. If you are short of time, start here.**

---

## 1. Scope

### In the syllabus

- **Reflection** of light; **spherical mirrors**; **mirror formula**
- **Refraction** of light; **total internal reflection** and **optical fibres**
- **Refraction at spherical surfaces**; **lenses**; **thin lens formula**; **lens maker's formula**
- **Magnification**; **power of a lens**; **combination of thin lenses in contact**
- **Refraction of light through a prism**
- **Optical instruments:** **microscopes** and **astronomical telescopes** (reflecting and
  refracting) and their **magnifying powers**

### Deleted — do not study

- **The human eye** — image formation, accommodation, and the correction of eye defects (myopia,
  hypermetropia) using lenses
- **Scattering of light** — the blue colour of the sky and the reddish appearance of the Sun at
  sunrise and sunset

> **Two notes.** (i) The eye-defects question ("what lens does a myopic person need?") was a
> standard 2-marker and is now out. Old question banks are full of it. (ii) Dispersion by a prism
> survives only as far as it is needed to discuss refraction through a prism; the
> Rayleigh-scattering explanations are out.

---

## 2. Brief

### Start here — in plain English

Put a straw in a glass of water and it looks bent. Look at yourself in a spoon and you are upside
down. This chapter explains both, and it does the whole job with one simplifying assumption: that
light travels in straight lines, called **rays**, until something makes it turn. That assumption is
not strictly true — Chapter 10 is about where it fails — but it is excellent whenever the objects
light meets are much bigger than its wavelength, which covers every mirror and lens you will ever
hold.

**Reflection** you already know: the angle in equals the angle out. What is new is curved mirrors.
A concave mirror (curving inwards, like the inside of a spoon) takes parallel rays and brings them
together at the focus; a convex mirror spreads them apart so they only *appear* to come from a focus
behind it. Everything about image formation follows from tracing two rays and seeing where they
meet, and the mirror formula 1/v + 1/u = 1/f is the algebra of that tracing. The magnification
m = −v/u tells you the size and, through its sign, whether the image is upright or inverted.

The sign convention is where most marks are lost, and it is not arbitrary — it is just "measure
everything from the mirror, and call the direction the light came from negative." Adopt it once,
apply it mechanically, never bend it mid-question. If your answer for a real image comes out
positive, you have slipped.

**Refraction** is the interesting half. Light travels slower in glass than in air, and when a wave
crosses a boundary at an angle, the side that enters first slows first, so the whole wavefront
pivots. That pivot is the bending. Snell's law, n₁ sin i = n₂ sin r, is the bookkeeping;
n = c/v is the definition of the refractive index — how many times slower light goes in that
material. The bent straw is exactly this, and so is the fact that a pond looks shallower than it is.

**Total internal reflection** is what happens when you push refraction past its limit. Going from
glass into air, light bends *away* from the normal, so at a large enough angle inside — the critical
angle — the refracted ray would have to bend past 90°, which is impossible. So none gets out; it all
reflects back inside. This is not a partial reflection but a perfect one, and it is why optical
fibres can carry light around corners for kilometres without losing it, and why a diamond sparkles.

The **prism** is the standard experiment: light in one face, out another, deviated by an angle δ.
Vary the angle of incidence and δ first falls, reaches a minimum, then rises — and at that minimum
the light passes symmetrically through the prism. That symmetry is what makes A + δ_m = i + e
collapse into the tidy formula for n. Because n depends slightly on colour, each colour deviates
differently and white light fans out into a spectrum. That is **dispersion**, and it is why a prism
makes a rainbow and why cheap lenses show coloured fringes.

**Lenses** are then refraction twice over, at two curved surfaces, and they behave like mirrors with
the signs rearranged: 1/v − 1/u = 1/f. **Power** P = 1/f, in dioptres, exists because when you stack
lenses their powers simply add, which is far more convenient than combining focal lengths — and it is
why your spectacle prescription is written in dioptres.

The chapter finishes with instruments — the microscope and the telescope — and both are the same
trick: one lens makes a real image, and a second lens is used as a magnifier to look at that image.
For a microscope you want both focal lengths short; for a telescope you want a long objective and a
short eyepiece, giving magnification f₀/fₑ. If you can explain *why* those requirements differ, you
have understood the instruments rather than memorised their formulae.

**Learn it from someone else too**

- **Video lecture** — [search: ray optics and optical instruments class 12 one shot](https://www.youtube.com/results?search_query=ray+optics+and+optical+instruments+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: ray optics and optical instruments](https://www.khanacademy.org/science/in-in-class-12th-physics-india/in-in-ray-optics-and-optical-instruments)
- **The book the paper is set from** — [NCERT Physics Part II, Chapter 9 (PDF)](https://ncert.nic.in/textbook/pdf/leph201.pdf)
- **HC Verma** — *Concepts of Physics* Part 1, Ch 18 *Geometrical Optics*, all of it. His treatment
  of the sign convention in §18.4 is the one to adopt, and §18.10–18.12 on the prism and dispersion
  covers the board's derivations. Ch 19 *Optical Instruments* for the microscope and telescope.

---

### The sign convention — get this right or lose the chapter

**The New Cartesian sign convention.** All distances are measured **from the pole (of a mirror) or the
optical centre (of a lens)**, taking the incident light as travelling from left to right.

| Quantity | Positive | Negative |
| --- | --- | --- |
| Distances **along** the incident light (to the right) | + | |
| Distances **against** the incident light (to the left) | | − |
| Heights **above** the principal axis | + | |
| Heights **below** the principal axis | | − |

**In practice, for an object placed on the left:**

```
      u is ALWAYS negative (real object)

      MIRRORS:   concave  f = −,  R = −          convex  f = +,  R = +
      LENSES:    convex   f = +                  concave f = −

      v positive → image on the far side (real for a lens, virtual for a mirror)
      v negative → image on the near side (virtual for a lens, real for a mirror)
```

> **Write u = −30 cm explicitly.** Substituting 30 and "remembering the sign later" is the single
> largest source of lost marks in this chapter. Write the signed values on their own line before you
> substitute.

### Reflection and spherical mirrors

**Laws of reflection:** (i) the angle of incidence equals the angle of reflection; (ii) the incident
ray, the reflected ray and the normal all lie in the same plane.

**Mirror formula:**

```
      1/v + 1/u = 1/f                     and         f = R/2
```

**Magnification:**

```
      m = h′/h = − v/u
```

- m positive → image is **erect** (and virtual, for a mirror)
- m negative → image is **inverted** (and real)
- |m| > 1 → magnified; |m| < 1 → diminished

**Image formation by a concave mirror** — worth having as a table:

| Object position | Image position | Nature | Size |
| --- | --- | --- | --- |
| At infinity | At F | real, inverted | highly diminished |
| Beyond C | Between F and C | real, inverted | diminished |
| At C | At C | real, inverted | same size |
| Between C and F | Beyond C | real, inverted | magnified |
| At F | At infinity | real, inverted | highly magnified |
| Between F and P | Behind the mirror | **virtual, erect** | magnified |

A **convex mirror** always gives a **virtual, erect, diminished** image between P and F, whatever the
object position — which is why it is used as a rear-view mirror (wide field of view, always erect).

### Refraction and Snell's law

**Laws of refraction:** (i) the incident ray, the refracted ray and the normal lie in one plane;
(ii) **Snell's law**:

```
      n₂₁ = sin i/sin r  =  n₂/n₁  =  v₁/v₂  =  λ₁/λ₂
```

**Absolute refractive index:**

```
      n = c/v                       (always ≥ 1)
```

**The frequency does not change** on refraction; the speed and the wavelength do.

**Relations worth knowing:**

```
      n₂₁ = 1/n₁₂                   n₃₁ = n₃₂ × n₂₁
```

**Apparent depth.** An object at real depth h under a medium of refractive index n appears to be at
depth h/n:

```
      n = (real depth)/(apparent depth)
```

**Normal shift** = h − h/n = h(1 − 1/n). This is why a pond looks shallower than it is, and why a
coin at the bottom of a glass of water appears raised.

### Total internal reflection

When light travels from a **denser to a rarer** medium, and the angle of incidence exceeds a certain
value, the light is **completely reflected** back into the denser medium. This is **total internal
reflection (TIR)**.

**Two conditions, both necessary:**
1. Light must travel from an **optically denser to an optically rarer** medium.
2. The angle of incidence must be **greater than the critical angle**.

**Critical angle.** The angle of incidence in the denser medium for which the angle of refraction is
exactly 90°:

```
      sin C = n₁/n₂ = 1/n                 (for a denser medium of index n adjoining air)
```

So a **larger refractive index gives a smaller critical angle**.

**Applications (a standard 2/3-mark question):**

- **Optical fibre.** A thin glass/plastic core of high refractive index surrounded by a cladding of
  lower refractive index. Light entering at one end strikes the core–cladding boundary at greater
  than the critical angle and is repeatedly totally internally reflected, so it travels along the
  fibre with almost no loss even around bends. Used in telecommunication and in endoscopy.
- **Totally reflecting prism.** A right-angled isosceles prism of glass (n = 1.5, so C ≈ 42°) turns
  light through 90° or 180°, or inverts an image, with no loss of intensity — better than a mirror,
  whose silvering absorbs some light. Used in periscopes and binoculars.
- **Mirage.** Successive refraction through layers of air of decreasing refractive index near hot
  ground, followed by TIR, creates the appearance of a distant water surface.
- **Brilliance of a diamond.** Diamond's very high refractive index (2.42) gives a small critical
  angle (~24°), so light entering it undergoes repeated TIR before emerging — hence the sparkle.

### Refraction at a single spherical surface

For refraction from medium n₁ into medium n₂ at a spherical surface of radius R:

```
      n₂/v − n₁/u = (n₂ − n₁)/R
```

### Lens maker's formula

For a thin lens of refractive index n (in air), with surfaces of radii R₁ and R₂:

```
      1/f = (n − 1) ( 1/R₁ − 1/R₂ )
```

**Thin lens formula:**

```
      1/v − 1/u = 1/f
```

**Magnification for a lens:**

```
      m = h′/h = v/u
```

*(Note: **m = v/u** for a lens, but **m = −v/u** for a mirror. The formulas differ by a sign — a
classic confusion.)*

**Consequences of the lens maker's formula** (these get asked):

- If the lens is placed in a medium of refractive index n_m, then 1/f = (n/n_m − 1)(1/R₁ − 1/R₂). So
  if **n = n_m**, then f = ∞ — **the lens stops behaving as a lens and becomes invisible**.
- If **n_m > n** (e.g. a glass convex lens immersed in a liquid denser than glass), f becomes
  **negative** — a **convex lens behaves as a diverging lens**.

### Power of a lens, and combinations

```
      P = 1/f                       f in metres, P in dioptres (D)
      P = 100/f                     f in centimetres
```

Convex (converging) lens: P positive. Concave (diverging) lens: P negative.

**Two thin lenses in contact:**

```
      1/F = 1/f₁ + 1/f₂                     P = P₁ + P₂                     m = m₁ × m₂
```

*(For lenses separated by a distance d, 1/F = 1/f₁ + 1/f₂ − d/(f₁f₂) — but the syllabus specifies
"in contact", so d = 0.)*

### Refraction through a prism

*Diagram:* a triangular prism with refracting angle A at the apex. A ray strikes face AB at angle of
incidence i, refracts at angle r₁, crosses to face AC where it is incident at r₂, and emerges at
angle of emergence e. The emergent ray is deviated by angle δ from the original direction.

**The two prism relations:**

```
      r₁ + r₂ = A                           (angle of the prism)
      i + e = A + δ                         (deviation)
```

**Derivation of these**, since it is asked:

In the quadrilateral formed by the two faces and the normals, the angles at the two feet of the
normals are 90° each, so

```
      A + ∠(between normals) = 180°
```

In the triangle formed by the refracted ray inside the prism and the two normals,

```
      r₁ + r₂ + ∠(between normals) = 180°
```

Comparing, **r₁ + r₂ = A**.

For the deviation: at the first face the ray is deviated by (i − r₁), and at the second face by
(e − r₂). The total deviation is the sum:

```
      δ = (i − r₁) + (e − r₂) = (i + e) − (r₁ + r₂) = (i + e) − A
```

hence **i + e = A + δ**.

**The i–δ graph and minimum deviation:**

```
   δ │╲                     ╱
     │ ╲                  ╱
     │  ╲               ╱
     │   ╲            ╱
     │     ╲___    ╱
  δm │        ‾╲╱‾           ← minimum, at i = e
     └──────────┴─────────── i
                i₁
```

As i increases, δ first decreases, reaches a **minimum δ_m**, then increases. At minimum deviation:

```
      i = e          and          r₁ = r₂ = A/2          and          i = (A + δ_m)/2
```

Substituting into Snell's law n = sin i/sin r₁:

```
      n = sin( (A + δ_m)/2 ) / sin( A/2 )
```

**This is the prism formula, and it is one of the most-asked results in Ray Optics.**

**Thin prism (small A):** the deviation is

```
      δ = (n − 1) A
```

### Compound microscope

*Ray diagram:* an objective lens O of short focal length f_o and an eyepiece E of somewhat longer
focal length f_e, separated by the tube length L. A small object AB is placed just beyond F_o. The
objective forms a **real, inverted, magnified** image A′B′ inside the focal length of the eyepiece.
The eyepiece acts as a simple magnifier and forms a **virtual, inverted, further magnified** final
image A″B″ at the near point (or at infinity). Mark f_o, f_e, the object, both images, and at least
two rays through each lens.

**Magnifying power:**

```
      m = m_o × m_e
```

where m_o = v_o/u_o for the objective.

**Final image at the near point (distance of distinct vision D = 25 cm):**

```
      m = (v_o/u_o) ( 1 + D/f_e )
```

**Final image at infinity (relaxed eye):**

```
      m = (v_o/u_o) ( D/f_e )
```

**Approximate form for a long tube** (v_o ≈ L, u_o ≈ f_o):

```
      m ≈ (L/f_o)(D/f_e)
```

**Why both focal lengths are short.** m ∝ 1/(f_o f_e), so both the objective and the eyepiece must
have **short focal lengths** for high magnification — with f_o the shorter of the two.

### Astronomical telescope (refracting)

*Ray diagram:* an objective of **large** focal length f_o and **large aperture**, and an eyepiece of
**small** focal length f_e. Parallel rays from a distant object form a real, inverted, diminished
image at the objective's focus, which coincides with the eyepiece's focus (normal adjustment). The
eyepiece renders the final image at infinity, inverted. Mark f_o, f_e, the intermediate image, and
the parallel emergent beam.

**Normal adjustment** (final image at infinity — the relaxed-eye setting):

```
      m = − f_o/f_e                         (magnitude f_o/f_e)

      Tube length L = f_o + f_e
```

**Final image at the near point:**

```
      m = (f_o/f_e)( 1 + f_e/D )

      Tube length L = f_o + u_e   where 1/u_e = 1/f_e − 1/D  (u_e < f_e)
```

**Why the objective must have a large focal length and large aperture:**
- **Large f_o** → large magnifying power, since m = f_o/f_e.
- **Large aperture** → gathers more light, so faint objects are visible, and gives better resolution.

**Reflecting telescope (Cassegrain).** A concave **mirror** replaces the objective lens. A small
secondary convex mirror reflects the converging beam back through a hole in the primary to the
eyepiece.

```
      m = f_o/f_e                (f_o here is the focal length of the concave mirror)
```

**Advantages of a reflecting over a refracting telescope** (a reliable 2/3-marker):

1. **No chromatic aberration** — a mirror reflects all wavelengths identically, whereas a lens
   refracts them by different amounts.
2. **Much reduced spherical aberration**, since a parabolic mirror can be used.
3. **Higher resolving power and brightness**, because large-aperture mirrors are far easier to make
   than large lenses.
4. **Mechanically easier** — a mirror is supported over its whole back surface, so it does not sag
   under its own weight, whereas a large lens can only be supported at its edge.
5. **Cheaper**, since only one surface needs figuring and the glass need not be optically
   homogeneous throughout.

### Quick recall box

```
SIGN CONVENTION: distances from the pole/optical centre; incident light left→right positive
  u always negative for a real object
  MIRROR: concave f = − , convex f = +      LENS: convex f = + , concave f = −

MIRROR : 1/v + 1/u = 1/f ,  f = R/2 ,  m = −v/u
LENS   : 1/v − 1/u = 1/f ,             m = +v/u        ← note the sign difference
  lens maker's : 1/f = (n − 1)(1/R₁ − 1/R₂)
  refraction at a spherical surface : n₂/v − n₁/u = (n₂ − n₁)/R
  P = 1/f (m) = 100/f (cm) , in dioptres
  in contact : 1/F = 1/f₁ + 1/f₂ ,  P = P₁ + P₂ ,  m = m₁m₂
  lens in a medium of the same index → f = ∞ , the lens disappears
  n_medium > n_lens → a convex lens DIVERGES

SNELL : n₂₁ = sin i/sin r = n₂/n₁ = v₁/v₂ = λ₁/λ₂ ;  n = c/v
  frequency UNCHANGED on refraction
  apparent depth : n = real depth/apparent depth ;  shift = h(1 − 1/n)

TIR : denser → rarer, AND i > C ;  sin C = 1/n
  uses: optical fibre, totally reflecting prism, mirage, diamond's sparkle

PRISM : r₁ + r₂ = A ;  i + e = A + δ
  at minimum deviation: i = e, r₁ = r₂ = A/2, i = (A + δm)/2
  n = sin[(A + δm)/2] / sin(A/2)
  thin prism : δ = (n − 1)A

COMPOUND MICROSCOPE (both f short, f_o shortest)
  near point : m = (v_o/u_o)(1 + D/f_e)      infinity : m = (v_o/u_o)(D/f_e)
  long tube  : m ≈ (L/f_o)(D/f_e)

ASTRONOMICAL TELESCOPE (f_o large, f_e small, large aperture)
  normal adjustment : m = f_o/f_e ,  L = f_o + f_e
  near point        : m = (f_o/f_e)(1 + f_e/D)
  reflecting: no chromatic aberration, less spherical aberration, brighter,
              mechanically stable, cheaper

D = 25 cm (least distance of distinct vision)
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* Draw a ray diagram for the formation of the image of a distant object by a
**refracting astronomical telescope** in normal adjustment. Derive an expression for its magnifying
power. State two advantages of a reflecting telescope over a refracting one.

**Q2.** *(5 marks)* Draw a labelled ray diagram of a **compound microscope** with the final image at
the near point. Derive an expression for its magnifying power. Why must both the objective and the
eyepiece have short focal lengths?

**Q3.** *(5 marks)* A ray of light passes through a prism. Derive the relation
i + e = A + δ. Hence show that at minimum deviation
n = sin[(A + δ_m)/2]/sin(A/2). Draw the i–δ graph.

**Q4.** *(3 marks)* Derive the **lens maker's formula** for a thin convex lens.

**Q5.** *(3 marks)* Derive the **mirror formula** for a concave mirror.

**Q6.** *(3 marks)* What is total internal reflection? State the conditions for it, and explain how
it is used in an optical fibre.

**Q7.** *(2 marks)* An object is placed 20 cm from a concave mirror of focal length 15 cm. Find the
position, nature and magnification of the image.

**Q8.** *(2 marks)* An object is placed 30 cm from a convex lens of focal length 20 cm. Find the
position and magnification of the image.

**Q9.** *(2 marks)* Two thin lenses of focal lengths +15 cm and −20 cm are placed in contact. Find
the focal length and the power of the combination.

**Q10.** *(2 marks)* Find the critical angle for a medium of refractive index 1.5.

**Q11.** *(3 marks)* A prism of refracting angle 60° gives a minimum deviation of 30°. Find its
refractive index and the angle of incidence at minimum deviation.

**Q12.** *(2 marks)* A convex lens of glass (n = 1.5) has a focal length of 20 cm in air. What happens
to its focal length if it is immersed in a liquid of refractive index 1.5? Explain.

**Q13.** *(4 marks, case study)* A telescope has an objective of focal length 150 cm and an eyepiece
of focal length 5 cm.
(i) Find its magnifying power in normal adjustment.
(ii) Find the length of the telescope tube in normal adjustment.
(iii) Find the magnifying power when the final image is formed at the near point (25 cm).
(iv) Why should the objective have a large aperture?

**Q14.** *(1 mark, MCQ)* The power of a concave lens of focal length 25 cm is
(a) +4 D (b) −4 D (c) +0.25 D (d) −0.25 D

---

## 4. Solutions

### Q1 — astronomical telescope

*Ray diagram (draw and label all of this):* the objective lens O of focal length f_o on the left,
receiving a parallel beam from a distant object arriving at a small angle α to the axis. It forms a
real, inverted, diminished image A′B′ at its second focal point. The eyepiece E of focal length f_e
is placed so that its first focal point coincides with A′B′ (normal adjustment). Rays leave the
eyepiece **parallel**, at a larger angle β to the axis, so the final image is at infinity. Mark f_o,
f_e, α, β, and the tube length L = f_o + f_e.

**Principle.** The objective forms a real, inverted, diminished image of the distant object at its
focus; the eyepiece then acts as a simple magnifier on that intermediate image.

**Derivation of the magnifying power.**

The **magnifying power** of a telescope is the ratio of the angle β subtended at the eye by the final
image to the angle α subtended at the eye (or objective) by the object itself:

```
      m = β/α
```

Let the intermediate image A′B′ have height h.

From the triangle formed at the objective, the angle subtended by the object at the objective equals
the angle subtended by the intermediate image at the objective's centre:

```
      tan α = h/f_o                 ⟹     α ≈ h/f_o          (angles are small)
```

From the triangle at the eyepiece, since A′B′ lies at the focus of the eyepiece:

```
      tan β = h/f_e                 ⟹     β ≈ h/f_e
```

Therefore

```
      m = β/α = (h/f_e)/(h/f_o)
```

```
      m = f_o/f_e
```

*(With the sign convention it is written m = −f_o/f_e, the minus indicating that the final image is
inverted.)*

**Length of the telescope in normal adjustment:**

```
      L = f_o + f_e
```

**Two advantages of a reflecting telescope over a refracting one:**

1. **No chromatic aberration.** A concave mirror reflects all wavelengths through the same angle,
   whereas a lens refracts different colours by different amounts and so produces coloured fringes.

2. **Greater brightness and resolving power, with mechanical stability.** Large-aperture mirrors are
   much easier and cheaper to make than large lenses, and a mirror is supported across its whole back
   surface so it does not sag under its own weight — a large lens can be supported only at its rim.

*(Also acceptable: much reduced spherical aberration, since a parabolic mirror may be used.)*

### Q2 — compound microscope

*Ray diagram (draw and label all of this):* an objective lens O of focal length f_o on the left and
an eyepiece E of focal length f_e on the right, separated by the tube length L. A small object AB is
placed just **beyond** F_o. The objective forms a **real, inverted, magnified** image A′B′ between the
eyepiece and its focus F_e. The eyepiece then forms a **virtual, magnified, inverted** final image
A″B″ at the near point, a distance D = 25 cm from the eye. Show at least two rays through each lens,
with arrowheads, and mark f_o, f_e, v_o, u_o, D.

**Principle.** The objective produces a real, magnified image of a very close object; the eyepiece
then acts as a simple magnifier on that image. The magnifications multiply.

**Derivation.**

The total magnifying power is the product of the two:

```
      m = m_o × m_e
```

**Objective.** Its linear magnification is

```
      m_o = v_o/u_o
```

where u_o is the object distance and v_o the image distance for the objective.

**Eyepiece.** It acts as a simple microscope. For a simple magnifier with the final image at the
near point D, the angular magnification is

```
      m_e = 1 + D/f_e
```

Therefore

```
      m = (v_o/u_o) ( 1 + D/f_e )
```

**If the final image is at infinity** (relaxed eye), the eyepiece magnification becomes D/f_e, so

```
      m = (v_o/u_o) ( D/f_e )
```

**Approximate form.** For a long tube, the objective's image distance v_o is nearly the tube length L,
and the object is placed just outside F_o so u_o ≈ f_o. Then

```
      m ≈ (L/f_o)(D/f_e)
```

**Why both focal lengths must be short.**

From m ≈ (L/f_o)(D/f_e), the magnifying power is **inversely proportional to both f_o and f_e**. So to
obtain a large magnification, **both** the objective and the eyepiece must have **short focal
lengths** — and since the object must be placed just outside the objective's focus and be strongly
magnified there, f_o is made the **shorter** of the two. ∎

### Q3 — refraction through a prism

*Diagram:* triangular prism ABC with refracting angle A at the apex. A ray PQ strikes face AB at
angle of incidence i, refracts into the prism at angle r₁, travels to face AC striking it at angle
r₂, and emerges as RS at angle of emergence e. Extend PQ and RS backwards/forwards to meet, and mark
the angle of deviation δ between them. Draw the normals at Q and R.

**Deriving r₁ + r₂ = A.**

In the quadrilateral AQNR (where N is the intersection of the two normals), the angles at Q and R are
each 90° (the normals are perpendicular to the faces). The angles of a quadrilateral sum to 360°:

```
      A + 90° + ∠QNR + 90° = 360°
⟹     A + ∠QNR = 180°                    …(i)
```

In the triangle QNR, the angles sum to 180°:

```
      r₁ + r₂ + ∠QNR = 180°               …(ii)
```

Comparing (i) and (ii):

```
      r₁ + r₂ = A
```

**Deriving i + e = A + δ.**

The ray is deviated at each face. At the first face the deviation is (i − r₁); at the second face it
is (e − r₂). The total deviation δ is the sum of these:

```
      δ = (i − r₁) + (e − r₂)
        = (i + e) − (r₁ + r₂)
        = (i + e) − A
```

Hence

```
      i + e = A + δ
```

**The i–δ graph:**

```
   δ │╲                        ╱
     │ ╲                     ╱
     │  ╲                  ╱
     │   ╲               ╱
     │    ╲__          ╱
  δm │       ‾‾╲____╱‾            ← ONE minimum, occurring at i = e
     └──────────┴────────────── i
                i₁
```

For each value of δ greater than δ_m there are **two** angles of incidence (one where the ray path is
the reverse of the other), but at the minimum the two coincide — i.e. **at minimum deviation,
i = e**.

**Deriving the prism formula.**

At minimum deviation, i = e, and therefore from Snell's law applied at both faces, r₁ = r₂ = r. Then:

```
      r₁ + r₂ = A       ⟹     2r = A       ⟹     r = A/2
```

and

```
      i + e = A + δ_m   ⟹     2i = A + δ_m ⟹     i = (A + δ_m)/2
```

Applying **Snell's law** at the first face:

```
      n = sin i/sin r
```

Substituting:

```
      n = sin[ (A + δ_m)/2 ] / sin( A/2 )
```

∎

### Q4 — lens maker's formula

*Diagram:* a thin double-convex lens of refractive index n₂ in a medium of index n₁, with its two
surfaces of radii R₁ and R₂. An object O on the axis; the first surface forms an intermediate image
I₁; the second surface forms the final image I.

Consider a thin lens of refractive index n₂ placed in a medium of index n₁, with surfaces of radii of
curvature R₁ and R₂. Let an object be at distance u from the lens.

**Refraction at the first surface.** Using the formula for refraction at a single spherical surface,
with the object at u and the image formed at v₁:

```
      n₂/v₁ − n₁/u = (n₂ − n₁)/R₁                    …(i)
```

**Refraction at the second surface.** The image I₁ from the first surface acts as the **object** for
the second surface. Light now travels from medium n₂ into medium n₁:

```
      n₁/v − n₂/v₁ = (n₁ − n₂)/R₂                    …(ii)
```

**Adding (i) and (ii)** — the v₁ terms cancel:

```
      n₁/v − n₁/u = (n₂ − n₁)/R₁ + (n₁ − n₂)/R₂
                  = (n₂ − n₁)( 1/R₁ − 1/R₂ )
```

Dividing by n₁:

```
      1/v − 1/u = ( n₂/n₁ − 1 )( 1/R₁ − 1/R₂ )
```

**Now identify f.** By definition, when the object is at infinity (u = ∞), the image forms at the
focus (v = f). Putting u = ∞:

```
      1/f = ( n₂/n₁ − 1 )( 1/R₁ − 1/R₂ )
```

For a lens **in air**, n₁ = 1 and n₂ = n, giving the **lens maker's formula**:

```
      1/f = ( n − 1 )( 1/R₁ − 1/R₂ )
```

and comparing with the earlier line, the **thin lens formula**:

```
      1/v − 1/u = 1/f
```

∎

### Q5 — mirror formula

*Diagram:* a concave mirror with pole P, centre of curvature C, and principal focus F. An object AB
of height h stands on the axis at distance u. Two rays are drawn: one parallel to the axis, reflected
through F; one through C, reflected back along itself. They meet at A′, forming the real inverted
image A′B′ of height h′ at distance v. Draw MN perpendicular from the point of incidence M to the
axis.

Consider a concave mirror of pole P, focus F and centre of curvature C. Let AB be an object of height
h at distance u, forming a real inverted image A′B′ of height h′ at distance v.

**Similar triangles, pair 1.** Triangles A′B′P and ABP are similar (both right-angled at B and B′,
with equal angles at P by the law of reflection):

```
      A′B′/AB = B′P/BP
⟹     h′/h = v/u                        (in magnitudes)         …(i)
```

**Similar triangles, pair 2.** Triangles A′B′F and MPF are similar (with MP = AB = h, since M is the
point where the ray parallel to the axis strikes the mirror):

```
      A′B′/MP = B′F/FP
⟹     h′/h = B′F/FP                                             …(ii)
```

**Equating (i) and (ii):**

```
      v/u = B′F/FP
```

Now express the distances in terms of u, v, f. Since B′F = PB′ − PF and FP = f (all in magnitudes):

```
      v/u = (v − f)/f
```

**Cross-multiplying:**

```
      v f = u(v − f) = uv − uf
⟹     v f + u f = u v
```

Dividing throughout by uvf:

```
      1/u + 1/v = 1/f
```

**Applying the sign convention** (u, v and f all negative for a real object in front of a concave
mirror), the relation retains the same form:

```
      1/v + 1/u = 1/f
```

∎

*(And from the geometry, PC = R = 2f, i.e. **f = R/2**.)*

### Q6 — total internal reflection and the optical fibre

**Definition.** When a ray of light travelling from an **optically denser medium to an optically rarer
medium** strikes the interface at an angle of incidence **greater than the critical angle**, it is
**completely reflected back into the denser medium**, with no refracted ray at all. This is **total
internal reflection**.

**Conditions (both are necessary):**
1. Light must travel from a **denser** to a **rarer** medium.
2. The angle of incidence must be **greater than the critical angle** C for that pair of media, where

```
      sin C = n_rarer/n_denser  =  1/n           (for a denser medium of index n adjoining air)
```

**Use in an optical fibre.**

*Diagram:* a long fibre with a core of high refractive index surrounded by a cladding of lower index;
a ray entering one end and bouncing repeatedly off the core–cladding boundary as it travels along.

An optical fibre consists of a thin **core** of glass or plastic of **high** refractive index,
surrounded by a **cladding** of **lower** refractive index.

Light entering one end of the fibre strikes the core–cladding boundary at an angle **greater than the
critical angle** for that pair of media. It therefore undergoes **total internal reflection**, and is
reflected back into the core. This is repeated thousands of times along the fibre's length, so the
light is guided along the fibre — **even around bends** — with almost no loss of intensity, because
total internal reflection involves no absorption at all (unlike reflection from a silvered mirror).

**Applications:** optical fibres carry telephone and internet signals over long distances, and are
used in **endoscopy** to see inside the human body.

### Q7 — concave mirror numerical

```
      u = −20 cm          f = −15 cm          (concave mirror: f negative)
```

**Mirror formula:**

```
      1/v + 1/u = 1/f
⟹     1/v = 1/f − 1/u
          = 1/(−15) − 1/(−20)
          = −1/15 + 1/20
          = (−4 + 3)/60
          = −1/60
⟹     v = −60 cm
```

**Magnification:**

```
      m = −v/u = −(−60)/(−20) = −60/20 = −3
```

**Conclusion.** The image is formed **60 cm in front of the mirror** (on the same side as the object,
since v is negative). It is **real** (v negative for a mirror means real), **inverted** (m negative)
and **magnified three times**.

*(Consistency check: f = 15, so C is at 30 cm. The object at 20 cm lies between F and C, and the
table in §2 says the image should then be real, inverted and magnified, beyond C — and 60 cm is
indeed beyond 30 cm ✓)*

### Q8 — convex lens numerical

```
      u = −30 cm          f = +20 cm          (convex lens: f positive)
```

**Lens formula:**

```
      1/v − 1/u = 1/f
⟹     1/v = 1/f + 1/u
          = 1/20 + 1/(−30)
          = (3 − 2)/60
          = 1/60
⟹     v = +60 cm
```

**Magnification:**

```
      m = v/u = 60/(−30) = −2
```

**Conclusion.** The image is formed **60 cm from the lens on the far side** from the object. It is
**real** (v positive for a lens), **inverted** (m negative) and **magnified twice**.

### Q9 — two thin lenses in contact

```
      f₁ = +15 cm          f₂ = −20 cm
```

**Combined focal length:**

```
      1/F = 1/f₁ + 1/f₂
          = 1/15 + 1/(−20)
          = (4 − 3)/60
          = 1/60
⟹     F = +60 cm
```

**Power:**

```
      P = 100/F  (F in cm) = 100/60 = +1.67 D
```

*(Or add the powers: P₁ = 100/15 = +6.67 D, P₂ = 100/(−20) = −5 D, so P = 6.67 − 5 = +1.67 D ✓)*

**F = +60 cm and P = +1.67 D.** The combination is **converging**, since F and P are positive.

### Q10 — critical angle

```
      sin C = 1/n = 1/1.5 = 0.6667
⟹     C = sin⁻¹(0.6667) = 41.8°
```

**C ≈ 41.8° (about 42°)**

*(This is the value for ordinary glass, which is why a 45°–45°–90° glass prism works as a totally
reflecting prism: 45° exceeds 42°.)*

### Q11 — prism refractive index at minimum deviation

```
      A = 60°          δ_m = 30°
```

**Angle of incidence at minimum deviation:**

```
      i = (A + δ_m)/2 = (60 + 30)/2 = 45°
```

**Refractive index:**

```
      n = sin[(A + δ_m)/2] / sin(A/2)
        = sin 45°/sin 30°
        = (0.7071)/(0.5)
        = 1.414
```

**n = √2 ≈ 1.41 and i = 45°.**

*(At minimum deviation r₁ = r₂ = A/2 = 30°, so the ray inside the prism travels parallel to the base
— a useful check, and often an explicit sub-part.)*

### Q12 — convex lens immersed in a liquid of the same refractive index

From the lens maker's formula for a lens of index n in a medium of index n_m:

```
      1/f = ( n/n_m − 1 )( 1/R₁ − 1/R₂ )
```

Here n = 1.5 and n_m = 1.5, so n/n_m = 1 and

```
      1/f = (1 − 1)( 1/R₁ − 1/R₂ ) = 0
⟹     f = ∞
```

**The focal length becomes infinite, and the lens has zero power** — it stops behaving as a lens
altogether.

**Explanation.** A lens works by **refracting** light at its surfaces, and refraction occurs only
when there is a **change of refractive index** across a surface. If the surrounding liquid has the
**same** refractive index as the glass, there is no change of index at either surface, so light
passes straight through undeviated. The lens becomes optically **invisible**.

*(Related, and often the follow-up: if the liquid's index were **greater** than the glass's, n/n_m
would be less than 1, making 1/f negative — so the **convex lens would behave as a diverging
lens**.)*

### Q13 — case study: astronomical telescope

```
      f_o = 150 cm          f_e = 5 cm          D = 25 cm
```

**(i) Magnifying power in normal adjustment:**

```
      m = f_o/f_e = 150/5 = 30
```

**m = 30** (the image is inverted, so with signs m = −30).

**(ii) Length of the tube in normal adjustment:**

```
      L = f_o + f_e = 150 + 5 = 155 cm
```

**L = 155 cm**

**(iii) Magnifying power with the final image at the near point:**

```
      m = (f_o/f_e)( 1 + f_e/D )
        = (150/5)( 1 + 5/25 )
        = (30)( 1 + 0.2 )
        = 30 × 1.2
        = 36
```

**m = 36**

*(Note that the near-point setting gives a **greater** magnification than normal adjustment, but at
the cost of eye strain — which is why normal adjustment, with the image at infinity and the eye
relaxed, is the usual choice.)*

**(iv) Why the objective should have a large aperture.**

Two reasons:
- **Light-gathering power.** A larger aperture collects more light from the distant object, so faint
  objects (distant stars and galaxies) become bright enough to see.
- **Resolving power.** A larger aperture reduces diffraction at the objective and so allows two
  closely spaced objects to be distinguished as separate — the telescope resolves finer detail.

### Q14 — power of a concave lens

For a **concave** lens, f is **negative**: f = −25 cm.

```
      P = 100/f (in cm) = 100/(−25) = −4 D
```

**Answer: (b) −4 D**

---

## 5. Test yourself

Time: 70 minutes. Answers below. **Draw a ray diagram wherever one is relevant** — that is part of
the exercise.

1. *(1)* The focal length of a spherical mirror of radius of curvature 30 cm is
   (a) 30 cm (b) 15 cm (c) 60 cm (d) 7.5 cm
2. *(1)* The magnification produced by a convex mirror is always
   (a) greater than 1 (b) less than 1 (c) equal to 1 (d) negative
3. *(1)* The refractive index of a medium in which light travels at 2 × 10⁸ m s⁻¹ is
   (a) 1.5 (b) 2 (c) 0.67 (d) 3
4. *(2)* An object is placed 10 cm from a convex mirror of focal length 15 cm. Find the image
   position and magnification.
5. *(2)* A concave lens of focal length 20 cm forms an image of an object placed 30 cm away. Find the
   image distance and magnification.
6. *(2)* Find the critical angle for diamond (n = 2.42).
7. *(2)* A coin lies at the bottom of a tank of water (n = 1.33) 60 cm deep. At what depth does it
   appear to be?
8. *(3)* Two lenses of powers +5 D and −2 D are placed in contact. Find the focal length of the
   combination.
9. *(3)* A prism has a refracting angle of 60° and a refractive index of 1.5. Find the angle of
   minimum deviation.
10. *(5)* Derive the mirror formula for a concave mirror, using a labelled ray diagram.
11. *(5)* Draw a labelled ray diagram of a compound microscope with the final image at infinity, and
    derive its magnifying power. A microscope has f_o = 2 cm and f_e = 6.25 cm; the object is placed
    2.5 cm from the objective and the final image is at infinity. Find the magnifying power.
12. *(3)* State three advantages of a reflecting telescope over a refracting telescope.
13. *(2)* Why does a diamond sparkle more than a piece of glass cut to the same shape?
14. *(2)* A ray of light is incident at 45° on one face of a right-angled isosceles glass prism
    (n = 1.5). Trace its path and explain.
15. *(3)* Show that for a lens immersed in a medium of higher refractive index than itself, a convex
    lens behaves as a diverging lens.

### Answer key

**1. (b) 15 cm.** f = R/2 = 30/2 = 15 cm.

**2. (b) less than 1.** A convex mirror always gives a diminished virtual image.

**3. (a) 1.5.** n = c/v = (3 × 10⁸)/(2 × 10⁸) = 1.5.

**4. v = +6 cm, m = +0.6.** Convex mirror: f = +15, u = −10.
1/v = 1/f − 1/u = 1/15 + 1/10 = (2 + 3)/30 = 5/30 = 1/6, so v = +6 cm.
m = −v/u = −6/(−10) = +0.6. Image is **virtual, erect, diminished**, 6 cm behind the mirror.

**5. v = −12 cm, m = +0.4.** Concave lens: f = −20, u = −30.
1/v = 1/f + 1/u = −1/20 − 1/30 = (−3 − 2)/60 = −5/60 = −1/12, so v = −12 cm.
m = v/u = −12/(−30) = +0.4. Image is **virtual, erect, diminished**, 12 cm from the lens on the same
side as the object.

**6. 24.4°.** sin C = 1/2.42 = 0.4132, so C = 24.4°.

**7. 45.1 cm.** Apparent depth = real depth/n = 60/1.33 = 45.1 cm.

**8. F = 33.3 cm.** P = P₁ + P₂ = 5 − 2 = +3 D. F = 100/P = 100/3 = 33.3 cm (converging).

**9. δ_m = 37.2°.** n = sin[(A + δ_m)/2]/sin(A/2), so
1.5 = sin[(60 + δ_m)/2]/sin 30° = sin[(60 + δ_m)/2]/0.5.
Hence sin[(60 + δ_m)/2] = 0.75, so (60 + δ_m)/2 = 48.6°, giving 60 + δ_m = 97.2° and
**δ_m ≈ 37.2°**.

**10.** Diagram and derivation as in §3 Q5, giving 1/v + 1/u = 1/f.

**11.** Diagram and derivation as in §3 Q2, with m = (v_o/u_o)(D/f_e) for the image at infinity.
Numerically: u_o = −2.5 cm, f_o = 2 cm.
1/v_o = 1/f_o + 1/u_o = 1/2 − 1/2.5 = 0.5 − 0.4 = 0.1, so v_o = 10 cm.
m_o = v_o/u_o = 10/(−2.5) = −4 (magnitude 4).
m_e = D/f_e = 25/6.25 = 4.
**m = 4 × 4 = 16** (the final image is inverted).

**12.** Any three of: (i) **no chromatic aberration**, since a mirror reflects all wavelengths
identically; (ii) **much reduced spherical aberration**, since a parabolic mirror may be used;
(iii) **higher resolving power and brightness**, because large-aperture mirrors are far easier to
make than large lenses; (iv) **mechanically more stable**, since a mirror is supported over its whole
back and does not sag; (v) **cheaper**, as only one surface must be figured.

**13.** Diamond has a very high refractive index (2.42) and hence a very **small critical angle**
(about 24°), much smaller than glass's (about 42°). A ray entering a cut diamond therefore strikes
the internal faces at more than the critical angle at almost every face, and undergoes **repeated
total internal reflection** many times before finally emerging. This concentrates the emerging light
into a few directions, producing the characteristic sparkle. Glass, with its larger critical angle,
loses much of the light by refraction out of the surfaces instead.

**14.** For glass with n = 1.5, the critical angle is about **42°**. A ray entering normally through
one of the shorter faces strikes the hypotenuse at **45°**, which is **greater than 42°**, so it
undergoes **total internal reflection** and is turned through **90°**, emerging normally through the
other short face. *(This is the totally reflecting prism, used in periscopes and binoculars in place
of a mirror, since TIR loses no intensity.)*

**15.** For a lens of index n in a medium of index n_m,

```
      1/f = ( n/n_m − 1 )( 1/R₁ − 1/R₂ )
```

For a **convex** lens, (1/R₁ − 1/R₂) is **positive**. If **n_m > n**, then n/n_m < 1, so the factor
(n/n_m − 1) is **negative**. Hence 1/f is negative, i.e. **f is negative** — and a lens of negative
focal length is a **diverging** lens. So a convex lens immersed in a medium denser than itself
behaves as a diverging lens. ∎

**Scoring.** Out of 37. Below 26 → do not move on. This chapter is worth 8–10 marks and everything in
it is learnable. The two priorities are (a) the sign convention, and (b) the two instrument ray
diagrams. Redo §3 Q1, Q2 and Q3 from memory.

---

## 6. Answering tips

**On the sign convention — the single biggest source of lost marks in Physics**

1. **Write the signed values on their own line** before substituting: "u = −30 cm, f = +20 cm".
   Never substitute a bare number and plan to fix the sign later.

2. **Learn the two formulas as a contrasting pair:**
   mirror 1/v + 1/u = 1/f with m = **−**v/u; lens 1/v **−** 1/u = 1/f with m = **+**v/u. Write both at
   the top of your rough page at the start of the paper.

3. **Interpret the sign of v in words.** For a **lens**, v positive → real image on the far side. For a
   **mirror**, v negative → real image in front. State the nature of the image explicitly — real or
   virtual, erect or inverted, magnified or diminished — because that is a separate mark.

4. **Sanity-check against the image table.** If the object is between F and C of a concave mirror, the
   image must be real, inverted, magnified and beyond C. If your answer disagrees, you have a sign
   error.

**On ray diagrams — worth 1–2 of every 5 marks**

5. **A ray diagram must have: at least two rays, arrowheads on every ray, all of F, 2F, O (and C for
   a mirror) marked, and the image clearly located and labelled.** Missing arrowheads is a routine
   half-mark loss.

6. **For the microscope, the intermediate image must be inside the eyepiece's focal length**, and the
   final image must be shown as virtual, on the same side as the object, and larger. Show both
   images.

7. **For the telescope in normal adjustment, the emergent rays must be parallel.** That is what
   "image at infinity" means, and drawing them converging is the standard error.

8. **Label f_o and f_e on the diagram** and mark the tube length. Then the derivation reads straight
   off it.

9. **Draw the diagram even if you cannot do the derivation.** It is marked independently.

**On the derivations**

10. **For the prism, derive both relations** (r₁ + r₂ = A and i + e = A + δ) before going to minimum
    deviation. Each is a mark, and the prism formula follows from them in three lines.

11. **State the minimum-deviation conditions explicitly:** "at minimum deviation i = e, hence
    r₁ = r₂ = A/2 and i = (A + δ_m)/2." Then Snell's law gives the formula. Those two lines are the
    heart of the question.

12. **For the lens maker's formula, do the two surfaces as two separate labelled steps** and then add.
    Do not attempt it in one line. And state that the image from the first surface acts as the object
    for the second — that sentence is a mark.

13. **For the mirror formula, identify your similar triangles by name** ("triangles A′B′F and MPF are
    similar") before writing the ratio. And finish by noting that the sign convention preserves the
    form of the result.

14. **For the telescope magnification, define m = β/α in words first.** "The magnifying power is the
    ratio of the angle subtended at the eye by the final image to that subtended by the object." Then
    the small-angle approximations.

**On numericals**

15. **Convert everything to the same unit before substituting**, and be consistent: if you work in cm,
    use P = 100/f. If in metres, P = 1/f.

16. **For lens combinations, adding the powers is usually faster than combining focal lengths.**
    P = P₁ + P₂, then F = 100/P.

17. **For prism numericals, watch whether you are given δ or δ_m.** The formula
    n = sin[(A + δ_m)/2]/sin(A/2) applies **only at minimum deviation**.

18. **For "what happens if the lens is immersed" questions, always go back to the lens maker's
    formula** with n/n_m. The three cases — n_m < n (still converging, longer f), n_m = n (f = ∞), and
    n_m > n (diverging) — are all one substitution away, and the explanation in words is the marked
    part.
