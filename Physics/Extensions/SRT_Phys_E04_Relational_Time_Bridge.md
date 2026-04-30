---
id: SRT-PHYS-E04-RELATIONAL-TIME-BRIDGE
type: bridge_extension
tags: [Physics, Time, Page-Wootters, Relational, Quantum Time, H-Phys-2 Alternative, Bridge]
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
  - SRT-SYMBOL-TABLE
  - SRT-CLAIM-LADDER
  - SRT-PHYS-E02-QRF-BRIDGE
machine_summary: >
  Bridge file giving SRT manifest time a published formal home in the
  Page-Wootters relational-time formalism and its modern revivals
  (Giovannetti-Lloyd-Maccone, Hoehn et al. trinity-of-relational-clocks).
  Provides an explicit non-discrete alternative to H-Phys-2; reads time
  as conditional-probability over an extended Hilbert space, not as a
  Planck-discrete tick. Lowers the empirical pressure FERMI/LIV places
  on H-Phys-2 by routing manifest time through a different formalism
  while keeping the selection-index reading available. Bridge layer
  only.
---

# SRT Physics Extension E04: Relational Time Bridge

> **Status**: Bridge / extension. Non-canonical. Pairs with E02 (QRF
> bridge) and serves as an *alternative formal home* for manifest time
> in SRT, distinct from H-Phys-2's discrete-time hypothesis.

> **Bold claim of this file**: SRT does not need H-Phys-2 (discrete
> Planck time) to give manifest time a physical home. The Page–Wootters
> mechanism — time as conditional probability on an entangled global
> state — is a published, internally consistent, FERMI-compatible
> formalism that exactly fits SRT's "no view from nowhere" commitment
> and supplies the relational structure SRT actually needs. SRT should
> *prefer E04* as its working time-bridge and treat H-Phys-2 as a
> distinct, more speculative, currently FERMI-pressed alternative.

> **Conservative caveat**: this is a *recommendation about which
> bridge to lead with*, not a deletion of H-Phys-2. H-Phys-2 stays as
> an alternate hypothesis. E04 simply offers a less FERMI-vulnerable
> primary formalization.

---

## 0. Source anchors

Primary literature:

- Page, D. N., Wootters, W. K. (1983). *Evolution without evolution:
  dynamics described by stationary observables.* Physical Review D,
  27(12), 2885.
- Wootters, W. K. (1984). *"Time" replaced by quantum correlations.*
  International Journal of Theoretical Physics, 23(8), 701.
- Giovannetti, V., Lloyd, S., Maccone, L. (2015). *Quantum time.*
  Physical Review D, 92, 045033.
- Marletto, C., Vedral, V. (2017). *Evolution without evolution and
  without ambiguities.* Physical Review D, 95, 043510.
- Höhn, P. A., Smith, A. R. H., Lock, M. P. E. (2021). *The trinity of
  relational quantum dynamics.* Physical Review D, 104, 066001.
- Smith, A. R. H., Ahmadi, M. (2020). *Quantizing time: interacting
  clocks and systems.* Quantum, 4, 271.
- Castro-Ruiz, E., Giacomini, F., Belenchia, A., Brukner, Č. (2020).
  *Quantum clocks and the temporal localisability of events in the
  presence of gravitating quantum systems.* Nature Communications,
  11, 2672.
- Sorci, G., Foo, J., Leibfried, D., Sanner, C., Pikovski, I. (2026).
  *Quantum signatures of proper time in optical ion clocks.*
  Physical Review Letters [P05 patch source].
- Rovelli, C. (1996). *Relational quantum mechanics.* International
  Journal of Theoretical Physics, 35(8), 1637.

Empirical pressure on the alternative (H-Phys-2):

- Abdo, A. A. et al. (Fermi GBM/LAT Collaborations) (2009). *A limit on
  the variation of the speed of light arising from quantum gravity
  effects.* Nature, 462, 331.

Internal anchors:

- [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md) H-Phys-2 [H1.4.2]
  and DP-PHYS-2.
- [`../patches/SRT_Phys_P05_Quantum_Proper_Time_Optical_Clocks_v0_1.md`](../patches/SRT_Phys_P05_Quantum_Proper_Time_Optical_Clocks_v0_1.md)
  for the cousin programme on quantum clocks.
- [`SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md`](SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md)
  for the QRF formalism that E04 sits inside.

---

## 1. Why this bridge matters for SRT

The current SRT physics-bridge has a structural problem with time:

1. **H-Phys-2 (discrete time at Planck scale)** is the only formalized
   bridge to physical time, and it is FERMI-pressed (DP-PHYS-2).
2. **The selection-index reading** ("time = ordinal of irreversible
   selection events") is interpretive and lacks formal physics
   machinery.
3. **Relational time** — the natural fit with SRT's no-view-from-nowhere
   commitment — has no current SRT formalization, even though it has
   been a published quantum-foundations programme since 1983.

E04 fills gap (3). It does not delete H-Phys-2, but it deprives
H-Phys-2 of its monopoly: SRT no longer needs a discrete-time
commitment to have a formal physical home for manifest time.

---

## 2. The Page–Wootters mechanism, in SRT vocabulary

### 2.1 The published mechanism

In the Page–Wootters formulation, the global universe state $|\Psi\rangle\rangle$
on $\mathcal{H}_{\mathrm{clock}} \otimes \mathcal{H}_{\mathrm{system}}$
is *stationary*:
$$
\hat{H}_{\mathrm{tot}} |\Psi\rangle\rangle = 0,
\qquad \hat{H}_{\mathrm{tot}} = \hat{H}_C \otimes I + I \otimes \hat{H}_S.
$$

There is no global time. *Manifest time* arises as the conditional
state of the system given a clock reading:
$$
|\psi_S(t)\rangle = \frac{\langle t |_C \otimes I_S |\Psi\rangle\rangle}{\sqrt{\langle\Psi|\Psi\rangle\rangle_t}}.
$$

The Schrödinger equation
$i \hbar\, \partial_t |\psi_S(t)\rangle = \hat{H}_S |\psi_S(t)\rangle$
emerges as a consistency condition.

Modern revivals (Giovannetti–Lloyd–Maccone, Höhn–Smith–Lock) show that
this is internally consistent, equivalent to other relational-time
formulations (the "trinity"), and extensible to interacting clocks.

### 2.2 SRT mapping

Bridge claim **B-E04-1**:

> SRT's $L_1$ manifest time, in its physical-quantum projection,
> reads as the *clock-conditioned reduced state* of the rest of the
> universe given a Page–Wootters clock subsystem. The choice of clock
> subsystem is part of $\theta$.

In SRT formal: the manifest content of $L_1$ at clock-reading $t$ is
the conditional system state
$$
\rho_S^{(\theta)}(t) \;\equiv\; \mathrm{Tr}_{C(\theta)}\!\left[\,\big(|t\rangle_{C(\theta)}\langle t| \otimes I_S\big)\, \rho_{\mathrm{tot}}\,\right] \big/ \mathcal{N}(t),
$$
where $C(\theta)$ is the embodied clock subsystem chosen by $\theta$
(specifically by $\theta_{boundary}$, since "what counts as the
clock" is a frame-system choice), $\rho_{\mathrm{tot}}$ is the global
stationary state, and $\mathcal{N}(t)$ is the appropriate
normalization. The clock parameter $t$ is *not* an extracted scalar
("the time"); it is an *index* labelling the family of clock-relative
system states that constitutes manifest temporal content.

This is the standard Page–Wootters / Höhn–Smith–Lock formulation
written in SRT vocabulary. SRT does not claim to have derived the
formula; SRT inherits it.

Bridge claim **B-E04-2**:

> SRT's "no view from nowhere" commitment becomes the published
> assertion that *there is no global $t$*; physical time is always
> conditional on a clock subsystem.

This is *not* SRT recasting the Page–Wootters formalism; it is SRT
noting that this formalism already says what SRT says, and adopting
it as the natural physical home.

### 2.3 Connection to QRF (E02)

In the modern QRF literature (Höhn et al. 2021), Page–Wootters is
*exactly* a temporal QRF: the clock subsystem is the QRF, and the
"trinity of relational dynamics" shows the equivalence between the
Page–Wootters, Dirac-quantization-with-clock, and relativized-
observable approaches.

Bridge claim **B-E04-3**:

> $\theta_{boundary}$ in E02 includes the choice of *temporal* QRF.
> Time-related embodiment is therefore a special case of QRF
> embodiment.

This unifies E02 and E04: time is not a separate domain; it is QRF
applied to a clock subsystem.

---

## 3. What this gives SRT that H-Phys-2 does not

| Concern | H-Phys-2 (Planck-discrete) | E04 (Page–Wootters / relational) |
|---|---|---|
| **Empirical pressure** | FERMI/LIV pressed, DP-PHYS-2 standing | No FERMI conflict; relational time is consistent with continuous Lorentz behaviour |
| **Mathematical home** | Heuristic ($t_n = n \tau_{Planck}$) | Published, decades-old, internally consistent |
| **Connection to selection** | Each tick = one selection (interpretive) | Conditional probability on clock observable; selection events are clock-readings |
| **Connection to QRF** | None | Direct (Höhn et al. trinity) |
| **Connection to GR** | Requires unspecified discrete-spacetime model | Natural in canonical-quantum-gravity / Wheeler–DeWitt setting |
| **Connection to subjective time (N11)** | Reads as background substrate | Provides the formal envelope inside which subjective time can be embodied without category error |

E04 wins on every row that matters for SRT's actual commitments.

---

## 4. The selection-index reading, preserved

H-Phys-2's interpretive content — *time as ordinal of irreversible
selection events* — is *preserved* by E04, and arguably sharpened.

Bridge claim **B-E04-4**:

> Under the Page–Wootters mechanism, an "irreversible selection event"
> is a clock-reading at which the conditional state $|\psi_S(t)\rangle$
> transitions to a $\hat{G}_\theta$-stable branch; the *index* of such
> events along the clock observable is the selection-index time of
> Core Axiom A1.

This means SRT can keep the selection-index reading fully *without*
committing to Planck-scale discreteness. H-Phys-2 becomes one
*additional* hypothesis (that the clock observable's spectrum is
discrete at Planck scale); E04 is independent of that hypothesis.

---

## 5. Connection to the P05 patch

The P05 patch
([`../patches/SRT_Phys_P05_Quantum_Proper_Time_Optical_Clocks_v0_1.md`](../patches/SRT_Phys_P05_Quantum_Proper_Time_Optical_Clocks_v0_1.md))
brings optical-ion-clock proper time into SRT as a structural bridge.
E04 supplies the *unifying formalism*:

- P05 shows that physical clocks under quantum control reveal the
  state-dependence of proper time;
- E04 says: this is what one expects when the clock is the QRF and
  time is conditional;
- The Sorci–Foo–Leibfried–Sanner–Pikovski experimental programme is
  then a direct test of relational-time predictions, not just a
  curiosity.

Bridge claim **B-E04-5**: E04 is the *unified theoretical home* for
P05's physical bridge, and for the structural-temporal claims in
SRT_Quant_02_Cosmology.md.

---

## 6. Falsifiability windows opened by E04

### 6.1 Window F-E04-α: relational-time vs absolute-time discriminator

E04 commits SRT to: the result of a temporal measurement is *only ever*
a clock-reading conditional on a chosen clock; there is no operationally
accessible global time independent of clock choice.

Test class: experiments comparing clock-readings across pairs of
reference clocks in non-trivial gravitational potential, where the
Castro-Ruiz–Giacomini–Belenchia–Brukner programme makes specific
predictions about temporal localizability.

Falsification threshold: a temporal measurement is found whose result
is independent of clock choice within the precision available. SRT's
B-E04-1 then has to retreat.

### 6.2 Window F-E04-β: Page–Wootters consistency under interacting clocks

Smith–Ahmadi (2020) extended Page–Wootters to interacting clocks. SRT's
$\theta$ structure (B-E04-3) entails that interacting embodied clocks
should obey the predicted modifications.

Test class: precision atomic-clock comparisons in optical-lattice
configurations where clock–system interaction is engineered.

Falsification threshold: experiments find clock-system coupling that
violates the published interacting-clock predictions, requiring an
independent SRT-specific correction.

### 6.3 Window F-E04-γ: selection-index alignment

B-E04-4 entails that *irreversible* selection events should align with
clock-reading transitions. This is in principle measurable in
continuous-monitoring quantum systems where both irreversibility (jump
events) and clock-reading times are independently recorded.

Test class: continuous-measurement platforms with high-precision
external clocks.

Falsification threshold: irreversibility-marking events are found to
have a systematic offset from clock-reading times that is not
accounted for by hardware delay.

---

## 7. Recommended use in the bridge layer

E04 should be the **primary** time-bridge for SRT going forward.

Recommended layering in `_SRT_Phys_Bridge.md` (this batch does *not*
edit that file; this section is a *recommendation* for a future
canonical update):

| Layer | Status | Role |
|---|---|---|
| E04 (relational time) | **primary** | Time as conditional probability over chosen clock; no FERMI conflict |
| H-Phys-2 (Planck-discrete) | hypothesis / bridge | Additional commitment about clock-spectrum discreteness; FERMI-pressed |
| Selection-index reading (A1) | interpretive | Preserved under E04 as ordering of clock-readings of irreversible events |
| P05 (quantum proper time) | external-material patch | Empirical handle on E04 predictions |

---

## 8. What this bridge does NOT claim

1. It does **not** claim to *prove* relational time is the correct
   physics; the Wheeler–DeWitt programme is unfinished and the
   Page–Wootters mechanism has open issues (the Kuchař critique, etc.).
2. It does **not** delete H-Phys-2; H-Phys-2 stays as an alternate
   hypothesis.
3. It does **not** identify SRT subjective time (N11 framework) with
   Page–Wootters time. They live at different levels and have
   different variables.
4. It does **not** claim SRT predicted Page–Wootters; it claims SRT
   should *use* it as its formal envelope.
5. It does **not** modify any canonical anchor.

---

## 9. Promotion criteria

E04 could ascend the claim ladder only if:

1. A canonical-registry update reorients
   [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md) to lead with E04
   for time and demote H-Phys-2;
2. A symbol-table reconciliation is done, distinguishing $t_{L_1}$
   (manifest), $t_{L_1}^{(\theta)}$ (clock-relative), and any
   subjective-time variable ($\tau$);
3. At least one of windows F-E04-α / F-E04-β / F-E04-γ returns a
   reproducible discriminator.

Until then, B-E04-1 through B-E04-5 stay at P3 (bridge mapping).

---

## 10. One-paragraph abstract

This bridge gives SRT manifest time a published formal home in the
Page–Wootters relational-time mechanism and its modern revivals
(Giovannetti–Lloyd–Maccone, Marletto–Vedral, Höhn–Smith–Lock). The
core identification is that SRT's $L_1$ manifest temporal content,
in its physical-quantum projection, reads as the family of
clock-conditioned reduced states $\rho_S^{(\theta)}(t)$ on the chosen
clock subsystem, where the clock choice is part of the embodiment
parameter $\theta_{boundary}$ shared with the QRF bridge of E02.
This formalization is FERMI-compatible (no Lorentz-invariance
pressure), connects directly to the P05 quantum-proper-time patch,
preserves the selection-index reading of Core Axiom A1, and should
serve as SRT's *primary* time-bridge — with H-Phys-2 demoted to an
additional, more speculative, currently FERMI-pressed alternative.
The bridge opens three falsification windows tied to clock-choice
dependence, interacting-clock consistency, and the alignment of
irreversibility-marking events with clock readings.
