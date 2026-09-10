# Ch 12 — Atoms

**Units VII + VIII (12 marks, shared with Ch 11 and Ch 13) · Typical appearance: 1 MCQ + a 2/3-mark
question on Bohr's postulates or the energy levels. Two memorised numbers do most of the work.**

---

## 1. Scope

### In the syllabus

- **Alpha-particle scattering experiment**; **Rutherford's model** of the atom
- **Bohr model** of the hydrogen atom; expressions for the **radius** of the nᵗʰ orbit, and the
  **velocity** and **energy** of the electron in the nᵗʰ orbit
- **Hydrogen line spectra** — the syllabus notes *"qualitative treatment only"*

### Deleted — do not study

- **de Broglie's explanation of Bohr's second postulate** (the standing-wave justification of
  angular-momentum quantisation)

> **On "qualitative treatment only" for the spectra.** Know the **names and regions** of the series
> (Lyman, Balmer, Paschen…) and which transitions produce them; the Rydberg formula is given below
> and is still useful for numericals, but the marks are concentrated in the energy-level picture
> rather than in wavelength arithmetic.

---

## 2. Brief

### Rutherford's alpha-particle scattering experiment

*Set-up:* a radioactive source emitting alpha particles, a narrow collimating slit, a **thin gold
foil** (about 10⁻⁷ m thick), and a rotatable zinc-sulphide screen with a microscope to count the
scattered particles at various angles.

**The observations:**

1. **Most** alpha particles passed **straight through** the foil, essentially undeviated.
2. A **small fraction** were deflected through **small** angles.
3. A **very few** — about 1 in 8000 — were deflected through **large** angles, and some were turned
   back through more than 90°.

**The conclusions:**

1. Since most particles passed undeviated, **the atom is mostly empty space**.
2. Since a few were deflected through very large angles, there must be a **concentrated centre of
   positive charge and mass** — the **nucleus** — capable of exerting a large repulsive Coulomb force.
3. Since only a **very few** were strongly deflected, the nucleus must be **extremely small** compared
   with the atom. (Rutherford estimated the nucleus at ~10⁻¹⁵ m against an atomic size of ~10⁻¹⁰ m —
   the nucleus occupies about 10⁻¹⁵ of the atom's volume.)
4. Essentially **all the mass** of the atom is concentrated in the nucleus, with the electrons
   revolving around it.

**Rutherford's model.** A tiny, dense, positively charged nucleus at the centre, with electrons
revolving around it in circular orbits, the necessary centripetal force being provided by the
electrostatic attraction:

```
      m v²/r = (1/4πε₀) · Z e²/r²
```

**Impact parameter (b).** The perpendicular distance of the initial velocity vector of the alpha
particle from the centre of the nucleus. **A smaller impact parameter gives a larger scattering
angle**; a head-on collision (b = 0) gives 180° back-scattering.

**Distance of closest approach (r₀).** For a head-on approach, the alpha particle stops when all its
kinetic energy has been converted into electrostatic potential energy:

```
      ½ m v² = (1/4πε₀) · (2e)(Ze)/r₀
⟹     r₀ = (1/4πε₀) · 2 Z e²/( ½ m v² )  =  (1/4πε₀) · 4 Z e²/(m v²)
```

**Two failures of Rutherford's model** — the reason Bohr was needed:

1. **Stability.** An electron moving in a circle is **accelerating** (centripetally), and classical
   electromagnetism says an accelerating charge must **radiate** energy continuously. Losing energy,
   the electron would spiral inward and fall into the nucleus in about 10⁻⁸ s. **Atoms would not be
   stable** — but they are.

2. **Spectra.** As the electron spiralled in, its frequency of revolution would change continuously,
   so it would emit a **continuous spectrum**. But atoms are observed to emit **sharp line spectra**
   at definite discrete wavelengths.

### Bohr's postulates

**Postulate 1 — stationary orbits.** An electron in an atom can revolve in certain **stable circular
orbits**, called **stationary states**, **without radiating energy**, even though it is accelerating.
The necessary centripetal force is provided by the electrostatic attraction of the nucleus.

**Postulate 2 — quantisation of angular momentum.** Only those orbits are permitted for which the
angular momentum is an **integral multiple of h/2π**:

```
      m v r = n h/(2π)                      n = 1, 2, 3, …
```

n is the **principal quantum number**.

**Postulate 3 — frequency condition.** An electron radiates or absorbs energy **only when it jumps
from one stationary orbit to another**. The energy of the emitted or absorbed photon equals the
difference between the two energy levels:

```
      h ν = E_i − E_f
```

### Radius, velocity and energy of the nᵗʰ orbit

**Setting up.** For a hydrogen-like atom of nuclear charge Ze, the Coulomb attraction provides the
centripetal force:

```
      m v²/r = (1/4πε₀) · Z e²/r²                    …(i)
```

and Bohr's second postulate gives

```
      m v r = n h/(2π)                               …(ii)
```

**Radius.** From (ii), v = nh/(2πmr). Substituting into (i):

```
      m/r · [ n h/(2π m r) ]² = (1/4πε₀) Z e²/r²
⟹     n² h²/(4π² m r) = Z e²/(4πε₀)
```

```
      r_n = n² h² ε₀ / (π m Z e²)
```

For **hydrogen (Z = 1)**, substituting the constants:

```
      r_n = 0.53 n²  Å  =  0.53 n² × 10⁻¹⁰ m
```

So **r ∝ n²**, and the first Bohr orbit (n = 1) has radius **0.53 Å** — the **Bohr radius**.

**Velocity.** From (ii), v_n = nh/(2πmr_n), and substituting r_n:

```
      v_n = Z e²/(2 ε₀ n h)
```

So **v ∝ 1/n** — the electron moves **more slowly in higher orbits**. For hydrogen, v₁ = c/137 (about
2.2 × 10⁶ m s⁻¹).

**Energy.** The kinetic energy is, from (i),

```
      K = ½ m v² = (1/2) · Z e²/(4πε₀ r)
```

and the potential energy is

```
      U = − Z e²/(4πε₀ r)  =  − 2K
```

so the total energy is

```
      E = K + U = K − 2K = −K = − Z e²/(8πε₀ r)
```

Substituting r_n:

```
      E_n = − m Z² e⁴/(8 ε₀² n² h²)
```

For **hydrogen (Z = 1)**, evaluating the constants:

```
      E_n = − 13.6/n²  eV
```

> **Memorise these two results and most of the chapter follows:**
>
> ```
>       r_n = 0.53 n²  Å                E_n = − 13.6/n²  eV
> ```

**The energy relations worth noting:**

```
      K = −E = + 13.6/n²  eV                U = 2E = − 27.2/n²  eV                U = −2K
```

**The negative sign of E** means the electron is **bound** to the nucleus. Energy must be *supplied*
to remove it.

### Energy level diagram for hydrogen

```
      E (eV)
        0  ────────────────────────  n = ∞    (ionised, free electron)
     −0.54 ────────────────────────  n = 5
     −0.85 ────────────────────────  n = 4
     −1.51 ────────────────────────  n = 3
                                              ↑ Paschen (to n=3, infrared)
     −3.40 ────────────────────────  n = 2
                                              ↑ Balmer (to n=2, VISIBLE)
     −13.6 ────────────────────────  n = 1    (ground state)
                                              ↑ Lyman (to n=1, ultraviolet)
```

- **Ground state:** n = 1, E = −13.6 eV.
- **Excited states:** n = 2, 3, 4, …
- The levels get **closer together** as n increases, converging on E = 0 at n = ∞.
- **Ionisation energy** of hydrogen = the energy needed to take the electron from n = 1 to n = ∞:

```
      = 0 − (−13.6) = 13.6 eV
```

- **First excitation energy** = E₂ − E₁ = −3.4 − (−13.6) = **10.2 eV**.

### Hydrogen spectral series

When an electron falls from a higher level n_i to a lower level n_f, a photon is emitted of energy

```
      h ν = E_i − E_f = 13.6 ( 1/n_f² − 1/n_i² )  eV
```

and wavelength given by the **Rydberg formula**:

```
      1/λ = R ( 1/n_f² − 1/n_i² )                     R = 1.097 × 10⁷ m⁻¹
```

| Series | n_f | n_i | Spectral region |
| --- | --- | --- | --- |
| **Lyman** | 1 | 2, 3, 4, … | **ultraviolet** |
| **Balmer** | 2 | 3, 4, 5, … | **visible** |
| **Paschen** | 3 | 4, 5, 6, … | infrared |
| **Brackett** | 4 | 5, 6, 7, … | infrared |
| **Pfund** | 5 | 6, 7, 8, … | far infrared |

**Within each series:** the transition from n_f + 1 gives the **longest** wavelength of that series
(smallest energy jump), and the transition from n_i = ∞ gives the **shortest** (the series limit).

> **The Balmer series is the visible one** — the only series that can be seen by eye, and hence the
> first to be discovered. That fact is asked directly.

**Number of spectral lines** possible when an atom is excited to level n and then de-excites:

```
      number of lines = n(n − 1)/2
```

### Limitations of Bohr's model

1. It applies only to **hydrogen and hydrogen-like (single-electron) atoms** — it fails for atoms
   with two or more electrons, because it takes no account of electron–electron interactions.
2. It cannot explain the **relative intensities** of the spectral lines.
3. It cannot explain the **fine structure** of spectral lines (the splitting into closely spaced
   components).
4. It provides **no justification** for the quantisation condition mvr = nh/2π — the postulate is
   simply asserted.
5. It cannot explain the **Zeeman and Stark effects** (splitting of lines in magnetic and electric
   fields).
6. It treats the electron as a **particle in a definite orbit**, which conflicts with the
   uncertainty principle.

### Quick recall box

```
RUTHERFORD SCATTERING
  observations: most pass through ; a few small deflections ; very few large (>90°)
  conclusions : atom mostly EMPTY ; small dense positive NUCLEUS ; nucleus ~10⁻¹⁵ m
                against atomic size ~10⁻¹⁰ m ; nearly all mass in the nucleus
  impact parameter b: smaller b → larger scattering angle ; b = 0 → 180°
  distance of closest approach: ½mv² = (1/4πε₀)(2e)(Ze)/r₀

RUTHERFORD FAILS: (1) an accelerating electron must radiate → atom would collapse in
                      ~10⁻⁸ s ; (2) it predicts a CONTINUOUS spectrum, not LINE spectra

BOHR'S POSTULATES
  1. stationary orbits — the electron revolves without radiating
  2. angular momentum quantised : m v r = n h/2π
  3. radiation only on a jump : hν = E_i − E_f

  r_n = n²h²ε₀/(πmZe²)         →  hydrogen: r_n = 0.53 n² Å        r ∝ n²
  v_n = Ze²/(2ε₀nh)                                                 v ∝ 1/n
  E_n = −mZ²e⁴/(8ε₀²n²h²)      →  hydrogen: E_n = −13.6/n² eV
  K = −E ;  U = 2E = −2K

  ground state n=1 : E = −13.6 eV
  ionisation energy = 13.6 eV ;  first excitation energy = 10.2 eV

SERIES : Lyman (n_f=1, UV) | BALMER (n_f=2, VISIBLE) | Paschen (n_f=3, IR)
         Brackett (4) | Pfund (5)
  1/λ = R(1/n_f² − 1/n_i²) ,  R = 1.097 × 10⁷ m⁻¹
  longest λ in a series: n_i = n_f + 1 ;  shortest (series limit): n_i = ∞
  number of lines from level n = n(n−1)/2

BOHR FAILS for: multi-electron atoms, line intensities, fine structure,
                Zeeman/Stark effects; and the quantisation is unjustified
```

---

## 3. Previous years' questions

**Q1.** *(5 marks)* State Bohr's postulates. Using them, derive an expression for the radius of the
nᵗʰ orbit of the electron in a hydrogen atom, and hence for its total energy.

**Q2.** *(3 marks)* Describe Rutherford's alpha-particle scattering experiment. State two conclusions
drawn from it.

**Q3.** *(3 marks)* State two drawbacks of Rutherford's atomic model, and explain how Bohr's model
overcame them.

**Q4.** *(3 marks)* Draw the energy level diagram of a hydrogen atom, and mark the transitions
corresponding to the Lyman and Balmer series. Which series lies in the visible region?

**Q5.** *(2 marks)* Find the radius and the energy of the electron in the third orbit of a hydrogen
atom.

**Q6.** *(2 marks)* Calculate the wavelength of the H_α line of the Balmer series
(the transition n = 3 → n = 2). Take R = 1.097 × 10⁷ m⁻¹.

**Q7.** *(2 marks)* Find the ionisation energy and the first excitation energy of a hydrogen atom.

**Q8.** *(2 marks)* The total energy of an electron in the first excited state of hydrogen is −3.4 eV.
Find its kinetic and potential energies in that state.

**Q9.** *(3 marks)* State three limitations of Bohr's model of the atom.

**Q10.** *(2 marks)* How many spectral lines are possible when hydrogen atoms are excited to the
n = 4 level?

**Q11.** *(1 mark, MCQ)* The radius of the nᵗʰ Bohr orbit is proportional to
(a) n (b) n² (c) 1/n (d) 1/n²

**Q12.** *(4 marks, case study)* A hydrogen atom in its ground state absorbs a photon and is excited
to the n = 3 level.
(i) Find the energy of the absorbed photon.
(ii) Find the wavelength of that photon.
(iii) How many spectral lines can be emitted as the atom returns to the ground state?
(iv) Which of the emitted lines has the longest wavelength?

**Q13.** *(2 marks)* Why does the electron in the ground state of a hydrogen atom not fall into the
nucleus, according to Bohr's model?

---

## 4. Solutions

### Q1 — Bohr's postulates, and the radius and energy of the nᵗʰ orbit

**Bohr's postulates.**

1. **Stationary orbits.** An electron in an atom revolves in certain **stable circular orbits**,
   called **stationary states**, **without radiating energy**. The centripetal force required is
   provided by the electrostatic attraction between the electron and the nucleus.

2. **Quantisation of angular momentum.** Only those orbits are permitted for which the angular
   momentum of the electron is an integral multiple of h/2π:

```
      m v r = n h/(2π)                      n = 1, 2, 3, …
```

3. **Frequency condition.** An electron emits or absorbs energy only when it **jumps** between two
   stationary orbits, and the photon involved has energy equal to the difference of the two levels:
   hν = E_i − E_f.

**Derivation of the radius.**

*Diagram:* an electron of charge −e and mass m in a circular orbit of radius r about a nucleus of
charge +e, with the Coulomb attraction shown pointing inward.

The electrostatic attraction provides the centripetal force:

```
      m v²/r = (1/4πε₀) · e²/r²                      …(i)
```

Bohr's second postulate gives

```
      m v r = n h/(2π)      ⟹      v = n h/(2π m r)     …(ii)
```

Substituting (ii) into (i):

```
      (m/r) [ n h/(2π m r) ]²  =  e²/(4πε₀ r²)

      n² h²/(4π² m r³)  =  e²/(4πε₀ r²)
```

Cancelling and rearranging:

```
      r = n² h² ε₀ / (π m e²)
```

Substituting h = 6.63 × 10⁻³⁴ J s, ε₀ = 8.854 × 10⁻¹² C² N⁻¹ m⁻², m = 9.1 × 10⁻³¹ kg,
e = 1.6 × 10⁻¹⁹ C:

```
      r_n = 0.53 n²  Å  =  0.53 n² × 10⁻¹⁰ m
```

So the **radius is proportional to n²**, and the smallest orbit (n = 1) has radius 0.53 Å.

**Derivation of the total energy.**

**Kinetic energy.** From (i), m v² = e²/(4πε₀ r), so

```
      K = ½ m v² = e²/(8πε₀ r)
```

**Potential energy.** For a charge −e at distance r from a charge +e:

```
      U = (1/4πε₀) · (e)(−e)/r = − e²/(4πε₀ r)
```

**Total energy:**

```
      E = K + U = e²/(8πε₀ r) − e²/(4πε₀ r) = − e²/(8πε₀ r)
```

Substituting r = n²h²ε₀/(πme²):

```
      E_n = − e²/(8πε₀) × π m e²/(n² h² ε₀)
```

```
      E_n = − m e⁴/(8 ε₀² n² h²)
```

Evaluating the constants and converting to electron-volts:

```
      E_n = − 13.6/n²  eV
```

∎

**Remarks worth adding:**
- E is **negative**, showing the electron is **bound**; energy must be supplied to free it.
- **E ∝ −1/n²**, so the levels get closer together as n increases, converging on 0 at n = ∞.
- Note that **K = −E** and **U = 2E = −2K**.

### Q2 — Rutherford's scattering experiment

*Diagram:* a lead-shielded radioactive source of alpha particles, a collimating slit, a thin gold
foil, and a rotatable zinc-sulphide screen with a microscope, showing alpha particles mostly passing
straight through and a few deflected through large angles.

**The experiment.** A narrow, collimated beam of alpha particles from a radioactive source was
directed at a **very thin gold foil** (about 10⁻⁷ m thick). The scattered alpha particles were
detected by the flashes they produced on a zinc-sulphide screen, which could be rotated to any angle,
and were counted with a microscope.

**Observations.**

1. **Most** alpha particles passed **straight through** the foil almost undeflected.
2. A **small fraction** were deflected through **small** angles.
3. A **very small number** — roughly 1 in 8000 — were deflected through **large** angles, some by more
   than 90°, effectively bouncing back.

**Two conclusions.**

1. **The atom is largely empty space, with the positive charge and mass concentrated in a tiny
   central nucleus.** Since most alpha particles went straight through, the atom cannot be a uniform
   sphere of positive charge; but since a few were violently deflected, there must be a very
   concentrated centre of positive charge capable of exerting a large Coulomb repulsion.

2. **The nucleus is extremely small compared with the atom.** Because only about one alpha particle
   in 8000 suffered a large deflection, the target responsible must occupy a tiny fraction of the
   foil's area. Rutherford estimated the nuclear radius as about **10⁻¹⁵ m**, against an atomic radius
   of about **10⁻¹⁰ m** — so the nucleus occupies roughly 10⁻¹⁵ of the atom's volume, while containing
   nearly all of its mass.

### Q3 — drawbacks of Rutherford's model, and how Bohr fixed them

**Drawback 1 — instability of the atom.**

In Rutherford's model the electron moves in a circular orbit, and so is **continuously accelerating**
(centripetal acceleration). Classical electromagnetic theory requires an **accelerating charge to
radiate energy continuously**. Losing energy, the electron's orbit would shrink and it would
**spiral into the nucleus within about 10⁻⁸ s**. Atoms would therefore be unstable — contrary to
observation.

**Drawback 2 — it predicts the wrong kind of spectrum.**

As the electron spiralled inward, its radius and hence its frequency of revolution would change
**continuously**, so the radiation emitted would cover a **continuous range of frequencies**. But
atoms are observed to emit sharp, discrete **line spectra** at definite wavelengths characteristic of
the element.

**How Bohr's model overcame them.**

**For the stability problem**, Bohr's **first postulate** simply asserts that certain orbits are
**stationary states** in which the electron does **not** radiate, despite accelerating. Combined with
the **second postulate** (mvr = nh/2π), this fixes a smallest permitted orbit — the n = 1 orbit of
radius 0.53 Å — below which the electron cannot go. So the atom has a **stable ground state** and
cannot collapse.

**For the spectrum problem**, Bohr's **third postulate** confines radiation to **jumps between
discrete levels**, with hν = E_i − E_f. Since the energies E_n = −13.6/n² eV are **discrete**, only
certain photon energies — and hence certain wavelengths — are possible. This gives a **line
spectrum**, and it correctly predicts the observed wavelengths of the hydrogen series.

### Q4 — energy level diagram, Lyman and Balmer series

```
      E (eV)
        0  ─────────────────────────────  n = ∞
     −0.54 ─────────────────────────────  n = 5
     −0.85 ─────────────────────────────  n = 4
                    │      │
     −1.51 ──────────┼──────┼───────────   n = 3
                    │      │   ↑
                    │      │   │ (Paschen, infrared)
     −3.40 ─────────┼──────▼───────────   n = 2
                    │  ↑↑↑
                    │  │││  BALMER series (to n = 2) — VISIBLE
     −13.6 ─────────▼──────────────────   n = 1   (ground state)
                 ↑↑↑
                 │││  LYMAN series (to n = 1) — ULTRAVIOLET
```

- The **Lyman series** consists of all transitions ending at **n = 1**. These are the largest energy
  jumps in hydrogen (at least 10.2 eV), so the photons have the shortest wavelengths — the series lies
  in the **ultraviolet**.
- The **Balmer series** consists of all transitions ending at **n = 2**. The energy jumps are smaller,
  and the wavelengths (656 nm, 486 nm, 434 nm, …) fall in the **visible** region.

**The series in the visible region is the Balmer series** — which is why it was the first to be
discovered, and why it is the one seen in a hydrogen discharge tube.

### Q5 — radius and energy of the third orbit

```
      r_n = 0.53 n² Å                E_n = −13.6/n² eV
```

For n = 3:

```
      r₃ = 0.53 × 9 = 4.77 Å = 4.77 × 10⁻¹⁰ m

      E₃ = −13.6/9 = −1.51 eV
```

**r₃ = 4.77 Å and E₃ = −1.51 eV.**

### Q6 — wavelength of the H_α line

The H_α line is the transition **n = 3 → n = 2** (the first line of the Balmer series).

```
      1/λ = R ( 1/n_f² − 1/n_i² )
          = (1.097 × 10⁷)( 1/2² − 1/3² )
          = (1.097 × 10⁷)( 1/4 − 1/9 )
          = (1.097 × 10⁷)( (9 − 4)/36 )
          = (1.097 × 10⁷)(5/36)
          = 1.524 × 10⁶ m⁻¹
```

```
      λ = 1/(1.524 × 10⁶) = 6.56 × 10⁻⁷ m = 656 nm
```

**λ = 656 nm** — in the **red** part of the visible spectrum, which is the familiar red H_α line of
hydrogen.

*(Cross-check via energies: E₃ − E₂ = −1.51 − (−3.40) = 1.89 eV, and λ = 1240/1.89 = 656 nm ✓ — using
hc = 1240 eV nm, this is much quicker than the Rydberg formula.)*

### Q7 — ionisation and first excitation energy

**Ionisation energy** is the energy required to remove the electron completely from the ground state,
i.e. to take it from n = 1 to n = ∞:

```
      Ionisation energy = E_∞ − E₁ = 0 − (−13.6) = 13.6 eV
```

**First excitation energy** is the energy required to take the electron from the ground state (n = 1)
to the first excited state (n = 2):

```
      E₂ = −13.6/4 = −3.40 eV

      First excitation energy = E₂ − E₁ = −3.40 − (−13.6) = 10.2 eV
```

**Ionisation energy = 13.6 eV; first excitation energy = 10.2 eV.**

### Q8 — kinetic and potential energy in the first excited state

The first excited state is n = 2, with total energy E = −3.4 eV.

Using the standard relations for a Coulomb-bound orbit:

```
      K = − E                       U = 2 E = − 2 K
```

Therefore

```
      K = −(−3.4) = + 3.4 eV

      U = 2(−3.4) = − 6.8 eV
```

**K = +3.4 eV and U = −6.8 eV.**

*Check:* K + U = 3.4 − 6.8 = −3.4 eV = E ✓

*(These relations follow from the derivation in Q1: K = e²/8πε₀r and U = −e²/4πε₀r, so U = −2K and
E = K + U = −K.)*

### Q9 — limitations of Bohr's model

Any three of:

1. **It applies only to hydrogen and hydrogen-like single-electron ions.** It fails for atoms with two
   or more electrons, because it takes no account of the **electron–electron repulsion**.

2. **It cannot explain the relative intensities** of the spectral lines — it says which wavelengths
   appear, but not how bright each is.

3. **It cannot explain the fine structure** of spectral lines, i.e. their splitting into several very
   closely spaced components when examined with a high-resolution spectrometer.

4. **The quantisation condition is unjustified.** Bohr simply postulated mvr = nh/2π without
   deriving it from any deeper principle.

5. **It cannot explain the Zeeman effect or the Stark effect** — the splitting of spectral lines when
   the atom is placed in a magnetic or electric field.

6. **It conflicts with the uncertainty principle**, since it assigns the electron a definite orbit
   with simultaneously definite position and momentum.

### Q10 — number of spectral lines from n = 4

```
      Number of lines = n(n − 1)/2
                      = 4(4 − 1)/2
                      = 4 × 3/2
                      = 6
```

**Six spectral lines are possible.**

*(Explicitly: 4→3, 4→2, 4→1, 3→2, 3→1, 2→1 — six transitions ✓)*

### Q11 — dependence of the Bohr radius on n

```
      r_n = 0.53 n² Å
```

**Answer: (b) n²**

### Q12 — case study: excitation to n = 3

**(i) Energy of the absorbed photon.**

```
      E₁ = −13.6 eV                E₃ = −13.6/9 = −1.51 eV

      Energy absorbed = E₃ − E₁ = −1.51 − (−13.6) = 12.09 eV
```

**≈ 12.1 eV**

**(ii) Wavelength of the photon.** Using hc = 1240 eV nm:

```
      λ = 1240/12.09 = 102.6 nm
```

**λ ≈ 103 nm** — in the **ultraviolet** (this is the second line of the Lyman series).

**(iii) Number of spectral lines emitted on returning to the ground state.**

```
      n(n − 1)/2 = 3(3 − 1)/2 = 3
```

**Three lines** — from the transitions 3→2, 3→1 and 2→1.

**(iv) Which emitted line has the longest wavelength?**

The longest wavelength corresponds to the **smallest energy jump**. Comparing the three:

```
      3 → 2 :  E₃ − E₂ = −1.51 − (−3.40) = 1.89 eV        ← smallest
      2 → 1 :  E₂ − E₁ = −3.40 − (−13.6) = 10.2 eV
      3 → 1 :  E₃ − E₁ = 12.09 eV                          ← largest
```

The **3 → 2** transition has the smallest energy (1.89 eV) and hence the **longest wavelength**:

```
      λ = 1240/1.89 = 656 nm
```

**The 3 → 2 transition, at 656 nm** — the red H_α line of the Balmer series.

### Q13 — why the electron does not fall into the nucleus

On **classical** physics it should: an electron in a circular orbit is accelerating, and an
accelerating charge radiates energy, so the electron would lose energy, spiral inward, and reach the
nucleus in about 10⁻⁸ s. This was Rutherford's fatal problem.

**Bohr's answer** is his **first postulate**: certain orbits are **stationary states** in which the
electron revolves **without radiating**, despite its acceleration. Radiation occurs only when the
electron **jumps between** such states (the third postulate).

Combined with the **quantisation condition** mvr = nh/2π, which permits only n = 1, 2, 3, …, there is
a **smallest allowed orbit** — the n = 1 orbit of radius 0.53 Å. The electron in the ground state
therefore has **no lower state to fall into**: it cannot radiate while in a stationary state, and
there is no stationary state below n = 1. Hence the atom is stable.

---

## 5. Test yourself

Time: 35 minutes. Answers below.

1. *(1)* The energy of the electron in the ground state of hydrogen is
   (a) −13.6 eV (b) +13.6 eV (c) −3.4 eV (d) 0
2. *(1)* Which spectral series of hydrogen lies in the visible region?
   (a) Lyman (b) Balmer (c) Paschen (d) Pfund
3. *(1)* According to Bohr, the angular momentum of an electron in the nᵗʰ orbit is
   (a) nh (b) nh/2π (c) 2πn/h (d) h/2πn
4. *(2)* State Bohr's second postulate and write its mathematical form.
5. *(2)* Find the energy and the radius of the electron in the second orbit of hydrogen.
6. *(2)* Find the wavelength of the radiation emitted when a hydrogen atom goes from n = 4 to n = 2.
7. *(2)* What is the ratio of the radii of the n = 2 and n = 1 orbits of hydrogen?
8. *(3)* State two observations of Rutherford's scattering experiment and the conclusion drawn from
   each.
9. *(3)* Draw the energy level diagram of hydrogen and mark the transition giving the shortest
   wavelength of the Balmer series.
10. *(5)* Using Bohr's postulates, derive the expression for the radius of the nᵗʰ orbit of a hydrogen
    atom. Hence find the radius of the n = 5 orbit.
11. *(2)* An electron in a hydrogen atom jumps from n = 5 to n = 2. Which series does this line belong
    to, and in what region of the spectrum does it lie?
12. *(2)* Why is the total energy of an electron in a Bohr orbit negative? What does it signify?
13. *(2)* How many spectral lines are emitted by atomic hydrogen excited to the n = 5 level?

### Answer key

**1. (a) −13.6 eV.**

**2. (b) Balmer.**

**3. (b) nh/2π.**

**4.** **Bohr's second postulate:** only those circular orbits are permitted for which the angular
momentum of the electron is an **integral multiple of h/2π**. Mathematically, **mvr = nh/2π**, where
n = 1, 2, 3, … is the principal quantum number.

**5. E₂ = −3.4 eV, r₂ = 2.12 Å.** E₂ = −13.6/4 = −3.4 eV; r₂ = 0.53 × 4 = 2.12 Å.

**6. 486 nm.** E₄ = −13.6/16 = −0.85 eV; E₂ = −3.40 eV. ΔE = −0.85 + 3.40 = 2.55 eV.
λ = 1240/2.55 = **486 nm** (the blue-green H_β line of the Balmer series).

**7. 4 : 1.** r ∝ n², so r₂/r₁ = 2²/1² = 4.

**8.** (i) **Most alpha particles passed straight through** → the atom is **mostly empty space**, so
the positive charge is not spread uniformly through it. (ii) **A very few were deflected through more
than 90°** → there is a **tiny, dense, concentrated positive nucleus** capable of exerting a very
large Coulomb repulsion, containing nearly all the atom's mass.

**9.** Diagram as in §4 Q4. The **shortest wavelength** of the Balmer series is the **series limit**,
the transition **n = ∞ → n = 2**, of energy 3.40 eV and wavelength λ = 1240/3.40 = **365 nm** (in the
near ultraviolet). Mark that transition with an arrow from the n = ∞ line down to n = 2.

**10.** Derivation as in §3 Q1, giving r_n = n²h²ε₀/(πme²) = 0.53 n² Å.
For n = 5: r₅ = 0.53 × 25 = **13.25 Å = 1.325 × 10⁻⁹ m**.

**11.** The transition ends at **n = 2**, so it belongs to the **Balmer series**, which lies in the
**visible** region. *(Specifically ΔE = −0.54 + 3.40 = 2.86 eV, so λ = 1240/2.86 = 434 nm — violet.)*

**12.** The total energy is E = K + U with U = −2K, so E = −K, which is **negative**. It signifies that
the electron is **bound** to the nucleus: its total energy is less than that of a free electron at
rest at infinity (which is taken as zero), so **energy must be supplied from outside** to remove the
electron from the atom. The magnitude |E| is precisely the energy needed to free it — the **binding
energy** of that state.

**13. 10.** n(n − 1)/2 = 5 × 4/2 = 10.

**Scoring.** Out of 28. Below 20 → memorise r_n = 0.53n² Å and E_n = −13.6/n² eV, and then redo every
numerical. Those two formulas plus hc = 1240 eV nm answer almost everything in this chapter.

---

## 6. Answering tips

**On the derivation (the 5-marker)**

1. **State all three postulates before deriving anything.** They are typically worth 1½ of the 5
   marks and are marked separately from the algebra.

2. **Write the two starting equations as labelled lines:** the force balance (i) and the quantisation
   condition (ii). Then say you are eliminating v between them. Naming the strategy is a mark.

3. **For the energy, do K and U as separate steps**, note U = −2K, and only then add. Do not write
   E = −13.6/n² and claim it as a derivation.

4. **End with the numerical forms** r_n = 0.53n² Å and E_n = −13.6/n² eV, and say they are obtained
   by substituting the values of the constants. The question almost always asks for a specific orbit.

5. **Add the interpretation:** E is negative because the electron is bound; the levels crowd together
   as n increases. These remarks are frequently separate sub-parts.

**On the numericals**

6. **Use hc = 1240 eV nm rather than the Rydberg formula** whenever you know the two energy levels.
   Find ΔE in eV from E_n = −13.6/n², then λ(nm) = 1240/ΔE(eV). It is two lines instead of five, and
   far less error-prone.

7. **E_n = −13.6/n² eV is the single most useful number in the chapter.** Almost every numerical is
   one arithmetic step from it.

8. **Keep the sign.** Energies of bound states are negative; energy *differences* (photon energies)
   are positive. A negative photon energy means you subtracted the wrong way round.

9. **For the number of spectral lines, use n(n−1)/2** — and if you have time, list the transitions to
   check.

10. **"Longest wavelength" means smallest energy jump.** So within a series it is the transition from
    the immediately higher level; "shortest wavelength" (the series limit) is from n = ∞.

**On the descriptive questions**

11. **For Rutherford's experiment, pair each observation with its conclusion.** Marks are awarded for
    the pairs, so never list observations without saying what each implies.

12. **For the drawbacks of Rutherford's model, give the mechanism.** "An accelerating charge radiates,
    so the electron would spiral in within ~10⁻⁸ s" earns the mark; "the model was unstable" does not.

13. **For the energy level diagram, label the energies in eV and the values of n**, and draw the
    levels **converging** towards E = 0 as n increases. Mark the transitions with arrows pointing
    **downwards** for emission.

14. **Know that Balmer is the visible series.** It is asked directly, and it also lets you sanity-check
    any wavelength answer: a Balmer transition should come out between about 365 nm and 656 nm.
