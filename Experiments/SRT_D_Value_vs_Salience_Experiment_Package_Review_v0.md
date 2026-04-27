---
id: SRT-D-VALUE-VS-SALIENCE-EXPERIMENT-PACKAGE-REVIEW-V0-2026-04-27
type: experiment_package_review
tags:
  - SRT
  - Experiments
  - Review
  - d-value
  - Salience
  - Stimulus-Bank
  - Analysis-Plan
  - Ethics-Note
  - Pre-Rating
status: review_v0
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: review
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Experiments/SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
  - Experiments/SRT_Pilot_Ethics_Note_v0.md
  - Experiments/SRT_Pilot_Cards_v1.md
machine_summary: >
  Review of the first d-value vs salience experiment package. It checks whether the stimulus bank,
  analysis plan, and ethics note are ready to support a pre-rating form and low-risk online pilot.
  It identifies strengths, gaps, required pre-rating decisions, minimum implementation package,
  and go/no-go criteria before running the pilot.
---

# SRT d-value vs Salience Experiment Package Review v0

> **Purpose**: Review whether the first SRT experiment package is ready to move from concept design to pre-rating implementation.  
> **Status**: Review v0. This is not a preregistration and not a completed experiment.  
> **Scope**: `d-value vs salience` pilot package.

---

## 0. Reviewed files

This review covers:

```text
Experiments/SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md
Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
Experiments/SRT_Pilot_Ethics_Note_v0.md
```

Supporting files:

```text
Experiments/SRT_Pilot_Cards_v1.md
Experiments/SRT_Experimental_Roadmap_v1.md
Core/SRT_Validation_Template.md
Papers/SRT_D_Value_Ontology_of_Concern_Outline.md
```

---

## 1. Executive review

The package is strong enough to proceed to a **pre-rating form template**, but not yet strong enough to run a main pilot.

Current readiness:

```text
Conceptual distinction: ready for pre-rating
Stimulus pool: draft-ready, needs pre-rating and item trimming
Analysis plan: draft-ready, suitable for preregistration after refinement
Ethics note: low-risk guardrails present
Main pilot readiness: not yet; needs pre-rating first
```

Recommended next action:

```text
Create Experiments/SRT_D_Value_vs_Salience_PreRating_Form_v0.md
```

---

## 2. Strengths

### 2.1 Construct separation is explicit

The package clearly distinguishes:

```text
d_proxy != d-value;
d_proxy != salience;
d_proxy != arousal;
d_proxy != preference;
d_proxy != moral goodness.
```

This protects the pilot from overclaiming.

### 2.2 Stimulus categories are usable

The stimulus bank already separates:

```text
A. high salience / low d_proxy
B. matched salience / high d_proxy
C. low-to-moderate salience / high d_proxy
D. low salience / low d_proxy controls
E. high salience / high d_proxy later-use items
```

This is sufficient to begin pre-rating.

### 2.3 Analysis plan has real failure conditions

The analysis plan includes:

```text
baseline controls;
mixed-effects models;
incremental validity tests;
robustness checks;
failure conditions;
narrowing rules.
```

This makes the pilot methodologically accountable.

### 2.4 Ethics guardrails are appropriate for first pilot

The ethics note keeps the study low-risk by excluding:

```text
trauma;
bereavement;
self-harm;
serious medical crisis;
political / religious identity attack;
highly distressing personal content.
```

This is appropriate for a first online study.

---

## 3. Main gaps before pre-rating

### Gap 1 — Need exact participant-facing rating wording

The analysis plan lists dimensions, but the pre-rating form needs final exact wording for each item.

Required:

```text
one stable question per construct;
one scale anchor set per question;
clear instruction not to disclose personal information;
optional skip / prefer not to answer.
```

### Gap 2 — Need item randomization and fatigue control

The stimulus bank has 45 items. Showing all dimensions for all items may be fatiguing.

Pre-rating should choose one of two designs:

```text
Option A: each participant rates all items on fewer dimensions;
Option B: each participant rates a subset of items on all dimensions.
```

Recommended for v0:

```text
subset design: 15-20 items per participant, all dimensions.
```

### Gap 3 — Need comprehension check policy

The stimulus bank suggests comprehension screening, but the pre-rating form should decide whether comprehension is:

```text
open-text for a subset;
multiple-choice;
self-rated clarity;
or simple “I understood this scenario” rating.
```

Recommended v0:

```text
clarity rating for every item + open-text comprehension for 3 random items.
```

### Gap 4 — Need language / culture decision

The current item pool is English. If running with Chinese participants, a Chinese version should be created separately.

Do not machine-translate blindly.

### Gap 5 — Need final item-selection thresholds

Pre-rating should define thresholds for item inclusion:

```text
distress_risk <= 3.5 preferred;
comprehension / clarity >= 5.0;
salience matched where possible;
d_proxy category separation large enough;
low collinearity between salience and d_proxy desirable.
```

---

## 4. Go / no-go criteria for pre-rating

### Go for pre-rating if:

```text
consent language is included;
skip/withdrawal option is included;
items are low-risk;
ratings are clearly worded;
participant burden is reasonable;
data collection does not request identifying information.
```

### No-go for pre-rating if:

```text
items ask for personal trauma or autobiographical disclosure;
all 45 items are rated on all dimensions by every participant without fatigue control;
no skip option exists;
no distress-risk rating is collected;
no clarity / comprehension check exists.
```

---

## 5. Recommended pre-rating form structure

### Page 1 — Consent

Include:

```text
study purpose in general terms;
voluntary participation;
skip / withdraw rights;
non-clinical statement;
no personal identifying information request;
contact / organizer placeholder if needed.
```

### Page 2 — Instructions

Tell participants:

```text
You will read short hypothetical scenarios.
Please rate how each scenario feels to you.
There are no right or wrong answers.
Do not include private personal information in any text field.
```

### Page 3+ — Scenario ratings

For each item:

```text
scenario text;
clarity rating;
salience;
arousal;
preference;
personal relevance;
future impact;
non-substitutability;
cost-bearing;
identity relevance;
obligation weight;
distress risk;
skip option.
```

### Final page — Debrief

Include short debrief from ethics note.

---

## 6. Minimum viable pre-rating dataset

Minimum viable pre-rating:

```text
N = 80 participants;
each item rated by at least 25-30 participants;
each participant rates 15-20 items;
all items receive distress, salience, and d_proxy component ratings.
```

Better:

```text
N = 120-150 participants;
each item rated by 40+ participants;
balanced assignment across categories.
```

---

## 7. Main-pilot readiness criteria after pre-rating

Proceed to main pilot only if pre-rating produces:

```text
at least 8-10 usable high-salience / low-d items;
at least 8-10 usable matched-salience / high-d items;
at least 8-10 usable low-to-moderate-salience / high-d items;
at least 8 neutral controls;
acceptable distress levels;
acceptable clarity;
usable d_proxy separation;
manageable salience/d_proxy collinearity.
```

If this fails, revise stimuli before main pilot.

---

## 8. Key interpretive guardrails

Even if the pilot works, do not claim:

```text
d-value is proven;
d_proxy is identical to d-value;
SRT is confirmed;
high d_proxy means moral goodness;
high d_proxy means consciousness;
salience is irrelevant.
```

Permitted claim if results support it:

```text
In this operationalization, d_proxy predicted downstream outcomes beyond salience and related baseline variables.
```

---

## 9. Recommended next artifacts

Priority order:

```text
1. Experiments/SRT_D_Value_vs_Salience_PreRating_Form_v0.md
2. Experiments/SRT_D_Value_vs_Salience_Data_Dictionary_v0.md
3. Experiments/SRT_D_Value_vs_Salience_Preregistration_v0.md
```

Do not create main-pilot materials until pre-rating design is clear.

---

## 10. Final verdict

The experiment package is ready for a pre-rating form template.

It is not yet ready for data collection in a main pilot.

Best next step:

```text
Create the pre-rating form template and then review item burden, wording, and ethical safeguards.
```
