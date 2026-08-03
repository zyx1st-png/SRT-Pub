---
id: SRT-PHYS-REP01-REPRESENTATION-COVARIANCE-COMPOSITION
type: hardening_patch
tags: [Physics, Quantum Foundations, Representation Covariance, Complex Numbers, Real Quantum Mechanics, Composite Systems, Tensor Product, Empirical Equivalence, Bridge]
status: active_v0_1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3
canonical_status: non_canonical
canonical: false
date: 2026-08-03
source_ids:
  - SRC-2026-08-03-PHYSICS-REAL-QUANTUM-REPRESENTATION-COMPOSITION
dependency:
  - Physics/SRT_Physics_Claim_Status.md
  - Physics/SRT_Quant_00_Intro_CompactCore.md
  - Physics/SRT_Quant_01_Selection_CompactCore.md
  - Physics/_SRT_Physics_Hardening_Index.md
  - Core_Law/SRT_L0_Metaphysics.md
  - _SRT_SYMBOL_TABLE.md
  - Governance/SRT_CLAIM_LADDER.md
machine_summary: >
  Non-canonical P3 physics hardening patch derived from real-valued reformulations
  of quantum mechanics. Introduces a representation-covariance guard: an SRT
  physics bridge should assign the same core interpretation to presentations
  that preserve empirical probabilities, local operations, composition, and
  physical equivalence relations. Separates the number field from the full
  theory package, treats composite-system rules as substantive rather than
  neutral notation, and prevents complex Hilbert space, the visible symbol i,
  or one matrix realization of tensor products from being identified with L0
  or with canonical SRT primitives. No canonical or established-physics claim.
---

# SRT Physics REP01: Representation Covariance and Composition Guard

> **Status**: non-canonical P3 physics bridge / hardening guard.  
> **Source anchor**: Quanta Magazine's 2025 synthesis, Barrios Hita et al. (`arXiv:2503.17307`; *Physical Review Letters* 136, 240202), Hoffreumon and Woods (`arXiv:2504.02808v2`), and the 2021 *Nature* comparator (`10.1038/s41586-021-04160-4`).  
> **Boundary**: this patch does not prove real-number ontology, refute complex quantum mechanics, solve measurement, or confirm SRT.

## 0. Adjudication

Pipeline 1 verdict:

```text
A -- bounded non-canonical physics bridge
```

Reason:

- there is a stable primary-source result, now including one peer-reviewed 2026 paper;
- the result creates a new hardening constraint for SRT quantum language;
- the constraint can be stated without promoting the external theory into SRT ontology;
- the principal value is a representation and composition guard, not a new physical prediction.

## 1. The narrow external result

The external result should be stated as a comparison between theory packages, not between bare number fields.

The 2021 network argument fixed a package approximately of the form:

```text
real Hilbert spaces
+ standard state/measurement postulates
+ a specified tensor-product composition rule
+ independent-source assumptions
```

Within that package, real and complex formulations produce different network correlations, and experiments rejected the restricted real package.

The later constructions modify the representation of composite systems while retaining physically motivated locality or representation-locality conditions. They reproduce the statistics of standard complex quantum mechanics using only real numbers.

Therefore:

```text
restricted real package falsified
!= every possible real-valued formulation falsified
```

and:

```text
complex formulation empirically successful
!= complex number field uniquely established as ontology
```

## 2. Why this matters for SRT

SRT begins from a pre-objectification question and then allows mathematical and scientific descriptions at later layers. That ordering creates a responsibility: SRT must not mistake the visible objects of one successful formalism for the unique constituents of the pre-object field.

Real-valued quantum reformulations provide a sharp pressure case because the following can change:

- the scalar field used in the presentation;
- the dimension of the representing space;
- the matrix realization of composition;
- the location of phase information;
- the equivalence relation on state vectors;

while the following are preserved:

- observable probabilities;
- local physical operations;
- multipartite predictions;
- operational indistinguishability;
- the phase/rotation structure in an alternative encoding.

The SRT bridge should track the preserved structure unless it supplies a genuine empirical discriminator.

## 3. Main bridge claim: representation covariance

### REP01-C1 -- Representation-covariance guard

Let two presentations `R1` and `R2` be equivalent for the purpose of an SRT physics bridge when a translation between them preserves:

1. observable probability assignments;
2. admissible local operations;
3. the physical composition of independent subsystems;
4. the equivalence relations that identify physically indistinguishable states;
5. the relevant empirical predictions.

Bridge-level schema:

```text
R1 ~emp+comp R2
  ->
B_SRT(R1) = B_SRT(R2)
```

where `B_SRT` is the SRT bridge interpretation, not a canonical mathematical function.

Meaning:

> An SRT physics claim must not change merely because an empirically and compositionally equivalent formulation moves information from complex coefficients into real flags, quotient classes, rotations, or an alternative matrix representation of the tensor product.

This is a P3 methodological bridge, not a theorem of physics or a new canonical SRT axiom.

## 4. Composition is part of the theory package

### REP01-C2 -- Composition-rule dependence

A physical theory is not specified by a number field alone. For this purpose, use the bridge tuple:

```text
T = (state spaces, operations, composition, equivalence, readout probabilities)
```

The 2021/2025-2026 sequence shows that changing the composition or representation component can alter whether a real formulation is inconsistent or empirically equivalent.

SRT consequence:

> The rule by which two candidate systems become one composite system is a substantive constraint on object formation and relation, not a neutral bookkeeping convention.

This does not mean that SRT has derived the correct quantum composition rule. It means that SRT quantum writing must name which composition package is being interpreted before drawing ontological conclusions.

## 5. Mapping table

| External structure | Safe SRT bridge use | Forbidden identity |
|---|---|---|
| explicit complex coefficient / `i` | compact representation of phase-rotation structure | `i = L_0` or complex number = latent reality substance |
| real flag / `SO(2)` rotation | alternative encoding that preserves complex-like structure | flag = selector or `G_hat_theta` |
| global-phase equivalence | example of physically meaningful equivalence classes exceeding raw vector identity | global phase = SRT ontological selection |
| quotient-space composite construction | evidence that composite-state representation is a substantive theory choice | quotient space = absolute SRT composition law |
| alternative tensor-product matrix representation | warning that a familiar representation is not automatically the unique physical rule | standard Kronecker product = canonical ontology |
| empirical equivalence of real and complex presentations | underdetermination of ontology by the tested observables | all mathematical formulations are equally explanatory |
| 2021 network discrimination | valid test of a restricted postulate package | experiment directly proved the ontological reality of complex numbers |

## 6. Correction pressure on existing SRT quantum shorthand

This patch does not directly edit the current quantum owner files. It records the constraints for a later controlled synthesis.

### 6.1 Wavefunction caution

Current shorthand such as:

```text
wavefunction = L0 possibility structure
```

must be read as a bridge abbreviation. Safer future prose:

```text
the wavefunction is one physical-mathematical representation of an accessible
possibility structure; it is not identical to absolute L0.
```

### 6.2 Selection operator caution

A quantum-facing `G_hat_theta` bridge cannot depend on whether the chosen presentation visibly contains `i`. If the proposed mechanism cannot be translated into an empirically equivalent real presentation, the proposal is representation-dependent and requires demotion or an explicit discriminator.

### 6.3 Entanglement and factorization caution

Statements such as "entanglement means L0 has not factorized" must specify:

- the state-space representation;
- the composition rule;
- the relevant notion of separability or equivalence;
- which feature is invariant across equivalent presentations.

A failure of factorization in one raw representation is not automatically an invariant ontological fact.

### 6.4 Hilbert-space caution

Complex Hilbert space, real Hilbert space, quotient space, configuration space, and path-integral domain remain candidate physical projections or formal scaffolds. None is licensed by this material as an identity with absolute `L_0`.

## 7. New bounded claim cluster

### REP01-C1 -- Representation covariance

An SRT physics bridge should remain invariant under empirically and compositionally equivalent reformulations.

### REP01-C2 -- Composition-rule dependence

Ontological conclusions about a theory cannot be attributed to its number field while silently fixing a non-unique representation of composite systems.

### REP01-C3 -- Scaffold / invariant distinction

A mathematically natural object may be an optimal compression of invariant relational structure without being a primitive ontological substance.

### REP01-C4 -- Theory-package targeting

Experiments test a bounded package of states, operations, composition, equivalence, independence, and readout assumptions. Public claims must name the package rather than announcing that a bare mathematical object has been proved or disproved.

All four claims are P3 hardening statements. None is P0/P1 or established physics beyond the cited primary results.

## 8. Formal audit protocol

For any SRT quantum claim `Q`, perform the following representation audit:

1. **Presentation**: identify whether `Q` is stated in complex-Hilbert, real-Hilbert, path-integral, algebraic, or another language.
2. **Translation**: translate the relevant states, operations, equivalences, and composition rule into an empirically equivalent presentation when available.
3. **Invariance**: ask whether the SRT interpretation survives the translation.
4. **Artifact test**: if `Q` disappears only because the symbol `i`, a matrix block, or a chosen tensor representation disappears, classify it as a representation artifact.
5. **Discriminator gate**: promote a representation-specific claim only when it yields a stated empirical difference not removed by equivalent reformulation.

Compressed test:

```text
survives equivalent reformulation
  -> candidate structural bridge

depends on notation only
  -> representation artifact

differs empirically
  -> specify discriminator and tested package
```

## 9. Operational consequences

This patch supplies an immediate repository audit rather than a new laboratory experiment.

### 9.1 Quantum-file audit

Search physics files for statements that identify:

- `L_0` with complex Hilbert space;
- `G_hat_theta` with an explicitly complex operation;
- entanglement with raw nonfactorization absent a composition qualifier;
- standard tensor/Kronecker representation with ontological composition;
- experimental use of complex numbers with proof of complex ontology.

### 9.2 Cross-formulation robustness test

For each future SRT quantum model, require a short note answering:

```text
What is invariant if the model is realified or expressed in another equivalent formalism?
```

### 9.3 Failure condition

REP01 adds no independent physical content if all it does is repeat the generic statement that coordinates are conventional. Its SRT value survives only if it improves concrete quantum claims by separating:

```text
representation choice
from
composition / equivalence / operation invariants
```

## 10. Boundary cautions

Do not claim:

- quantum mechanics has eliminated imaginary numbers in every meaningful sense;
- the real formulation is ontologically preferred;
- the 2021 experiment was erroneous rather than scope-limited;
- empirical equivalence implies explanatory equivalence;
- every mathematical structure is merely conventional;
- complex phase structure has disappeared;
- the cited work confirms `L_0`, selection ontology, collapse, or SRT.

Preserve:

```text
explicit i removable
!= complex-like relational structure removable

representation non-uniqueness
!= absence of objective structure

empirical equivalence
!= equal simplicity / naturalness / explanatory value
```

## 11. Integration target

Primary future target:

```text
Physics/SRT_Physics_Bridge_v0_2.md
```

Suggested insertion:

```text
Representation covariance and composite-system guard
```

Possible later owner-file cautions:

- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Physics_Claim_Status.md`

Do not directly edit canonical files from this patch.

## 12. One-paragraph abstract

Real-valued reformulations of quantum mechanics show that the explicit use of complex numbers is not uniquely forced by observable statistics once the representation of composite systems is handled differently. For SRT, the durable lesson is not that reality is real-numbered, but that a physics bridge must distinguish representation from invariant structure and must treat composition, physical equivalence, local operations, and readout rules as part of the tested theory package. REP01 therefore introduces a non-canonical representation-covariance guard: SRT interpretations should survive empirically and compositionally equivalent reformulations, while claims that depend only on visible complex notation, one matrix representation of tensor products, or a direct identification of Hilbert space with `L_0` must be demoted as representation artifacts unless they supply an independent empirical discriminator.
