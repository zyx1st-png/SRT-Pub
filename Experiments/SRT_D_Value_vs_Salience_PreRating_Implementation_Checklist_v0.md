---
id: SRT-D-VALUE-VS-SALIENCE-PRERATING-IMPLEMENTATION-CHECKLIST-V0-2026-04-27
type: implementation_checklist
tags:
  - SRT
  - Experiments
  - Pre-Rating
  - Implementation
  - Checklist
  - Survey-Platform
  - d-value
  - Salience
  - Data-Export
status: draft_v0
layer: empirical_bridge
epistemic_layer: experimental_implementation
claim_mode: checklist
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Experiments/SRT_D_Value_vs_Salience_PreRating_Form_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Data_Dictionary_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
  - Experiments/SRT_Pilot_Ethics_Note_v0.md
machine_summary: >
  Narrow implementation checklist for building the d-value vs salience pre-rating form in an actual survey
  platform. It checks consent, item assignment, randomization, participant burden, skip options, scale anchors,
  export variables, sample CSV compatibility with the data dictionary, and go/no-go criteria before launching
  pre-rating. It does not authorize main pilot data collection.
---

# SRT d-value vs Salience Pre-Rating Implementation Checklist v0

> **Purpose**: Check the actual survey-platform implementation before collecting pre-rating data.  
> **Status**: Draft implementation checklist.  
> **Scope**: Pre-rating only. This does **not** authorize main pilot data collection.

---

## 0. Implementation verdict rule

The pre-rating form can launch only if all critical checks pass.

Critical rule:

```text
No main pilot materials should be created or launched until pre-rating data are collected,
cleaned, and used to select / trim the item set.
```

---

## 1. Platform setup

Record platform:

```text
Platform:
Form URL:
Builder / owner:
Date built:
Version:
```

Supported platforms:

```text
Qualtrics;
Google Forms;
Wenjuanxing / 问卷星;
Prolific + survey platform;
PsychoPy / Pavlovia;
custom web form.
```

Checklist:

```text
[ ] Platform can randomize item order or item blocks.
[ ] Platform can assign item subsets or support multiple form versions.
[ ] Platform can export CSV.
[ ] Platform supports skip / prefer-not-to-answer options.
[ ] Platform records completion time or equivalent.
[ ] Platform can preserve item_id in export.
```

---

## 2. Consent page check

Required elements:

```text
[ ] Study described as rating brief everyday hypothetical scenarios.
[ ] Voluntary participation stated.
[ ] Skip rights stated.
[ ] Withdrawal rights stated.
[ ] Non-clinical / non-diagnostic statement included.
[ ] No personal identifying information requested.
[ ] Open-text privacy warning included if open text exists.
[ ] Continue / do-not-agree option included.
```

Do not launch if consent is missing.

---

## 3. Instructions page check

Required elements:

```text
[ ] Participants told there are no right or wrong answers.
[ ] Participants told to rate the scenario, not disclose personal experiences.
[ ] Participants told they may skip uncomfortable or unclear scenarios.
[ ] Participants told scenarios are hypothetical.
[ ] Instructions are short enough to read comfortably.
```

---

## 4. Item assignment check

Recommended design:

```text
15-20 scenarios per participant;
balanced representation from A/B/C/D categories;
Category E optional or limited;
item order randomized;
each item should eventually receive at least 25-30 ratings, ideally 40+.
```

Checklist:

```text
[ ] Participants see no more than 20 scenarios.
[ ] Each participant receives A/B/C/D items.
[ ] Category E is absent or limited.
[ ] Item order is randomized.
[ ] Each scenario includes visible or hidden item_id.
[ ] Each scenario text matches stimulus bank exactly or changes are documented.
```

If using multiple fixed form versions:

```text
[ ] Version A/B/C/D assignment is documented.
[ ] Item balance table exists.
[ ] Each item appears in roughly equal number of versions.
```

---

## 5. Scenario block check

For each scenario block, confirm these fields exist:

```text
[ ] item_id stored.
[ ] item_category_initial stored.
[ ] item_text stored or reconstructable from item_id.
[ ] clarity rating present.
[ ] salience rating present.
[ ] arousal rating present.
[ ] valence rating present.
[ ] personal_relevance rating present.
[ ] future_impact rating present.
[ ] non_substitutability rating present.
[ ] cost_bearing rating present.
[ ] identity_relevance rating present.
[ ] obligation_weight rating present.
[ ] distress_risk rating present.
[ ] skip / prefer not to answer option present.
```

---

## 6. Scale anchor check

All 1-7 scales should preserve direction:

```text
1 = low / none
7 = high / extreme
```

Valence should preserve:

```text
-3 = very negative
0 = neutral
+3 = very positive
```

Checklist:

```text
[ ] No scale is accidentally reversed.
[ ] All scales use consistent anchors.
[ ] Prefer-not-to-answer is not coded as a numeric value.
[ ] Skip values export as blank, NA, or explicit text that can be recoded.
```

---

## 7. Comprehension / clarity check

Required minimum:

```text
[ ] Clarity rating included for every item.
```

Recommended:

```text
[ ] 3 random items include short comprehension text.
[ ] Open-text prompt says not to include personal information.
```

If open text is not feasible:

```text
[ ] Use “I understood this scenario” rating instead.
```

---

## 8. Attention check

Checklist:

```text
[ ] At least one low-pressure attention check included.
[ ] Attention check is not embedded in emotionally sensitive item.
[ ] Attention check is simple and fair.
[ ] Failure rule is documented before launch.
```

Recommended failure handling:

```text
attention_check_failed = TRUE;
exclude in primary cleaning or run sensitivity check.
```

---

## 9. Participant burden check

Before launch, test the form with 2-3 internal reviewers.

Record:

```text
Reviewer 1 completion time:
Reviewer 2 completion time:
Reviewer 3 completion time:
Average completion time:
```

Launch only if:

```text
[ ] Average completion time is reasonable.
[ ] Reviewers report no confusing repeated wording.
[ ] Reviewers do not experience item fatigue.
[ ] Rating blocks display cleanly on desktop and mobile.
```

---

## 10. Distress and content safety check

Checklist:

```text
[ ] No trauma / bereavement / self-harm / explicit medical crisis items.
[ ] No political or religious identity attack items.
[ ] No race / ethnicity / gender identity targeting.
[ ] No sexual content or abuse content.
[ ] No severe financial ruin or public humiliation stimuli.
[ ] Distress risk is collected for every item.
```

If an internal reviewer flags an item as distressing:

```text
[ ] Rewrite or remove before launch.
```

---

## 11. Export variable check

Run a test export with fake responses.

Confirm exported fields include:

```text
[ ] participant_id
[ ] completion_time_sec or timestamp fields
[ ] item_order
[ ] item_id
[ ] item_category_initial
[ ] clarity
[ ] salience
[ ] arousal
[ ] valence
[ ] personal_relevance
[ ] future_impact
[ ] non_substitutability
[ ] cost_bearing
[ ] identity_relevance
[ ] obligation_weight
[ ] distress_risk
[ ] skip_flag or skip values
[ ] attention_check
[ ] comprehension_text if used
```

Export file name:

```text
raw_survey_export_test.csv
```

---

## 12. Data dictionary compatibility check

Compare the test export to:

```text
Experiments/SRT_D_Value_vs_Salience_Data_Dictionary_v0.md
```

Checklist:

```text
[ ] Every required raw field can be mapped to a data dictionary variable.
[ ] Prefer-not-to-answer responses can be recoded to NA.
[ ] item_id survives export.
[ ] item_order survives export.
[ ] all ratings can be parsed as numeric after cleaning.
[ ] valence exports correctly as -3 to +3 or can be recoded cleanly.
[ ] d_proxy can be computed from exported fields.
[ ] participant quality flags can be computed.
[ ] item-level summaries can be generated.
```

Do not launch if item_id or core rating variables are not exported cleanly.

---

## 13. Minimal sample CSV row schema

The export must be convertible into this long format:

```csv
participant_id,item_id,item_order,item_category_initial,clarity,salience,arousal,valence,personal_relevance,future_impact,non_substitutability,cost_bearing,identity_relevance,obligation_weight,distress_risk,skip_flag,attention_check,completion_time_sec
P001,A01,1,A,6,5,3,1,2,2,1,1,1,1,1,FALSE,pass,480
P001,B03,2,B,6,4,4,0,5,5,6,5,5,6,2,FALSE,pass,480
```

If the platform exports wide format, document the transformation to long format.

---

## 14. Pre-launch go / no-go

### Launch pre-rating only if:

```text
[ ] Consent and debrief are present.
[ ] Skip / withdrawal rights are present.
[ ] Participant sees no more than 20 scenarios.
[ ] Distress-risk rating is included.
[ ] item_id exports correctly.
[ ] Test export maps to Data Dictionary v0.
[ ] Internal reviewers report acceptable burden.
[ ] No high-risk stimuli remain.
```

### Do not launch if:

```text
[ ] item_id is lost in export.
[ ] Prefer-not-to-answer is coded as a valid numeric rating.
[ ] Scale direction is inconsistent.
[ ] Participants must answer all items without skip option.
[ ] Completion time is too long.
[ ] Any high-risk content remains.
```

---

## 15. Post-launch pre-rating review

After collecting pre-rating data, produce a short review:

```text
N participants;
item rating counts;
participant exclusions;
item exclusions;
distress-risk distribution;
clarity distribution;
salience-d_proxy correlation;
selected Category A/B/C/D items;
items needing rewrite;
go/no-go for main pilot.
```

Suggested future file:

```text
Experiments/SRT_D_Value_vs_Salience_PreRating_Results_Review_v0.md
```

Do not create this file until actual pre-rating data exist.

---

## 16. Minimal conclusion

This checklist exists to prevent a common failure:

```text
a good theoretical design becoming unusable because the survey export cannot support the analysis.
```

The most important implementation check is:

```text
Can the exported test CSV be transformed into analysis_ready_long.csv according to Data Dictionary v0?
```
