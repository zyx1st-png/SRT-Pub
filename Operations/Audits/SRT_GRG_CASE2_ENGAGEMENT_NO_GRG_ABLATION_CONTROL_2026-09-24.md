---
id: SRT-GRG-CASE2-ENGAGEMENT-NO-GRG-ABLATION-CONTROL-20260924
type: audit
status: draft
date: 2026-09-24
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
research_mode: TEST
dependency:
  - Operations/Audits/SRT_GRG_CASE2_ENGAGEMENT_VERTICAL_DECOMPOSITION_RESULT_2026-09-24.md
tags: [GRG, Case2, Engagement, Control, Ablation, MethodContraction]
---

# Post-stop-loss control — engagement decomposition without GRG probes

## 0. Purpose

This is a **post-stop-loss, non-adjudicative ablation**.

It asks one narrow question:

> If the same model is asked to decompose engagement using ordinary causal / systems analysis, without GRG vocabulary or GRG probe prompts, does it recover approximately the same role separations?

This control does **not**:

- reopen case 2;
- change its verdict;
- change §8.1 counting;
- rescue the fusion lane;
- constitute a new prospective test;
- establish training-data blindness.

## 1. Important limitation

This is **not** a clean blinded control.

The model has already:

- generated the GRG preregistration;
- read the engagement source literature;
- seen the case-2 result;
- seen the independent review.

Therefore this control is contaminated by both:

- model training priors;
- within-session / within-project exposure.

It can only answer:

~~~text
Does explicit GRG prompting appear necessary
to produce the broad decomposition now?
~~~

It cannot answer:

~~~text
Did GRG cause the original preregistered decomposition?
~~~

## 2. Control instruction

Use no SRT / GRG terminology.

Do not use:

- differential actualisation;
- foreground / background;
- retained efficacy;
- reach;
- reconstruction / writeback;
- Selection;
- cross-objectification.

Task:

> Analyze “engagement” as an optimization target in recommender/platform systems using ordinary causal, measurement, and systems analysis. Identify distinct roles that should not be conflated, explain which separations matter operationally, and state where optimization can feed back into later observations.

## 3. No-GRG decomposition output

### C0 — opportunity / exposure

Before an interaction can occur, the system determines which content is eligible and shown.

Operational distinction:

~~~text
not shown
!=
shown and ignored
~~~

### C1 — response probability conditional on context

Given exposure, the probability of clicking / watching / interacting depends on:

- user history;
- item characteristics;
- position / presentation;
- session context;
- candidate slate;
- prior system state.

Operational distinction:

~~~text
predicted response probability
!=
actual response
~~~

### C2 — realized interaction

Observed event:

- click;
- dwell / watch;
- share;
- conversion;
- return.

Operational distinction:

~~~text
one realized event
!=
the metric later computed from events
~~~

### C3 — measurement / objective construction

The platform chooses how events are:

- weighted;
- aggregated;
- normalized;
- combined across objectives;
- converted into ranking or RL reward.

Operational distinction:

~~~text
behavioral event
!=
optimization objective
~~~

### C4 — dynamic system effect

An interaction can change:

- future recommendations;
- user history;
- model parameters;
- training data distribution;
- future exposure opportunities.

Operational distinction:

~~~text
same immediate reward
-/>
same future-state effect
~~~

### C5 — downstream objective / proxy alignment

Engagement can be used as a proxy for:

- satisfaction;
- retention;
- long-term value;
- task success;
- ecosystem utility.

Operational distinction:

~~~text
metric improvement
-/>
improvement in the ultimate objective
~~~

### C6 — level / aggregation dependence

The meaning of engagement can change across:

- impression / item;
- slate;
- session;
- user;
- cohort;
- platform / ecosystem.

A metric useful at one grain may not retain the same interpretation at another.

## 4. Comparison with frozen GRG preregistration

| No-GRG control | Frozen case-2 role / test | Relation |
|---|---|---|
| C0 opportunity / exposure | E0 / T1 | near-equivalent |
| C1 response probability | E1 / T2 | near-equivalent |
| C2 realized interaction | E2 | near-equivalent |
| C3 objective construction | E3 / T3 | near-equivalent |
| C4 dynamic system effect | E4 / T4 / P5 | near-equivalent |
| C5 proxy alignment | E5 / T5 | near-equivalent |
| C6 aggregation dependence | T6 / P6 | near-equivalent |

The no-GRG control also naturally raises:

- exposure bias;
- immediate versus long-term consequence;
- feedback loops;
- metric / proxy misalignment;
- multi-level aggregation.

These are the same major seams that the GRG preregistration froze.

## 5. Incremental contribution audit

Question:

> What decomposition role appears in the GRG version that is absent from the no-GRG control?

Current answer:

~~~text
NONE CLEARLY ESTABLISHED
~~~

Question:

> Does the GRG version organize the roles in a materially sharper way?

Possible modest difference:

- GRG explicitly emphasizes retained efficacy, consequence reach, and reconstruction as distinct probe questions;
- ordinary systems analysis tends to collect these under generic feedback / dynamics.

But in this target, mature recommender theory already operationalizes those distinctions through:

- state transition;
- policy feedback;
- exposure distribution shift;
- long-term value;
- ecosystem effects.

Therefore:

~~~text
incremental target-domain decomposition payoff from GRG:
  NONE ESTABLISHED
~~~

## 6. Control verdict

~~~text
NO-GRG CONTROL REPRODUCES THE MAIN DECOMPOSITION
~~~

Interpretation:

> explicit GRG prompting was not necessary to recover the principal engagement seams in this post hoc ablation.

This supports a narrower conclusion than the original positive framing:

~~~text
GRG as uniquely valuable decomposition tool:
  NOT ESTABLISHED

ordinary causal / systems analysis:
  sufficient to recover the major seams in this target
~~~

## 7. What remains potentially useful

The surviving value of GRG in this lane is best characterized as:

- a standardized checklist for recurring generative questions;
- a governance discipline for prospective decomposition;
- a cross-project vocabulary for tracking whether distinctions are source-owned, new, or merely analogical.

What is **not** established:

- superior decomposition performance;
- novel scientific discovery;
- predictive advantage over ordinary expert/system analysis.

## 8. Relation to stop-loss

This control was added **after** the stop-loss verdict and therefore cannot alter it.

~~~text
case2 verdict:
  unchanged

§8.1 count:
  unchanged

fusion lane:
  PAUSE / CONTRACT if result landing is upheld

replacement domain:
  not authorized
~~~

Its only role is to clarify the post-stop-loss positioning of GRG methodology.
