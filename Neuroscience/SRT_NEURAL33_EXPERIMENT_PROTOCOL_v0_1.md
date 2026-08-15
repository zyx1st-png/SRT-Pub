---
id: SRT-NEURO-NEURAL33-EXPERIMENT-PROTOCOL
type: experimental_protocol
status: draft
record_stage: draft_active
version: v0_1
layer: empirical_bridge
epistemic_layer: experimental
claim_mode: prediction
claim_level: P4-P5
canonical: false
domain: neuroscience_memory_ripples_history_eligibility_relational_reinstatement
dependency:
  - Neuroscience/patches/SRT_Neuro_NEURAL33_Distributed_Ripple_Relational_Reinstatement_v0_1.md
  - Neuroscience/patches/SRT_Neuro_NEURAL23_Embodied_Rhythmic_Eligibility_v0_1.md
  - Neuroscience/patches/SRT_Neuro_NEURAL31_Astrocytic_Historical_Eligibility_Memory_Reentry_v0_1.md
  - Neuroscience/SRT_Neuro_Predictions_Table.md
created: 2026-08-15
tags:
  - mechanism-level-prediction
  - history
  - eligibility
  - ripple
  - relational-reinstatement
  - intracranial
  - falsification
---

# NEURAL33 Experiment Protocol v0.1 — History × Eligibility × Relational Reinstatement

> **Purpose**: convert the NEURAL33 bridge from post-hoc interpretation into mechanism-level differential predictions. This protocol does not treat any listed effect as established SRT evidence. It specifies what would count as support, downgrade or failure for the bridge.

---

## 1. Core question

Does prior history interact with the organism's current physiological / neural timing state to change the probability or similarity of an encoding-related distributed neural relation during later retrieval?

Compact target:

\[
H_m \times E_t
\rightarrow
S_R(m,t)
\rightarrow
Y_t,
\]

where all symbols are protocol-local:

- `H_m` = item-specific historical / learning-strength variable;
- `E_t` = current embodied / neural eligibility state before the coordination event;
- `S_R(m,t)` = scalar similarity between declared encoding and retrieval relation structures;
- `Y_t` = behavioral output such as RT, accuracy or confidence.

For binary re-entry analyses use a separate quantity:

\[
P_{reentry}(m,t).
\]

The key differential claim is not merely that history matters or phase matters. It is that **history-conditioned re-entry depends on the current state in a way that is not fully reducible to additive memory strength, local firing or generic arousal.**

---

## 2. Primary study family — human intracranial retrieval

### 2.1 Preferred sample

Use patients undergoing clinically indicated intracranial monitoring where the following can be recorded simultaneously:

```text
single-unit spikes;
local field potentials;
respiration;
ECG / cardiac phase;
behavioral response;
preferably pupil / eye movement or another arousal proxy.
```

Do not place electrodes for research purposes. Electrode coverage remains clinically determined.

### 2.2 Task

Use a repeated encoding–delay–retrieval task with enough item repetitions and memory-strength variation to estimate item-specific re-entry.

Required features:

```text
multiple stimulus identities;
within-subject repeated retrieval;
matched sensory input for critical encoding/retrieval comparisons;
at least two memory-load or retention-strength levels;
trial count sufficient for relation-level estimates;
confidence measure if feasible.
```

A Sternberg-style design is acceptable, but the preferred extension includes a longer retention interval or repeated retrieval block so that historical strength can be estimated independently of immediate task load.

---

## 3. Variable families

### 3.1 Historical variable H_m

`H_m` should not be a single subjective label if avoidable. Candidate operationalizations include:

```text
encoding repetition count;
encoding performance;
subsequent recognition strength;
item-specific neural encoding reliability;
retention interval;
prior successful retrieval count.
```

Use at least one measure that can vary by item while current sensory input is held constant.

### 3.2 Eligibility variable E_t

Estimate current pre-event state in a preregistered window, e.g. `-500 to 0 ms` before the detected retrieval co-ripple or before a fixed stimulus-locked analysis point.

Candidate features:

```text
respiratory phase;
cardiac phase;
respiration-heart coupling;
large-scale low-frequency phase state;
theta phase / theta-gamma coupling;
regional phase-gradient or phase-alignment summary;
arousal proxy;
recent ripple history.
```

No single variable is assumed to equal `E_t`. `E_t` is an analysis family for current eligibility-related predictors.

### 3.3 Coordination-window variable W_t

Primary candidate:

```text
cross-region co-ripple event
```

with controls:

```text
single-site ripple;
no-ripple matched window;
low-gamma co-event;
very-high-gamma event;
continuous amplitude-envelope correlation.
```

### 3.4 Relation structure and reinstatement metrics

Use distinct types throughout:

\[
\mathcal R_m^{enc}
\]

= encoding relation structure / graph / set for item `m`;

\[
\mathcal R_m^{ret}(t)
\]

= retrieval relation structure at time `t`;

\[
S_R(m,t)=sim\!\left(\mathcal R_m^{enc},\mathcal R_m^{ret}(t)\right)
\]

= scalar relational similarity;

\[
P_{reentry}(m,t)
\]

= probability of a preregistered binary re-entry event when that analysis is used.

Candidate primary relation definitions include:

```text
repetition of cell-pair co-firing within a declared temporal window;
weighted graph similarity between encoding and retrieval co-firing networks;
spike-time relation similarity;
population-level relational geometry similarity after component-rate normalization.
```

At least one primary measure must preserve stimulus identity and be compared against within-subject stimulus-label shuffles.

### 3.5 Component-level state X_t

Controls must include component features that could otherwise explain `S_R` or `P_reentry`:

```text
single-neuron firing rates;
regional mean firing;
ripple power and duration;
number of recruited units;
local event rate;
stimulus identity;
load;
trial position;
recording quality.
```

### 3.6 Behavioral outcome Y_t

Primary outcomes:

```text
reaction time;
accuracy if error count is sufficient;
confidence if collected.
```

Secondary outcomes:

```text
later retention;
subsequent recall precision;
post-retrieval memory strengthening or weakening.
```

---

## 4. Primary hypotheses

### H1 — relational reinstatement is not exhausted by component activity

After modeling component activity, event power, load, stimulus and arousal, relation-level reinstatement should retain incremental out-of-sample prediction of retrieval efficiency.

Primary comparison:

```text
Model A: Y ~ X + task + arousal
Model B: Y ~ X + S_R + task + arousal
```

Support criterion:

```text
Model B improves preregistered held-out prediction / information criterion beyond a trivial effect.
```

Downgrade criterion:

```text
S_R adds no stable predictive value after X is controlled.
```

### H2 — history and current eligibility interact

For continuous relational similarity:

\[
S_R(m,t)
=
\beta_0
+\beta_1H_m
+\beta_2E_t
+\beta_3(H_m\times E_t)
+\mathbf C\gamma
+u_{subject}
+u_{item}
+\epsilon.
\]

For binary re-entry use an explicit generalized model, e.g.:

\[
\operatorname{logit}P_{reentry}(m,t)
=
\beta_0+\beta_1H_m+\beta_2E_t+\beta_3(H_m\times E_t)+\mathbf C\gamma+\cdots
\]

`C` includes preregistered controls.

Support criterion:

```text
a non-trivial, replicable H x E interaction improves out-of-sample prediction.
```

Failure / downgrade:

```text
strong studies repeatedly support only additive H + E effects.
```

### H3 — pre-event state predicts content-specific re-entry, not only generic readiness

Train a model using pre-event `E_t` features to predict which encoding-related relation pattern will be reinstated.

Required comparison:

```text
content-specific prediction
vs
prediction of generic fast/slow RT or generic ripple occurrence.
```

Support requires incremental content-specific prediction after controlling cue identity and arousal.

Downgrade if pre-state predicts only general response speed or ripple probability.

### H4 — relation similarity can survive partial component turnover

For repeated retrieval of the same content, compare:

\[
O_V=\frac{|V_1\cap V_2|}{|V_1\cup V_2|}
\]

with preregistered relational similarity `S_R`.

Because `O_V` and `S_R` are structurally dependent, do **not** interpret a simple residual regression as decisive. Require all of:

1. **overlap matching / stratification**: compare relation similarity within narrow `O_V` strata where feasible;
2. **conditional permutation null**: shuffle relation identity while preserving component membership / overlap distributions;
3. **incremental held-out prediction**: compare `Y ~ O_V + controls` against `Y ~ O_V + S_R + controls`;
4. **collinearity diagnostics**: report VIF / condition indices or a justified equivalent and show stability across specifications.

Support means `S_R` carries stable incremental information beyond component overlap under those controls.

Failure means component overlap fully accounts for recurrence and the conditional-permutation / held-out relational increment collapses.

### H5 — coordination windows mediate, rather than merely accompany, load-sensitive re-entry

Compare co-ripple, single-ripple and matched no-ripple windows under matched firing / power conditions.

A stronger NEURAL33 pattern would be:

```text
history/current-state effects
-> stronger relation reinstatement specifically in co-ripple windows
-> behavioral efficiency
```

This remains a mediation-style observational analysis unless the coordination window is experimentally manipulated.

---

## 5. Required negative controls

At minimum include:

1. **stimulus-label shuffle** preserving overall firing / event rates;
2. **spike-time shuffle** preserving declared within-trial rate structure;
3. **duration-matched no-ripple windows**;
4. **single-site ripple windows**;
5. **firing-rate matched analyses**;
6. **ripple-power / duration controls**;
7. **load and RT controls** so that faster responses do not trivially define the relation effect;
8. **arousal controls** using physiological or pupillary measures where possible;
9. **epileptiform / seizure-onset exclusion**;
10. **subject-level replication**, not only pooled cell-pair significance.

Where possible, report effect sizes and cross-validated prediction rather than relying on extreme P values from very large pair counts.

---

## 6. Frequency / event specificity test

NEURAL33 does not require ripple uniqueness, but the ripple-window hypothesis should be compared against adjacent alternatives.

Preregister:

```text
low gamma: 30–55 Hz
ripple: 70–100 Hz
very high gamma: 120–190 Hz
```

and separately compare:

```text
discrete co-event metrics
vs
continuous amplitude-envelope correlation.
```

Possible outcomes:

```text
A. ripple-specific relational increment -> strengthens NEURAL33 ripple implementation
B. multiple bands show comparable relational increment -> retain transient-coordination bridge, downgrade ripple specificity
C. only continuous power correlation matters -> downgrade event-window interpretation
```

---

## 7. Directionality guard

A temporal lead such as:

```text
HIP ripple onset before AMY ripple onset
```

must not be interpreted as causal transmission without intervention or directional-identification evidence.

Required language:

```text
temporal precedence
!= directed causation
```

If directionality is tested, use methods with explicit assumptions and validate them against common-input and conduction-delay alternatives.

---

## 8. Secondary study family — historical eligibility manipulation

This arm is not implied by the Verzhbinsky human paper. It is a **conditional bridge-on-bridge prediction** and is admissible only while the independent NEURAL31 historical-eligibility bridge survives its own causal discrimination / downgrade tests.

### 8.1 Animal design family

During learning:

```text
tag memory-related neuronal ensemble
+ tag candidate historical-eligibility substrate such as learning-linked astrocytic ensemble
```

During later retrieval:

```text
measure neuronal relation-level reinstatement
+ selectively manipulate the historical-eligibility substrate
```

Measure separately:

```text
cue-specific content decoding;
re-entry probability;
re-entry latency;
relation stability;
general arousal / fear;
generalization;
post-retrieval persistence.
```

### 8.2 Discriminating prediction

Conditional on NEURAL31 remaining supported, a NEURAL31-compatible eligibility result is:

```text
historical-eligibility manipulation
-> altered re-entry probability / latency / stability
while some cue-specific neuronal content coding remains measurable
```

If NEURAL31 is downgraded, this arm must be reclassified or removed rather than used as independent support for NEURAL33.

A stronger independent-content result would require substantially different evidence and would force revision of the current NEURAL31 content/eligibility separation.

---

## 9. Retention vs retrievability arm

Select memories / items with comparable retention-strength metrics, then sample retrieval across different current physiological / phase states.

Test whether:

\[
Trace_A\approx Trace_B
\]

can coexist with:

\[
P_{reentry}(A|E_t)\neq P_{reentry}(B|E_t).
\]

This directly tests:

```text
retention
!= current retrievability
```

and avoids treating a retrieval failure as automatic evidence of complete trace loss.

---

## 10. Statistical discipline

### 10.1 Hierarchical structure

Cell-pairs and trials are nested within sessions and patients. Use hierarchical / mixed-effects models or another explicitly justified dependence-aware approach.

### 10.2 Avoid pair-count pseudo-certainty

Large neuron-pair counts can produce extremely small P values. Predefine:

```text
minimum effect size;
subject-level consistency threshold;
out-of-sample prediction criterion;
confidence intervals.
```

### 10.3 Interaction reliability

For `H x E`, preregister:

```text
feature construction;
phase binning or continuous model;
interaction sign / form when theoretically justified;
regularization;
held-out evaluation.
```

Do not mine many physiological phases and retain only the best interaction without multiplicity control.

### 10.4 Mediation caution

An observational chain:

```text
H/E -> W -> S_R -> Y
```

is not automatically causal mediation. Report it as predictive / temporal structure unless interventions identify the arrows.

---

## 11. Decisive result matrix

| Result | NEURAL33 consequence |
|---|---|
| `S_R` predicts behavior beyond component activity across replications | strengthens `component state != organizational state` bridge |
| `H x E` predicts relation reinstatement | strengthens history-conditioned current eligibility bridge |
| pre-event state predicts which content relation re-enters | strengthens content-selective eligibility, not just generic readiness |
| relation similarity survives overlap matching + conditional permutation + held-out component-overlap controls | strengthens organizational-continuity hypothesis |
| ripple specificity fails but transient event coordination remains | downgrade ripple specificity; retain relational-window bridge |
| all relation effects vanish after rate/power controls | major downgrade of NEURAL33 |
| pre-state predicts only arousal / RT | downgrade content-selective eligibility claim |
| same-content recurrence is fully explained by component overlap | downgrade relation-over-membership increment |
| causal manipulation changes only excitability, not relation-specific retrieval | downgrade coordination-window mechanism |

---

## 12. What this protocol does not test

It does not directly test:

```text
whether co-ripples cause consciousness;
whether a distributed coalition is the bearer;
whether L1 equals neural broadcast;
whether d-value or Psi_f has a ripple proxy;
whether relations are metaphysically fundamental;
whether SRT ontology is true.
```

Those require separate operationalizations and must not be inferred from a successful NEURAL33 experiment.

---

## 13. Minimal preregistered test if resources are limited

If only one study is feasible, prioritize:

### History × Phase × Relational Reinstatement

Collect:

```text
item-specific encoding strength H_m;
respiration + ECG + LFP pre-retrieval state E_t;
co-ripple timing W_t;
encoding-to-retrieval relational similarity S_R;
RT / accuracy Y_t.
```

Primary tests:

```text
1. S_R ~ H + E + H:E + controls
2. Y ~ X + S_R + controls
3. content-specific S_R prediction from pre-event E vs generic RT prediction
```

This minimal package targets the most distinctive bridge claim:

> **Past history changes what can be re-entered, but that historical efficacy is expressed conditionally through the system's current state rather than as a fixed stored-output scalar.**
