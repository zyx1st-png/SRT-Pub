---
id: HOOK-PHIL-PH-ETH01-MORAL-STATUS-ATTRIBUTION-RECOGNITION
patch_id: PATCH-PHIL-PH-ETH01-MORAL-STATUS-ATTRIBUTION-RECOGNITION-SEPARATION
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: philosophy_ethics_moral_psychology_ai_welfare
status: active
integration_status: pending
landing_ledger:
  - target: "Philosophy/SRT_Ethics_PH_SS_Guardrails.md"
    state: pending
    blocked_by: "Add recognition/attribution typing only in a dedicated ethics hardening pass; do not redefine moral legitimacy or create a new moral scalar from survey judgments."
  - target: "Philosophy/SRT_Ethics_Casebook.md"
    state: pending
    blocked_by: "Case-template wording should distinguish actual affected subjects from entities receiving moral consideration/recognition without implying that public attribution settles patienthood."
  - target: "Philosophy/SRT_Subjecthood_Threshold_Interface.md"
    state: pending
    blocked_by: "Preserve bearer-unit-first and S0-S6 ownership; add only the guard that moral-status attribution is not subjecthood evidence and subjecthood is not an exhaustive policy rule."
  - target: "AI/Consciousness_Annex/02_Report_Reality_Moral_Status_Interface.md"
    state: pending
    blocked_by: "Future AI welfare pass may separate ontology assessment, precautionary governance and public/institutional recognition; no moral-status or consciousness promotion from this survey alone."
---

# PH-ETH01 Moral-status attribution / recognition integration hook

## 1. Integration payload

Retain the following typed separation:

```text
actual target organization / stake-bearing facts
!= moral-status attribution / recognition
!= normative legitimacy
!= governance protection threshold
```

and the descriptive source-backed pressure:

```text
moral-status attribution is associated with
both target-side properties and attributor / relation / context variables
```

Do not convert this into a new SRT moral-status definition.

---

## 2. Target A — `Philosophy/SRT_Ethics_PH_SS_Guardrails.md`

### Existing strength to preserve

The guardrails already separate:

```text
moral reality
moral intensity
moral legitimacy
```

and already reject:

```text
d-value expansion -> automatic moral legitimacy
stable L2 -> automatic goodness
```

### Suggested future clarification

Add a compact recognition note only if it reduces ambiguity:

```text
Moral-status attribution is an attributor-indexed judgment and should not be confused with the target's actual subjecthood / suffering / stake profile or with the legitimacy of a norm governing that target. Recognition can be socially real as an L2 constraint while remaining fallible about both ontology and moral justification.
```

### Guard

Do not define actual moral status as social recognition.

---

## 3. Target B — `Philosophy/SRT_Ethics_Casebook.md`

### Existing pressure

The current case template asks:

```text
Who has d-value-bearing future selectability at stake?
```

This is useful for affected-subject analysis but may be misread as exhaustively defining every object of moral consideration.

### Suggested future typing

When cases involve animals, ecosystems, fetuses, AI systems, institutions or non-subject entities, distinguish:

```text
Affected subjects / stake-bearing candidates
Entities granted moral consideration or recognition
Norms / relations / environments carrying instrumental moral significance
```

The categories may overlap but should not be collapsed by template wording.

### Guard

Do not infer that every socially protected entity is a subject or bearer.

---

## 4. Target C — `Philosophy/SRT_Subjecthood_Threshold_Interface.md`

### Existing strength to preserve

The file already states:

```text
bearer-unit first;
S0-S6 second;
moral status last.
```

and distinguishes subjecthood from responsibility.

### Suggested future clarification

Near the cross-domain / ethics guardrails, add:

```text
moral-status attribution != subjecthood evidence
subjecthood evidence != automatic moral-legitimacy verdict
```

The first clause blocks recognition-to-ontology reversal. The second blocks ontology-to-policy overreach.

### Guard

Do not alter S0-S6 thresholds or create a post-S6 moral-status rung.

---

## 5. Target D — `AI/Consciousness_Annex/02_Report_Reality_Moral_Status_Interface.md`

### Existing strength to preserve

The annex already says:

```text
moral caution is not an ontology proof
moral personhood should come after consciousness criteria rather than reverse-defining them
```

### Suggested future extension

AI welfare analysis may explicitly type three decision surfaces:

```text
ontology / subjecthood evidence
precautionary welfare-governance threshold
public / institutional moral-status recognition
```

A system may receive precautionary protection under uncertainty without satisfying subjecthood criteria, and public recognition may vary with familiarity / expertise / framing without becoming ontic evidence.

### Guard

Do not use the Hirschhorn survey to infer that current LLMs are conscious, non-conscious, moral persons or rights-bearing subjects.

---

## 6. Future empirical route — optional, not landed

A future SRT-adjacent moral-recognition study could separate:

```text
Target evidence T
Attributor state A
Relation/context R
Attribution judgment J
Treatment/protection decision P
```

and ask whether:

```text
J changes under A/R manipulation while T is held fixed
```

then separately whether:

```text
J causally changes P
```

and, in real interactive systems, whether changed `P` alters target future options or consequence exposure.

No such SRT-specific result is established by the present source.

---

## 7. Do not include

Do not land any owner sentence asserting:

```text
moral status is subjective
moral status is whatever society recognizes
consciousness is irrelevant to ethics
valence is sufficient for moral standing
AI expertise reveals true AI consciousness
recognition creates subjecthood
all protected entities are bearers
all bearers must receive identical protection
```

---

## 8. Future synthesis target

Use PH-ETH01 only when a future ethics / AI-welfare hardening pass needs a clean interface among:

```text
ontology
recognition
normative legitimacy
policy / protection
```

Until then, keep this hook pending and non-canonical.
