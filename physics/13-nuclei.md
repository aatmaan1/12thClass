# Ch 13 — Nuclei

**Units VII + VIII (12 marks, shared with Ch 11 and Ch 12) · Typical appearance: 1 MCQ + a 2/3-mark
question, most often on the binding-energy-per-nucleon curve or a mass-defect numerical.**

---

## 1. Scope

### In the syllabus

- **Composition and size** of the nucleus
- **Nuclear force**
- **Mass–energy relation**; **mass defect**
- **Binding energy per nucleon** and its **variation with mass number**
- **Nuclear fission**; **nuclear fusion**

### Deleted — do not study

- **Radioactivity** in its entirety:
  - alpha, beta and gamma particles/rays and their properties
  - **radioactive decay law**, N = N₀e^(−λt)
  - **half-life** and **mean life**
  - activity, becquerel and curie

> **This is one of the largest deletions in the Physics syllabus.** Radioactivity used to supply most
> of this chapter's numericals — half-life problems, decay-law calculations, activity questions.
> **All of it is out.** Pre-2023 papers and question banks are dominated by it, so cross those
> questions out before practising.
>
> What remains is small and highly predictable, and centres almost entirely on the **binding energy
> per nucleon curve**.

---

## 2. Brief

### Start here — in plain English

Rutherford found the nucleus. This chapter asks what it is made of, why it holds together, and why
some of them fall apart.

It is made of protons and neutrons — collectively **nucleons** — packed into a sphere about
10⁻¹⁵ m across. A quick calculation with R = R₀A^(1/3) gives a density of around 10¹⁷ kg/m³, which
is roughly a hundred million tonnes per teaspoon. Notice also what that formula says: the radius
grows as the cube root of the number of nucleons, so volume grows in proportion to A, so **nuclear
density is the same for every nucleus**. Nucleons are packed like marbles in a bag, touching, not
compressible.

Which raises the obvious problem: a nucleus is a handful of protons, all positive, jammed together.
Coulomb's law says they should blow apart violently. Something much stronger is holding them, and it
is called the **strong nuclear force** — attractive, indifferent to charge, and with an extremely
short range. Beyond a few femtometres it is simply absent, which is why very large nuclei are
unstable: add enough protons and the electrostatic repulsion, which reaches across the whole
nucleus, starts to beat a force that only acts between neighbours.

Now the chapter's central and most beautiful fact. Weigh a helium nucleus and it comes out *lighter*
than its two protons and two neutrons weighed separately. Mass has gone missing. It has become
binding energy, via E = mc²: the **mass defect** Δm is the mass equivalent of the energy you would
have to supply to pull the nucleus apart. Bound systems weigh less than their parts. The
conventional unit here is the atomic mass unit, and the number to remember is that **1 u releases
931.5 MeV**.

Divide the binding energy by the number of nucleons and you get **binding energy per nucleon**,
which measures how tightly each nucleon is held — and the graph of it against A is the single most
important picture in the chapter. It rises steeply for light nuclei, peaks around A = 56 (iron), and
then falls slowly. Everything about nuclear energy is on that graph. Nuclei to the left can move
*up* the curve by joining together, releasing energy: that is **fusion**, and it is what the Sun
does. Nuclei to the right can move up by splitting: that is **fission**, and it is what a reactor
does. Both release energy because both end up with more tightly bound nucleons. Iron sits at the
peak, which is why it is the ash of stellar burning and why you cannot extract energy from it by
either route.

**Radioactivity** is the other half of the chapter, and it is simpler than it looks. An unstable
nucleus has three ways out. **Alpha** decay throws out a helium nucleus, dropping A by 4 and Z by 2
— the route heavy nuclei take to shed bulk. **Beta** decay converts a neutron into a proton (or the
reverse), changing Z by one while A stays put — the route for nuclei with the wrong neutron-to-proton
balance. **Gamma** emission changes neither; it is just an excited nucleus dropping to a lower
energy level, the nuclear version of Chapter 12's photon jump.

The **decay law** is worth understanding rather than memorising, because it explains the half-life.
Each nucleus has a fixed probability of decaying in the next second, and no memory of how long it
has already waited. So the number decaying per second is proportional to how many are left:
dN/dt = −λN, giving N = N₀e^(−λt). A fixed *fraction* goes per unit time, which is exactly what
makes the **half-life** a constant — the time for half of whatever remains to go, the same whether
you start with a kilogram or a microgram.

**Learn it from someone else too**

- **Video lecture** — [search: nuclei class 12 physics one shot](https://www.youtube.com/results?search_query=nuclei+class+12+physics+one+shot)
- **Interactive lessons and practice** — [Khan Academy: nuclei, mass defect and binding energy](https://www.khanacademy.org/search?page_search_query=mass%20defect%20binding%20energy%20nuclei)
- **The book the paper is set from** — [NCERT Physics Part II, Chapter 13 (PDF)](https://ncert.nic.in/textbook/pdf/leph205.pdf)
- **HC Verma** — *Concepts of Physics* Part 2, Ch 46 *The Nucleus*. §46.2–46.5 on binding energy and
  the BE-per-nucleon curve, then §46.6–46.9 for the decay law and the three decay modes. His
  discussion of why the curve's shape permits both fission and fusion is the one to read.

---

### Composition of the nucleus

The nucleus contains **protons** and **neutrons**, collectively called **nucleons**.

```
      Z = atomic number   = number of protons
      N = neutron number  = number of neutrons
      A = mass number     = Z + N = total number of nucleons
```

A nuclide is written **ᴬ_Z X**, e.g. ²³⁸₉₂U has Z = 92 protons and N = 238 − 92 = 146 neutrons.

| Term | Definition | Example |
| --- | --- | --- |
| **Isotopes** | same Z, different A (same element, different neutron number) | ¹H, ²H, ³H |
| **Isobars** | same A, different Z | ³H and ³He |
| **Isotones** | same N, different Z | ³H (N = 2) and ⁴He (N = 2) |

**Atomic mass unit:**

```
      1 u = 1.66 × 10⁻²⁷ kg  =  1/12 of the mass of a ¹²C atom
      1 u × c² = 931.5 MeV                  so  1 u ≡ 931.5 MeV/c²
```

**Masses to have available:**

```
      m_proton  = 1.00728 u                 m_neutron = 1.00867 u
      m_electron = 0.00055 u                m_H atom  = 1.00783 u
```

### Nuclear size and density

Experiment (electron and neutron scattering) gives

```
      R = R₀ A^(1/3)                        R₀ = 1.2 × 10⁻¹⁵ m = 1.2 fm
```

so the **nuclear radius is proportional to A^(1/3)**, and the **nuclear volume is proportional to A**.

**Nuclear density.**

```
      ρ = mass/volume = (A × 1.66 × 10⁻²⁷) / [ (4/3)π R₀³ A ]
```

The **A cancels**, giving

```
      ρ ≈ 2.3 × 10¹⁷ kg m⁻³            — INDEPENDENT of A
```

> **"Nuclear density is independent of the mass number" is asked directly**, and the reason is exactly
> the cancellation above: mass ∝ A and volume ∝ A, so their ratio is a constant. It also implies
> that **nuclear matter is incompressible** and that nucleons are closely packed in every nucleus.
>
> For scale: nuclear density is about 10¹⁴ times the density of water.

### Nuclear force — characteristics

A standard 2/3-mark question. The nuclear force that binds nucleons has these properties:

1. It is the **strongest** of the known interactions in nature at nuclear distances — far stronger
   than the electrostatic repulsion between protons, which is why nuclei hold together at all.
2. It is **short range** — effective only up to about **2–3 fm**, and essentially zero beyond that.
3. It is **charge independent** — the force between two protons, two neutrons, or a proton and a
   neutron is essentially the same. (So it is not electrical in origin.)
4. It is **attractive** at normal nuclear separations, but becomes strongly **repulsive** at very
   short distances (below about 0.8 fm) — which is why the nucleus does not collapse.
5. It **saturates** — a given nucleon interacts only with its **immediate neighbours**, not with every
   other nucleon in the nucleus. This is why the binding energy per nucleon is roughly constant over
   most of the periodic table.
6. It **depends on spin** — the force between two nucleons depends on the relative orientation of
   their spins.
7. It is **non-central** — it does not act purely along the line joining the two nucleons.

### Mass defect and binding energy

**The observation.** The measured mass of a nucleus is always **less** than the sum of the masses of
its constituent free nucleons. The difference is the **mass defect**:

```
      Δm = [ Z m_p + (A − Z) m_n ] − M_nucleus
```

**Binding energy.** By E = mc², this missing mass corresponds to an energy

```
      BE = Δm c²
```

and with Δm in atomic mass units,

```
      BE (in MeV) = Δm (in u) × 931.5
```

**Physical meaning.** The binding energy is:
- the energy **released** when the free nucleons come together to form the nucleus, **or equivalently**
- the energy that must be **supplied** to break the nucleus completely apart into its free nucleons.

**Binding energy per nucleon:**

```
      BE/A = (Δm c²)/A
```

This is the meaningful measure of nuclear stability — **a larger BE/A means a more stable nucleus**.

> **Careful with the definition of the mass defect** when the problem gives you **atomic** masses
> rather than **nuclear** masses. If atomic masses are given, use Z m_H (hydrogen atoms) rather than
> Z m_p, because the Z electrons are then automatically accounted for. The question will make clear
> which masses it is giving.

### The binding-energy-per-nucleon curve

**You must be able to draw this curve and read conclusions off it.** It is the single most-asked item
in the chapter.

```
  BE/A
  (MeV)
    9 │              ●Fe-56  (~8.8 MeV, the peak)
      │          ╱‾‾‾‾‾‾‾‾‾‾‾‾╲___
    8 │       ╱                    ‾‾‾‾‾‾‾‾‾───────╲  U-238 (~7.6 MeV)
      │     ╱ ●O-16
    7 │    ╱
      │   ╱
    6 │  ╱
      │ │ ●He-4 (7.07)
    5 │ │
      │ │
    2 │ ●H-2 (1.1)
      │
    0 └──┴────┴────┴────┴────┴────┴────┴────┴──── A
       0   20   50   56  100  150  200  238
```

**The features to state:**

1. **It rises steeply** for very light nuclei (A < 20), from about 1.1 MeV for deuterium.
2. **It is roughly constant at about 8 MeV** for the broad range 30 < A < 170.
3. **It peaks at about 8.8 MeV near A = 56** (iron-56) — **the most stable nucleus**.
4. **It falls slowly** for heavy nuclei, reaching about 7.6 MeV at A = 238 (uranium).
5. Certain light nuclei (⁴He, ¹²C, ¹⁶O) sit noticeably **above** the general trend — they are unusually
   stable.

**The three conclusions drawn from the curve** — each is an examinable point:

**(a) The nuclear force is short range and saturated.** BE/A is nearly constant over most of the
curve. If each nucleon interacted with **all** the others, the total BE would grow as A² and BE/A
would grow as A — it does not. So a nucleon interacts only with its **immediate neighbours**.

**(b) Fission of heavy nuclei releases energy.** A heavy nucleus (A ≈ 240, BE/A ≈ 7.6 MeV) splitting
into two medium nuclei (A ≈ 120 each, BE/A ≈ 8.5 MeV) moves the fragments **up** the curve to greater
binding energy per nucleon. The gain of about 0.9 MeV per nucleon, over 240 nucleons, releases about
**200 MeV**.

**(c) Fusion of light nuclei releases energy.** Two very light nuclei fusing move **up** the steep
left-hand part of the curve, where BE/A increases sharply with A. So energy is released, and per
nucleon the gain is much larger than in fission.

**In both cases, energy is released because the products have a higher BE/A than the reactants.** That
sentence is the answer to most "why does X release energy" questions in this chapter.

### Nuclear fission

**Definition.** The splitting of a heavy nucleus into two lighter nuclei of comparable mass, with the
release of a large amount of energy.

**A typical reaction:**

```
      ²³⁵₉₂U + ¹₀n  →  ²³⁶₉₂U*  →  ¹⁴¹₅₆Ba + ⁹²₃₆Kr + 3 ¹₀n + Q          Q ≈ 200 MeV
```

- The energy released per fission is about **200 MeV** (about 0.9 MeV per nucleon).
- The energy appears mainly as the **kinetic energy of the fragments**.
- The reaction releases **2 or 3 neutrons**, which can induce further fissions — a **chain reaction**,
  which is the basis of both nuclear reactors (controlled) and fission weapons (uncontrolled).

**Why energy is released:** the fragments (A ≈ 95 and 140) lie **higher on the BE/A curve** than
uranium, so the total binding energy of the products exceeds that of the reactant, and the difference
is released.

### Nuclear fusion

**Definition.** The combining of two very light nuclei to form a heavier nucleus, with the release of
energy.

**Examples:**

```
      ²₁H + ²₁H  →  ³₂He + ¹₀n + 3.27 MeV
      ²₁H + ³₁H  →  ⁴₂He + ¹₀n + 17.59 MeV
```

**The proton–proton cycle in stars**, net effect:

```
      4 ¹₁H + 2 e⁻  →  ⁴₂He + 2ν + 6γ + 26.7 MeV
```

**Why fusion needs extremely high temperature.** Both nuclei are **positively charged**, so they repel
each other electrostatically. To get within the ~2 fm range of the attractive nuclear force, they
must overcome this **Coulomb barrier**, which requires kinetic energies corresponding to temperatures
of the order of **10⁷–10⁹ K**. This is why fusion is called a **thermonuclear** reaction, and why it
occurs naturally only in stellar interiors.

**Fission vs fusion — the comparison:**

| | **Fission** | **Fusion** |
| --- | --- | --- |
| Process | a heavy nucleus splits | two light nuclei combine |
| Energy per reaction | ~200 MeV | ~17–27 MeV |
| Energy **per nucleon** | ~0.9 MeV | **~3–7 MeV — much greater** |
| Conditions needed | ordinary temperature; a slow neutron | **extremely high** temperature (~10⁷ K) |
| Controllability | can be **controlled** (nuclear reactors) | very difficult to control on Earth |
| Products | radioactive fragments (waste problem) | mostly non-radioactive |
| Occurs naturally in | some heavy nuclei | **stars**, including the Sun |

> **Fusion releases more energy per nucleon than fission**, even though fission releases more per
> reaction — because a fission event involves ~236 nucleons and a fusion event only a handful. This
> distinction is frequently the point of the question.

### Nuclear reactions — the conservation rules

In every nuclear reaction:
- **Charge (Z) is conserved** — the sum of the atomic numbers is the same on both sides.
- **Mass number (A) is conserved** — the sum of the mass numbers is the same on both sides.
- **Energy and momentum are conserved** (with mass–energy taken together).

The **Q value** of a reaction:

```
      Q = ( total mass of reactants − total mass of products ) × c²
```

Q > 0 → energy is **released** (exoergic). Q < 0 → energy must be **supplied** (endoergic).

### Quick recall box

```
A = Z + N ;  ᴬ_Z X
isotopes: same Z | isobars: same A | isotones: same N

1 u = 1.66 × 10⁻²⁷ kg ;   1 u ≡ 931.5 MeV
m_p = 1.00728 u ; m_n = 1.00867 u ; m_H = 1.00783 u

SIZE : R = R₀ A^(1/3) ,  R₀ = 1.2 fm     ⟹  volume ∝ A
DENSITY ρ ≈ 2.3 × 10¹⁷ kg m⁻³ — INDEPENDENT of A (mass ∝ A and volume ∝ A cancel)

NUCLEAR FORCE : strongest at nuclear range | SHORT range (~2–3 fm) |
  CHARGE INDEPENDENT | attractive but repulsive below ~0.8 fm |
  SATURATED (only nearest neighbours) | spin dependent | non-central

MASS DEFECT  Δm = [Z m_p + (A−Z) m_n] − M
  (use Z m_H instead of Z m_p if ATOMIC masses are given)
BINDING ENERGY  BE = Δm c² ;   BE(MeV) = Δm(u) × 931.5
BE/A : larger ⟹ more stable

BE/A CURVE : rises steeply to ~8 MeV by A ≈ 20 ; ~constant 8 MeV for 30 < A < 170 ;
  PEAK ~8.8 MeV at A = 56 (Fe, most stable) ; falls to ~7.6 MeV at A = 238
  conclusions: (a) nuclear force is saturated and short range
               (b) FISSION of heavy nuclei releases energy (products move UP the curve)
               (c) FUSION of light nuclei releases energy (products move UP the curve)

FISSION : ²³⁵U + n → Ba + Kr + 3n + ~200 MeV ; chain reaction possible
FUSION  : ²H + ³H → ⁴He + n + 17.6 MeV ; needs ~10⁷ K to beat the COULOMB BARRIER
  fusion gives MORE energy PER NUCLEON ; fission more per reaction

Q = (mass of reactants − mass of products)c² ;  Q > 0 ⟹ energy released
Z and A are conserved in every nuclear reaction
```

---

## 3. Previous years' questions

**Q1.** *(3 marks)* Draw a graph showing the variation of binding energy per nucleon with mass number.
State any two conclusions that can be drawn from it.

**Q2.** *(3 marks)* Define mass defect and binding energy. Calculate the binding energy per nucleon of
⁴₂He, given m_p = 1.00728 u, m_n = 1.00867 u and M(⁴He nucleus) = 4.00151 u.

**Q3.** *(3 marks)* Show that the density of a nucleus is independent of its mass number.

**Q4.** *(3 marks)* State four characteristics of nuclear forces.

**Q5.** *(3 marks)* Explain, using the binding-energy-per-nucleon curve, why energy is released in
both the fission of a heavy nucleus and the fusion of two light nuclei.

**Q6.** *(2 marks)* Find the radius of a ²⁷₁₃Al nucleus. Take R₀ = 1.2 fm.

**Q7.** *(3 marks)* Distinguish between nuclear fission and nuclear fusion, giving three points of
difference.

**Q8.** *(2 marks)* Why does nuclear fusion require extremely high temperatures?

**Q9.** *(2 marks)* Calculate the energy released in the fusion reaction
²₁H + ³₁H → ⁴₂He + ¹₀n, given the masses 2.014 u, 3.016 u, 4.003 u and 1.009 u respectively.

**Q10.** *(1 mark, MCQ)* The nucleus with the highest binding energy per nucleon is that of
(a) ²³⁸U (b) ⁴He (c) ⁵⁶Fe (d) ²H

**Q11.** *(2 marks)* The ratio of the radii of two nuclei is 1 : 2. What is the ratio of their mass
numbers?

**Q12.** *(4 marks, case study)* Consider the fission reaction
²³⁵₉₂U + ¹₀n → ¹⁴¹₅₆Ba + ⁹²₃₆Kr + x ¹₀n + Q.
(i) Find x.
(ii) Verify that charge and mass number are conserved.
(iii) If Q ≈ 200 MeV, find the energy released per nucleon.
(iv) Why can this reaction sustain a chain reaction?

**Q13.** *(2 marks)* Two nuclei have mass numbers in the ratio 8 : 125. What is the ratio of their
nuclear densities?

---

## 4. Solutions

### Q1 — the binding-energy-per-nucleon curve

```
  BE/A
  (MeV)
    9 │                ●  Fe-56  (~8.8 MeV — the maximum)
      │            ╱‾‾‾‾‾‾‾‾‾‾‾╲____
    8 │        ╱                      ‾‾‾‾‾‾‾‾───────╲ U-238 (~7.6)
      │      ╱  ● O-16
    7 │     ╱
      │    ╱
    6 │   ╱
      │  │ ● He-4 (7.07)
    5 │  │
      │  │
    2 │  ● H-2 (1.1)
      │
    0 └──┴─────┴─────┴─────┴─────┴─────┴─────┴────→ A
       0   20    56    100   150   200   238
```

*(Label both axes — "binding energy per nucleon (MeV)" and "mass number A" — and mark the peak at
A ≈ 56 with value ≈ 8.8 MeV.)*

**Features:** BE/A rises steeply for light nuclei, is roughly **constant at about 8 MeV** over the
broad range 30 < A < 170, reaches a **maximum of about 8.8 MeV at A ≈ 56 (iron)**, and then falls
slowly to about 7.6 MeV at A = 238.

**Two conclusions:**

**1. The nuclear force is short range and saturated.** Over most of the curve BE/A is almost
constant, i.e. the total binding energy is roughly proportional to A. If every nucleon attracted
every other one, the total binding energy would go as A(A − 1)/2 ≈ A², and BE/A would rise linearly
with A. Since it does not, **each nucleon must interact only with its immediate neighbours** — the
nuclear force is short range and saturates.

**2. Both fission of heavy nuclei and fusion of light nuclei release energy.** Nuclei with **higher
BE/A are more stable**. A heavy nucleus (BE/A ≈ 7.6 MeV) splitting into two medium ones
(BE/A ≈ 8.5 MeV) moves **up** the curve; two light nuclei fusing also move **up** the steep left-hand
side. In both cases the products are more tightly bound than the reactants, so the excess energy is
**released**.

*(A third acceptable conclusion: iron-56, at the peak, is the most stable nucleus — which is why it is
the end point of nuclear fusion in stellar cores.)*

### Q2 — mass defect, binding energy, and the BE/A of helium

**Mass defect.** The **mass defect** of a nucleus is the difference between the sum of the masses of
its constituent free nucleons and the actual mass of the nucleus:

```
      Δm = [ Z m_p + (A − Z) m_n ] − M
```

**Binding energy.** The **binding energy** is the energy equivalent of the mass defect, BE = Δm c². It
is the energy released when the free nucleons combine to form the nucleus, and equally the energy
that must be supplied to break the nucleus completely into free nucleons.

**Numerical for ⁴₂He** (Z = 2, A = 4, so 2 protons and 2 neutrons):

```
      Sum of nucleon masses = 2 m_p + 2 m_n
                            = 2(1.00728) + 2(1.00867)
                            = 2.01456 + 2.01734
                            = 4.03190 u

      Mass of nucleus       = 4.00151 u
```

**Mass defect:**

```
      Δm = 4.03190 − 4.00151 = 0.03039 u
```

**Binding energy:**

```
      BE = Δm × 931.5 MeV
         = 0.03039 × 931.5
         = 28.31 MeV
```

**Binding energy per nucleon:**

```
      BE/A = 28.31/4 = 7.08 MeV
```

**BE/A ≈ 7.08 MeV per nucleon.**

*(This agrees with the accepted value of about 7.07 MeV, and you can see on the curve in Q1 that
⁴He sits noticeably above the general trend for such light nuclei — it is an unusually stable
nucleus.)*

### Q3 — nuclear density is independent of A

**Mass of the nucleus.** A nucleus of mass number A contains A nucleons, each of mass approximately
1 u = 1.66 × 10⁻²⁷ kg. So

```
      M ≈ A × 1.66 × 10⁻²⁷ kg                        i.e.  M ∝ A
```

**Volume of the nucleus.** Taking the nucleus as a sphere of radius R = R₀A^(1/3):

```
      V = (4/3)π R³ = (4/3)π (R₀ A^(1/3))³ = (4/3)π R₀³ A          i.e.  V ∝ A
```

**Density:**

```
      ρ = M/V = ( A × 1.66 × 10⁻²⁷ ) / ( (4/3)π R₀³ A )
```

The **A cancels between numerator and denominator**:

```
      ρ = (1.66 × 10⁻²⁷) / ( (4/3)π R₀³ )
```

which contains **no reference to A at all**. So the nuclear density is the **same for all nuclei**. ∎

**Evaluating it**, with R₀ = 1.2 × 10⁻¹⁵ m:

```
      (4/3)π R₀³ = (4/3)(3.1416)(1.2 × 10⁻¹⁵)³
                 = (4.1888)(1.728 × 10⁻⁴⁵)
                 = 7.24 × 10⁻⁴⁵ m³

      ρ = (1.66 × 10⁻²⁷)/(7.24 × 10⁻⁴⁵)
        = 2.3 × 10¹⁷ kg m⁻³
```

**ρ ≈ 2.3 × 10¹⁷ kg m⁻³**, about 10¹⁴ times the density of water.

**What it signifies:** the nucleons are **equally closely packed in every nucleus**, whatever its
size — so nuclear matter is essentially **incompressible**, and this is itself evidence that the
nuclear force **saturates**.

### Q4 — characteristics of nuclear forces

Any four of:

1. **They are the strongest known forces at nuclear range** — much stronger than the electrostatic
   repulsion between protons, which is why nuclei with many protons remain bound.

2. **They are short range.** The nuclear force is effective only up to about **2–3 fm**, and is
   essentially zero beyond that. (This is in sharp contrast to the electrostatic and gravitational
   forces, which are long range.)

3. **They are charge independent.** The nuclear force between two protons, between two neutrons, and
   between a proton and a neutron is essentially the **same**. Hence the force is not electrical in
   origin.

4. **They are attractive at normal nuclear distances but strongly repulsive at very short range** —
   below about 0.8 fm the force becomes repulsive, which prevents the nucleus from collapsing.

5. **They saturate.** A given nucleon interacts only with its **immediate neighbours**, not with every
   other nucleon in the nucleus. This is the reason the binding energy per nucleon is nearly constant
   over most of the periodic table.

6. **They depend on the spin** of the interacting nucleons, and are **non-central** (they do not act
   purely along the line joining the two nucleons).

### Q5 — why both fission and fusion release energy

*Reference the curve from Q1.*

**The governing principle:** a nucleus with a **higher binding energy per nucleon is more tightly
bound and more stable**. In any nuclear process, if the **products have a higher BE/A than the
reactants**, the excess binding energy is **released** as the energy of the reaction.

**Fission of a heavy nucleus.**

Take uranium, A ≈ 235, with BE/A ≈ 7.6 MeV. When it splits into two medium-mass fragments of
A ≈ 120 each, those fragments have BE/A ≈ 8.5 MeV, because they lie in the flat middle region of the
curve, **above** the heavy-nucleus end.

```
      Gain in BE/A ≈ 8.5 − 7.6 = 0.9 MeV per nucleon
      Total energy released ≈ 0.9 × 235 ≈ 200 MeV
```

So the fragments are more tightly bound than the parent, and about 200 MeV is released per fission.

**Fusion of two light nuclei.**

At the light end (A < 20) the curve **rises very steeply**. So combining two very light nuclei
produces a nucleus much further **up** the curve. For instance, deuterium has BE/A ≈ 1.1 MeV while
helium-4 has BE/A ≈ 7.07 MeV — a gain of nearly **6 MeV per nucleon**.

So the product is far more tightly bound than the reactants, and energy is released.

**The unifying statement:** in both processes the products lie **closer to the peak of the curve
(A ≈ 56)** than the reactants do. Fission moves *down* in A towards the peak from the right; fusion
moves *up* in A towards the peak from the left. **Every energy-releasing nuclear process moves the
system towards A ≈ 56.**

*(And note the per-nucleon comparison: fusion's gain of ~6 MeV per nucleon far exceeds fission's
~0.9 MeV, which is why fusion is a much richer energy source per unit mass — even though a single
fission event releases more total energy.)*

### Q6 — radius of an aluminium nucleus

```
      A = 27                R₀ = 1.2 fm = 1.2 × 10⁻¹⁵ m
```

```
      R = R₀ A^(1/3)
        = (1.2 × 10⁻¹⁵) × 27^(1/3)
        = (1.2 × 10⁻¹⁵) × 3                    (since 27^(1/3) = 3)
        = 3.6 × 10⁻¹⁵ m
```

**R = 3.6 × 10⁻¹⁵ m = 3.6 fm**

### Q7 — fission vs fusion

| | **Nuclear fission** | **Nuclear fusion** |
| --- | --- | --- |
| **Process** | a **heavy** nucleus **splits** into two lighter nuclei of comparable mass | two **light** nuclei **combine** to form a heavier nucleus |
| **Energy released per nucleon** | about **0.9 MeV** | about **3–7 MeV** — much greater |
| **Conditions required** | occurs at ordinary temperature, initiated by a slow neutron | requires **extremely high temperature** (~10⁷ K) to overcome the Coulomb repulsion |
| **Controllability** | can be **controlled**, as in a nuclear reactor | extremely difficult to control on Earth |
| **Products** | radioactive fragments, giving a waste-disposal problem | mostly non-radioactive |

*(Any three rows is a full 3-mark answer. Note that each row compares the **same** attribute on both
sides.)*

### Q8 — why fusion needs very high temperatures

For two nuclei to fuse, they must come within about **2 fm** of each other — the range of the
attractive **nuclear force**.

But both nuclei are **positively charged**, so as they approach they experience a strong
**electrostatic repulsion** that grows as 1/r². This repulsion constitutes a **Coulomb potential
barrier** of the order of several hundred keV, which the nuclei must **overcome** by their kinetic
energy of approach.

The only practical way to give a large number of nuclei such kinetic energies is to raise the
temperature enormously, since the average kinetic energy of a particle is of order kT. Requiring
kinetic energies of hundreds of keV implies temperatures of the order of **10⁷ to 10⁹ K**.

This is why fusion is called a **thermonuclear** reaction, and why it occurs naturally only in
**stellar interiors**, where such temperatures and pressures exist.

### Q9 — energy released in a fusion reaction

```
      ²₁H + ³₁H  →  ⁴₂He + ¹₀n
```

```
      Mass of reactants = 2.014 + 3.016 = 5.030 u
      Mass of products  = 4.003 + 1.009 = 5.012 u
```

**Mass difference (the Q value in mass units):**

```
      Δm = 5.030 − 5.012 = 0.018 u
```

**Energy released:**

```
      Q = Δm × 931.5 MeV
        = 0.018 × 931.5
        = 16.77 MeV
```

**Q ≈ 16.8 MeV**

The mass of the products is **less** than that of the reactants, so Δm > 0 and energy is **released**
— the reaction is exoergic.

### Q10 — highest binding energy per nucleon

From the BE/A curve, the maximum lies at A ≈ 56, which is iron-56 (BE/A ≈ 8.8 MeV).

**Answer: (c) ⁵⁶Fe**

*(For comparison: ⁴He ≈ 7.07 MeV, ²³⁸U ≈ 7.6 MeV, ²H ≈ 1.1 MeV.)*

### Q11 — ratio of mass numbers from the ratio of radii

```
      R = R₀ A^(1/3)                ⟹      R ∝ A^(1/3)
```

So

```
      R₁/R₂ = (A₁/A₂)^(1/3)
⟹     A₁/A₂ = (R₁/R₂)³
```

With R₁ : R₂ = 1 : 2:

```
      A₁/A₂ = (1/2)³ = 1/8
```

**The ratio of the mass numbers is 1 : 8.**

### Q12 — case study: the fission of uranium-235

```
      ²³⁵₉₂U + ¹₀n  →  ¹⁴¹₅₆Ba + ⁹²₃₆Kr + x ¹₀n + Q
```

**(i) Find x.** Use conservation of **mass number**:

```
      LHS:  235 + 1 = 236
      RHS:  141 + 92 + x(1) = 233 + x

      236 = 233 + x
⟹     x = 3
```

**x = 3** — three neutrons are released.

**(ii) Verify conservation of charge and mass number.**

**Charge (atomic number Z):**

```
      LHS:  92 + 0 = 92
      RHS:  56 + 36 + 3(0) = 92          ✓
```

**Mass number (A):**

```
      LHS:  235 + 1 = 236
      RHS:  141 + 92 + 3(1) = 236        ✓
```

Both are conserved, as they must be in any nuclear reaction.

**(iii) Energy released per nucleon.**

The total number of nucleons involved is 236 (from ²³⁵U plus the incident neutron):

```
      Energy per nucleon = Q/236 = 200/236 = 0.847 MeV
```

**≈ 0.85 MeV per nucleon**

*(Consistent with the BE/A curve: uranium sits at about 7.6 MeV and the fragments at about 8.5 MeV,
a difference of roughly 0.9 MeV per nucleon ✓)*

**(iv) Why a chain reaction is possible.**

The reaction is initiated by **one** neutron but releases **three** neutrons. Each of those neutrons
can, if suitably slowed (moderated) and if it strikes another ²³⁵U nucleus rather than escaping or
being absorbed, **induce a further fission**, which in turn releases three more neutrons.

The number of fissions can therefore **multiply from one generation to the next** — a self-sustaining
**chain reaction**. If the multiplication is held at exactly one fission per fission (by absorbing
the surplus neutrons with control rods), the reaction is **controlled**, as in a nuclear reactor. If
it is allowed to grow, the release becomes explosive.

### Q13 — ratio of nuclear densities

**The nuclear density is independent of the mass number** (as shown in Q3), because the mass is
proportional to A and the volume is also proportional to A, so their ratio is a constant.

Therefore, whatever the mass numbers,

```
      ρ₁ : ρ₂ = 1 : 1
```

**The ratio of the nuclear densities is 1 : 1** — they are equal.

*(The 8 : 125 ratio of mass numbers is a distractor. It would matter for the ratio of **radii**, which
would be (8/125)^(1/3) = 2 : 5.)*

---

## 5. Test yourself

Time: 35 minutes. Answers below.

1. *(1)* 1 u is equivalent to
   (a) 931.5 MeV (b) 1.6 × 10⁻¹⁹ J (c) 13.6 eV (d) 200 MeV
2. *(1)* The nuclear radius is proportional to
   (a) A (b) A^(1/3) (c) A² (d) A^(1/2)
3. *(1)* Nuclear density
   (a) increases with A (b) decreases with A (c) is independent of A (d) is zero
4. *(2)* Define binding energy per nucleon. Why is it a better measure of nuclear stability than the
   total binding energy?
5. *(2)* ³H and ³He — are these isotopes, isobars or isotones? Justify.
6. *(2)* Find the radius of a ⁶⁴₂₉Cu nucleus. (R₀ = 1.2 fm)
7. *(2)* Why is the nuclear force said to be charge independent?
8. *(3)* Find the binding energy of ⁷₃Li, given m_p = 1.00783 u (hydrogen atom), m_n = 1.00867 u and
   the atomic mass of ⁷Li = 7.01600 u.
9. *(3)* Draw the BE/A curve and use it to explain why very heavy nuclei are unstable.
10. *(3)* Distinguish between nuclear fission and fusion, giving three differences.
11. *(2)* Complete and balance: ²³⁸₉₂U → ²³⁴₉₀Th + ?
12. *(2)* Calculate the energy released when four hydrogen nuclei fuse to form one helium nucleus,
    given the mass of ¹H = 1.00783 u and of ⁴He = 4.00260 u. (Ignore the electrons.)
13. *(2)* Two nuclei have radii in the ratio 3 : 5. Find the ratio of their mass numbers and of their
    nuclear densities.

### Answer key

**1. (a) 931.5 MeV.**

**2. (b) A^(1/3).**

**3. (c) is independent of A.**

**4.** The **binding energy per nucleon** is the total binding energy of a nucleus divided by its mass
number, BE/A. It is a better measure of stability than the total binding energy because the total BE
naturally grows with the number of nucleons — a heavy nucleus has a large total BE simply because it
has more nucleons. Dividing by A gives the **average binding energy holding each nucleon**, which
allows nuclei of different sizes to be **compared** on the same footing. The nucleus with the largest
BE/A is the most stable.

**5. Isobars.** They have the **same mass number** (A = 3) but different atomic numbers (Z = 1 for
³H and Z = 2 for ³He). Nuclides with the same A and different Z are **isobars**.
*(They are not isotones either: ³H has N = 2 while ³He has N = 1.)*

**6. 4.8 fm.** R = R₀A^(1/3) = 1.2 × 64^(1/3) = 1.2 × 4 = **4.8 fm = 4.8 × 10⁻¹⁵ m**.

**7.** Experiments show that the nuclear force between **two protons**, between **two neutrons**, and
between **a proton and a neutron** is essentially the **same** in magnitude. Since protons carry
charge and neutrons do not, a force that is unaffected by this difference cannot depend on charge —
it is therefore said to be **charge independent**, and cannot be electrical in origin.

**8. 39.2 MeV.** Since **atomic** masses are given (via m_H), use Z hydrogen atoms:
Sum = 3(1.00783) + 4(1.00867) = 3.02349 + 4.03468 = 7.05817 u.
Δm = 7.05817 − 7.01600 = 0.04217 u.
BE = 0.04217 × 931.5 = **39.28 MeV** (so BE/A = 39.28/7 = 5.61 MeV).

**9.** Curve as in §4 Q1. From the curve, BE/A **falls** for A above about 56, reaching only ~7.6 MeV
at A = 238. So heavy nuclei are **less tightly bound per nucleon** than medium-mass nuclei. The
physical reason is that the **long-range Coulomb repulsion** between the many protons grows as Z²
and acts across the whole nucleus, whereas the **short-range attractive nuclear force saturates** and
acts only between neighbours. As A increases, the repulsion grows faster than the attraction can
compensate. A heavy nucleus can therefore **increase** its binding energy per nucleon by splitting
into two medium-mass fragments — which is why such nuclei are unstable and undergo fission.

**10.** Any three rows from the table in §4 Q7.

**11. ⁴₂He (an alpha particle).**
Mass number: 238 = 234 + A, so A = 4. Charge: 92 = 90 + Z, so Z = 2. Hence the particle is ⁴₂He.
*(The decay process itself is out of syllabus; only the balancing of A and Z is required.)*

**12. 26.7 MeV.**
Mass of reactants = 4 × 1.00783 = 4.03132 u. Mass of product = 4.00260 u.
Δm = 4.03132 − 4.00260 = 0.02872 u.
Q = 0.02872 × 931.5 = **26.75 MeV** — the energy released in the proton–proton cycle that powers the
Sun.

**13. Mass numbers 27 : 125; densities 1 : 1.**
Since R ∝ A^(1/3), A₁/A₂ = (R₁/R₂)³ = (3/5)³ = 27/125.
Nuclear density is independent of A, so the densities are **equal**, 1 : 1.

**Scoring.** Out of 26. Below 18 → the BE/A curve is the whole chapter. Draw it with the axes labelled
and the Fe-56 peak marked, and write out the three conclusions from memory.

---

## 6. Answering tips

**On the BE/A curve**

1. **Label both axes** — "binding energy per nucleon (MeV)" and "mass number A". An unlabelled graph
   loses most of the mark.

2. **Mark the peak at A ≈ 56 with the value ≈ 8.8 MeV**, and mark the ~7.6 MeV value at A = 238. Those
   two numbers are what the conclusions are built from.

3. **State the conclusions as reasoned statements, not observations.** "BE/A is nearly constant,
   therefore each nucleon interacts only with its neighbours, therefore the nuclear force saturates" —
   the chain of reasoning is the mark.

4. **The unifying answer to "why is energy released":** the products have a **higher BE/A** than the
   reactants, i.e. they lie **closer to the peak** of the curve. Say it in those words.

**On mass-defect numericals**

5. **Check whether you are given nuclear or atomic masses.** If atomic (or if m_H = 1.00783 u is
   given rather than m_p = 1.00728 u), use **Z m_H**, which accounts for the electrons automatically.
   Mixing them up gives an answer wrong by about Z × 0.00055 u.

6. **Keep five decimal places in u throughout**, and only round at the end. The mass defect is a small
   difference between two nearly equal numbers, so early rounding destroys the answer.

7. **Use 1 u = 931.5 MeV.** BE in MeV = Δm in u × 931.5. There is no need to convert to kilograms and
   joules unless the question asks for joules.

8. **Distinguish BE from BE/A.** If the question asks for the binding energy per nucleon, remember to
   divide by A. This is a routine dropped mark.

**On sizes and densities**

9. **R ∝ A^(1/3), so A ∝ R³.** For ratio questions, cube or cube-root as appropriate, and say which
   you are doing.

10. **"Nuclear density is independent of A" is the answer to any density-ratio question** — the ratio
    is always 1 : 1. And be ready to *prove* it: mass ∝ A, volume ∝ A, so the A cancels.

**On descriptive questions**

11. **For nuclear-force characteristics, give four distinct properties with a word of explanation
    each.** "Short range — effective only up to about 2–3 fm" scores; "short range" alone often does
    not.

12. **For fission vs fusion, use a table with parallel rows**, and include the **per-nucleon** energy
    comparison — that is the distinction most questions are really after.

13. **For nuclear reactions, balance A and Z explicitly as two separate lines.** It is the whole
    method, and it is worth the marks even when the identity of the missing particle is obvious.

14. **Do not write anything about half-life, decay constant, or alpha/beta/gamma decay properties.**
    That material is deleted, and time spent on it is wasted. Balancing a reaction's A and Z is still
    fair game; the decay law is not.
