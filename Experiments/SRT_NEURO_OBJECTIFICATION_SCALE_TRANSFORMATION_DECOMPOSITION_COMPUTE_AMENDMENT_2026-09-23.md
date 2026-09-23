---
id: SRT-NEURO-OBJECTIFICATION-SCALE-TRANSFORMATION-DECOMPOSITION-COMPUTE-AMENDMENT-20260923
type: experiment_amendment
status: frozen
version: v0_1
record_stage: phase3c_compute_amendment_before_deltaq_inspection
date: 2026-09-23
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
post_primary_exploratory: true
tags: [Neuroscience, Objectification, Transformation, ComputeAmendment, ResultBlind]
dependency:
  - Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_TRANSFORMATION_DECOMPOSITION_PREREGISTRATION_2026-09-23.md
---

# Phase 3C — compute amendment: transformation-repeat count

## Amendment boundary

This amendment is frozen before inspection or comparison of any new R1/R2
`DeltaQ`, subset outcome, random-aggregation outcome, or synthetic outcome. It
does not amend any scientific parameter or any earlier experiment record.

## Reason

The first result-blind runtime benchmark showed that one RIKEN Anesthesia
transformation unit containing five source windows and 200 Louvain trials per
window required approximately 23 seconds on the local machine. The measured
estimate for the preregistered 100-repeat RIKEN control matrix was therefore
approximately 10 hours before the Hamburg matrix and synthetic calibration.
The full Hamburg matrix contains substantially more recording × grain ×
transformation units. This is a computational-burden amendment, not an
outcome-based amendment.

The benchmark was obtained from runtime/checkpoint logs only. No Q value,
`DeltaQ`, direction, sign, grain pattern, or transformation result was read.

## Frozen change

```text
R1 N-only subset repeats:       100 -> 50
R2 random aggregation repeats:  100 -> 50
```

The same value applies to every eligible recording, both target grains, both
datasets, and both transformation families. Existing completed repeats are
retained; the resumed checkpoint executes only repeats `0..49`. No repeat is
selected or excluded using a network outcome.

## Unchanged scientific parameters

```text
seed root: 12345
Louvain trials per window: 200
Q rule: maximum of 200 trials
RIKEN graph: connected MST plus strongest remaining edges, k_bar=16
Hamburg graph: connected MST plus strongest remaining edges, k_bar=4
R1: exact N-only sampling without replacement
R2: exact R3 group-size multiset, random permutation and arithmetic mean
R3: existing frozen spatial construction
biological unit: animal
synthetic model and parameters: unchanged
```

R1 and R2 remain synchronized at the same repeat count. This amendment does
not claim that 50 is scientifically superior; it only makes the predeclared
result-blind decomposition computationally executable within a bounded local
run.
