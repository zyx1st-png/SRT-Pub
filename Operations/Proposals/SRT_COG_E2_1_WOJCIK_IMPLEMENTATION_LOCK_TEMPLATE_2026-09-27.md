---
id: SRT-COG-E2-1-WOJCIK-IMPLEMENTATION-LOCK-TEMPLATE-20260927
type: proposal
status: draft
record_stage: pre_target_template
canonical: false
layer: operations
epistemic_layer: execution_handoff
claim_mode: preregistration_template
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Proposals/SRT_COG_E2_1_WOJCIK_E2B_PREREG_2026-09-27.md
  - Operations/Proposals/SRT_COG_E2_1_WOJCIK_TARGET_BLIND_CENSUS_HANDOFF_2026-09-27.md
  - Operations/Audits/SRT_COG_E2_1_TARGET_BLIND_CODEPATH_AUDIT_2026-09-27.md
tags: [Cognition, Wójcik, ImplementationLock, E2b, TargetBlind]
---

# COG-E2-1 — E2b implementation-lock template

> This template must be filled and committed **after target-blind census, before any per-session context-xgen target is generated or inspected**.

> If any field below cannot be frozen without viewing the target, STOP.

## 1. Census provenance

Fill:

    census manifest SHA256: <pending>
    archive checksum file SHA256: <pending>
    external source commit: 48ada8054940f6a7ac26e8e83d150357a9f249d2
    census code commit: <pending>
    environment lock: <pending>

## 2. Eligible sessions

Target-independent eligibility rule:

    <pending>

Eligible Womble sessions:

    <pending>

Eligible Wilfred sessions:

    <pending>

Counts:

    Womble n = <pending>
    Wilfred n = <pending>
    total n = <pending>

Required minimum:

    total >= 12
    each animal >= 4

If not met:

    E2b = UNDERPOWERED / STOP

## 3. Primary target — fixed, not yet generated

    Y_j = session-level context cross-stimulus-set generalisation

Source-compatible window:

    color-locked [50,100]

Target-generation code path:

    <pending exact wrapper/function>

Target values:

    MUST REMAIN BLANK IN THIS LOCK FILE.

## 4. Secondary target — fixed, not yet generated

    Y2_j = context selectivity alignment across stimulus sets

Exact estimator:

    <pending>

Target values:

    MUST REMAIN BLANK IN THIS LOCK FILE.

## 5. H1 frozen specification

Candidate allowed predictors:

- ordinary context decoding;
- task-set decoding;
- behavioral / termination metric;
- session ordinal / normalized learning progress;
- animal indicator if pooled.

Final H1 predictor list:

    <pending after target-blind feasibility only>

Transform / scaling:

    <pending>

Regularization:

    <pending>

## 6. H2 frozen specification

Primary family:

    regularized low-rank latent representation
    + task-variable interactions
    + H1 covariates.

Exact input matrix:

    <pending>

Rank grid:

    <pending>

Penalty grid:

    <pending>

Nested-CV rule:

    <pending>

Effective-complexity report:

    <pending definition>

Fairness guard:

    H2 may reproduce low-dimensional geometry;
    no weakening after target inspection.

## 7. H3 frozen specification

H3 receives H1 covariates plus a non-context relational-geometry block.

Candidate geometry features:

- shape cross-set generalisation;
- XOR cross-set generalisation;
- width cross-set generalisation;
- task-set relational alignment;
- shattering-dimensionality / declared source equivalent;
- non-context selectivity covariance / factorization summaries.

Final common feature set:

    <pending after target-blind feasibility only>

Feature transforms:

    <pending>

Regularization:

    <pending>

Critical guard:

    primary context xgen is not in H3 input;
    no target-derived feature sign / threshold / selection.

## 8. Outer validation — fixed

Primary:

    leave-one-session-out (LOSO)

For each held-out session:

    all model fitting / rank / penalty selection occurs on training sessions only.

Animal handling:

    <pending exact blocked/indicator rule>

Secondary:

    animal-to-animal transfer where estimable
    rolling-origin next-session precursor

Neither secondary may replace the primary after results.

## 9. Primary score

    LOSO mean squared prediction error for Y_j

Required outputs:

- per-session held-out error;
- per-animal mean error;
- pooled mean error;
- H3-H1 delta;
- H3-H2 delta;
- model complexity summary.

Exact aggregation / uncertainty:

    <pending>

## 10. Decision rule — fixed

E2b bounded PASS requires:

    H3 error < H1 error
    AND
    H3 adds nontrivial value beyond H2
    AND
    gain is not solely one-animal driven
    AND
    at least one predeclared no-time / target-normalized sensitivity survives
    AND
    no target leakage / post-target feature selection.

E2b PARTIAL:

    H3 > H1 but ~= H2
    OR
    animal-specific / time-dependent fragile gain
    OR
    secondary target does not agree.

E2b NO-GAIN:

    H3 <= H1
    OR
    H2 >= H3 at equal/lower burden.

## 11. Predeclared sensitivities

Freeze exact implementation for:

1. remove session ordinal;
2. normalize target by ordinary context decoding;
3. secondary Y2;
4. geometry block without XOR;
5. animal-to-animal transfer if estimable;
6. rolling-origin next-session precursor.

No new sensitivity may be promoted to primary after target reveal.

## 12. Target-blind certification

Before changing this file to `status: frozen`, the executor must certify:

    [ ] no per-session context xgen was printed
    [ ] no per-session context xgen was plotted
    [ ] no per-session context xgen was cached outside opaque target-generation code
    [ ] no context-selectivity-alignment target was inspected
    [ ] no H1/H2/H3 target error was inspected
    [ ] feature availability decisions used counts/shapes/errors only
    [ ] eligibility decisions were target-independent
    [ ] exact code commit is recorded

Any failed box:

    prereg prospective status = LOST;
    continue only as explicitly post-hoc analysis.

## 13. Freeze transition

When all fields are filled without target exposure:

    status: frozen
    record_stage: implementation_locked_pre_target

Then and only then authorize:

    target generation
    H1/H2/H3 execution

Canonical edit remains NO.