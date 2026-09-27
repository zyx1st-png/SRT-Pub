---
id: SRT-COG-E2-1-WOJCIK-TARGET-BLIND-CENSUS-HANDOFF-20260927
type: proposal
status: active
canonical: false
layer: operations
epistemic_layer: execution_handoff
claim_mode: bounded_execution
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_SESSION_MAPPING_2026-09-27.md
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_G1_REPRODUCTION_2026-09-27.md
  - Operations/Proposals/SRT_COG_E2_1_WOJCIK_E2B_PREREG_2026-09-27.md
tags: [Cognition, Wójcik, ExecutionHandoff, TargetBlind, Census, Exp2]
---

# COG-E2-1 — target-blind feasibility census handoff

> Scope: local execution preparation only.
> Hard guard: do not inspect or compute per-session context cross-set generalisation / context selectivity alignment before the census disposition and final E2b implementation lock are committed.

## 1. External source lock

Clone outside SRT-Pub:

    repository: m-j-wojcik/pfc_learning
    commit: 48ada8054940f6a7ac26e8e83d150357a9f249d2

Verify:

    git rev-parse HEAD

must equal the locked commit.

Do not modify the external source checkout in place.

Use a separate local analysis workspace / branch for adapters and new scripts.

## 2. Download scope — Experiment 2 only

Do not download all 50 sessions initially.

Womble / Monkey 1 Exp2:

    m1_ses18.zip -> Wom20201005
    m1_ses19.zip -> Wom20201006
    m1_ses20.zip -> Wom20201007
    m1_ses21.zip -> Wom20201008
    m1_ses22.zip -> Wom20201009
    m1_ses23.zip -> Wom20201012
    m1_ses24.zip -> Wom20201013
    m1_ses25.zip -> Wom20201014

Wilfred / Monkey 2 Exp2:

    m2_ses11.zip -> Wil20201104
    m2_ses12.zip -> Wil20201106
    m2_ses13.zip -> Wil20201109
    m2_ses14.zip -> Wil20201110
    m2_ses15.zip -> Wil20201111
    m2_ses16.zip -> Wil20201112
    m2_ses17.zip -> Wil20201113
    m2_ses18.zip -> Wil20201116
    m2_ses19.zip -> Wil20201117
    m2_ses20.zip -> Wil20201118
    m2_ses21.zip -> Wil20201119
    m2_ses22.zip -> Wil20201120
    m2_ses23.zip -> Wil20201123
    m2_ses24.zip -> Wil20201124
    m2_ses25.zip -> Wil20201125

Keep original Dryad archive names immutable.

Record SHA256 for every downloaded archive.

## 3. Adapter rule

Create a reversible mapping layer from Dryad IDs to the code's date-labelled IDs.

Allowed:

- symlinks;
- generated manifest;
- copied aliases with checksums.

Not allowed:

- renaming originals without a manifest;
- inferring identity from file size;
- changing source labels.

Required manifest fields:

    dryad_archive
    dryad_sha256
    code_session_id
    animal
    experiment
    extracted_paths

## 4. Census-only outputs

For each of the 23 Exp2 sessions record:

- session ID;
- animal;
- archive size;
- extracted file inventory;
- neuron/unit count;
- sampled PFC-area counts;
- total usable trial count;
- trial count for each of the 16 source conditions;
- missing conditions;
- whether source preprocessing completes;
- whether source within-session decoding functions can be instantiated without target execution;
- whether each preregistered non-target predictor family is computable.

Allowed result fields are counts / availability / errors only.

## 5. Prohibited during census

Do NOT compute, print, plot, cache or inspect:

- per-session context cross-set generalisation;
- per-session context selectivity alignment across stimulus sets;
- correlations between candidate H3 features and either context target;
- model prediction errors for H1/H2/H3;
- target-informed session exclusions;
- target-informed transforms / feature signs.

If an existing source function automatically computes context target together with other variables, do not call that function during census. Write a target-blind wrapper or stop.

## 6. Allowed predictor feasibility checks

Without exposing target values, determine whether the following can be computed in each session:

- ordinary context decoding;
- task-set decoding;
- shape cross-set generalisation;
- XOR cross-set generalisation;
- width cross-set generalisation;
- shattering dimensionality / declared source equivalent;
- selectivity covariance / factorization summaries;
- behavioral / termination metrics;
- session ordinal.

For target-blindness, feasibility output is boolean / shape / error only, not metric value.

## 7. Source windows

Use source windows only:

    context / color-locked: [50, 100]
    selectivity: [70, 100]
    shape-locked: [100, 150]

Do not tune windows during census.

## 8. Session eligibility

Do not invent a neuron/trial threshold after viewing target values.

Census must report the empirical count distributions first.

Then freeze one common eligibility rule based only on:

- code execution requirements;
- minimum class/condition support;
- source-compatible CV feasibility;
- model identifiability.

Any excluded session must have a target-independent reason recorded before targets are generated.

## 9. E2b implementation lock after census

After the census and before target computation, commit a short implementation-lock packet containing:

1. eligible sessions;
2. exact common predictor set;
3. H1 formula;
4. H2 family + rank/penalty grid;
5. H3 geometry feature transform;
6. primary outer validation scheme;
7. first eligible rolling-origin index or revised cross-animal scheme, if target-blind feasibility requires it;
8. primary score;
9. no-gain rule;
10. code commit / environment lock.

Changing any of 1–10 after target inspection requires a new explicitly post-hoc sensitivity label.

## 10. Stop conditions

STOP and return to the repository without target execution if:

- source mapping conflicts with extracted metadata;
- fewer than 8 usable next-session targets can be obtained under one common target-blind rule;
- the preregistered geometry block is not computable consistently;
- H2 cannot be made strong/fair under the available sample structure;
- target-blindness cannot be maintained because source functions inseparably reveal context target values.

Do not weaken H2 or remove failed sessions to rescue H3.

## 11. Census deliverables

Write outside SRT-Pub during execution:

    census_manifest.csv
    archive_sha256.txt
    environment.txt
    census_log.txt

Then write into SRT-Pub only:

    one census audit markdown
    one implementation-lock / prereg update

No raw or processed neural data are committed to SRT-Pub.

## 12. Current authorization

    Exp2-only download = AUTHORIZED
    checksum + extraction = AUTHORIZED
    target-blind census = AUTHORIZED
    context target generation = PROHIBITED
    H1/H2/H3 result execution = PROHIBITED
    canonical edit = NO