---
id: SRT-COG-E2-1-TARGET-BLIND-CODEPATH-AUDIT-20260927
type: audit
status: active
record_stage: codepath_review
canonical: false
layer: operations
epistemic_layer: os
claim_mode: source_code_audit
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Proposals/SRT_COG_E2_1_WOJCIK_TARGET_BLIND_CENSUS_HANDOFF_2026-09-27.md
tags: [Cognition, Wójcik, TargetBlind, CodePath, E2b]
---

# COG-E2-1 — target-blind source-code path audit

> Purpose: determine which author-code paths can be used during the feasibility census without revealing the decisive context cross-set target.

External source lock:

    m-j-wojcik/pfc_learning
    commit = 48ada8054940f6a7ac26e8e83d150357a9f249d2

## 1. Safe census path

The following source functions are target-blind with respect to context cross-set generalisation when used only for counts / shapes / availability:

### get_data

Loads per-session:

- preprocessed spikes;
- metadata / nonzero trial labels;
- declared time window.

It does not decode context or compute cross-set generalisation.

### exclude_neurons

Filters units by anatomical sampled-area code and optional generic thresholds.

For the current census use only the source sampled-area filter; do not introduce target-informed selectivity exclusion.

It does not compute the context target.

### condition / trial census

Trial labels can be counted by the 16 source conditions without computing any context decoder.

Cell-location CSV can be counted by area without target exposure.

Verdict:

    raw-load + anatomical-filter + count census = TARGET-BLIND SAFE.

## 2. Unsafe composite path during census

The source functions:

    run_decoding_colour_locked
    run_decoding_ler_null_colour_locked

jointly compute context and task-set decoding / xgen.

Calling them during the census would reveal the primary context target.

Verdict:

    prohibited before implementation lock.

## 3. Safe non-target predictor path

The source lower-level primitives are separable enough to compute non-target predictors without calling the composite context function.

Available building blocks include:

- decode;
- decode_xgen_within_ses;
- get_xgen_cross_set_null;
- assign_lables;
- get_betas_cross_val;
- condition averaging / covariance utilities.

Therefore a target-blind wrapper can compute only:

- task-set ordinary decoding;
- shape cross-set generalisation;
- XOR cross-set generalisation;
- width cross-set generalisation;
- non-context selectivity / covariance summaries;
- dimensionality summaries that do not use the held-out context target.

## 4. Ordinary context decoding

Ordinary context decoding is an allowed H1 predictor because the decisive target is context **cross-set alignment**, not context information availability.

However it must be computed by a wrapper that returns only within-set / ordinary context decoding and never calls or stores context xgen.

This preserves the intended dissociation:

    local context information
    vs
    cross-set context geometry.

## 5. Source pseudopopulation path is not the primary E2b unit

get_data_stages + split_data_stages_moveavg pools sessions into stage-level pseudopopulations.

That path is valid for E2a / source reproduction but should not control E2b because:

- it destroys individual-session holdout structure;
- source-known Figure-4 stage trajectory has already been inspected;
- it can blur animal/session independence.

Use individual-session data for decisive E2b.

## 6. Within-session support

The source repository already contains lower-level within-session decoding machinery, including:

    run_within_session_decoding
    decode_xgen_within_ses

so E2b does not require inventing a new decoder family.

New code should be limited to:

- target-blind wrappers;
- session-level geometry extraction;
- outer holdout orchestration;
- fair H1/H2/H3 comparison.

## 7. Critical sample-size observation

Experiment 2 has:

    Womble = 8 sessions
    Wilfred = 15 sessions
    total = 23 sessions.

A primary rolling-origin next-session regression provides at most:

    7 + 14 = 21 transitions

before additional eligibility exclusions.

This is too fragile as the first decisive arena for comparing a strong latent H2 with a relational H3 unless both are reduced to very low-dimensional fixed summaries.

Therefore the code audit recommends:

    primary E2b = leave-one-session-out held-out context alignment
    secondary = next-session / rolling-origin precursor

before target inspection.

## 8. Primary E2b unit recommended

For each eligible session independently compute, from source trials:

- H1 local-information / progression predictors;
- H2 latent summary;
- H3 non-context relational geometry summary;
- context xgen target only after implementation freeze.

Outer evaluation:

    leave one entire session out;
    fit model mapping on remaining eligible sessions;
    predict held-out session context xgen;
    repeat across sessions;
    keep animal identity blocked / stratified in scoring.

This is predictive E2.

It does not claim temporal recursion.

## 9. Next-session route

Retain:

    geometry_s -> context alignment_(s+1)

only as a secondary E4-shaped sensitivity / precursor.

No E4 credit may be awarded.

## 10. Codepath verdict

    target-blind census feasibility = PASS
    composite color-locked source decoder during census = PROHIBITED
    target-blind lower-level wrappers = FEASIBLE
    primary rolling-origin design = DEMOTE
    leave-one-session-out E2b = RECOMMENDED
    target remains UNINSPECTED