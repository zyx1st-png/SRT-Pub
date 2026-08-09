---
id: SRT-NEURAL25-EXPERIMENT-PROTOCOL-V0-1
type: experimental_protocol
status: pilot_ready_v0_1
canonical: false
claim_level: P4
claim_mode: lab_hypothesis
layer: neuroscience_lab
created: 2026-08-09
updated: 2026-08-09
owner_patch: Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md
source_card: Materials/2026/SRC_2026_08_09_Neuro_Lu_Strategy_Competition_Memory_Control.md
dependencies:
  - Core/SRT_Core_24_Discriminating_Predictions.md
  - Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md
  - 03_Bridges/SRT_Selection_Event_CompactCore.md
  - Neuroscience/SRT_Neuroscience_Claim_Status.md
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
preregistration_status: protocol_defined_not_formal_sample_lock
formal_lock_requires:
  - computational_parameter_recovery
  - independent_calibration_cohort
  - fixed_training_schedule
  - fixed_sample_size_from_power_simulation
  - fixed_perturbation_implementation
  - ethics_approval
ai_do_not_use_for_definition: true
tags: [NEURAL25, experiment, memory, history, L2, selection-authority, accessibility, switching-cost, hysteresis, preregistration, falsification]
---

# SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1

## Matched Current State / Different History

### Testing whether past selection history changes future path accessibility beyond current strategy state

> **Protocol status**: independent P4 lab protocol. It is designed to become preregistration-ready after a separate calibration and power-simulation pass. It does **not** define canonical `L_2`, memory, `G_hat_theta`, real choice, consciousness, subjecthood, or freedom.
>
> **Primary discipline**: this experiment is not allowed to count any residual history effect as an SRT success. The strong NEURAL25 bridge is supported only if history produces a structured joint signature involving **local trained-path efficiency, constraint on alternatives, and hysteresis under perturbation**, and that structure survives comparison with strong ordinary learning / arbitration models.

---

# 0. Executive summary

The protocol asks one narrow question:

> **If two animals are made as similar as possible in their current strategy state, does the depth of the history by which they arrived there still predict how easily they can adopt, switch to, and remain on a new strategy?**

The target dissociation is:

```text
same current observable strategy state
+
different prior history depth
->
different future accessibility / switching / recovery dynamics ?
```

The experiment is motivated by NEURAL25's distinction:

```text
Acquisition
-> Availability
-> Authority
-> Expression
-> Write-back
```

and by Core 24 P24-3's stronger hardening signature:

```text
reduced local selection cost
+
increased constraint on alternatives
+
hysteresis under perturbation
```

The experiment is deliberately designed so that four result classes remain possible:

1. **No residual history effect** — current-state learning / habit models are sufficient in this window; NEURAL25's stronger history-field bridge weakens.
2. **Residual history effect, but ordinary latent-history model wins** — history matters, but no SRT-specific structural advantage is established.
3. **Representation–authority dissociation only** — supports the CG-1 / CG-2 separation, but not strong `L_2` hardening.
4. **Triple-signature history structure + superior held-out prediction** — supports the bounded P24-3 / NEURAL25 bridge and justifies further replication.

---

# 1. Research question and target estimand

## 1.1 Primary research question

After matching current behavioral policy state and immediate strategy-strength proxies, does experimentally manipulated **history depth** explain residual variance in:

1. accessibility of a newly learned auditory strategy;
2. switching cost away from the old win-stay strategy;
3. rebound / hysteresis after perturbation?

## 1.2 Primary causal contrast

Define two pretraining conditions:

- `H_deep`: substantially overtrained prior win-stay history;
- `H_shallow`: criterion-level prior win-stay history with substantially less cumulative exposure.

Before the novel auditory strategy is introduced, the groups must pass a **terminal current-state matching gate**.

The primary contrast is therefore not:

```text
strong habit vs weak habit
```

but:

```text
similar terminal current state
arrived at through different history depth
```

## 1.3 Primary estimand

The main estimand is the residual effect of randomized history condition on new-strategy control after terminal-state matching:

\[
\Delta_H = E[Y \mid H_{deep}, S_{terminal}\approx s]
          - E[Y \mid H_{shallow}, S_{terminal}\approx s]
\]

where `Y` is defined separately for accessibility, transition cost, and hysteresis.

`S_terminal` is not a canonical SRT object. It is the pre-registered set of measured current-state covariates listed in §7.

---

# 2. Claim boundary

## 2.1 What a positive result may support

A positive result may support only the P4 claim that:

> under this task and measurement regime, prior selection history has measurable effects on future strategy accessibility / transition dynamics that are not exhausted by the frozen set of current-state variables and ordinary comparator models.

If the triple signature is met, the result may be described as:

> a bounded empirical bridge compatible with the SRT prediction that history-bearing hardening restructures future path accessibility rather than merely strengthening retained content.

## 2.2 What the experiment cannot establish

The experiment cannot by itself establish:

- canonical `L_2` identity;
- that memory is not representation;
- `memory = selection weight`;
- `mPFC = L_2`;
- `ACx = L_0`;
- consciousness or phenomenal experience;
- subjecthood;
- free will;
- `d-value`;
- `Psi_f`;
- `T_dir`;
- universal superiority of SRT over reinforcement learning;
- that every memory changes future possibility structure.

## 2.3 SRT-specific success is not defined as "history matters"

Ordinary reinforcement learning, habit, arbitration, latent-state, and mixture-of-experts models can all contain history-dependent variables.

Therefore:

```text
history coefficient != SRT-specific support
```

The stronger bridge requires a **pre-specified structural pattern** and meaningful out-of-sample model discrimination.

---

# 3. Evidence anchor and implementation scope

The immediate empirical anchor is the Lu et al. pup-search strategy task recorded in:

- `Materials/2026/SRC_2026_08_09_Neuro_Lu_Strategy_Competition_Memory_Control.md`;
- `Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md`.

The verified source basis for this protocol is the 2023 bioRxiv full text plus the 2025 COSYNE update recorded there.

The first prospective implementation should stay close to the source task for comparability:

- naturalistic pup search / retrieval;
- previous-location win-stay as the old strategy;
- an online auditory cue as the novel strategy;
- trial-level first-arm choice as the cleanest behavioral expression variable.

The exact animal strain, age window, apparatus dimensions, neural recording hardware, and perturbation technology must follow the collaborating laboratory's validated SOP and local ethics approval. This protocol intentionally does not prescribe surgical, viral, dosing, or device-operation procedures.

---

# 4. Conceptual decomposition to be tested

NEURAL25 separates five stages:

| Stage | Operational question |
|---|---|
| Acquisition | Has the sound-location association been learned at all? |
| Availability | Does the auditory strategy enter effective competition on this trial/session? |
| Authority | Can the auditory strategy causally control the first arm choice? |
| Expression | Does the auditory strategy actually win this trial? |
| Write-back | Does this realized path alter later accessibility, switching cost, or recovery dynamics? |

The protocol is designed to prevent behavioral learning curves from collapsing all five into one number.

---

# 5. Hypotheses H1–H5

## H1 — Residual alternative-accessibility effect

**Prediction**: after the terminal-state matching gate is satisfied, deep prior win-stay history will reduce early accessibility / control acquisition of the auditory strategy relative to shallow history.

Primary behavioral signature:

\[
AULC_{sound,deep} < AULC_{sound,shallow}
\]

across a fixed acquisition window defined before the formal cohort.

`AULC_sound` is the area under the trial-indexed probability curve for **auditory-cued first choices on strategy-conflict trials**.

Interpretation:

- supports residual history dependence if positive;
- does not by itself establish SRT-specific hardening.

---

## H2 — Asymmetric switching-cost effect

**Prediction**: deep-history animals will pay a larger cost when leaving the old win-stay strategy for the new auditory strategy, even though terminal win-stay performance was matched.

Candidate co-primary measures, frozen before formal enrollment:

1. decision latency from trial start to committed arm entry;
2. excess path length / hesitation before the first committed arm entry;
3. probability of old-strategy perseveration on conflict trials.

The confirmatory switching-cost endpoint must be selected during calibration and then frozen. The other measures become secondary.

Expected direction:

\[
K_{old\to new,deep} > K_{old\to new,shallow}
\]

The protocol prefers an **interaction** measure over raw latency:

\[
K_{switch} = Cost_{conflict} - Cost_{congruent}
\]

so that generic locomotor or motivational differences are less likely to masquerade as switching cost.

---

## H3 — Representation–authority dissociation

**Neural extension; not required for the first behavior-only formal cohort.**

When an auditory-strategy neural representation is decodable before the animal expresses the auditory strategy, a transient intervention targeting the old-strategy-supporting circuit should be capable of changing auditory-guided first-choice probability without requiring an acute increase in auditory representation strength.

Target pattern:

\[
\Delta P(sound\ choice) > 0
\]

while

\[
\Delta R_{auditory} \approx 0
\]

within the pre-specified intervention window.

This is a **representation vs path-efficacy** test:

```text
decodable candidate
!=
current behavioral authority
```

A positive H3 supports CG-1 / CG-2 separation. It still does not establish strong `L_2` hardening because ordinary arbitration architectures can predict this dissociation.

---

## H4 — Hysteresis / rebound after perturbation

**Prediction**: after a temporary perturbation that reduces expression or reliability of the old strategy, deep-history animals will show stronger rebound and/or slower recovery away from the old strategy once the perturbation is removed.

The perturbation may be implemented at one of two levels, frozen before the formal cohort:

### Behavioral implementation

A temporary contingency or task block that reduces the usefulness of win-stay while preserving the ability to compare pre- and post-perturbation strategy expression.

### Neural implementation

A laboratory-validated transient intervention affecting the old-strategy-supporting circuit.

Only one implementation is confirmatory in a given formal cohort.

Primary hysteresis estimand:

\[
HYS = \int_{post} [P(old\ strategy)_t - P_{new\ equilibrium}(old)]\,dt
\]

or an equivalent recovery half-life estimator selected and frozen during calibration.

Expected direction:

\[
HYS_{deep} > HYS_{shallow}
\]

---

## H5 — P24-3 triple-signature gate

The strongest SRT-facing claim requires three signatures to co-occur in the formal cohort:

### Signature A — local trained-path efficiency

Deep history must produce lower execution cost on old-strategy-aligned / congruent trials, without relying only on higher correctness.

Candidate measure:

\[
E_{local}=Cost_{shallow,congruent}-Cost_{deep,congruent}>0
\]

### Signature B — alternative-path constraint

Deep history must reduce access to or increase transition cost toward the auditory alternative after terminal current-state matching.

### Signature C — hysteresis

Deep history must produce stronger post-perturbation rebound / recovery lag.

The P24-3 bridge is considered **supported in this task only if all three signatures pass their frozen directional tests**.

One or two positive components are not enough.

---

# 6. Study architecture

The program has four strictly separated stages.

## Stage 0 — Computational identifiability

Purpose:

- determine whether the competing models can be distinguished at realistic trial counts;
- perform parameter-recovery and model-recovery tests;
- prevent an expensive animal study whose hypotheses are mathematically non-identifiable.

Stage 0 uses synthetic data only.

Required outputs before Stage 1:

1. parameter recovery for all formal model parameters;
2. confusion matrix for model recovery;
3. simulated power / precision curves across plausible group sizes and effect ranges;
4. a frozen list of identifiable primary observables;
5. proof that the SRT-inspired model is not guaranteed to win merely by having more parameters.

### Stage-0 advancement gate

Do not advance if:

- the ordinary latent-history comparator and SRT-inspired shared-hardening model are practically indistinguishable under plausible designs;
- key parameters show severe posterior / likelihood non-identifiability;
- model recovery is driven primarily by trial count artifacts rather than the target signatures.

A failed Stage 0 is an **informative design failure**, not evidence against or for SRT.

---

## Stage 1 — Independent calibration cohort

Purpose:

- choose exact deep/shallow exposure schedules;
- establish a terminal-state matching band;
- select the confirmatory switching-cost measure;
- select the fixed acquisition window for H1;
- select the perturbation duration and recovery window;
- estimate variance components for formal power simulation.

Calibration animals / sessions are never pooled into confirmatory inference.

All decisions from Stage 1 must be frozen in a dated protocol lock before Stage 2 begins.

---

## Stage 2 — Formal behavioral cohort

This is the minimum flagship experiment.

Required features:

1. prospective randomized assignment to `H_deep` vs `H_shallow`;
2. pre-defined terminal-state matching gate;
3. identical novel auditory strategy introduction after matching;
4. fixed acquisition window;
5. fixed perturbation and post-perturbation recovery window;
6. blinded outcome analysis where feasible;
7. fixed sample size with no optional stopping for significance.

Stage 2 is sufficient to test H1, H2, H4, and H5.

---

## Stage 3 — Neural / causal extension

Stage 3 is a separate confirmatory cohort unless the collaborating laboratory can justify simultaneous recording without compromising Stage-2 power or welfare.

Target additions:

- auditory-cortex population representation;
- mPFC / old-strategy-related population representation;
- trial-level decoder outputs calculated without label leakage;
- laboratory-validated transient causal perturbation.

Stage 3 tests H3 and strengthens interpretation of H1/H4.

Stage 3 data must not be required to rescue a failed Stage-2 triple-signature test.

---

# 7. History manipulation and terminal-state matching

## 7.1 Operational definition of history depth

`HistoryDepth` must be experimentally manipulated by cumulative successful exposure to the old win-stay strategy before novel-cue introduction.

The formal lock must record at minimum:

- total prior trials;
- total prior rewarded win-stay-compatible trials;
- number of sessions / days;
- recency distribution of the last training block;
- terminal criterion attainment.

The deep/shallow separation must be large by design, but the exact ratio is selected in Stage 1 and frozen before Stage 2.

## 7.2 Terminal matching variables

Before novel sound introduction, groups must be matched on a frozen set including at minimum:

1. terminal win-stay first-choice probability;
2. terminal reward / success rate;
3. recent-trial outcome history summary;
4. fitted current win-stay strategy-weight proxy;
5. session number relative to terminal matching block;
6. gross locomotor / engagement measure if it materially predicts decision latency.

If Stage 3 is used, add:

7. immediate mPFC previous-location decoder-strength proxy, if stable enough for matching without excessive attrition.

## 7.3 Matching gate

Default formal target:

- standardized mean difference `|SMD| <= 0.10` on each primary matching variable;
- no primary variable may exceed `|SMD| = 0.15`;
- model-based overlap must show no severe positivity violation.

If calibration demonstrates these bands are infeasible, replacement bands must be fixed **before** Stage 2 and justified from calibration rather than formal outcomes.

## 7.4 Matching failure

If groups cannot be made sufficiently similar on terminal current-state measures without destroying the history-depth contrast, the study is classified:

> **NON-IDENTIFIABLE DESIGN — CURRENT STATE AND HISTORY DEPTH NOT SEPARABLE UNDER THIS TASK**

Do not proceed to interpret group differences as historical-field effects.

---

# 8. Trial taxonomy

Each formal trial must be classified before outcome analysis.

## 8.1 Conflict trial

The novel auditory cue recommends the opposite arm from the old win-stay strategy.

These trials carry the highest information about strategy authority.

## 8.2 Congruent trial

The auditory cue and win-stay strategy recommend the same arm.

These trials are useful for local efficiency and general movement controls but cannot identify which strategy controlled the action.

## 8.3 Neutral / diagnostic trial

Optional task-specific trials used for cue detectability, locomotion, or strategy validation. They are not part of the primary H1 estimator unless frozen in Stage 1.

---

# 9. Outcomes

## 9.1 Co-primary behavioral outcomes

Three co-primary quantities correspond to the strong history-hardening test:

### `Y_A` — alternative accessibility

Auditory-guided first-choice probability across the frozen early conflict-trial window, summarized as trial-level hierarchical learning curve and AULC.

### `Y_K` — switching cost

Frozen conflict-minus-congruent cost metric selected during Stage 1.

### `Y_H` — hysteresis

Frozen post-perturbation rebound area or recovery half-life.

## 9.2 Required local-efficiency outcome

`Y_E` — execution cost on old-strategy-aligned congruent trials.

H5 requires the expected deep-history efficiency direction.

## 9.3 Neural outcomes for Stage 3

- `R_AUD`: cross-validated auditory-strategy decoder evidence;
- `R_OLD`: cross-validated previous-location / old-strategy decoder evidence;
- `PEF_AUD`: causal change in auditory-guided first-choice probability under intervention;
- intervention-induced change in representation strength within the pre-registered neural window.

## 9.4 Secondary outcomes

May include:

- total search duration;
- retrieval latency;
- error-correction behavior after initial wrong choice;
- session-to-session retention;
- re-learning slope;
- strategy entropy;
- trajectory hesitation metrics.

Secondary outcomes cannot rescue failed co-primary tests.

---

# 10. Data schema

Minimum trial-level fields:

```text
animal_id
history_group
history_exposure_count
history_rewarded_count
session_id
trial_index
formal_stage
previous_reward_side
sound_side
strategy_congruency
first_arm_choice
first_choice_auditory_correct
first_choice_win_stay
reward_obtained
decision_latency
path_length_or_equivalent
perturbation_state
post_perturbation_trial_index
terminal_match_block_id
```

Stage-3 additions:

```text
auditory_decoder_score
old_strategy_decoder_score
neural_window_id
intervention_on
intervention_target_class
signal_quality_flags
```

All derived variables must be generated by version-controlled scripts before treatment labels are unblinded for confirmatory analysis wherever feasible.

---

# 11. Competing models — frozen comparator set

The formal analysis must compare four models. New models may be explored afterward, but they cannot replace the frozen comparator verdict.

## M0 — Current-state competition model

A minimal two-strategy competition model.

Behavior depends on current old-strategy and auditory-strategy weights, updated from trial outcomes.

Schematic:

\[
P(AUD_t)=softmax(W^{aud}_t,W^{old}_t)
\]

No explicit residual history-depth term is allowed after the current weights are specified.

Purpose:

- test whether current policy state is sufficient.

---

## M1 — Current-state competition + perseveration / switching cost

Adds standard ordinary mechanisms such as:

- choice stickiness / perseveration;
- forgetting / recency;
- generic switch penalty;
- cue reliability.

History affects behavior only through ordinary evolving current-state variables.

Purpose:

- prevent generic habit inertia from being mislabeled as an SRT-specific historical field.

---

## M2 — Flexible latent-history comparator

Adds history-depth effects with **separate unconstrained coefficients** for accessibility, switching, and rebound.

Example structure:

\[
Y_A \sim \beta_{HA}H
\]

\[
Y_K \sim \beta_{HK}H
\]

\[
Y_H \sim \beta_{HH}H
\]

The coefficients need not share sign or latent structure.

Purpose:

- serve as the strongest ordinary "history matters" comparator;
- prevent SRT from winning merely because M0/M1 omit a useful historical predictor.

If M2 predicts held-out data as well as or better than M3, the result does not establish the stronger SRT structural claim.

---

## M3 — Shared history-accessibility / hardening model

This is the SRT-inspired P4 model, not a canonical equation.

A shared latent hardening term `H*` is constrained to generate the joint signature:

\[
H^* \uparrow
\Rightarrow
\begin{cases}
local\ old\ path\ cost \downarrow \\
alternative\ accessibility \downarrow \\
old\to new\ switching\ cost \uparrow \\
post\ perturbation\ hysteresis \uparrow
\end{cases}
\]

The exact link functions are frozen after Stage-0 identifiability work.

Purpose:

- test whether one constrained history structure predicts multiple future-selection effects more efficiently than unrelated historical coefficients.

M3 must not receive post-hoc parameters after formal outcomes are seen.

---

# 12. Model-validation rules

## 12.1 Parameter recovery

Before formal data collection, synthetic recovery must show that target parameters can be estimated without severe bias at the planned trial count.

The Stage-0 report must include:

- true vs recovered parameter plots;
- bias and RMSE;
- interval coverage or equivalent uncertainty calibration;
- parameter correlation / confounding matrix.

## 12.2 Model recovery

Synthetic data generated from each M0–M3 must be passed through the frozen model-selection pipeline.

Advance only if the recovery matrix demonstrates practically useful discrimination, with particular attention to M2 vs M3.

## 12.3 Held-out validation

Formal model comparison is animal-level, not random-trial-level.

Allowed approaches:

- leave-one-animal-out cross-validation;
- nested animal-level K-fold cross-validation;
- an independently held-out replication cohort.

Randomly splitting trials from the same animal across train/test sets is not sufficient because it leaks individual history structure.

## 12.4 Primary predictive score

One score must be frozen before Stage 2, such as:

- held-out log predictive density;
- held-out negative log likelihood;
- Brier score for trial-level strategy choice.

Calibration is reported separately.

---

# 13. Confirmatory statistical analysis

## 13.1 Unit of inference

The biological unit of inference is the **animal**.

Trials are repeated observations nested within animals and sessions.

Do not treat trial count as independent sample size.

## 13.2 H1 analysis

Primary model:

- hierarchical / mixed-effects logistic learning-curve model on conflict trials;
- fixed effects include history group, standardized trial index, and their interaction;
- pre-registered terminal current-state covariates may be included for precision;
- random animal intercept and, if identifiable, random learning slope.

Primary summary:

- between-group difference in frozen-window AULC with animal-level uncertainty.

## 13.3 H2 analysis

Use a hierarchical model appropriate to the frozen switching-cost endpoint.

Preferred design:

```text
cost ~ history_group * conflict_status + session/trial covariates + animal random effects
```

The key coefficient is the group × conflict interaction.

## 13.4 H4 analysis

Use either:

- hierarchical recovery-curve model;
- survival / time-to-recovery model;
- pre-specified rebound-area comparison.

The exact model is chosen from Stage-1 diagnostics and frozen before Stage 2.

## 13.5 H5 intersection-union gate

The strong P24-3 support statement is permitted only if all three directional components are supported:

1. local trained-path efficiency;
2. alternative-path constraint / switching penalty;
3. hysteresis.

Treat this as an **intersection-union claim gate**: failure of any one component blocks the strong triple-signature conclusion.

Report each component effect and confidence interval separately.

Do not average the three into a composite score that allows one large effect to compensate for one failed gate.

---

# 14. Power and sample-size lock

## 14.1 No invented sample size in v0.1

This protocol intentionally does not invent a final `n` before variance and identifiability are known.

The formal sample size must be locked using Stage-0 simulation plus Stage-1 independent calibration data.

## 14.2 Simulation target

The sample-size simulation must model:

- animal-level heterogeneity;
- trial-level autocorrelation;
- group-by-conflict effects;
- learning-curve variance;
- attrition / unusable-session rate;
- perturbation recovery variance;
- neural-signal attrition if Stage 3 is planned.

## 14.3 Power target

Default planning target:

- at least 90% power for the weakest co-primary directional component under the chosen smallest effect of scientific interest;
- at least 80% power for the full H5 intersection-union gate under the frozen joint-effect scenario.

If those targets are infeasible under ethical / resource constraints, the protocol must be narrowed rather than silently lowering the evidential claim.

## 14.4 Smallest effect of scientific interest

The SESOI must be selected from:

1. source-task behavioral variability where available;
2. independent calibration data;
3. a pre-specified minimum change large enough to alter actual strategy control, not merely reach statistical detectability.

SESOI cannot be chosen after inspecting formal group differences.

---

# 15. Randomization, blinding, exclusion, and missingness

## 15.1 Randomization

Randomize animals to deep vs shallow history condition before history manipulation.

Stratify only on variables declared before randomization, such as batch or baseline task engagement.

## 15.2 Blinding

Where operationally feasible:

- primary outcome extraction is automated;
- analysts receive coded group labels until QC / exclusions are frozen;
- neural decoder construction is performed without access to future behavioral outcomes beyond the decoder's training labels.

## 15.3 Pre-specified exclusions

Possible exclusion classes must be frozen before Stage 2, including:

- failure to engage with the task;
- failure to reach the terminal criterion;
- failure of the current-state matching gate;
- hardware / tracking failure above a frozen missing-data threshold;
- neural recording failure if required for Stage 3;
- welfare-related withdrawal.

Do not exclude an animal because its result contradicts the hypothesis.

## 15.4 Matching failures are not ordinary exclusions

If one history group systematically fails the terminal matching gate, this is evidence that history and current state could not be separated by the design.

Report it as a **design-identifiability failure**, not as routine attrition.

## 15.5 Missing data

Freeze rules for:

- incomplete trials;
- tracking gaps;
- session interruption;
- neural-channel dropout.

Primary analysis should not use single-value imputation for trial outcomes.

---

# 16. Perturbation rules

## 16.1 Purpose

Perturbation exists to test hysteresis and, in Stage 3, causal control authority.

It is not included merely to create a larger group difference.

## 16.2 Freeze before formal cohort

The following must be fixed before Stage 2/3:

- perturbation type;
- onset relative to task events;
- duration;
- recovery observation window;
- primary rebound measure;
- sham / control condition.

## 16.3 No method switching after results

A failed behavioral perturbation may motivate a future neural experiment, but the neural experiment cannot retroactively rescue the original formal cohort.

Likewise, a failed neural intervention cannot be reclassified as a successful "behavioral perturbation" result.

---

# 17. CG-0–CG-4 mapping

This protocol uses the selection-event audit only as a P2/P3/P4 operational interface.

| Gate | Protocol role | Maximum claim from this experiment |
|---|---|---|
| CG-0 / DMF | sound-side and previous-location differences enter effective channels | effective candidate difference |
| CG-1 / NER | neural / model state non-equivalently registers strategy-relevant information | internal registration candidate |
| CG-2 / PEF | candidate state causally changes first-arm choice probability | path-efficacy candidate |
| CG-3 / CBP | task-specific cost / delay / failed-first-choice consequence | limited consequence-bearing evidence only |
| CG-4 / HEF | prior path changes future accessibility, switching probability, or recovery | historical-efficacy candidate if independently demonstrated |

Because CG-3 is weak in the source task, this protocol does **not** aim to establish a complete real-choice event or subject-level stake structure.

The primary scientific leverage is the CG-1 / CG-2 / CG-4 separation.

---

# 18. Decision matrix

Formal interpretation must use this matrix before narrative discussion.

| Result | Required interpretation | NEURAL25 status |
|---|---|---|
| H1/H2/H4 absent after valid matching | no detectable residual history restructuring in this task | **Failure / downgrade strong bridge** |
| residual history effect present, but M2 >= M3 in held-out prediction or triple signature fails | history matters but unconstrained ordinary latent-history account is sufficient | **Pressure; no SRT-specific advantage** |
| H3 positive only | representation and current control authority dissociate | **Supports CG-1/CG-2 bridge only** |
| H1/H2/H4 directional + H5 triple signature passes, but M3 not better than M2 | structured behavioral signature exists, but SRT model not discriminating | **Bridge-compatible, not discriminating** |
| H5 passes + M3 robustly outperforms M0–M2 out of sample + replication direction holds | bounded evidence for history-dependent selection-field bridge | **Strongest permitted P4 support** |
| terminal matching fails systematically | current state and history depth not experimentally separable | **Uninterpretable protocol** |
| Stage-0 M2/M3 non-identifiable | model architecture cannot adjudicate claim | **Do not run formal animal test** |

---

# 19. Formal failure conditions

The strong NEURAL25 bridge must be weakened if any of the following occur in a validly powered formal study:

1. history depth adds no reliable predictive value after terminal current-state matching;
2. deeper history improves old-path efficiency but does not constrain alternatives;
3. alternative constraint occurs without measurable hysteresis;
4. apparent hysteresis is fully explained by generic fatigue, locomotion, cue reliability, or immediate perseveration controls;
5. the unconstrained ordinary latent-history model M2 predicts held-out data as well as or better than the shared-hardening M3;
6. M3's advantage disappears under animal-level rather than trial-level validation;
7. required effects appear only after post-hoc outcome-window or exclusion changes;
8. current-state matching cannot be achieved without collapsing the history manipulation.

A failure cannot be repaired by adding an unconstrained latent variable after formal outcomes are known.

Any post-failure model change must produce a new, independently testable prediction and be tested in new data.

---

# 20. Negative controls and confound checks

At minimum, the formal design should control or test:

## 20.1 Sensory detectability

Confirm that history groups do not differ materially in basic sound detection / localization capacity before interpreting auditory-strategy accessibility.

## 20.2 Locomotion

Separate strategy-switching latency from generic movement-speed differences.

## 20.3 Motivation / task engagement

Track completion rate and reward-retrieval engagement so reduced auditory adoption is not automatically read as historical constraint.

## 20.4 Simple perseveration

M1 explicitly models choice stickiness. A deep-history effect must survive this comparator to count as more than ordinary immediate perseveration.

## 20.5 Reward-history leakage

Because history depth necessarily alters cumulative experience, do not claim reward history is "held constant." Instead test whether its effect is exhausted by current-policy and ordinary learning-state variables versus requiring residual future-path structure.

## 20.6 Cue-congruency imbalance

The pseudorandom schedule must ensure adequate conflict trials in both groups and must not allow recent side streaks to confound history-group effects.

---

# 21. Neural-decoder safeguards for Stage 3

## 21.1 Cross-validation

Decoder performance must be evaluated on held-out trials / sessions according to a frozen scheme.

## 21.2 No circular outcome labels

A decoder used as evidence for representation before choice may not use post-choice neural activity or behavioral outcome features from the same trial in a way that leaks the label.

## 21.3 Representation strength is not selection authority

Decoder accuracy / separability is recorded as `R`, not automatically as path efficacy.

Only a causal or sufficiently controlled behavioral link may support PEF language.

## 21.4 No reverse ontology

Even a perfect decoder does not establish canonical `L_0`, `L_1`, `L_2`, `d`, `Psi_f`, or consciousness.

---

# 22. Stopping rules

## 22.1 Formal cohort

The formal sample size is fixed before unblinding.

No significance-based optional stopping.

## 22.2 Welfare

Animal welfare criteria and veterinary / ethics-mandated stopping override statistical plans.

Such stopping is reported transparently and is not counted as hypothesis-based optional stopping.

## 22.3 Technical incident

A pre-defined hardware or task failure may suspend a cohort. Resume only after a documented correction; do not mix pre- and post-correction data without a frozen handling rule.

---

# 23. Replication rule

A single formal cohort can support the P4 bridge but not establish a robust domain law.

Before owner-level neuroscience synthesis, require at least one of:

1. independent within-lab replication with frozen protocol;
2. independent laboratory replication;
3. convergent task generalization showing the same triple signature with a different old/new strategy pair.

A Stage-3 neural result without behavioral triple-signature replication should remain a mechanism bridge, not a general memory theory.

---

# 24. Immediate work package

The protocol can be worked on immediately without new animal procedures.

## Work Package A — Simulation

Create scripts that:

1. implement M0–M3;
2. generate synthetic deep/shallow histories;
3. enforce terminal-state matching;
4. simulate acquisition, switching, and rebound;
5. run parameter recovery;
6. run model recovery;
7. estimate sample-size / trial-count requirements.

Suggested future paths:

```text
Neuroscience/experiments/neural25/simulate_models.py
Neuroscience/experiments/neural25/fit_models.py
Neuroscience/experiments/neural25/power_simulation.py
Neuroscience/experiments/neural25/model_spec.md
```

These paths are suggestions only; creating them is a separate implementation task.

## Work Package B — Retrospective-data request

If Lu et al. trial-level data become available, run a **retrospective feasibility analysis only**:

- estimate current strategy weights;
- test representation–authority dissociation;
- inspect whether cumulative history predicts switching beyond current state;
- estimate variance for the prospective design.

Do not use retrospective findings to claim the prospective preregistered prediction has been confirmed.

## Work Package C — Formal preregistration lock

After Stage 0 and Stage 1, create:

```text
SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_2_FORMAL_LOCK.md
```

with immutable:

- exact training schedule;
- exact trial counts;
- final sample size;
- fixed primary endpoint definitions;
- fixed perturbation implementation;
- frozen M0–M3 equations and parameter priors / bounds;
- frozen analysis scripts / commit hash;
- ethics approval reference;
- exclusion rules.

---

# 25. Minimal preregistration checklist

Before the first formal animal is enrolled, all boxes must be checked:

- [ ] Stage-0 parameter recovery passed.
- [ ] Stage-0 M2 vs M3 model recovery is adequate.
- [ ] Calibration cohort completed and excluded from confirmation.
- [ ] Deep/shallow history schedule frozen.
- [ ] Terminal current-state matching gate frozen.
- [ ] Conflict/congruent trial schedule frozen.
- [ ] H1 acquisition window frozen.
- [ ] H2 switching-cost endpoint frozen.
- [ ] H4 perturbation and recovery window frozen.
- [ ] H5 triple-signature decision rule frozen.
- [ ] Sample size frozen from power simulation.
- [ ] M0–M3 implementation frozen.
- [ ] Animal-level cross-validation scheme frozen.
- [ ] Exclusion and missingness rules frozen.
- [ ] Randomization sequence generated and secured.
- [ ] Blinding / coded-analysis plan frozen.
- [ ] Ethics approval active.
- [ ] Formal analysis code version / commit frozen.

If any required item is missing, the cohort remains pilot / calibration and cannot be presented as confirmatory.

---

# 26. Reporting template

Every formal report must state in this order:

1. Was terminal current-state matching achieved?
2. Did H1 alternative-accessibility effect occur?
3. Did H2 switching-cost effect occur?
4. Did H4 hysteresis occur?
5. Did local-efficiency signature occur?
6. Did H5 triple-signature gate pass?
7. Which model won animal-level held-out prediction: M0, M1, M2, or M3?
8. Did H3 representation–authority dissociation occur, if Stage 3 was run?
9. Which result class in §18 applies?
10. What claim must be retained, weakened, or withdrawn?

Do not lead the report with a narrative interpretation before these ten fields are filled.

---

# 27. Protocol-level falsification statement

The shortest falsifiable statement of this protocol is:

> **If deep and shallow prior histories can be brought to matched current strategy states, but history depth then fails to predict alternative-path accessibility, switching cost, or post-perturbation hysteresis beyond strong current-state and latent-history comparator models, the NEURAL25 claim that memory hardening has an additional future-selection-field signature must be weakened to ordinary memory / habit / policy weighting for this experimental regime.**

The strongest allowed positive statement is:

> **If matched-current-state animals with deeper history show the pre-registered triple signature of lower old-path execution cost, greater alternative-path constraint, and stronger hysteresis, and a constrained shared-history model predicts held-out animals better than both current-state and flexible latent-history comparators, the result provides bounded P4 support for the SRT bridge that historical hardening restructures future path accessibility rather than merely preserving or strengthening remembered content.**

---

# 28. Relationship to current SRT files

## Canonical / authority guard

- `Core/SRT_Core_21b_Constitutive_Theorems.md` remains the P1 authority for Real Choice Moment.
- Canonical `L_2` meaning is not redefined here.
- `d-value`, `Psi_f`, and `T_dir` are not measured by this protocol.

## Bridge / prediction owners

- `Neuroscience/patches/SRT_Neuro_NEURAL25_Memory_as_Historical_Selection_Bias_v0_1.md` owns the source-derived bridge intuition.
- `Core/SRT_Core_24_Discriminating_Predictions.md P24-3` owns the triple-signature discriminating prediction.
- `Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md` supplies the CG-0–CG-4 operational hygiene.

## Future integration condition

Do not use this protocol's existence as evidence that NEURAL25 has been empirically validated.

Only an executed, pre-registered formal cohort can change the empirical status of the bridge.
