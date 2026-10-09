---
id: SRT-CN2-A-P1-P6-OBSERVABILITY-IDENTIFIABILITY-PREPASS-20261009
type: audit
status: draft
canonical: false
layer: operations
epistemic_layer: machine_analysis
claim_mode: bounded_paper_only_feasibility
created: 2026-10-09
updated: 2026-10-09
research_mode: U
root_question: Which A-family P1–P6 human observations are source-native, genuinely adaptable, or missing, and is a fair model-relative E2 held-out predictive question identifiable before data/model selection?
comparative_claim: none; source-native observability and rival adequacy checks, not a claim of SRT predictive gain
named_comparator: null
n_mode_triggered: false
dependency:
  - STATUS.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_FIRST_E2_TASK_FAMILY_A_2026-10-09.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_NAMED_MODEL_FAIR_COMPARISON_2026-10-08.md
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
  - Operations/Proposals/SRT_L0_FACING_E2_E4_MULTIPROBE_RECUTTING_DESIGN_2026-09-26.md
  - Operations/Audits/SRT_CN2_E2_FIRST_TASK_FAMILY_FEASIBILITY_AND_AUTHOR_CHOICE_PACKET_2026-10-08.md
  - Operations/Audits/SRT_CN2_E2_STRONG_H2_SUBSTITUTION_AND_LEAKAGE_AUDIT_2026-10-08.md
tags: [CN2, E2, TaskFamilyA, P1P6, Observability, SourceNative, ModelFairness, Readout, Hold]
---

# CN-2 first family A — P1–P6 observability and E2 identifiability prepass (PAPER ONLY)

> **Verdict: bounded PAPER MAPPING feasible; a fully specified cross-probe E2 held-out comparison is NOT READY.** Some A-family behaviors are directly present in published work; **no checked source here establishes same-subject, same-consequence-history, observed P1–P6 with an actual novel-action P6**. No quantified E2 gain, code run, dataset download, model-arm selection, preregistration, experimental start, canonical claim or CN-3 release. This is a one-file machine analysis under the single merged-main CURRENT NEXT, for independent review.

## 0. Authorization and scope trace

The controlling merged author source, `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_FIRST_E2_TASK_FAMILY_A_2026-10-09.md`, records the exact author choice:

> 顺着来，先 A

This selected **A: consequence-driven multiattribute concept learning as the FIRST CN-2 *paper-only* task family**. After PR #1111 was explicitly merged, the machine proposed the **A-family P1–P6 paper observability audit**; the author's current reply was **"继续"**. The scope is a **bounded paper analysis** using existing source literature, not a new author adjudication of task/model/protocol, author permission to download datasets, or authority to schedule MG-1, code or experiments. **The earlier "CN-2 Option A" is a distinct named-model-comparison adjudication**; both remain in force.

### Hard measurement question before model coding

> For one specified participant's prior lawful stimulus/consequence history, can we define independently observed responses to multiple different probe tasks, and prospectively predict one held-out response type or novel stimulus with a common learned representation *better than capable named H1/H2 alternatives*?

The **response types and training histories are not yet fixed**. A representational geometry is a possible **H2 realization/readout**, not a third mechanism H3 that automatically defeats H2. "Selection" here is not equated to choosing a pre-given category label, attention filter, feedback reward or descriptive state change.

## 1. Source-native prior art and why the stronger comparison is hard

**A1. Nosofsky (1986), GCM/MDS**, [DOI 10.1037/0096-3445.115.1.39](https://doi.org/10.1037/0096-3445.115.1.39), PMID 2937873. MDS-choice model of **human item-identification confusion** related to **classification**, with task-sensitive attention. It does NOT supply P1's free similarity ratings, nor an online feedback-driven trial-by-trial learning process by itself. Cross-task representations and selective-attention adjustment are **mature**.

**A2. Kruschke (1992), ALCOVE**, [DOI 10.1037/0033-295X.99.1.22](https://doi.org/10.1037/0033-295X.99.1.22), PMID 1546117. Error-driven feature-attention and exemplar/category readout updates can predict feedback-based classification. Do not call any learning-dependent reweighting novel, nor weaken ALCOVE to fixed weights.

**A3. Love, Medin & Gureckis (2004), SUSTAIN**, [DOI 10.1037/0033-295X.111.2.309](https://doi.org/10.1037/0033-295X.111.2.309), PMID 15065912. Learned categories can recruit and revise clusters; not a fixed-latent straw rival. **Mack, Love & Preston (2016)**, [DOI 10.1073/pnas.1614048113](https://doi.org/10.1073/pnas.1614048113), PMCID PMC5135299, fitted SUSTAIN to subject classification performance and related model representations to hippocampal fMRI similarity under two feature-relevant tasks. **fMRI RSA is not the human P1 similarity response or P2 label-free grouping**.

**A4. Ashby, Bowman & Zeithamova (2020)**, [DOI 10.3758/s13423-020-01754-3](https://doi.org/10.3758/s13423-020-01754-3), PMCID PMC7415669, explicitly measured human **pairwise 1–6 similarity ratings before and after learning**, feedback-based category learning in Exp. 1 (paired-associate face names in Exp. 2), then **category-label generalization to new blended faces**; postlearning similarity bias predicted generalization performance. Study reports a public OSF data/materials project, [e8htb](https://osf.io/e8htb/). This is **DIRECT P1** and **P6-adjacent unseen-item classification**, **NOT P6 novel action/affordance**. Ratings occurred **before** generalization testing: time order helps prospective description but measurement itself could change learning, so the pair is not automatically a passive independent two-probe readout or a predeclared E2 head-to-head model win.

**A5. Ashby & Vucovich (2016)**, [DOI 10.1037/xlm0000277](https://doi.org/10.1037/xlm0000277), PMCID PMC5097011. Human categorization compared high vs degraded **behavior–feedback contingency** while stimuli, optimal decisions and accuracy targets were matched across conditions. Degraded contingency suppressed learning in many participants. **Source-native job:** feedback contingency matters to categorization. **Not shown:** altered consequence topology simultaneously predicts P1–P6, or SRT Gate/Bearer.

**A6. Carvalho & Goldstone (2022), SAT-M**, [DOI 10.1111/cogs.13128](https://doi.org/10.1111/cogs.13128), model code and fitting-procedure lead [OSF q782h](https://osf.io/q782h/). The **Sequential Attention Theory Model** explicitly adapts item feature encoding to **local temporal training context**. It predicts blocked-versus-interleaved category-learning results and in the paper's compared studies outperformed implementations of ALCOVE, SUSTAIN and a no-local-context ablation. **This is stronger H2/context/history rival pressure**, not proof SAT-M would predict *our unobserved P1–P6* or any consequence-revaluation task; code link is reference only, **not permission to clone or run**.

**A7. Goldstone (1994)**, [DOI 10.1037/0096-3445.123.2.178](https://doi.org/10.1037/0096-3445.123.2.178), PMID 8014612, assessed category-learning effects on **perceptual discrimination**: a P1-adjacent mechanism/behavior, **not direct P1 similarity rating**.

**Scientific consequence:** GCM/ALCOVE/SUSTAIN/SAT-M and feedback-contingency studies already cover substantial portions of representation updating, category generalization, trial order and consequence-sensitive learning. A model that merely predicts new labels from ratings, changes attention after feedback or fits task-dependent neural geometry has **no justified local SRT increment**. No named model has been implemented in this project for a fair all-probe same-target comparison.

## 2. P1–P6 audit table — keep actual observations distinct from model interpretations

Legend: **SOURCE-NATIVE** = the named literature already collected essentially that *human observation* in its own task; **ADAPTABLE** = a similar established behavioral paradigm suggests a paper-defined extra readout but not verified in the named same-context data; **MISSING** = no matching human readout identified in the presently checked A-family sources; **UNKNOWN** = row-level data availability or compatibility unverified. These labels are *source-and-task specific*, not universal declarations about all cognitive science.

| Probe and owner target | Closest verified source-native observation | Current A-family readout status | Example observational interface (PAPER EXAMPLE, not a fixed likelihood) | Strong confound/STOP |
|---|---|---|---|---|
| **P1 similarity geometry:** spontaneously near/far | **SOURCE-NATIVE:** Ashby 2020 1–6 pairwise subjective ratings pre/post learning. GCM identification-confusion and Goldstone discrimination are **adjacent, NOT the same**. | **NATIVE** within Ashby 2020; **UNKNOWN** if raw paired rows usable without file inspection. | Individual ordinal pair rating with per-person threshold/noise; model-produced embedding distances are **not observations**. | Ratings may prime similarity before later P6-adjacent test; physical face similarity and category instruction must be distinguished. |
| **P2 unlabelled grouping/equivalence** | Ashby, Mack and GCM collect or model **given category labels** and classification responses; not spontaneous *label-free* grouping on the same items. | **ADAPTABLE / matching observed P2 MISSING**. | Explicit assignment/partition or pairwise group membership in a separately defined task; if pairs share an underlying grouping, **do not multiply correlated pair ratings as independent**. | A trained label response does not license spontaneous unlabelled equivalence. |
| **P3 interpolated morph / category boundary** | Ashby 2020 uses blended faces and unseen-category transfer; category choices are native, but a *continuous boundary locus* conditional on controlled morph coordinates is not verified as measured. | **ADAPTABLE / morph-boundary locus UNKNOWN or MISSING**. | Anchor-relative forced choice at prespecified morph positions; Bernoulli or multi-choice response conditional on stimulus and participant. | Infer a behavioral boundary only from validated ordered continuum and observed responses; do not substitute latent model coordinates or task-instructed label border. |
| **P4 transition expectation / reachable continuation** | Existing checked A classics focus on category learning/feedback, not direct human probability/choice over **the next event given a partial transition history**. | **MISSING** for the owner P4 in checked sources; sequence order in SAT-M data does not itself equal a subjective next-event report. | Participant next-event choice/distribution given an explicit prefix and allowable events. | If event transitions are not learnable/defined in the stimulus task, P4 is not measurable merely by adding a category label. |
| **P5 anomaly / perceived structural mismatch** | SUSTAIN and SAT-M use error/surprise-like **internal learning signals**, but source-native measurements of the required human subjective unexpectedness under a matched violation probe were **not identified** here. | **MISSING** for reported P5 in checked sources. | Human anomaly judgment or ordinal surprise rating, conditional on equally plausible sensory events with differing learned structural predictions. | Model surprisal, classifier error, RT or pupil changes **do not automatically count as observed conscious surprise**. |
| **P6 action/affordance transfer to untouched combinations** | **Ashby 2020 SOURCE-NATIVE for *new-item category LABEL generalization***; this is a close analog, **not** novel choice of an outcome-relevant action. | **MISSING for action P6; ADAPTABLE only via separately defined action and outcome task**. | Action-choice distribution over **predefined previously learned feasible actions** on an **untouched novel feature/relation combination**, with observable consequences/relevant action goal. | Novel combination != unlearned new action type; impossible to assess an unknown action without a specified affordance/action mapping. Label generalization alone never satisfies owner P6. |

**Net result:** one direct matched source-native *P1* measurement, one direct **category generalization** outcome adjacent to (but distinct from) action P6, conventional classification judgments adjacent to P2/P3, and **no verified P4, P5, or owner action-P6** from the presently inspected studies. The Ashby paper says its underlying data/materials are public; actual **file names, participant keys, complete rows, stimulus mappings, licenses and train/test provenance were not downloaded/audited**. This is an **evidence coverage** verdict, not proof that any future legal data source can never cover all six.

### Sizing P1–P6 without inventing E2 performance

| Paper target | What an existing paper can currently license | What it cannot license |
|---|---|---|
| **Calibration C0** | Describe Ashby's within-study human P1 similarity ratings and later new-face category-label generalization; verify that this behavioral connection is prior art. | **Cannot declare E2 predictive gain**, a new whole-field mechanism or P6 *action* transfer; no model head-to-head has been run. |
| **Calibration C1 (hypothetical later)** | If lawful participant-matched raw OSF rows are inspected with consent, assess whether a **predefined** P1-derived predictor can forecast unseen-category labels in a leakage-safe split and whether capable category learners equal it. | Not automatically an all-six-probe E2 pass; do not fit P1 geometry with held-out category answers, tune using test faces, or claim cross-participant generalization from repeated within-person faces. |
| **Actual owner-target E2** | A paper question about **one learned consequence organization predicting genuinely held-out other observed probes with a common geometry vs named capable H1/H2 implementations** can be *formulated*. | **NOT READY** for a model test: source-native P2/P3 interfaces are incomplete, P4/P5/action-P6 absent here, no protocol/model/data/holdout ledger is frozen. |
| **Future E3/E4/W1–W4** | Can state distinct stronger target and governance requirements. | **No causal/intervention or recursive success** is conferred by C0/C1 or a positive E2 correlation. |

## 3. The smallest honest candidate scientific question (not an authorized experiment)

**Paper candidate Q-A0 — a discriminability / negative-control question:**

> Given a declared *multiattribute, consequence-relevant* learning history and P1/P2 calibration observations, is there any **additional pre-specified held-out P3 boundary or P6 action-choice behavior** that a named, capable shared-organization predictor can prospectively predict **better than** an equivalently informed and trained ALCOVE / SUSTAIN / SAT-M / latent-context competitor?

This is a **conditional candidate**, NOT a claim that data exist, a selected model lineup or author acceptance of a final hypothesis. The **first missing item is an actual measured behavioral target** (especially actual *action P6*, not category generalization) with legitimate training records. If the only accessible target is Ashby's new-face **category label**, rename the paper question to **prior-art calibration / model comparison**, **not** "novel action-transfer E2."

**Two distinct routes must never be fused:**

1. **Existing-source calibration route (no execution approved):** demonstrate that already-published P1 similarity + classification/generalization belong to mature science; later check whether individual/source-level rows, training history and holdouts permit the same behavioral prediction. A fair negative result would be informative as **SOURCE-OWNED AT THIS EXPLANATORY JOB**, not "SRT disproven."
2. **Owner-equivalent future route:** if an independently measured P3 or action-P6 endpoint is necessary, that is **a new measurement design**, with separate author choice and experimental governance; do not fabricate these outputs from the existing OSF catalog or call a computer model's own internal variable a human report.

### Paper-only observation contracts to write *before* any later model choice

For **each claimed probe**, minimally define `subject_id, session, trial_time, stimulus_id, stimulus_features, relation/context_id, action/options (where applicable), learning_feedback_history, condition, probe_type, observed_response, response_encoding`. **Not a claim that these columns exist in any public dataset**.

- **Likelihood/score type (illustrative):** ordinal categorical for P1/P5 ratings; grouped partition/assignment (non-independent within set) for P2; Bernoulli/multinomial for P3; categorical next-event for P4; categorical observed action for P6. Define response calibration and missingness before calling these runnable likelihoods. A probabilistic prediction should be assessed with a proper held-out predictive score and uncertainty, not in-sample embedding fit.
- **Probe-order reactivity:** administering P1, P2 or P3 can **itself change encoding or attention**, and repeated questions can induce explicit category labels; assessment effects may contaminate target P6. Define the actual observation order and distinguish learning `history -> probe` from `probe -> later outcome`; do not assume independent simultaneous passive readouts.
- **World A/B comparability:** matched stimuli or marginal frequencies do **not** automatically match action histories, feedback informativeness, exposure to diagnostic examples, fatigue or policy acquisition. If "consequence" means a changed category correctness signal, state so; **do not infer altered action/outcome topology** from that weaker manipulation.

## 4. Strict evaluation permissions and no-leak contract

A candidate **same-target E2 predictive** future assessment must first have separately declared estimands:

| Split / claim | What must be held out | What cannot be inferred |
|---|---|---|
| **A: new probe type on seen stimuli** | That probe's response values (and preprocessing/selection using them) on test units. Cross-probe inference requires a prespecified or train-only-calibrated **probe observation model** for each contender. | Not unseen-stimulus transfer; a readout trained on the test probe invalidates "cross-probe". |
| **B: new stimulus/feature/relation combination** | Untouched item/combo pool set aside before model selection and training; verify same lawful access across worlds/models. | Not earned merely by probing seen stimulus IDs through new words or labels. |
| **C: forward-time learning/revaluation** | Future outcomes/labels/intervention responses after a specified cutoff; chronology preserved. | No E3 causality or E4 recursive proof just from sequential E2 prediction; later gates remain. |
| **D: new participant/session/context** | Whole participant/session/context blocks at outer test and proper inner tuning, if that generalization is claimed. | No population forecast from randomly split trials of the same participant. |

**Model parity:** named *implementable* H1 per-probe learning, GCM (fitted descriptive attention only at its actual strength), ALCOVE (feedback-learned exemplar attention), SUSTAIN (cluster recruitment), **SAT-M (local sequence-sensitive encoding)**, and any latent-context/structure learner selected later must have declared lawful inputs, feedback, prior structure/learning permissions, model complexity, optimization and same readout access. These are **strongest-neighbor capability candidates, not a frozen lineup or a claim of available code/licenses**. A geometric embedding with learned readouts may itself be an H2 implementation. Permitting one model unobserved P3/P6 labels or a fully task-specific output mapping while denying that training privilege to others invalidates fairness.

**Outcome adjudication, paper-only:**

- **SOURCE-NATIVE / NO LOCAL COMPARATIVE INCREMENT:** only mature cross-task classification/similarity, attention learning, context-specific encoding, neural representational shifts or feedback contingency demonstrated; all already source-owned at those jobs.
- **NOT READY:** matching observed responses, lawful training history, symmetric readouts, withheld targets, capable specified comparator or independent review missing.
- **UNDERDETERMINED:** equal available predictive distributions / H2 reparameterization / unidentifiable latent representations; a pretty geometry is a display choice, not an independent mechanism.
- **POTENTIAL TESTABLE E2 TARGET (NOT PASS):** a fully specified and lawfully observable cross-probe prediction with capable fair named rivals, frozen leakage-safe targets and separate independent review/author experimental authorization still to come. **No positive prediction is asserted**.

**E2 PASS is never awarded merely for compression.** At *comparable held-out predictive adequacy* compression may be a separate, secondary report. The older 09-26 E2–E4 draft §5's "predictive gain OR compression advantage" wording conflicts with the controlling 10-08 author comparator source / programme; this historical phrasing is **not edited here** and cannot be used to lower the current evidential bar.

## 5. Independent review focus and next stop condition

1. **Source fidelity:** verify the difference between Ashby 2020 directly observed P1 and P6-adjacent label generalization, ALCOVE learned attention, SUSTAIN recruitable clusters, **SAT-M 2022 sequence-sensitive encoding**, Ashby–Vucovich 2016 feedback contingency, and Mack's SUSTAIN-fitted fMRI. Confirm none is misrepresented as a complete six-probe same-history experiment.
2. **P1–P6 mapping:** check that P2 unlabelled grouping, P3 continuous morph boundary, P4 next-event *human* expectation, P5 *human* anomaly and P6 true **action** choice are not invented from labels, model surprise, fMRI geometry or subjective perceptions measured in other experiments.
3. **Admissibility and scoring:** ask whether C0 calibration is explicitly weaker than E2, and whether Q-A0 retains owner whole-field purpose without smuggling a new geometry's own readouts as behavioral evidence. Check shared-model vs competitor *training channels* and probe-order contamination.
4. **New strongest-neighbor pressure:** check SAT-M exact explanatory task and source-native ALCOVE/SUSTAIN comparison, plus Ashby–Vucovich's feedback-contingency experimental control, without converting paper results into SRT anti-novelty proof.
5. **Authorization:** is this still one machine_analysis / noncanonical audit under the merged first family A? No new author decision, experiment, benchmark run, data download, prereg, STATUS second NEXT, MG-1 review schedule or canon edits?

**Stop here after presenting the audited matrix and paper Q-A0.** Further steps (actual OSF file-level data access, probe schema freeze, model implementations, feedback-intervention or experiment) need additional scoped author instruction and existing independent FR-ADV/experiment gates as applicable. This prepass is **not a new CN-3 work package**, and it cannot close MG-1, MG-2, E2, E3, E4 or the Bearer/Concern O3 question.

## 6. 外部对照三项

1. **事实冲突：** 无（本轮已核材料范围内未发现作者陈述与实证事实的冲突）。本审计纠正的是候选测量可用性过度概括的风险；没有读取任何完整公开数据表，更没有给出新的实验结果。
2. **内部矛盾：** 无（本轮已核范围内未发现新的作者陈述矛盾）。既有09-26 E2草案“压缩或预测PASS”与后续作者“预测PASS、压缩另列”的运行措辞冲突保留为另外的定点修正。
3. **已有说法：** Nosofsky/GCM的辨识->分类空间、ALCOVE/SUSTAIN的反馈注意/类别簇、Ashby 2020的相似度->新类别泛化、Ashby–Vucovich 2016的反馈关联条件，以及**Carvalho–Goldstone 2022 SAT-M的局部顺序驱动编码变化**，与本路线多个局部说明**高度或部分重合**。这阻止这些局部工作被直接标为SRT新增贡献，但不提前裁决其更广泛本体问题。
