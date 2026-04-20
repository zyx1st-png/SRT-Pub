---
id: SRT-CORE-21
type: index
tags: [Formal logic, Axioms, Claim Ladder, Index]
status: active_v3
layer: L1
epistemic_layer: os
claim_mode: mixed_index
dependency: [SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CORE-21C-BRIDGE-HYPOTHESES, SRT-CLAIM-LADDER]
---

# SRT Core Definition 21: Formal Axioms Index

> **Role change (2026-04-20)**: This file is no longer the mixed "all formal axioms in one layer" body.
> It is now the index for the split Core 21 claim layers.

## Why This Split Exists

The former hybrid `Core_21` placed primitive axioms, constitutive theorems, canonical interpretations, bridge mappings, and empirical threshold claims in one apparent axiom track. That made lower-hardness propositions look as if they were P0/P1 core.

The new structure separates **file role** from **claim hardness**:

- a file can be canonical without every statement inside it being P0;
- a bridge claim can be valuable without becoming an axiom;
- a lab threshold can guide research without defining the core.

Claim-level rules are now governed by:

- `Governance/SRT_CLAIM_LADDER.md`

---

## Current Core 21 Layers

| Layer | File | Claim level | Role |
|---|---|---:|---|
| Minimal axioms | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 | Primitive axioms only |
| Constitutive theorems | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 | Theorems internal to SRT once P0 is granted |
| Bridge hypotheses | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3/P4 | Canonical interpretations, cross-domain mappings, empirical thresholds |

**Default citation rule**:

- cite primitive axioms from `Core/SRT_Core_21_Minimal_Axioms.md`;
- cite stable ISP, real choice moment, anti-closure asymmetry, ontological time, and `L_2` downward constraint from `Core/SRT_Core_21b_Constitutive_Theorems.md`;
- cite fitness, assembly, holography, universality, Fisher-geometry `\Psi_f`, and strong information-creation unification from `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

---

## Legacy Numbering Map

| Former Core 21 item | New home | Current level |
|---|---|---:|
| `Ax-F-01` Primacy of Selection | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 |
| `Ax-F-02` Existence as Anchoring | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 |
| `Ax-F-03` Causality as Projection | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| `Ax-F-03b` Spacetime as Memory Horizon | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| `Ax-F-04` Information-Existence Equivalence | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3 |
| `Ax-F-05` Fitness Beats Truth | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3/P4 |
| `Ax-F-06` Assembly Criterion | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P4 |
| `Ax-F-07` Holographic Duality | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3/P4 |
| `Ax-F-08` Topological Normativity | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3 |
| `Ax-F-09` Scale Consistency | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3 |
| `Ax-F-10` Downward Causation Constraint | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| `Ax-F-11` Ghost Operator Universality | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3 |
| `Ax-F-12` `\Psi_f` as Generative Principle | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3 |
| `Ax-F-13` Selection-Information Creation Equivalence | `Core/SRT_Core_21b_Constitutive_Theorems.md` for minimal theorem; `Core/SRT_Core_21c_Bridge_Hypotheses.md` for strong unification | P1 / P2-P3 |
| `T-ε-Constitute` | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| Part B `A1-A5` minimal table | split across P0/P1/P3 according to claim role | mixed |
| Part B assembly / deep time notes | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3/P4 |

---

## What Did Not Change

This split does **not** change the intended meaning of:

- selection primacy;
- existence as anchoring;
- `L_2` as convergence / constraint;
- `\Psi_f` as ontological friction;
- `d-value` as canonical stake-coupled concern;
- the stable ISP anti-closure theorem.

It changes the **epistemic rank** and citation behavior of mixed claims.

---

## What Must No Longer Happen

- Do not cite this file as if it contains the full axiom body.
- Do not cite bridge claims such as fitness beats truth, holographic duality, assembly thresholds, or ghost-operator universality as P0/P1.
- Do not use `D_eff` as the canonical definition of d-value. Use `_SRT_D_VALUE_CANONICAL.md`.
- Do not use `Core_21c` empirical or bridge claims to override `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, `_SRT_T_DIR_CANONICAL.md`, or `Core_Law/SRT_L0_Metaphysics.md`.

---

## Minimal Reading Path

For a core-theory pass, read:

1. `Core/SRT_Core_21_Minimal_Axioms.md`
2. `Core/SRT_Core_21b_Constitutive_Theorems.md`
3. `Core/SRT_Core_22_Equations.md`
4. `Core/SRT_Core_21c_Bridge_Hypotheses.md` only when bridge or hypothesis material is needed

For claim governance, read:

1. `Governance/SRT_CLAIM_LADDER.md`
2. `Governance/SRT_EDIT_PROTOCOL.md`
3. `Governance/SRT_CANONICAL_FREEZE.md`
