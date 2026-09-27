---
id: SRT-COG-E2-1-WOJCIK-G1-REPRODUCTION-20260927
type: audit
status: complete
canonical: false
layer: operations
epistemic_layer: os
claim_mode: reproduction
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_SESSION_MAPPING_2026-09-27.md
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_SOURCE_CODE_AUDIT_2026-09-27.md
tags: [Cognition, Wójcik, Reproduction, G1, Context, CrossGeneralisation]
---

# COG-E2-1 — G1 source-result reproduction

> Result: PASS.
> Scope: numerical reproduction from the author's locked processed-data cache and exact source statistical function. This is a source-integrity gate, not a new scientific result.

## 1. Source lock

Code / cache repository:

    m-j-wojcik/pfc_learning
    commit = 48ada8054940f6a7ac26e8e83d150357a9f249d2

Processed-data object:

    processed_data/exp2_decoding_collocked_50_100_stages_4.pickle
    blob = 5c3d2c4c06893a8309c53dbc292c57efb9933000

Source functions:

    run_decoding_colour_locked
    run_decoding_ler_null_colour_locked
    plot_dec_xgen
    compute_p_value

Config:

    N_STAGES = 4
    N_WINDOWS = 3
    N_REPS = 1000
    EXP2 color-locked window = [50, 100]

## 2. Observed context scores recovered from author cache

The pickled scores_context_early array is shape 2 × 4:

    ordinary context decoding:
    stage1 = 0.5950680272
    stage2 = 0.5692176871
    stage3 = 0.6476190476
    stage4 = 0.5759353741

    context cross-set generalisation:
    stage1 = 0.4638605442
    stage2 = 0.5514455782
    stage3 = 0.6390306122
    stage4 = 0.5616496599

Observed stage1→stage4 changes:

    ordinary decoding delta = -0.0191326531
    cross-set generalisation delta = +0.0977891156

## 3. Null structure recovered from author cache

run_decoding_ler_null_colour_locked constructs:

    scores_context_rnd
    shape = (1000 reps, 2 decoding-types, 2 stages)

where the stage axis is original stage1 vs original stage4 after random neuron reassignment.

The same cache stores this 1000-repetition null distribution.

## 4. Exact source statistic reproduced

Author compute_p_value uses:

    diff = obs_stage1 - obs_stage4
    diff_rnd = rnd_stage1 - rnd_stage4

with a two-sided test for ordinary decoding and a greater-learning one-sided test for cross-generalisation.

Recomputed:

    ordinary context decoding:
    P = 0.595

    context cross-set generalisation:
    P = 0.023

These exactly match the published Figure 4 values.

Null-difference summary:

    ordinary decoding null:
    mean = 0.01094
    2.5% = -0.05689
    97.5% = 0.08112

    cross-set xgen null:
    mean = 0.00281
    2.5% = -0.09611
    97.5% = 0.09786

## 5. G1 interpretation

The intended source-owned dissociation is reproduced:

    context information availability ≈ stable across learning

while

    context cross-stimulus-set alignment increases across learning.

This supports context as the cleanest geometry-vs-information calibration target in this dataset.

It does not establish E2 scientific increment, whole-field causality, a novel geometry effect, or SRT-specific evidence.

## 6. Important anti-posthoc correction

Because the paper and cache publicly reveal the context learning effect, this exact Figure-4 outcome is not an unknown prospective target.

Therefore:

    E2a source-known calibration = allowed;
    E2 scientific PASS cannot be awarded merely by reconstructing the known context trajectory.

A decisive E2 test must use information not already consumed by source inspection, such as:

- held-out session-level trajectory;
- leave-one-animal-out prediction;
- held-out source trials / session blocks under a preregistered model;
- or a second dataset.

## 7. G1 disposition

    G0 session mapping = PASS
    G1 source-result reproduction = PASS

    source-known Figure-4 context effect = CALIBRATION ONLY

    next gate = freeze genuinely held-out E2b model comparison
                before inspecting its target outputs.