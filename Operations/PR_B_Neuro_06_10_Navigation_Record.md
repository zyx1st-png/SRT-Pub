---
id: SRT-OPS-PR-B-NEURO-06-10-NAV-2026-04-28
type: audit_record
tags:
  - Operations
  - Navigation
  - Neuroscience
  - PR-B
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-28
reference_audit: Operations/PR_A2_Neuroscience_06_10_Audit.md
machine_summary: >
  Navigation-only record for adding Current Reading Map, Dependency Map,
  Companion Links, and Refactor Notes blocks to Neuroscience 06-10.
  No formulas, frontmatter, theory content, sections, or Annex directories
  were changed.
---

# PR-B: Neuroscience 06-10 Navigation Record

**Date**: 2026-04-28
**Scope**: Navigation-only additions to the five files audited in [`Operations/PR_A2_Neuroscience_06_10_Audit.md`](PR_A2_Neuroscience_06_10_Audit.md).

## Files Modified

- `Neuroscience/SRT_Neuro_06_Field_Effects.md`
- `Neuroscience/SRT_Neuro_07_Evo_Devo.md`
- `Neuroscience/SRT_Neuro_08_Immune_Dist.md`
- `Neuroscience/SRT_Neuro_09_Integ_Eq.md`
- `Neuroscience/SRT_Neuro_10_Advanced_Models.md`

## Navigation Blocks Added

Each file received the same navigation-only block family before Part A:

- `## Current Reading Map`
- `## Dependency Map`
- `## Companion Links`
- `## Refactor Notes (PR-B: navigation-only)`

These blocks summarize owner-file dependencies, bridge/interface areas, empirical anchors, companion links, and PR-D extraction cautions. They do not redefine any SRT claim.

## Safety Record

- No formulas changed.
- No frontmatter changed.
- No `claim_mode`, `canonical`, `status`, `layer`, or `epistemic_layer` fields changed.
- No theory content changed.
- No sections moved.
- No content deleted.
- No Annex directory created.
- No `Neuroscience_Annex/` directory created.
- No CompactCore file touched.
- No `Core/`, `Core_Law/`, `AI/`, `Philosophy/`, `Public/`, `Papers/`, or `graphify-out/` file touched.
- SRT-NEURO-08 AD/Tanycyte interface equations were not changed.
- SRT-NEURO-09 Def-Phi-Unity, Ax-CLIN-1b, and BioQuantum sections were not changed.
- SRT-NEURO-10 Ax-ADV-2 Feeling-as-Friction and T1 tension resolution were not changed.

## Future PR-D Candidate Summary

| File | PR-D candidate summary | Extraction readiness |
|---|---|---|
| `SRT_Neuro_06_Field_Effects.md` | Part B §2 synaptic/GWT/IIT and §6 GRT. QUALIA-1/2, Ax-FIELD-1, Def-Ephaptic-Binding, T-FIELD-2, `κ_sync`, `Ĝ_macro`, and H-Field predictions stay in owner. GRT deduplication with 07 §6 required. | Medium |
| `SRT_Neuro_07_Evo_Devo.md` | §3.2 Levin interface, §5 convergent evolution, §6 GRT, §8 Waddington. BIO-1 through EVO-3, Evo-Devo Bridge Note, `Ĝ_devo`, `L2^bioelectric`, Genome-as-Generative-Model, and H-Evo predictions stay in owner. GRT deduplication with 06 §6 required. | Medium |
| `SRT_Neuro_08_Immune_Dist.md` | Lowest extraction readiness. Possible future interface review for §2 PNI/gut-brain/embodied cognition, §4 Varela history, and §5 inflammation-depression. AD/Tanycyte sections require human boundary decision before extraction. | Low |
| `SRT_Neuro_09_Integ_Eq.md` | Highest extraction readiness. §1 Babel Tower, §2 absorption table, §3 anti-neuromania defense, and §4 panpsychism comparison are future Annex candidates. Def-Phi-Unity, Ax-CLIN-1b, Ax-CLIN-2/3/4/5/6, T-INTEG-1, C-INTEG-1, and BioQuantum stay in owner. | High |
| `SRT_Neuro_10_Advanced_Models.md` | Navigation-only is sufficient for now. Part B comparisons are tightly bound to Part A axioms; extraction is low priority. Ax-ADV-1 through ADV-6, T-ADV-1, C-ADV-1, H-Adv predictions, Ax-ADV-2, and T1 tension resolution stay in owner. | Low |

## Next Step Recommendation

1. Review this PR as a navigation-only safety layer.
2. Do not create Annex files in PR-B.
3. For PR-D, start with SRT-NEURO-09 §1-§4 after human review of the absorption table boundary.
4. Decide whether GRT comparison material in SRT-NEURO-06 §6 and SRT-NEURO-07 §6 should become one shared GRT interface or two per-file interfaces.
5. Run a separate boundary pass before any SRT-NEURO-08 extraction, especially for Eq-Neuro-AD-PI-1 and Eq-Neuro-TAN-1/2.
