---
id: SRT-OPS-PHYSICS-P2B-EARTH-ACCRETION-INTERFACE-EXTRACTION-2026-04-29
type: extraction_record
tags: [Operations, Physics, Earth-Accretion, Reservoir-Selection, Annex, Extraction, Interface]
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Operations/Archive_Records/Physics_P2b_Earth_Accretion_Interface_Adjudication.md
  - Physics/Earth_Accretion_Annex/README.md
  - Physics/Earth_Accretion_Annex/01_Reservoir_Selection_Interface.md
  - Physics/SRT_Physics_Hardening_Earth_Inner_Solar_System_Accretion_v0_1.md
  - Physics/SRT_Physics_Claim_Status.md
machine_summary: >
  Extraction record for small-batch Earth accretion / reservoir-selection interface annex. Uses copy-to-annex pattern
  and does not delete or move owner hardening-note content. Psi_f, d-value, formal bridge model, and positive SRT claim clusters remain owner-bound.
---

# Physics P2-B Earth Accretion Interface Extraction Record

## 0. Scope

This PR executes the small Earth accretion / reservoir-selection interface extraction allowed by `Operations/Archive_Records/Physics_P2b_Earth_Accretion_Interface_Adjudication.md`.

Created:

- `Physics/Earth_Accretion_Annex/README.md`
- `Physics/Earth_Accretion_Annex/01_Reservoir_Selection_Interface.md`

Updated:

- `ANNEX_REGISTRY.md` with the Earth accretion annex entry.

## 1. Extraction pattern

This PR uses a **copy-to-annex** pattern.

It does not delete or move original sections from:

- `Physics/SRT_Physics_Hardening_Earth_Inner_Solar_System_Accretion_v0_1.md`
- `Physics/SRT_Physics_Bridge_Integration_Hooks_for_QBox_EarthAccretion.md`

Reason: Earth accretion material remains physics-interface content. Copy-to-annex provides a safer external interface layer while preserving the hardening note as owner context.

## 2. Extracted / copied interface material

The annex includes only low-risk material:

- source anchors;
- external cosmochemistry summary;
- reservoir-selection / accessibility-limitation analogy;
- proxy mapping table;
- volatile-boundary problem;
- boundary cautions;
- public-facing paragraph;
- one-paragraph abstract.

## 3. Explicitly not moved

The following remain owner-bound:

- `Psi_f` relation section;
- d-value relation section;
- New SRT claim cluster;
- formal bridge model unless separately simplified and adjudicated;
- claims that Earth accretion proves SRT;
- claims that planetary formation involves agency, intention, concern, or choice.

## 4. Safety Record

- No Physics source body text deleted.
- No Physics source body text rewritten.
- No formulas changed.
- No Earth accretion / cosmochemistry claim promoted.
- New annex files are `canonical: false`.
- No Core / Core_Law / AI / Neuroscience / Philosophy / Public / Papers / graphify-out files touched.

## 5. Guardrails added

The Earth accretion annex states:

- Earth accretion does not prove SRT.
- Planetary accretion is not agency, intention, concern, or choice.
- Reservoir selection is used as a physical analogy for accessibility-limited selection.
- d-value should not be projected onto prebiotic planetary formation.
- `Psi_f` should not be locally defined as a planetary equation.
- The proxy mapping table does not define SRT primitives.

## 6. Next recommendation

Pause Physics interface extraction after this PR unless a new read-only adjudication is prepared.

Do not continue with gravity, constants, discrete time, or collapse/MWI synthesis.

A good next move is a Physics P2 closure report summarizing QBox + Earth accretion extractions and freezing remaining high-risk topics.
