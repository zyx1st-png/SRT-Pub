---
id: SRT-CN2-A-PUBLIC-DATASET-P6-E2-FEASIBILITY-TRIAGE-20261011
type: audit
status: draft
canonical: false
layer: operations
epistemic_layer: machine_analysis
claim_mode: bounded_public_metadata_feasibility_triage
created: 2026-10-11
updated: 2026-10-11
research_mode: U
root_question: Can an existing public human-behavior corpus instantiate first-family A consequential choice on untrained combinations and independent cross-probe E2 prediction without information leakage?
comparative_claim: no SRT empirical gain; strong mature prototype-action-reward and policy learning precede this candidate
named_comparator: null
n_mode_triggered: false
dependency:
  - STATUS.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_FIRST_E2_TASK_FAMILY_A_2026-10-09.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_P6_CONSEQUENTIAL_INDEPENDENT_ACTION_2026-10-11.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CN2_NAMED_MODEL_FAIR_COMPARISON_2026-10-08.md
  - Operations/Audits/SRT_CN2_A_P1_P6_OBSERVABILITY_IDENTIFIABILITY_PREPASS_2026-10-09.md
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
tags: [CN2, E2, FirstTaskFamilyA, P6, PublicData, Feasibility, InstrumentalAction, StrongH2, FirstEncounter, Hold]
---

# CN-2 family A — public dataset feasibility triage for consequential choice and genuine cross-probe E2 (2026-10-11)

> **Verdict: TWO-TRACK PAPER GO, EXPERIMENT/MODEL RUN NO-GO.** Several public human datasets **may** support *specific* learned-action-choice calibration or first-transfer prediction, especially Pettine et al. (2023) and Klein et al. (2017); the Dryad Ben-Artzi et al. (2023) landing page explicitly documents raw trial-wise actions/rewards and participant keys. **No examined source demonstrates a single verified participant-matched P1/P2/P4-training + P3/P5/P6-held-out, novel combination, consequence-validated six-probe corpus. E2 FULL-TARGET NOT READY.** This is **metadata/publisher-method READ-ONLY**; public data files/code were **not downloaded, opened, parsed, executed, or fitted**. One noncanonical paper audit, not a new CURRENT NEXT or endorsement of a particular experiment or model.

## 0. Scope, authority, and source verification level

- Merged #1111 selected **first CN-2 paper task family A**; merged #1112 adjudicated that **P6 is a freely/independently chosen human action with actual task consequences on a novel combination**, **not mere category labeling**, and that E2 scores the **human FIRST choice**, with realized environment outcome **only verifying task consequence/feedback chronology**. The author then said `继续` to proceeding with the expressly proposed **concrete A-family public-data feasibility investigation**. It authorizes **bounded source/metadata investigation**, **NOT** data download, code, preregistration, participant recruitment, named baseline selection, task freeze, CN-3 release or merge.
- **Evidence levels:** `ARTICLE` = human task/method as published; `CATALOG` = repository landing page, named published data link or README metadata; `ROW-CHECKED` = actual participant-level files inspected (there are **ZERO** of these in this prepass). `CODE-CATALOG` = publisher lists model or task code only, not independently executed or licensed for us. Avoid treating a DOI, a catalog file listing or a paper's model result as row-level verified dataset compatibility.
- The author chose only broad P6 **independent consequential action**; **a meaningful virtual/point/resource consequence might qualify** if genuinely contingent on independent goal-relevant action. A correct-label point tally does **not by itself** supply that independent choice. This dataset audit does **not** silently select a blanket numeric-reward prohibition, an external physical outcome requirement, or a new P6 outcome likelihood.
- **First-encounter leakage guard** applies to P6: one first independent action per **participant × exact reserved novel feature/relation combination** *before any same-combination consequence feedback*; timestamp action, actual realized outcome and **feedback visibility**. P3/P5 on that combination must be explicitly tagged before choice, after choice/before feedback, or after feedback; post-feedback responses cannot be counted as naïve heldout transfer.

## 1. Dataset/source-native candidate ledger (no files acquired)

### D1. Pettine, Raman, Redish & Murray (2023): **first inspect metadata/row-contract — HIGHEST methodological adjacency**, NOT a verified E2-ready corpus

- **SOURCE:** `ARTICLE` [Human generalization of internal representations through prototype learning with goal-directed attention](https://doi.org/10.1038/s41562-023-01543-7), *Nature Human Behaviour* 7, 442–463 (2023). Publisher explicitly describes **three human latent-state learning tasks**, **multiattribute features and goal-oriented discriminative attention**, **instrumental action–reward feedback**, and generalization to novel situations; a majority of human behavior is modeled by a **prototype representation plus goal-directed discriminative attention**. Source-native local prior art on nearly the **same conceptual target**.
- **DATA LEAD:** `CATALOG-POINTER ONLY` [Zenodo record 7186975](https://zenodo.org/record/7186975), as explicitly named in publisher Data Availability; **this record's content/participant keys/file columns were NOT accessible/inspected** in this research pass. `CODE-CATALOG` publisher also identifies [instrumentalLatentStateLearning](https://github.com/murraylab/instrumentalLatentStateLearning), [alienArtifactsLearningTask](https://github.com/murraylab/alienArtifactsLearningTask), and model-intuition notebook. These links are **not a selected runnable arm** or code execution permission.
- **P6 fidelity:** action–reward learning with multidimensional stimulus generalization is particularly promising; **UNKNOWN** if there is a genuinely **reserved first action on an unseen combination**, action-outcome causal contingency specifically at that test trial, outcome/feedback timing and symmetric model access. Publisher source does **not establish** all requested P1–P6 human reports; **NO claim of observed P1 free similarity, P2 label-free grouping, P4 subjective next-event, or P5 human anomaly**.
- **Threat/strongest H2:** **ProDAtt / ExDAtt-like prototype-plus-goal-discrimination**, exemplars and latent context/attention structure are **DIRECT strongest-neighbor competitor families**, not just weak fixed-weight GCM/ALCOVE. The paper reports fitting mature behavior; do not rebrand learned prototype/action mapping as novel SRT Selection.
- **Triage:** **P1 priority for later file-level lawful row/schema audit**, not "dataset selected", no PR experimental permission.

### D2. Klein et al. (2017): **strong first-encounter transfer calibration with public behavioral supplement**, not six-probe E2

- **SOURCE:** `ARTICLE` [Learning relative values in the striatum induces violations of normative decision making](https://doi.org/10.1038/ncomms16033), *Nature Communications* 8:16033 (2017). Human participants learned option values in fixed pairs, then were **first tested on cross-pair transfer choices** (TYPE I/II). The published analyses specifically focus on **the first transfer trial**, before fresh pairing feedback could drive relearning. A relative-value learner and absolute-value learner make different first-transfer predictions; the **relative learner is an existing source-native success**, not an SRT advantage.
- **DATA:** `CATALOG` paper **states behavioral raw data are in Supplementary Information**, while fMRI and analysis code are available by request; **supplementary file rows/format not inspected** here. A publication's supplementary link is not proof that our first-choice/feedback time fields are complete.
- **P6 resemblance:** new pairing of *previously experienced options* after reward feedback is a particularly natural **novel combination × first-choice** audit candidate. **UNKNOWN** whether the relevant first-transfer test action had a realized consequential result and whether outcome/feedback visibility and exact participant-level key fields suffice for the author's **actual consequence** criterion. It is a **first transfer behavior** precedent; do NOT pretend all P1–P6 probes were measured.
- **Threat:** strong relative value, context and policy learning. Avoid strong claims of novelty about "choice over a new pair after different reward histories".
- **Triage:** **P2 priority for later supplement/schema inspection**, conditional on data-use terms.

### D3. Ben-Artzi, Kessler, Nicenboim & Shahar (2023): **best concrete column-level catalog**, not proof of unseen-combination transfer

- **SOURCE/CATALOG:** Dryad [Computational mechanisms underlying latent value updating of unchosen actions](https://doi.org/10.5061/dryad.d51c5b08d), *Science Advances* [doi:10.1126/sciadv.adi2704](https://doi.org/10.1126/sciadv.adi2704). Dryad landing metadata documents `df_raw.csv` (3.04 MB), `df.rdata`, README, **178 retained participants** (after exclusions), **40,601 raw rows, 14 variables**, four blocks × 50 nominal trials with four fractal cards per block, two randomly offered choices per trial. Win/loss play dollars and a performance-dependent cash bonus give **actual instrumental reward consequences**.
- **SOURCE-NATIVE fields from Dryad README (NOT verified by CSV download):** `subj, prolific_id, blk, trl, frcA, frcB, key, ch, rw, cond, rt, prob1, prob2, bonus`. Recorded **choice, offered actions/cards, reward, trial order, subject IDs** support narrow **choice–reward chronology**, though the exact result display time is not listed. The card-pair space in each block has only four cards; **novel pair status is not established**, random offers can repeat, and first visit to a pairing must not be conflated with a new *multiattribute feature conjunction*.
- **Strongest H2:** author's own **select/reject and double-updating value models** (documented in the dataset README) plus capable action-value/policy models; no common P1/P2/P4 -> P3/P5/P6 human observation battery.
- **Triage:** **P3 priority as a low-overhead column-level action-feedback audit/control** if authorized later. **Calibration / H2 pressure only** until new-combination and true multiattribute structure can be proved. Do NOT infer a named six-probe split from the README.

### D4. Tanaka, Tavera, Haider & Tanaka (2026): **strong prior art for voluntary choice generalization; test consequence unverified**, so NOT automatically P6

- **SOURCE:** `ARTICLE` [From exemplars to categories: generalization of action-effect learning in a free-choice task](https://doi.org/10.1007/s00426-026-02347-w), *Psychological Research* 90:133, **published 2026-07-11**, four human experiments. During **learning**, a freely chosen F/J key **produced a category-associated image**. **Test** presents **untrained category exemplars** and participants freely choose F/J in a Go/No-go task; each novel image is used **once per block**, **four blocks** (so only its **first occurrence per participant** can qualify as a naïve new-item response). Evidence for group-level choice-congruency transfer is partly driven by near-deterministic subjects and weakened after exclusions.
- **DATA LEAD:** `CATALOG-POINTER ONLY` publisher reports data and R/JASP analyses at [OSF 624NE](https://osf.io/624ne/), DOI [10.17605/OSF.IO/624NE](https://doi.org/10.17605/OSF.IO/624NE). Raw participant columns not inspected.
- **P6 validity caveat:** *Learning-phase keypress* visibly causes images; **test-phase F/J choice is reported as a free response to an image, and the test-phase method does NOT describe new actions producing a corresponding task consequence**. Do **not** conflate training action effects with **actual consequences of the first test choice**; a voluntary response under a Go task may lack the author's independent consequential P6 outcome. Also the study's novel exemplars are new *members of known categories*, not verified novel **feature/relation combinations**.
- **Triage:** direct **choice-generalization H2/prior-art** reference, **NOT proven P6-qualifying**. Excellent negative control for overstating "action" in titles.

### D5. CPC18: large-scale consequential choice data, **not the owner shared multi-probe battery**

- **SOURCE/CATALOG:** Zenodo [All raw data for CPC18](https://doi.org/10.5281/zenodo.2571510) (2019). Public catalog lists one raw CSV **65.4 MB** and a **198.8 kB dictionary**, overall **694,500 consequential human decisions** across risk, ambiguity and decisions from experience, plus competition training/testing sets. These are corpus/competition splits, **not automatically participant-level first unseen-conjunction feedback embargoes** or P1/P2/P4 measurements. Existing choice prediction competitions contain strong decision-theory baselines and prior scoring experience.
- **Triage:** supplementary **H1/H2 choice-prediction stress-test lead** only; no evidence same-subject perceptual/probe labels, novel-combination first encounter, or shared six-probe training is present. Raw rows/dictionary content not inspected.

### D6. Zhang, Paily & Maloney (2015): **excellent novel-combination choice-task method**, public trial data NOT established

- **SOURCE:** `ARTICLE` [Decision from Models: Generalizing Probability Information to Novel Tasks](https://doi.org/10.1037/dec0000022), *Decision* 2(1):39–53. Virtual minefield: participants chose shorter/safer/lower-reward versus longer/riskier/higher-reward paths; **160 feedback training trials** followed by **600 new path-length/reward-combination test choices with NO feedback**. Researchers compared nine decision models, and exponential hazard models explain many choices. The absence of **test feedback** helps prevent same-combination outcome learning, but **source description does not verify that an actual task consequence was realized for each test choice**, so **consequential P6 validity remains UNDERDETERMINED**, not PASS. Source-specific concrete stimuli and old model comparison are prior art.
- **DATA:** paper/method located; **no independent public row-level repository verified**, no raw data inspected. This is a **design/reference lead**, not a dataset-ready result.

### D7. Tabrik et al. (2026): **cross-modal P1/category comparator, explicit participant mismatch**

- **SOURCE:** `ARTICLE` [Larg-scale multimodal fMRI dataset of visual and haptic 3D object category learning](https://doi.org/10.1038/s41597-026-07814-y), *Scientific Data* 13:1064, **published 2026-07-16**. Study reports **134 participants**: **50** did a similarity-rating task, while the **remaining 84** performed a category-learning experiment in unimodal/crossmodal conditions. Source advertises public data including similarity-rating data at [Mendeley 8k7ys2xw4h](https://data.mendeley.com/datasets/8k7ys2xw4h/1), and neuroimaging data.
- **CRITICAL NOT-SAME-SUBJECT:** similarity ratings and category trials **are separate participant groups** in the described dataset. Do **NOT** join their observations into fictitious same-person P1-to-P6 cross-probe conditioning, and do not substitute fMRI RSA for human P1 or categorical crossmodal transfer for independently consequential P6.
- **Triage:** good **P1/crossmodal literature comparator** and **negative join-test**, not owner-E2.

## 2. Comparison table: eligibility evidence, not fabricated adequacy scores

| Lead | Independent human consequential choice source? | New combination / first-encounter evidence? | Multiple independent P1/P2/P4 input probes from SAME subject? | Public data/column evidence checked | Paper judgement |
|---|---|---|---|---|---|
| **Pettine 2023** | Action–reward learning SOURCE-NATIVE | **Partial ARTICLE; exact heldout combination and feedback unknown** | **NO evidence** | Publisher says Zenodo data; files **NOT OPENED** | **P1: inspect next** (conditional) |
| **Klein 2017** | Rewarded option choice SOURCE-NATIVE | **ARTICLE YES first cross-pair transfer; outcome at test UNKNOWN** | **NO evidence** | Supplementary behavioral data declared; rows NOT OPENED | **P2: inspect next** (conditional) |
| **Ben-Artzi 2023** | **YES**, choice + reward, performance bonus | **UNKNOWN**; 4 cards/block repeating pairs possible | **NO evidence** | **Strong catalog README field schema**, NOT raw file read | **P3: controls** |
| **Tanaka 2026** | Training action-effect YES; **test consequence UNKNOWN/unreported** | New *category exemplars* and first exposure; not guaranteed novel feature conjunction | **NO evidence** | OSF link declared, not inspected | Prior-art / **NOT P6 established** |
| **CPC18** | **YES** risk choices described as consequential | **UNKNOWN** participant × exact combination | **NO evidence** | Zenodo file/dictionary sizes verified, rows NOT READ | Other-task calibration |
| **Zhang 2015** | Feedback-phase reward YES; test consequence UNCLEAR | **YES article novel test path/value combinations** | **NO evidence** | **No raw-row dataset verified** | Methodological neighbor |
| **Tabrik 2026** | Category learning, **not independent P6 action** | Not material for owner-P6 | **NO: similarity and category groups DISJOINT** | Publisher data locations only | Negative same-subject match |

**Interpretation:** the `P1/P2/P3` labels above are **inspection priority order**, NOT SRT P1/P2/P3 probe identifiers. Source-native `YES` is limited to the named source task and its evidence class. Most rows have unknown actual **first test consequence** and **no joint multi-probe human observations**. No "several sources jointly form one participant's P1–P6" shortcut is permitted.

## 3. Exact next file-level eligibility questions — PAPER PRIORITIES, not permission to acquire files

**Pettine / Klein before Ben-Artzi**, chosen for **information value of a narrow later inspection** if the author separately permits accessing specific public data files. Keep two disjoint scientific products:

### Track C — source-native / mature-model calibration (NOT SRT E2)

A truly observed first choice/action-reward dataset can support **calibrating or challenging a mature H2's own declared task**. It can reveal that a prototype, relative value, action policy, or model-based learner already predicts the first behavior under precisely the information available. If the winner is a mature H2, register **NO LOCAL COMPARATIVE INCREMENT** at this narrow job; not a falsification of the philosophical SRT root. Avoid posthoc SRT geometry construction using test choices and calling it a new forecast.

### Track E — owner-style shared-geometry E2 (NOT READY)

The existing proposal `P1 + P2 + P4 -> held-out P3 + P5 + P6` remains only a **candidate**. The necessary **individual source-vetted** fields, if ever available, would include:
`subject_id, training_condition, chronological_action_feedback_history, stimulus_feature_vector, novel_conjunction_id, first_encounter, available_actions, prechoice_goal, chosen_action, action_time, actual_task_effect_for_VALIDATION, consequence_occurrence_time, feedback_visible_time, P1_rating_human, P2_group_human, P4_next_event_human, heldout_P3_boundary_human, heldout_P5_anomaly_human, P6_human_first_action, probe_time_order, allowed_competitor_inputs`.
**These are a DESIDERATA schema, not columns verified in any cited dataset.**

**Critical data-use/measurement questions before any code:**

1. **Same subject and same learned world?** Cross-study collages of P1 in one cohort and P6 in another cannot count as within-person shared-geometry evidence.
2. **Novelty index?** Verify whether the actual reserved unit is *novel item*, *novel pair of learned actions*, *new conjunction of features/relations*, *new task context*, or simply repeated stimulus. A first `A versus C` pair can be new even if A/C individually appeared; it need not equal the author's stronger new-feature conjunction without explicit owner-compatible task definition.
3. **Consequential action validity vs environment forecast?** Human **first chosen action** is the E2 scoring target. Realized result is used to certify action has operational consequences and when feedback was visible; no joint scoring of environment reward/noise as a second "human P6" response.
4. **Feedback embargo / probing intervention?** Require first encounter per participant × exact reserved combo, action before same-combination feedback; track P3/P5 as pre-choice, after-choice/pre-feedback, or post-feedback. **Feedback-naïve only before feedback**; repeated trials must be typed as learning-after-feedback, not mixed with first transfer.
5. **Strong model parity:** candidate rivals include **ProDAtt/exemplar/prototype with task-discriminative attention (Pettine), relative-value learner (Klein), model-based action policy, successor/latent-state inference as task-suitable**, in addition to GCM/ALCOVE/SUSTAIN/SAT-M only where source-task compatible. **Do not freeze a runnable lineup from this list**. Each gets symmetric train-only probe-to-choice observation mapping, reward/action histories, learnable latent structure and budgets.
6. **Prespecified evaluation units:** outer sealed item-combination/participant/time/probe split as separately claimed; no feedback-test leakage, no repeated participant identical combo showing up in both train and heldout. If a candidate has only single behavior type `choice`, it cannot support joint-multi-probe E2 irrespective of predictive success.
7. **Legal/extraction readiness:** inspect license/consent/use terms, code/data version, anonymous subject keys, original versus preprocessed data, per-row actual feedback visibility and training histories. **No claim of full legal or file compatibility has been established here**.

## 4. Practical decision and stopping points

- **PAPER GO:** source- and repository-level **manifest/schema inspection PLAN** centered on **Pettine 2023**, **Klein 2017** and **Ben-Artzi 2023**, in that order for scientifically distinctive questions, not implementation ease. Any actual data access/reproduction remains separately authorized.
- **Mature-neighbor warning:** **Pettine's prototype-plus-attention learning** is likely a stronger task-adjacent alternative than artificially weak fixed-space category learners. **Klein's first-transfer relative-value model** is already a direct successful competing forecast. If both reproduce the source task, this removes claims of SRT originality for these local phenomena.
- **NO-GO for full E2:** no checked cohort has all three key ingredients concurrently: independently measured several input probes, truly reserved human first consequential choice under feedback firewall, and separately observed held-out other probe responses linked to the same context.
- **HOLD:** no new algorithm, participant recruitment, data ingestion, task code, model fit, E2 success statement, E3/E4/W1–W4 claim, CN-3/toy experiment, canonical/Gate/Bearer revision, or second CURRENT NEXT is authorized by this packet.
- **Independent review:** confirm source boundaries (especially Pettine raw file access NOT CHECKED; Tanaka test actions vs learning effects; Tabrik disjoint cohorts), mature H2 inventory and no phantom P1–P6 joins; require new source/author permission before promoting Track C/E to data work.

## 5. 外部对照三项

1. **事实冲突：** 无（对本轮核查的公开论文/仓库目录范围）；已发现多份候选足以反驳“该类行动迁移完全无人研究”的粗泛说法。没有读取原始数据行，因此**不能确认任一候选直接符合完整P6/E2标准**。
2. **内部矛盾：** 无（本轮已核范围）。持续保留作者“有实际后果的独立行动”裁决与较新的P6行为预测口径；环境实际结果仅为后果有效性与反馈时序证据。**C0/C1属于Q-A0来源校准阶段，Q-A1为多探针E2条件性研究问题**。
3. **已有说法：** Pettine 2023的目标导向原型/维度注意学习、Klein 2017的相对价值首轮新配对迁移、Ben-Artzi 2023的未选行动潜在价值更新、Tanaka 2026的行动效应到新类成员泛化，以及Zhang 2015的新路径—奖励组合选择，分别与方案A不同的局部行为假设**部分或高度重合**。是否存在SRT专有的跨探针增量，仍需具名强模型与合法留出数据严格对照。
