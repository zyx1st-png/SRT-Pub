---
id: SRT-PHYSICS-README
type: directory_entry
tags: [Physics, Quantum, Cosmology, Bridge, Claim-Status, Extensions, Navigation]
status: active_v1
layer: meta
epistemic_layer: bridge
claim_mode: navigation
canonical_status: non_canonical
canonical: false
date: 2026-04-30
dependency:
  - SRT-PHYS-BRIDGE
  - SRT-PHYSICS-COMPACT-REGISTRY
  - SRT-PHYSICS-CLAIM-STATUS
  - SRT-CLAIM-LADDER
  - SRT-L0-METAPHYSICS
  - SRT-PSIF-CANONICAL
  - SRT-D-VALUE-CANONICAL
  - SRT-T-DIR-CANONICAL
  - SRT-SYMBOL-TABLE
machine_summary: >
  Directory entry for SRT Physics materials. Separates bridge foundations,
  claim-status guardrails, compact registry, longform files, interface
  annexes, hardening / patch layers, and the non-canonical v0.1 Extensions
  batch. Navigation only; does not define quantum collapse, gravity, time,
  d-value, Psi_f, G_hat_theta, L0/L1/L2, T_dir, or any physical law.
---

# Physics

This directory contains SRT's physics-facing bridge, quantum, cosmology,
formalism, complexity / ontology, interface-annex, hardening, and extension
materials.

Physics is a **high-risk bridge / pressure-test domain** for SRT. Physics-domain
files may translate SRT primitives into quantum, cosmological, and
information-theoretic language, but they must not be read as experimentally
established physics unless separately supported. They must not redefine
`L_0/L_1/L_2`, `d-value`, `Psi_f`, `T_dir`, or `G_hat_theta`; those terms route
back to canonical anchors.

## Read order

1. [`SRT_Physics_Claim_Status.md`](SRT_Physics_Claim_Status.md)
   Claim-status audit for physics-domain materials. Use this before reading
   any claim about collapse, many-worlds compatibility, discrete time, gravity,
   constants, cosmology, QBox-style interface material, or extension-layer
   physics bridges.

2. [`_SRT_Phys_Bridge.md`](_SRT_Phys_Bridge.md)
   Main physics bridge layer. It uses collapse-family / anchoring language by
   default and requires explicit MWI / Everett translation notes where relevant.

3. [`PHYSICS_COMPACT_REGISTRY.md`](PHYSICS_COMPACT_REGISTRY.md)
   Compact registry and shortest reading path.

4. Compact core entries:
   - [`SRT_Quant_00_Intro_CompactCore.md`](SRT_Quant_00_Intro_CompactCore.md)
   - [`SRT_Quant_01_Selection_CompactCore.md`](SRT_Quant_01_Selection_CompactCore.md)
   - [`SRT_Quant_02_Cosmology_CompactCore.md`](SRT_Quant_02_Cosmology_CompactCore.md)
   - [`SRT_Physics_Cosmology_CompactCore.md`](SRT_Physics_Cosmology_CompactCore.md)
   - [`SRT_Phys_09_Formalism_Ext_CompactCore.md`](SRT_Phys_09_Formalism_Ext_CompactCore.md)
   - [`SRT_Phys_10_Integration_CompactCore.md`](SRT_Phys_10_Integration_CompactCore.md)
   - [`SRT_Phys_07_Complex_Systems_CompactCore.md`](SRT_Phys_07_Complex_Systems_CompactCore.md)
   - [`SRT_Phys_08_Ontology_Ext_CompactCore.md`](SRT_Phys_08_Ontology_Ext_CompactCore.md)

5. Longform counterparts:
   - [`SRT_Quant_00_Intro.md`](SRT_Quant_00_Intro.md)
   - [`SRT_Quant_01_Selection.md`](SRT_Quant_01_Selection.md)
   - [`SRT_Quant_02_Cosmology.md`](SRT_Quant_02_Cosmology.md)
   - [`SRT_Physics_Cosmology.md`](SRT_Physics_Cosmology.md)
   - [`SRT_Phys_09_Formalism_Ext.md`](SRT_Phys_09_Formalism_Ext.md)
   - [`SRT_Phys_10_Integration.md`](SRT_Phys_10_Integration.md)
   - [`SRT_Phys_07_Complex_Systems.md`](SRT_Phys_07_Complex_Systems.md)
   - [`SRT_Phys_08_Ontology_Ext.md`](SRT_Phys_08_Ontology_Ext.md)

6. Non-canonical interface annexes:
   - [`QBox_Annex/`](QBox_Annex/) — QBox / hyperdecoherence external interface layer.
   - [`Earth_Accretion_Annex/`](Earth_Accretion_Annex/) — Earth accretion / reservoir-selection external interface layer.

7. Hardening / patch layer:
   - [`_SRT_Physics_Hardening_Index.md`](_SRT_Physics_Hardening_Index.md)
   - [`patches/`](patches/)
   - [`hooks/`](hooks/)

8. Non-canonical Extensions v0.1:
   - [`Extensions/README.md`](Extensions/README.md) — quantum-instrument, QRF, information-thermodynamics, relational-time, and falsifiability bridge batch.

## Claim-status guardrails

- Collapse / measurement language is bridge language unless the claim is explicitly restricted to a collapse-family interpretation.
- MWI / Everett compatibility requires explicit translation: branch-relative anchoring is not global collapse.
- Discrete time is a hypothesis / bridge, not a derived theorem of SRT physics.
- Gravity / `Psi_f` links are weak compatibility or analogy unless a tensor-level derivation is supplied.
- Physical constants tables are structural placement constraints, not derivations of exact values.
- Holography / entanglement / d-value mappings are candidate analogies unless independently justified.
- QBox / hyperdecoherence / post-quantum references must be treated as external interface pressure-tests, not proof of SRT.
- Earth accretion / reservoir-selection references must be treated as physical analogy, not proof of SRT or evidence of agency / intention / concern.
- Extensions v0.1 files are `claim_mode: bridge`, `canonical_status: non_canonical`; they give published mathematical homes to bridge projections, not new canonical definitions.

## Current restructuring status

Physics P2 interface work is closed. See [`../Operations/Physics_P2_Interface_Closure_Report.md`](../Operations/Physics_P2_Interface_Closure_Report.md).

Current safe state:

- compact registry exists;
- main bridge exists;
- longform / compact counterparts exist;
- claim-status audit exists;
- Physics frontmatter / claim-mode normalization is complete;
- QBox interface annex exists as `canonical: false`;
- Earth accretion interface annex exists as `canonical: false`;
- Extensions v0.1 exists as a non-canonical bridge batch;
- Physics source text has not been moved during P2 copy-to-annex work.

Before any further extraction or promotion, run a new targeted adjudication for
specific files / sections.

## Paused high-risk material

Do not extract or promote the following without separate adjudication:

- collapse-dependent measurement claims;
- Everett / MWI compatibility claims;
- discrete-time / Planck-time hypotheses;
- gravity / `Psi_f` / Einstein-tensor analogies;
- physical constants and Standard Model parameter claims;
- cosmology / anthropic / multiverse claims;
- candidate empirical predictions;
- anything that would read as a new physics prediction or proof-language claim.

## Editing rule for Physics

Per [`../Governance/SRT_CANONICAL_FREEZE.md`](../Governance/SRT_CANONICAL_FREEZE.md):

- `Physics/SRT_Physics_Cosmology.md` is on the **B-list** (cross-check required, not a free-edit target).
- All other physics files in this directory are bridge / split / patch / hook / compact-core / extension layer and must not silently redefine primitives.

When in doubt, cross-check:

1. [`../_SRT_SYMBOL_TABLE.md`](../_SRT_SYMBOL_TABLE.md)
2. The relevant canonical file in `_SRT_*_CANONICAL.md` or `Core_Law/`.
3. Whether a claim is being read past its level on the claim ladder ([`../Governance/SRT_CLAIM_LADDER.md`](../Governance/SRT_CLAIM_LADDER.md)).

## Core guardrails

1. Do not promote a bridge / patch / extension claim into a canonical claim without a registry update.
2. Do not collapse `\hat{G}_\theta` into a standard quantum operator without keeping the `\theta` embodiment parameter explicit.
3. Do not collapse `Psi_f` into raw entropy, raw Fisher information, raw thermodynamic free energy, or the bridge-local `sigma_f^{phys}` proxy; the canonical anchor is [`../_SRT_PSI_F_CANONICAL.md`](../_SRT_PSI_F_CANONICAL.md).
4. Do not read H-Phys-2 (discrete time) or H-Phys-4 (gravity / friction) as physics theorems; they remain hypothesis / bridge per [`_SRT_Phys_Bridge.md`](_SRT_Phys_Bridge.md) §VI.
5. Do not infer a derivation of physical constants from the structural placement table in `_SRT_Phys_Bridge.md` §V.
6. Do not read the Extensions v0.1 provisional physics-facing HC lines as the canonical SRT hard core.

## Operations

- Pre-audit: [`../Operations/Physics_Split_Annex_PreAudit_2026-04-29.md`](../Operations/Physics_Split_Annex_PreAudit_2026-04-29.md)
- P1 closure: [`../Operations/Physics_P1_Frontmatter_Normalization_Closure_Report.md`](../Operations/Physics_P1_Frontmatter_Normalization_Closure_Report.md)
- P2 high-risk adjudication: [`../Operations/Physics_P2_High_Risk_Category_Adjudication.md`](../Operations/Physics_P2_High_Risk_Category_Adjudication.md)
- P2 closure: [`../Operations/Physics_P2_Interface_Closure_Report.md`](../Operations/Physics_P2_Interface_Closure_Report.md)

## Cross-domain links

- Canonical registry: [`../CANONICAL_REGISTRY.md`](../CANONICAL_REGISTRY.md)
- Symbol table: [`../_SRT_SYMBOL_TABLE.md`](../_SRT_SYMBOL_TABLE.md)
- d-value canonical: [`../_SRT_D_VALUE_CANONICAL.md`](../_SRT_D_VALUE_CANONICAL.md)
- `Psi_f` canonical: [`../_SRT_PSI_F_CANONICAL.md`](../_SRT_PSI_F_CANONICAL.md)
- `T_dir` canonical: [`../_SRT_T_DIR_CANONICAL.md`](../_SRT_T_DIR_CANONICAL.md)
- Claim ladder: [`../Governance/SRT_CLAIM_LADDER.md`](../Governance/SRT_CLAIM_LADDER.md)
- Edit protocol: [`../Governance/SRT_EDIT_PROTOCOL.md`](../Governance/SRT_EDIT_PROTOCOL.md)
- Cross-domain matrix: [`../_SRT_CROSS_DOMAIN_MATRIX.md`](../_SRT_CROSS_DOMAIN_MATRIX.md)
- Physics coverage index: [`../_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md`](../_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md)
