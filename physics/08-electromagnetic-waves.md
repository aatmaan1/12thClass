# Ch 8 — Electromagnetic Waves

**Units V + VI (18 marks, shared with Ch 9 and Ch 10) · Typical appearance: 1–2 MCQs + a 2-mark
question on the EM spectrum or the properties of EM waves. Small chapter, reliable marks — the best
marks-per-page ratio in the book.**

---

## 1. Scope

### In the syllabus

- **Basic idea of displacement current**
- **Electromagnetic waves**, their **characteristics**, their **transverse nature** (qualitative ideas
  only)
- **Electromagnetic spectrum** — radio waves, microwaves, infrared, visible, ultraviolet, X-rays,
  gamma rays — including **elementary facts about their uses**

### Deleted

Nothing substantial. Note the phrase "**qualitative ideas only**" — you are not asked to derive the
wave equation from Maxwell's equations, only to know the properties and be able to justify them.

> **Why this chapter is worth your time.** It is two or three pages of content that reliably supplies
> 2–4 marks, mostly in Sections A and B, and the marks come from a single memorised table. Learn the
> spectrum table cold and you have banked them.

---

## 2. Brief

### Start here — in plain English

By 1860 there were four laws of electricity and magnetism, and Maxwell noticed that one of them was
broken. Ampere's law said a magnetic field circles a current — but what about the gap between a
capacitor's plates, where no charge crosses and yet the circuit plainly works? Follow the law
literally and you get a magnetic field on one side of the gap and none on the other, which is
absurd.

Maxwell's fix was to say that a **changing electric field** is, for magnetic purposes, as good as a
current. He called it the **displacement current**, I_d = ε₀ dφ_E/dt. In the capacitor gap the field
between the plates is building up, and that build-up is exactly what keeps the magnetic field
continuous. It is a small repair with an enormous consequence, and it is the one thing to remember
from this short chapter.

Because now look at what the laws say together. A changing magnetic field creates an electric field
— that is Faraday, Chapter 6. And a changing electric field creates a magnetic field — that is
Maxwell's new term. So a changing field of either kind creates the other, which is itself changing,
which recreates the first. The two fields sustain each other and travel, needing no wire, no charge
and no medium at all. That is an **electromagnetic wave**, and light is one.

Maxwell could even compute how fast it goes, from two numbers already measured in laboratories with
batteries and magnets: c = 1/√(μ₀ε₀), which comes out at 3 × 10⁸ m/s. That matched the measured
speed of light, and settled what light was — a question that had been open for two centuries.

The **structure** of the wave is worth picturing properly, because it is asked directly. E and B
oscillate in step, both at right angles to each other *and* both at right angles to the direction
of travel — the wave is transverse twice over. Their magnitudes are locked: E₀/B₀ = c, so the
electric part is numerically much larger, which is why light interacts with matter mostly through
its electric field. The direction of travel is along E × B.

The wave carries energy, split equally between the electric and magnetic halves. It also carries
**momentum**, which is why a light beam exerts a faint pressure — the principle behind solar sails.

The **spectrum** is the same phenomenon across twenty-odd orders of magnitude of frequency, and the
only reason the bands have different names is the history of how each was discovered. Radio waves,
microwaves, infrared, visible, ultraviolet, X-rays, gamma rays — one family, in order of increasing
frequency and decreasing wavelength. Learn that order, one production method and one use per band,
and roughly where the boundaries sit; that is the whole of the chapter's factual load and it appears
almost every year as a one- or two-marker. Visible light occupies a laughably narrow slice, about
400 to 700 nm, and the ozone layer's job is absorbing the ultraviolet just above it.

This is the shortest chapter in the book and among the most reliably rewarding: the questions are
short, factual and repetitive. Do not skip it because it looks slight.

**Learn it from someone else too**

- **Video lecture** — [search: electromagnetic waves class 12 one shot](https://www.youtube.com/results?search_query=electromagnetic+waves+class+12+one+shot)
- **Interactive lessons and practice** — [Khan Academy: electromagnetic waves](https://www.khanacademy.org/search?page_search_query=electromagnetic%20waves%20class%2012)
- **The book the paper is set from** — [NCERT Physics Part I, Chapter 8 (PDF)](https://ncert.nic.in/textbook/pdf/leph108.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 40 *Electromagnetic Waves*. It is brief, which
  suits the chapter; read §40.1–40.3 for the displacement current and how the wave equation falls
  out, and use the NCERT for the spectrum table.

---

### Displacement current — why Ampere's law needed fixing

**The problem.** Consider a **capacitor being charged**. A current flows in the wires, but **no charge
crosses the gap** between the plates.

Apply Ampere's law, ∮**B**·d**l** = μ₀I, to a circular loop around the wire, and choose two different
surfaces bounded by that loop:

- A surface that the **wire** pierces → the enclosed conduction current is I, so ∮**B**·d**l** = μ₀I.
- A surface that passes **between the plates** → no conduction current pierces it, so
  ∮**B**·d**l** = 0.

The same loop gives two different answers. **Ampere's law, as originally stated, is inconsistent.**

**Maxwell's resolution.** Between the plates there is no conduction current, but there **is a
changing electric field**, and hence a changing electric flux. Maxwell proposed that a changing
electric flux is itself equivalent to a current — the **displacement current**:

```
      I_d = ε₀ (dφ_E/dt)
```

where φ_E is the electric flux.

**The corrected law — the Ampere–Maxwell law:**

```
      ∮ B · dl = μ₀ ( I_c + I_d )  =  μ₀ ( I_c + ε₀ dφ_E/dt )
```

where I_c is the conduction current.

**With this correction the inconsistency disappears:** between the plates, the displacement current
is exactly equal to the conduction current in the wires, so both surfaces give the same answer.
The **total current** (conduction + displacement) is continuous around a circuit.

> **The conceptual point, and it is the asked one:** just as a changing magnetic field produces an
> electric field (Faraday's law), a **changing electric field produces a magnetic field**. This
> symmetry between the two is what makes self-sustaining electromagnetic waves possible.

### Maxwell's equations (qualitative)

The four equations that summarise all of classical electromagnetism:

| Equation | Meaning |
| --- | --- |
| ∮**E**·d**A** = q/ε₀ | Gauss's law for electricity — charges produce electric fields |
| ∮**B**·d**A** = 0 | Gauss's law for magnetism — no magnetic monopoles |
| ∮**E**·d**l** = −dφ_B/dt | Faraday's law — a changing **B** produces **E** |
| ∮**B**·d**l** = μ₀(I_c + ε₀ dφ_E/dt) | Ampere–Maxwell law — currents and a changing **E** produce **B** |

Maxwell showed that these equations predict **electromagnetic waves** travelling through vacuum at
speed 1/√(μ₀ε₀), which turned out to equal the measured speed of light — the discovery that light
*is* an electromagnetic wave.

### Nature and properties of electromagnetic waves

An EM wave consists of **mutually perpendicular, oscillating electric and magnetic fields**
propagating through space.

```
                    E (oscillating, say along y)
                    ↑
                    │
                    │
      ──────────────┼───────────────→  direction of propagation (say x)
                   ╱
                  ╱
                 B (oscillating, along z)

           E ⊥ B ⊥ direction of propagation
```

**The properties — this list is a standard 2- or 3-mark question:**

1. **Transverse.** Both **E** and **B** oscillate **perpendicular to the direction of propagation**
   (and perpendicular to each other). The direction of propagation is along **E** × **B**.

2. **They need no material medium.** EM waves propagate through vacuum — unlike sound, which requires
   a medium. This is because they are sustained by the mutual generation of **E** and **B**.

3. **Speed in vacuum:**

```
      c = 1/√(μ₀ ε₀) = 3 × 10⁸ m s⁻¹
```

   The same for all EM waves, whatever their frequency.

4. **The field amplitudes are related by:**

```
      c = E₀/B₀                     (and at every instant, E/B = c)
```

   So B₀ is smaller than E₀ by the factor c — which is why the magnetic effects of light are hard to
   detect.

5. **E and B oscillate in phase** — they reach their maxima and zeros together.

6. **They are not deflected** by electric or magnetic fields, because they carry **no charge**.

7. **They carry energy and momentum**, and therefore exert **radiation pressure** on a surface they
   fall on. Momentum delivered p = U/c for complete absorption.

8. **Energy is shared equally** between the electric and magnetic fields:

```
      u_E = ½ ε₀ E²                 u_B = B²/(2μ₀)                 ⟨u_E⟩ = ⟨u_B⟩
```

   and the average total energy density is

```
      ⟨u⟩ = ½ ε₀ E₀²/2 + … = ½ ε₀ E_rms²  ×  2  =  ½ ε₀ E₀²  ×  ½  ×  2
```

   which is most simply written as ⟨u⟩ = ½ε₀E₀² (half from each field, with E_rms² = E₀²/2).

9. **They are produced by accelerating charges** (an oscillating charge radiates at its own frequency
   of oscillation).

10. **In a medium** of refractive index n, the speed is reduced:

```
      v = 1/√(μ ε) = c/n
```

    The **frequency stays the same**; the **wavelength** shortens to λ/n.

### The electromagnetic spectrum

**Learn this table.** It answers most of what this chapter is asked.

| Radiation | Wavelength range | Source | Detection | Uses |
| --- | --- | --- | --- | --- |
| **Radio waves** | > 0.1 m | oscillating LC circuits, accelerated charges in aerials | receiving aerials | radio and TV broadcasting, cellular telephony |
| **Microwaves** | 0.1 m – 1 mm | klystrons, magnetrons | point-contact diodes | radar, satellite communication, microwave ovens, speed guns |
| **Infrared** | 1 mm – 700 nm | hot bodies and molecules | thermopiles, bolometers, thermal cameras | heating, remote controls, night vision, physiotherapy, greenhouse effect |
| **Visible light** | 700 nm – 400 nm | the Sun, lamps, arcs | the eye, photocells, photographic film | vision, photosynthesis, optics, photography |
| **Ultraviolet** | 400 nm – 1 nm | the Sun, arc lamps, mercury vapour lamps | photocells, photographic film | sterilising water and surgical instruments, LASIK eye surgery, detecting forgeries |
| **X-rays** | 1 nm – 10⁻³ nm | X-ray tubes, inner-shell electron transitions | photographic film, Geiger tubes | medical radiography, cancer treatment, crystal-structure studies, security scanning |
| **Gamma rays** | < 10⁻³ nm | radioactive nuclei, nuclear reactions | ionisation chambers, scintillation counters | cancer treatment (radiotherapy), sterilising medical equipment, studying nuclear structure |

**The order — memorise the sequence:**

```
      RADIO → MICROWAVE → INFRARED → VISIBLE → ULTRAVIOLET → X-RAY → GAMMA
      ←──── wavelength increasing ────      ────  frequency and energy increasing ────→
```

**Mnemonic:** "**R**oman **M**en **I**nvented **V**ery **U**nusual **X**-ray **G**uns."

**Visible light in detail** (worth having): violet ≈ 400 nm, and red ≈ 700 nm. So **violet has the
shortest wavelength and highest frequency** of visible light, red the longest and lowest.

> **The commonest exam question in this chapter** is: "identify the radiation given its wavelength /
> its use / its source". It is answered directly from the table above. The second commonest is "which
> has the highest frequency / shortest wavelength / most energy", answered from the order.

### Useful relations

```
      c = ν λ                       ν = frequency, λ = wavelength
      E = h ν = h c/λ               energy of one photon (see Ch 11)
      ω = 2π ν                      k = 2π/λ                 c = ω/k
```

A plane EM wave travelling along x:

```
      E_y = E₀ sin(kx − ωt)                 B_z = B₀ sin(kx − ωt)
```

### Quick recall box

```
DISPLACEMENT CURRENT : I_d = ε₀ dφ_E/dt
  needed because Ampere's law is inconsistent for a CHARGING CAPACITOR
  Ampere–Maxwell : ∮B·dl = μ₀(I_c + ε₀ dφ_E/dt)
  a CHANGING ELECTRIC FIELD produces a MAGNETIC FIELD

EM WAVE PROPERTIES
  transverse ; E ⊥ B ⊥ direction of propagation (direction along E × B)
  need NO medium ;  c = 1/√(μ₀ε₀) = 3 × 10⁸ m s⁻¹ ;  c = E₀/B₀
  E and B in phase ;  not deflected by E or B fields (no charge)
  carry energy AND momentum → radiation pressure
  energy shared EQUALLY between the E and B fields
  produced by ACCELERATING charges
  in a medium : v = c/n ,  λ → λ/n ,  FREQUENCY UNCHANGED

SPECTRUM ORDER (increasing frequency / decreasing wavelength):
  RADIO → MICROWAVE → INFRARED → VISIBLE → ULTRAVIOLET → X-RAY → GAMMA
  visible: violet ≈ 400 nm (highest f)  ...  red ≈ 700 nm (lowest f)

c = νλ ;  E_photon = hν = hc/λ
```

---

## 3. Previous years' questions

**Q1.** *(3 marks)* What is displacement current? Explain why Maxwell found it necessary to introduce
it, and write the modified form of Ampere's circuital law.

**Q2.** *(3 marks)* State any four characteristics of electromagnetic waves.

**Q3.** *(2 marks)* Arrange the following in ascending order of frequency: X-rays, microwaves,
infrared, gamma rays, visible light.

**Q4.** *(2 marks)* Write two uses each of (i) microwaves and (ii) ultraviolet radiation.

**Q5.** *(2 marks)* Show that the speed of an electromagnetic wave in vacuum is given by
c = 1/√(μ₀ε₀), and compute its value. (μ₀ = 4π × 10⁻⁷ T m A⁻¹, ε₀ = 8.854 × 10⁻¹² C² N⁻¹ m⁻²)

**Q6.** *(2 marks)* An electromagnetic wave has an electric field amplitude of 60 V m⁻¹. Find the
amplitude of the magnetic field.

**Q7.** *(2 marks)* Why are electromagnetic waves not deflected by an electric or a magnetic field?

**Q8.** *(2 marks)* Name the electromagnetic radiation used (i) in radar, (ii) to sterilise surgical
instruments, (iii) in remote controls, (iv) for medical imaging of bones.

**Q9.** *(2 marks)* An EM wave has a frequency of 5 × 10¹⁴ Hz. Find its wavelength in vacuum and
identify the part of the spectrum it belongs to.

**Q10.** *(1 mark, MCQ)* In an electromagnetic wave, the electric and magnetic fields are
(a) parallel to each other (b) perpendicular to each other and to the direction of propagation
(c) parallel to the direction of propagation (d) at 45° to each other

**Q11.** *(2 marks)* State the direction of propagation of an electromagnetic wave whose electric
field oscillates along the y-axis and whose magnetic field oscillates along the z-axis.

**Q12.** *(1 mark, Assertion–Reason)*
**A:** Electromagnetic waves can travel through vacuum.
**R:** Electromagnetic waves are produced by accelerating charges.

---

## 4. Solutions

### Q1 — displacement current

**Definition.** The **displacement current** is the current equivalent to a **changing electric flux**:

```
      I_d = ε₀ (dφ_E/dt)
```

**Why Maxwell found it necessary.**

*Diagram:* a capacitor being charged, with a circular Amperian loop around the connecting wire, and
two alternative surfaces bounded by that loop — one pierced by the wire, and one that passes through
the gap between the plates.

Consider a **capacitor being charged**. A conduction current I flows in the connecting wires, but **no
charge crosses the gap** between the plates.

Now apply Ampere's law, ∮**B**·d**l** = μ₀I, to a circular loop encircling the wire. The law refers to
"the current through the loop", which means the current through **any surface bounded by that loop**.
But:

- Choosing a **flat surface pierced by the wire**, the enclosed current is I, so ∮**B**·d**l** = μ₀I.
- Choosing instead a **bulging surface that passes between the capacitor plates**, no conduction
  current pierces it at all, so ∮**B**·d**l** = 0.

The same loop gives two contradictory results, so **Ampere's law in its original form is
inconsistent**.

**Maxwell's resolution.** Between the plates there is no conduction current, but the charge on the
plates is increasing, so the electric field — and hence the **electric flux** — between them is
**changing**. Maxwell proposed that this changing electric flux acts as a current, the displacement
current I_d = ε₀ dφ_E/dt, and that it must be added to the conduction current.

**Modified (Ampere–Maxwell) law:**

```
      ∮ B · dl = μ₀ ( I_c + I_d )  =  μ₀ ( I_c + ε₀ dφ_E/dt )
```

With this correction, the displacement current between the plates is exactly equal to the conduction
current in the wires, so both choices of surface give the same result and the inconsistency
disappears. The **total** current is continuous around the circuit.

**The deeper significance:** it establishes that a **changing electric field produces a magnetic
field**, the counterpart of Faraday's law that a changing magnetic field produces an electric field.
This mutual generation is what allows self-sustaining electromagnetic waves.

### Q2 — characteristics of electromagnetic waves

Any four of:

1. **They are transverse waves.** The electric field **E** and the magnetic field **B** both oscillate
   **perpendicular to the direction of propagation**, and are also perpendicular to each other. The
   wave travels along the direction of **E** × **B**.

2. **They require no material medium** for propagation and can travel through vacuum, unlike
   mechanical waves such as sound.

3. **They travel in vacuum with the same speed** for all frequencies:

```
      c = 1/√(μ₀ε₀) = 3 × 10⁸ m s⁻¹
```

4. **The amplitudes of the fields are related by** c = E₀/B₀, and **E** and **B** oscillate **in
   phase**.

5. **They are not deflected** by electric or magnetic fields, since they carry no charge.

6. **They carry energy and momentum**, and hence exert **radiation pressure** on a surface.

7. **The energy is shared equally** between the electric and the magnetic field.

8. **They are produced by accelerating (oscillating) charges.**

### Q3 — ascending order of frequency

Using the spectrum order (increasing frequency: radio → microwave → infrared → visible →
ultraviolet → X-ray → gamma):

```
      microwaves  <  infrared  <  visible light  <  X-rays  <  gamma rays
```

*(Equivalently, in descending order of wavelength: microwaves, infrared, visible, X-rays, gamma
rays.)*

### Q4 — uses

**(i) Microwaves** — any two of:
- **Radar** and speed-detection guns (traffic police)
- **Satellite communication** and long-distance telecommunication
- **Microwave ovens** — the microwave frequency matches the natural frequency of water molecules, so
  the water in food absorbs the energy efficiently and the food is heated from within

**(ii) Ultraviolet radiation** — any two of:
- **Sterilising** drinking water and surgical instruments (UV kills bacteria)
- **LASIK** eye surgery
- **Detecting forgeries** in banknotes and signatures (fluorescence)
- Producing vitamin D in the skin

### Q5 — speed of an EM wave in vacuum

Maxwell's equations predict that electromagnetic disturbances propagate through vacuum as waves with
speed

```
      c = 1/√(μ₀ ε₀)
```

**Computing it:**

```
      μ₀ ε₀ = (4π × 10⁻⁷)(8.854 × 10⁻¹²)
            = (1.2566 × 10⁻⁶)(8.854 × 10⁻¹²)
            = 1.1127 × 10⁻¹⁷
```

```
      √(μ₀ε₀) = √(1.1127 × 10⁻¹⁷) = 3.336 × 10⁻⁹
```

```
      c = 1/(3.336 × 10⁻⁹) = 2.998 × 10⁸ m s⁻¹
```

**c ≈ 3 × 10⁸ m s⁻¹**

The fact that this computed value agreed with the experimentally measured speed of light was
Maxwell's decisive evidence that **light is an electromagnetic wave**.

### Q6 — magnetic field amplitude

```
      c = E₀/B₀
⟹     B₀ = E₀/c
          = 60/(3 × 10⁸)
          = 2 × 10⁻⁷ T
```

**B₀ = 2 × 10⁻⁷ T**

*(Note how small this is compared with the electric amplitude — smaller by a factor of c. This is
why the magnetic effects of light are far harder to observe than the electric ones.)*

### Q7 — why EM waves are not deflected

Electric and magnetic fields exert forces only on **charged** particles:

```
      F = q(E + v × B)
```

An electromagnetic wave consists of **oscillating electric and magnetic fields** — it is a
disturbance in the fields themselves, and **carries no net charge** (q = 0). Since the deflecting
force is proportional to the charge, the force on an EM wave is zero, and it therefore travels
undeviated through electric and magnetic fields.

*(Contrast: a beam of electrons or of alpha particles **is** deflected, because those particles are
charged. This is a standard way to distinguish gamma rays from beta and alpha radiation.)*

### Q8 — naming radiations by their use

| Use | Radiation |
| --- | --- |
| (i) Radar | **Microwaves** |
| (ii) Sterilising surgical instruments | **Ultraviolet** |
| (iii) Remote controls (TV, air conditioner) | **Infrared** |
| (iv) Medical imaging of bones | **X-rays** |

### Q9 — wavelength from frequency

```
      c = ν λ
⟹     λ = c/ν
        = (3 × 10⁸)/(5 × 10¹⁴)
        = 0.6 × 10⁻⁶
        = 6 × 10⁻⁷ m
        = 600 nm
```

**λ = 600 nm**, which lies in the **visible** region of the spectrum (400–700 nm) — specifically in
the orange part.

### Q10 — orientation of E and B

**Answer: (b) perpendicular to each other and to the direction of propagation**

### Q11 — direction of propagation

The direction of propagation of an electromagnetic wave is along **E** × **B**.

With **E** along ĵ (the y-axis) and **B** along k̂ (the z-axis):

```
      ĵ × k̂ = î
```

**The wave propagates along the +x direction (the x-axis).**

### Q12 — Assertion–Reason

**A:** "Electromagnetic waves can travel through vacuum." **True.**

**R:** "Electromagnetic waves are produced by accelerating charges." **True.**

**Does R explain A?** **No.** How an EM wave is *produced* is a different matter from whether it needs
a *medium* to propagate. The correct explanation of A is that an EM wave is sustained by the mutual
generation of oscillating electric and magnetic fields — a changing **E** produces **B** and a
changing **B** produces **E** — which requires no material medium.

**Answer: (b) Both A and R are true, but R is not the correct explanation of A.**

---

## 5. Test yourself

Time: 25 minutes. Answers below.

1. *(1)* Which of the following has the shortest wavelength?
   (a) radio waves (b) X-rays (c) gamma rays (d) ultraviolet
2. *(1)* The speed of all electromagnetic waves in vacuum is
   (a) the same (b) greater for shorter wavelengths (c) greater for longer wavelengths (d) zero
3. *(1)* Displacement current arises due to a changing
   (a) magnetic flux (b) electric flux (c) current (d) resistance
4. *(2)* Write the Ampere–Maxwell law and identify each term.
5. *(2)* Name the radiation used in (i) satellite communication and (ii) treating cancer.
6. *(2)* An EM wave has a wavelength of 3 cm. Find its frequency and name the part of the spectrum.
7. *(2)* The magnetic field amplitude of an EM wave is 5 × 10⁻⁸ T. Find the electric field amplitude.
8. *(3)* State four properties of electromagnetic waves.
9. *(2)* Why does a microwave oven heat food containing water particularly efficiently?
10. *(2)* An EM wave travels along the +z direction with its electric field along the x-axis. In which
    direction does the magnetic field oscillate?
11. *(2)* How does the wavelength and frequency of light change when it passes from air into glass of
    refractive index 1.5?
12. *(2)* Arrange in increasing order of wavelength: gamma rays, radio waves, visible light,
    ultraviolet.

### Answer key

**1. (c) gamma rays.**

**2. (a) the same.**

**3. (b) electric flux.**

**4.** ∮**B**·d**l** = μ₀(I_c + ε₀ dφ_E/dt). Here ∮**B**·d**l** is the line integral of the magnetic
field around a closed loop; **I_c** is the **conduction current** threading the loop; and
**ε₀ dφ_E/dt** is the **displacement current**, arising from the rate of change of electric flux
through the loop.

**5.** (i) **Microwaves**; (ii) **Gamma rays** (radiotherapy). *(X-rays are also used in cancer
treatment and are acceptable.)*

**6. ν = 10¹⁰ Hz; microwaves.** ν = c/λ = (3 × 10⁸)/(3 × 10⁻²) = 10¹⁰ Hz. A wavelength of 3 cm lies in
the **microwave** region (0.1 m to 1 mm).

**7. E₀ = 15 V m⁻¹.** E₀ = cB₀ = (3 × 10⁸)(5 × 10⁻⁸) = 15 V m⁻¹.

**8.** Any four from §4 Q2 — transverse; no medium needed; c = 1/√(μ₀ε₀) the same for all frequencies;
c = E₀/B₀ with E and B in phase; undeflected by E and B fields; carry energy and momentum and exert
radiation pressure; energy shared equally between the fields; produced by accelerating charges.

**9.** The frequency of the microwaves used in an oven is close to the **natural (resonant) frequency
of vibration of water molecules**. Water molecules in the food therefore **absorb the microwave
energy very efficiently**, gaining kinetic energy which is shared with the surrounding food as heat.
Because the microwaves penetrate the food, it is heated **throughout its volume** rather than only at
the surface.

**10. Along the y-axis.** The direction of propagation is along **E** × **B**. With propagation along
k̂ and **E** along î, we need î × **B̂** = k̂. Since î × ĵ = k̂, **B** oscillates along **ĵ (the
y-axis)**.

**11.** The **frequency remains unchanged** — it is set by the source. The **speed** falls to
v = c/n = c/1.5, so since v = νλ with ν fixed, the **wavelength decreases** to λ/1.5, i.e. to two
thirds of its value in air.

**12.** gamma rays < ultraviolet < visible light < radio waves.

**Scoring.** Out of 22. Below 16 → the spectrum table is the whole chapter. Write it out from memory
(radiation, wavelength range, one source, two uses) and you are done.

---

## 6. Answering tips

1. **The spectrum table is the chapter.** Write it out from memory once a week during revision:
   seven radiations, in order, with wavelength range, one source, and two uses each. Nearly every
   question here is a lookup from that table.

2. **For the displacement-current question, the capacitor argument is essential.** State the two
   different surfaces and the two different answers explicitly. Just writing I_d = ε₀dφ_E/dt scores
   about a third of the marks; explaining *why* it was needed scores the rest.

3. **Draw the two Amperian surfaces on your diagram.** One pierced by the wire, one through the
   capacitor gap. It makes the inconsistency visible and it is worth a mark.

4. **Say the conceptual conclusion:** "a changing electric field produces a magnetic field, just as a
   changing magnetic field produces an electric field." Examiners look for that sentence.

5. **For "state the properties", give a numbered list and be specific.** "Transverse" alone is weak;
   "transverse — **E** and **B** both oscillate perpendicular to the direction of propagation and
   perpendicular to each other" is the full mark.

6. **Use E × B for the direction of propagation.** Write the cross product of the unit vectors
   explicitly (î × ĵ = k̂) — it is one line and it is the method mark.

7. **c = E₀/B₀, so B₀ = E₀/c.** Note which way round it goes: the magnetic amplitude is the **smaller**
   of the two by a factor of c. If your B₀ comes out larger than E₀, you have inverted it.

8. **In a medium, frequency is unchanged and wavelength shortens.** This gets asked in Ray Optics too
   ([Ch 9](09-ray-optics-and-optical-instruments.md)). The frequency is fixed by the source; the
   medium changes the speed, and hence the wavelength.

9. **Learn the visible-range endpoints:** violet ≈ 400 nm, red ≈ 700 nm. Then any "identify the
   region" question is answered by comparison.

10. **Do not use "displacement current means charge moves across the gap."** Nothing crosses the gap —
    it is the *changing electric flux* that plays the role of a current. Saying otherwise loses the
    conceptual mark.
