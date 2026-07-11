---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-MATCHING-FEASIBILITY-20260711
type: empirical_feasibility_report
status: design_infeasible_v1
layer: paper_working
epistemic_layer: bridge
claim_mode: negative_result
claim_level: P4
canonical: false
created: 2026-07-11
v1_decision_changed: false
future_tasks_executed: false
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-MATCHED-ENDPOINT-MULTIFUTURE-SPEC-20260711
---

# Matching Feasibility Report

## Decision: DESIGN INFEASIBLE

The locked A/B-only feasibility gate failed. No future-task loader, branch, metric, or outcome was constructed. The matching window was not changed.

This result does not alter the v1 NO-GO. It shows that the four Stage-4 interventions did not support the required same-endpoint counterfactual under the preregistered matching rules.

## 1. Execution integrity

- feasibility seeds: `3001`–`3005`;
- shared A checkpoints: 5/5 complete;
- B paths: 20/20 complete;
- B checkpoints per path: B0 through B20;
- B trajectory rows: 420;
- failed runs: 0;
- automated tests: 7/7 passed after execution;
- within each seed, all four B paths carried the same A state-dict tensor hash;
- every B row carried `uses_future_data=false`;
- future output files: 0;
- `matched_B_checkpoints.parquet` and `endpoint_balance.csv` were written and hash-frozen before this report.

The feasibility result is therefore a scientific/design failure rather than a software failure.

## 2. Locked feasibility criteria

The gate required at least three of five complete four-path matched groups. A group had to satisfy:

- B validation balanced-accuracy range no greater than `0.015`;
- B validation NLL range no greater than `0.060`;
- B validation ECE range no greater than `0.030`;
- stable, adequate candidate checkpoints in every path;
- a nontrivial history contrast in at least 60% of matched groups.

Observed complete matched groups: **0/5**.

Because the first requirement failed, the path-diversity fraction was not estimable for matched groups and cannot rescue the gate.

## 3. Candidate availability

All four paths generated at least one stable and adequate candidate for every seed. Failure was therefore not caused by an empty candidate list.

| Seed | Standard candidates | Head-only candidates | Replay candidates | Head-reset candidates |
|---|---:|---:|---:|---:|
| 3001 | 19 | 17 | 19 | 17 |
| 3002 | 18 | 9 | 16 | 18 |
| 3003 | 17 | 16 | 19 | 16 |
| 3004 | 19 | 17 | 18 | 17 |
| 3005 | 17 | 5 | 17 | 16 |

The failure was lack of common endpoint support after candidate stabilization.

## 4. Systematic endpoint separation

The maximum B accuracy attained by `head_only` was between `0.7618` and `0.7918` across seeds. The three full-network paths reached approximately `0.870`–`0.880` and had substantially lower NLL.

| Seed | Head-only max accuracy | Head-only min NLL | Best full-path accuracy range* | Best full-path NLL range* |
|---|---:|---:|---:|---:|
| 3001 | 0.7916 | 0.6246 | 0.8701–0.8748 | 0.3610–0.3668 |
| 3002 | 0.7670 | 0.6809 | 0.8713–0.8758 | 0.3581–0.3708 |
| 3003 | 0.7793 | 0.6623 | 0.8730–0.8760 | 0.3529–0.3580 |
| 3004 | 0.7918 | 0.6205 | 0.8748–0.8784 | 0.3487–0.3550 |
| 3005 | 0.7618 | 0.6942 | 0.8729–0.8800 | 0.3472–0.3606 |

`*` Descriptive best values over the trajectories, not selected checkpoints.

The head-only intervention did create a different learning path, but it also imposed a lower attainable B state. It could not be treated as a different history reaching the same endpoint.

## 5. Nearest four-path tuples

For diagnosis only, the closest four-path tuple under the locked normalized range metric was identified for each seed. None qualified.

| Seed | Accuracy range | NLL range | ECE range | Selected epochs: standard/head/replay/reset |
|---|---:|---:|---:|---|
| 3001 | 0.0388 | 0.1489 | 0.0330 | 3 / 20 / 3 / 7 |
| 3002 | 0.0629 | 0.2078 | 0.0073 | 4 / 16 / 4 / 2 |
| 3003 | 0.0351 | 0.1429 | 0.0334 | 2 / 18 / 2 / 2 |
| 3004 | 0.0388 | 0.1431 | 0.0346 | 2 / 17 / 2 / 2 |
| 3005 | 0.0691 | 0.2079 | 0.0291 | 2 / 18 / 2 / 3 |

Relative to the lock:

- the nearest accuracy ranges were `2.34` to `4.61` times the allowed range;
- the nearest NLL ranges were `2.38` to `3.47` times the allowed range;
- ECE sometimes fit or nearly fit, but accuracy and NLL never jointly did.

The epoch pattern is itself informative: full-network paths entered adequate stable regions at epochs 2–4, while head-only required epochs 16–20 and still remained at a worse endpoint.

## 6. Why the window was not widened

Widening accuracy to 4–7 percentage points and NLL to 0.14–0.21 would no longer constitute a close endpoint match. It would recreate the v1 structure:

\[
\text{different intervention}
\rightarrow
\text{different B state}
\rightarrow
\text{different future performance}.
\]

The preregistration explicitly classified post hoc widening as `DESIGN INFEASIBLE`. The protocol therefore stops before any future task.

## 7. Interpretation

The feasibility result supports only the following domain-level statement:

> Under this CNN, B shift, and intervention set, freezing the trunk prevented the head-only path from reaching common B accuracy/NLL support with the three full-network paths within 20 epochs.

It does not show that path history has or lacks an independent effect. No valid matched contrast and no multi-future outcome exists.

The result also does not justify replacing head-only with a more convenient path in the same locked experiment. A new intervention set would be a new protocol and would require a new preregistration.

## 8. Required final questions

1. **Was v1 failure mainly caused by endpoint mismatch?**
   v1 clearly contained severe endpoint mismatch, and Stage-4 reproduced the difficulty of constructing common support. However, because the new matched contrast was infeasible, the claim that endpoint mismatch was the *main causal reason* remains untested.

2. **Is there an independent path effect after equal endpoints?**
   Not identified. No equal-endpoint group was formed.

3. **Did the multi-future design improve identification of retained adaptability?**
   Not evaluated. The precondition for running future tasks failed.

4. **Is there reason to enter architecture comparison?**
   No. Changing architecture would add another identification variable before a valid within-CNN matched contrast exists.

5. **Should the result be interpreted as path dependence, retained plasticity, or no independent effect?**
   None of these is established. The proper interpretation is **intervention-induced endpoint non-overlap / design infeasibility**.

## 9. Stop declaration

Stage-4 stops at the feasibility gate. Files `13`, `14`, and `15` are retained only as explicit non-execution and terminal-decision records. They contain no future-task data. The following data artifacts were not created because doing so would imply a future experiment that did not occur:

- `future_branch_manifest.csv`;
- `future_learning_curves.parquet`;
- `future_outcomes.csv`;
- `path_effect_models.csv`.

No CIFAR-10 experiment, architecture comparison, `SR_preC v2`, full paper, v1 revision, or SRT canonical edit was performed.
