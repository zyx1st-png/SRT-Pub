---
source_id: SRC-2026-08-03-NEURO-ASAOKA-HABIT-STRATEGY-EXECUTION-DISSOCIATION
title: "Dissociable roles of prefrontal plasticity in decision-making strategy and execution of habitual behavior"
source_type: peer_reviewed_open_access_original_research
domain: neuroscience_habit_plasticity_action_control
url: "https://www.nature.com/articles/s41467-026-75706-1"
doi: "10.1038/s41467-026-75706-1"
authors: "Nozomi Asaoka; Diane Pagano; Yasunori Hayashi"
publication: "Nature Communications"
date_published: "2026-07-27"
date_added: "2026-08-03"
evidence_level: peer_reviewed_open_access_primary_abstract_and_publisher_metadata
reliability_level: high_for_reported_mouse_pathway_dissociation; full_method_close_read_pending
content_access: "Primary Nature Communications abstract and metadata plus detailed Kyoto University research report; full article methods not close-read in this pass"
srt_relevance: very_high
integration_priority: high
related_srt_claims:
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
  - anterior_cingulate_cortex
  - retrosplenial_cortex
  - orbitofrontal_cortex
  - striatum
  - synaptic_plasticity
  - Nature_Communications
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-08-03-NEURO-ASAOKA-HABIT-STRATEGY-EXECUTION-DISSOCIATION
---

# SourceCard: Dissociable Habit Strategy and Execution Control

## 1. One-line summary

Asaoka, Pagano, and Hayashi report that the transition from motivation-sensitive to habitual decision strategy and the amount of habitual behavior executed are controlled by plasticity in distinct cortical pathways, allowing selective alteration of strategy or execution level without necessarily altering the other.

## 2. Core source claims

Usable source-level claims:

1. The study developed a training paradigm that induced habit formation within a defined four-day window in male mice.
2. Habit formation was operationalized as a shift from motivation-driven or outcome-sensitive control toward an automatic strategy.
3. Plasticity in an anterior cingulate cortex to retrosplenial cortex pathway was associated with whether behavior shifted into a habitual strategy.
4. Connectivity in this pathway weakened during the transition reported by the authors.
5. Plasticity in a lateral orbitofrontal cortex to central striatum pathway was associated with the amount or intensity of habitual execution.
6. Animals differed in execution level even after habit formation.
7. Experimental erasure or manipulation of each plasticity selectively changed either decision strategy or execution amount without changing the other in the reported tests.
8. The authors therefore propose a dual regulatory model of habitual behavior.
9. The findings may inform maladaptive habits and compulsive or addictive disorders, but the experiment is not itself a human OCD study.
10. The identified pathways are implementation-level mechanisms and do not define habit, agency, or choice across all systems.

## 3. Evidence and method

- Species and sex: male mice.
- Behavioral design: two-stage training with a rapid, defined habit-induction period.
- Behavioral distinction: decision-making strategy versus quantity, frequency, or duration of execution.
- Neural focus: prefrontal projections involving ACC-to-RSC and lateral OFC-to-central striatum pathways.
- Causal logic: pathway plasticity was experimentally erased or bidirectionally manipulated to test selective effects.
- Primary source statement: erasing each plasticity selectively altered decision strategy or execution level without affecting the other.
- Evidence boundary: the article is peer reviewed and open access, but this card was prepared from primary abstract and publisher metadata plus the institutional report; detailed methods, statistics, and supplementary analyses remain to be close-read.

## 4. Main limits

1. The study uses an accelerated laboratory habit paradigm in male mice.
2. Outcome-insensitive or automatic control is an operational behavioral construct, not proof that no real choice occurs.
3. Repetition count alone cannot identify whether strategy conversion has occurred.
4. High execution intensity does not necessarily imply deeper habit formation.
5. The pathways may be task-, species-, sex-, and protocol-dependent.
6. Clinical relevance to OCD and addiction is prospective rather than directly demonstrated in patients.
7. Circuit plasticity does not define canonical `L_2`, `G_hat_theta`, `d`, `Psi_f`, or subjecthood.
8. Full-method close-read is still required before importing detailed pathway timing, statistical effect sizes, or clinical claims.

## 5. SRT relevance

The source gives SRT a strong correction to an overly compressed model of habit:

```text
habit strength
is not one variable
```

At minimum, the following should be separated:

```text
strategy conversion:
  does historical control replace current outcome-sensitive control?

execution gain:
  once the historical policy is active, how much behavior is produced?
```

This matters for the SRT distinction between real choice moments and script execution. Repeated or intense behavior cannot by itself establish that `L_2` has replaced live choice. A behavior may show strong execution with limited strategy conversion, or clear strategy conversion with modest execution.

A safe bridge is:

```text
L2 policy takeover
!=
L2 execution intensity
```

An unsafe identity is:

```text
ACC-RSC = L2
lOFC-striatum = G_hat_theta
habitual behavior = absence of real choice
```

## 6. Bidirectional gain card

### New interface

- `script-admission gate`: whether action control becomes relatively insensitive to current motivational outcome.
- `script-execution gain`: frequency or amount of action after the script is active.
- pathway-specific causal dissociation between the two.

### Reverse correction to SRT

- Do not infer `L_2` replacement from behavioral repetition alone.
- Do not infer loss of real choice from high execution volume alone.
- Do not treat automaticity as a unitary scalar.
- Do not generalize one mouse circuit as the universal implementation of history-based control.

### Strengthened SRT content

- Historical constraints can control policy selection and output intensity through separable mechanisms.
- Healthy support versus lethal replacement should be tested through outcome sensitivity and reselection, not raw frequency.
- Intervention can in principle reduce pathological execution without erasing all learned structure.

### SRT contribution back to the source

SRT can add a third dimension absent from the basic dual model:

```text
strategy conversion
x execution gain
x reselection capacity
```

Two systems with similar habit strategy and execution may differ in whether they can reopen the policy, register consequences, and reorganize future behavior.

### Residual pressure

If strategy conversion, execution gain, and ordinary reinforcement-learning variables fully explain persistence, reversal, and consequence sensitivity, SRT must show what independent prediction is added by `L_2` replacement or real-choice terminology.

## 7. Suggested patch target

Primary patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL20_Habit_Strategy_Execution_Dissociation_v0_1.md
```

Future synthesis targets:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuro_Predictions_Table.md
```
