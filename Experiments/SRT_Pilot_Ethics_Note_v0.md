---
id: SRT-PILOT-ETHICS-NOTE-V0-2026-04-27
type: ethics_note
tags:
  - SRT
  - Experiments
  - Ethics
  - Pilot
  - Low-Risk
  - Consent
  - Distress-Protection
  - Data-Privacy
  - Online-Study
status: draft_v0
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: ethics_note
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Experiments/SRT_Pilot_Cards_v1.md
  - Experiments/SRT_D_Value_vs_Salience_Stimulus_Bank_v0.md
  - Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
machine_summary: >
  Draft ethics note for low-risk SRT online pilot studies, especially the d-value vs salience pilot.
  It defines stimulus exclusion rules, participant consent, withdrawal rights, skip options, distress
  minimization, anonymous data handling, non-clinical framing, debriefing language, and review requirements.
  It is not a substitute for formal IRB or local ethics approval.
---

# SRT Pilot Ethics Note v0

> **Purpose**: Keep early SRT pilot studies low-risk, reviewable, and ethically disciplined.  
> **Status**: Draft ethics note. Not a substitute for formal IRB / institutional ethics approval.  
> **Scope**: Low-risk online behavioral pilots, especially `d-value vs salience`.

---

## 0. Core ethics position

The first SRT pilots should be deliberately modest.

They should not attempt to induce trauma, grief, shame, fear, political conflict, or clinical distress.

Core rule:

```text
Use mild everyday scenarios first.
Do not test high-intensity existential stakes before low-risk proxies are validated.
```

---

## 1. Study risk level

Intended risk level:

```text
minimal risk / low-risk online survey-style study
```

The study should use:

```text
short hypothetical scenarios;
ordinary decision / memory / rating tasks;
no deception beyond incidental memory structure if approved;
no personally identifying data unless necessary;
no clinical diagnosis;
no vulnerable-population targeting.
```

---

## 2. Stimulus exclusion rules

Exclude or rewrite stimuli involving:

```text
explicit trauma;
bereavement;
serious medical crisis;
self-harm;
suicide;
sexual content;
abuse;
violent threat;
severe financial ruin;
political identity attack;
religious identity attack;
race / ethnicity / gender identity targeting;
criminal accusation;
public humiliation;
child harm;
family death;
major irreversible loss.
```

For the first pilot, avoid even moderately distressing versions of these themes.

---

## 3. Distress risk threshold

Every item should be pre-rated for distress risk.

Exclusion rule:

```text
Exclude items with mean distress_risk > 5.0 on a 1-7 scale.
Prefer mean distress_risk <= 3.5 for the first pilot.
Review any item with high variance in distress ratings.
```

If an item is theoretically useful but distressing, it should be moved to a later, separately reviewed study.

---

## 4. Participant consent language v0

Draft consent text:

```text
You are invited to participate in a short research-style study about how people rate and remember everyday scenarios.
You will read brief hypothetical scenarios and answer questions about how noticeable, relevant, replaceable, or personally meaningful they feel.
Some scenarios may involve mild obligations, opportunities, or personal choices, but the study is designed to avoid highly distressing material.
Your participation is voluntary. You may skip any question or stop at any time without penalty.
This study is not a clinical, diagnostic, or therapeutic assessment.
Please do not include personally identifying information in open-text responses.
```

---

## 5. Withdrawal and skip rights

Participant-facing rule:

```text
Participants may skip any scenario or question.
Participants may stop the study at any time.
Skipping should not reduce compensation if the platform permits fair compensation.
```

Implementation requirement:

```text
Add “Prefer not to answer / skip” where feasible.
Avoid forced open-text responses.
Use optional text fields when possible.
```

---

## 6. Data minimization

Collect only data needed for the pilot.

Recommended:

```text
anonymous participant ID;
ratings;
reaction time if platform supports it;
basic demographic variables only if necessary;
no names;
no phone numbers;
no email addresses;
no precise location;
no open-ended personal disclosures requested.
```

If demographics are collected, keep them broad and optional.

---

## 7. Open-text response guardrail

If open-text recall is used, include:

```text
Please summarize the scenario in general terms. Do not include personal identifying information or private life details.
```

Avoid prompts that ask participants to describe their own trauma, grief, medical history, family conflict, or political identity.

---

## 8. Incidental memory task ethics

If the study includes an incidental memory task, avoid misleading participants in a harmful way.

Safer wording:

```text
You will read and rate several short scenarios. Later, we may ask what you remember from the study.
```

Avoid claiming there will be no memory task if one is planned.

---

## 9. Debrief language v0

Draft debrief:

```text
Thank you for participating. This study examines whether scenarios that feel personally meaningful or hard to replace are remembered or evaluated differently from scenarios that are merely attention-catching.
The study is part of an early-stage theoretical research program on selection, concern, and future relevance.
It is not a clinical or diagnostic assessment.
If any scenario made you uncomfortable, you may close the study or contact the study organizer according to the platform instructions.
```

---

## 10. Compensation and fairness

If using a paid platform:

```text
estimate completion time honestly;
pay fairly for time;
do not penalize reasonable skipping;
do not reject participants solely for skipping a small number of items;
use attention checks sparingly and clearly.
```

---

## 11. Attention checks

Use low-pressure checks.

Acceptable:

```text
For this item, please select “Somewhat agree.”
```

Avoid:

```text
humiliating checks;
trick questions tied to distressing content;
checks that punish language/culture differences unfairly.
```

---

## 12. Cultural and language review

Before running the pilot, review items for:

```text
local cultural assumptions;
class / education bias;
family-role assumptions;
religious / political overtones;
translation ambiguity;
idioms that may not travel across cultures.
```

If running in Chinese, create a separate Chinese stimulus version rather than directly machine-translating the English set.

---

## 13. Special populations

Do not target vulnerable populations in the first pilot.

Avoid recruiting specifically from:

```text
minors;
patients;
people currently in crisis;
grief / trauma support communities;
clinical populations;
institutionally dependent groups;
employees under direct authority of the researcher.
```

If such populations become relevant later, use formal ethics review.

---

## 14. Data storage and sharing

Recommended practices:

```text
store anonymized data only;
separate consent logs from response data if identifiers are used;
remove open-text personal identifiers before analysis;
share only de-identified aggregate data;
document exclusion criteria before analysis;
do not publish raw text that could identify participants.
```

---

## 15. Non-clinical framing

Do not frame the pilot as measuring:

```text
mental health;
trauma;
personality disorder;
clinical anxiety;
moral worth;
consciousness level;
life value;
true personal identity.
```

Use instead:

```text
ratings of hypothetical everyday scenarios;
attention and memory;
replaceability;
future relevance;
subjective meaningfulness.
```

---

## 16. Ethics checklist before running

```text
[ ] All items screened for distress risk.
[ ] No trauma / bereavement / self-harm / explicit medical crisis stimuli.
[ ] Consent text included.
[ ] Skip / withdrawal option included.
[ ] No personally identifying data requested.
[ ] Open-text fields warn against personal disclosure.
[ ] Debrief included.
[ ] Compensation fair if paid platform is used.
[ ] Exclusion criteria documented before analysis.
[ ] Study clearly marked non-clinical and non-diagnostic.
[ ] Local IRB / ethics requirements checked if applicable.
```

---

## 17. What requires separate review

Separate ethics review is needed before studies involving:

```text
trauma reminders;
grief / bereavement;
shame induction;
pain induction;
political or religious identity threat;
clinical populations;
minors;
patients;
institutional dependence;
highly personal autobiographical recall;
longitudinal tracking with identifiers;
biometric or physiological recording.
```

---

## 18. Minimal conclusion

Early SRT pilots should test construct separation, not existential intensity.

The safest first goal is:

```text
Can low-risk d_proxy items predict memory, substitution resistance,
cost-bearing, or future reweighting beyond salience?
```

That question can be studied without exposing participants to high-risk existential material.
