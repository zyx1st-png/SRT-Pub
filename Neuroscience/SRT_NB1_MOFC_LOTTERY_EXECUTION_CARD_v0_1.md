---
id: SRT-NB1-MOFC-LOTTERY-EXECUTION-CARD-V0-1
type: execution_card
status: active
version: v0_1
canonical: false
claim_level: P4
claim_mode: lab_hypothesis
layer: neuroscience_lab
epistemic_layer: bridge
created: 2026-08-12
updated: 2026-08-12
parent_contract: Core/SRT_Core_14_Dynamics_Scaling.md
parent_audit: Operations/SRT_NEURAL_NORMALIZATION_BEHAVIORAL_SELECTION_FLOOR_AUDIT_2026-08-12.md
preregistration_status: execution_card_defined_not_formally_locked
execution_status: not_started
w0_status: access_inventory_complete_request_draft_not_sent
ai_do_not_use_for_definition: true
dependency:
  - Core/SRT_Core_14_Dynamics_Scaling.md
  - Operations/SRT_NEURAL_NORMALIZATION_BEHAVIORAL_SELECTION_FLOOR_AUDIT_2026-08-12.md
  - Neuroscience/SRT_Neuroscience_Claim_Status.md
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
tags: [Neuroscience, P3-Scale-NB1, P4, divisive-normalization, mOFC, lottery-choice, execution-card]
---

# NB1-MOFC-Lottery-v0

## Neural divisive normalization → frozen readout → task-level saccadic choice

> **Status:** P4 execution card defined; formal lock not completed; execution not started. This file is not a canonical definition source and does not upgrade `P3-Scale-NB1` to green.

---

## 0. Scope and one-connection rule

This card tests exactly one bounded connection:

> In a cued lottery task, estimate divisive-normalization parameters from mOFC neural data, freeze the candidate map and population readout, and test whether the resulting distribution predicts held-out risky/safe saccadic choices better than preregistered rivals; a local P3 pass additionally requires a neural intervention to produce the predicted denominator-dependent neural and behavioral shift.

The permitted chain is:

`mOFC divisive-normalization parameters → frozen population readout → risky/safe saccadic choice distribution`

This card does **not** test or establish actualisation, agency, subjecthood, consciousness, free will, moral status, or a general neural-to-behavioral identity. The historical task labels “free choice” and “forced choice” describe trial instructions only; they are not SRT claims about real choice or agency.

### Burden labels

| Link | Burden | Current status |
|---|---:|---|
| offered candidate values → relative mOFC response under an explicit model and time window | D + C | supported as a model candidate; not uniquely identified |
| relative mOFC response → frozen task-action distribution | C + P3 | untested under the full anti-circularity contract |
| neural intervention → predicted parameter shift → predicted behavior shift | P4 | protocol candidate only |
| completed data satisfy all gates | O | not yet evaluated |

---

## 1. Evidence roles and non-composition guard

The following sources constrain different parts of the card. They do not form one completed experiment and may not be spliced into a green verdict.

| Source | Permitted role | What it does not supply |
|---|---|---|
| Yamada et al. (2018), *Nature Communications* | awake-monkey lottery-task and mOFC divisive-normalization feasibility anchor; candidate task/model source | simultaneous population readout, frozen neural-to-choice test, or neural intervention |
| Ballesta et al. (2020), *Nature* | causal OFC microstimulation feasibility and intensity-specific control anchor | divisive-normalization parameter identification or the present task/readout |
| McGinty & Lupkin (2023), *Nature Neuroscience* | simultaneous OFC population and trial-wise choice-readout feasibility anchor | proof that divisive normalization generated the decoded choice signal |
| Keung et al. (2020), *Nature Communications* | behavioral divisive-normalization/DDM comparison and negative-control anchor | neural measurement or neural intervention |
| Bavard & Palminteri (2023), *eLife* | strong range-normalization rival and task-dependence warning | direct same-task refutation of mOFC divisive normalization |

**Non-composition rule:** results from different animals, tasks, laboratories, recording modes, and interventions cannot be composed into a `P3-Scale-NB1` pass. A pass must occur inside one preregistered workline with an explicit candidate map, frozen readout, held-out test, rival set, tolerance, and intervention.

---

## 2. Two execution lanes

### Lane A — retrospective feasibility

W0 access/provenance record: `SRT_NB1_W0_DATA_ACCESS_PROVENANCE_2026-08-12.md`. Public-source review found an author-request data route but no confirmed public trial-level dataset or code repository. The request is drafted but not sent; Lane A access remains unknown.

1. Request trial-level neural and behavioral data and analysis metadata for the Yamada et al. workline.
2. Reproduce the published neural model comparison.
3. If trial structure permits, construct a leakage-safe neural-to-choice analysis with neural parameters estimated independently of held-out choice outcomes.
4. Treat non-simultaneous single-unit pooling as a pseudo-population sensitivity analysis only.

Lane A can expose non-identifiability, leakage, insufficient power, or task-design defects. It cannot turn the bridge green because it lacks a within-workline neural intervention and may lack simultaneous population structure.

### Lane B — prospective decisive study

Run a new nonhuman-primate lottery task with simultaneous mOFC population recording, neural-only parameter estimation, a frozen behavioral readout, preregistered range and non-normalization rivals, and an interleaved low-current OFC microstimulation manipulation after calibration, power analysis, ethics approval, and parameter-recovery simulation.

Lane B is the preferred route to a local P3 verdict. No sample size is fixed in v0.1; it must be derived before preregistration from simulation-based recovery and minimally relevant predictive/intervention effects.

---

## 3. Research question and hypotheses

### Primary question

Does a neural divisive-normalization model estimated independently from mOFC activity support a frozen readout that predicts held-out task choices and tracks a neural intervention better than declared rivals?

### Confirmatory hypotheses

- **H-N (neural model):** the divisive-normalization model has better held-out neural predictive performance than the preregistered range-normalization, subtractive/difference, and absolute/linear rivals.
- **H-R (frozen readout):** neural-derived scores passed through a frozen readout predict held-out risky/safe choices within `ε_NB` and outperform the best preregistered behavioral rival by the minimum practical gain fixed at formal lock.
- **H-I (intervention):** low-current OFC microstimulation changes independently estimated neural normalization parameters, and the frozen readout predicts the direction and context dependence of the resulting behavioral change.
- **H-D (denominator discrimination):** the intervention effect interacts with alternative/total offered value in the direction predicted by the fitted denominator term, rather than appearing only as a context-independent value boost, arousal shift, or motor bias.

Failure of any confirmatory hypothesis blocks a full local P3 pass. Exploratory patterns may motivate a revised P4 card but may not be used to rewrite this card after outcome inspection.

---

## 4. Task, candidates, and event boundary

### Task skeleton

- Each trial offers a risky and a safe lottery; the registered action set is `A = {saccade_risky, saccade_safe}`.
- `X_N` contains the neurally encoded offer candidates; `X_B` contains the task-labelled risky/safe candidates.
- `π_X:X_N→X_B` is the candidate-identity map. Screen side, cue order, and offer order are counterbalanced so that identity is not reducible to motor direction or presentation order.
- Trial contexts must vary, preferably factorially: focal expected value, alternative/total offered value (denominator manipulation), payoff range (range-normalization rival), and free/forced instruction as task labels.

### Observed choice event

An observed choice is a target-directed saccade entering the preregistered target region and satisfying the preregistered dwell and latency criteria. Omission, fixation break, anticipatory movement, ambiguous landing, and invalid-trial outcomes remain separate event classes; they may not be imputed as risky or safe choices.

The exact cue-aligned valuation window, stimulation window, saccade thresholds, regions of interest, and exclusion rules must be frozen at formal lock using the validated laboratory SOP. Until then, `π_R[N_η(x)]` denotes only a choice distribution—not a realized action event.

---

## 5. Model objects and frozen readout

### Neural candidate

A primary neural candidate, adapted to the task and neural likelihood, is:

\[
r_i
=
R_{\max,i}
\frac{\beta_i + EV_i}
{\sigma_i + EV_i + EV_j}.
\]

The observation model for spikes or firing rates, parameter hierarchy, regularization, and time window must be explicit. `η` denotes all neural normalization parameters and is estimated from neural training data without held-out choice labels.

### Candidate map and population representation

- `N_η:X_N→R_N` produces the neural response representation.
- `π_X` maps neuron/offer identity to the risky/safe task candidates.
- Simultaneous population activity is required for the confirmatory Lane B result. A pseudo-population may be reported only as exploratory and cannot support a green verdict.

### Frozen readout

The primary readout is a preregistered two-stage object:

1. Construct risky and safe population scores from the neural model without using outer-test choices.
2. On the behavioral training partition only, estimate the minimal calibration parameters `a,g`:

\[
P(\text{risky}\mid x)
=
\operatorname{logit}^{-1}
\left(a+g[s_{\text{risky}}(x)-s_{\text{safe}}(x)]\right).
\]

Freeze `η`, `π_X`, the score construction, `a`, `g`, preprocessing, and all decision rules before evaluating the outer test partition. No condition-specific refit, post hoc relabelling, or test-set calibration is allowed.

---

## 6. Split, freeze, and leakage control

- Use grouped outer splits by animal, session, and payoff block as supported by the final design; never rely on random trial splits that leak session or block structure.
- Estimate `η` from neural training data only.
- Estimate `a,g` from training choices only after neural score construction is fixed.
- Select rival hyperparameters inside the training partition by nested validation.
- Freeze the outer split, exclusions, missing-data rules, outlier rules, preprocessing, candidate identities, neural window, readout, distance, tolerance, and adjudication script before outer-test evaluation.
- Report animal-level and session-level variation; pooled accuracy alone is insufficient.

The exact split unit and allocation remain **formal-lock items**, not analyst discretion during execution.

---

## 7. Metrics, tolerance, and discriminating gain

### Neural metric

Primary neural comparison: held-out log predictive density under the preregistered spike-count or firing-rate likelihood. Report calibration and residual structure in addition to aggregate score.

### Behavioral metrics

- Primary: held-out log loss / cross-entropy.
- Secondary: Brier score, calibration curve, and condition-cell prediction intervals.
- Bridge discrepancy: a preregistered distributional distance `D`, provisionally weighted Jensen–Shannon divergence over registered condition cells.

### Tolerance

`ε_NB` is not a universal constant and may not be chosen after seeing model error. At formal lock it must be derived from a behavioral reliability/noise-ceiling procedure, provisionally the 95th percentile of a clustered split-half or bootstrap discrepancy distribution under repeatable conditions.

### Rival gain

A pass requires improvement over the best preregistered rival, with an animal/session-clustered confidence interval excluding zero and exceeding a minimum practical gain selected before confirmatory analysis from recovery and power simulations. v0.1 intentionally contains no invented numeric threshold.

---

## 8. Rival set

### Neural rivals

1. range normalization;
2. subtractive or value-difference coding;
3. absolute/linear value coding;
4. a flexible but complexity-penalized neural baseline fixed at formal lock.

### Behavioral rivals

1. direct objective-expected-value softmax;
2. rank-based choice;
3. drift-diffusion, race, or leaky-competing-accumulator family selected before execution;
4. a flexible policy model used as a predictive ceiling, not a mechanistic winner by default.

### Intervention rivals

1. context-independent subjective-value boost;
2. global gain/arousal or motivation change;
3. cue visibility or sensory perturbation;
4. motor/saccade bias;
5. nonspecific high-current disruption.

Model complexity, likelihood family, parameter pooling, and comparison criterion must be matched or explicitly adjusted. A normalization label does not win merely by having more degrees of freedom.

---

## 9. Intervention and causal discrimination

The prospective study uses calibrated **low-current** OFC microstimulation as the primary causal candidate. High-current effects are treated as nonspecific disruption controls and cannot by themselves support H-I.

### Required structure

1. Hold the focal offer value constant while varying the alternative/total offered value.
2. Independently vary payoff range to separate divisive-denominator and range-normalization predictions.
3. Estimate the stimulation-related change in neural parameters in a calibration partition.
4. Freeze the changed parameter vector and propagate it through the frozen readout to predict behavioral direction, magnitude, and context interaction.
5. Evaluate the prediction on held-out stimulation trials.

### Control channels

Pupil, fixation stability, reaction time, saccade metrics, cue visibility, reward history, stimulation artefact, session drift, satiety/motivation, and general response variability must be measured or blocked as appropriate. If recording artefact prevents simultaneous neural estimation during stimulation, the calibration design and temporal separation must be preregistered; behavioral effects may not be reverse-engineered into an inferred neural parameter shift.

---

## 10. Adjudication gates

### Full local P3 pass — green

All five conditions are necessary:

1. the neural divisive-normalization candidate wins the held-out neural comparison;
2. the frozen neural-to-behavior readout satisfies `\mathcal E_{NB}≤ε_{NB}`;
3. it exceeds the minimum practical predictive gain over the best preregistered rival;
4. the neural intervention changes independently estimated neural parameters and produces the preregistered denominator-dependent behavioral effect through the frozen readout;
5. the result survives leakage checks, negative controls, and animal/session sensitivity without condition-specific refitting.

### Partial result — yellow

Yellow includes any of the following: neural model and frozen readout succeed but the intervention is absent; intervention direction succeeds but neural parameter identification is ambiguous; effects are underpowered; only a pseudo-population is available; or rival discrimination remains unresolved.

### Failure / downgrade — red

Red follows if the best rival wins, the frozen readout misses `ε_NB`, the intervention changes behavior without the predicted neural/context signature, results require test-set recalibration, or the apparent effect is explained by arousal, sensory, motor, range, or session confounds.

**No cross-study assembly rule:** Yamada + Ballesta + McGinty/Lupkin + a behavioral normalization paper is still not a pass. The contract must close within the registered workline.

---

## 11. Formal-lock checklist

The following items are unresolved in v0.1 and must be frozen before preregistration or confirmatory execution:

- data-use permission and availability for Lane A;
- prospective recording/stimulation feasibility and ethics approval;
- exact offer distributions, payoff blocks, trial counts, counterbalancing, and task instructions;
- candidate identity rules and excluded/ambiguous candidate cases;
- neural observation likelihood, valuation/stimulation windows, parameter hierarchy, and priors/regularization;
- complete neural, behavioral, and intervention rival specifications;
- outer/inner split units and allocation;
- exact `D`, reliability estimator, and numeric `ε_NB`;
- minimum practical neural, behavioral, and intervention gains;
- mapping from stimulation to candidate neural parameter change;
- simulation-based parameter recovery, identifiability, power, and sample-size decision;
- event, exclusion, missing-data, adverse-event, and stopping rules;
- code revision, random seeds, environment lock, data schema, and adjudication script;
- preregistration venue, timestamp, and amendment policy.

Current state: **card-defined, not formally locked**. None of these blanks may be silently filled after outcome inspection.

---

## 12. Work packages and required artifacts

| Work package | Deliverable | Exit condition |
|---|---|---|
| W0 — access and provenance | public inventory and request draft complete; request not sent | Lane A feasibility still unknown; exit not met |
| W1 — retrospective reproduction | reproduction report; leakage-safe feasibility analysis; discrepancy log | published result reproduced or failure explained |
| W2 — identifiability | synthetic generator; parameter-recovery and rival-confusion report; power curves | frozen design can distinguish intended models |
| W3 — calibration and governance | stimulation/recording calibration; ethics/SOP references; event and exclusion specification | safety and measurement gates satisfied |
| W4 — preregistration | formally locked protocol, code, hashes, and adjudication script | immutable confirmatory package registered |
| W5 — execution | blinded/held-out result report and machine-readable verdict | local P3 adjudicated |

Create an experiment artifact directory only when W2 begins. Do not create an empty folder that could be mistaken for an active experiment.

---

## 13. Current SRT-floor verdict

| Connection | Hardness |
|---|---|
| offered candidates → fitted normalized neural response | 🟡 model-dependent |
| normalized population response → frozen task-choice distribution | 🟡 conditionally testable; not yet executed |
| choice distribution → one realized saccadic event | 🔴 without an explicit sampling/accumulation and motor gate; this card specifies an event gate but has not tested it |
| observed behavior → unique neural mechanism identity | 🔴 underdetermined without rival and intervention success |
| task choice → agency / subjecthood / consciousness | 🔴 forbidden inference |

Therefore:

- broad `normalized neural response → behavioral choice` remains **red / soft**;
- the bounded `P3-Scale-NB1` contract remains **yellow / conditional P3**;
- `NB1-MOFC-Lottery-v0` is **yellow / P4 card-defined**, not preregistered and not executed;
- the Core main chain is unchanged.

---

## 14. References and access routes

- Yamada, Louie, Tymula & Glimcher (2018), “Free choice shapes normalized value signals in medial orbitofrontal cortex,” *Nature Communications*: <https://www.nature.com/articles/s41467-017-02614-w>
- Ballesta, Shi, Conen & Padoa-Schioppa (2020), “Values encoded in orbitofrontal cortex are causally related to economic choices,” *Nature*: <https://www.nature.com/articles/s41586-020-2880-x>
- Ballesta et al. analysis repository: <https://github.com/PadoaSchioppaLab/2020_Ballesta_etal_Nature>
- McGinty & Lupkin (2023), “Behavioral read-out from population value signals in primate orbitofrontal cortex,” *Nature Neuroscience*: <https://www.nature.com/articles/s41593-023-01473-7>
- Keung et al. (2020), “Divisive normalization and decision making in multi-attribute choice,” *Nature Communications*: <https://www.nature.com/articles/s41467-020-15630-0>
- Keung et al. data route: <https://osf.io/fekpn/>
- Bavard & Palminteri (2023), “The dynamics of reward context-dependent encoding and choice,” *eLife*: <https://elifesciences.org/articles/83891>
- Bavard & Palminteri analysis repository: <https://github.com/hrl-team/3options>
