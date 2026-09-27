---
id: SRT-COG-E2-1-WOJCIK-E2B-PREREG-20260927
type: proposal
status: frozen_candidate
canonical: false
layer: operations
epistemic_layer: research_program
claim_mode: preregistration
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Proposals/SRT_COG_E2_1_WOJCIK_PREREG_HANDOFF_2026-09-27.md
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_G1_REPRODUCTION_2026-09-27.md
tags: [Cognition, NeuralGeometry, Wójcik, E2b, Preregistration, RollingOrigin, HeldOutPrediction]
---

# COG-E2-1 — E2b genuinely held-out preregistration

> Purpose: replace source-known Figure-4 reconstruction with a genuinely held-out session-level prediction test.
> Scientific boundary: neutral cognition science only. Positive results do not establish SRT, O0, primitive Selection, or a literal field.

## 1. Why E2b is required

G1 reproduced the source-known result exactly:

    ordinary context decoding learning effect: P = 0.595
    context cross-set generalisation learning effect: P = 0.023

Because that trajectory is public and has now been inspected, fitting a model to reproduce it cannot count as prospective E2 evidence.

Therefore:

    E2a = source-known calibration / machinery check only
    E2b = decisive held-out prediction

## 2. E2b target

Primary target for animal a, session s+1:

    Y(a,s+1) = session-level context cross-stimulus-set generalisation

computed in the source color-locked window using source-compatible SVM / xgen code.

Primary scientific question:

> Does geometry measured in session s predict the next session's context cross-set alignment beyond current local information, behavior/session progression, and a strong latent-representation baseline?

This is predictive E2, not causal E3.

## 3. Secondary target

Secondary:

    Y2(a,s+1) = next-session context selectivity alignment

defined as the correlation/alignment of context selectivity coefficients across stimulus sets within that session.

Credit is stronger if model ordering agrees for Y and Y2.

## 4. Source unit

Use individual Experiment-2 sessions, not pooled four-stage pseudopopulations.

Known session counts:

    Womble / Monkey 1 = 8 Exp2 sessions
    Wilfred / Monkey 2 = 15 Exp2 sessions

Session order is fixed chronologically by the G0 mapping.

No stable-neuron identity across sessions is assumed.

Each session yields its own population-level geometry summary.

## 5. Rolling-origin evaluation

No future session may contribute to model fitting for an earlier prediction.

For each animal separately:

    use session 1..k as available history
    predict session k+1
    advance k

Primary scoring begins only once the training set contains enough observations to fit every compared model under its preregistered regularization.

If H2/H3 cannot be fit before a minimum history is reached, those early transitions are excluded symmetrically from all models.

Final implementation must record the first eligible k before target outputs are inspected.

## 6. H1 — strong local / progression baseline

H1 predictors from session s may include:

- current context ordinary decoding;
- current context cross-set generalisation;
- current task-set decoding;
- current behavioral performance / termination metric available source-natively;
- session ordinal / normalized learning progress;
- animal indicator when models are pooled.

H1 is explicitly allowed to exploit autocorrelation and monotonic learning.

H1 answers:

> Can next-session context geometry be predicted without a broader geometry state?

## 7. H2 — strong latent-state baseline

H2 receives source-trial / condition data from session s but no session s+1 target information.

Primary H2 family:

    regularized low-rank latent representation of condition activity
    + task-variable interactions
    + current behavioral/session covariates.

Rank and penalties are selected by nested training-only validation.

H2 may use enough flexibility to reconstruct low-dimensional structure.

If H2 matches/exceeds H3 at equal or lower effective burden:

    whole-geometry incremental value = NO-GAIN.

## 8. H3 — relational geometry predictor

H3 is not a literal field variable.

H3 uses a shared geometry feature set from session s, excluding the primary context cross-set target itself from the added geometry block.

Primary geometry block:

- shape cross-set generalisation;
- XOR cross-set generalisation;
- width cross-set generalisation / irrelevance structure;
- shattering dimensionality or source-equivalent dimensionality summary;
- selectivity-covariance / factorization summaries;
- task-set alignment / relational structure available without using Y(s+1).

H3 also receives the H1 covariates.

Therefore the decisive comparison is:

    H1 local/progression
    vs
    H2 latent representation + H1
    vs
    H3 relational geometry + H1.

H3 must use one shared predictor specification across both animals.

## 9. Anti-leakage rule

Prohibited before the E2b result is frozen:

- plotting or inspecting per-session context xgen trajectory;
- inspecting next-session target values while choosing H3 features;
- changing feature signs / transforms based on target correlation;
- choosing the first eligible session k based on result quality;
- choosing regularization from outer-test sessions;
- dropping a session because its target looks anomalous.

Allowed:

- checking trial counts / missingness;
- verifying code executes;
- source-owned labels / event timing;
- G1 stage-level source result already consumed and explicitly quarantined as E2a.

## 10. Missingness / feasibility gate

Before target extraction, run a target-blind feasibility census:

- neuron count by session;
- trial count by condition;
- missing task conditions;
- whether source within-session xgen functions execute;
- which source-native geometry features can be computed in every eligible session.

Freeze the common feature set after this census and before reading per-session target trajectories.

If fewer than 8 total next-session prediction targets survive across both animals:

    E2b = UNDERPOWERED / STOP

rather than relaxing the model after seeing outcomes.

## 11. Primary score

Primary model score:

    rolling-origin out-of-sample squared prediction error for Y(a,s+1).

Report:

- error per predicted transition;
- mean error by animal;
- pooled mean error with animal-block uncertainty;
- H3-H1 error difference;
- H3-H2 error difference.

Do not count sessions as independent animals.

## 12. Model-complexity rule

All models must report:

- number of fitted coefficients / effective rank;
- regularization choice;
- training sample count;
- outer prediction count.

H3 does not earn credit from a tiny error difference purchased by materially larger effective complexity.

Primary comparison is predictive error under nested regularization; complexity is a required interpretation constraint, not a post-hoc rescue metric.

## 13. Sensitivity analyses

Predeclared only:

1. leave-one-animal-out transfer where mathematically estimable;
2. target normalized by current ordinary context decoding;
3. secondary Y2 selectivity-alignment target;
4. remove session ordinal to test dependence on monotonic time;
5. geometry block without XOR, because XOR is already highly aligned early.

These are sensitivity analyses, not alternate primary endpoints.

## 14. Decision rule

### E2b PASS — bounded

Require:

    H3 lower out-of-sample error than H1
    AND
    H3 adds nontrivial prediction beyond H2
    AND
    direction not produced solely by one animal
    AND
    result survives at least one target-normalized / no-time sensitivity
    AND
    no leakage / post-target feature selection.

Interpretation:

    relational whole-geometry summary carries bounded next-step predictive information
    beyond local/progression and latent-state baselines in this dataset.

Still not E3/E4 or SRT-specific evidence.

### E2b PARTIAL

Examples:

- H3 > H1 but H3 ~= H2;
- pooled gain driven mainly by one animal;
- gain vanishes when session ordinal is removed;
- primary Y improves but Y2 does not.

Interpretation:

    geometry is useful as a representation/summary,
    independent whole-geometry increment not established.

### E2b NO-GAIN

If H2 equals/exceeds H3, or H3 does not beat H1:

    whole-geometry scientific increment = NOT ESTABLISHED in COG-E2-1.

Do not rescue by changing SRT vocabulary or adding post-hoc features.

## 15. E4 firewall

One-step-ahead prediction is only an E4-shaped precursor.

It does not establish:

    consequence -> geometry -> recutting causal recursion.

E4 requires a separate causal / intervention design.

## 16. Execution order

    G0 mapping PASS
    G1 source-result reproduction PASS
    -> target-blind session feasibility census
    -> freeze common features + first eligible rolling-origin index
    -> freeze implementation commit
    -> compute per-session target trajectory for the first time
    -> execute H1/H2/H3 outer predictions
    -> result packet
    -> independent review

## 17. Current authorization

    session feasibility census = AUTHORIZED
    target trajectory inspection = NOT YET
    H1/H2/H3 inferential execution = NOT YET
    raw data full download = only as required for the census / execution
    canonical edit = NO