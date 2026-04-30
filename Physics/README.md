---
id: SRT-PHYSICS-README
type: directory_entry
tags: [Physics, Quantum, Cosmology, Bridge, Navigation]
status: active_v1
layer: meta
epistemic_layer: bridge
claim_mode: navigation
canonical_status: non_canonical
canonical: false
date: 2026-04-30
dependency:
  - SRT-PHYSICS-COMPACT-REGISTRY
  - SRT-PHYS-BRIDGE
  - SRT-CANONICAL-REGISTRY
  - SRT-PSIF-CANONICAL
  - SRT-D-VALUE-CANONICAL
  - SRT-T-DIR-CANONICAL
machine_summary: >
  Directory entry for SRT Physics materials. Routes readers across the existing
  physics bridge, quantum line, cosmology line, complex-systems / ontology line,
  the hardening / patches layer, and the v0.1 Extensions batch (quantum
  instrument, QRF, information thermodynamics, relational time, falsifiability
  program). Navigation only; does not define L0/L1/L2, G_hat_theta, Psi_f,
  d-value, or T_dir.
---

# Physics

This directory contains SRT's physics-facing bridge, quantum, cosmology,
formalism, complex-systems, ontology-extension, hardening, and patch
materials.

Physics is a **bridge / pressure-test domain** for SRT, not the theory's
definition engine. Physics-domain files must not redefine `L_0/L_1/L_2`,
`d-value`, `\Psi_f`, `T_dir`, or `\hat{G}_\theta`; they route those terms
back to canonical anchors.

## Read order

1. [`_SRT_Phys_Bridge.md`](_SRT_Phys_Bridge.md)
   Main physics bridge document. Treat `Axiom`, `Theorem`, `Corollary` labels
   as bridge-formalization devices unless separately promoted. Includes the
   collapse-family / MWI language commitment and the §VI domain-pressure
   audit.

2. [`PHYSICS_COMPACT_REGISTRY.md`](PHYSICS_COMPACT_REGISTRY.md)
   Current compact-core registry and shortest first-pass reading order.

3. Quantum line:
   - [`SRT_Quant_00_Intro_CompactCore.md`](SRT_Quant_00_Intro_CompactCore.md)
   - [`SRT_Quant_01_Selection_CompactCore.md`](SRT_Quant_01_Selection_CompactCore.md)
   - [`SRT_Quant_02_Cosmology_CompactCore.md`](SRT_Quant_02_Cosmology_CompactCore.md)

4. Core physics line:
   - [`SRT_Physics_Cosmology_CompactCore.md`](SRT_Physics_Cosmology_CompactCore.md)
   - [`SRT_Phys_09_Formalism_Ext_CompactCore.md`](SRT_Phys_09_Formalism_Ext_CompactCore.md)
   - [`SRT_Phys_10_Integration_CompactCore.md`](SRT_Phys_10_Integration_CompactCore.md)

5. Complexity / ontology line:
   - [`SRT_Phys_07_Complex_Systems_CompactCore.md`](SRT_Phys_07_Complex_Systems_CompactCore.md)
   - [`SRT_Phys_08_Ontology_Ext_CompactCore.md`](SRT_Phys_08_Ontology_Ext_CompactCore.md)

6. Hardening layer:
   - [`_SRT_Physics_Hardening_Index.md`](_SRT_Physics_Hardening_Index.md)
   - [`patches/`](patches/)
   - [`hooks/`](hooks/)

7. Extensions v0.1 (this batch):
   - [`Extensions/README.md`](Extensions/README.md)

## Status distinction

- `_SRT_Phys_Bridge.md`: the main physics bridge; bridge layer.
- `PHYSICS_COMPACT_REGISTRY.md`: navigation registry, not canonical.
- Compact core files (`*_CompactCore.md`): concise reading paths; not
  replacements for canonical anchors.
- Owner longforms (`SRT_Quant_*.md`, `SRT_Phys_*.md`,
  `SRT_Physics_Cosmology.md`): full domain arguments. Edit cautiously and
  cross-check `_SRT_SYMBOL_TABLE.md` and the relevant canonical files.
- `Cosmology_Split/` and `Formalism_Ext_Split/`: long-form reading aids only;
  not independent canonical entries.
- `patches/` and `hooks/`: external-material patch notes and integration
  hooks; bridge layer; do not modify primitives.
- `Extensions/`: v0.1 academic-formalism bridge batch (this round). All
  files are `claim_mode: bridge`, `canonical_status: non_canonical`.

## Editing rule for Physics

Per [`../Governance/SRT_CANONICAL_FREEZE.md`](../Governance/SRT_CANONICAL_FREEZE.md):

- `Physics/SRT_Physics_Cosmology.md` is on the **B-list** (cross-check
  required, not a free-edit target).
- All other physics files in this directory are bridge / split / patch /
  hook / compact-core / extension layer and must not silently redefine
  primitives.

When in doubt, cross-check:

1. [`../_SRT_SYMBOL_TABLE.md`](../_SRT_SYMBOL_TABLE.md)
2. The relevant canonical file in `_SRT_*_CANONICAL.md` or `Core_Law/`.
3. Whether a claim is being read past its level on the claim ladder
   ([`../Governance/SRT_CLAIM_LADDER.md`](../Governance/SRT_CLAIM_LADDER.md)).

## Core guardrails

1. Do not promote a bridge / patch / extension claim into a canonical claim
   without a registry update.
2. Do not collapse `\hat{G}_\theta` into a standard quantum operator
   without keeping the `\theta` embodiment parameter explicit.
3. Do not collapse `\Psi_f` into raw entropy, raw Fisher information, or raw
   thermodynamic free energy; the canonical anchor is
   [`../_SRT_PSI_F_CANONICAL.md`](../_SRT_PSI_F_CANONICAL.md).
4. Do not read H-Phys-2 (discrete time) or H-Phys-4 (gravity / friction) as
   physics theorems; they remain hypothesis / bridge per
   [`_SRT_Phys_Bridge.md`](_SRT_Phys_Bridge.md) §VI.
5. Do not infer a derivation of physical constants from the structural
   placement table in `_SRT_Phys_Bridge.md` §V.

## Cross-domain links

- Canonical registry: [`../CANONICAL_REGISTRY.md`](../CANONICAL_REGISTRY.md)
- Symbol table: [`../_SRT_SYMBOL_TABLE.md`](../_SRT_SYMBOL_TABLE.md)
- d-value canonical: [`../_SRT_D_VALUE_CANONICAL.md`](../_SRT_D_VALUE_CANONICAL.md)
- `\Psi_f` canonical: [`../_SRT_PSI_F_CANONICAL.md`](../_SRT_PSI_F_CANONICAL.md)
- `T_dir` canonical: [`../_SRT_T_DIR_CANONICAL.md`](../_SRT_T_DIR_CANONICAL.md)
- Claim ladder: [`../Governance/SRT_CLAIM_LADDER.md`](../Governance/SRT_CLAIM_LADDER.md)
- Edit protocol: [`../Governance/SRT_EDIT_PROTOCOL.md`](../Governance/SRT_EDIT_PROTOCOL.md)
- Cross-domain matrix: [`../_SRT_CROSS_DOMAIN_MATRIX.md`](../_SRT_CROSS_DOMAIN_MATRIX.md)
- Physics coverage index: [`../_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md`](../_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md)
