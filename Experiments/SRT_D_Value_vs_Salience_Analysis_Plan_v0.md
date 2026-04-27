---
id: SRT-D-VALUE-VS-SALIENCE-ANALYSIS-PLAN-V0-2026-04-27
type: analysis_plan
tags:
  - SRT
  - Experiments
  - Analysis-Plan
  - d-value
  - Salience
  - Pilot
  - Mixed-Models
  - Pre-Registration
  - Proxy-Measurement
status: draft_v0
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: analysis_plan
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Experiments/SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md
  - Experiments/SRT_Pilot_Cards_v1.md
  - Experiments/SRT_Experimental_Roadmap_v1.md
  - Core/SRT_Validation_Template.md
  - Papers/SRT_D_Value_Ontology_of_Concern_Outline.md
machine_summary: >
  Draft analysis plan for the first SRT pilot: d-value vs salience. It defines pre-rating, item selection,
  main task structure, primary and secondary outcomes, mixed-effects models, exclusion criteria, robustness
  checks, expected patterns, failure conditions, and narrowing rules. It treats d_proxy as an operational proxy,
  not as identical to d-value.
---

# SRT d-value vs Salience Analysis Plan v0

> **Purpose**: Make the `d-value vs salience` pilot statistically and methodologically executable.  
> **Status**: Draft analysis plan. Not a preregistered protocol yet.  
> **Core rule**: `d_proxy` is an operational proxy candidate, not identical to `d-value`.

---

## 0. Research question

Can SRT's `d-value` construct be empirically separated from salience?

Main question:

```text
Do d_proxy ratings predict delayed recall, substitution resistance, cost-bearing,
and future decision reweighting beyond salience, arousal, preference, and confidence?
```

---

## 1. Core hypothesis

### H1 — Primary SRT hypothesis

Items with higher `d_proxy` will predict downstream outcomes beyond salience.

Primary outcomes:

```text
delayed recall;
substitution resistance;
willingness to bear cost;
future decision reweighting.
```

Baseline controls:

```text
salience;
arousal;
preference;
confidence;
attention capture.
```

### H0 — Baseline reduction hypothesis

Salience, arousal, preference, and confidence fully explain downstream outcomes. `d_proxy` adds no predictive value.

---

## 2. Operational definitions

### 2.1 Salience

Participant-rated noticeability / attention capture.

Suggested item:

```text
How much does this scenario stand out or catch your attention?
1 = not at all; 7 = extremely
```

### 2.2 d_proxy

Operational proxy candidate for `d-value`.

```text
d_proxy = mean(
  personal_relevance,
  future_impact,
  non_substitutability,
  cost_bearing,
  identity_relevance,
  obligation_weight
)
```

Guardrail:

> `d_proxy` is not the same as `d-value`; it is a first-pass measurable proxy family.

### 2.3 Downstream reorganization

In this pilot, downstream reorganization is approximated by:

```text
memory persistence;
substitution resistance;
willingness to bear time/effort cost;
future decision impact.
```

---

## 3. Study structure

### Phase 1 — Pre-rating study

Purpose:

```text
select and match items before the main pilot.
```

Participants:

```text
N = 80-150 online participants
```

Task:

```text
rate each scenario on salience, arousal, preference, personal relevance,
future impact, non-substitutability, cost-bearing, identity relevance,
obligation weight, distress risk, and comprehension.
```

Output:

```text
final item set with matched or statistically controllable salience.
```

### Phase 2 — Main pilot

Participants:

```text
N = 100-200 online participants
```

Task structure:

```text
1. scenario exposure;
2. immediate ratings;
3. filler task;
4. incidental memory test;
5. substitution resistance task;
6. cost-bearing task;
7. future reweighting task;
8. optional delayed recall after 24 hours.
```

---

## 4. Item selection rules

From `SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md`, select:

```text
10-15 high salience / low d_proxy items;
10-15 matched salience / high d_proxy items;
10-15 low-to-moderate salience / high d_proxy items;
10 neutral controls.
```

Exclusion rules:

```text
distress risk mean > 5.0;
comprehension failure > 20%;
extreme demographic skew;
ceiling salience and ceiling d_proxy simultaneously;
strong political / religious / traumatic content;
ambiguous or culturally narrow wording.
```

Matching strategy:

```text
Primary contrast should match salience where possible.
If exact matching is not possible, salience enters as a covariate.
```

---

## 5. Primary outcomes

### 5.1 Delayed recall

Measures:

```text
free recall accuracy;
recognition accuracy;
recall detail score;
false recall rate;
confidence in recall.
```

Primary recall variable:

```text
RecallScore = standardized composite of recall accuracy + detail - false recall
```

### 5.2 Substitution resistance

Prompt:

```text
Would replacing what is at stake with a more convenient or more expensive alternative preserve what mattered?
```

Scale:

```text
1 = easily replaceable;
7 = not replaceable without losing what mattered.
```

### 5.3 Cost-bearing

Prompt:

```text
How much time or effort would you be willing to spend to preserve, repair, or avoid losing what is at stake?
```

Scale:

```text
1 = none;
7 = a great deal.
```

### 5.4 Future reweighting

Prompt:

```text
Would this scenario change what you choose next week or next month?
```

Scale:

```text
1 = no effect;
7 = strong effect.
```

---

## 6. Secondary outcomes

```text
reaction time;
immediate emotional intensity;
confidence;
preference valence;
attention capture;
scenario vividness;
subjective importance;
identity relevance as separate predictor;
obligation weight as separate predictor.
```

---

## 7. Primary models

### 7.1 Continuous outcomes

Use mixed-effects regression:

```text
Outcome ~ d_proxy + Salience + Arousal + Preference + Confidence +
          (1 | Participant) + (1 | Item)
```

Outcomes:

```text
SubstitutionResistance;
CostBearing;
FutureReweighting;
RecallScore.
```

Primary test:

```text
d_proxy coefficient > 0 and remains meaningful after baseline controls.
```

### 7.2 Binary recall outcome

If recall is binary:

```text
RecallBinary ~ d_proxy + Salience + Arousal + Preference + Confidence +
               (1 | Participant) + (1 | Item)
```

Use logistic mixed-effects model.

---

## 8. Incremental validity tests

Compare nested models.

Baseline model:

```text
Outcome ~ Salience + Arousal + Preference + Confidence +
          (1 | Participant) + (1 | Item)
```

SRT proxy model:

```text
Outcome ~ Salience + Arousal + Preference + Confidence + d_proxy +
          (1 | Participant) + (1 | Item)
```

Key comparison:

```text
Does adding d_proxy improve model fit or predictive performance?
```

Possible metrics:

```text
AIC / BIC;
cross-validated prediction error;
likelihood ratio test;
Bayesian model comparison if using Bayesian models;
standardized beta / credible interval.
```

---

## 9. Robustness checks

### 9.1 d_proxy component check

Test components separately:

```text
personal_relevance;
future_impact;
non_substitutability;
cost_bearing;
identity_relevance;
obligation_weight.
```

Goal:

```text
Check whether d_proxy is driven by only one component.
```

### 9.2 Salience-matched subset

Run primary models only on items where salience is closely matched.

### 9.3 Low-distress subset

Exclude items with distress risk above a conservative threshold.

### 9.4 Preference-valence control

Test whether positive vs negative valence explains the pattern.

### 9.5 Moral-obligation control

Test whether obligation weight alone explains all d_proxy effects.

This is important because:

```text
d-value should not collapse into moral intensity.
```

---

## 10. Expected patterns

### Strong support for SRT

```text
d_proxy predicts all or most primary outcomes beyond salience/arousal/preference/confidence;
model comparison favors adding d_proxy;
effects remain in salience-matched and low-distress subsets;
non-substitutability and future impact contribute independently.
```

### Moderate support

```text
d_proxy predicts substitution resistance and future reweighting,
but not delayed recall after controls.
```

### Weak support

```text
d_proxy predicts outcomes only before salience/arousal/preference controls.
```

### Failure pattern

```text
salience/arousal/preference/confidence fully explain all outcomes;
d_proxy adds no predictive value;
item category differences disappear after baseline controls.
```

---

## 11. Failure and narrowing rules

### Failure condition

If baseline variables fully explain outcomes, then this pilot does not support a distinct `d-value` construct.

### Narrowing rule 1

If only non-substitutability predicts outcomes:

```text
narrow d-value to non-substitutability rather than broad concern bandwidth.
```

### Narrowing rule 2

If only moral obligation predicts outcomes:

```text
separate moral intensity from d-value or narrow d-value to obligation-bearing cases.
```

### Narrowing rule 3

If only identity relevance predicts outcomes:

```text
narrow d-value to identity / self-continuity contexts.
```

### Narrowing rule 4

If no component predicts beyond salience:

```text
treat d-value as a theoretical redescription until better proxies are designed.
```

---

## 12. Exclusion criteria

Participant-level exclusion:

```text
failed attention checks;
completion time unrealistically fast;
missing more than 20% responses;
straight-lining across rating scales;
failed comprehension on more than 30% sampled items.
```

Item-level exclusion:

```text
mean distress risk > 5.0;
comprehension failure > 20%;
ambiguous or culturally dependent interpretation;
excessive salience/d_proxy collinearity;
ceiling/floor effects.
```

---

## 13. Data dictionary v0

| Variable | Type | Description |
|---|---|---|
| participant_id | string | anonymous participant identifier |
| item_id | string | scenario ID from stimulus bank |
| category | categorical | A/B/C/D/E stimulus category |
| salience | numeric 1-7 | noticeability rating |
| arousal | numeric 1-7 | emotional activation |
| preference | numeric -3 to +3 | like/dislike or preference valence |
| confidence | numeric 1-7 | confidence in rating or recall |
| personal_relevance | numeric 1-7 | personal relevance |
| future_impact | numeric 1-7 | future option impact |
| non_substitutability | numeric 1-7 | replacement resistance |
| cost_bearing | numeric 1-7 | willingness to bear cost |
| identity_relevance | numeric 1-7 | relation to self / desired self |
| obligation_weight | numeric 1-7 | responsibility / obligation |
| distress_risk | numeric 1-7 | discomfort / distress |
| d_proxy | numeric | mean of d_proxy components |
| recall_binary | binary | recalled or not |
| recall_detail | numeric | coded detail score |
| substitution_resistance | numeric 1-7 | outcome |
| future_reweighting | numeric 1-7 | outcome |
| rt_ms | numeric | reaction time in milliseconds |

---

## 14. Reporting template

Report results as:

```text
1. Item pre-rating summary;
2. Correlation matrix among salience, arousal, preference, and d_proxy;
3. Primary mixed model results;
4. Incremental validity tests;
5. Robustness checks;
6. Failure / narrowing interpretation;
7. Next pilot revision.
```

Do not report the pilot as confirming SRT. Use:

```text
supports / does not support a distinct d_proxy effect in this operationalization.
```

---

## 15. Minimal preregistration text

Possible preregistration statement:

```text
We test whether an operational proxy for SRT d-value predicts memory persistence,
substitution resistance, willingness to bear cost, and future decision reweighting beyond salience,
arousal, preference, and confidence. We define d_proxy as the mean of personal relevance,
future impact, non-substitutability, cost-bearing, identity relevance, and obligation weight.
The primary analysis will use mixed-effects models with random intercepts for participant and item.
If d_proxy does not improve prediction beyond baseline variables, we will treat this pilot as failing
to support d-value as a distinct operational construct in this design and will narrow the construct or revise proxies.
```

---

## 16. Minimal conclusion

This analysis plan makes the first SRT pilot falsifiable in a limited sense.

It does not test all of SRT.

It tests one operational question:

```text
Does d_proxy explain downstream effects that salience does not?
```
