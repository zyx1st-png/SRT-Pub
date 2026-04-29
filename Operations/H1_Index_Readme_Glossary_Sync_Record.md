---
id: SRT-OPS-H1-INDEX-README-GLOSSARY-SYNC-2026-04-29
type: sync_record
tags: [Operations, Index, README, Glossary, Governance, Hygiene]
status: active_record_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - README.md
  - Operations/README.md
  - SRT_Glossary_Structural_Governance_Terms.md
  - Operations/Closure_Index_2026-04-29.md
  - Operations/Structural_Governance_Rollup_2026-04-29.md
  - ANNEX_REGISTRY.md
machine_summary: >
  H1 sync record for repository index, README, and terminology governance hygiene. Updates public README,
  Operations README, and adds structural governance glossary addendum. Does not modify theory body, formulas,
  thresholds, annex content, or large index/glossary files through risky full-file rewrites.
---

# H1 Index / README / Glossary Sync Record

## 0. Scope

This PR performs low-risk repository entry synchronization after AI and Physics closure work.

Updated / created:

- `README.md`
- `Operations/README.md`
- `SRT_Glossary_Structural_Governance_Terms.md`
- `Operations/H1_Index_Readme_Glossary_Sync_Record.md`

## 1. What changed

### Public README

`README.md` now points new readers to:

- `ANNEX_REGISTRY.md`
- `Operations/Closure_Index_2026-04-29.md`
- `Operations/Structural_Governance_Rollup_2026-04-29.md`
- `SRT_Glossary_Structural_Governance_Terms.md`
- `AI/README.md`
- `Physics/README.md`

### Operations README

`Operations/README.md` now includes:

- current structure governance read order;
- closure index;
- structural governance rollup;
- AI / Physics closure reports;
- stop rule against opportunistic extraction.

### Structural governance glossary addendum

`SRT_Glossary_Structural_Governance_Terms.md` adds definitions for:

- `canonical: false`
- `claim_mode`
- `interface_annex`
- `owner-bound`
- `copy-to-annex`
- `adjudication`
- `closure report`
- `pressure-test domain`
- `external interface`
- `proxy mapping`
- `frozen high-risk topic`

## 2. Deliberately not changed

This PR does **not** directly rewrite:

- `_SRT_INDEX.md`
- `SRT_Glossary.md`
- `_SRT_SYMBOL_TABLE.md`

Reason:

- `_SRT_INDEX.md` and `SRT_Glossary.md` are large, high-value navigation/reference files.
- Full-file rewrite through the connector risks accidental deletion/truncation.
- The safer pattern is to add a focused glossary addendum and schedule a future local/Codex patch for `_SRT_INDEX.md`.

## 3. Safety Record

- No theory body text moved.
- No formulas changed.
- No thresholds changed.
- No domain claims promoted.
- No Core / Core_Law / AI / Neuroscience / Philosophy / Physics / Public / Papers / graphify-out files touched.
- No annex content changed.
- No extraction performed.

## 4. Remaining index task

Future local/Codex-safe task:

```text
Patch _SRT_INDEX.md to add:
- ANNEX_REGISTRY.md in Entry Surfaces if not already sufficiently visible;
- Operations/Closure_Index_2026-04-29.md;
- Operations/Structural_Governance_Rollup_2026-04-29.md;
- SRT_Glossary_Structural_Governance_Terms.md;
- AI/Architecture_Annex/README.md;
- AI/Consciousness_Annex/README.md;
- Physics/README.md;
- Physics/SRT_Physics_Claim_Status.md;
- Physics/QBox_Annex/README.md;
- Physics/Earth_Accretion_Annex/README.md.
```

Do this as a surgical patch, not full-file rewrite.

## 5. Bottom line

The most visible public and Operations entry points are now synchronized with the latest structure-governance state.

The remaining gap is `_SRT_INDEX.md`, which should be patched with a safer local/Codex workflow rather than edited wholesale through connector replacement.
