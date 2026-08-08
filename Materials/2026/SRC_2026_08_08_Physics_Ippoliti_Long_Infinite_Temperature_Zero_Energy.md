---
source_id: SRC-2026-08-08-PHYSICS-IPPOLITI-LONG-INFINITE-TEMPERATURE-ZERO-ENERGY
title: "Infinite Temperature at Zero Energy"
source_type: peer_reviewed_primary_theory_full_text
source_url: "https://journals.aps.org/prx/abstract/10.1103/tvny-gtzp"
arxiv: "2509.04410"
doi: "10.1103/tvny-gtzp"
authors: "Matteo Ippoliti; David M. Long"
publication: "Physical Review X 16, 031030 (2026)"
date_published: "2026-08-07"
date_added: "2026-08-08"
evidence_level: peer_reviewed_primary_full_text
reliability_level: high_for_stated_mathematical_construction_and_proved_properties; bridge_only_for_srt_interpretation
content_access: "APS open-access article plus arXiv version; close-read of construction, ETH/entanglement argument, and discussion"
domain: physics_quantum_manybody_floquet_eth_entanglement_computation
srt_relevance: high
integration_priority: high
related_srt_claims:
  - state_coordinate_insufficiency
  - observable_access_algebra
  - history_representation_vs_sedimentation
  - local_rule_global_state_complexity
  - mechanism_criterion_separation
  - L2_irreversible_trace_guard
  - physics_bridge_claim_hygiene
tags:
  - quantum_many_body
  - floquet
  - eigenstate_thermalization
  - feynman_kitaev
  - history_state
  - volume_law_entanglement
  - LFSR
  - access_algebra
  - state_coordinates
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-08-08-PHYSICS-IPPOLITI-LONG-INFINITE-TEMPERATURE-ZERO-ENERGY
---

# SourceCard: Ippoliti & Long, *Infinite Temperature at Zero Energy* (2026)

## 1. One-line summary

Ippoliti and Long construct static, geometrically local Hamiltonians whose eigenstates inherit infinite-temperature-like properties from periodically driven systems, including volume-law entanglement across the spectrum and in the ground state; for SRT, the strongest use is a hardening case showing that energy position, eigenvector structure, accessible observable algebra, dynamical origin, and irreversible historical sedimentation must not be collapsed into one descriptor.

## 2. Bibliographic anchor

```text
Matteo Ippoliti and David M. Long
Infinite Temperature at Zero Energy
Physical Review X 16, 031030 (2026)
Published 7 August 2026
DOI: 10.1103/tvny-gtzp
arXiv: 2509.04410
```

The APS version is open access and peer reviewed. The paper was accepted 16 June 2026 and published 7 August 2026.

## 3. Core claims of the source

The following are source-level claims/results, not SRT claims.

1. A periodic-boundary-condition variant of the Feynman-Kitaev clock maps periodically driven (Floquet) eigenstates into eigenstates of a static Hamiltonian.
2. The construction can be made geometrically local rather than remaining only an abstract circuit-to-Hamiltonian mapping.
3. If the input Floquet circuit satisfies eigenstate thermalization at infinite temperature, the resulting static Hamiltonian inherits corresponding local eigenstate properties.
4. These inherited properties include extensive / volume-law entanglement across the spectrum, including the ground-state sector.
5. The construction can place a chosen Floquet eigenstate at zero energy by an appropriate phase twist in the periodic clock.
6. The paper also supplies an exactly solvable family of Floquet circuits based on linear-feedback-shift-register structure for which the relevant ETH behavior is proved rather than merely assumed.
7. Combining the two constructions yields local Hamiltonians with provably volume-law-entangled ground states; the authors identify this as the first such construction where the volume law holds for all contiguous subsystems in the stated regime.
8. The construction separates properties that are often strongly correlated in generic many-body systems: spectral position, entanglement structure, thermal-looking local reduced states, dynamical generation, and conventional chaos/equilibration diagnostics.

## 4. Mechanism sketch

### 4.1 Periodic Feynman-Kitaev history encoding

For a circuit sequence `u_t`, the ordinary FK history-state idea encodes successive circuit states together with a clock register. Imposing periodic clock boundary conditions forces consistency after a full cycle and therefore selects Floquet eigenstates:

```text
periodic clock closure
-> full-cycle consistency
-> Floquet eigenphase condition
-> static Hamiltonian eigenstate
```

The important structural point is that the Hamiltonian can enforce local transition consistency without containing the entire global history as one nonlocal rule.

### 4.2 Spectral structure versus inherited spin structure

Within a fixed Floquet sector, the clock problem reduces to a simple hopping/spectral problem, while the spin-sector eigenvector can carry the high-entanglement / ETH structure. This makes the paper an unusually clean example in which:

```text
where a state sits in a constructed spectrum
!=
all of the state's internal relational / entanglement structure
```

### 4.3 Exact thermal-looking input circuits

The LFSR-based Floquet construction is valuable because it turns the main result from a purely conditional statement (`if ETH holds`) into an explicit family where the relevant eigenstate property can be controlled analytically.

## 5. Evidence and method

Evidence type:

- analytic construction;
- local-Hamiltonian mapping;
- exact spectral reduction in the clock sectors;
- ETH matrix-element analysis;
- entanglement lower bounds;
- exact / finite-field analysis for the LFSR family.

This is not an experimental paper. Its evidential strength lies in the explicit mathematical construction and proof of the claimed model properties.

## 6. Main limits

1. The result does **not** mean a thermodynamic system is literally at `T = 0` and `T = infinity` in one undifferentiated sense.
2. `Zero energy` refers to spectral position in the constructed static Hamiltonian; `infinite-temperature-like` refers to selected eigenstate/local-observable properties inherited from the Floquet sector.
3. The construction is deliberately engineered and does not show that generic low-energy ground states have infinite-temperature structure.
4. Standard gapped-area-law intuition is not simply overturned; the relevant constructions evade its premises rather than falsifying the theorem.
5. Volume-law entanglement is not identical to SRT `d-value`, `Psi_f`, `L_2`, selection, consciousness, agency, or ontological depth.
6. A Feynman-Kitaev history state is a coherent encoding of a trajectory. By itself it does not establish irreversible historical trace or future-path rewriting.
7. Access-dependent effective descriptions do not imply that physical reality is subjective or observer-created.
8. ETH, equilibration, ergodicity, random-matrix spectral statistics, and generic quantum chaos should not be treated as interchangeable labels merely because they often co-occur.

## 7. SRT relevance: surviving interfaces

### 7.1 State-coordinate insufficiency

The paper supplies a sharp physics case against treating one successful scalar coordinate as a sufficient description of a state's structure:

```text
energy position
!= entanglement structure
!= local reduced-state structure
!= dynamical origin
```

SRT-safe use:

> A physical bridge should state which descriptor is being used and should not infer the complete relational organization of a state from one coordinate merely because the variables are tightly correlated in generic models.

### 7.2 Observable / access-algebra qualification

The construction supports a disciplined distinction between a global state and what different restricted operator sets can stably read from it. Spin-local observables can inherit infinite-temperature-like values while clock-sensitive correlations retain information that distinguishes the static Hamiltonian's low-energy structure.

SRT-safe use:

> Effective state descriptions should be indexed to the declared accessible observables or subsystem algebra; this is an operational qualification, not a claim that observers create the underlying state.

### 7.3 History representation versus history sedimentation

The periodic FK construction shows that a dynamical trajectory can be re-encoded as constraints inside a static state:

```text
dynamical history
-> static relational encoding
```

But SRT canonical `L_2` requires more than representation. P0-03 requires irreversible trace: a selection that has occurred cannot be treated as never having occurred, and reversal is itself a new event.

Therefore:

```text
history represented in a state
!= history-dependent future accessibility
!= irreversible L2 sedimentation
```

The paper is strongest here as a negative-control / boundary case.

### 7.4 Criterion versus mechanism separation

The LFSR construction is a useful methodological warning that satisfying a high-level criterion does not uniquely identify the generating mechanism. For SRT this supports an audit rule:

```text
same diagnostic output
!= same mechanism
!= same causal architecture
!= same ontological interpretation
```

### 7.5 Local rules versus global state complexity

A geometrically local Hamiltonian can support globally extensive entanglement. Therefore local simplicity does not entail global relational simplicity.

SRT-safe use:

> Do not infer the complexity or ontological depth of admissible global structures directly from the apparent simplicity or locality of the rule grammar that constrains them.

## 8. Reverse correction / pressure on SRT

The paper pressures five overstatements that SRT physics should avoid:

1. `low energy -> simple state` as a conceptual necessity;
2. `history encoded -> L_2 established`;
3. `observable-dependent effective description -> subjective reality`;
4. `ETH -> chaos/equilibration/mechanism uniquely identified`;
5. `local rule -> simple global organization`.

The strongest surviving correction is methodological rather than ontological.

## 9. Suggested patch target

Primary patch:

```text
Physics/patches/SRT_Phys_THERM01_State_Coordinate_Access_Algebra_History_Guard_v0_1.md
```

Future synthesis target:

```text
Physics/_SRT_Phys_Bridge.md
```

or a later versioned physics synthesis if/when `Physics/SRT_Physics_Bridge_v0_2.md` is created.

## 10. Pipeline 1 adjudication

```text
Verdict: A -- bounded non-canonical P3 physics hardening bridge
Evidence: peer-reviewed primary theoretical result
Canonical writeback: none
Physics-body writeback: none in this pass
```

Reason for A:

- primary peer-reviewed source with a precise mathematical construction;
- clear incremental hardening value beyond existing quantum measurement / representation patches;
- surviving claims can be stated without identifying external variables with SRT primitives;
- directly useful as a negative-control case for `L_2`, access, and mechanism-criterion separation.

## 11. Boundary statement

This source is **not** evidence that SRT is true, that energy is unreal, that temperature is observer-created, that entanglement is `d-value`, or that reversible history-state encoding supplies the irreversible trace required by canonical `L_2`. Its proper role is to harden SRT's distinctions among state coordinates, access algebras, generative mechanisms, and historically consequential constraint sedimentation.
