---
id: SRT-PHYS-E05-FALSIFIABILITY-PROGRAM
type: research_program
tags: [Physics, Falsifiability, Lakatos, Research Program, Experimental Tests, Bridge]
status: active_v1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
canonical_status: non_canonical
canonical: false
batch: physics_extensions_v0_1
date: 2026-04-30
dependency:
  - SRT-PHYS-BRIDGE
  - SRT-PHYS-E01-QUANTUM-INSTRUMENT-BRIDGE
  - SRT-PHYS-E02-QRF-BRIDGE
  - SRT-PHYS-E03-INFO-THERMO-BRIDGE
  - SRT-PHYS-E04-RELATIONAL-TIME-BRIDGE
  - SRT-CLAIM-LADDER
machine_summary: >
  Lakatos-style research-programme statement for SRT physics. Defines
  the hard core (irreducible commitments), the protective belt
  (revisable bridges), seven concrete near-term falsification windows
  pulled from E01-E04 plus the existing _SRT_Phys_Bridge.md DP-PHYS
  pressures, degenerative-shift criteria, and a clear definition of
  what would count as a positive empirical handle. Bridge layer only;
  does not modify primitives.
---

# SRT Physics Extension E05: Falsifiability Program

> **Status**: Bridge / extension. Non-canonical. Capstone of the v0.1
> Extensions batch.

> **Bold claim of this file**: SRT physics is a *Lakatosian research
> programme*, not a sealed theory. It has a hard core of irreducible
> commitments, a protective belt of revisable bridges, and a stated
> path to either progressive-shift confirmation or degenerative-shift
> abandonment. This file makes both ends explicit, pulling together
> the seven concrete falsification windows opened in E01–E04 and the
> existing DP-PHYS pressures in `_SRT_Phys_Bridge.md` §VI.

> **Conservative caveat**: making the programme explicit is *not*
> claiming any of the falsification windows will favour SRT. Several
> of them — especially F-E03-β (Landauer-saturation) and F-E04-α
> (clock-choice independence) — could plausibly land against SRT's
> bridge readings. The point is to make the bet *legible*.

---

## 0. Source anchors

Methodological:

- Lakatos, I. (1970). *Falsification and the methodology of scientific
  research programmes.* In *Criticism and the Growth of Knowledge*,
  Cambridge University Press, 91–196.
- Popper, K. R. (1959). *The Logic of Scientific Discovery.* Hutchinson.
- Worrall, J. (1989). *Structural realism: the best of both worlds?*
  Dialectica, 43(1–2), 99.

Internal:

- [`SRT_Phys_E01_Quantum_Instrument_Bridge.md`](SRT_Phys_E01_Quantum_Instrument_Bridge.md)
  §5.
- [`SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md`](SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md)
  §5.
- [`SRT_Phys_E03_Information_Thermodynamics_Bridge.md`](SRT_Phys_E03_Information_Thermodynamics_Bridge.md)
  §5.
- [`SRT_Phys_E04_Relational_Time_Bridge.md`](SRT_Phys_E04_Relational_Time_Bridge.md)
  §6.
- [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md) §VI (DP-PHYS-1
  through DP-PHYS-4) and "Future Derivation Standard".

---

## 1. The provisional physics-facing hard core

The set of commitments below is a **provisional physics-facing hard
core**: a tentative, repo-internal, programme-bookkeeping construct
for the v0.1 Extensions batch. It is *not* the canonical SRT hard
core. Canonical SRT primitives live in `Core_Law/`, `Core/`, and
`_SRT_*_CANONICAL.md`; nothing in this file replaces or constrains
them.

The provisional hard core states which physics-facing commitments
this Extensions batch is willing to put under explicit empirical
pressure, and what would refute *the physics-bridge programme* (not
SRT-as-a-whole) if it failed.

| HC# | Provisional physics-facing commitment | Source |
|---|---|---|
| HC-1 | Selection events resist full eliminability: any complete physical description of $L_1$ that drops $\hat{G}_\theta$ also loses access to the embodiment-relative content of measurement. | Core Axiom A1; Def-Phys-1 |
| HC-2 | Embodiment is non-trivial: there is no view from nowhere on the physical projection; $\theta$ tracks a real physical degree of freedom (Heisenberg cut, frame system, dilation environment). | `_SRT_Phys_Bridge.md` §I; E01 §3; E02 §2 |
| HC-3 | Selection has cost: the physical projection of $\hat{G}_\theta$ obeys a *generalized payability constraint* — a non-negative cost is incurred whenever the event includes irreversible record stabilization. The specific mathematical form (Sagawa–Ueda, Crooks-style, Fisher-monotone, or another) is one of several allowed instantiations under E03. | E03 (one instantiation); `_SRT_PSI_F_CANONICAL.md` |
| HC-4 | Manifest time is relational: physical-domain $t_{L_1}$ is given through a clock-conditioned reduced state, not a globally extracted scalar. | E04 B-E04-1 |
| HC-5 | $L_2$ has an embodiment-invariant content: some structure survives every change of $\theta$, and physics-side conservation laws are an image of that content. | T-Phys-3; E02 B-E02-7 |

A reproducible experiment that falsified an HC line in its
*physics-bridge reading* would refute the physics-bridge programme —
i.e., would force replacement of the corresponding canonical-to-physics
projection — without by itself refuting SRT-as-a-whole, because
canonical SRT does not depend on any single physical projection.

The provisional hard core is *small on purpose*. The physics-bridge
programme survives by keeping HC-1 through HC-5 small, sharp, and
falsifiable in their physics-facing readings.

Critically, **HC-3 is not bound to Sagawa–Ueda**. E03 supplies one
instantiation (the entropy-production proxy $\sigma_f^{phys}$ of
B-E03-5), but a Fisher-monotone instantiation (per
`SRT_Phys_09_Formalism_Ext_CompactCore.md` §4) or any other
non-negative payability quantity also satisfies HC-3. Failure of one
instantiation is a belt-line retraction, not a hard-core failure.

---

## 2. The protective belt

The protective belt is the set of revisable bridges. These are
hypotheses that can be modified or replaced without disturbing the
provisional physics-facing hard core in §1.

| PB# | Bridge | Source | Replaceability |
|---|---|---|---|
| PB-1 | $\hat{G}_\theta$ as Davies–Lewis instrument | E01 | Replaceable by other CPTP-formal homes |
| PB-2 | $\theta_{boundary}$ as QRF coset | E02 | Replaceable if a different mathematics for the cut emerges |
| PB-3 | $\Psi_f^{phys}$ as Sagawa–Ueda residual | E03 | Replaceable by other published thermodynamic-information frameworks |
| PB-4 | Manifest time as Page–Wootters | E04 | Replaceable by Dirac-quantization-with-clock or other relational-dynamics formalism |
| PB-5 | Discrete time at Planck scale (H-Phys-2) | `_SRT_Phys_Bridge.md` H1.4.2 | *Already pressed* by FERMI; demoted to alternate hypothesis below E04 |
| PB-6 | Gravity / friction structural analogy (H-Phys-4) | `_SRT_Phys_Bridge.md` H1.4.4 | Open research direction, no current empirical pressure or support |
| PB-7 | Selection-index reading of A1 | `_SRT_Phys_Bridge.md` H-Phys-2 commentary | Preserved under E04; survives even if H-Phys-2 fails |

The provisional physics-facing hard core (HC-*) does *not* depend on
any single PB-* line. The physics-bridge programme can lose any one
of PB-1 through PB-7 and remain alive.

---

## 3. Falsification windows (consolidated)

The following table consolidates falsification windows from E01–E04 and
the existing `_SRT_Phys_Bridge.md` §VI domain pressures. Each window has
a hard threshold: a specific experimental observation that would push a
specific belt line toward retraction.

| ID | Source | Test class | Falsification threshold |
|---|---|---|---|
| **F-E01-α** | E01 §5.1 | Continuously-monitored systems with reconfigured $\theta_{boundary}$ | Standard QM error model reproduces all reconfiguration-rate-dependent error within stated uncertainty |
| **F-E01-β** | E01 §5.2 | Engineered-reservoir cavity- / circuit-QED platforms | Instrument calibration cost is invariant under swap of mathematically-equivalent dilation environment |
| **F-E01-γ** | E01 §5.3 | Continuous-measurement (homodyne / photon counting) on identical reduced dynamics | Multiple inequivalent unravelings reproduce all apparatus behaviour without any distinguishing parameter |
| **F-E02-α** | E02 §5.1 | QRF-style frame-relative classicality experiments | Frame-relative classicality is invariant under physical reconfiguration of apparatus environment |
| **F-E02-β** | E02 §5.2 | Dual-rail interferometry with reconfigurable QRF role | Calibration cost invariant under swap of mathematically-equivalent rail roles |
| **F-E03-α** | E03 §5.1 | Optical-trap colloidal feedback under shifted formal prior | Sagawa–Ueda saturation without an SRT residual across $\theta_{formal}$ shifts |
| **F-E03-β** | E03 §5.2 | State-of-the-art Landauer-erasure (single atom, superconducting) | Bound saturated to within quantum-limit precision, no SRT residual |
| **F-E03-γ** | E03 §5.3 | Detection events in routine vs. high-irreversibility-context | Dissipation-per-bit is contextual-irreversibility-independent within precision |
| **F-E04-α** | E04 §6.1 | Castro-Ruiz–Giacomini–Belenchia–Brukner-style temporal-localizability | Temporal measurement result independent of clock choice within available precision |
| **F-E04-β** | E04 §6.2 | Optical-lattice precision atomic-clock comparisons | Clock-system coupling violates published interacting-clock predictions in an SRT-incompatible direction |
| **F-E04-γ** | E04 §6.3 | Continuous-monitoring with high-precision external clock | Irreversibility-marking events systematically offset from clock-readings beyond hardware delay |
| **DP-PHYS-1** | `_SRT_Phys_Bridge.md` §VI | Quantum-foundations interpretation contests | Robust experimental discriminator forces MWI over collapse-family and Ax-P1's $\hat{G}_\theta$ collapse-language reading |
| **DP-PHYS-2** | `_SRT_Phys_Bridge.md` §VI | Lorentz-invariance precision tests (FERMI/LAT, GRB) | Already constraining H-Phys-2 (PB-5) — demoted; not refuting the hard core under E04 |
| **DP-PHYS-4** | `_SRT_Phys_Bridge.md` §VI | Constants-explanation programmes (EFT flow, string landscape, anthropic) | External programme delivers a derivation of constants; SRT must absorb without claiming priority |

These thirteen windows are not equally near-term. The single most
empirically-pressing window in 2026 is **F-E04-β** (interacting
quantum clocks): the Sorci–Foo–Leibfried–Sanner–Pikovski programme is
moving toward laboratory tests on a near horizon.

---

## 4. Asymmetry: what would count as positive empirical support

Lakatos requires that a research programme also state *progressive*
discoveries: empirical handles that would push it forward.

| Window | Positive-direction discovery |
|---|---|
| F-E01-α / β / γ | An SRT residual error / cost / unraveling-uniqueness term emerges in published replication |
| F-E02-α / β | Frame-maintenance asymmetry tracks a $\theta_{boundary}$-dependent quantity not predicted by base QRF alone |
| F-E03-α / β / γ | Sagawa–Ueda or Landauer experiments show a residual term tracking a $\theta_{instrument}$ / $\theta_{formal}$ / $d$-value index |
| F-E04-α / β / γ | Temporal-localizability or interacting-clock or selection-index-alignment data fits SRT's relational-with-embodiment prediction better than minimal Page–Wootters |
| DP-PHYS-3 reverse | An independent tensor-level derivation of $G_{\mu\nu}$ from a $\Psi_f$-shaped quantity emerges and is empirically discriminated from Verlinde / Jacobson |

Any *single* line crossing the positive-discovery threshold is *not* a
proof of SRT, but it is a progressive shift: the protective belt has
absorbed an empirical anomaly that base physics did not predict in the
same form.

---

## 5. Degenerative-shift criteria

A research programme degenerates when its protective belt accumulates
ad hoc auxiliary hypotheses that absorb anomalies without empirical
gain. The following criteria flag SRT physics as degenerating:

| Criterion | Trigger |
|---|---|
| **Belt-line proliferation without prediction** | Each falsification window forces a new belt-line auxiliary that does not predict any independent test |
| **Hard-core erosion** | A provisional HC-* line is silently relaxed to accommodate a failure (e.g. HC-3 silently narrowed from "generalized payability constraint" to "Sagawa–Ueda within experimental noise" without an open governance entry) |
| **Bridge proliferation** | More than ~3 distinct formal homes for the same primitive (e.g., three different mathematical homes for $\hat{G}_\theta$) maintained simultaneously without prediction-discriminating |
| **Empirical-anchor abandonment** | The Bérut / Yan / Toyabe et al. anchors are explicitly abandoned in favour of "but our $\sigma_f^{phys}$ is not theirs" |
| **Empirical retreat** | After any positive-direction discovery, no follow-up testable prediction is generated |

If two or more of these criteria are satisfied, the research-programme
governance body (here: the canonical-registry maintainers) should mark
SRT physics as degenerating and either restructure the hard core or
suspend new bridge additions.

---

## 6. Five-year priority matrix

If only a few falsification windows can be pursued, the following
priority is recommended:

| Priority | Window | Reason |
|---|---|---|
| **1** | **F-E04-β** (interacting quantum clocks) | Empirical infrastructure already published (P05 patch); near-term laboratory horizon; tests HC-4 in projection |
| **2** | **F-E03-α** (Sagawa–Ueda residual under $\theta_{formal}$) | Builds on existing colloidal-feedback infrastructure; tests one HC-3 instantiation |
| **3** | **F-E03-γ** ($d$-value scaling of Landauer dissipation) | High-leverage, distinctive of SRT, but highest experimental difficulty; restricted to record-stabilization scope |
| **4** | **F-E02-β** (dual-rail QRF cost asymmetry) | Tests HC-2 in projection; existing dual-rail interferometry infrastructure |
| **5** | **F-E01-β** (dilation-environment selection) | Tests HC-1's non-eliminability route; existing engineered-reservoir platforms |

F-E03-γ deserves a separate note: it is the one window where SRT could
*decisively* differentiate itself from non-equilibrium statistical
mechanics. A confirmation would be a major shift; a clean failure
would be a meaningful retreat.

---

## 7. What this program does NOT claim

1. It does **not** claim any of the falsification windows favours SRT.
2. It does **not** make SRT into a finished theory; it makes SRT into
   a *legibly betting* research programme.
3. It does **not** modify any canonical anchor.
4. It does **not** dismiss the §VI DP-PHYS pressures; it inherits
   them.
5. It does **not** treat MWI as refuted (DP-PHYS-1); it treats DP-PHYS-1
   as a permanent open interface, not a falsification window in the
   Lakatos sense.
6. It does **not** treat constants-explanation as an SRT problem to
   solve (DP-PHYS-4); it treats SRT as required to absorb whatever
   external physics delivers.

---

## 8. Self-update rule

This program-statement should be revised when:

| Trigger | Action |
|---|---|
| A falsification window returns a positive or negative discriminator | Revise §3 row, add follow-up prediction or retract belt-line in §2 |
| A new bridge file is added under `Physics/Extensions/` | Append to §1 / §2 as HC or PB; add windows to §3 |
| Any HC-* line is challenged | Open a `Governance/SRT_OPEN_TENSIONS.md` entry before quietly weakening the line |
| External physics produces a constants-derivation, gravity-derivation, or MWI-discriminator | Update §1 / §3 / §5 |
| Two §5 degenerative criteria are simultaneously met | Trigger the governance review described in §5 |

---

## 9. One-paragraph abstract

This file states the SRT physics-bridge programme as an explicit
Lakatosian research programme: a *provisional physics-facing* hard
core of five commitments (selection resists full eliminability;
embodiment is non-trivial; selection has cost as a generalized
payability constraint; manifest time is relational via clock-
conditioned states; $L_2$ has embodiment-invariant content), a
protective belt of seven revisable bridges (E01–E04 plus H-Phys-2,
H-Phys-4, and the selection-index reading), and a consolidated table
of thirteen falsification windows pulled from E01–E04 §5 and
`_SRT_Phys_Bridge.md` §VI. The provisional hard core is *not* the
canonical SRT hard core; it is a programme-bookkeeping construct
specifying what would refute the physics-bridge programme without
refuting SRT-as-a-whole. HC-3 is deliberately not bound to any
single inequality (Sagawa–Ueda or otherwise); E03's instantiation is
one of several allowed forms. The programme is degenerating if its
belt proliferates without prediction, a provisional HC-* line is
silently relaxed, or its empirical anchors are abandoned. The single
most empirically-pressing near-term window in 2026 is F-E04-β
(interacting quantum clocks); the most SRT-distinctive is F-E03-γ
($d$-value scaling of Landauer dissipation, restricted to the
record-stabilization scope). The programme makes the physics-side
bet legible without claiming victory.
