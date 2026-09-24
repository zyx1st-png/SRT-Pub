---
id: SRT-GRG-CASE2-ENGAGEMENT-VERTICAL-DECOMPOSITION-PREREG-20260924
type: preregistration
status: frozen
date: 2026-09-24
layer: operations
epistemic_layer: os
claim_mode: research_programme
canonical: false
research_mode: TEST
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_DECISION_GRG_CASE2_ENGAGEMENT_2026-09-24.md
  - Operations/Proposals/SRT_GRG_FUSION_CASE_CARD_ITERATION_PLAN_2026-09-23.md
  - Operations/Proposals/SRT_GRG_CROSS_OBJECTIFICATION_GENERATIVE_ARCHITECTURE_V0_1_2026-09-23.md
  - Operations/GRG/SRT_GRG_CROSS_OBJECTIFICATION_ANTI_DRIFT_PROTOCOL_V0_1_2026-09-23.md
tags: [GRG, Case2, Engagement, RecommenderSystems, Preregistration, VerticalDecomposition]
---

# Preregistration — case 2: engagement as a bundled optimization object

## 0. Freeze boundary

This preregistration is frozen **before source-literature inspection for this case**.

The target is:

> engagement as an optimization object / metric in recommender systems and digital platforms.

This is the one author-authorized prospective case 2.

Do not:

- switch to another target after seeing results;
- replace engagement with satisfaction, retention, addiction, polarization, or another neighboring object;
- broaden to all recommender-system theory;
- add new probes after source inspection;
- change §8.1 status after the result.

## 1. Source-native adequacy gate — must be scored first

Before any GRG interpretation, establish:

### A0 — source identity

At least one mature source family where engagement is operationalized as an optimization target / metric.

### A1 — event/process unit

A source-native interaction unit sufficient to distinguish at minimum:

- opportunity / exposure;
- response or interaction;
- later system/user consequence if source-supported.

### A2 — strongest reasonable baseline

Before GRG scoring, the source review must explicitly inspect the strongest relevant baseline families, including where applicable:

- exposure / position / selection bias;
- click / watch / dwell-time prediction;
- counterfactual or debiased recommendation / learning-to-rank;
- long-term recommendation / sequential decision methods;
- feedback-loop / recommender-induced state-change work;
- metric alignment / satisfaction or long-term objective work.

### A3 — actual bundled-object use

Evidence must show that “engagement” or a closely related engagement objective is actually treated as a target / proxy / metric in the bounded source family.

If A0–A3 are not adequately grounded:

```text
SOURCE_ADEQUACY = FAIL
CASE2_COUNT = NO
STOP
```

If A0–A3 are grounded:

```text
SOURCE_ADEQUACY = PASS
CASE2_COUNT = YES
```

and the case counts under §8.1 regardless of GRG outcome.

## 2. Prospective GRG-generated decomposition

Before source inspection, freeze these hypothesized roles.

### E0 — opportunity / exposure formation

What determines whether an item/action possibility becomes available to the user at all?

### E1 — response propensity under context

Given exposure, what organization determines the user's tendency to respond?

### E2 — realized interaction

What actually occurs: click, watch, dwell, share, return, or another declared engagement event?

### E3 — metric attribution / aggregation

How are realized events converted into the engagement quantity used for optimization, comparison, ranking, or evaluation?

### E4 — downstream state writeback

What part of the realized interaction changes later generative conditions, such as:

- future user state;
- future ranking state;
- learned model state;
- candidate availability / exposure;
- session or platform state?

### E5 — longer-horizon consequence

What later consequence is being implicitly or explicitly used to justify the engagement objective, if any?

Examples may include satisfaction, retention, task completion, or welfare, but none is assumed source-native before review.

## 3. Frozen separations to test

### T1 — exposure != preference / propensity

Prediction:

```text
not observed
does not imply
not preferred
```

Failure condition:

- source already fully owns and operationally separates exposure opportunity from response propensity, leaving no extra target-source payoff.

### T2 — propensity != realized interaction

Prediction:

```text
response tendency
!=
realized engagement event
```

Failure condition:

- mature source already owns the distinction and GRG adds no diagnostic.

### T3 — realized interaction != engagement metric

Prediction:

```text
event occurrence
!=
the aggregation / weighting rule that makes it count as engagement
```

Failure condition:

- source measurement theory already makes this separation explicit and sufficient.

### T4 — engagement event != state-changing event

Prediction:

Two events can have similar immediate engagement value while differing materially in whether/how they alter future user/model/exposure conditions.

This is the most important prospective seam.

Failure condition:

- mature source work already explicitly separates immediate engagement reward from long-term user/system state effects and provides the needed diagnostics.

### T5 — metric gain != target consequence gain

Prediction:

Increasing the engagement metric need not imply improvement in the later consequence used to justify it.

Failure condition:

- source-native metric-alignment / long-term objective theory already owns the distinction sufficiently.

### T6 — grain recut

Prediction:

A quantity that is coherent at event/session level may change meaning under user/cohort/platform recuts.

Failure condition:

- mature source already makes the aggregation / causal-level dependence explicit and no extra diagnostic remains.

## 4. Frozen GRG-originated probes

### P1 — differential actualisation

Where does a merely available opportunity become an operative user/system difference, and is that distinct from realized interaction?

### P2 — foreground / background

Which background relations (ranking position, session state, candidate set, user history, interface context) alter consequence without being reducible to the focal item?

### P3 — retained efficacy

What from an engagement event actually enters later generative conditions, and what event would count as engagement without retained efficacy?

### P4 — consequence reach

When does a local engagement event remain local versus propagate into:

- user-state update;
- model update;
- future exposure;
- aggregate optimization?

### P5 — reconstruction / writeback

Does optimizing engagement alter the process that generates future engagement observations?

### P6 — recut survival

Which distinctions E0–E5 survive recutting from event to session to user to cohort/platform?

## 5. Predeclared positive threshold

A GRG vertical-gain candidate requires **all**:

1. SOURCE_ADEQUACY = PASS;
2. at least one T1–T6 separation is source-real;
3. the strongest mature source baseline does not already organize that separation sufficiently;
4. at least one P1–P6 probe yields a source-checkable diagnostic / intervention / negative control / failure boundary;
5. the payoff survives deletion of GRG vocabulary;
6. the payoff survives at least one legitimate grain recut;
7. no source mechanism is rebranded as a GRG discovery.

## 6. Allowed primary verdicts

Exactly one:

```text
SOURCE_INADEQUATE_CASE2_DOES_NOT_COUNT

SOURCE_OWNED_DECOMPOSITION_NO_GRG_GAIN

PARTIAL_VERTICAL_PAYOFF

RESIDUAL_VERTICAL_GAIN_CANDIDATE

INSUFFICIENT_EVIDENCE_AFTER_ADEQUACY
```

## 7. Stop-loss rule

If:

```text
SOURCE_ADEQUACY = PASS
and
primary verdict = SOURCE_OWNED_DECOMPOSITION_NO_GRG_GAIN
```

then:

```text
§8.1 adequate no-gain count:
  case 2

fusion lane:
  PAUSE / CONTRACT

third fusion domain:
  NO

replacement target:
  NO

post hoc narrower metric:
  NO
```

If SOURCE_ADEQUACY fails, the case does not count, but the lane does not get permission to shop indefinitely for replacements; a new target would require a fresh author root-return decision.

## 8. No post-result widening

Do not rescue a negative result by:

- switching from engagement to satisfaction;
- switching from immediate engagement to retention;
- choosing a different platform type;
- adding health / politics / polarization harms as a new success criterion;
- adding another GRG probe;
- changing the grain only after seeing failure;
- claiming cross-domain recurrence as payoff.

## 9. Execution order

```text
1. verify prereg freeze on main / landed route
2. source adequacy A0-A3
3. only if adequate, run T1-T6
4. run P1-P6
5. strongest-baseline absorption
6. recut test
7. exactly one primary verdict
8. §8.1 accounting
9. root return
```
