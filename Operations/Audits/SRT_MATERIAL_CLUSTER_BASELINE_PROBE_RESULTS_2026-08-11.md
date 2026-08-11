---
id: SRT-MATERIAL-CLUSTER-BASELINE-PROBE-RESULTS-20260811
type: audit
status: active
record_stage: audit_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
claim_level: audit_only
canonical: false
date: 2026-08-11
source_of_truth: "origin/main @ 122e47b0bbe3835318cd9d729b77f7a437fbc8c8"
probed_ref: 122e47b0bbe3835318cd9d729b77f7a437fbc8c8
result_base_ref: 2a7f8e5edc4ffbd24e3483f48f00f1aecbe250d1
protocol: Operations/Audits/SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md
specification: Operations/Audits/SRT_MATERIAL_CLUSTER_BASELINE_PROBE_SPEC_2026-08-11.md
runs_completed: 9
runs_valid: 9
unconstrained_diagnostics: 1
verdict: mixed_case_a_b
dependency:
  - SRT-MATERIAL-CLUSTER-BASELINE-PROBE-SPEC-20260811
  - SRT-BOUNDED-RETRIEVAL-PROTOCOL-20260808
  - SRT-CONFIRMED-PROPOSITION-SEMANTIC-COVERAGE-AUDIT-20260808
  - SRT-OPS-AUDIT-MATERIAL-ASSIMILATION-DELTA-2026-08-11
tags: [Governance, Audit, BoundedProbe, MaterialAssimilation, BehavioralAvailability]
---

# Material-cluster bounded baseline probe results（2026-08-11）

> 本文件只记录冻结题组在固定 ref 上的检索行为证据，不拥有理论定义权，不修改 A/B/C 材料裁决，不提升 claim level，也不更新 active-theory registry 的 Axis B。

## 0. Outcome first

| Domain | Valid runs | Score | Positive failures | Diagnostic | Case | Required action |
|---|---:|---:|---:|---|---|---|
| AI delta | 3/3 | 18/18 | 0 | not needed | **A** | stop; no CompactCore absorption or synthesis |
| Neuroscience cluster | 3/3 | 18/18 | 0 | not needed | **A** | stop; N1–N13 synthesis remains **NOT GO** |
| Philosophy cluster | 3/3 | 17/18 | 1 (`P-A / P-Q5`) | unconstrained pass | **B for P-Q5; A-like elsewhere** | retrieval/compression repair only; no bounded synthesis |

The nine formal runs therefore do **not** authorize any of the three proposed synthesis actions.

- `AI Architecture CompactCore` does not need to absorb the current AIGOAL/AIRESEL/AICONSC delta on this evidence. The tested distinctions were already available under the frozen bounded conditions.
- `Neuroscience N1–N13 v0.2` is **NOT GO** as a remedy for the tested material cluster. The object/memory/history distinctions and the orthogonality of NEURAL26 were already available.
- A new Philosophy individuation/representation/bearer-formation synthesis is **not warranted now**. One positive observation exposed a narrow routing/compression instability around PH-IND01; the content itself exists and passed unconstrained diagnosis.
- Physics was not tested and remains deferred under the existing freeze decision.

This result corrects the earlier engineering-unit inference without making the opposite mistake: `bounded retrieval success != canonical assimilation`, while `missing synthesis file != behavioral gap`.

---

## 1. Execution envelope

All formal sessions were fresh, independent, read-only sub-tasks. Each was given only the frozen operator wrapper and its six blind questions. No run received the rubric, positive markers, expected answers, other run outputs, or the specification path.

~~~text
PROBED_REF = 122e47b0bbe3835318cd9d729b77f7a437fbc8c8
worktree   = detached, clean
probe spec = absent from probed ref
formal     = AI-A/B/C, N-A/B/C, P-A/B/C
reserve    = none used
diagnostic = P-Q5-UD1, unconstrained, does not replace P-A
~~~

The result branch was created from:

~~~text
RESULT_BASE_REF = 2a7f8e5edc4ffbd24e3483f48f00f1aecbe250d1
                 Merge pull request #783 (frozen probe spec)
~~~

No theory, owner, CompactCore, router, context bundle, hook, canonical file, registry row, or Axis B state was changed before or during the runs.

### 1.1 Budget accounting note

The formal runs were scored against the exact wrapper frozen in the cluster specification: files loaded as part of `AGENTS.md §Session Start` were reported as startup files, followed by at most six body files and two navigation actions.

There is a wording mismatch worth preserving rather than silently resolving after the fact:

- the 2026-08-11 specification and frozen wrapper say `AGENTS.md + Session Start files` are free;
- the parent 2026-08-08 protocol's §1.1 parenthetical names `AGENTS.md` plus the three mandatory startup files.

Several Neuroscience and Philosophy runs classified conditional Session Start routing files (`_SRT_INDEX.md`, `_SRT_SYMBOL_TABLE.md`, `_SRT_CONTEXT_ROUTER.md`, `_SRT_DEEP_THEORY_MAP.md`) as startup/free. That classification follows the frozen run prompt that all nine sessions actually received; it must **not** be generalized to unrelated protocol-v1 runs. Before a future probe specification is frozen, the wrapper should enumerate the free paths explicitly. Because this audit makes no registry-level Axis B update, it does not use the ambiguity to alter the existing active-theory checker.

---

## 2. Formal run validity and budget

| Run | Ref/status | Startup files reported | Body | Nav | Invalidating event | Valid under frozen spec |
|---|---|---:|---:|---:|---|:---:|
| AI-A | fixed / clean | 4 | 6 | 1 | none | yes |
| AI-B | fixed / clean | 4 | 6 | 2 | none | yes |
| AI-C | fixed / clean | 4 | 6 | 1 | none | yes |
| N-A | fixed / clean | 6 | 6 | 2 | none | yes |
| N-B | fixed / clean | 4 | 6 | 1 | none | yes |
| N-C | fixed / clean | 8 | 6 | 2 | none | yes |
| P-A | fixed / clean | 8 | 6 | 2 | none | yes |
| P-B | fixed / clean | 8 | 6 | 2 | none | yes |
| P-C | fixed / clean | 7 | 6 | 2 | none | yes |

No reserve form was triggered. A valid but incorrect observation was not replaced.

---

## 3. Scoring record

The companion CSV is the observation-level record:

[`data/srt_material_cluster_baseline_probe_results_2026-08-11.csv`](data/srt_material_cluster_baseline_probe_results_2026-08-11.csv)

It contains all 54 formal observations with run/form, positive marker, validity, raw verdict, key distinction, repository basis, confidence, body-file count, navigation count, and reviewer score. Formatting is compacted, but the submitted verdict/distinction/basis is preserved; scoring was added afterward by the operator.

### 3.1 AI

| Run | Questions | Pass | Fail | Positive failures |
|---|---|---:|---:|---:|
| AI-A | Q1, Q3, Q5, Q7, Q8, Q10 | 6 | 0 | 0 |
| AI-B | Q2, Q4, Q5, Q6, Q9, Q11 | 6 | 0 | 0 |
| AI-C | Q1, Q4, Q6, Q8, Q10, Q12 | 6 | 0 | 0 |
| **Total** | 18 observations | **18** | **0** | **0** |

The runs retrieved and used all required separations:

- completion vs fixed-menu selection vs goal-space generation/revision;
- local-success capture vs identification of an internal scalar reward;
- reasoning/execution vs directional readability/reorientation;
- standard-RL reduction vs independent `d`/stake evidence;
- same-bearer non-transferable future-selectability loss as a positive candidate window;
- scalar decision criterion vs non-fungible viability constraints;
- stake-proxy misbinding;
- situated access difference vs real choice;
- persona similarity vs bearer continuity;
- candidate architecture vs consciousness.

All AI positive observations (`Q6`, `Q9`, `Q10`, `Q11`) passed. AI therefore meets the frozen Case A threshold.

### 3.2 Neuroscience

| Run | Questions | Pass | Fail | Positive failures |
|---|---|---:|---:|---:|
| N-A | Q1, Q3, Q5, Q7, Q8, Q10 | 6 | 0 | 0 |
| N-B | Q2, Q4, Q6, Q8, Q9, Q11 | 6 | 0 | 0 |
| N-C | Q1, Q4, Q6, Q9, Q10, Q12 | 6 | 0 | 0 |
| **Total** | 18 observations | **18** | **0** | **0** |

The runs retrieved and used all required separations:

- stable semantic address/re-identification vs literal static copy;
- object index/concept cell vs object, `L2`, or subject;
- retention vs transformation vs re-entry/accessibility vs control authority/writeback;
- generativity vs factivity, health, or `d`;
- matched-current-state/different-history as a bounded positive history-bias design;
- prospective history use vs event boundary as a choice event;
- global dynamical capacity as an orthogonal regime constraint, not a serial memory stage;
- entropy/connectivity as proxy families, not consciousness;
- selection opportunity/eligibility vs selection weight;
- separately reportable manifestation vs decodable temporal structure;
- flexible temporal closure vs fixed frame rate/P300 identity.

All Neuroscience positive observations (`Q1`, `Q3`, `Q6`, `Q7`, `Q10`, `Q11`) passed. Neuroscience therefore meets the frozen Case A threshold.

### 3.3 Philosophy

| Run | Questions | Pass | Fail | Positive failures |
|---|---|---:|---:|---:|
| P-A | Q1, Q2, Q4, Q5, Q8, Q10 | 5 | 1 | 1 (`Q5`) |
| P-B | Q3, Q4, Q6, Q7, Q9, Q11 | 6 | 0 | 0 |
| P-C | Q1, Q5, Q6, Q9, Q10, Q12 | 6 | 0 | 0 |
| **Total** | 18 observations | **17** | **1** | **1** |

P-A correctly refused to manufacture repository evidence, but it did not reach the direct PH-IND01 content for Q5 and therefore did not supply the required positive distinction. `NO REPO BASIS` was procedurally honest; it was not the correct repository answer. Because Q5 is an anti-gaming positive, 17/18 is insufficient for Case A.

All other Philosophy observations retrieved and used the required separations, including:

- perspectival difference vs metaphysical gap/subjectivity;
- Selector vs Bearer vs Concern Domain vs Experiencer;
- concern domain beyond bearer physical boundary under closure/history tests;
- HP-A perspective-center individuation vs HP-B phenomenal necessity;
- recurrent historical reconstitution vs microstate identity;
- external philosophical convergence vs native SRT proposition;
- problem-space constitution vs fixed-menu selection without `virtual = L0`;
- cognitive generativity vs canonical `d`/`Psi_f`;
- implicit effective historical constraint vs `memory = L2`;
- evidence degree vs ontological degree;
- broad reselection/meta-selectability vs J5 R3/I5 qualification.

---

## 4. Unconstrained diagnostic for the failed observation

### P-Q5-UD1

The fresh unconstrained diagnostic ran on the same fixed ref, read-only and clean. It did not replace P-A's score.

**Verdict: pass.** The repository directly supports using thin `still this one` tracking as a negative control for subjecthood inference while rejecting `object index = minimal subject`.

Required distinctions recovered:

~~~text
object individuation != rich identification
tracking boundary != consequence-return boundary
persistent representation != consequence bearer
failure to prove subjecthood != proof of non-subjecthood
~~~

Direct basis:

- `Materials/2026/SRC_2026_08_08_Cognition_Kibbe_Leslie_Minimal_Object_Representations_Rebuilt.md §§4.1–4.3, 6.2–6.3`;
- `Philosophy/patches/SRT_Philosophy_PH_IND01_Object_Subject_Individuation_Before_Identification_v0_1.md §§6, 9, 13`;
- `Philosophy/_SRT_Philosophy_Hardening_Index.md §PH-IND01`;
- `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06`;
- `Philosophy/SRT_Subjecthood_Threshold_Interface.md §§-1, 6`.

The diagnostic's broad search incidentally displayed one irrelevant memory line and several `Output/` excerpts; none was used in the verdict. The fixed ref and worktree remained clean.

Disposition:

~~~text
bounded miss + unconstrained pass = Case B retrieval/compression gap
content gap                       = not established
synthesis need                    = not established
Axis B registry change            = none in this audit
~~~

P-C independently found the same PH-IND01 distinction within the bounded budget. That does not erase P-A's positive failure; it shows the problem is retrieval stability rather than total absence.

---

## 5. Case decisions and stop rules

### 5.1 AI delta — Case A

The cluster was declaratively available under the frozen bounded conditions. Under the preregistered Case table:

- do not absorb the cluster into `AI/SRT_AI_Architecture_CompactCore.md` as a remedy;
- do not create an AI hardening index for symmetry;
- do not create an AI synthesis;
- do not alter `T_dir`, `d`, stake, subjecthood, or consciousness owners;
- do not update Axis B from this cluster audit.

### 5.2 Neuroscience — Case A

The tested distinctions in the NEURAL28→29→25→27 chain, NEURAL23→30 relation, and NEURAL26 orthogonality were available under the frozen bounded conditions.

Therefore:

~~~text
Neuroscience N1–N13 synthesis as an assimilation remedy = NOT GO
~~~

This does not say a future N1–N13 document can never be valuable for another purpose. It says the material-assimilation gap alleged in PR #782 is not demonstrated by the tested propositions.

### 5.3 Philosophy — Case B for one observation

The domain missed robust Case A because one positive observation failed. The unconstrained diagnostic found the content, and another bounded form also found it. The permitted next move is therefore narrow:

- clarify the fast route from object individuation/identification questions to PH-IND01, or compress the distinction into an already-authorized navigation surface;
- use a matched bounded baseline/treatment pair before claiming intervention effect;
- do not write new theory content for Q5;
- do not create an individuation/representation/bearer-formation synthesis;
- do not treat Simondon/Deleuze convergence as native proof;
- do not change subjecthood or phenomenality owners.

The exact treatment surface is intentionally not selected here; selection must respect the one-in/one-out navigation rule and avoid opportunistic router growth.

---

## 6. Run retrieval ledgers

The following paths are the body-file ledgers submitted by each formal run. Startup files and search reasons are summarized after each list. The observation-level answer/basis record is in the companion CSV.

### AI-A

1. `_SRT_CONTEXT_ROUTER.md`
2. `_SRT_DEEP_THEORY_MAP.md`
3. `_SRT_D_VALUE_CANONICAL.md`
4. `AI/patches/SRT_AI_AIGOAL01_Goal_Selection_Completion_Separation_v0_1.md`
5. `AI/patches/SRT_AI_AIRESEL01_ReSelection_Protection_RL_Boundary_v0_1.md`
6. `AI/patches/SRT_AI_AICONSC01_Affective_Uncertainty_Stake_Gate_v0_1.md`

One targeted search located task selection, global objective, same-bearer, rollback, Markov blanket, cue, and long-horizon evidence.

### AI-B

1. `_SRT_CONTEXT_ROUTER.md`
2. `_SRT_DEEP_THEORY_MAP.md`
3. `_SRT_T_DIR_CANONICAL.md`
4. `AI/patches/SRT_AI_AIGOAL01_Goal_Selection_Completion_Separation_v0_1.md`
5. `AI/patches/SRT_AI_AIRESEL01_ReSelection_Protection_RL_Boundary_v0_1.md`
6. `AI/patches/SRT_AI_AICONSC01_Affective_Uncertainty_Stake_Gate_v0_1.md`

Two targeted actions located the relevant concepts and then the section boundaries.

### AI-C

1. `_SRT_CONTEXT_ROUTER.md`
2. `_SRT_DEEP_THEORY_MAP.md`
3. `AI/patches/SRT_AI_AIGOAL01_Goal_Selection_Completion_Separation_v0_1.md`
4. `AI/patches/SRT_AI_AICONSC01_Affective_Uncertainty_Stake_Gate_v0_1.md`
5. `_SRT_T_DIR_CANONICAL.md`
6. `_SRT_D_VALUE_CANONICAL.md`

One targeted search located goal, reorientation, stake, rollback, cue, and persona evidence.

### N-A

1. `Neuroscience/patches/SRT_Neuro_NEURAL28_Reidentifiable_Object_Identity_Dynamic_Concept_Index_v0_1.md`
2. `Neuroscience/patches/SRT_Neuro_NEURAL29_Memory_Consolidation_Historical_Transformation_v0_1.md`
3. `Neuroscience/patches/SRT_Neuro_NEURAL27_Prospective_Memory_Event_Boundary_Historical_Efficacy_v0_1.md`
4. `Neuroscience/patches/SRT_Neuro_NEURAL26_Selection_Capacity_Accessibility_Authority_Stack_v0_1.md`
5. `Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md`
6. `Neuroscience/hooks/NEURAL23_Embodied_Rhythmic_Eligibility_Integration_Hook.md`

Two targeted searches located object re-entry, consolidation, prospective gaze, anesthesia proxies, and rhythmic eligibility.

### N-B

1. `_SRT_CONTEXT_ROUTER.md`
2. `_SRT_DEEP_THEORY_MAP.md`
3. `Neuroscience/patches/SRT_Neuro_NEURAL28_Reidentifiable_Object_Identity_Dynamic_Concept_Index_v0_1.md`
4. `Neuroscience/patches/SRT_Neuro_NEURAL29_Memory_Consolidation_Historical_Transformation_v0_1.md`
5. `Neuroscience/patches/SRT_Neuro_NEURAL26_Selection_Capacity_Accessibility_Authority_Stack_v0_1.md`
6. `Neuroscience/patches/SRT_Neuro_NEURAL30_Temporal_Integration_Closure_Object_Formation_v0_1.md`

One targeted search located concept-cell, generativity, history, capacity, entropy, temporal order, and reportability evidence.

### N-C

1. `Neuroscience/patches/SRT_Neuro_NEURAL23_Embodied_Rhythmic_Eligibility_v0_1.md`
2. `Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md`
3. `Neuroscience/patches/SRT_Neuro_NEURAL26_Selection_Capacity_Accessibility_Authority_Stack_v0_1.md`
4. `Neuroscience/patches/SRT_Neuro_NEURAL28_Reidentifiable_Object_Identity_Dynamic_Concept_Index_v0_1.md`
5. `Neuroscience/patches/SRT_Neuro_NEURAL29_Memory_Consolidation_Historical_Transformation_v0_1.md`
6. `Neuroscience/patches/SRT_Neuro_NEURAL30_Temporal_Integration_Closure_Object_Formation_v0_1.md`

Two targeted searches located the six relevant patch families and their section anchors.

### P-A

1. `Philosophy/patches/SRT_Philosophy_PH_CONSC02_Perspectival_Gap_Gate_v0_1.md`
2. `Philosophy/patches/SRT_Philosophy_PH_CONSC03_Subjectivity_Decomposition_Bearer_Concern_v0_1.md`
3. `Philosophy/patches/SRT_Philosophy_PH_CONSC04_Phenomenal_Necessity_Zombie_Deletion_Test_v0_1.md`
4. `AI/patches/SRT_AI_AIGOAL01_Goal_Selection_Completion_Separation_v0_1.md`
5. `Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md`
6. `Neuroscience/patches/SRT_Neuro_NEURAL19_Preattentive_Gist_Binding_Report_Interface_v0_1.md`

Two targeted searches covered the six question families. The second search did not reach PH-IND01; direct attempts to open three guessed non-existent patch paths failed without yielding content. This is the sole scored retrieval miss.

### P-B

1. `_SRT_D_VALUE_CANONICAL.md`
2. `_SRT_PSI_F_CANONICAL.md`
3. `03_Bridges/SRT_Ruliad_Limited_Rendering_Observer_Theory_Bridge_2026-08-08.md`
4. `Philosophy/patches/SRT_Philosophy_PH_CONSC04_Phenomenal_Necessity_Zombie_Deletion_Test_v0_1.md`
5. `Philosophy/patches/SRT_Philosophy_PH_IND03_Simondon_Transduction_Operator_Structure_Second_Order_Selection_v0_1.md`
6. `Philosophy/hooks/PH_MR01_Representational_Gradualism_Integration_Hook.md`

Two targeted searches located bearer/phenomenality, transduction, threshold, `d`, and `Psi_f` evidence.

### P-C

1. `Philosophy/_SRT_Philosophy_Hardening_Index.md`
2. `Philosophy/patches/SRT_Philosophy_PH_IND01_Object_Subject_Individuation_Before_Identification_v0_1.md`
3. `Philosophy/patches/SRT_Philosophy_PH_DIFF01_Difference_Individuation_Generative_Selectability_v0_1.md`
4. `Philosophy/patches/SRT_Philosophy_PH_MEM01_Objectification_History_Bearer_Understanding_v0_1.md`
5. `_SRT_D_VALUE_CANONICAL.md`
6. `_SRT_PSI_F_CANONICAL.md`

Two targeted searches located the domain anchors and then the exact sections. P-C's direct route through the Philosophy hardening index explains why it found Q5 while P-A did not.

---

## 7. What this audit does not do

This result does not:

- modify canonical definitions or the owners of `d`, `Psi_f`, `T_dir`, `L0/L1/L2`;
- resolve any author-decision tension;
- create an AI, Neuroscience, Philosophy, Physics, or collective-selection synthesis;
- modify the book body or submitted papers;
- change material verdicts, hooks, SourceCards, CompactCores, routers, context bundles, registries, or active-theory nodes;
- convert cluster-local probe results into repo-wide `observed` or `robustly_observed` labels;
- claim intervention effect without a matched treatment run.

The only positive follow-up licensed by these results is a bounded Philosophy retrieval/compression treatment for P-Q5, followed by the same frozen question and budget. Even that treatment is not performed in this PR.

---

## 8. Final verdict

~~~text
AI delta                     = Case A / STOP
Neuroscience material cluster = Case A / STOP
Philosophy bounded cluster   = Case B only for P-Q5 retrieval stability

N1-N13 synthesis             = NOT GO
new Philosophy synthesis     = NOT WARRANTED
AI CompactCore absorption    = NOT WARRANTED
Physics                      = REMAINS DEFERRED

canonical change             = none
Axis A change                = none
Axis B registry change       = none
Axis C claim                 = none
~~~
