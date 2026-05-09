---
source_id: SRC-2026-05-08-PHIL-SOC-ACTIVE-INFERENCE-DISCRIMINATORY-COGNITION
title: "An active inference explanation of discriminatory cognition with regard to social attitudes and harmful behaviour"
source_type: peer_reviewed_open_access_article
domain: philosophy_social_cognition
url: "https://www.sciencedirect.com/science/article/pii/S0303264726001036"
preprint_url: "https://osf.io/download/2h3et/"
doi: "10.1016/j.biosystems.2026.105793"
pii: "S0303-2647(26)00103-6"
authors: "Hector M. Manrique; Karl J. Friston; Michael J. Walker"
publication: "BioSystems, article 105793"
date_published: "2026-06-30 cover date; online metadata available before cover month"
date_added: "2026-05-08"
evidence_level: peer_reviewed_theoretical_article_plus_osf_preprint_full_text
reliability_level: high_for_conceptual_bridge_medium_for_empirical_claim
content_access: "Elsevier metadata via PII; OSF preprint full-text PDF with matching title and authors"
srt_relevance: high
integration_priority: high
related_srt_claims:
  - social_cognition
  - discriminatory_cognition
  - dehumanization
  - active_inference
  - zones_of_bounded_surprisal
  - d_exclusion
  - recognition_channel
  - occlusion_dynamics
  - collective_selection
  - structural_suffering
tags:
  - active_inference
  - discriminatory_cognition
  - dehumanization
  - zones_of_bounded_surprisal
  - social_attitudes
  - bystander_silence
  - institutional_betrayal
status: source_card
---

# SourceCard: Active Inference, ZBS, and Discriminatory Cognition

## 1. One-line summary

Manrique, Friston, and Walker use active inference and zones of bounded surprisal (ZBS) to explain how discriminatory and dehumanising cognition can become self-confirming, socially reinforced, and resistant to corrective evidence.

## 2. Core claims of source

The article argues that social attitudes and harmful discriminatory behavior can be interpreted through active inference. The key bridge concept is the zone of bounded surprisal: a cognitive range within which unfamiliar or contradictory information can be tolerated, sampled, and used for updating.

The paper's strongest usable claims for SRT are:

1. discriminatory minds may have narrow ZBS bandwidths with respect to out-group evidence;
2. in-group acquiescence and bystander silence can reinforce harmful attitudes by lowering immediate cognitive dissonance;
3. dehumanising minds represent an extreme where racist, misogynous, homophobic, or otherwise discriminatory beliefs are deeply self-identifying;
4. active behavior can make the social world conform to prior expectations, turning belief into self-evidencing social structure;
5. policy can sometimes work by changing the econiche first, forcing repeated exposure to counter-evidence and new normative behavior before beliefs fully change.

## 3. Evidence / method

This is a peer-reviewed theoretical article in *BioSystems* with a final ScienceDirect / Elsevier metadata record:

```text
DOI: 10.1016/j.biosystems.2026.105793
PII: S0303-2647(26)00103-6
Journal: BioSystems
Article number: 105793
```

Local access notes:

- ScienceDirect direct HTML was blocked by the publisher's anti-bot layer during processing.
- Elsevier's metadata endpoint confirmed the title, DOI, PII, journal, open-access status, and license.
- An OSF preprint PDF with the same title and authors provided the full text used for close reading.

## 4. Limits

1. The article is a theoretical / explanatory synthesis, not a new direct experiment on discriminatory cognition.
2. ZBS is an active-inference bridge concept; it should not be rewritten as SRT's canonical `d`, `\Psi_f`, `T_dir`, or recognition operator.
3. The paper's mechanism does not imply that discriminatory actors are morally or legally excused by narrow ZBS.
4. In-group favoritism, discriminatory belief, bystander silence, and dehumanising violence must remain separate levels.
5. Policy claims are plausible mechanism hypotheses, not universal recipes.

## 5. SRT relevance

The material directly strengthens SRT's social cognition branch by giving an external mechanism for a known SRT pattern:

```text
external suffering signal -> group prior conflict -> signal suppression -> structural suffering export
```

SRT-compatible translation:

```text
narrow cross-group ZBS
  -> lower update tolerance for out-group evidence
  -> higher L2 rigidity and recognition-channel attenuation
  -> d-exclusion / bystander silence / collective M(t) asymmetry risk
```

The most important bridge is not "active inference proves SRT." It is narrower:

```text
ZBS offers a useful proxy for how much contradiction a social-cognitive system can tolerate before it protects identity rather than updating belief.
```

## 6. Suggested patch target

Primary target:

```text
Philosophy/SRT_Social_Cognition.md
```

Patch record:

```text
Philosophy/patches/SRT_Philosophy_SOC_COG01_ZBS_Discriminatory_Cognition_v0_1.md
```

Integration hook:

```text
Philosophy/hooks/SOC_COG01_ZBS_Discriminatory_Cognition_Integration_Hook.md
```

## 7. Pipeline 1裁决

- Conclusion: A, as a small social-cognition bridge integration.
- Evidence level: peer-reviewed theoretical article plus matching preprint full text.
- Claim strength: bridge / mechanism interface, not P0/P1 proof.
- Main integration: `T-Cog-6: Bounded-Surprisal Discrimination Gate`.
