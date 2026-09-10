# Ch 11 — Dual Nature of Radiation and Matter

**Units VII + VIII (12 marks, shared with Ch 12 and Ch 13) · Typical appearance: 1–2 MCQs + a
2/3-mark question on Einstein's equation or the graphs, and a frequent source of Section-D case
studies (the graphs make ideal "source material").**

**Highly formulaic — one equation and two graphs generate nearly every question.**

---

## 1. Scope

### In the syllabus

- **Dual nature of radiation**
- **Photoelectric effect**; **Hertz and Lenard's observations**
- **Einstein's photoelectric equation** — the particle nature of light
- **Experimental study** of the photoelectric effect
- **Matter waves** — the wave nature of particles; the **de Broglie relation**

### Deleted — do not study

- **Davisson–Germer experiment**

---

## 2. Brief

### The photoelectric effect

**Definition.** The **emission of electrons** from the surface of a metal when light of a suitable
frequency falls on it. The emitted electrons are called **photoelectrons**.

**Hertz and Lenard's observations.** Hertz (1887) found that a spark discharge occurred more readily
when the electrodes were illuminated with ultraviolet light. Lenard (1902) showed that the effect was
due to the emission of **electrons** from the illuminated cathode, and that the current flowed only
while the light was falling on it.

### The terms — know these definitions exactly

| Term | Definition |
| --- | --- |
| **Work function** φ₀ | The **minimum energy** required to just liberate an electron from the metal surface. Unit: eV (or J). A material constant. |
| **Threshold frequency** ν₀ | The **minimum frequency** of incident radiation below which no photoemission occurs, however great the intensity. φ₀ = hν₀ |
| **Threshold wavelength** λ₀ | The corresponding **maximum** wavelength: λ₀ = c/ν₀ = hc/φ₀ |
| **Stopping potential** V₀ | The **minimum negative** potential on the collector at which the photocurrent becomes **zero**. It measures the maximum kinetic energy: eV₀ = K_max |
| **Saturation current** | The maximum photocurrent, reached when all emitted electrons are collected. It depends on the **intensity** |

Note that **φ₀, ν₀ and λ₀ are properties of the metal**, not of the incident light.

### The four experimental laws of photoelectric emission

1. **For a given frequency (above threshold), the photocurrent — and hence the number of
   photoelectrons emitted per second — is directly proportional to the intensity** of the incident
   radiation.

2. **The maximum kinetic energy of the photoelectrons depends only on the frequency** of the incident
   radiation and on the metal, and is **completely independent of the intensity**.

3. **There exists a threshold frequency ν₀ for each metal, below which no emission occurs**, however
   intense the radiation and however long it is applied.

4. **The emission is instantaneous** — the time lag between the incidence of radiation and the
   emission of electrons is less than about 10⁻⁹ s.

### Einstein's photoelectric equation

Einstein proposed that radiation consists of discrete **photons**, each of energy hν, and that
photoemission is a **one-photon–one-electron** process. An electron absorbs one whole photon; it uses
φ₀ of that energy to escape the surface, and the rest appears as kinetic energy:

```
      h ν = φ₀ + K_max
```

so

```
      K_max = h ν − φ₀ = h ν − h ν₀ = h(ν − ν₀)
```

and since K_max = eV₀,

```
      e V₀ = h ν − φ₀                     ⟹      V₀ = (h/e) ν − φ₀/e
```

Also, in terms of wavelength:

```
      h c/λ = φ₀ + ½ m v²_max
```

**How the equation explains all four laws** (this is the marked part of the question):

| Law | Explanation from hν = φ₀ + K_max |
| --- | --- |
| Current ∝ intensity | Intensity = number of photons per second. More photons ⟹ more electrons emitted ⟹ larger current. |
| K_max independent of intensity | K_max = hν − φ₀ contains no intensity term. Increasing the intensity sends more photons, but each still carries the same energy hν. |
| Threshold frequency exists | If hν < φ₀ then K_max would be negative, which is impossible. So emission requires ν ≥ ν₀ = φ₀/h, whatever the intensity. |
| Emission is instantaneous | The process is a single-photon absorption by a single electron — no time is needed to accumulate energy. |

### Why the wave theory fails

The classical wave picture predicts the **opposite** of what is observed, in three ways:

1. **Energy should depend on intensity.** On the wave theory a brighter beam carries more energy per
   unit area, so the electrons should come off with **greater** kinetic energy. Observation: K_max is
   completely independent of intensity.

2. **There should be no threshold frequency.** A wave of any frequency should eventually supply enough
   energy if applied long enough or intensely enough. Observation: below ν₀, **no** electrons are
   emitted at all, however intense the light.

3. **There should be a measurable time lag.** An electron would need time to absorb enough energy
   from a spread-out wave — calculations give hours for a dim source. Observation: emission is
   instantaneous (< 10⁻⁹ s).

### The graphs — learn all three as objects

**Graph 1 — photocurrent vs collector potential, at fixed frequency, for different intensities:**

```
     I │              ────────── I₃  (highest intensity)
       │            ╱
       │        ────────────── I₂
       │      ╱  ╱
       │  ──────────────  I₁
       │ ╱ ╱  ╱
   ────┴┴┴───────────────────→  V (collector potential)
     −V₀   0
       ↑
   SAME stopping potential for all intensities
```

- The **saturation currents differ** — higher intensity gives a larger saturation current.
- The **stopping potential is the same** for all three, because K_max depends only on the frequency.

**Graph 2 — photocurrent vs collector potential, at fixed intensity, for different frequencies:**

```
     I │        ───────────────  (same saturation current)
       │      ╱ ╱ ╱
       │    ╱ ╱ ╱
   ────┴───┴─┴─┴──────────────→  V
    −V₀₃ −V₀₂ −V₀₁  0
       ↑
   DIFFERENT stopping potentials;  ν₃ > ν₂ > ν₁
```

- The **saturation current is the same**, since the intensity (photons per second) is unchanged.
- The **stopping potentials differ** — a higher frequency gives a larger V₀.

**Graph 3 — stopping potential vs frequency (the most-asked graph):**

```
   V₀ │                    ╱ metal A     ╱ metal B
      │                  ╱             ╱
      │                ╱             ╱
      │              ╱             ╱
   ───┼────────────●─────────────●──────────→ ν
      │          ν₀A           ν₀B
 −φ₀/e│        ╱
      │      ╱
```

From V₀ = (h/e)ν − φ₀/e, this is a **straight line** with:

```
      slope           = h/e                    — the SAME for every metal
      x-intercept     = ν₀                     — the threshold frequency
      y-intercept     = −φ₀/e                  — gives the work function
```

> **This graph is a favourite because it packs three facts into one line.** The slope is universal
> (it is how h was first measured accurately by Millikan); only the intercept changes from metal to
> metal, and a metal with a larger work function has a larger threshold frequency, so its line lies
> further right.

### The photon — properties

| Property | Statement |
| --- | --- |
| Energy | E = hν = hc/λ |
| Momentum | p = E/c = hν/c = **h/λ** |
| Rest mass | **zero** |
| Charge | **zero** — so a photon is **not deflected** by electric or magnetic fields |
| Speed | c in vacuum, for all photons |
| Number | photons are **not conserved** — they can be created and absorbed |
| Intensity | intensity = (number of photons per unit area per second) × hν |

**Effective (relativistic) mass:** m = E/c² = hν/c². *(This is not a rest mass; a photon has no rest
mass.)*

### de Broglie's hypothesis — matter waves

De Broglie proposed that **every moving particle has a wave associated with it**, of wavelength

```
      λ = h/p = h/(m v)
```

**For an electron accelerated through a potential difference V:**

```
      Kinetic energy:   K = eV = ½ m v²          ⟹      v = √(2eV/m)
      Momentum:         p = m v = √(2 m e V)
```

so

```
      λ = h/√(2 m e V)
```

Substituting the constants for an electron gives the very useful working formula:

```
      λ = 12.27/√V  Å                (V in volts, λ in ångström)

         = 1.227/√V  nm
```

**In terms of kinetic energy K:**

```
      λ = h/√(2 m K)
```

**Points that get asked:**

- λ ∝ 1/√V, so a **larger accelerating voltage gives a shorter wavelength**.
- For the **same kinetic energy**, a heavier particle has a **shorter** de Broglie wavelength
  (λ ∝ 1/√m). So a proton has a much shorter wavelength than an electron of the same energy.
- For the **same speed**, again λ ∝ 1/m.
- The de Broglie wavelength of ordinary macroscopic objects (a cricket ball, say) is around 10⁻³⁴ m —
  far too small to detect, which is why we do not see wave behaviour in everyday life.

### Constants to have memorised

```
      h = 6.63 × 10⁻³⁴ J s                          h/e = 4.14 × 10⁻¹⁵ V s
      1 eV = 1.6 × 10⁻¹⁹ J                          hc = 1240 eV nm
      m_e = 9.1 × 10⁻³¹ kg                          e = 1.6 × 10⁻¹⁹ C
```

> **hc = 1240 eV nm is worth its weight in gold.** It turns E = hc/λ into a one-line calculation:
> a photon of wavelength 400 nm has energy 1240/400 = 3.1 eV. No powers of ten, no unit conversion.

### Quick recall box

```
PHOTOELECTRIC EFFECT: emission of electrons when light of suitable frequency hits a metal

φ₀ = work function = hν₀ = hc/λ₀      (a property of the METAL)
V₀ = stopping potential ;  eV₀ = K_max
saturation current depends on INTENSITY

EINSTEIN : hν = φ₀ + K_max = φ₀ + eV₀
           K_max = h(ν − ν₀)
           V₀ = (h/e)ν − φ₀/e

FOUR LAWS: current ∝ intensity ;  K_max depends only on ν ;
           threshold ν₀ exists ;  emission is instantaneous (<10⁻⁹ s)

WAVE THEORY FAILS on all three of: K_max should depend on intensity (it doesn't),
  there should be no threshold (there is), there should be a time lag (there isn't)

GRAPHS
  I vs V, different INTENSITIES (same ν): different saturation currents, SAME V₀
  I vs V, different FREQUENCIES (same I): same saturation current, DIFFERENT V₀
  V₀ vs ν : straight line ; slope = h/e (SAME for all metals) ;
            x-intercept = ν₀ ; y-intercept = −φ₀/e

PHOTON : E = hν = hc/λ ;  p = h/λ ;  rest mass 0 ;  charge 0 (undeflected by E, B)

de BROGLIE : λ = h/p = h/mv ;  λ = h/√(2mK)
  accelerated electron : λ = h/√(2meV) = 12.27/√V Å
  λ ∝ 1/√V ;  for the same K, heavier particle → shorter λ

CONSTANTS: h = 6.63×10⁻³⁴ J s ; 1 eV = 1.6×10⁻¹⁹ J ; hc = 1240 eV nm ;
           m_e = 9.1×10⁻³¹ kg
```

---

## 3. Previous years' questions

**Q1.** *(3 marks)* Write Einstein's photoelectric equation and use it to explain (i) the existence
of a threshold frequency and (ii) why the maximum kinetic energy of the photoelectrons is independent
of the intensity of the incident radiation.

**Q2.** *(3 marks)* Draw a graph showing the variation of stopping potential with the frequency of
incident radiation for two different metals. What does the slope of the graph represent? How is the
work function obtained from the graph?

**Q3.** *(3 marks)* Draw graphs showing the variation of photocurrent with collector potential for
(i) different intensities at constant frequency and (ii) different frequencies at constant intensity.
Explain the essential difference between the two.

**Q4.** *(3 marks)* State three observations of the photoelectric effect that the wave theory of light
cannot explain, and state how the photon picture explains each.

**Q5.** *(2 marks)* Define work function and threshold frequency. Write the relation between them.

**Q6.** *(3 marks)* The work function of a metal is 2.14 eV. Light of wavelength 500 nm is incident on
it. Find (i) the threshold wavelength, (ii) the maximum kinetic energy of the photoelectrons and
(iii) the stopping potential.

**Q7.** *(2 marks)* Find the de Broglie wavelength of an electron accelerated through a potential
difference of 100 V.

**Q8.** *(2 marks)* An electron and a proton have the same kinetic energy. Which has the greater
de Broglie wavelength, and why?

**Q9.** *(2 marks)* Find the energy and momentum of a photon of wavelength 620 nm.

**Q10.** *(1 mark, MCQ)* The stopping potential in a photoelectric experiment depends on
(a) the intensity of the incident light (b) the frequency of the incident light
(c) the distance of the source (d) the area of the cathode

**Q11.** *(4 marks, case study)* In a photoelectric experiment, the stopping potential V₀ is measured
for different frequencies ν of the incident radiation, and the graph of V₀ against ν is found to be a
straight line of slope 4.14 × 10⁻¹⁵ V s, cutting the ν-axis at 5 × 10¹⁴ Hz.
(i) What physical constant does the slope give?
(ii) Find the value of Planck's constant from the slope.
(iii) Find the work function of the metal in eV.
(iv) Would the slope change if a different metal were used? Explain.

**Q12.** *(2 marks)* Why are photons not deflected by an electric or a magnetic field?

**Q13.** *(1 mark, Assertion–Reason)*
**A:** No photoelectrons are emitted if the frequency of the incident light is below the threshold
frequency, however intense the light.
**R:** Photoemission is a one-photon–one-electron process, and a single photon of energy less than
the work function cannot liberate an electron.

---

## 4. Solutions

### Q1 — Einstein's equation and two of the laws

**Einstein's photoelectric equation.** Radiation consists of photons, each of energy hν. In
photoemission, **one photon is absorbed by one electron**. Part of the photon's energy, equal to the
work function φ₀, is used in liberating the electron from the metal surface, and the remainder appears
as the electron's kinetic energy:

```
      h ν = φ₀ + K_max                      or          K_max = h ν − φ₀
```

Since K_max = eV₀, this can also be written eV₀ = hν − φ₀.

**(i) The existence of a threshold frequency.**

Kinetic energy cannot be negative, so emission is possible only if

```
      h ν − φ₀ ≥ 0
⟹     ν ≥ φ₀/h
```

Defining ν₀ = φ₀/h, emission occurs **only if ν ≥ ν₀**. If ν < ν₀, then a single photon simply does
not carry enough energy to liberate an electron — and since the process is one photon per electron,
increasing the **intensity** only supplies **more** such inadequate photons, never a more energetic
one. Hence **no emission occurs below ν₀, however intense the light**. This is the threshold
frequency.

**(ii) Why K_max is independent of the intensity.**

```
      K_max = h ν − φ₀
```

The right-hand side contains **only the frequency ν and the material constant φ₀** — the intensity
does not appear.

Physically: the **intensity determines the number of photons arriving per second**, not the energy of
each photon. Each electron absorbs exactly **one** photon, of energy hν. So increasing the intensity
increases the **number** of photoelectrons (and hence the photocurrent) but leaves the energy
available to each one — and therefore K_max — unchanged.

### Q2 — stopping potential vs frequency graph

From Einstein's equation, eV₀ = hν − φ₀, so

```
      V₀ = (h/e) ν − φ₀/e
```

which is a **straight line** in V₀ against ν.

**Graph** (for two metals A and B with φ₀A < φ₀B):

```
   V₀ │                     ╱ A         ╱ B
      │                   ╱           ╱
      │                 ╱           ╱        (the two lines are PARALLEL)
      │               ╱           ╱
   ───┼─────────────●───────────●──────────────→ ν
      │           ν₀A         ν₀B
      │         ╱
 −φ₀/e│       ╱
```

**What the slope represents.** Comparing with y = mx + c, the slope is

```
      slope = h/e
```

the ratio of **Planck's constant to the electronic charge**. Crucially, this is a combination of two
**universal constants**, so the slope is the **same for every metal** — the two lines are parallel.
(This is how Millikan first measured h accurately.)

**How the work function is obtained.**

Two equivalent ways:
1. From the **intercept on the V₀-axis**, which equals **−φ₀/e**. So φ₀ = e × (magnitude of the
   y-intercept).
2. From the **intercept on the ν-axis**, which is the threshold frequency ν₀, since V₀ = 0 there.
   Then φ₀ = **h ν₀**.

A metal with a **larger work function** has a **larger threshold frequency**, so its line is shifted
to the **right** — which is the only difference between the two metals on this graph.

### Q3 — photocurrent vs collector potential graphs

**(i) Different intensities, at constant frequency:**

```
     I │                 ─────────── I₃
       │               ╱
       │           ─────────────── I₂
       │         ╱   ╱
       │     ──────────────── I₁
       │   ╱   ╱   ╱
   ────┴───────────────────────────→  V
     −V₀      0
       ↑
   the SAME stopping potential for all three
```

**(ii) Different frequencies, at constant intensity:**

```
     I │            ──────────────── (all reach the SAME saturation current)
       │        ╱  ╱  ╱
       │      ╱  ╱  ╱
       │    ╱  ╱  ╱
   ────┴───┴──┴──┴────────────────→  V
    −V₀₃ −V₀₂ −V₀₁  0
                       ν₃ > ν₂ > ν₁
```

**The essential difference.**

| | Different **intensities**, same ν | Different **frequencies**, same intensity |
| --- | --- | --- |
| Saturation current | **different** — larger for greater intensity | **the same** for all |
| Stopping potential | **the same** for all | **different** — larger for higher frequency |

**Why:** the **saturation current** measures the *number* of photoelectrons per second, which is set
by the **number of photons per second**, i.e. by the **intensity**. The **stopping potential**
measures K_max = hν − φ₀, which is set by the **frequency** alone.

So the first graph varies the number of photons (changing the current but not their energy), and the
second varies the energy per photon (changing the maximum kinetic energy but not the number).

### Q4 — three failures of the wave theory

| Observation | Wave theory predicts | Photon theory explains |
| --- | --- | --- |
| **K_max is independent of intensity** | A more intense wave carries more energy per unit area, so electrons should emerge with **greater** kinetic energy | Intensity = number of photons per second; each electron absorbs **one** photon of energy hν, so K_max = hν − φ₀ does not involve the intensity |
| **A threshold frequency exists** | A wave of **any** frequency should eventually eject electrons, if intense enough or applied long enough | A single photon of energy hν < φ₀ cannot liberate an electron at all, and since one electron absorbs one photon, more such photons do not help |
| **Emission is instantaneous (< 10⁻⁹ s)** | An electron must **accumulate** energy from the spread-out wave; classical estimates give a time lag of hours for a dim source | The energy arrives in a **single concentrated packet** and is absorbed all at once, so emission is immediate |

### Q5 — work function and threshold frequency

**Work function (φ₀).** The **minimum energy** required to just liberate an electron from the surface
of a metal, i.e. to bring it to the surface with zero kinetic energy. It is a **characteristic of the
metal** and is usually expressed in electron-volts.

**Threshold frequency (ν₀).** The **minimum frequency** of incident radiation below which
photoelectric emission does **not** occur from a given metal, however great the intensity of the
radiation.

**Relation between them:**

```
      φ₀ = h ν₀                     (and equivalently φ₀ = h c/λ₀)
```

### Q6 — photoelectric numerical

```
      φ₀ = 2.14 eV          λ = 500 nm
```

**(i) Threshold wavelength.** Using hc = 1240 eV nm:

```
      λ₀ = h c/φ₀ = 1240/2.14 = 579 nm
```

**λ₀ ≈ 579 nm**

*(Since the incident λ = 500 nm is **less** than λ₀ = 579 nm, the incident frequency exceeds the
threshold, so emission does occur ✓ — worth stating.)*

**(ii) Maximum kinetic energy.**

Energy of an incident photon:

```
      E = h c/λ = 1240/500 = 2.48 eV
```

```
      K_max = E − φ₀ = 2.48 − 2.14 = 0.34 eV
```

**K_max = 0.34 eV** (= 0.34 × 1.6 × 10⁻¹⁹ = 5.44 × 10⁻²⁰ J)

**(iii) Stopping potential.**

```
      e V₀ = K_max
⟹     V₀ = K_max/e = 0.34 eV/e = 0.34 V
```

**V₀ = 0.34 V**

> Notice how the **hc = 1240 eV nm** shortcut makes this whole question three lines of arithmetic
> with no powers of ten. And note that when K_max is expressed in **eV**, the stopping potential in
> **volts** is numerically the same — because eV₀ = K_max.

### Q7 — de Broglie wavelength of an accelerated electron

```
      V = 100 V
```

Using the working formula:

```
      λ = 12.27/√V  Å
        = 12.27/√100
        = 12.27/10
        = 1.227 Å
```

**λ = 1.227 Å = 1.227 × 10⁻¹⁰ m ≈ 0.123 nm**

*(Full method, if the formula is not quoted:
p = √(2meV) = √(2 × 9.1 × 10⁻³¹ × 1.6 × 10⁻¹⁹ × 100) = √(2.912 × 10⁻⁴⁷) = 5.4 × 10⁻²⁴ kg m s⁻¹,
so λ = h/p = (6.63 × 10⁻³⁴)/(5.4 × 10⁻²⁴) = 1.23 × 10⁻¹⁰ m ✓)*

### Q8 — electron vs proton of the same kinetic energy

For a particle of mass m and kinetic energy K,

```
      p = √(2 m K)                  ⟹      λ = h/p = h/√(2 m K)
```

So at the **same kinetic energy K**,

```
      λ ∝ 1/√m
```

The electron's mass is far smaller than the proton's (m_p ≈ 1836 m_e), so

```
      λ_electron/λ_proton = √(m_p/m_e) = √1836 ≈ 43
```

**The electron has the greater de Broglie wavelength** — about 43 times greater — because for the
same kinetic energy the lighter particle has the smaller momentum, and λ is inversely proportional to
momentum.

### Q9 — energy and momentum of a photon

```
      λ = 620 nm = 620 × 10⁻⁹ m
```

**Energy**, using hc = 1240 eV nm:

```
      E = hc/λ = 1240/620 = 2 eV = 2 × 1.6 × 10⁻¹⁹ = 3.2 × 10⁻¹⁹ J
```

**E = 2 eV = 3.2 × 10⁻¹⁹ J**

**Momentum:**

```
      p = h/λ = (6.63 × 10⁻³⁴)/(620 × 10⁻⁹)
        = (6.63 × 10⁻³⁴)/(6.2 × 10⁻⁷)
        = 1.07 × 10⁻²⁷ kg m s⁻¹
```

**p ≈ 1.07 × 10⁻²⁷ kg m s⁻¹**

*(Check with p = E/c = (3.2 × 10⁻¹⁹)/(3 × 10⁸) = 1.07 × 10⁻²⁷ ✓)*

### Q10 — what the stopping potential depends on

From eV₀ = hν − φ₀, the stopping potential depends on the **frequency** of the incident light and on
the work function of the metal — not on the intensity, the distance of the source, or the geometry.

**Answer: (b) the frequency of the incident light**

### Q11 — case study: the V₀–ν graph

```
      slope = 4.14 × 10⁻¹⁵ V s          ν-intercept = 5 × 10¹⁴ Hz
```

**(i) What the slope gives.** From V₀ = (h/e)ν − φ₀/e, the slope is **h/e** — the ratio of Planck's
constant to the electronic charge.

**(ii) Planck's constant:**

```
      h/e = 4.14 × 10⁻¹⁵
⟹     h = (4.14 × 10⁻¹⁵)(1.6 × 10⁻¹⁹)
        = 6.62 × 10⁻³⁴ J s
```

**h ≈ 6.6 × 10⁻³⁴ J s** — in good agreement with the accepted value.

**(iii) Work function.** The ν-intercept is the threshold frequency ν₀ = 5 × 10¹⁴ Hz, so

```
      φ₀ = h ν₀ = (6.62 × 10⁻³⁴)(5 × 10¹⁴) = 3.31 × 10⁻¹⁹ J
```

In electron-volts:

```
      φ₀ = (3.31 × 10⁻¹⁹)/(1.6 × 10⁻¹⁹) = 2.07 eV
```

**φ₀ ≈ 2.07 eV**

*(Faster route: φ₀/e = (h/e) × ν₀ = (4.14 × 10⁻¹⁵)(5 × 10¹⁴) = 2.07 V, so φ₀ = 2.07 eV directly.)*

**(iv) Would the slope change for a different metal?**

**No.** The slope is **h/e**, a combination of two **universal constants**, and contains nothing
specific to the metal. So the graph for any other metal is a **parallel** straight line.

What *does* change is the **intercept**: a different metal has a different work function, hence a
different threshold frequency ν₀ = φ₀/h, so its line is shifted horizontally. A metal with a larger
work function has its line shifted further to the right.

### Q12 — why photons are not deflected by fields

The force on a particle in electric and magnetic fields is

```
      F = q(E + v × B)
```

which is **proportional to the charge q**.

A photon is **electrically neutral** — it carries **zero charge**. Therefore the force exerted on it
by any electric or magnetic field is **zero**, and it travels through such fields undeviated.

*(This is a standard way of distinguishing gamma rays from beta and alpha radiation: only the gamma
rays, being photons, pass through a magnetic field undeflected.)*

### Q13 — Assertion–Reason

**A:** "No photoelectrons are emitted below the threshold frequency, however intense the light."
**True** — this is one of the four experimental laws.

**R:** "Photoemission is a one-photon–one-electron process, and a single photon of energy less than
the work function cannot liberate an electron." **True.**

**Does R explain A?** **Yes** — and precisely. Because each electron absorbs exactly one photon,
increasing the intensity increases only the **number** of photons, not the energy of any one of them.
If hν < φ₀, then no single photon has enough energy, and no number of them will do.

**Answer: (a) Both A and R are true, and R is the correct explanation of A.**

---

## 5. Test yourself

Time: 40 minutes. Answers below.

1. *(1)* The momentum of a photon of wavelength λ is
   (a) h/λ (b) hλ (c) hc/λ (d) λ/h
2. *(1)* The maximum kinetic energy of photoelectrons depends on
   (a) intensity (b) frequency (c) the area of the cathode (d) the distance of the source
3. *(1)* The de Broglie wavelength of a particle of mass m moving with speed v is
   (a) h/mv (b) mv/h (c) hmv (d) h/v
4. *(2)* Define stopping potential. How is it related to the maximum kinetic energy of the
   photoelectrons?
5. *(2)* The work function of caesium is 2.14 eV. Find its threshold wavelength.
6. *(2)* Find the energy in eV of a photon of wavelength 400 nm.
7. *(2)* An electron is accelerated through 400 V. Find its de Broglie wavelength.
8. *(3)* Light of frequency 8 × 10¹⁴ Hz is incident on a metal of work function 2 eV. Find the maximum
   kinetic energy of the photoelectrons and the stopping potential.
9. *(3)* State the four laws of photoelectric emission.
10. *(3)* Draw the graph of stopping potential against frequency for two metals of different work
    functions, and state two things that can be found from it.
11. *(2)* Why is the wave nature of matter not apparent in our everyday observations?
12. *(2)* A proton and an alpha particle are accelerated through the same potential difference. Find
    the ratio of their de Broglie wavelengths.
13. *(2)* If the intensity of the incident light is doubled while the frequency is unchanged, what
    happens to (i) the saturation current and (ii) the stopping potential?

### Answer key

**1. (a) h/λ.**

**2. (b) frequency.**

**3. (a) h/mv.**

**4.** The **stopping potential** is the minimum negative potential applied to the collector at which
the photoelectric current becomes **zero** — i.e. at which even the fastest photoelectrons are just
turned back. It is related to the maximum kinetic energy by **eV₀ = K_max**.

**5. 579 nm.** λ₀ = hc/φ₀ = 1240/2.14 = 579 nm.

**6. 3.1 eV.** E = hc/λ = 1240/400 = 3.1 eV.

**7. 0.613 Å.** λ = 12.27/√400 = 12.27/20 = 0.613 Å = 6.13 × 10⁻¹¹ m.

**8. K_max = 1.31 eV; V₀ = 1.31 V.**
E = hν = (6.63 × 10⁻³⁴)(8 × 10¹⁴) = 5.30 × 10⁻¹⁹ J = 5.30 × 10⁻¹⁹/1.6 × 10⁻¹⁹ = 3.31 eV.
K_max = 3.31 − 2 = 1.31 eV. V₀ = 1.31 V.

**9.** (i) For a fixed frequency above threshold, the photocurrent is **proportional to the
intensity**. (ii) The **maximum kinetic energy** of the photoelectrons depends only on the
**frequency** and the metal, and is independent of the intensity. (iii) For each metal there is a
**threshold frequency** below which no emission occurs, whatever the intensity. (iv) Emission is
**instantaneous** (< 10⁻⁹ s).

**10.** Graph as in §4 Q2 — two **parallel** straight lines with different ν-intercepts. From it one
can find: (i) **Planck's constant**, from the slope h/e; (ii) the **threshold frequency** of each
metal, from its ν-intercept — and hence its **work function**, φ₀ = hν₀ (or from the magnitude of the
V₀-intercept, φ₀/e).

**11.** The de Broglie wavelength λ = h/mv is inversely proportional to the mass. For everyday
objects the mass is enormous compared with atomic scales — a 100 g ball moving at 10 m s⁻¹ has
λ = (6.63 × 10⁻³⁴)/(0.1 × 10) ≈ **6.6 × 10⁻³⁴ m**. This is unimaginably smaller than any aperture or
obstacle available, so no diffraction or interference can be observed and the wave nature is
completely undetectable. Wave behaviour becomes apparent only for particles of very small mass, such
as electrons.

**12. λ_p/λ_α = 2√2 : 1.** For acceleration through the same V, λ = h/√(2mqV), so λ ∝ 1/√(mq).
For a proton, m = m, q = e. For an alpha particle, m = 4m, q = 2e.
λ_p/λ_α = √(4m × 2e)/√(m × e) = √8 = **2√2 ≈ 2.83**.

**13.** (i) The **saturation current doubles**, since twice as many photons arrive per second and hence
twice as many photoelectrons are emitted per second. (ii) The **stopping potential is unchanged**,
because eV₀ = hν − φ₀ depends only on the frequency, which has not changed.

**Scoring.** Out of 26. Below 18 → the gap is almost certainly the three graphs. Draw all three from
memory, labelled, and state what the slope and intercepts of the third one mean.

---

## 6. Answering tips

**On Einstein's equation**

1. **Always write hν = φ₀ + K_max first**, then rearrange to whatever the question needs. Do not
   start from K_max = h(ν − ν₀).

2. **When explaining a law, quote the equation and point to the missing variable.** "K_max = hν − φ₀
   contains no intensity term" is the mark for the independence-of-intensity question.

3. **Say "one photon, one electron".** That phrase carries the whole conceptual content, and it is
   what makes the threshold-frequency argument work.

**On the graphs**

4. **Label both axes with quantity and unit**, mark the stopping potential(s) on the negative
   V-axis, and label which curve corresponds to which intensity or frequency. Unlabelled graphs score
   little.

5. **For the intensity graph: different saturation currents, same stopping potential.** For the
   frequency graph: **same** saturation current, **different** stopping potentials. Get these the
   right way round — it is exactly what is being tested.

6. **For the V₀–ν graph, state all three readings:** slope = h/e (universal, so lines for different
   metals are parallel), ν-intercept = ν₀, V₀-intercept = −φ₀/e. Three facts, and each can be a mark.

7. **Draw two parallel lines when two metals are asked for.** Non-parallel lines contradict the
   physics and lose the mark.

**On numericals**

8. **Use hc = 1240 eV nm.** It turns E = hc/λ into a division: 1240/λ(nm) gives the energy directly
   in eV. This single shortcut removes most of the arithmetic in this chapter.

9. **Use λ = 12.27/√V Å for accelerated electrons.** Quote it, then substitute. If the question asks
   you to derive it, show p = √(2meV) and then λ = h/p.

10. **When K_max is in eV, V₀ in volts is numerically the same.** So "K_max = 0.34 eV" immediately
    gives "V₀ = 0.34 V" — say why (eV₀ = K_max), and you get both marks in one line.

11. **Check whether emission occurs at all.** If the incident wavelength exceeds λ₀ (or the frequency
    is below ν₀), the answer is "no photoelectrons are emitted", and any calculated "negative kinetic
    energy" is a sign you have missed this. CBSE sets such questions deliberately.

12. **For comparison questions (electron vs proton, proton vs alpha), reduce to a proportionality
    first.** λ ∝ 1/√(mK) for equal energies, λ ∝ 1/√(mq) for equal accelerating voltages. Then
    substitute the ratios. Much faster and less error-prone than computing both wavelengths.

13. **Units:** eV or J for energy, V for stopping potential, Å or nm or m for wavelength,
    kg m s⁻¹ for momentum, Hz for frequency.
