---
id: SRT-OPS-PHYSICS-P2A-QBOX-INTERFACE-EXTRACTION-2026-04-29
type: extraction_record
tags: [Operations, Physics, QBox, Hyperdecoherence, Annex, Extraction, Interface]
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/Physics_P2a_QBox_Interface_Adjudication.md
  - Physics/QBox_Annex/README.md
  - Physics/QBox_Annex/01_QBox_Hyperdecoherence_Interface.md
  - Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md
  - Physics/SRT_Physics_Claim_Status.md
machine_summary: >
  Extraction record for small-batch QBox / hyperdecoherence interface annex. Uses copy-to-annex pattern
  and does not delete or move owner hardening-note content. Operator definitions, Psi_f/d-value material,
  and positive SRT claim clusters remain owner-bound.
---

# Physics P2-A QBox Interface Extraction Record

## 0. Scope

This PR executes the small QBox interface extraction allowed by `Operations/Physics_P2a_QBox_Interface_Adjudication.md`.

Created:

- `Physics/QBox_Annex/README.md`
- `Physics/QBox_Annex/01_QBox_Hyperdecoherence_Interface.md`

Updated:

- `ANNEX_REGISTRY.md` with the QBox annex entry.

## 1. Extraction pattern

This PR uses a **copy-to-annex** pattern.

It does not delete or move original sections from:

- `Physics/SRT_Physics_Hardening_QBox_Hyperdecoherence_v0_1.md`
- `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md`

Reason: QBox material remains high-risk physics-interface content. Copy-to-annex provides a safer external interface layer while preserving the hardening note as owner context.

## 2. Extracted / copied interface material

The annex includes only low-risk material:

- source anchors;
- external concept overview;
- QBox-to-SRT proxy mapping table;
- L0-not-hidden-classical-substrate boundary;
- layered analogy;
- guardrails;
- research questions;
- public-facing paragraph.

## 3. Explicitly not moved

The following remain owner-bound:

- `G_hat_theta = selection + stabilization + access limitation` as an operator expansion;
- `Psi_f` / d-value relation section;
- `New SRT claim cluster`;
- no-go theorem bypass as SRT-support evidence;
- claims that QBox is physically established;
- claims that QBox confirms SRT.

## 4. Safety Record

- No Physics source body text deleted.
- No Physics source body text rewritten.
- No formulas changed.
- No QBox / hyperdecoherence claim promoted.
- New annex files are `canonical: false`.
- No Core / Core_Law / AI / Neuroscience / Philosophy / Public / Papers / graphify-out files touched.

## 5. Guardrails added

The QBox annex states:

- QBox does not prove SRT.
- L0 is not literally QBox.
- Hyperdecoherence is used as an analogy for access-limited effective layering unless independently established as physical reality.
- The proxy mapping table does not define SRT primitives.
- The annex does not define `L0/L1/L2`, `G_hat_theta`, `Psi_f`, d-value, quantum mechanics, or any physical law.

## 6. Next recommendation

Do not continue with gravity, constants, discrete time, or collapse/MWI synthesis.

The next safe candidate is a separate read-only adjudication for Earth accretion / reservoir-selection material, because it is already separated and can be handled as physical analogy rather than new physics proof.
