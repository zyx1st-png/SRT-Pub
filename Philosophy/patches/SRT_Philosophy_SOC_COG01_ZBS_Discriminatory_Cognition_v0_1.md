---
patch_id: PATCH-PHIL-SOC-COG01-ZBS-DISCRIMINATORY-COGNITION
source_ids:
  - SRC-2026-05-08-PHIL-SOC-ACTIVE-INFERENCE-DISCRIMINATORY-COGNITION
domain: philosophy_social_cognition
claim_level: bridge
canonical_status: domain_bridge_integrated
status: patch
target_document: "Philosophy/SRT_Social_Cognition.md"
related_claims:
  - social_cognition
  - discriminatory_cognition
  - dehumanization
  - zones_of_bounded_surprisal
  - active_inference
  - d_exclusion
  - collective_selection
tags:
  - active_inference
  - ZBS
  - discrimination
  - dehumanization
  - recognition
  - bystander_silence
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_patch
id: PATCH-PHIL-SOC-COG01-ZBS-DISCRIMINATORY-COGNITION
---

# SRT Philosophy Patch SOC-COG01: ZBS and Discriminatory Cognition v0.1

> Status: social cognition bridge patch.
> Canonical caution: this patch does not modify SRT primitives. ZBS is used as an external active-inference proxy for social update bandwidth.

## 0. Source anchor

Primary source:

- Hector M. Manrique, Karl J. Friston, and Michael J. Walker. (2026). "An active inference explanation of discriminatory cognition with regard to social attitudes and harmful behaviour." *BioSystems*, article 105793. DOI: `10.1016/j.biosystems.2026.105793`.

Full-text processing used the matching OSF preprint PDF because the ScienceDirect page was blocked by the publisher's anti-bot layer in local access.

---

## 1. Why this matters for SRT

SRT already has strong language for dehumanization as `d`-exclusion, recognition-channel break, hidden friction export, occlusion, and asymmetric `M(t)` consequence return. What was missing was a crisp external cognitive mechanism for why discriminatory systems can remain stable even when contrary evidence is present.

The article supplies that mechanism through active inference and zones of bounded surprisal:

```text
some social-cognitive systems can only tolerate a narrow range of contradiction before protecting identity rather than updating belief.
```

---

## 2. Main SRT bridge claim

### Claim SOC-COG01

Discriminatory cognition can be modeled as a narrowed cross-subject update gate: out-group evidence, out-group suffering, or in-group wrongdoing generates surprise, but the system handles that surprise by suppressing the signal, protecting prior identity, or changing the social environment to fit the prior.

SRT formulation:

```text
narrow ZBS_cross + high group-prior precision + attenuated out-group recognition
  -> discriminatory cognition candidate
```

Extreme case:

```text
dehumanising cognition
  -> out-group operator removed from effective d-field
  -> recognition channel breaks
  -> harm can be processed as maintenance rather than violation
```

---

## 3. Mapping table

| Source concept | SRT interpretation | Guardrail |
|---|---|---|
| narrow ZBS | low tolerance for cross-group surprise / contradiction | proxy only; not `d` |
| high prior precision | rigid group `L_2` and confirmation bias | not identical to `\Psi_f` |
| discriminatory mind | biased evidence weighting plus in-group self-evidencing | not all bias becomes violence |
| dehumanising mind | effective `d`-exclusion and recognition attenuation | not merely lack of empathy |
| bystander silence | suppression of `S_sig`; conversion into hidden `S_str` | does not cancel responsibility |
| hostile econiche | environment that confirms the discriminatory prior | policy target, not proof of cure |

---

## 4. Relation to existing SRT files

Primary integration:

```text
Philosophy/SRT_Social_Cognition.md
  -> T-Cog-6: Bounded-Surprisal Discrimination Gate
```

Secondary links:

```text
Core_Law/SRT_Occlusion_Dynamics.md
  -> B-phase occlusion / locked update failure

Core_Law/SRT_Collective_Selection.md
  -> asymmetric M(t) / collective L2 self-protection

Core_Law/SRT_Suffering.md
  -> S_sig suppression and S_str externalization

Philosophy/SRT_Social_Political_PH_SS_Guardrails.md
  -> dehumanization as d-exclusion

Philosophy/SRT_Soc_02_Behavioral.md
  -> recognition operator / dehumanization as cooperation-channel break

Neuroscience/SRT_Clin_02_FEP.md
  -> FEP terms remain one-way bridge proxies
```

---

## 5. Operational consequences

This bridge suggests looking for cases where:

1. counter-stereotypical evidence is repeatedly encountered but discounted;
2. in-group wrongdoing produces silence rather than correction;
3. out-group suffering fails to enter the agent's morally relevant selection field;
4. policy changes the social econiche before private belief changes;
5. enforced non-discriminatory behavior eventually makes previous discriminatory priors harder to maintain.

These are operational hypotheses, not completed SRT predictions.

---

## 6. Boundary cautions

- Do not write "ZBS = d-value."
- Do not write "active inference proves SRT."
- Do not infer that all group preference is dehumanization.
- Do not use mechanism explanation as exculpation.
- Do not treat the article as direct experimental proof; it is a theoretical bridge.

---

## 7. Integration status

Integrated as `T-Cog-6` in:

```text
Philosophy/SRT_Social_Cognition.md
```

Future use should compress this patch into 2-4 paragraphs when cited in public-facing text.
