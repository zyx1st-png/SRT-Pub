---
id: SRT-PHYS-E02-QRF-BRIDGE
type: bridge_extension
tags: [Physics, Quantum Reference Frames, Heisenberg Cut, Theta Boundary, Bridge]
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
  - SRT-SYMBOL-TABLE
  - SRT-CLAIM-LADDER
machine_summary: >
  Bridge file giving theta_boundary (Heisenberg cut) a textbook formal
  home in the Giacomini-Castro-Ruiz-Brukner quantum-reference-frame
  formalism. Reads the Heisenberg cut as a QRF transformation orbit
  rather than as an arbitrary observer choice. Shows that in SRT, what
  looks like observer-relative non-classicality (mass superposition,
  entanglement) is the natural reading of the cut as a physical degree
  of freedom. Bridge layer only; does not redefine theta or modify
  Def-Phys-1.
---

# SRT Physics Extension E02: Quantum Reference Frames Bridge

> **Status**: Bridge / extension. Non-canonical. Pairs with E01.

> **Bridge claim of this file**: SRT's $\theta_{boundary}$ — the
> Heisenberg cut placement parameter — admits a *QRF-compatible
> projection* in the Giacomini–Castro-Ruiz–Brukner sense. Under that
> projection, changes of cut behave like quantum-reference-frame
> transformations and the cut acquires partial group-theoretic
> structure. SRT thereby gains a published mathematical home for what
> previously read as embodied perspectivalism, *without* claiming that
> $\theta_{boundary}$ is exhausted by any single coset construction.

> **Conservative caveat**: SRT does not claim to predict the outcomes of
> QRF experiments. It claims that the outcomes already published in QRF
> literature are best read as *empirical confirmation that
> $\theta_{boundary}$ is a physical parameter*, not a hidden variable
> outside physics.

---

## 0. Source anchors

Primary literature:

- Giacomini, F., Castro-Ruiz, E., Brukner, Č. (2019). *Quantum
  mechanics and the covariance of physical laws in quantum reference
  frames.* Nature Communications, 10, 494.
- Castro-Ruiz, E., Giacomini, F., Belenchia, A., Brukner, Č. (2020).
  *Quantum clocks and the temporal localisability of events in the
  presence of gravitating quantum systems.* Nature Communications, 11,
  2672.
- de la Hamette, A.-C., Galley, T. D. (2020). *Quantum reference frames
  for general symmetry groups.* Quantum, 4, 367.
- Vanrietvelde, A., Höhn, P. A., Giacomini, F., Castro-Ruiz, E. (2020).
  *A change of perspective: switching quantum reference frames via a
  perspective-neutral framework.* Quantum, 4, 225.
- Krumm, M., Höhn, P. A., Müller, M. P. (2021). *Quantum reference frame
  transformations as symmetries and the paradox of the third particle.*
  Quantum, 5, 530.
- Aharonov, Y., Susskind, L. (1967). *Charge superselection rule.*
  Physical Review, 155(5), 1428. [historical anchor]
- Bartlett, S. D., Rudolph, T., Spekkens, R. W. (2007). *Reference
  frames, superselection rules, and quantum information.* Reviews of
  Modern Physics, 79(2), 555.

Internal anchors:

- [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md) §I (operator
  mapping), Def-Phys-1 [D1.1.1].
- [`SRT_Phys_E01_Quantum_Instrument_Bridge.md`](SRT_Phys_E01_Quantum_Instrument_Bridge.md)
  §3 ($\theta_{boundary}$ as Stinespring bipartition).
- [`../patches/SRT_Phys_P05_Quantum_Proper_Time_Optical_Clocks_v0_1.md`](../patches/SRT_Phys_P05_Quantum_Proper_Time_Optical_Clocks_v0_1.md)
  for the cousin programme on quantum clocks.

---

## 1. Why this bridge matters for SRT

Three current physics-bridge gaps:

1. **$\theta_{boundary}$ as the Heisenberg cut** has no published
   mathematical structure in `_SRT_Phys_Bridge.md`. It is named, and
   asserted to be physical, but its group structure is left implicit.
2. **Observer perspectivalism in SRT** (the claim that there is no "view
   from nowhere") would normally be dismissed as philosophy. QRF makes
   it a published quantum-information research programme with falsifiable
   transformation laws.
3. **Compatibility with both Copenhagen and MWI** is asserted in §VI of
   `_SRT_Phys_Bridge.md` but without machinery. QRF provides such
   machinery: changes of QRF are unitary, so the formalism is reading-
   neutral.

E02 closes these gaps.

---

## 2. The bridge: $\theta_{boundary}$ as a QRF orbit

### 2.1 QRF reminder (bridge-local)

In the QRF programme, given a global Hilbert space describing $N$
systems and a symmetry group $G$ acting on the relevant external
parameters (translations, rotations, boosts, time evolution), one
*chooses a system to play the role of frame*. Physical states are then
described relative to that frame. A change of frame is a unitary
transformation
$$
\hat{S}_{C \to A}^{(G)} : \mathcal{H}^{(C)} \to \mathcal{H}^{(A)},
$$
where $\mathcal{H}^{(C)}$ is the Hilbert space "as seen from frame $C$"
(which factors out $C$'s degrees of freedom) and likewise for $A$.

Crucially, $\hat{S}^{(G)}$ can map a *classical* description in one
frame to a *quantum-superposed* description in another. The
Giacomini–Castro-Ruiz–Brukner result is that this is not a paradox; it
is the QRF analogue of a Lorentz boost mapping a static configuration
into a moving one.

### 2.2 SRT mapping

Bridge claim **B-E02-1** (QRF-compatible projection):
$$
\theta_{boundary} \;\xrightarrow{\;\Pi_{QRF}\;}\; [\,\mathrm{frame\ system}\,] \in \mathcal{F}/G,
$$
where $\mathcal{F}$ is the set of admissible frame systems
(subsystems that can play the role of QRF), $G$ is the relevant
symmetry group, and $\Pi_{QRF}$ is the QRF-compatible projection.
Under that projection, the Heisenberg cut content of
$\theta_{boundary}$ is represented as a coset selecting a frame.

In words: when SRT's cut is read through the QRF formalism, the
choice of cut maps onto the choice of which subsystem plays the role
of the reference frame. This is not a free philosophical choice in
that projection. SRT does *not* claim that the entirety of
$\theta_{boundary}$ — including non-quantum, biological, or
historical contributions — is exhausted by $\mathcal{F}/G$.

Bridge claim **B-E02-2**: under the QRF-compatible projection, changes
of $\theta_{boundary}$ are represented by unitary QRF transformations
$\hat{S}^{(G)}_{C \to A}$.

This means SRT inherits a published transformation law for the
projected component. Two SRT descriptions with different
$\theta_{boundary}$ are then related, in projection, by a specific
unitary — not by an arbitrary epistemic relabeling.

### 2.3 Frame-relative classicality

A central published QRF result: a state can be classical relative to
one frame and quantum-superposed relative to another. Specifically, if
two systems are entangled in the laboratory frame, choosing either of
them as the QRF can render the other in a definite state.

Bridge claim **B-E02-3**: SRT's "$L_1$ is the manifest layer relative to
embodied selection" *is* this QRF result, written in SRT vocabulary.
Manifest classicality is *frame-relative*. The SRT addition is the
identification of the frame system with the embodied selector
$\hat{G}_\theta$.

This is a substantive bridge, not a redescription. It says: the
"observer-dependence" in SRT is the same observer-dependence that QRF
publications already establish, not a separate philosophical layer.

---

## 3. Group structure of $\theta$ (under projection)

Once $\theta_{boundary}$ is read into $\mathcal{F}/G$ via $\Pi_{QRF}$,
the rest of $\theta$ acquires partial structure on the same projection:

| SRT component | QRF-side counterpart |
|---|---|
| $\theta_{boundary}$ | choice of frame system + section of $G$-bundle |
| $\theta_{basis}$ | choice of orthogonal decomposition of $\mathcal{H}^{(\theta_{boundary})}$ |
| $\theta_{H_{int}}$ | choice of interaction Hamiltonian *relative to the chosen frame* |

Bridge claim **B-E02-4** (projected hierarchy): in the QRF projection,
$\theta$ has a *partially ordered* structure on its components:
$\theta_{boundary}$ is fixed first (it sets the Hilbert space we work
in), $\theta_{basis}$ is then chosen on
$\mathcal{H}^{(\theta_{boundary})}$, and $\theta_{H_{int}}$ governs
the post-projection dynamics.

This hierarchy holds *under the QRF projection*. The full
embodiment parameter need not satisfy a strict tuple decomposition;
real embodied selectors may have entangled or co-determined
components that this projection coarse-grains away.

---

## 4. What SRT adds back to QRF

If SRT just inherits the QRF formalism, what does SRT contribute?

### 4.1 Non-arbitrariness of $\theta_{boundary}$

Standard QRF is *covariant*: physics looks the same in any QRF.
Frame choice is conventional.

SRT asserts:

> Bridge claim **B-E02-5**: although physics is QRF-covariant, *which
> frame an embodied selector actually occupies* is not arbitrary. It is
> determined by physical, biological, computational, and historical
> constraints on what subsystems can stably function as a reference
> frame for that selector.

In QRF terms: SRT supplies a *selection rule on $\mathcal{F}$* — not all
admissible mathematical frames are realizable embodiment frames.

This is the SRT contribution: QRF gives the geometry of the frame
bundle, SRT gives a payability constraint on which sections are
physically supportable.

### 4.2 Connection to $\Psi_f$

Bridge claim **B-E02-6**: maintaining a QRF requires resources. A frame
system must remain coherent enough to serve as a reference. The
maintenance cost is a $\Psi_f^{phys}$-style burden:
$$
\Psi_f^{phys}[\theta_{boundary}] \approx \text{cost of stabilizing the chosen frame system as a reference}.
$$
This is *not* identified with thermodynamic free energy on its own (see
E03 for the right inequality). It is a structural placement: $\Psi_f$
includes a frame-maintenance contribution.

### 4.3 Connection to the L0 / L1 / L2 mapping

Per Def-Phys-2 in `_SRT_Phys_Bridge.md`:

| SRT layer | Standard projection | QRF reading |
|---|---|---|
| $L_0$ | Hilbert space $\mathcal{H}$ | the *perspective-neutral* layer (Vanrietvelde et al. 2020) |
| $L_1$ | classical pointer states | the manifest content of $\mathcal{H}^{(\theta_{boundary})}$ for a stable frame choice |
| $L_2$ | conservation laws / symmetries | the QRF symmetry group $G$ acts as a *bridge image* of the $L_2$ invariant structure across frame choices |

Bridge claim **B-E02-7** (invariant-structure bridge): under the
QRF-compatible projection, the QRF symmetry group $G$ provides a
*bridge image* of $L_2$'s embodiment-invariant content; conservation
laws on this projection are SRT's name for "what survives every
change of $\theta_{boundary}$ in the QRF projection".

SRT does not claim that $L_2$ is exhausted by $G$. The full $L_2$
includes biological, historical, and cultural invariants that need
not have any QRF representation. This bridge is a *projection-level
identification*, not an exhaustive equation, and is therefore a
sharpening — but not an upgrade in claim strength — of T-Phys-3
("conservation from symmetry").

---

## 5. Falsifiability windows opened by E02

### 5.1 Window F-E02-α: frame-relative classicality experiments

QRF experiments (gravitational time dilation in superposition,
Belenchia–Wald-style proposals, optical-trap quantum-frame
demonstrators) are pushing toward direct laboratory tests of frame-
relative classicality. SRT's B-E02-5 predicts that the frame *actually
chosen* by an embodied apparatus is not arbitrary: changing the
apparatus's physical embedding should change which states it sees as
classical.

Falsification threshold: if a robust QRF experiment demonstrates that
the frame-relative classicality of a state is invariant under physical
reconfiguration of the apparatus's environment, SRT's
non-arbitrariness claim fails for that domain.

### 5.2 Window F-E02-β: frame-maintenance cost asymmetry

B-E02-6 predicts that different choices of $\theta_{boundary}$ have
different maintenance costs. Two frames with mathematically equivalent
QRF descriptions should differ in $\Psi_f$ when one is more thermo-
dynamically supportable than the other.

Test class: dual-rail interferometry with engineered reservoirs where
either rail can play the QRF role.

Falsification threshold: instrument calibration cost is invariant under
swap of frame role between mathematically equivalent rails.

### 5.3 Window F-E02-γ: hierarchical $\theta$ structure

B-E02-4 predicts a partial order on $\theta$. Experiments that probe
$\theta_{basis}$ before $\theta_{boundary}$ is fixed should produce
ill-defined statistics, while the reverse order should not.

Test class: weak-measurement protocols with reconfigurable bipartitions.

Falsification threshold: experiments work identically regardless of the
order in which $\theta_{boundary}$ and $\theta_{basis}$ are specified.

---

## 6. Relation to the §VI domain pressure

Per `_SRT_Phys_Bridge.md` §VI / DP-PHYS-1 (MWI challenge to Ax-P1):

E02 strengthens the SRT response to MWI. Because QRF transformations
are unitary, the QRF formalism is fully compatible with MWI: changing
$\theta_{boundary}$ in MWI does not require collapse, just a unitary
relabeling. SRT's $\hat{G}_\theta$ in MWI then becomes:

> the QRF-relative anchoring of branch content from the perspective of
> the frame system that the embodied selector occupies.

This is not a global collapse event, but neither is it a hand-wave; it
inherits the published QRF unitary structure. The collapse-family /
MWI translation note in `_SRT_Phys_Bridge.md` is therefore made more
precise by E02, without changing the language commitment.

---

## 7. What this bridge does NOT claim

1. It does **not** claim QRF experiments confirm SRT.
2. It does **not** claim $\theta_{boundary}$ is uniquely specified by
   physics; only that its admissible values are constrained.
3. It does **not** identify SRT $L_2$ with the gauge group of any
   particular field theory.
4. It does **not** turn Def-Phys-1 from bridge into theorem.
5. It does **not** modify Def-Phys-2 in
   [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md).
6. It does **not** claim that all physical perspectives are equally
   privileged; B-E02-5 explicitly says embodiment selects.

---

## 8. Promotion criteria

E02 could ascend the claim ladder only if:

1. A QRF-style experiment returns a positive frame-maintenance asymmetry
   matching SRT predictions (window F-E02-β); and
2. A canonical-registry update is performed for $\theta_{boundary}$;
   and
3. Symbol-table reconciliation is completed.

Until then, B-E02-1 through B-E02-7 stay at P3.

---

## 9. One-paragraph abstract

This bridge proposes a QRF-compatible projection of SRT's
$\theta_{boundary}$ — the Heisenberg cut parameter — onto a coset in
the quantum-reference-frame space of Giacomini–Castro-Ruiz–Brukner.
Under that projection, changes of $\theta_{boundary}$ are represented
by unitary QRF transformations, and the well-published result that
classicality is frame-relative is read as the physical content of
SRT's $L_0 / L_1$ split. SRT contributes a non-arbitrariness rule on
the projection: admissible embodiment frames lie in the subspace where
the frame system can be physically maintained as a reference, with the
physical projection of $\Psi_f$ tracking the maintenance cost. The
QRF symmetry group $G$ acts as a bridge image — not an exhaustive
equation — of $L_2$'s embodiment-invariant content. The bridge tightens
SRT's response to the multi-world challenge, gives $\theta$ a
projected hierarchical structure, and opens three falsifiability
windows tied to frame-relative classicality experiments,
frame-maintenance cost asymmetry, and the hierarchical specification
of the embodiment parameter.
