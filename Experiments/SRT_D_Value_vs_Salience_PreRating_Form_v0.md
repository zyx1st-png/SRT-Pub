---
id: SRT-D-VALUE-VS-SALIENCE-PRERATING-FORM-V0-2026-04-27
type: pre_rating_form_template
tags:
  - SRT
  - Experiments
  - Pre-Rating
  - Survey-Template
  - d-value
  - Salience
  - Stimulus-Bank
  - Low-Risk
status: draft_v0
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: form_template
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Experiments/SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
  - Experiments/SRT_Pilot_Ethics_Note_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Experiment_Package_Review_v0.md
machine_summary: >
  Pre-rating form template for the d-value vs salience pilot. It provides participant-facing consent,
  instructions, item rating blocks, scale anchors, comprehension/clarity checks, skip options,
  randomization and item assignment logic, and export variables for selecting stimuli for the main pilot.
---

# SRT d-value vs Salience Pre-Rating Form v0

> **Purpose**: Convert the stimulus bank into a practical pre-rating survey template.  
> **Status**: Draft form template. Adapt to the chosen survey platform before use.  
> **Scope**: Low-risk online pre-rating for `d-value vs salience` stimuli.

---

## 0. Form goal

The pre-rating form should identify which stimulus items can be used in the main pilot.

Main selection goals:

```text
1. estimate salience for each scenario;
2. estimate d_proxy components for each scenario;
3. exclude distressing or unclear items;
4. find high-salience / low-d items;
5. find matched-salience / high-d items;
6. find low-to-moderate-salience / high-d items;
7. find neutral control items.
```

---

## 1. Recommended design

Use a **balanced subset design**.

```text
Total item pool: 45 candidate scenarios
Items per participant: 15-20 scenarios
Ratings per scenario: fixed scale set
Target item ratings: at least 25-30 participants per item; ideally 40+
Target sample: N = 80-150 participants
```

Reason:

> Asking every participant to rate all 45 items on all dimensions would create fatigue and lower data quality.

---

## 2. Page structure

Recommended form pages:

```text
Page 1: Consent
Page 2: General instructions
Page 3-N: Scenario rating blocks
Final page: Debrief
```

Optional:

```text
Demographics page, broad and minimal only if needed.
```

---

## 3. Page 1 — Consent text

Participant-facing draft:

```text
You are invited to participate in a short research-style study about how people rate brief everyday scenarios.

You will read short hypothetical scenarios and answer questions about how noticeable, relevant, replaceable, or personally meaningful they feel.

Some scenarios may involve mild obligations, opportunities, or personal choices, but the study is designed to avoid highly distressing material.

Your participation is voluntary. You may skip any question or stop at any time without penalty.

This study is not a clinical, diagnostic, or therapeutic assessment.

Please do not include personally identifying information in any open-text response.

By continuing, you confirm that you understand the instructions and agree to participate voluntarily.
```

Required button:

```text
[ I agree to participate ]
[ I do not agree ]
```

---

## 4. Page 2 — General instructions

Participant-facing draft:

```text
You will see a series of short hypothetical scenarios.

For each scenario, please answer based on your immediate impression.
There are no right or wrong answers.

Please rate the scenario itself, not whether it has happened to you personally.
Do not include private personal information in any text field.

You may choose “Prefer not to answer” or skip if a scenario feels uncomfortable or unclear.
```

---

## 5. Scenario rating block template

For each assigned scenario:

```text
Scenario <item_id>:
<scenario text>
```

Then ask the rating items below.

### 5.1 Clarity / comprehension

```text
How clear and understandable is this scenario?
1 = not clear at all
2 = mostly unclear
3 = somewhat unclear
4 = neutral / unsure
5 = somewhat clear
6 = mostly clear
7 = very clear
Prefer not to answer
```

### 5.2 Salience

```text
How much does this scenario stand out or catch your attention?
1 = not at all
2 = very slightly
3 = slightly
4 = moderately
5 = noticeably
6 = strongly
7 = extremely
Prefer not to answer
```

### 5.3 Arousal

```text
How emotionally activating is this scenario?
1 = not activating at all
2 = very slightly activating
3 = slightly activating
4 = moderately activating
5 = noticeably activating
6 = strongly activating
7 = extremely activating
Prefer not to answer
```

### 5.4 Preference / valence

```text
How positive or negative does this scenario feel to you?
-3 = very negative
-2 = negative
-1 = slightly negative
0 = neutral
+1 = slightly positive
+2 = positive
+3 = very positive
Prefer not to answer
```

### 5.5 Personal relevance

```text
How personally relevant does this scenario feel?
1 = not relevant at all
2 = very slightly relevant
3 = slightly relevant
4 = moderately relevant
5 = noticeably relevant
6 = strongly relevant
7 = extremely relevant
Prefer not to answer
```

### 5.6 Future impact

```text
How much could this kind of scenario affect someone's future options?
1 = no effect on future options
2 = very small effect
3 = small effect
4 = moderate effect
5 = noticeable effect
6 = strong effect
7 = very strong effect
Prefer not to answer
```

### 5.7 Non-substitutability

```text
How hard would it be to replace what is at stake in this scenario without losing what mattered?
1 = very easy to replace
2 = easy to replace
3 = somewhat easy to replace
4 = unsure / neutral
5 = somewhat hard to replace
6 = hard to replace
7 = impossible or nearly impossible to replace
Prefer not to answer
```

### 5.8 Cost-bearing

```text
How much time or effort would someone reasonably be willing to spend to preserve, repair, or avoid losing what is at stake?
1 = none
2 = very little
3 = a little
4 = a moderate amount
5 = a noticeable amount
6 = a lot
7 = a great deal
Prefer not to answer
```

### 5.9 Identity relevance

```text
How much does this scenario relate to who someone is or wants to be?
1 = not related at all
2 = very slightly related
3 = slightly related
4 = moderately related
5 = noticeably related
6 = strongly related
7 = extremely related
Prefer not to answer
```

### 5.10 Obligation weight

```text
How much does this scenario involve responsibility, obligation, or keeping faith with someone or something?
1 = not at all
2 = very slightly
3 = slightly
4 = moderately
5 = noticeably
6 = strongly
7 = extremely
Prefer not to answer
```

### 5.11 Distress risk

```text
How uncomfortable or distressing is this scenario?
1 = not distressing at all
2 = very slightly distressing
3 = slightly distressing
4 = moderately distressing
5 = noticeably distressing
6 = strongly distressing
7 = extremely distressing
Prefer not to answer
```

---

## 6. Optional comprehension check

Do not require open text for every item.

Recommended:

```text
For 3 randomly selected scenarios, ask a short comprehension question.
```

Question:

```text
In a few words, what is the scenario about?
Please do not include personal information.
```

Alternative low-burden option:

```text
I understood what happened in this scenario.
1 = strongly disagree ... 7 = strongly agree
```

---

## 7. Randomization / assignment logic

Recommended balanced assignment:

```text
Each participant rates 15-20 items.
Each participant receives items from all major categories A-D.
Category E items should be optional or limited.
Each item should receive roughly equal rating counts.
Item order randomized per participant.
```

Suggested per-participant allocation for 20 items:

```text
5 Category A items
5 Category B items
5 Category C items
5 Category D items
0-2 Category E items only if needed
```

If using 15 items:

```text
4 Category A
4 Category B
4 Category C
3 Category D
0-1 Category E
```

---

## 8. Export variable names

Use consistent variable names.

| Variable | Meaning |
|---|---|
| participant_id | anonymous participant identifier |
| item_id | stimulus ID, e.g. A01 |
| item_category | A/B/C/D/E |
| item_text | scenario text |
| clarity | clarity rating 1-7 |
| salience | salience rating 1-7 |
| arousal | arousal rating 1-7 |
| valence | preference / positivity rating -3 to +3 |
| personal_relevance | personal relevance 1-7 |
| future_impact | future impact 1-7 |
| non_substitutability | non-substitutability 1-7 |
| cost_bearing | cost-bearing 1-7 |
| identity_relevance | identity relevance 1-7 |
| obligation_weight | obligation/responsibility 1-7 |
| distress_risk | distress rating 1-7 |
| skip_flag | whether participant skipped |
| comprehension_text | optional text answer |
| completion_time | participant completion time |
| item_order | item order shown to participant |

Derived variable:

```text
d_proxy = mean(personal_relevance, future_impact, non_substitutability, cost_bearing, identity_relevance, obligation_weight)
```

---

## 9. Item inclusion thresholds after pre-rating

Preferred thresholds:

```text
clarity mean >= 5.0
comprehension failure <= 20%
distress_risk mean <= 3.5 preferred; >5.0 excluded
sufficient variance in salience and d_proxy
no severe salience/d_proxy collinearity
```

Category assignment after pre-rating:

```text
A = high salience, low d_proxy, low distress, clear
B = moderate/high salience, high d_proxy, low distress, clear
C = low/moderate salience, high d_proxy, low distress, clear
D = low salience, low d_proxy, low distress, clear
E = high salience and high d_proxy; reserve for later or secondary analysis
```

---

## 10. Attention check

Use one low-pressure attention check.

Example:

```text
Attention check: To show that you are reading the questions, please select “moderately” for this item.
```

Do not embed attention checks inside emotionally sensitive scenarios.

---

## 11. Final debrief page

Participant-facing draft:

```text
Thank you for participating.

This study examines whether scenarios that feel personally meaningful or hard to replace are rated differently from scenarios that are mainly attention-catching.

The study is part of an early-stage research program on attention, memory, concern, and future relevance.

This is not a clinical or diagnostic assessment.

If any scenario made you uncomfortable, you may close the study or contact the study organizer according to the platform instructions.
```

---

## 12. Platform implementation notes

This template can be adapted to:

```text
Qualtrics;
Google Forms;
Wenjuanxing / 问卷星;
Prolific + survey platform;
PsychoPy / Pavlovia;
custom web form.
```

For serious timing data, use a platform that records reaction time reliably.

For simple pre-rating, ordinary survey platforms are sufficient.

---

## 13. Chinese version note

If running with Chinese participants, create a separate Chinese version:

```text
Experiments/SRT_D_Value_vs_Salience_PreRating_Form_CN_v0.md
```

Do not directly machine-translate final stimuli without review.

Chinese version should check:

```text
义务 / 责任 wording;
不可替代性 wording;
未来选项 wording;
身份相关 wording;
情绪唤起 wording;
文化偏差;
家庭义务过强导致 moral weight 与 d_proxy 混淆.
```

---

## 14. Minimal go condition

This pre-rating form is ready to implement when:

```text
[ ] final item list selected from stimulus bank;
[ ] participant item count set to 15-20;
[ ] consent text added;
[ ] skip option added;
[ ] all variable names fixed;
[ ] distress-risk rating included;
[ ] clarity/comprehension check included;
[ ] debrief page included;
[ ] export format tested.
```

---

## 15. Minimal conclusion

The pre-rating form should answer one practical question:

```text
Which scenarios have the rating profile needed to test d_proxy against salience?
```

It does not test SRT directly. It prepares the item set for the main pilot.
