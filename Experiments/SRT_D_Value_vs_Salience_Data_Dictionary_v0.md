---
id: SRT-D-VALUE-VS-SALIENCE-DATA-DICTIONARY-V0-2026-04-27
type: data_dictionary
tags:
  - SRT
  - Experiments
  - Data-Dictionary
  - d-value
  - Salience
  - Pre-Rating
  - Analysis-Input
  - d_proxy
  - Missing-Data
status: draft_v0
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: data_dictionary
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Experiments/SRT_D_Value_vs_Salience_PreRating_Form_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Experiment_Package_Review_v0.md
machine_summary: >
  Data dictionary for the d-value vs salience pre-rating and pilot workflow. It defines raw survey
  export variables, cleaned variables, missing-data rules, exclusion flags, derived variables including
  d_proxy, item-level summaries, participant-level summaries, analysis-ready long format, and handoff
  requirements for the analysis plan.
---

# SRT d-value vs Salience Data Dictionary v0

> **Purpose**: Define how pre-rating survey data should be exported, cleaned, transformed, and handed to the analysis plan.  
> **Status**: Draft v0. Adapt to the actual survey platform before use.  
> **Scope**: `d-value vs salience` pre-rating and later main-pilot data structure.

---

## 0. Core principle

The data structure should preserve three levels:

```text
participant-level data;
item-level data;
participant × item rating data.
```

Recommended analysis format:

```text
long format: one row = one participant's rating of one item.
```

---

## 1. Required files after export

Minimum recommended exports:

```text
raw_survey_export.csv
cleaned_long_ratings.csv
item_summary_prerating.csv
participant_quality_flags.csv
analysis_ready_long.csv
```

Optional later:

```text
stimulus_selected_for_main_pilot.csv
main_pilot_analysis_ready_long.csv
```

---

## 2. Raw survey export fields

These are expected from the pre-rating form.

| Raw variable | Type | Required | Description |
|---|---:|---:|---|
| participant_id | string | yes | anonymous participant identifier |
| session_id | string | optional | platform session identifier, if available |
| start_time | datetime | optional | survey start time |
| end_time | datetime | optional | survey end time |
| completion_time_sec | numeric | yes | total survey time in seconds |
| item_order | integer | yes | order in which item was displayed |
| item_id | string | yes | stimulus ID, e.g. A01, B03 |
| item_category_initial | string | yes | category from stimulus bank A/B/C/D/E before pre-rating |
| item_text | string | yes | exact scenario text shown |
| clarity_raw | numeric/string | yes | clarity rating or skip value |
| salience_raw | numeric/string | yes | salience rating or skip value |
| arousal_raw | numeric/string | yes | arousal rating or skip value |
| valence_raw | numeric/string | yes | -3 to +3 valence or skip value |
| personal_relevance_raw | numeric/string | yes | personal relevance or skip value |
| future_impact_raw | numeric/string | yes | future impact or skip value |
| non_substitutability_raw | numeric/string | yes | non-substitutability or skip value |
| cost_bearing_raw | numeric/string | yes | willingness to bear cost or skip value |
| identity_relevance_raw | numeric/string | yes | identity relevance or skip value |
| obligation_weight_raw | numeric/string | yes | obligation / responsibility or skip value |
| distress_risk_raw | numeric/string | yes | distress rating or skip value |
| comprehension_text | string | optional | short text response for sampled items |
| attention_check | numeric/string | optional | attention check response |
| skip_flag_raw | boolean/string | yes | whether participant skipped an item |
| platform | string | optional | survey platform name |

---

## 3. Cleaned rating variables

Convert raw values into standardized variables.

| Clean variable | Type | Range | Missing code | Description |
|---|---:|---:|---:|---|
| clarity | numeric | 1-7 | NA | scenario clarity |
| salience | numeric | 1-7 | NA | attention / noticeability |
| arousal | numeric | 1-7 | NA | emotional activation |
| valence | numeric | -3 to +3 | NA | negative to positive feeling |
| personal_relevance | numeric | 1-7 | NA | subjective personal relevance |
| future_impact | numeric | 1-7 | NA | impact on future options |
| non_substitutability | numeric | 1-7 | NA | replacement resistance |
| cost_bearing | numeric | 1-7 | NA | willingness to spend time / effort |
| identity_relevance | numeric | 1-7 | NA | relation to who one is / wants to be |
| obligation_weight | numeric | 1-7 | NA | responsibility / obligation weight |
| distress_risk | numeric | 1-7 | NA | discomfort or distress |
| skip_flag | boolean | TRUE/FALSE | FALSE default | item skipped or prefer not to answer |

Rule:

```text
Convert “Prefer not to answer”, blank, skipped, or invalid values to NA and set skip_flag = TRUE where appropriate.
```

---

## 4. Derived variables

### 4.1 d_proxy

Primary operational proxy candidate:

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

Missing-data rule:

```text
Compute d_proxy only if at least 4 of 6 components are non-missing.
Otherwise set d_proxy = NA.
```

### 4.2 d_proxy_core

Stricter non-substitutability / future-selectability proxy:

```text
d_proxy_core = mean(
  future_impact,
  non_substitutability,
  cost_bearing,
  identity_relevance
)
```

Missing-data rule:

```text
Compute only if at least 3 of 4 components are non-missing.
```

### 4.3 moral_component

To check whether `d_proxy` collapses into obligation / moral intensity:

```text
moral_component = obligation_weight
```

### 4.4 salience_arousal_composite

Optional baseline composite:

```text
salience_arousal = mean(salience, arousal)
```

Compute only if both are available, or with one missing if documented.

### 4.5 absolute_valence

Preference / affective intensity regardless of positive or negative direction:

```text
absolute_valence = abs(valence)
```

### 4.6 quality flags

| Flag | Definition |
|---|---|
| item_low_clarity_flag | item-level mean clarity < 5.0 |
| item_high_distress_flag | item-level mean distress_risk > 5.0 |
| item_preferred_distress_flag | item-level mean distress_risk > 3.5 |
| participant_fast_flag | completion_time_sec below minimum threshold |
| participant_straightline_flag | low variance across ratings |
| participant_attention_fail_flag | failed attention check |
| item_high_missing_flag | item missing rate > 20% |

---

## 5. Participant-level quality rules

Participant exclusion candidates:

```text
failed attention check;
completion time unrealistically fast;
missing more than 20% of required responses;
straight-lining across rating scales;
failed or nonsensical comprehension on more than 30% sampled items.
```

Recommended threshold placeholders:

```text
completion_time_sec < median_time * 0.33 -> review / possible exclusion;
missing_required_rate > 0.20 -> exclude;
attention_check_failed == TRUE -> exclude or sensitivity check;
straightline_sd < 0.20 across main ratings -> review.
```

Do not exclude participants after looking at hypothesis results unless the exclusion rule was pre-specified.

---

## 6. Item-level summary variables

Create one row per item.

| Variable | Type | Description |
|---|---:|---|
| item_id | string | scenario ID |
| item_category_initial | string | original category A/B/C/D/E |
| item_text | string | scenario text |
| n_ratings | integer | number of valid item ratings |
| clarity_mean | numeric | mean clarity |
| salience_mean | numeric | mean salience |
| arousal_mean | numeric | mean arousal |
| valence_mean | numeric | mean valence |
| absolute_valence_mean | numeric | mean affect intensity |
| personal_relevance_mean | numeric | mean personal relevance |
| future_impact_mean | numeric | mean future impact |
| non_substitutability_mean | numeric | mean non-substitutability |
| cost_bearing_mean | numeric | mean cost-bearing |
| identity_relevance_mean | numeric | mean identity relevance |
| obligation_weight_mean | numeric | mean obligation weight |
| distress_risk_mean | numeric | mean distress risk |
| d_proxy_mean | numeric | mean d_proxy |
| d_proxy_core_mean | numeric | mean d_proxy_core |
| missing_rate | numeric | missing / skipped proportion |
| item_keep_flag | boolean | recommended for main pilot |
| item_exclusion_reason | string | if excluded |
| item_category_final | string | A/B/C/D/E after pre-rating |

---

## 7. Final item category assignment

Use pre-rating to assign final categories.

### Category A — high salience / low d_proxy

Suggested rule:

```text
salience_mean >= sample median or upper tertile;
d_proxy_mean <= sample median or lower tertile;
clarity_mean >= 5.0;
distress_risk_mean <= 3.5 preferred.
```

### Category B — matched salience / high d_proxy

Suggested rule:

```text
salience_mean overlaps Category A range;
d_proxy_mean >= upper tertile;
clarity_mean >= 5.0;
distress_risk_mean <= 3.5 preferred.
```

### Category C — low-to-moderate salience / high d_proxy

Suggested rule:

```text
salience_mean <= median or moderate range;
d_proxy_mean >= upper tertile;
clarity_mean >= 5.0;
distress_risk_mean <= 3.5 preferred.
```

### Category D — low salience / low d_proxy controls

Suggested rule:

```text
salience_mean <= lower tertile;
d_proxy_mean <= lower tertile;
clarity_mean >= 5.0;
distress_risk_mean <= 3.5 preferred.
```

### Category E — high salience / high d_proxy

Suggested rule:

```text
salience_mean >= upper tertile;
d_proxy_mean >= upper tertile;
reserve for secondary or later use.
```

---

## 8. Analysis-ready long format

Final long-format file should include:

```text
participant_id
item_id
item_order
item_category_initial
item_category_final
clarity
salience
arousal
valence
absolute_valence
personal_relevance
future_impact
non_substitutability
cost_bearing
identity_relevance
obligation_weight
distress_risk
d_proxy
d_proxy_core
moral_component
salience_arousal
skip_flag
participant_quality_flags
item_quality_flags
```

For main pilot, add outcomes:

```text
recall_binary
recall_detail
recognition_accuracy
substitution_resistance
future_reweighting
rt_ms
confidence
```

---

## 9. Missing-data handling

### 9.1 Rating-level missingness

Use `NA` for:

```text
Prefer not to answer;
skipped item;
blank response;
invalid value outside range.
```

### 9.2 Derived variable missingness

```text
d_proxy requires at least 4 of 6 components;
d_proxy_core requires at least 3 of 4 components;
salience_arousal requires at least salience or arousal, but report rule clearly.
```

### 9.3 Item exclusion due to missingness

Exclude or review items if:

```text
missing_rate > 20%;
clarity_mean < 5.0;
comprehension failure > 20%;
distress_risk_mean > 5.0.
```

---

## 10. Primary handoff to analysis plan

The analysis plan expects:

```text
analysis_ready_long.csv
item_summary_prerating.csv
participant_quality_flags.csv
```

Main model from analysis plan:

```text
Outcome ~ d_proxy + Salience + Arousal + Preference + Confidence +
          (1 | Participant) + (1 | Item)
```

Pre-rating does not yet test this model fully unless outcome variables are included.

Pre-rating mainly supports:

```text
item selection;
construct separation;
distress / clarity filtering;
salience-d_proxy correlation inspection;
category assignment.
```

---

## 11. Pre-rating summary report template

After pre-rating, report:

```text
1. sample size and item rating counts;
2. participant exclusion summary;
3. item exclusion summary;
4. descriptive statistics for each rating dimension;
5. correlation matrix: salience, arousal, valence, d_proxy, distress;
6. item category reassignment;
7. selected items for main pilot;
8. items needing rewrite;
9. decision: proceed / revise / stop.
```

---

## 12. Red flags after pre-rating

Stop or revise if:

```text
salience and d_proxy correlate too strongly to separate;
most high-d items are also high distress;
participants do not understand many scenarios;
obligation_weight alone drives d_proxy;
identity relevance alone drives d_proxy;
items are culturally unclear;
neutral controls are not actually neutral;
Category B cannot be matched with Category A on salience.
```

---

## 13. Minimal go condition for main pilot

Proceed only if pre-rating yields:

```text
at least 8-10 usable Category A items;
at least 8-10 usable Category B items;
at least 8-10 usable Category C items;
at least 8 usable Category D controls;
clarity_mean >= 5.0 for selected items;
distress_risk_mean <= 3.5 preferred for selected items;
reasonable salience matching for A vs B;
clear d_proxy separation for A vs B/C;
no single d_proxy component fully drives the pattern.
```

---

## 14. Minimal conclusion

This data dictionary connects the form template to the analysis plan.

The key implementation rule is:

```text
Do not run the main pilot until pre-rating produces a clean selected item set.
```
