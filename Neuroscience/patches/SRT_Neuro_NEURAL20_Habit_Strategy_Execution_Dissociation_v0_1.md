---
patch_id: PATCH-NEURO-NEURAL20-HABIT-STRATEGY-EXECUTION-DISSOCIATION
source_ids:
  - SRC-2026-08-03-NEURO-ASAOKA-HABIT-STRATEGY-EXECUTION-DISSOCIATION
domain: neuroscience_habit_plasticity_action_control
claim_level: bridge
canonical_status: non_canonical
status: patch
target_documents:
  - "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
  - "Neuroscience/SRT_Neuro_Predictions_Table.md"
related_claims:
  - L2_script_formation
  - L2_execution_gain
  - real_choice_moment
  - script_execution
  - outcome_sensitivity
  - reselection_capacity
  - compulsive_behavior
tags:
  - habit
  - automaticity
  - strategy
  - execution
  - prefrontal_plasticity
  - outcome_devaluation
  - reselection
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_patch
id: PATCH-NEURO-NEURAL20-HABIT-STRATEGY-EXECUTION-DISSOCIATION
---

# SRT Neuroscience Patch NEURAL20: Habit Strategy–Execution Dissociation v0.1

> **Status**: bounded neuroscience action-control bridge.  
> **Canonical caution**: this patch does not define `L_2`, real choice, habit, compulsion, or the neural implementation of `G_hat_theta`. It separates two experimentally dissociable dimensions of habitual behavior.

## 0. Source anchor

Primary source:

- Nozomi Asaoka, Diane Pagano, and Yasunori Hayashi. "Dissociable roles of prefrontal plasticity in decision-making strategy and execution of habitual behavior." *Nature Communications* (2026). DOI: `10.1038/s41467-026-75706-1`.

Source card:

```text
Materials/2026/SRC_2026_08_03_Neuro_Asaoka_Habit_Strategy_Execution_Dissociation.md
```

## 1. Why this matters for SRT

SRT distinguishes real choice moments from script execution and describes `L_2` as historically sedimented constraint. A common operational shortcut is nevertheless too coarse:

```text
more repeated or intense behavior
-> stronger habit
-> more complete L2 replacement of live choice
```

The source reports a causal dissociation between the mechanism associated with adopting a habitual strategy and the mechanism regulating how much habitual behavior is executed. This means behavioral frequency cannot serve as a unitary readout of historical policy takeover.

## 2. Source-to-SRT mapping

| Source result | Local operational role | Bounded SRT bridge | Must not be identified with |
|---|---|---|---|
| ACC-to-RSC plasticity | reported control of decision strategy transition | candidate script-admission mechanism in this task | canonical `L_2` or loss of choice |
| lOFC-to-central-striatum plasticity | reported control of execution amount | candidate script-execution gain mechanism | `G_hat_theta` or compulsivity in general |
| outcome or motivation insensitivity | behavioral habit criterion | local proxy for policy takeover | proof that real choice is absent |
| execution frequency or duration | quantity of habitual output | local output-gain measure | habit depth or stake |
| selective pathway manipulation | causal dissociation test | evidence that strategy and execution can vary separately | universal circuit architecture |

## 3. Main SRT bridge claim

### Claim NEURAL20

At least three dimensions should be separated when SRT analyzes habitual or scripted behavior:

\[
\mathcal H_{local}
=
\left(H_{gate},\ H_{gain},\ R_{reselect}\right),
\]

where:

- `H_gate` is a declared laboratory proxy for transition from current outcome-sensitive control to a history-dominated policy;
- `H_gain` is the amount, frequency, or persistence of execution once that policy is active;
- `R_reselect` is the capacity to reopen, revise, or reverse the policy when consequences or rules change.

These are local bridge variables, not canonical SRT symbols.

The stable distinction is:

```text
script admission
!=
script execution gain
!=
reselection capacity
```

## 4. Why repetition is insufficient

Four cases are possible in principle:

| Strategy conversion | Execution gain | Interpretation |
|---|---|---|
| low | low | predominantly current outcome-sensitive control with limited output |
| low | high | strong output without clear evidence of historical policy takeover |
| high | low | history-dominated strategy with modest execution |
| high | high | history-dominated strategy with strong execution |

A fifth diagnostic question cuts across all four:

```text
Can the system reopen the policy when outcomes, rules, or consequences change?
```

This reselection question is closer to SRT's support-versus-replacement boundary than raw repetition is.

## 5. New claim cluster

### NEURAL20a — habit is not a unitary scalar

Strategy selection and execution quantity can be manipulated separately. SRT-facing studies should therefore avoid a single "habit strength" score when evidence permits decomposition.

### NEURAL20b — script replacement requires an outcome-sensitivity test

Repeated action is not sufficient evidence that a historical policy has displaced current evaluation. Outcome devaluation, contingency degradation, rule reversal, or equivalent tests are required.

### NEURAL20c — real-choice claims require reselection evidence

Outcome insensitivity supports an automaticity claim but does not prove ontological absence of real choice. A stronger SRT test must ask whether the policy can be reopened, whether consequences return, and whether future action architecture changes.

### NEURAL20d — pathological intervention may target different axes

A system may require intervention at strategy admission, execution gain, reselection, or more than one axis. Suppressing output is not the same as restoring live choice.

## 6. Experimental and operational consequences

### H-NEURAL20a: matched execution, different strategy

Select animals or conditions with similar action counts but different outcome sensitivity. SRT predicts that reversal cost and future policy rigidity should track strategy conversion and reselection more closely than action count alone.

### H-NEURAL20b: matched strategy, different execution

Among subjects that meet the same habit criterion, manipulate or measure execution gain. High output should not automatically imply lower `T_dir`, greater `L_2` replacement, or higher stake.

### H-NEURAL20c: third-axis reselection test

After habit induction, introduce a rule or consequence change that requires policy reopening rather than simple extinction. Measure:

- latency to detect the change;
- exploration of alternative actions;
- reversal and reinstatement costs;
- sensitivity to returned consequences;
- persistence after the original cue is removed;
- later policy flexibility.

### H-NEURAL20d: support versus replacement

Compare a trained routine that lowers local burden while preserving rapid revision with a routine that performs efficiently but resists consequence-sensitive reopening. Similar performance with different `R_reselect` would support the SRT distinction between supportive and replacement-like `L_2`.

## 7. Boundary cautions

1. Outcome-insensitive behavior is not proof that real choice is metaphysically absent.
2. The identified mouse pathways are task-specific implementation candidates, not universal SRT operators.
3. The study is not a clinical OCD or addiction trial.
4. Only male mice were reported in the discovery material used for this pass.
5. Full methods, statistics, and supplementary analyses still require close-read before importing fine-grained circuit claims.
6. `H_gate`, `H_gain`, and `R_reselect` are bridge variables, not canonical additions.
7. Ordinary reinforcement-learning and action-control models remain the primary competitors; SRT must generate residual predictions rather than rename their variables.

## 8. Integration hook

```text
Neuroscience/hooks/NEURAL20_Habit_Strategy_Execution_Dissociation_Integration_Hook.md
```

## 9. One-paragraph abstract

NEURAL20 separates habitual policy conversion from habitual execution amount and adds reselection capacity as the SRT-specific diagnostic dimension. The source supports a bounded bridge in which a behavior can become relatively outcome-insensitive through one pathway while its execution level is regulated through another. This blocks the inference from repetition or intensity to complete historical policy takeover. The patch proposes `H_gate`, `H_gain`, and `R_reselect` only as local operational coordinates and requires outcome-sensitivity, reversal, consequence-return, and policy-reopening tests before making claims about `L_2` replacement or real choice.
