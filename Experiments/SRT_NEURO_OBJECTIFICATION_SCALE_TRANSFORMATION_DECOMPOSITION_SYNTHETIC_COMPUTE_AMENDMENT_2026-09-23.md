---
id: SRT-NEURO-OBJECTIFICATION-SCALE-TRANSFORMATION-DECOMPOSITION-SYNTHETIC-COMPUTE-AMENDMENT-20260923
type: experiment_amendment
status: frozen
version: v0_1
record_stage: phase3c_synthetic_compute_amendment_after_result_blind_pause
date: 2026-09-23
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
post_primary_exploratory: true
tags: [Neuroscience, Objectification, Transformation, Synthetic, ComputeAmendment, ResultBlind]
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_PREREGISTRATION_2026-09-23.md
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_COMPUTE_AMENDMENT_2026-09-23.md
---

# Phase 3C — synthetic compute amendment

## Amendment boundary

This amendment is frozen after the empirical RIKEN and Hamburg primary chains
and their aggregation were complete, but before inspection of any synthetic
estimated `DeltaQ`, sign-error rate, substantive reversal rate, effect
direction, or FS-A/B/C/D classification. It does not amend the original
Phase 3C preregistration and does not change the empirical results.

The synthetic runtime was safely paused after 21 fully written replicates. The
next replicate had no completed output file and was not counted.

## Result-blind checkpoint audit

The 21 unit files were structurally validated against the checkpoint:

```text
fully written unit files: 21
state/file key match:     PASS
active incomplete unit:   none retained
synthetic outcomes read:  false
```

The existing synthetic unit schema retained only the final per-replicate row;
it did not retain the 200 per-seed Q values or a per-unit seed list. The seeds
remain reconstructible from the frozen seed formula, but a cumulative-max
convergence audit cannot be computed from the saved historical files without
rerunning them. No unsupported convergence reduction is therefore claimed.

## Frozen optimizer decision

```text
chosen Louvain repeats R*: 200
```

Candidates 25, 50 and 100 are not certified by the available per-seed-Q
checkpoint. The conservative uniform rule is to retain 200 for every
synthetic graph. This avoids mixing max-of-200 and max-of-R* semantics. The
existing 21 replicates therefore remain valid under the amended run and are
counted without rerunning.

## Frozen replicate-count change

```text
independent paired replicates per N × effect cell: 200 -> 100
number of cells: 3 N regimes × 3 effect levels = 9
total synthetic replicates: 1800 -> 900
```

All nine cells use exactly 100 replicates. The 21 completed replicates remain
in their preassigned cell; no replicate is discarded or selected by outcome.

The reason is computational burden discovered during result-blind synthetic
execution. The empirical experiment was already complete, and no synthetic
effect or reversal outcome was inspected. One hundred replicates per cell are
sufficient for the intended rare-versus-common reversal calibration: if zero
reversals are observed in a cell, 100 trials imply an approximate 95% upper
bound of about 3% for that event rate.

## Unchanged scientific parameters

```text
scientific model: unchanged degree-controlled SBM
N regimes: unchanged, inherited from RIKEN result-blind node counts
effect levels: unchanged
true-effect direction: unchanged
K: 4 planted communities
expected mean degree: 16
Wake ratio: 1.5
Target ratios: 1.75, 2.5, 4.0
seed root: 12345
graph construction: unchanged synthetic SBM construction
Louvain algorithm: unchanged frozen Python implementation
Louvain repeats: uniformly 200
max-Q rule: unchanged
classification: unchanged FS-A/FS-B/FS-C/FS-D rules
```

This is a computational amendment only. It does not use any synthetic
outcome to choose a cell-specific sample count, repeat count, model, or
classification rule.
