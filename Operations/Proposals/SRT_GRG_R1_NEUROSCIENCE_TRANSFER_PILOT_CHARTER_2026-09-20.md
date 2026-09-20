---
id: SRT-GRG-R1-NEUROSCIENCE-TRANSFER-PILOT-CHARTER-20260920
type: experimental_charter
status: active
record_stage: preregistered_before_target_result
version: v0.1
date: 2026-09-20
layer: operations
epistemic_layer: experimental
claim_mode: prediction
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
comparative_claim: none
named_comparator: none
n_mode_triggered: false
dependency:
  - Operations/Audits/SRT_GRG_DISTRIBUTED_NEIGHBOR_EXTRACTION_PASS1_2026-09-20.md
  - Neuroscience/SRT_NEURAL34_MATCHED_STATE_RELATIONAL_HISTORY_PROTOCOL_v0_1.md
  - Neuroscience/patches/SRT_Neuro_NEURAL36_Structured_History_Dynamical_Scaffold_Absorption_Pressure_v0_1.md
  - Materials/2026/SRC_2026_09_08_Neuro_Bowler_Structured_Experience_Strategy_Dynamics.md
tags: [GRG, GRGR1, TransferPilot, Neuroscience, RNN, RetainedOrganization, Withdrawal, Recombination, Preregistered]
---

# GRG-R1 bounded neuroscience transfer-pilot charter v0.1

> Freeze point: this file is to be committed before running the target simulation or inspecting any target result.
>
> This is a bounded transfer pilot for GRG-R1. It is not a new broad neuroscience deep well, not a test of whole-SRT novelty, not a canonical experiment, and not a claim that RNN organization is an ontological One.

## 0. Frozen GRG relation

### GRG-R1 — retained-organization re-entry

~~~text
A relation among components / participants produces an identifiable organization O.

O remains identifiable at the declared grain after the immediate formation event.

Holding relevant component capacities as fixed as the domain permits,
perturbing / removing O changes later transition, accessibility,
support, inhibition or coordination relations.

When O is withdrawn, the predicted organization-sensitive effect
disappears or changes in the predeclared direction.
~~~

Non-identities:

~~~text
GRG-R1 != generic path dependence
GRG-R1 != mere correlation
GRG-R1 != One automatically
GRG-R1 != downward extra force
GRG-R1 != universal Selection definition
~~~

The wording above is frozen for this pilot. If the result is inconvenient, the relation may be rejected or narrowed later, but its core meaning may not be changed to rescue the pilot.

## 1. Why this is not NEURAL34 renamed

NEURAL34 asks whether relation-specific history adds prediction after rich present-state controls.

GRG-R1 adds a stronger causal requirement:

~~~text
history / training
-> identifiable formed organization O
-> O is independently measured before the target transfer test
-> targeted withdrawal of O
-> changed later transition / accessibility
~~~

A history coefficient without an independently identified and perturbable O is insufficient.

A generic lesion / noise effect is also insufficient.

The critical new control is:

~~~text
organization-targeted withdrawal
vs
dimension-matched / magnitude-matched generic perturbation.
~~~

## 2. Domain and model class

Domain: computational neuroscience / recurrent neural dynamics.

Model: small recurrent neural networks trained on a context-dependent sequential classification task.

This pilot uses a synthetic RNN because:

- the relation can be frozen before target-result inspection;
- organization can be measured and perturbed directly;
- component and perturbation controls can be made explicit;
- the old exact NEURAL34 human-data charter remains DATA-ACCESS-0 NO-GO and must not be weakened for convenience.

A positive synthetic result is at most a realization / transfer result. It does not establish a biological mechanism.

## 3. Histories

Two training-history classes:

### Structured history S

Train simpler context-conditioned subtasks first, then the common full base task.

### Direct history D

Train only the common full base task.

Both groups must reach the same base-task competence threshold before entering the critical transfer phase.

The pilot does not require S to outperform D at baseline. If baseline competence cannot be matched, the run is invalid for the primary comparison.

## 4. Base task

Each trial contains:

- a context cue;
- a short sequence of binary / categorical observations;
- a response determined by a context-dependent mapping.

The full base task contains at least two contexts that require different mappings over partially overlapping inputs.

The base task is intentionally simple enough that both S and D histories can reach high performance.

## 5. Target transfer task

The target is a **context recombination / reversal** not used during training.

It changes which learned relation between context and input determines the correct response while keeping:

- input alphabet;
- recurrent unit count;
- output format;
- trial duration;
- observation statistics

as close as possible to the base task.

Primary transfer readouts:

1. zero-shot transfer accuracy before any target-task weight update;
2. epochs / updates to a fixed transfer criterion if fine-tuning is enabled;
3. switching / context-routing error rate;
4. relapse / hysteresis toward the old mapping during early fine-tuning.

The target is not inspected before the intervention definitions below are frozen.

## 6. Independent identification of organization O

O must be identified from **base-task activity only**, before target-transfer outcomes are computed.

Primary O:

~~~text
the low-dimensional hidden-state subspace carrying context-dependent routing information
during the decision-relevant portion of the base task.
~~~

Operational extraction:

1. collect hidden states on held-out base-task trials;
2. center within declared trial phase;
3. fit a linear context decoder on training folds only;
4. derive a rank-k orthonormal context-discriminative subspace from decoder weight / between-context hidden-state structure;
5. choose k by a fixed rule before target evaluation:
   smallest k in {1,2,3,4} reaching >= 90% of cross-validated context-decoding performance of k=4;
6. freeze the resulting basis per network.

O is admitted only if held-out base-task context decoding exceeds 80%.

Failure to identify O above threshold means that network is excluded from the **O-withdrawal** test for a predeclared technical reason, not because of target results.

## 7. Interventions

Run all interventions on the same frozen trained network.

### I0 — intact

No hidden-state projection.

### I-O — targeted O withdrawal

At each recurrent step in the declared decision interval, remove the projection of hidden state onto O:

~~~text
h' = h - P_O h
~~~

No weights are retrained before zero-shot evaluation.

### I-R — random-subspace control

Remove a random rank-k orthonormal subspace from hidden state.

Requirements:

- same k as I-O;
- same intervention timing;
- random basis drawn independently of target labels;
- at least 8 random bases per network;
- report the mean random-control effect and distribution.

### I-N — magnitude-matched isotropic-noise control

Add zero-mean noise calibrated on base-task held-out activity so that the mean hidden-state displacement norm matches the displacement produced by I-O within +/-10%.

This distinguishes organization-specific withdrawal from generic disruption magnitude.

## 8. Primary prediction

Let:

~~~text
Delta_O = transfer performance(intact) - transfer performance(I-O)

Delta_R = transfer performance(intact) - mean transfer performance(I-R)

Delta_N = transfer performance(intact) - transfer performance(I-N)
~~~

For accuracy-like metrics, the preregistered GRG-R1-compatible direction is:

~~~text
Delta_O > Delta_R
and
Delta_O > Delta_N.
~~~

For epochs-to-criterion / error-like metrics, use the sign-reversed equivalent.

Primary inferential unit = independently trained network seed, not individual trial.

The pilot is positive for GRG-R1 only if the targeted-withdrawal effect is larger than both control families with a non-trivial seed-level effect.

## 9. Retention / re-entry requirement

A targeted perturbation effect alone is not enough.

O must additionally satisfy:

### retention

O is measured after base-task training and before target transfer.

### re-entry

O predicts or supports later context routing on the new transfer task.

### withdrawal

Removing O produces a larger transfer impairment than dimension- and magnitude-matched controls.

The pilot does not require that the original training provenance remain irreducible once O is specified.

## 10. History role

History is secondary to the GRG-R1 primary test.

Exploratory but predeclared comparison:

~~~text
Does structured history S change:
- probability that an admissible O forms;
- dimensionality k of O;
- context-decoding strength of O;
- targeted-withdrawal effect Delta_O;
- target adaptation speed?
~~~

A history-group difference is not required for GRG-R1 realization.

If S and D both form causal O, the result supports a generic retained-organization relation rather than a history-specific SRT claim.

## 11. Negative controls and failure conditions

### Semantic failure

Record SEMANTIC-FAIL if interpreting the result requires redefining O after target inspection or changing GRG-R1's dependency direction.

### Domain transfer failure

Record TRANSFER-FAIL if ordinary domain practice already supplies exactly the same question, intervention and controls and the GRG transfer introduced no additional design constraint.

### Causal failure

Record CAUSAL-FAIL if:

- I-O is not more disruptive than random / magnitude controls;
- O is not independently decodable before target evaluation;
- the effect appears only after selecting O using target outcomes;
- intervention effects are fully explained by generic hidden-state norm collapse.

### Competence failure

Record BASE-MATCH-FAIL if the history groups cannot be brought to the declared common base competence range.

### Interpretation ceiling

Even a positive pilot does not establish:

- primitive Selection;
- One / Bearer / subject / consciousness;
- biological MEC implementation;
- SRT scientific distinctiveness;
- GRG universality.

## 12. Run plan

Initial run:

~~~text
network architecture: simple tanh RNN
hidden units: 32
training seeds: 12 structured + 12 direct
sequence length: fixed across histories and target
base competence gate: >= 95% held-out base accuracy
optimizer / learning-rate schedule: fixed before target evaluation
random-subspace controls: 8 per eligible network
target: one predeclared context-recombination mapping
~~~

If fewer than 8 eligible networks per history pass the base competence gate, the run is exploratory and cannot receive the pilot's primary PASS verdict.

## 13. Verdict contract

Exactly one primary outcome:

### PILOT-PASS

All of:

- O independently identified before target evaluation;
- enough eligible network seeds;
- targeted withdrawal impairs transfer more than both controls;
- result does not require semantic drift.

This means GRG-R1 successfully generated a domain-native causal design and survived this synthetic realization.

### PILOT-NULL

Execution valid but targeted O withdrawal does not outperform both controls.

GRG-R1 is not supported by this realization.

### PILOT-INVALID

Base-match, implementation, identification or intervention-matching requirements fail.

No theory inference.

### PILOT-SEMANTIC-FAIL

The relation must be changed after seeing results to claim success.

This is adverse evidence against current GRG-R1 transferability.

## 14. Repository / programme boundary

No canonical edit.

No NEURAL34 owner rewrite.

No NEURAL36 owner rewrite.

No new broad neuroscience deep well.

No strongest-neighbor winner claim.

After the run, write one noncanonical result record and return the result to the GRG programme scorecard: compression, constraint, transfer, revision.
