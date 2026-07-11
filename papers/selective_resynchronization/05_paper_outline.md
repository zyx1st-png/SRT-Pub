---
id: PAPER-SELECTIVE-RESYNCHRONIZATION-OUTLINE-20260710
type: paper_outline
status: draft_v0_1
layer: paper_working
epistemic_layer: bridge
claim_mode: proposal
claim_level: mixed_P2-P4
canonical: false
created: 2026-07-10
depends_on:
  - PAPER-SELECTIVE-RESYNCHRONIZATION-SOURCE-AUDIT-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-REFRAMING-MEMO-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-CONSTRUCT-HARDENING-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-TWO-SHIFT-PROTOCOL-20260710
  - PAPER-SELECTIVE-RESYNCHRONIZATION-PREREGISTERED-ANALYSIS-20260710
---

# Paper Skeleton: Selective Resynchronization in Neural Learning

## 0. Manuscript status

Proposed type:

> **A preregistered theory-and-method proposal written in Stage-1-style / registered-report-style form.**

This is not a formal Registered Report unless a journal later accepts it into that process. At the present stage there is no Results section, no abstract, no empirical conclusion, and no claim of support.

Provisional working title:

> **Beyond Convergence: Operationalizing Selective Resynchronization and Retained Adaptability in Neural Learning**

The title is provisional. Fisher is deliberately absent from the main title because it is a candidate predictor rather than the paper's answer.

## 1. Single contribution and paper-level claim

The manuscript has one contribution:

> **An operational framework for studying selective resynchronization: how an adaptive system reorganizes perturbation-induced variability into a stable adaptation while retaining capacity for subsequent adaptation.**

The four-state framework, candidate measures, two-shift protocol, retained-adaptability outcome, and Fisher comparison are components of this one contribution.

The strongest paper-level claim that can be made before data collection is:

> The proposed framework supplies a non-circular and falsifiable way to test whether pre-second-shift learning dynamics predict later adaptability beyond current performance and standard baselines.

Whether the construct is useful is an empirical question, not a premise.

## 2. Section architecture at a glance

| Section | Unique function | Maximum pre-results claim level | Depends on results? |
|---|---|---|---|
| 1. Introduction | establish the unresolved problem and one contribution | problem statement + method proposal | no for rationale; yes for later significance |
| 2. Related Work | show overlap and residual gap without novelty inflation | literature synthesis | no, but requires verified citations |
| 3. Construct Definition and Discriminant Validity | make the construct testable and killable | new method proposal | validity claim depends on results |
| 4. Four-State Framework | specify trajectories, contrast states, and boundary rules | new operational taxonomy | reliability depends on results |
| 5. Candidate Measures | define proxies and Fisher's limited role | standard methods + new measurement proposal | predictive value depends on results |
| 6. Two-Shift Experimental Protocol | separate current adaptation from future adaptability | preregistered method | no for design; yes for feasibility |
| 7. Preregistered Hypotheses and Analysis | fix outcomes, models, decisions, and nulls | empirical hypotheses | entirely unresolved |
| 8. Falsification and Failure Conditions | state what would kill construct and Fisher bridge | methodological guardrail | adjudicated by results |
| 9. Relationship to Selective Reality Theory | disclose provenance and prohibit extrapolation | SRT-inspired interpretation | no support claim permitted |
| 10. Limitations | state scope and unresolved threats | bounded methodological assessment | partly updated after execution |
| 11. Planned Discussion | prespecify interpretation branches | no empirical claim | yes; branch selected only after results |

## 3. Detailed outline

### 1. Introduction

**Unique purpose**

Establish why endpoint convergence is insufficient for evaluating adaptation under sequential change, then introduce the need to distinguish productive reorganization from rigidity, noise, rollback, and collapse.

**Core claims**

1. Systems with similar current performance can differ in later ability to learn.
2. Existing endpoint metrics do not by themselves characterize the transition from perturbation to stable, reusable adaptation.
3. The paper proposes one operational framework and a two-shift test, not a proof of a general theory.

**Evidence required**

- primary studies demonstrating plasticity loss distinct from forgetting;
- continual-learning work measuring transfer and retention;
- distribution-shift and learning-dynamics studies showing endpoint metrics can miss path differences;
- evidence that a two-shift design is necessary to observe future adaptability rather than current adaptation.

**Existing materials**

- source audit and reframing memo;
- operational `A -> B -> C` protocol;
- primary evidence that deep networks can lose future learning capacity even while continual learning remains the target ([Dohare et al., 2024](https://www.nature.com/articles/s41586-024-07711-7));
- GEM metrics framing transfer and forgetting in task sequences ([Lopez-Paz & Ranzato, 2017](https://proceedings.neurips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html)).

**Missing materials**

- systematic, verified review of current learning-dynamics and retained-plasticity literature;
- direct evidence that existing endpoint approaches fail on the proposed tasks;
- all new experimental data.

**Claim level**

- literature statements: established empirical work when directly cited;
- paper's gap: literature-synthesis claim requiring careful qualification;
- proposed response: new method proposal.

**Results dependence**

The problem statement does not depend on the new results. Any claim that the framework resolves the problem does.

**Likely reviewer attack**

“The problem is already the stability-plasticity dilemma or loss of plasticity with new terminology.” The Introduction must state the narrower proposed increment: a pre-`C` process signature tested against later adaptability after matched current performance.

---

### 2. Related Work

**Unique purpose**

Map the proposed framework onto existing fields and identify exactly what is inherited, compared, and not claimed as novel.

**Planned subsections**

1. distribution shift and nonstationary learning;
2. continual learning, forgetting, forward transfer, and loss of plasticity;
3. representation drift and representation similarity;
4. robustness and recovery after perturbation;
5. synchronization/resynchronization in adaptive and sensorimotor systems;
6. critical transitions and critical slowing down;
7. information geometry, natural gradient, empirical Fisher, Hessian, KL, and sharpness;
8. online change-point detection: BOCPD and CUSUM.

**Core claim**

No adjacent concept is denied or displaced. Selective resynchronization is proposed only as a conjunction of episode-level opening, selective incorporation, new-state stability, and later adaptability whose incremental validity must be tested.

**Evidence required**

- original or authoritative primary papers for each subsection;
- explicit comparison of definitions, units of analysis, and outcome variables;
- an updated term search before submission.

**Existing materials**

- CKA representation comparison ([Kornblith et al., 2019](https://proceedings.mlr.press/v97/kornblith19a));
- EWC catastrophic-forgetting study ([Kirkpatrick et al., 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5380101/));
- corruption/perturbation robustness benchmark ([Hendrycks & Dietterich, 2019](https://openreview.net/forum?id=HJz6tiCqYm));
- critical-slowing empirical analysis ([Dakos et al., 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2567225/));
- BOCPD ([Adams & MacKay, 2007](https://arxiv.org/abs/0710.3742));
- CUSUM ([Page, 1954](https://academic.oup.com/biomet/article-abstract/41/1-2/100/456627));
- empirical-Fisher limitation analysis ([Kunstner et al., 2019](https://proceedings.neurips.cc/paper/2019/hash/46a558d97954d0692411c861cf78ef79-Abstract.html));
- perturbation/resynchronization in paced tapping ([Laje et al., 2019](https://www.nature.com/articles/s41598-019-54133-x)).

**Missing materials**

- verified primary citations for stability-plasticity theory, modern distribution-shift taxonomies, relearning, and optimizer-state plasticity `[CITATION NEEDED]`;
- comprehensive novelty search for the exact construct phrase and close variants;
- a formal systematic-review protocol is not planned and must not be implied.

**Claim level**

Literature synthesis; no empirical novelty claim until the search is completed.

**Results dependence**

No, except that later Discussion must position the observed pattern against this map.

**Likely reviewer attack**

“Selective resynchronization cherry-picks pieces of continual learning, recovery, and representation drift.” The section must expose this risk and specify the construct kill rule rather than defend novelty rhetorically.

---

### 3. Construct Definition and Discriminant Validity

**Unique purpose**

Define the construct, separate `SR_preC` from the future outcome `Q_C`, and establish retention/kill criteria.

**Core claims**

1. A minimal non-circular operational definition can be stated.
2. Proxies are not definitions.
3. The construct is retained only if `SR_preC` predicts `Q_C` beyond existing concepts and controls.

**Evidence required**

- operational reliability of primary measures;
- discriminant comparison with adaptation, recovery, retained plasticity, continual learning, drift, robustness, and critical-transition metrics;
- out-of-sample incremental prediction after `B` matching.

**Existing materials**

- minimal/full definitions, necessary/non-necessary/exclusion conditions in `02_construct_hardening.md`;
- full discriminant-validity matrix;
- explicit construct-retention and kill criteria.

**Missing materials**

- measure reliability estimates;
- empirical discriminant validity;
- evidence that selective-incorporation subspace overlap has task-relevant meaning;
- external expert review of terminology.

**Claim level**

New method proposal; usefulness is an empirical hypothesis.

**Results dependence**

Definition: no. Construct validity and retention: yes.

**Likely reviewer attack**

“The definition embeds successful later adaptation and is therefore tautological.” The answer is the preregistered separation: `SR_preC` is formed without `C`; `Q_C` is the later test outcome.

---

### 4. Four-State Framework

**Unique purpose**

Specify operational contrasts among rigidity, desynchronization-open, candidate/full selective resynchronization, and disorganization/collapse.

**Core claims**

1. The categories are time-window states, not four mutually exclusive whole-run labels.
2. “Productive desynchronization” is retrospective; the real-time label is desynchronization-open.
3. High current performance with poor later adaptability is adaptive lock-in, not target success.

**Evidence required**

- calibration-anchor manipulation checks;
- inter-rule reliability under probe and threshold resampling;
- continuous metric separation among anchor conditions;
- state transitions that predict `Q_C` without using Fisher.

**Existing materials**

- state table, precedence rules, thresholds, and boundary cases in `02_construct_hardening.md`;
- planned rigidity, disorganization, rollback, and no-shift controls.

**Missing materials**

- empirical state frequencies;
- evidence that the categories are stable across tasks and architectures;
- evidence that a categorical account is superior to continuous dynamics.

**Claim level**

Operational taxonomy proposal; distinguishability is an empirical hypothesis.

**Results dependence**

Yes. If labels are unstable but continuous effects remain, categorical claims must be removed.

**Likely reviewer attack**

“The states overlap, and successful runs necessarily pass through more than one.” The section must make the state-machine/time-window logic explicit and avoid run-level forced classification.

---

### 5. Candidate Measures

**Unique purpose**

Define `D`, selective-incorporation/restabilization measures, `Q_C`, and Fisher burden while exposing estimator and proxy limits.

**Planned subsections**

1. gradient disagreement;
2. representation displacement and change-subspace overlap;
3. restabilization and robustness profile;
4. retained adaptability outcome;
5. Fisher-geometric burden;
6. direct baselines and change-point measures;
7. computational complexity and projection failure.

**Core claims**

1. No single measure directly measures selective resynchronization.
2. Fisher metric, quadratic form, path accumulation, `Psi_f`, and realized training costs are different objects.
3. `G_t = 1/2 Delta theta_t^T F_t Delta theta_t` is a candidate predictor only.

**Evidence required**

- estimator definitions and computational validation;
- empirical versus model-sampled Fisher sensitivity;
- probe, layer, parameterization, and damping sensitivity;
- direct comparisons with KL, norms, drift, Hessian/sharpness, entropy, loss, BOCPD, and CUSUM;
- predictive reliability and cost.

**Existing materials**

- old fixed-probe/Gram-trick implementation description, as an unaudited method seed only;
- current SRT Fisher/`Psi_f` boundary files;
- executable quadratic-product plan;
- verified empirical-Fisher limitation source.

**Missing materials**

- new implementation and unit tests;
- true/model-sampled Fisher comparison on the study models;
- actual runtime/memory benchmarks;
- parameter-rescaling control;
- validated Hessian/sharpness implementation.

**Claim level**

- Fisher/KL background: established mathematics under stated assumptions;
- CKA/BOCPD/CUSUM: standard methods;
- selected proxy bundle: new method proposal;
- incremental predictive value: empirical hypothesis.

**Results dependence**

Method definitions: no. Any ranking or special Fisher role: yes.

**Likely reviewer attack**

“The empirical Fisher is neither the Fisher nor a reliable curvature matrix, and `G_t` just approximates KL or update size.” This is a required competitor/projection-failure test, not an objection to be dismissed.

---

### 6. Two-Shift Experimental Protocol

**Unique purpose**

Provide an executable design that separates current adaptation from later adaptability under mechanistically distinct changes.

**Core claims**

1. `A -> B -> C` is necessary for the proposed outcome distinction.
2. Matching current `B` performance reduces endpoint-mastery confounding.
3. The MVP is feasible without full Fisher computation.

**Evidence required**

- deterministic environment and split validation;
- common support for `B` matching;
- shift-severity manipulation checks;
- adequate seeds and simulation-based power;
- compute/resource benchmark;
- head-local confound analysis for partial label remapping.

**Existing materials**

- Fashion-MNIST MVP specification;
- CIFAR-10 core factorial design;
- background/covariate `B` and partial label-rule `C`;
- matching algorithm, controls, ablations, compute range, and output schema in `03_two_shift_protocol.md`.

**Missing materials**

- code, tests, configuration files, and immutable manifests;
- calibration constants;
- actual common-support assessment;
- actual compute measurements;
- power simulation.

**Claim level**

Preregistered method proposal.

**Results dependence**

Design rationale: no. Feasibility, matching success, and generality: yes.

**Likely reviewer attack**

“The shifts are artificial; `C` can be solved by output-head remapping; checkpoint matching induces selection bias.” Required responses are changed/unchanged-class reporting, head/trunk controls, fixed-budget sensitivity, explicit common-support limits, and restrained external validity.

---

### 7. Preregistered Hypotheses and Analysis

**Unique purpose**

Fix the primary outcome, nested models, multiple-comparison policy, missing-run handling, and decision rules before confirmatory data.

**Core claims**

1. `M_D` versus `M_0` is the primary construct test.
2. `M_FD` versus `M_D` is the primary Fisher incremental-value test.
3. Fisher win/tie/lose/inconclusive and construct retain/kill outcomes are all permitted.

**Evidence required**

- frozen preregistration;
- synthetic/null-data validation of analysis code;
- calibration-based thresholds and matching;
- seed-level cross-validation and uncertainty;
- complete deviation log.

**Existing materials**

- primary/secondary hypotheses;
- `M_0`, `M_F`, `M_D`, `M_FD`, `M_T`;
- outcome, effect sizes, corrections, exclusions, robustness, null, and stopping rules in `04_preregistered_analysis.md`.

**Missing materials**

- final calibration constants;
- simulation-based power justification;
- frozen analysis code;
- immutable preregistration record.

**Claim level**

Empirical hypotheses and analysis plan.

**Results dependence**

All substantive hypothesis conclusions depend on new results.

**Likely reviewer attack**

“The feature blocks are large relative to seeds, and nested model improvement will overfit.” The design must use compact frozen features, leave-one-seed-out evaluation, paired seed bootstrap, simulation-based power, and an adequately seeded CIFAR main study.

---

### 8. Falsification and Failure Conditions

**Unique purpose**

Make clear what would refute the construct, weaken Fisher, invalidate the protocol, or merely leave an inconclusive result.

**Core claims**

1. Failure of Fisher does not automatically kill the construct.
2. Failure of `SR_preC` incremental validity does kill or sharply narrow the new construct.
3. Uncertainty is not equivalence, and a technical failure is not scientific collapse.

**Evidence required**

- complete reporting of all decision branches;
- reliability, common-support, and threshold-sensitivity checks;
- comparison with ordinary adaptation/retained-plasticity models;
- negative controls and scientific-failure counts.

**Existing materials**

- construct-retention/kill criteria;
- Fisher win/tie/lose rules;
- null interpretation matrix;
- stop conditions.

**Missing materials**

- observed adjudication;
- independent reproduction across at least one harder task/architecture.

**Claim level**

Methodological guardrail; empirical verdict pending.

**Results dependence**

Yes.

**Likely reviewer attack**

“The framework is designed to survive every null.” The section must show the opposite: if ordinary controls explain `Q_C` and `SR_preC` adds no value, the new term is withdrawn even if the two-shift protocol remains useful.

---

### 9. Relationship to Selective Reality Theory

**Unique purpose**

Disclose intellectual provenance while preventing SRT from carrying empirical or mathematical claims in the machine-learning paper.

**Mandatory statements**

1. This study does not prove, validate, or empirically confirm SRT.
2. It operationalizes one SRT-inspired bridge hypothesis in a restricted neural-learning domain.
3. Results may support, weaken, or reject that bridge hypothesis.
4. Fisher geometry is not the complete definition of `Psi_f`, selection cost, or ontological friction.
5. Machine-learning results do not directly generalize to ontology, consciousness, subjectivity, embodiment, or reality-selection.

**Core claim**

SRT supplied a research heuristic: stabilization should be evaluated together with transition burden and preservation of future adaptive capacity. The empirical framework stands or falls on ordinary scientific criteria.

**Evidence required**

- exact citation to the non-canonical source-intuition trace as provenance;
- exact citation to current `Psi_f` boundary documents;
- claim audit confirming no identity or ontology inference.

**Existing materials**

- source audit of the remote trace;
- `_SRT_PSI_F_CANONICAL.md` and bridge/claim-status files;
- explicit paper-level boundary language.

**Missing materials**

- final citation format for repository theory documents;
- independent editorial review for overclaim and audience fit.

**Claim level**

SRT-inspired interpretation / provenance statement only.

**Results dependence**

No proof/support statement is allowed. The bridge-strength assessment depends on results.

**Likely reviewer attack**

“The ontology motivated the answer and Fisher was chosen to validate it.” The design directly permits Fisher to lose and the construct to be killed; the paper must foreground that fact and keep this section short.

---

### 10. Limitations

**Unique purpose**

Bound what the proposed study can establish before any Discussion branch is selected.

**Required limitations**

- artificial and supervised environment shifts;
- one primary `A -> B -> C` order;
- partial label-rule shift can be head-local;
- representation proxies depend on probe, layer, and invariances;
- gradient disagreement can reflect sampling and imbalance;
- state thresholds are calibration-dependent;
- matching restricts inference to common support and can introduce selection concerns;
- Fisher approximations and parameterization sensitivity;
- compute limits on metric cadence and seeds;
- no causal identification of a latent “resynchronization mechanism” from prediction alone;
- no direct claims about biological systems, consciousness, subjects, or ontology;
- preliminary term search is not a proof of novelty;
- Fashion-MNIST is a gate, not general evidence.

**Core claim**

At best, the study can establish predictive and discriminant validity for a domain-level operational framework under specified learning protocols.

**Evidence required**

- protocol-specific sensitivity analyses;
- transparent non-generalization statements;
- final limitations updated after execution.

**Existing materials**

- proxy and projection-failure audits;
- matching/common-support failure rule;
- scale-up gate.

**Missing materials**

- observed severity of each limitation;
- replication outside supervised image classification.

**Claim level**

Bounded methodological assessment.

**Results dependence**

Partly. The limitations exist now; their practical impact depends on data.

**Likely reviewer attack**

“The acknowledged limitations make the construct too task-specific.” The paper should accept a task-specific result if that is what the data support rather than claim universality.

---

### 11. Planned Discussion

**Unique purpose**

Prespecify interpretation branches so the eventual Discussion cannot convert every result into support.

**Branch A: construct and Fisher both add value**

- domain-level result: pre-`C` dynamics predict retained adaptability;
- methodological result: Fisher adds incremental prediction in the tested regime;
- permitted SRT interpretation: one bridge hypothesis remains viable;
- prohibited extrapolation: Fisher is `Psi_f`, SRT is proven, or neural networks demonstrate ontological selection.

**Branch B: construct adds value; Fisher ties or loses**

- retain the operational construct provisionally;
- report that simpler process/function-space measures are preferable;
- weaken or reject the Fisher bridge for this setting;
- frame Fisher failure as informative, not anomalous.

**Branch C: Fisher predicts; construct block does not**

- report a local geometric predictor of future adaptation;
- do not claim selective-resynchronization construct validity;
- consider reframing as a learning-dynamics measurement paper.

**Branch D: current performance or standard plasticity metrics suffice**

- withdraw or narrow “selective resynchronization”;
- retain the two-shift/matched-performance protocol only if it has independent methodological value;
- no SRT-specific support claim.

**Branch E: measures or matching fail**

- conclude inconclusive/invalid for the primary question;
- report the failure and redesign requirements;
- do not substitute post hoc thresholds or selected seeds.

**Evidence required**

Only the completed preregistered analyses and deviations log can select a branch.

**Existing materials**

- null-result matrix and decision rules.

**Missing materials**

- all results.

**Claim level**

No current empirical claim; prospective interpretation plan.

**Results dependence**

Entirely.

**Likely reviewer attack**

“The Discussion will overinterpret a predictive association as a mechanism.” Every branch must distinguish predictive validity, process description, causal mechanism, and SRT-inspired interpretation.

## 4. Evidence and claim ledger

| Planned statement | Category | Current evidence | Maximum wording before results |
|---|---|---|---|
| Fisher metric describes local statistical distinguishability | Established mathematics | current theory boundary + verified literature still needed | “provides a local statistical geometry under stated assumptions” |
| local Fisher quadratic is related to local KL under regularity/locality | Established mathematics | old manuscript seed; citation verification required | “motivates a candidate local transition measure” |
| CKA compares representation similarity | Standard method | Kornblith et al. | “we use CKA as a representation proxy” |
| BOCPD/CUSUM detect changes | Standard method | Adams–MacKay; Page | “change-detection baselines” |
| `SR_preC` is a useful feature block | New method proposal | design only | “we propose” |
| four states are separable | Empirical hypothesis | no new data | “we test whether” |
| `SR_preC` predicts `Q_C` | Primary empirical hypothesis | no new data | “we hypothesize” |
| intermediate Fisher burden is productive | Secondary empirical hypothesis | no new data | “we test a possible non-monotonic relation” |
| Fisher adds incremental predictive value | Secondary empirical hypothesis | no new data | “may add; can tie or lose” |
| SRT motivated the question | SRT-inspired interpretation | source trace + boundaries | “motivated by” |
| SRT or ontology is supported | Unsupported extrapolation | none | prohibited |

## 5. Citation worklist before full drafting

Verified primary starting points are listed in the detailed outline. The following still require primary-source verification before prose is drafted:

- formal Fisher/KL/natural-gradient background and exact regularity conditions;
- Cencov/Chentsov uniqueness and its limited scope;
- stability-plasticity dilemma origins and modern neural formulations;
- distribution-shift taxonomy and nonstationary evaluation;
- retained-plasticity/relearning measures beyond the 2024 Nature study;
- optimizer-state and feature-rank correlates of plasticity loss;
- sharpness/Hessian approximations used in the planned baseline;
- representation-subspace overlap as a selective-incorporation proxy;
- common-support/matching methodology appropriate to the analysis;
- statistical equivalence and predictive-model comparison methods.

Unverified references remain `[CITATION NEEDED]`; they are not filled from memory.

## 6. Drafting gate

Do not generate the full English manuscript yet. Full drafting becomes reasonable only after:

1. the user approves this construct/protocol/analysis direction;
2. the exact citation worklist is verified;
3. the MVP code and calibration plan are feasible;
4. the manuscript's article type and target venue are selected;
5. a preregistration-ready version of the protocol is frozen.

The scientific status at this outline stage is **CONDITIONAL GO**, not support for the construct.
