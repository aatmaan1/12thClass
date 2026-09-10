# Ch 10 — Wave Optics

**Units V + VI (18 marks, shared with Ch 8 and Ch 9) · Typical appearance: 1–2 MCQs + a 3-mark
question on YDSE or single-slit diffraction, and sometimes a 5-marker combining both.**

---

## 1. Scope

### In the syllabus

- **Wavefront** and **Huygens' principle**
- Reflection and refraction of a plane wave at a plane surface using wavefronts; **proof of the laws
  of reflection and refraction using Huygens' principle**
- **Interference**; **Young's double slit experiment** and the expression for **fringe width**
  — the syllabus notes *"no derivation, final expression only"*
- **Coherent sources** and **sustained interference** of light
- **Diffraction due to a single slit**; **width of the central maximum** — the syllabus notes
  *"qualitative treatment only"*

### Deleted — do not study

- **Resolving power** of a microscope and of an astronomical telescope
- **Validity of ray optics** (the Fresnel-distance discussion)
- **Polarisation by scattering** (the blue sky / Rayleigh discussion)

### Scope you should verify for your year

The **polarisation block** — plane polarised light, **Brewster's law**, Malus's law, Polaroids and
their uses — has been progressively trimmed from this chapter, and sources disagree about exactly
what remains for the current session.

> **Practical advice, honestly stated.** Treat polarisation as **low priority**: read the summary
> below once so you are not blank if a 1-mark question appears, but do **not** derive Brewster's law
> or drill Malus's-law numericals. Put that time into YDSE and single-slit diffraction, which are
> certainly in the syllabus and carry most of the marks. Then confirm against the current CBSE
> syllabus PDF for your session.

Note also the two syllabus qualifiers above. "**Final expression only**" for the fringe width and
"**qualitative treatment only**" for the central maximum mean the board does not require the full
derivations. The short derivation is given below anyway — it is three lines, it makes the formula
memorable, and boards have sometimes asked for it — but if you are short of time, the **formula plus
its consequences** is what you must have.

---

## 2. Brief

### Wavefront

A **wavefront** is the locus of all points of a medium that are vibrating **in the same phase** at a
given instant.

| Type | Produced by |
| --- | --- |
| **Spherical** | a point source |
| **Cylindrical** | a linear (slit) source |
| **Plane** | a source at a very large distance (a small portion of a spherical wavefront far from the source) |

A **ray** is simply a line drawn **perpendicular to the wavefront**, in the direction of propagation.

### Huygens' principle

**Statement — two parts, both required:**

1. Every point on a given wavefront acts as a **source of secondary wavelets**, which spread out in
   all directions with the **speed of the wave in that medium**.
2. The **new position of the wavefront** after a time t is the **forward envelope** (the common
   tangent surface) of all these secondary wavelets.

*(The backward envelope is discarded — no backward wave is observed.)*

### Proof of the law of reflection using Huygens' principle

*Diagram:* a plane wavefront AB incident at angle i on a plane reflecting surface XY. While the
disturbance travels from B to C on the surface (distance BC = ct), a secondary wavelet from A travels
a distance AD = ct into the medium. The reflected wavefront is CD, making angle r with the surface.
Mark i, r, AC as the common hypotenuse.

Let a plane wavefront AB strike a plane mirror XY at angle of incidence i. Let the wave take time t
to travel from B to C.

```
      BC = c t                      (distance travelled along the surface)
      AD = c t                      (radius of the secondary wavelet from A, after time t)
```

so **BC = AD**.

Now consider the two right-angled triangles **ABC** and **ADC**:

- ∠ABC = ∠ADC = 90°
- **BC = AD** (both equal ct)
- **AC is common**

So the triangles are **congruent** (RHS), and therefore

```
      ∠BAC = ∠DCA
```

But ∠BAC = i (the angle of incidence, between the incident wavefront and the surface) and
∠DCA = r (the angle of reflection). Hence

```
      i = r
```

which is the **law of reflection**. And since the incident ray, the normal and the reflected ray all
lie in the plane of the diagram, the second law follows too. ∎

### Proof of the law of refraction (Snell's law) using Huygens' principle

*Diagram:* a plane wavefront AB incident at angle i on the plane boundary XY between medium 1 (speed
v₁) and medium 2 (speed v₂ < v₁). While the disturbance travels B → C in medium 1 (distance
BC = v₁t), the secondary wavelet from A travels AD = v₂t into medium 2. The refracted wavefront is
CD, at angle r.

Let a plane wavefront AB be incident at angle i on the boundary between two media in which the wave
speeds are v₁ and v₂. Let the disturbance take time t to travel from B to C in the first medium.

```
      BC = v₁ t                     AD = v₂ t
```

In triangle ABC:

```
      sin i = BC/AC = v₁t/AC
```

In triangle ADC:

```
      sin r = AD/AC = v₂t/AC
```

Dividing:

```
      sin i/sin r = v₁/v₂
```

This ratio is a constant for the given pair of media, which is **Snell's law**. Writing v₁ = c/n₁ and
v₂ = c/n₂:

```
      sin i/sin r = n₂/n₁  =  n₂₁
```

∎

> **The physical insight worth stating:** refraction occurs because the wave travels at a **different
> speed** in the second medium. The **frequency is unchanged** (it is set by the source), so since
> v = νλ, the **wavelength changes** in proportion to the speed.

### Interference — the principle of superposition

When two waves meet, the resultant displacement at any point is the **vector sum** of the individual
displacements.

**Conditions for constructive and destructive interference:**

| | Path difference | Phase difference | Result |
| --- | --- | --- | --- |
| **Constructive** (bright) | nλ | 2nπ | maximum intensity |
| **Destructive** (dark) | (2n − 1)λ/2 | (2n − 1)π | minimum intensity |

with n = 0, 1, 2, …

**Relation between path and phase difference:**

```
      phase difference = (2π/λ) × path difference
```

**Intensity of the resultant:**

```
      I = I₁ + I₂ + 2√(I₁I₂) cos φ

      I_max = ( √I₁ + √I₂ )²                I_min = ( √I₁ − √I₂ )²
```

If the two sources have equal intensity I₀, then I_max = 4I₀ and I_min = 0.

Since I ∝ a² (amplitude squared), and for equal slits I ∝ (width), useful ratios follow:

```
      I_max/I_min = ( √I₁ + √I₂ )² / ( √I₁ − √I₂ )²  =  (a₁ + a₂)²/(a₁ − a₂)²
```

### Coherent sources and sustained interference

**Coherent sources** are two sources that emit waves of the **same frequency** with a **constant
phase difference** between them.

**Conditions for sustained (steady, observable) interference:**

1. The two sources must be **coherent** — same frequency, constant phase difference.
2. The two waves must have **nearly equal amplitudes** (for good contrast between bright and dark
   fringes).
3. The sources must be **narrow** (otherwise each acts as many sources and the pattern washes out).
4. The two sources must be **close together**, and the screen reasonably far, so that the fringes are
   wide enough to be seen.
5. For complete darkness in the dark fringes, the waves should be in the **same state of
   polarisation**.

> **Why two independent lamps never produce interference.** Two separate sources emit light in
> random, rapidly changing bursts, so their phase difference varies randomly millions of times a
> second. The pattern shifts far faster than the eye can follow, and only the average — uniform
> illumination — is seen. Young's insight was to derive **both** beams from a **single** source, by
> passing the light through two slits: then any fluctuation affects both beams identically, and the
> phase difference stays constant. **This is the reason for the two-slit arrangement**, and it is
> frequently the asked part.

### Young's double slit experiment

*Diagram:* a monochromatic source illuminating a single slit S, then two narrow slits S₁ and S₂
separated by d, and a screen at distance D. Mark a point P on the screen at distance y from the
centre O, the path difference S₂P − S₁P, and the fringe pattern of equally spaced bright and dark
bands.

**Path difference at a point P a distance y from the centre of the screen:**

```
      path difference = y d / D
```

**Bright fringes** (constructive): path difference = nλ, so

```
      y_n = n λ D / d                       n = 0, ±1, ±2, …
```

**Dark fringes** (destructive): path difference = (2n − 1)λ/2, so

```
      y_n = (2n − 1) λ D / (2d)             n = 1, 2, 3, …
```

**Fringe width** — the separation between two consecutive bright (or two consecutive dark) fringes:

```
      β = λ D / d
```

*(Derivation, in one line: β = y_(n+1) − y_n = (n+1)λD/d − nλD/d = λD/d.)*

**All fringes are of equal width and equal intensity**, and the pattern is symmetric about the
central bright fringe at O.

**Angular fringe width:**

```
      θ = β/D = λ/d
```

**Effect of changing the parameters** — this is asked constantly:

| Change | Effect on β = λD/d |
| --- | --- |
| Wavelength λ increased (e.g. blue → red) | β **increases** |
| Screen distance D increased | β **increases** |
| Slit separation d increased | β **decreases** |
| Whole apparatus immersed in a liquid of index n | λ → λ/n, so β **decreases** to β/n |
| One slit covered | interference **disappears**; only single-slit diffraction remains |
| Monochromatic source replaced by white light | central fringe **white**, flanked by a few coloured fringes (violet nearest the centre, since β ∝ λ) |
| Slit width increased (both slits) | fringes lose contrast and eventually wash out |

### Diffraction at a single slit

*Diagram:* a plane wavefront incident on a slit of width a, with a screen at distance D. Show the
broad central bright maximum, flanked by minima and progressively weaker secondary maxima, and the
intensity-distribution curve beside it.

Diffraction is the **bending of light around the edges of an obstacle or aperture**, and the
consequent spreading into the geometrical shadow. It becomes noticeable when the size of the
aperture is **comparable to the wavelength**.

**Positions of the minima (dark):**

```
      a sin θ = n λ                 n = ±1, ±2, ±3, …          (note: n ≠ 0)
```

**Positions of the secondary maxima (bright):**

```
      a sin θ = (2n + 1) λ/2        n = 1, 2, 3, …
```

**The central maximum** lies at θ = 0 and is much broader and far more intense than the others.

**Width of the central maximum:**

```
      Angular half-width  θ = λ/a
      Angular full width  2θ = 2λ/a

      Linear width on a screen at distance D:   w = 2 λ D / a
```

**Consequences that get asked:**
- **Narrower slit (a smaller) → wider central maximum.** The pattern spreads more.
- **Longer wavelength → wider central maximum.**
- If a >> λ, the central maximum is very narrow and diffraction is negligible — which is why ray
  optics works for ordinary apertures.

**Intensity distribution:**

```
   I │        ╱╲
     │       ╱  ╲          ← broad, intense central maximum
     │      ╱    ╲
     │     ╱      ╲
     │ ╱╲ ╱        ╲ ╱╲    ← weak secondary maxima
     │╱  V          V  ╲
     └────┴────┴────┴────┴──── θ
        −2λ/a −λ/a  λ/a 2λ/a
```

### Interference vs diffraction — the comparison table

| | **Interference** | **Diffraction** |
| --- | --- | --- |
| Cause | superposition of waves from **two (or more) separate coherent sources** | superposition of waves from **different parts of the same wavefront** |
| Fringe width | all fringes are of **equal width** | the central maximum is **much wider** than the others |
| Intensity of maxima | all bright fringes are of **equal intensity** | intensity **falls off rapidly** away from the centre |
| Minima | dark fringes are **perfectly dark** (for equal amplitudes) | minima are **not perfectly dark** |
| Number of fringes | many fringes of comparable brightness | a few, with most of the light in the central maximum |

### Polarisation — read once, do not drill

*(See the scope note in §1: treat this section as low priority and verify against the current
syllabus.)*

Light from an ordinary source is **unpolarised** — the electric field vibrates in all directions
perpendicular to the direction of propagation. In **plane (linearly) polarised** light, the electric
field vibrates in **one plane** only.

**Polarisation is possible only for transverse waves**, so its observation in light is direct
evidence that **light is a transverse wave**. That single sentence is the most likely thing to be
asked here.

**Polaroids** are sheets that transmit only the component of the electric field along their
transmission axis. Two Polaroids in series:
- axes **parallel** → maximum transmission;
- axes **perpendicular (crossed)** → **no light** transmitted.

**Malus's law:** I = I₀ cos²θ, where θ is the angle between the polariser's and the analyser's axes.

**Brewster's law:** when unpolarised light is incident on a surface at the **polarising angle** θ_p,
the reflected light is completely plane polarised, and

```
      tan θ_p = n
```

**Uses of Polaroids:** sunglasses (reducing glare from horizontal surfaces), camera filters,
photoelastic stress analysis, LCD displays, controlling the intensity of light in windows.

### Quick recall box

```
WAVEFRONT: locus of points in the SAME PHASE ;  a ray is ⊥ to the wavefront
  spherical (point source) | cylindrical (slit) | plane (distant source)

HUYGENS: every point on a wavefront is a source of secondary wavelets;
         the new wavefront is the FORWARD ENVELOPE of these wavelets
  reflection : BC = AD = ct, triangles congruent ⟹ i = r
  refraction : sin i/sin r = v₁/v₂ = n₂/n₁
  frequency UNCHANGED on refraction; wavelength changes with the speed

INTERFERENCE
  constructive: path diff = nλ      ,  phase diff = 2nπ
  destructive : path diff = (2n−1)λ/2, phase diff = (2n−1)π
  phase diff = (2π/λ) × path diff
  I = I₁ + I₂ + 2√(I₁I₂)cos φ ;  I_max = (√I₁+√I₂)² ;  I_min = (√I₁−√I₂)²

COHERENT SOURCES: same frequency, CONSTANT phase difference
  two independent lamps cannot interfere — random, rapidly varying phase
  hence YDSE derives both beams from ONE source

YDSE : path difference = yd/D
  bright : y = nλD/d          dark : y = (2n−1)λD/2d
  FRINGE WIDTH  β = λD/d       angular width = λ/d
  λ↑ → β↑ ;  D↑ → β↑ ;  d↑ → β↓ ;  immersed in liquid n → β/n
  white light → central fringe WHITE, then a few coloured fringes

SINGLE-SLIT DIFFRACTION
  minima : a sin θ = nλ  (n ≠ 0)      secondary maxima : a sin θ = (2n+1)λ/2
  central maximum: angular half-width λ/a, full width 2λ/a
  linear width on screen = 2λD/a
  narrower slit → WIDER central maximum

INTERFERENCE vs DIFFRACTION: two sources vs one wavefront ; equal vs unequal widths ;
  equal vs falling intensity ; perfectly dark vs not perfectly dark minima

POLARISATION (low priority): proves light is TRANSVERSE
  Malus: I = I₀cos²θ ;  Brewster: tan θ_p = n ;  crossed Polaroids → no light
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* State Huygens' principle. Use it to prove the laws of reflection of a plane wave
at a plane reflecting surface.

**Q2.** *(5 marks)* Use Huygens' principle to derive Snell's law of refraction for a plane wave at a
plane interface. What happens to the frequency, wavelength and speed of light when it goes from a
rarer to a denser medium?

**Q3.** *(3 marks)* In Young's double slit experiment, write the expression for the fringe width. In
an experiment, two slits 0.3 mm apart are illuminated by light of wavelength 600 nm, and the screen
is 1.5 m away. Find the fringe width and the distance of the third bright fringe from the centre.

**Q4.** *(3 marks)* What are coherent sources? Why can two independent sources of light not produce a
sustained interference pattern? State two conditions for sustained interference.

**Q5.** *(3 marks)* Describe the diffraction pattern due to a single slit. Derive (or write) the
expression for the width of the central maximum and state how it changes if (i) the slit is made
narrower and (ii) red light is used instead of blue.

**Q6.** *(3 marks)* Distinguish between interference and diffraction of light, giving three points of
difference.

**Q7.** *(2 marks)* How does the fringe width in Young's experiment change if (i) the screen is moved
further away, (ii) the separation between the slits is increased, (iii) the whole apparatus is
immersed in water?

**Q8.** *(2 marks)* In a YDSE, the intensity at the central maximum is I₀. What is the intensity at a
point where the path difference is λ/3?

**Q9.** *(2 marks)* A slit of width 0.2 mm is illuminated by light of wavelength 600 nm. Find the
angular width of the central maximum.

**Q10.** *(2 marks)* What is observed in Young's double slit experiment if the monochromatic source
is replaced by white light?

**Q11.** *(1 mark, MCQ)* In a single-slit diffraction pattern, the first minimum occurs at an angle θ
given by
(a) a sin θ = λ/2 (b) a sin θ = λ (c) a sin θ = 2λ (d) a sin θ = 3λ/2

**Q12.** *(4 marks, case study)* In a Young's double slit experiment, the slit separation is 0.5 mm
and the screen is 1 m from the slits. The source emits light of wavelength 500 nm.
(i) Find the fringe width.
(ii) Find the distance between the 2nd and the 5th bright fringes.
(iii) Where is the 3rd dark fringe located?
(iv) What happens to the pattern if one of the slits is covered?

**Q13.** *(2 marks)* Why does the observation of polarisation of light establish that light is a
transverse wave?

---

## 4. Solutions

### Q1 — Huygens' principle and the law of reflection

**Statement of Huygens' principle.**

1. Every point on a given wavefront acts as a **source of secondary wavelets** which spread out in
   all directions with the **speed of the wave in that medium**.
2. The position of the wavefront after a time t is the **forward envelope** (the common tangent
   surface) of all these secondary wavelets. The backward envelope is discarded, since no backward
   wave is observed.

**Proof of the laws of reflection.**

*Diagram:* the reflecting surface XY drawn horizontally. A plane wavefront AB approaches at angle i,
with A on the surface and B above it. While the disturbance travels from B to C along the surface, a
secondary wavelet centred on A grows to radius AD. The reflected wavefront is the tangent CD, making
angle r with the surface. Draw the normals, and mark i and r.

Let a plane wavefront AB be incident at angle i on a plane reflecting surface XY. Let c be the speed
of the wave, and let t be the time taken for the disturbance to travel from B to C, where C is on the
surface.

Then

```
      BC = c t
```

During the same time t, the secondary wavelet originating at A spreads out to a radius

```
      AD = c t
```

So

```
      BC = AD                    …(i)
```

The reflected wavefront is the tangent from C to this wavelet, i.e. **CD**.

Now compare the right-angled triangles **ABC** and **ADC**:

```
      ∠ABC = ∠ADC = 90°          (AB is the incident wavefront, CD the reflected one)
      BC = AD                     from (i)
      AC = AC                     common
```

By the **RHS congruence** criterion, the triangles ABC and ADC are **congruent**. Therefore the
corresponding angles are equal:

```
      ∠BAC = ∠DCA
```

From the geometry, ∠BAC = **i** (the angle of incidence) and ∠DCA = **r** (the angle of reflection).
Hence

```
      i = r
```

which is the **first law of reflection**. Also, the incident wavefront, the reflected wavefront and
the normal all lie in the same plane (the plane of the diagram), which is the **second law**. ∎

### Q2 — Huygens' principle and Snell's law

*Diagram:* the interface XY between medium 1 (above, speed v₁) and medium 2 (below, speed v₂ < v₁).
A plane wavefront AB is incident at angle i, A on the interface. While the disturbance travels
B → C along the interface in medium 1, the secondary wavelet from A grows to radius AD in medium 2.
The refracted wavefront is the tangent CD, at angle r. Mark i, r, BC = v₁t and AD = v₂t.

Let a plane wavefront AB be incident at angle i on the plane interface between two media, in which
the wave speeds are v₁ and v₂.

Let t be the time taken for the disturbance at B to reach the interface at C. In medium 1,

```
      BC = v₁ t
```

During the same time t, the secondary wavelet from A travels into medium 2, where the speed is v₂, so
it reaches a radius

```
      AD = v₂ t
```

The refracted wavefront is the tangent CD.

**In triangle ABC** (right-angled at B), the angle at A equals the angle of incidence i:

```
      sin i = BC/AC = v₁ t / AC                    …(i)
```

**In triangle ADC** (right-angled at D), the angle at C equals the angle of refraction r:

```
      sin r = AD/AC = v₂ t / AC                    …(ii)
```

**Dividing (i) by (ii):**

```
      sin i/sin r = v₁/v₂
```

The right-hand side is a **constant** for the given pair of media, which is exactly **Snell's law**.
Writing the speeds in terms of the refractive indices, v₁ = c/n₁ and v₂ = c/n₂:

```
      sin i/sin r = (c/n₁)/(c/n₂) = n₂/n₁ = n₂₁
```

∎

**Going from a rarer to a denser medium:**

| Quantity | Change |
| --- | --- |
| **Frequency** | **unchanged** — it is determined by the source, not the medium |
| **Speed** | **decreases**, v = c/n |
| **Wavelength** | **decreases**, λ → λ/n (since v = νλ with ν fixed) |

### Q3 — YDSE fringe width and fringe position

**Expression for the fringe width:**

```
      β = λ D / d
```

where λ is the wavelength, D the distance from the slits to the screen, and d the slit separation.

**Numerical.**

```
      d = 0.3 mm = 0.3 × 10⁻³ m = 3 × 10⁻⁴ m
      λ = 600 nm = 600 × 10⁻⁹ m = 6 × 10⁻⁷ m
      D = 1.5 m
```

**Fringe width:**

```
      β = λD/d
        = (6 × 10⁻⁷)(1.5)/(3 × 10⁻⁴)
        = (9 × 10⁻⁷)/(3 × 10⁻⁴)
        = 3 × 10⁻³ m
        = 3 mm
```

**β = 3 mm**

**Distance of the third bright fringe from the centre:**

```
      y₃ = 3 β = 3 × 3 = 9 mm
```

*(Equivalently y₃ = 3λD/d = 3 × 3 mm = 9 mm.)*

**y₃ = 9 mm from the central fringe.**

### Q4 — coherent sources and sustained interference

**Coherent sources.** Two sources of light are said to be **coherent** if they emit waves of the
**same frequency** (and wavelength) with a **constant phase difference** between them that does not
change with time.

**Why two independent sources cannot produce sustained interference.**

Light from an ordinary source is emitted by a vast number of atoms independently, in short bursts
lasting about 10⁻⁸ s. The phase of the light from each source therefore **changes randomly and
extremely rapidly** — millions of times a second.

For two **independent** sources, the phase difference between them is therefore **not constant** but
fluctuates randomly. The positions of the bright and dark fringes shift far faster than the eye (or
any detector) can follow, so only the **time average** is observed — which is **uniform
illumination**, with no visible fringe pattern.

This is precisely why Young derived **both** interfering beams from a **single** source, by letting
the light fall on two narrow slits. Any random fluctuation in the source then affects the two beams
**identically**, so their phase difference remains **constant** and a steady fringe pattern is
observed.

**Two conditions for sustained interference** (any two):

1. The two sources must be **coherent** — same frequency, constant phase difference. In practice this
   means both must be derived from a single source.
2. The two waves must have **nearly equal amplitudes**, so that the dark fringes are nearly dark and
   the pattern has good contrast.
3. The sources must be **narrow** and **close together**, and the screen sufficiently distant, so that
   the fringes are wide enough to be resolved.

### Q5 — single-slit diffraction pattern and the central maximum

**Description of the pattern.**

*Diagram:* a slit of width a illuminated by a plane wavefront, with a screen at distance D showing a
**broad, bright central maximum** flanked on both sides by **dark minima** and progressively **weaker
secondary maxima**. Draw the intensity curve alongside.

When monochromatic light passes through a narrow single slit, the pattern on the screen consists of:

- a **broad, very intense central bright maximum** directly opposite the slit;
- on either side, alternate **dark and bright bands**;
- the secondary maxima are **much weaker** than the central one and their intensity **falls off
  rapidly** with distance from the centre;
- the minima are **not perfectly dark**.

The pattern arises from the superposition of secondary wavelets from **different parts of the same
wavefront** passing through the slit.

**Positions of the minima.** A dark fringe occurs when the slit can be divided into pairs of strips
whose contributions cancel, which gives

```
      a sin θ = n λ                 n = ±1, ±2, ±3, …
```

**Width of the central maximum.** The central maximum extends from the **first minimum on one side to
the first minimum on the other**. The first minimum is at

```
      a sin θ = λ           ⟹      sin θ = λ/a           ⟹      θ ≈ λ/a   (for small θ)
```

So the **angular half-width** is λ/a and the

```
      angular width of the central maximum = 2θ = 2λ/a
```

On a screen at distance D, the linear width is

```
      w = D × 2θ = 2 λ D / a
```

**(i) If the slit is made narrower** (a decreased): since w ∝ 1/a, the central maximum becomes
**wider** — the pattern spreads out more. (In the limit of a very narrow slit, the light spreads
almost uniformly.)

**(ii) If red light is used instead of blue** (λ increased, since λ_red > λ_blue): since w ∝ λ, the
central maximum becomes **wider**.

### Q6 — interference vs diffraction

| | **Interference** | **Diffraction** |
| --- | --- | --- |
| **Origin** | superposition of waves from **two (or more) separate coherent sources** | superposition of secondary waves from **different parts of the same wavefront** |
| **Fringe width** | all fringes have the **same width** | the **central maximum is much wider** than the rest, and the fringes are unequally spaced |
| **Intensity of maxima** | all bright fringes have **the same intensity** | intensity of the maxima **decreases rapidly** away from the centre |
| **Minima** | dark fringes are **perfectly dark** (for equal amplitudes) | minima are **not perfectly dark** |

*(Any three rows constitutes a full 3-mark answer. Note that each row compares the **same** attribute
on both sides — that parallel structure is what the marking scheme rewards.)*

### Q7 — effect of changes on the fringe width

Since β = λD/d:

**(i) Screen moved further away (D increased):** β ∝ D, so the fringe width **increases**.

**(ii) Slit separation increased (d increased):** β ∝ 1/d, so the fringe width **decreases**.

**(iii) Whole apparatus immersed in water** (refractive index n = 1.33): the wavelength in water
becomes λ_water = λ/n, while D and d are unchanged. So

```
      β_water = λ_water D/d = (λ/n)(D/d) = β/n
```

The fringe width **decreases** by the factor n — to about β/1.33, i.e. about 75% of its value in air.

### Q8 — intensity at a path difference of λ/3

**Phase difference** corresponding to a path difference of λ/3:

```
      φ = (2π/λ) × (path difference) = (2π/λ)(λ/3) = 2π/3
```

For two waves of equal intensity I₁ = I₂ = I, the resultant intensity is

```
      I_R = I + I + 2√(I·I) cos φ = 2I(1 + cos φ) = 4I cos²(φ/2)
```

**At the central maximum**, φ = 0, so I₀ = 4I, i.e. I = I₀/4.

**At the point in question**, φ = 2π/3, so φ/2 = π/3 and

```
      I_R = 4I cos²(π/3) = 4I (1/2)² = 4I × ¼ = I
```

Since I = I₀/4,

```
      I_R = I₀/4
```

**The intensity is I₀/4.**

### Q9 — angular width of the central maximum

```
      a = 0.2 mm = 0.2 × 10⁻³ m = 2 × 10⁻⁴ m
      λ = 600 nm = 6 × 10⁻⁷ m
```

```
      Angular width = 2λ/a
                    = 2(6 × 10⁻⁷)/(2 × 10⁻⁴)
                    = (12 × 10⁻⁷)/(2 × 10⁻⁴)
                    = 6 × 10⁻³ rad
```

**Angular width = 6 × 10⁻³ rad** (about 0.34°).

*(The angular half-width is 3 × 10⁻³ rad.)*

### Q10 — YDSE with white light

With white light instead of a monochromatic source:

1. **The central fringe is white.** At the centre the path difference is zero for **every**
   wavelength, so all colours interfere constructively there and combine to give white.

2. **The fringes on either side are coloured.** Since β = λD/d, the fringe width is **different for
   each wavelength** — greatest for red and least for violet. So the maxima for different colours
   fall at different positions, producing coloured fringes with **violet nearest the centre and red
   furthest out** in each order.

3. **Only a few fringes are visible.** Beyond the first few orders the fringe patterns of the
   different wavelengths overlap so heavily that the colours merge into general white illumination,
   and no distinct fringes can be seen.

### Q11 — first minimum in single-slit diffraction

The minima are at a sin θ = nλ with n = 1, 2, 3, …, so the **first** minimum (n = 1) is at

```
      a sin θ = λ
```

**Answer: (b) a sin θ = λ**

*(Option (a), a sin θ = λ/2, is the trap — that is the condition for a *maximum* in two-slit
interference, not a single-slit minimum. Note also that n = 0 is excluded from the minima condition,
since θ = 0 is the central **maximum**.)*

### Q12 — case study: YDSE numerical

```
      d = 0.5 mm = 5 × 10⁻⁴ m          D = 1 m          λ = 500 nm = 5 × 10⁻⁷ m
```

**(i) Fringe width:**

```
      β = λD/d = (5 × 10⁻⁷)(1)/(5 × 10⁻⁴) = 10⁻³ m = 1 mm
```

**β = 1 mm**

**(ii) Distance between the 2nd and 5th bright fringes:**

Bright fringes are at y_n = nβ, so

```
      y₅ − y₂ = (5 − 2)β = 3 × 1 mm = 3 mm
```

**3 mm**

**(iii) Position of the 3rd dark fringe:**

```
      y_n(dark) = (2n − 1) λD/(2d) = (2n − 1) β/2
```

For n = 3:

```
      y₃ = (2×3 − 1)(1/2) = 5 × 0.5 = 2.5 mm
```

**The 3rd dark fringe is 2.5 mm from the central bright fringe.**

*(Sensible: the dark fringes sit midway between the bright ones, so the 3rd dark fringe lies between
the 2nd and 3rd bright fringes, at 2.5 mm ✓)*

**(iv) If one slit is covered:**

The **interference pattern disappears**, because interference requires two coherent beams and there is
now only one. What remains is the **single-slit diffraction pattern** of the open slit — a broad
central bright band with weak fringes on either side — and the screen is much less bright overall and
shows no equally spaced fringes.

### Q13 — polarisation and the transverse nature of light

**Polarisation is a phenomenon that can occur only for transverse waves.**

In a **transverse** wave, the vibrations are perpendicular to the direction of propagation, so there
are **many possible directions of vibration** in the plane perpendicular to the propagation
direction. It is therefore meaningful to select one of them — which is exactly what polarisation
does.

In a **longitudinal** wave (such as sound), the vibrations are **along** the direction of
propagation, so there is only **one** possible direction of vibration. There is nothing to select,
and a longitudinal wave **cannot be polarised**.

Since light **can** be polarised — as demonstrated by the fact that two crossed Polaroids block it
completely — it follows that light must be a **transverse** wave. This was historically the decisive
evidence for the transverse nature of light, and it is consistent with light being an
electromagnetic wave, in which **E** and **B** oscillate perpendicular to the direction of
propagation.

---

## 5. Test yourself

Time: 45 minutes. Answers below.

1. *(1)* In Young's double slit experiment, the fringe width is
   (a) λd/D (b) λD/d (c) dD/λ (d) λ/(dD)
2. *(1)* If the distance between the slits in YDSE is doubled, the fringe width
   (a) doubles (b) halves (c) is unchanged (d) quadruples
3. *(1)* The condition for the first minimum in single-slit diffraction is
   (a) a sin θ = λ (b) a sin θ = λ/2 (c) a cos θ = λ (d) a sin θ = 2λ
4. *(2)* Define a wavefront. What is the shape of the wavefront from a point source, and from a very
   distant source?
5. *(2)* State Huygens' principle.
6. *(2)* In a YDSE, d = 1 mm, D = 1 m and λ = 600 nm. Find the fringe width.
7. *(2)* What is the path difference for (i) the 4th bright fringe and (ii) the 3rd dark fringe?
8. *(3)* Light of wavelength 500 nm falls on a slit of width 0.1 mm. Find the angular width of the
   central maximum and its linear width on a screen 2 m away.
9. *(3)* Two coherent sources have intensities in the ratio 4 : 1. Find the ratio of the maximum to
   the minimum intensity in the interference pattern.
10. *(5)* State Huygens' principle and use it to prove Snell's law. What happens to the wavelength of
    light when it enters water (n = 1.33) from air, if its wavelength in air is 600 nm?
11. *(3)* Give three differences between interference and diffraction.
12. *(2)* Why is the diffraction of sound waves much more readily observed than that of light waves?
13. *(2)* In a YDSE with white light, why is the central fringe white while the others are coloured?

### Answer key

**1. (b) λD/d.**

**2. (b) halves.** β ∝ 1/d.

**3. (a) a sin θ = λ.**

**4.** A **wavefront** is the locus of all points of a medium vibrating in the **same phase** at a
given instant. A **point source** gives a **spherical** wavefront. A **very distant source** gives
(effectively) a **plane** wavefront, since a small portion of a very large sphere is nearly flat.

**5.** (i) Every point on a wavefront acts as a source of **secondary wavelets** spreading out in all
directions with the speed of the wave in that medium. (ii) The new wavefront after time t is the
**forward envelope** (common tangent) of all these secondary wavelets.

**6. 0.6 mm.** β = λD/d = (6 × 10⁻⁷)(1)/(10⁻³) = 6 × 10⁻⁴ m = 0.6 mm.

**7.** (i) 4th bright fringe: path difference = nλ with n = 4, so **4λ**.
(ii) 3rd dark fringe: path difference = (2n − 1)λ/2 with n = 3, so **5λ/2**.

**8. Angular width = 10⁻² rad; linear width = 2 cm.**
Angular width = 2λ/a = 2(5 × 10⁻⁷)/(10⁻⁴) = 10⁻² rad.
Linear width = 2λD/a = (10⁻²)(2) = 2 × 10⁻² m = 2 cm.

**9. 9 : 1.** With I₁/I₂ = 4/1, we have √I₁ : √I₂ = 2 : 1.
I_max/I_min = (√I₁ + √I₂)²/(√I₁ − √I₂)² = (2 + 1)²/(2 − 1)² = 9/1.

**10.** Statement and proof as in §3 Q2.
Numerically: λ_water = λ_air/n = 600/1.33 = **451 nm**. The **frequency is unchanged**; the speed and
the wavelength both fall by the factor n.

**11.** Any three rows from the table in §4 Q6.

**12.** Diffraction becomes appreciable only when the **wavelength is comparable to the size of the
aperture or obstacle**. Sound waves in air have wavelengths of the order of **centimetres to metres**,
comparable to the size of doorways, walls and other everyday obstacles — so sound diffracts strongly
and we hear round corners. Light has wavelengths of the order of **5 × 10⁻⁷ m**, tens of thousands of
times smaller than ordinary obstacles, so its diffraction is negligible for everyday apertures and
becomes observable only with very narrow slits.

**13.** At the **central** fringe the path difference is **zero for every wavelength**, so all colours
interfere constructively there and combine to produce **white**. Away from the centre, the fringe
width β = λD/d **depends on the wavelength**, so each colour has its maxima at different positions.
The colours therefore separate, giving **coloured fringes** — with violet nearest the centre (smallest
β) and red furthest out.

**Scoring.** Out of 29. Below 20 → the two Huygens proofs plus the YDSE formula and its consequences
are the priority. Everything else in this chapter is secondary.

---

## 6. Answering tips

**On the Huygens proofs (the 5-markers)**

1. **State the principle in two numbered parts** — secondary wavelets, and the forward envelope.
   Both halves are marked, and mentioning that the backward envelope is discarded is a nice extra.

2. **The diagram is essential and must be labelled.** Show the incident wavefront AB, the point C on
   the surface, the secondary wavelet radius AD, the reflected/refracted wavefront CD, and the angles
   i and r. Without the labels the proof cannot be followed.

3. **For reflection, name the congruence criterion (RHS)** and list the three matching parts. That is
   the mark.

4. **For refraction, write BC = v₁t and AD = v₂t explicitly**, then take the two sines and divide.
   Three lines. Do not skip to sin i/sin r = n₂/n₁.

5. **Add the frequency/wavelength/speed conclusion** — it is very often an explicit sub-part.
   Frequency unchanged; speed and wavelength both reduced by n.

**On YDSE**

6. **The syllabus says "final expression only", so state β = λD/d confidently** and then use it. If
   you want to justify it, the one-line derivation β = y_(n+1) − y_n is enough.

7. **Write down the SI conversions on their own line.** mm → 10⁻³ m, nm → 10⁻⁹ m, μm → 10⁻⁶ m. Almost
   every numerical error in this chapter is a power-of-ten slip here.

8. **For "effect of changing…" questions, quote the formula and reason from it.** "Since β = λD/d and
   β ∝ 1/d, doubling d halves the fringe width." Quoting the proportionality is the mark.

9. **For immersion in a liquid, change only λ.** λ → λ/n, so β → β/n. D and d are geometric and
   unchanged.

10. **For the coherence question, the answer is about the randomly varying phase**, and the point of
    the single slit before the double slit is to make the two beams share that variation. Say both
    things.

**On single-slit diffraction**

11. **The minima condition excludes n = 0.** a sin θ = nλ with n = ±1, ±2, … — because θ = 0 is the
    central **maximum**, not a minimum. Stating that exclusion shows understanding.

12. **Width of the central maximum is 2λ/a angular, 2λD/a linear.** Note the factor of 2 — it spans
    from the first minimum on one side to the first on the other. Forgetting the 2 is the standard
    error.

13. **Draw the intensity distribution**, with the broad central peak and rapidly decaying secondary
    maxima, and label the axes. It is worth a mark.

**On comparison questions**

14. **Use a table with parallel rows.** Each row must compare the **same** attribute for interference
    and for diffraction. Three parallel rows is a full 3-mark answer; three unrelated statements is
    not.

**On priorities**

15. **Spend your time on YDSE and single-slit diffraction, not on polarisation.** Given the scope
    uncertainty noted in §1, know that polarisation proves light is transverse and know what crossed
    Polaroids do — and leave it there.
