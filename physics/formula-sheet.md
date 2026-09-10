# Physics (042) — Complete Formula Sheet

Everything in the current syllabus, chapter by chapter. **Deleted topics are not here** — if a
formula you half-remember is missing, check
[`../docs/00-exam-blueprint.md`](../docs/00-exam-blueprint.md) §3 before hunting for it; it is
probably out of syllabus.

Use this for the daily 20-minute revision in February, and read it once on the morning of the exam.

---

## Constants

```
c   = 3 × 10⁸ m s⁻¹                     speed of light in vacuum
e   = 1.6 × 10⁻¹⁹ C                     elementary charge
h   = 6.63 × 10⁻³⁴ J s                  Planck's constant
m_e = 9.1 × 10⁻³¹ kg                    electron mass
ε₀  = 8.854 × 10⁻¹² C² N⁻¹ m⁻²          permittivity of vacuum
μ₀  = 4π × 10⁻⁷ T m A⁻¹                 permeability of vacuum
R   = 1.097 × 10⁷ m⁻¹                   Rydberg constant
R₀  = 1.2 × 10⁻¹⁵ m                     nuclear radius constant
1 u = 1.66 × 10⁻²⁷ kg  ≡  931.5 MeV
D   = 25 cm                             least distance of distinct vision

WORKING SHORTCUTS — memorise these, they save real time
  k = 1/4πε₀   = 9 × 10⁹ N m² C⁻²
  1/2πε₀       = 1.8 × 10¹⁰
  μ₀/4π        = 10⁻⁷ ;   μ₀/2π = 2 × 10⁻⁷
  hc           = 1240 eV nm         →  E(eV) = 1240/λ(nm)
  h/e          = 4.14 × 10⁻¹⁵ V s
  λ(electron)  = 12.27/√V  Å        (V in volts)
  E_n(hydrogen) = −13.6/n² eV ;  r_n = 0.53 n² Å
```

---

## Ch 1 — Electric Charges and Fields

```
q = ne ;  e = 1.6 × 10⁻¹⁹ C

COULOMB : F = k q₁q₂/r²           F_medium = F_vacuum/K
FIELD   : E = F/q₀ = k q/r²       unit N C⁻¹ = V m⁻¹

DIPOLE  : p = q(2a), directed from −q to +q      unit C m
  axial      : E = 2kpr/(r² − a²)²      → r >> a :  E = 2kp/r³   (along p)
  equatorial : E = kp/(r² + a²)^(3/2)   → r >> a :  E = kp/r³    (antiparallel to p)
  axial = 2 × equatorial ;  dipole field ∝ 1/r³
  torque τ = pE sin θ = p × E ;  NET FORCE = 0 in a uniform field
  τ max at θ = 90° ;  stable at θ = 0°, unstable at 180°

FLUX  : φ = ∮E·dA = EA cos θ      unit N m² C⁻¹ = V m
GAUSS : φ = q_enclosed/ε₀
  independent of the surface's shape and size; external charges give ZERO net flux

  infinite straight wire  : E = λ/(2πε₀ r)        ∝ 1/r
  infinite plane sheet    : E = σ/(2ε₀)           independent of distance
  charged spherical shell : outside E = kq/r² ;  INSIDE E = 0 ;  at surface σ/ε₀
  charge at the centre of a cube: total flux q/ε₀ ;  through one face q/6ε₀

CONDUCTOR (electrostatic equilibrium): E = 0 inside ; charge on the outer surface ;
  E ⊥ to the surface just outside, magnitude σ/ε₀ ; whole conductor at one potential
```

## Ch 2 — Electrostatic Potential and Capacitance

```
V = W/q  (volt = J C⁻¹) ;  V = kq/r  — a SCALAR, sign carried ;  V ∝ 1/r
System of charges : V = Σ kqᵢ/rᵢ                (algebraic sum)
Dipole : V = kp cos θ/r² ;  axial ±kp/r² ;  EQUATORIAL V = 0 ;  V ∝ 1/r²
E = −dV/dr ;  uniform field between plates E = V/d

EQUIPOTENTIAL SURFACE: no work done along it ; E ⊥ to it everywhere ;
  never intersect ; closer together where E is stronger ;
  spheres for a point charge, parallel planes for a uniform field

POTENTIAL ENERGY
  two charges   : U = k q₁q₂/r                  (sign carried; negative ⟹ bound)
  three charges : U = k[q₁q₂/r₁₂ + q₂q₃/r₂₃ + q₁q₃/r₁₃]
  dipole in E   : U = −pE cos θ = −p·E ;  min −pE at θ = 0° (stable)
  work to rotate: W = pE(cos θ₁ − cos θ₂)

CAPACITANCE  C = Q/V   (farad = C V⁻¹)
  parallel plate      : C = ε₀A/d ;  with dielectric C = Kε₀A/d
  slab of thickness t : C = ε₀A/(d − t + t/K)
  series   : 1/C = Σ 1/Cᵢ      (C smaller than the smallest)
  parallel : C = Σ Cᵢ          (C larger than the largest)
  — the OPPOSITE way round from resistors

  U = ½CV² = ½QV = Q²/2C ;   energy density u = ½ε₀E²
  net field in a dielectric : E = E₀/K

DIELECTRIC INSERTED
  battery CONNECTED    (V fixed): C ↑K ,  Q ↑K ,  E same ,  U ↑K
  battery DISCONNECTED (Q fixed): C ↑K ,  V ↓K ,  E ↓K   ,  U ↓K

Two capacitors joined : V = (C₁V₁ + C₂V₂)/(C₁ + C₂)
  energy lost ΔU = C₁C₂(V₁ − V₂)²/[2(C₁ + C₂)]   ≥ 0 always
```

## Ch 3 — Current Electricity

```
I = q/t = dq/dt  (ampere) ;  conventional current opposite to the electron drift

v_d = eEτ/m  (~10⁻⁴ m s⁻¹) ;   I = n e A v_d
  R = ml/(ne²Aτ) ;   ρ = m/(ne²τ)
J = I/A = n e v_d = σE   (a VECTOR) ;  μ = v_d/E = eτ/m ;  σ = neμ = 1/ρ

R = ρl/A ;  wire stretched to n times its length → R becomes n²R
ρ_T = ρ₀[1 + α(T − T₀)]
  metals: α > 0, ρ ↑ (τ falls, n fixed)
  semiconductors: α < 0, ρ ↓ (n rises sharply)

CELL : ε = I(R + r) ;  V = ε − Ir (discharging) ;  V = ε + Ir (charging) ;  V = ε at I = 0
  V–I graph of a cell: intercept = ε , |slope| = r ;  short-circuit I = ε/r
  series   : ε_eq = Σεᵢ ,  r_eq = Σrᵢ
  parallel : ε_eq = (ε₁r₂ + ε₂r₁)/(r₁ + r₂) ,  r_eq = r₁r₂/(r₁ + r₂)

KIRCHHOFF : junction rule ΣI = 0  → conservation of CHARGE
            loop rule ΣΔV = 0     → conservation of ENERGY

WHEATSTONE (balanced, I_g = 0) : P/Q = R/S           — a NULL method
METRE BRIDGE : R = S · l/(100 − l)

P = VI = I²R = V²/R ;  maximum power to an external R when R = r
1 kWh = 3.6 × 10⁶ J
```

## Ch 4 — Moving Charges and Magnetism

```
BIOT–SAVART : dB = (μ₀/4π) I dl sin θ/r² ;   vector (μ₀/4π) I (dl × r̂)/r²
  circular loop, on the axis : B = μ₀NIR²/[2(R² + x²)^(3/2)]
  at the centre              : B = μ₀NI/(2R)
  arc subtending θ (radians) : B = μ₀Iθ/(4πR)

AMPERE : ∮B·dl = μ₀ I_enclosed
  long straight wire : B = μ₀I/(2πr)   ∝ 1/r, concentric circular field lines
  long solenoid      : B = μ₀nI inside ;  μ₀nI/2 at an end ;  ≈ 0 outside

MOVING CHARGE : F = q(v × B) = qvB sin θ
  F ⊥ v always ⟹ NO WORK done ; speed and kinetic energy unchanged
  v ⊥ B : r = mv/(qB) ;  T = 2πm/(qB) ;  f = qB/(2πm)   — T independent of v
  v at an angle to B → HELICAL path
  Lorentz : F = q(E + v × B) ;  velocity selector v = E/B

CONDUCTOR : F = I(l × B) = BIl sin θ            (Fleming's left-hand rule)

PARALLEL WIRES : F/l = μ₀I₁I₂/(2πd)
  same direction → ATTRACT ;  opposite → REPEL
  ampere: 2 × 10⁻⁷ N m⁻¹ between wires 1 m apart each carrying 1 A

CURRENT LOOP : m = NIA  (A m²) ;  τ = NIAB sin θ = m × B ;  net force = 0
  τ maximum when the PLANE of the coil is PARALLEL to B

GALVANOMETER : NIAB = kφ ⟹ φ ∝ I ;  radial field keeps sin θ = 1 (uniform scale)
  current sensitivity I_s = NAB/k
  voltage sensitivity V_s = NAB/(kG) = I_s/G
  → AMMETER   : shunt in PARALLEL,  S = I_g G/(I − I_g) ;  ideal R = 0, in series
  → VOLTMETER : resistance in SERIES, R = V/I_g − G ;      ideal R = ∞, in parallel
```

## Ch 5 — Magnetism and Matter

```
FIELD LINES: continuous CLOSED loops ; N→S outside, S→N inside ; never intersect
∮B·dA = 0  ⟹  NO MAGNETIC MONOPOLES      (contrast ∮E·dA = q/ε₀)

BAR MAGNET ≡ SOLENOID :  m = NIA (solenoid) ;  m = q_m × 2l (bar magnet), S → N inside
  cutting a magnet gives TWO complete magnets — an isolated pole is impossible
  cut ⊥ to the length: q_m unchanged, length halved ⟹ m halved

DIPOLE IN A FIELD : τ = mB sin θ = m × B ;  net force = 0 in a uniform field
  U = −mB cos θ = −m·B ;  stable at θ = 0°, unstable at 180°
  W(θ₁ → θ₂) = mB(cos θ₁ − cos θ₂)

EARTH'S MAGNETIC ELEMENTS : declination, dip (δ), horizontal component B_H
  B_H = B cos δ        B_V = B sin δ        B_V = B_H tan δ
  tan δ = B_V/B_H      B = √(B_H² + B_V²)
  magnetic equator: δ = 0°, B = B_H     magnetic poles: δ = 90°, B = B_V
  Earth's magnetic SOUTH pole is near the geographic NORTH

MATERIALS (qualitative only)
  dia   — weakly REPELLED ; no net atomic moment ; e.g. bismuth, copper
  para  — weakly ATTRACTED ; random permanent moments ; T-dependent ; e.g. aluminium
  ferro — STRONGLY attracted ; domains ; lost above the CURIE temperature ; e.g. iron

(χ, μ_r, M, H and hysteresis are OUT of syllabus — do not use them in answers)
```

## Ch 6 — Electromagnetic Induction

```
FLUX : φ = BA cos θ  (weber = T m²) ;  flux linkage = Nφ
FARADAY : ε = −N dφ/dt ;  I = ε/R
  charge q = NΔφ/R      — depends only on the TOTAL flux change, not on the time taken

LENZ : the induced current OPPOSES the change in flux
  — the minus sign in Faraday's law
  — a consequence of CONSERVATION OF ENERGY

MOTIONAL EMF : ε = Blv
  I = Blv/R ;  F = B²l²v/R ;  P_mech = P_elec = B²l²v²/R
  rod rotating about one end : ε = ½Bωl²

EDDY CURRENTS : induced loops within the bulk of a conductor
  minimised by a LAMINATED core
  uses: electromagnetic braking, induction furnace, induction motor, energy meters

SELF-INDUCTANCE : φ = LI ;  ε = −L dI/dt ;  unit HENRY
  long solenoid : L = μ₀n²Al = μ₀N²A/l   (× μ_r with a core)
  energy stored : U = ½LI²
  L ∝ N² ;  independent of the current

MUTUAL INDUCTANCE : φ₂ = MI₁ ;  ε₂ = −M dI₁/dt ;  M₁₂ = M₂₁ (reciprocity)
  two coaxial solenoids : M = μ₀n₁n₂Al = μ₀N₁N₂A/l
  M = k√(L₁L₂) ;  maximum when coaxial and close ;  ZERO when the axes are ⊥

AC GENERATOR : Nφ = NBA cos ωt  ⟹  ε = NBAω sin ωt = ε₀ sin ωt ,  ε₀ = NBAω
  emf MAXIMUM when the coil's PLANE is PARALLEL to B ;  zero when perpendicular
  SLIP RINGS (not a commutator) give the alternating output
```

## Ch 7 — Alternating Current

```
i = i₀ sin ωt ;  ω = 2πf
mean over a full cycle = 0 ;  over a half cycle = 2i₀/π = 0.637 i₀
RMS : i_rms = i₀/√2 = 0.707 i₀ ;  v_rms = v₀/√2
  — the DC that gives the SAME HEATING ; AC meters read rms
  220 V mains → peak = 220√2 ≈ 311 V

SINGLE ELEMENTS
  R : V and I IN PHASE
  L : I LAGS V by π/2 ;  X_L = ωL = 2πfL      ∝ f    (blocks high f, passes DC)
  C : I LEADS V by π/2 ;  X_C = 1/ωC = 1/2πfC ∝ 1/f  (passes high f, BLOCKS DC)
  "CIVIL": in C, I leads V ;  V leads I in L
  average power in a pure L or a pure C = ZERO

SERIES LCR (phasors)
  Z = √(R² + (X_L − X_C)²)      tan φ = (X_L − X_C)/R      cos φ = R/Z
  X_L > X_C → inductive, V leads I ;  X_L < X_C → capacitive, V lags I

RESONANCE : X_L = X_C
  ω₀ = 1/√(LC) ;  f₀ = 1/(2π√(LC))
  Z MINIMUM = R ;  I MAXIMUM = V/R ;  φ = 0 ;  power factor = 1
  Q = ω₀L/R = 1/(ω₀CR) = (1/R)√(L/C) = ω₀/Δω ,  bandwidth Δω = R/L
  small R → sharp resonance, high Q, more selective   (an "acceptor" circuit)

POWER : P_avg = V_rms I_rms cos φ ;   power factor cos φ = R/Z
  wattless current = i_rms sin φ  (consumes no average power)

TRANSFORMER (mutual induction)
  V_s/V_p = N_s/N_p = I_p/I_s
  step-up: N_s > N_p, V↑ I↓ ;  step-down: N_s < N_p, V↓ I↑ ;  power (ideally) unchanged
  losses → remedies: copper → thick wire ; eddy → laminated core ;
    hysteresis → soft iron ; flux leakage → closed core, coils wound over each other
  will NOT work on DC (dφ/dt = 0)
  transmission at high V and low I, because the line loss is I²R
```

## Ch 8 — Electromagnetic Waves

```
DISPLACEMENT CURRENT : I_d = ε₀ dφ_E/dt
  needed because Ampere's law is INCONSISTENT for a charging capacitor
  Ampere–Maxwell : ∮B·dl = μ₀(I_c + ε₀ dφ_E/dt)
  ⟹ a CHANGING ELECTRIC FIELD produces a MAGNETIC FIELD

EM WAVE PROPERTIES
  transverse ;  E ⊥ B ⊥ direction of propagation (direction along E × B)
  need NO medium ;  c = 1/√(μ₀ε₀) = 3 × 10⁸ m s⁻¹ ;  c = E₀/B₀
  E and B oscillate IN PHASE ;  not deflected by E or B fields (no charge)
  carry energy AND momentum → radiation pressure
  energy shared EQUALLY between the E and B fields:  u_E = ½ε₀E² , u_B = B²/2μ₀
  produced by ACCELERATING charges
  in a medium : v = c/n ,  λ → λ/n ,  FREQUENCY UNCHANGED

c = νλ ;   E_photon = hν = hc/λ ;   ω = 2πν ,  k = 2π/λ ,  c = ω/k

SPECTRUM (increasing frequency, decreasing wavelength):
  RADIO → MICROWAVE → INFRARED → VISIBLE → ULTRAVIOLET → X-RAY → GAMMA
  "Roman Men Invented Very Unusual X-ray Guns"
  visible: violet ≈ 400 nm (highest f)  …  red ≈ 700 nm (lowest f)
  radar → microwaves | remote controls → infrared | sterilising → UV
  bone imaging → X-rays | radiotherapy → gamma
```

## Ch 9 — Ray Optics and Optical Instruments

```
SIGN CONVENTION: distances from the pole/optical centre; incident light left→right positive
  u always negative for a real object
  MIRROR : concave f = − , convex f = +      LENS : convex f = + , concave f = −

MIRROR : 1/v + 1/u = 1/f ,  f = R/2 ,  m = −v/u
LENS   : 1/v − 1/u = 1/f ,               m = +v/u      ← note the sign difference
  lens maker's : 1/f = (n − 1)(1/R₁ − 1/R₂)
  in a medium  : 1/f = (n/n_m − 1)(1/R₁ − 1/R₂)
    n_m = n → f = ∞, the lens disappears ;  n_m > n → a convex lens DIVERGES
  refraction at a spherical surface : n₂/v − n₁/u = (n₂ − n₁)/R
  P = 1/f (m) = 100/f (cm) , in dioptres ; convex P > 0, concave P < 0
  in contact : 1/F = 1/f₁ + 1/f₂ ,  P = P₁ + P₂ ,  m = m₁m₂

SNELL : n₂₁ = sin i/sin r = n₂/n₁ = v₁/v₂ = λ₁/λ₂ ;   n = c/v
  frequency UNCHANGED on refraction
  apparent depth : n = real depth/apparent depth ;  normal shift = h(1 − 1/n)

TIR : denser → rarer, AND i > C ;   sin C = 1/n
  larger n → smaller C  (diamond n = 2.42, C ≈ 24° ;  glass n = 1.5, C ≈ 42°)
  uses: optical fibre, totally reflecting prism, mirage, diamond's sparkle

PRISM : r₁ + r₂ = A ;   i + e = A + δ
  at minimum deviation: i = e , r₁ = r₂ = A/2 , i = (A + δm)/2
  n = sin[(A + δm)/2] / sin(A/2)
  thin prism : δ = (n − 1)A

COMPOUND MICROSCOPE (both f short, f_o the shorter)
  near point : m = (v_o/u_o)(1 + D/f_e)     infinity : m = (v_o/u_o)(D/f_e)
  long tube  : m ≈ (L/f_o)(D/f_e)

ASTRONOMICAL TELESCOPE (f_o large, f_e small, large aperture)
  normal adjustment : m = f_o/f_e ,  tube length L = f_o + f_e
  near point        : m = (f_o/f_e)(1 + f_e/D)
  reflecting telescope advantages: no chromatic aberration, less spherical
    aberration, brighter and higher resolution, mechanically stable, cheaper

D = 25 cm (least distance of distinct vision)
```

## Ch 10 — Wave Optics

```
WAVEFRONT: locus of points in the SAME PHASE ;  a ray is ⊥ to the wavefront
  spherical (point source) | cylindrical (slit) | plane (distant source)

HUYGENS: every point on a wavefront is a source of secondary wavelets ;
  the new wavefront is the FORWARD ENVELOPE of those wavelets
  reflection : BC = AD = ct , triangles congruent (RHS) ⟹ i = r
  refraction : BC = v₁t , AD = v₂t ⟹ sin i/sin r = v₁/v₂ = n₂/n₁

INTERFERENCE
  constructive : path diff = nλ        , phase diff = 2nπ
  destructive  : path diff = (2n−1)λ/2 , phase diff = (2n−1)π
  phase difference = (2π/λ) × path difference
  I = I₁ + I₂ + 2√(I₁I₂) cos φ
  I_max = (√I₁ + √I₂)² ;  I_min = (√I₁ − √I₂)²
  I_max/I_min = (a₁ + a₂)²/(a₁ − a₂)²

COHERENT SOURCES: same frequency, CONSTANT phase difference
  two independent lamps cannot interfere — their phase difference varies randomly
  hence YDSE derives both beams from ONE source

YDSE : path difference = yd/D
  bright : y = nλD/d          dark : y = (2n − 1)λD/2d
  FRINGE WIDTH  β = λD/d ;   angular width = λ/d
  λ↑ → β↑ ;  D↑ → β↑ ;  d↑ → β↓ ;  immersed in a liquid of index n → β/n
  one slit covered → interference disappears, only diffraction remains
  white light → central fringe WHITE, then a few coloured fringes (violet innermost)

SINGLE-SLIT DIFFRACTION
  minima : a sin θ = nλ   (n = ±1, ±2, … ;  n ≠ 0)
  secondary maxima : a sin θ = (2n + 1)λ/2
  central maximum: angular half-width λ/a ;  FULL angular width 2λ/a
  linear width on a screen at distance D = 2λD/a
  narrower slit or longer λ → WIDER central maximum

INTERFERENCE vs DIFFRACTION
  two sources vs one wavefront | equal vs unequal fringe widths |
  equal vs rapidly falling intensity | perfectly dark vs not perfectly dark minima

POLARISATION (low priority — verify the scope for your year)
  proves light is TRANSVERSE ; crossed Polaroids transmit nothing
  Malus : I = I₀ cos²θ ;   Brewster : tan θ_p = n
```

## Ch 11 — Dual Nature of Radiation and Matter

```
φ₀ = work function = hν₀ = hc/λ₀        (a property of the METAL)
V₀ = stopping potential ;   eV₀ = K_max
saturation current depends on the INTENSITY

EINSTEIN : hν = φ₀ + K_max = φ₀ + eV₀
           K_max = h(ν − ν₀)
           V₀ = (h/e)ν − φ₀/e

FOUR LAWS: current ∝ intensity | K_max depends only on ν |
           a threshold ν₀ exists | emission is instantaneous (<10⁻⁹ s)

WAVE THEORY FAILS on all three: K_max should depend on intensity (it doesn't) ;
  there should be no threshold (there is) ; there should be a time lag (there isn't)

GRAPHS
  I vs V, different INTENSITIES (same ν): different saturation currents, SAME V₀
  I vs V, different FREQUENCIES (same I): same saturation current, DIFFERENT V₀
  V₀ vs ν : straight line ; slope = h/e (SAME for every metal) ;
            x-intercept = ν₀ ; y-intercept = −φ₀/e ; lines for two metals are PARALLEL

PHOTON : E = hν = hc/λ ;  p = E/c = h/λ ;  rest mass 0 ;  charge 0 (undeflected)
  intensity = (photons per unit area per second) × hν

de BROGLIE : λ = h/p = h/mv ;   λ = h/√(2mK)
  accelerated electron : λ = h/√(2meV) = 12.27/√V Å
  λ ∝ 1/√V ;  same K → heavier particle has SHORTER λ (λ ∝ 1/√m)
  same accelerating V → λ ∝ 1/√(mq)
```

## Ch 12 — Atoms

```
RUTHERFORD SCATTERING
  observations: most pass through | a few small deflections | very few large (>90°)
  conclusions : the atom is mostly EMPTY | a small dense positive NUCLEUS |
                nucleus ~10⁻¹⁵ m vs atom ~10⁻¹⁰ m | nearly all the mass in the nucleus
  impact parameter b: smaller b → larger scattering angle ; b = 0 → 180°
  distance of closest approach : ½mv² = (1/4πε₀)(2e)(Ze)/r₀

  RUTHERFORD FAILS: (1) an accelerating electron must radiate → the atom would
    collapse in ~10⁻⁸ s ;  (2) it predicts a CONTINUOUS spectrum, not LINE spectra

BOHR'S POSTULATES
  1. stationary orbits — the electron revolves without radiating
  2. angular momentum quantised : m v r = n h/2π
  3. radiation only on a jump : hν = E_i − E_f

  r_n = n²h²ε₀/(πmZe²)     → hydrogen : r_n = 0.53 n² Å        r ∝ n²
  v_n = Ze²/(2ε₀nh)                                             v ∝ 1/n
  E_n = −mZ²e⁴/(8ε₀²n²h²)  → hydrogen : E_n = −13.6/n² eV
  K = −E ;   U = 2E = −2K

  ground state n = 1 : E = −13.6 eV
  ionisation energy = 13.6 eV ;   first excitation energy = 10.2 eV

SERIES : Lyman (n_f = 1, UV) | BALMER (n_f = 2, VISIBLE) | Paschen (n_f = 3, IR)
         Brackett (4) | Pfund (5)
  1/λ = R(1/n_f² − 1/n_i²) ,  R = 1.097 × 10⁷ m⁻¹
  (faster: ΔE from E_n = −13.6/n², then λ(nm) = 1240/ΔE(eV))
  longest λ in a series : n_i = n_f + 1 ;  shortest (series limit) : n_i = ∞
  number of lines from level n = n(n − 1)/2

BOHR FAILS for: multi-electron atoms | line intensities | fine structure |
                Zeeman and Stark effects | and the quantisation is unjustified
```

## Ch 13 — Nuclei

```
A = Z + N ;  ᴬ_Z X
isotopes: same Z | isobars: same A | isotones: same N
1 u = 1.66 × 10⁻²⁷ kg ≡ 931.5 MeV
m_p = 1.00728 u ; m_n = 1.00867 u ; m_H atom = 1.00783 u

SIZE : R = R₀ A^(1/3) ,  R₀ = 1.2 fm      ⟹  volume ∝ A ,  A ∝ R³
DENSITY ρ ≈ 2.3 × 10¹⁷ kg m⁻³ — INDEPENDENT of A
  (mass ∝ A and volume ∝ A, so the A cancels ⟹ nuclear matter is incompressible)

NUCLEAR FORCE : strongest at nuclear range | SHORT range (~2–3 fm) |
  CHARGE INDEPENDENT | attractive, but repulsive below ~0.8 fm |
  SATURATED (nearest neighbours only) | spin dependent | non-central

MASS DEFECT  Δm = [Z m_p + (A − Z) m_n] − M
  (use Z m_H instead of Z m_p when ATOMIC masses are given)
BINDING ENERGY  BE = Δm c² ;   BE(MeV) = Δm(u) × 931.5
BE/A : larger ⟹ more stable

BE/A CURVE : rises steeply to ~8 MeV by A ≈ 20 ; ~constant 8 MeV for 30 < A < 170 ;
  PEAK ≈ 8.8 MeV at A = 56 (Fe — the most stable) ; falls to ≈ 7.6 MeV at A = 238
  conclusions: (a) the nuclear force is short range and SATURATED
               (b) FISSION of heavy nuclei releases energy
               (c) FUSION of light nuclei releases energy
  — in both cases the products have a HIGHER BE/A, i.e. lie closer to A ≈ 56

FISSION : ²³⁵U + n → ¹⁴¹Ba + ⁹²Kr + 3n + ~200 MeV  (~0.9 MeV per nucleon)
  releases 2–3 neutrons ⟹ a CHAIN REACTION is possible
FUSION  : ²H + ³H → ⁴He + n + 17.6 MeV ;  4 ¹H → ⁴He + 26.7 MeV (the Sun)
  needs ~10⁷ K to overcome the COULOMB BARRIER — hence "thermonuclear"
  fusion gives MORE energy PER NUCLEON ; fission more per reaction

Q = (mass of reactants − mass of products) c² ;   Q > 0 ⟹ energy released
Z and A are conserved in every nuclear reaction

(radioactivity, the decay law, half-life and mean life are OUT of syllabus)
```

## Ch 14 — Semiconductor Electronics

```
ENERGY BANDS  (E_g = forbidden gap between the valence and conduction bands)
  CONDUCTOR     : E_g = 0, bands overlap ;  conductivity ↓ with T
  SEMICONDUCTOR : E_g ≈ 1 eV (Si 1.1 , Ge 0.7) ;  conductivity ↑ with T
  INSULATOR     : E_g > 3 eV (diamond ≈ 6 eV)

INTRINSIC : pure ;  n_e = n_h = n_i ;  conduction by BOTH electrons and holes
  pairs created thermally ;  n_i rises rapidly with T ;  a perfect insulator at 0 K

EXTRINSIC (doping ≈ 1 impurity atom per 10⁶ host atoms)
  n-TYPE : PENTAVALENT dopant (P, As, Sb, Bi) = DONOR
           majority ELECTRONS, minority holes ;  n_e >> n_h
  p-TYPE : TRIVALENT dopant (B, Al, In, Ga) = ACCEPTOR
           majority HOLES, minority electrons ;  n_h >> n_e
  BOTH ARE ELECTRICALLY NEUTRAL       n_e n_h = n_i²

p-n JUNCTION
  diffusion of majority carriers → immobile ions exposed → DEPLETION REGION
    (negative acceptor ions on the p-side, positive donor ions on the n-side)
  internal field n → p ;  BARRIER POTENTIAL V_B ≈ 0.3 V (Ge) , 0.7 V (Si)
  equilibrium: diffusion current = drift current, net current zero

FORWARD BIAS (p to +) : barrier ↓ , depletion width ↓ , current LARGE (mA) ,
  MAJORITY carriers , resistance LOW ;  knee voltage 0.3 V Ge / 0.7 V Si
REVERSE BIAS (p to −) : barrier ↑ , depletion width ↑ , current TINY (µA) ,
  MINORITY carriers , resistance HIGH
  reverse saturation current is nearly independent of voltage (limited by the number
  of thermally generated minority carriers) but rises with temperature ;
  breakdown at a large reverse voltage

I–V CHARACTERISTIC : non-linear ⟹ the diode is NON-OHMIC
  label the current axis mA for forward and µA for reverse
  dynamic resistance r_d = ΔV/ΔI

RECTIFIER : AC → unidirectional DC (the diode conducts one way only)
  HALF-WAVE : 1 diode ; alternate half-cycles ; output frequency = input ;
              efficiency ≈ 40.6%
  FULL-WAVE : 2 diodes + CENTRE-TAPPED transformer ; both half-cycles ;
              output frequency = 2 × input ; efficiency ≈ 81.2% ; less ripple
  a capacitor in PARALLEL with the load acts as a FILTER, smoothing the ripple

(Zener diode, LED, photodiode, solar cell, transistors and logic gates are OUT)
```

---

## The last-page checklist, for the exam hall

Before you hand the paper in:

1. **Every numerical has a unit.** N, C, V, A, Ω, T, F, H, W, J, eV, m, Hz.
2. **Every graph has both axes labelled**, with quantity **and** unit — and the diode I–V has
   **mA forward, µA reverse**.
3. **Every ray diagram has arrowheads**, at least two rays, and F, 2F, O (and C for a mirror) marked.
4. **Every circuit diagram is labelled** — and the full-wave rectifier's transformer is
   **centre-tapped**.
5. **The phasor diagram is drawn** for any LCR question, asked for or not.
6. **Sign convention checked** on every optics numerical: u negative, concave mirror f negative,
   concave lens f negative.
7. **cos φ included** in every AC power calculation.
8. **Abandoned internal-choice attempts crossed out.**
9. **Question numbers match the paper.**
10. **"Distinguish between" answers are in a two-column table**, comparing the same attribute on each
    row.
