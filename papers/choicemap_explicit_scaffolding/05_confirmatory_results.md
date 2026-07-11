---
type: confirmatory_results
status: completed
claim_mode: evidence
canonical: false
---

# Locked confirmatory results

## Execution and integrity

- Scale: 30 independent confirmatory seeds × 4 environment families × 9 systems ×
  200 episodes = **216,000 episodes**.
- Failed runs: **0**.
- Tests: **10/10 passed** before lock and before confirmatory execution.
- Protocol integrity: confirmatory YAML and experiment-source SHA256 values matched their
  locked manifest after execution.
- Budget: every episode/system used 6 interactions, 144 node expansions, and 6 reserved
  planning calls; mismatches: **0**.
- Leakage: hidden regime, concrete future task before transition, and oracle RFS were absent
  from `AgentView`; audit passed.
- Raw Parquet row counts: episode 216,000; candidate 1,587,580; commitment 82,112.

Parquet files were repacked after the run with GZIP compression from the frozen raw CSVs
to satisfy repository file-size limits. This changed storage only; source/config hashes,
rows, metrics, and decisions did not change.

## Gate A: current-task noninferiority

The strongest observed non-ChoiceMap baseline was OptionScalar. Across the preregistered
comparison, ChoiceMap's seed-level mean current-task difference was **+3.28 percentage
points**, above the locked -3-point noninferiority margin. Gate A passed.

In the hidden irreversible families specifically, ChoiceMap current success was 0.9757
(no shift) and 0.9517 (shift), versus 0.8975 for OptionScalar.

## Gate B: unforeseen future-task performance

Across Hidden-Irreversible and Hidden-Irreversible-Shift:

- mean paired seed difference vs OptionScalar: **+33.21 percentage points**;
- median paired seed difference: **+33.12 points**;
- seed-bootstrap 95% interval: **+31.53 to +34.83 points**;
- paired sign-permutation p: **0.00005**;
- standardized paired effect: **7.07**.

ChoiceMap exceeded every main baseline on all 30 seeds: +33.58 points vs Greedy and
+33.21 points vs Search and OptionScalar. The practical +5-point threshold passed.

By family, ChoiceMap future success was 0.8468 in Hidden-Irreversible and 0.8077 in
Hidden-Irreversible-Shift, versus 0.4952 for Search/OptionScalar. In Stable-Reversible,
the difference from the strongest baseline was **-0.05 points**, consistent with the
preregistered boundary prediction rather than a universal advantage.

## RFS, failure, and commitment

- RFS AUC paired difference: **+0.2129**, 95% interval +0.2096 to +0.2165.
- Irreversible-failure paired difference: **-35.07 points**, 95% interval -36.72 to
  -33.41 points.
- Relative irreversible-failure reduction vs OptionScalar: **69.46%**.
- Wrong commitment: 0.0310 without shift and 0.1175 with shift for ChoiceMap, versus
  0.6793 for OptionScalar.
- Mean probes: 2.92 without shift and 4.00 with shift.

## Ablations—including negative results

Three removals reduced future success by about 33.21 points and RFS AUC by 0.2129:

- `C-noReversibility`;
- `C-immediateCommit`;
- `C-scalarized`.

This supports reversibility metadata, delayed commitment, and non-scalarized selection as
load-bearing in this implementation.

Two preregistered ablations did **not** support necessity:

- `C-noProbe` future success exceeded full ChoiceMap by 4.86 points;
- `C-noBranchMemory` exceeded full ChoiceMap by 5.44 points.

Both chose the conservative safe route, preserved more future options, and sacrificed
some current success. Relative to OptionScalar, C-noProbe current success was -2.17 points
(still within the noninferiority margin) and future success was +38.07 points;
C-noBranchMemory was -1.58 and +38.65 points. Thus probe and branch memory are **not shown
to be necessary for maximizing future success in this environment**. Full ChoiceMap
occupies a different trade-off: materially higher current success with slightly less
future preservation than these conservative variants.

## Generalization

- Leave-one-seed-out: every exclusion retained a positive mean difference; positive-seed
  fraction 1.0.
- Leave-one-regime-template-out: mean differences remained positive (+24.14, +24.17,
  and +50.88 points); positive-seed fraction 1.0.
- Leave-one-future-task-family-out: +33.50 points when access tasks were omitted and
  +32.43 when resource tasks were omitted; positive-seed fraction 1.0.
- Held-out templates `future_4`–`future_7`: ChoiceMap future success 0.8674, versus
  0.4727 for Search/OptionScalar.
- Worst hidden environment family remained positive. No single seed, regime, task family,
  or hidden environment generated the effect alone.

## Cost

Reserved node and interaction budgets were identical. Mean measured wall-clock per
episode was about 0.000631 s for ChoiceMap and 0.000243 s for OptionScalar, approximately
2.6× overhead in this small Python implementation. Wall-clock is supplementary because
the preregistered fairness basis is model access and interaction count.

## Scope

These results concern one synthetic environment family and one explicit implementation.
They do not validate SRT ontology, the complete selection operator, Fisher-as-cost,
selective resynchronization v1, or the existing human-facing ChoiceMap workflow.

