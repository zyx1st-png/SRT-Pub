---
id: SRT-COG-E2-1-WOJCIK-PREREG-HANDOFF-20260927
type: proposal
status: active
canonical: false
layer: operations
epistemic_layer: research_program
claim_mode: preregistration
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Proposals/SRT_PREOBJECT_COGNITION_E2E4_DISCRIMINATOR_PACKET_2026-09-27.md
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_SOURCE_CODE_AUDIT_2026-09-27.md
tags: [Cognition, NeuralGeometry, Wójcik, E2, Preregistration, Handoff]
---

# COG-E2-1 Wójcik — preregistration / execution handoff draft

> **Status:** G0 mapping PASS; prereg model/metric lock remains provisional until G1 source-result reproduction passes.
>
> **Execution rule:** fail closed. No H1/H2/H3 inferential duel may begin until G1 source-owned result reproduction passes and the final prereg commit is frozen.
>
> **Scientific boundary:** neutral cognition architecture only. No SRT primitive evidence.

## 1. Primary question

> Does a shared geometry-level organization predict held-out cross-condition / cross-task generalisation beyond fair local-update and latent-representation baselines?

This is E2 predictive geometry only.

## 2. Source lock

External analysis code:

~~~text
m-j-wojcik/pfc_learning
commit = 48ada8054940f6a7ac26e8e83d150357a9f249d2
~~~

Paper:

~~~text
Wójcik et al. 2026
Nature Neuroscience 29:1966-1975
DOI 10.1038/s41593-026-02333-w
~~~

Data:

~~~text
Dryad 10.5061/dryad.c2fqz61kb
32.11 GB total
~~~

## 3. G0 session mapping — PASS

Resolved by `Operations/Audits/SRT_COG_E2_1_WOJCIK_SESSION_MAPPING_2026-09-27.md`.

Source-grounded result:

~~~text
m1 = Monkey 1 = Womble
m2 = Monkey 2 = Wilfred
Dryad session ordinal = chronological code-session ordinal
G0 = PASS
~~~

No archive-size inference was used.

## 4. Reproduction gate G1

Before any new E2 test, reproduce exactly one source-owned E1 result using author windows / stage grouping.

Preferred G1 target:

> **Experiment 2 late shape-locked cross-generalisation of XOR/reward structure across task sets shows the published stage-dependent organization using the source pipeline.**

Why:

- directly adjacent to the intended E2 holdout;
- source code provides decoding + xgen;
- uses the 16-condition Experiment-2 factorial structure;
- tests that file mapping, preprocessing, stage construction and trial labels are correct.

Use source defaults:

~~~text
N_STAGES = 4
N_WINDOWS = 3
EXP2 shape-locked = [100, 150]
trl_min = 49 where source function applies
sampled PFC areas = [1..4]
~~~

G1 must match the source output direction and numerical scale within a declared reproducibility tolerance.

Do not tune E2 models until G1 passes.

## 5. E2 target split

### Primary target E2-T1

Held-out **cross-task-set XOR generalisation** in Experiment 2.

Training data for H3 may use:

- Experiment-1 learning structure;
- Experiment-2 within-task geometry excluding the primary cross-task-set target;
- relevant factor labels needed to define training relations.

H3 may **not** fit its free parameters to the primary cross-task XOR xgen score.

### Secondary target E2-T2

Held-out cross-task **shape** relation.

### Negative-control target E2-NC1

Width is task-irrelevant.

The model should not earn credit by predicting that all variables become more aligned / decodable.

A useful geometry model should distinguish task-relevant abstraction from irrelevant-feature structure.

## 6. Unit and geometry

Primary unit:

~~~text
stage-level pseudopopulation condition geometry
~~~

Source-compatible observations:

- condition/selectivity vectors;
- cross-validated pairwise distances;
- task1/task2 cosine relations;
- within/cross-task decoder geometry.

Do not assume stable neuron identity across sessions/stages.

## 7. Baseline H1 — local model

H1 may use:

- stage;
- factor-specific decoder strength;
- condition-wise means / tuning summaries;
- independent task-variable interactions;
- source behavioral stage covariates.

H1 predicts each target separately.

H1 is allowed to be accurate.

## 8. Baseline H2 — latent representation model

Primary H2:

~~~text
cross-validated reduced-rank representation
with task-variable interactions
and stage conditioning.
~~~

Freeze latent rank using nested CV on training relations only.

Allowed:

- nonlinear XOR interaction term;
- session/stage-dependent latent coefficients;
- same neural inputs as H3.

Not allowed:

- target-label leakage from E2-T1;
- rank chosen on test score;
- extra data unavailable to H3.

Sensitivity H2b only after primary analysis:

- factor analysis / probabilistic low-rank;
- optionally flexible nonlinear latent model with explicit complexity penalty.

If H2 matches H3 held-out performance at equal/lower effective complexity:

~~~text
H3 incremental value = NO-GAIN.
~~~

## 9. Candidate H3 — shared geometry model

H3 must be more constrained than one bespoke model per probe.

Minimum form:

~~~text
one geometry representation / transformation family
shared across the declared training relations
-> predicts held-out task relation(s).
~~~

Candidate features:

- crossvalidated condition-distance matrix;
- dimensionality;
- factorization;
- task-relevant axis alignment;
- irrelevant-axis normalization;
- geometry transformation across learning stages.

The model must expose which parameters are shared.

## 10. Primary outcome metric

Primary:

~~~text
held-out prediction of E2-T1 cross-task XOR generalisation
~~~

Use an out-of-sample score such as:

- held-out MSE / deviance for continuous xgen values; or
- likelihood / prediction error for window-level xgen estimates.

Secondary:

- E2-T2;
- width negative control;
- joint cross-probe score.

Report uncertainty by source-respecting resampling.

Do not treat pseudopopulation pseudo-trials as independent animals.

## 11. Compression criterion

H3 earns **compression** only if:

1. the same shared parameterization predicts E2-T1 and at least one secondary structural target;
2. it uses fewer or comparable effective degrees of freedom than a set of independent H1 fits;
3. H2 does not recover the same performance at equal/lower burden.

AIC/BIC alone is not sufficient if independence assumptions are violated.

Prefer nested held-out predictive comparison plus explicit parameter/rank accounting.

## 12. Animal guard

Only two animals.

Required:

- report Wom/Wil separately after G0 mapping;
- pooled result is secondary;
- include animal-stratified / leave-one-animal sensitivity where mathematically possible;
- no population-general prevalence claim.

## 13. Leakage guards

Prohibited:

- tuning H3 on E2-T1;
- defining geometry using the target xgen score itself;
- selecting time window after inspecting target;
- choosing stage partition after inspecting target;
- trial reuse across train/test through pseudopopulation construction;
- target-informed latent-rank selection.

Required:

- session-aware/source-trial-aware split;
- frozen source windows;
- frozen N_STAGES=4 primary analysis;
- preregistered fallback if a fold lacks adequate trial counts.

## 14. Decision table

### E2 PASS — bounded

Require all:

~~~text
G0 PASS
G1 PASS

H3 > H1 on E2-T1 held-out prediction
AND
H3 adds value beyond primary H2
AND
shared H3 predicts >=1 secondary structural target
AND
width negative control does not show generic indiscriminate gain
AND
result is not driven by one animal only without disclosure.
~~~

Interpretation:

~~~text
whole-geometry organizational description
has bounded predictive/compression value in this dataset.
~~~

No SRT claim.

### E2 PARTIAL

Examples:

- H3 > H1 but ~= H2;
- H3 predicts T1 but not any secondary probe;
- result depends strongly on one animal.

Interpretation:

~~~text
geometry useful as descriptive / latent-representation reading;
independent whole-field increment not established.
~~~

### E2 NO-GAIN

If H2 equals/exceeds H3 at equal/lower burden, or H3 fails holdout:

~~~text
whole-field scientific increment
= NOT ESTABLISHED in COG-E2-1.
~~~

Do not rescue with alternative SRT vocabulary.

## 15. E3/E4 firewall

This execution cannot establish:

- causal geometry;
- whole-field mechanism;
- recursive causal reconstitution;
- primitive Selection;
- O0;
- L0 ontology.

If E2 passes:

~~~text
next
= separate E3/E4 design package
  with perturbation / consequence-loop evidence.
~~~

## 16. Local execution handoff

Recommended local workspace:

~~~text
external source repo clone
+ separate analysis branch / scripts
+ downloaded Dryad data outside SRT-Pub
+ SRT-Pub stores prereg / result / audit only
~~~

Do not vendor the 32.11 GB dataset into SRT-Pub.

Execution sequence:

~~~text
1. resolve G0 mapping;
2. checksum downloaded subset;
3. reproduce G1;
4. freeze final prereg commit;
5. only then run H1/H2/H3;
6. write result packet;
7. independent review;
8. decide E2 PASS / PARTIAL / NO-GAIN.
~~~

## 17. Current disposition

~~~text
G0 SESSION MAPPING = PASS;
PREREG MODEL/METRIC LOCK = PROVISIONAL UNTIL G1;
DATA EXECUTION = NOT YET AUTHORIZED;
CURRENT NEXT = G1 bounded source-result reproduction -> freeze final prereg;
canonical edit = NO.
~~~
