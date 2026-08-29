---
id: SRC-2026-08-26-PHIL-AMORNBUNCHORNVEJ-DISAGREEMENT-ATTENTION
source_id: SRC-2026-08-26-PHIL-AMORNBUNCHORNVEJ-DISAGREEMENT-ATTENTION
type: source_card
status: active
layer: materials
epistemic_layer: evidence
claim_mode: evidence
title: "Disagreement without Representational Deficit: Attention Dynamics over a Shared Evaluative Basis"
source_type: user_supplied_full_text_pdf
domain: philosophy_cognitive_science_attention_disagreement
authors: [Chainarong Amornbunchornvej]
publication: bibliographic_status_not_independently_verified_in_this_pass
date_published: 2026
date_added: 2026-08-26
url: null
doi: null
evidence_level: full_text_primary_argument_with_secondary_use_of_cited_empirical_literature
reliability_level: high_for_source_argument_medium_for_cited_empirical_claims_pending_primary_verification
srt_relevance: very_high
integration_priority: high
verdict: A
canonical: false
related_srt_claims:
  - P24-3
  - P24-4
  - P2/P3-B13
  - HEF-3/HEF-4
  - PH-IND06
  - SRT-OPEN-TENSIONS
  - Selection-D2
  - CandidateField
tags: [Attention, Disagreement, Representation, Engagement, Plasticity, Lock, LearnedInattention, RivalModel, P24-3, P24-4]
---

# SourceCard — Amornbunchornvej, *Disagreement without Representational Deficit*

## 1. One-line summary

Amornbunchornvej argues that persistent evaluative disagreement and fixation need not imply representational deficit: agents can share the same evaluative basis while differing in relative attention profile, total engagement, and slowly changing attentional gain states, so durability of disagreement alone underdetermines the underlying structure.

## 2. Bibliographic / source anchor

- Author: Chainarong Amornbunchornvej, National Electronics and Computer Technology Center (NECTEC), Thailand.
- Title: *Disagreement without Representational Deficit: Attention Dynamics over a Shared Evaluative Basis*.
- Source used in this intake: user-supplied 23-page full-text PDF.
- Full close-read completed 2026-08-26.
- Publication venue / DOI for this paper were **not independently verified in this pass**; do not infer peer-review status from the PDF alone.

## 3. Core claims of the source

### 3.1 Persistence does not diagnose representational mismatch

The paper targets the inference that a disagreement surviving years of mutually intelligible exchange must reflect incompatible representational resources. It instead decomposes cases under a shared evaluative basis into profile difference, engagement difference, and bounded relative plasticity.

**Anchors:** Abstract, PDF p.1; §1, PDF pp.1–3, especially p.2.

Compact source claim:

```text
representational loss
!= profile disagreement
!= engagement disagreement
```

### 3.2 Shared basis and persistent positive gain state

Representable evaluative dimensions are modeled as a fixed basis:

```text
B = {b1, ..., bn}
```

with a persistent log-gain state `lambda_t` and strictly positive gains:

```text
theta_t,i = exp(lambda_t,i) > 0
```

A dimension can therefore become arbitrarily weak in current evaluation without being mathematically annihilated from the basis.

**Anchors:** §2.1, PDF pp.3–4.

Source distinction:

```text
absent from basis
!= present but functionally negligible
```

### 3.3 Relative profile and total engagement are separate variables

In context `c`, the expressed gain vector is factorized into:

```text
w_i(c) = h_i / sum_j h_j
s(c)   = sum_j h_j
```

where `w` is the normalized relative profile and `s` is total engagement. The valuation rule is:

```text
e_t(x | c) = sum_i h_i(lambda_t,c) x_i
           = s_t(c) * sum_i w_t,i(c) x_i
```

Two agents can therefore rank considerations identically while differing in how much the whole domain matters to them.

**Anchors:** §§2.2–2.3, PDF pp.4–5.

### 3.4 Context modulates expression without necessarily rewriting disposition

A reference multiplicative expression class is:

```text
h_i(lambda,c) = exp(lambda_i + phi_i(c))
w(c) = softmax(lambda + phi(c))
```

so persistent disposition and context-conditioned expression remain analytically distinct.

**Anchor:** §2.2, PDF p.5.

### 3.5 Bounded relative plasticity yields self-gated revision

Endogenous learning is modeled as:

```text
lambda_{t+1} = lambda_t + delta_t
||delta_t||_infinity <= epsilon
```

which bounds multiplicative gain change per step. The paper derives:

```text
|Delta theta_i| <= (exp(epsilon)-1) theta_i
```

and therefore argues that a currently weak dimension can change only a small absolute amount per step. The paper summarizes this mechanism as attention gating its own revision.

**Anchor:** §3, PDF pp.6–7.

### 3.6 Lock is cross-context dominance, not semantic pathology

A state is locked on a dimension when that dimension retains near-total profile dominance across a class of contexts that would ordinarily pull attention apart. The definition is content-neutral: scholarly vocation, parental concern, and clinically significant fixation can all instantiate the same formal shape.

**Anchor:** §4.1, PDF pp.7–8.

### 3.7 Persistence is a finite-horizon reachability result, not impossibility

Given a lock margin and bounded drift, the paper derives a lower bound on the time before the lock can be lost. In the multiplicative reference class the bound is proportional to margin divided by the plasticity ceiling. The author explicitly distinguishes exact impossibility from practical non-reachability within a relevant horizon.

**Anchors:** §4.2, PDF pp.8–9.

### 3.8 Recovery is generally a new forward state

Even if the previously dominant gain later returns toward its old value, other coordinates may have changed in the interim, so the recovered state generally need not equal the old one. The paper treats recovery as a further forward transition rather than an inverse replay.

**Anchor:** §4.2, PDF p.9.

### 3.9 Persistent disagreement under shared representation

The taxonomy distinguishes basis mismatch from profile difference, engagement difference, and mutual lock. The paper further separates persistence of the underlying profile source from inertia of any one evaluative output gap.

**Anchors:** §5, PDF pp.9–12; Table 1, PDF p.10.

### 3.10 Transfer from dimensional attention to evaluative attention is an explicit hypothesis

The paper imports structural commitments—not parameter values—from category-learning work: a fixed stock of dimensions, persistent state, context-conditioned graded weighting, and bounded gated revision. It explicitly states that the transfer is defeasible rather than established by analogy alone.

**Anchors:** §6.1, PDF pp.12–13.

### 3.11 One latent state is assigned two roles

A pivotal identification treats the state that gates learning as the same state that weights valuation. The paper acknowledges this as a genuine empirical exposure: if learning-gating and valuation-weighting states dissociate, the persistent-disagreement result weakens.

**Anchors:** §6.2, PDF pp.13–14.

### 3.12 Encoded / retrievable can dissociate from online influence

The paper's strongest SRT-relevant empirical anchor is its discussion of Gao et al. (2024): non-dominant dimensions were reportedly recognized above chance and usable when the dominant dimension was removed, yet had no measurable online effect while that dominant feature remained available.

Paper's compact interpretation:

```text
knowledge present, influence absent
```

**Anchor:** §7.1, PDF p.14.

Important source-status guard: this intake verified what **this paper reports** about Gao et al.; the Gao primary paper was not independently re-read in this pass.

### 3.13 Attention need not have a fixed total budget

The paper separates relative profile from total engagement and argues, via its review of attention-model comparisons, that total attention can vary with demand. It allows approximately budget-like behavior to reappear as a regime when an engagement ceiling binds.

**Anchor:** §7.2, PDF pp.14–15.

### 3.14 Learned inattention provides a behavioral analogue of lock

The paper cites learned-inattention, developmental switching-cost, learning-trap, and exploration findings as evidence that selective history can produce entrenched configurations and costly reallocation.

**Anchor:** §7.3, PDF p.16.

### 3.15 Reweighting is not basis extension

The model explicitly holds the representational basis fixed. The author states that attention dynamics redistribute over dimensions already given and do not create genuinely new evaluative dimensions.

**Anchor:** §8, PDF pp.16–17.

### 3.16 Persistence underdetermines “deep” disagreement

The paper's philosophical result is not that deep disagreement never exists, but that persistence under comprehending exchange is a non-diagnostic behavioral signature because a shallower shared-basis attention dynamic can generate it as well.

**Anchor:** §9, PDF pp.17–19.

## 4. Evidence / method

The paper is a formal-philosophical construction with literature-grounded assumptions rather than a new empirical experiment. Its argument has four layers:

1. define a shared representational basis and positive gain state;
2. factor expression into profile and engagement;
3. impose bounded relative plasticity and derive persistence bounds;
4. connect the model to category-learning / attention literature and state explicit falsifiers.

The source's empirical anchors are therefore mostly cited external studies. This SourceCard treats those as **paper-reported evidence** unless independently verified elsewhere in SRT-Pub.

## 5. Limits and failure conditions stated by the source

### 5.1 Fixed basis

The model does not explain acquisition of genuinely new evaluative dimensions or recoding of the basis.

**Anchors:** §2.1, PDF p.4; §8, PDF p.17.

### 5.2 Multiplicative plasticity is the weakest pivotal modeling bet

The paper explicitly states that fitted update rules in the literature it reviews lean additive. Published support is stronger for multiplicative decay than growth; the exact log-gain bounded update should therefore be treated as a modeling choice rather than an established empirical law.

**Anchor:** §7.4, PDF p.16.

### 5.3 Persistence only; no unlocking floor

A1 is a ceiling on update magnitude. It allows `delta_t = 0` and therefore cannot predict when disconfirmation must produce revision. A direction-sensitive floor would require further theory.

**Anchor:** §10, PDF p.20.

### 5.4 History-blind persistence bound

The bound depends on current margin and plasticity ceiling; formation history leaves no independent trace once those variables are given. The paper explicitly leaves open whether history acts only through current state or has additional effects.

**Anchor:** §10, PDF p.20.

### 5.5 Collected falsifiers

The source identifies several failure exposures, including:

- encoded dimensions having exactly zero evaluative contribution rather than graded-negligible influence;
- a long-ignored dimension leaping to dominance through one ordinary endogenous experience;
- demonstrated per-stimulus maximum / discrete-system selection replacing the smooth weighted-sum valuation form;
- dissociation of learning-gating and valuation-weighting states.

**Anchor:** §10, PDF p.20.

## 6. SRT relevance

### 6.1 Source-backed pressure

The source directly pressures any SRT-adjacent inference of the form:

```text
behavioral silence
-> representation absence
```

or:

```text
persistence / fixation / slow switching
-> deep framework change
```

because the paper supplies a structured ordinary account in which the basis remains shared while weighting and engagement differ and reweighting is slow.

### 6.2 SRT-side synthesis after owner subtraction

The useful audit distinctions are:

```text
representable
!= retrievable / available
!= relatively weighted
!= total engagement
!= online operative influence
!= SRT Selection
!= historical writeback
```

This is a category-hygiene sequence, **not** a new canonical stage model.

Further guards:

```text
profile w != matter / concern / d
engagement s != bearer-relative stake / d
attention lock != bearer admission
attention lock != L2 by definition
```

### 6.3 Rival value for P24-3

Self-gated attention / learned-inattention dynamics can absorb ordinary signatures such as fixation, slow alternative reactivation, switching cost, history-conditioned weighting, hysteresis-like persistence, and practical non-reachability within a horizon.

Therefore these signatures cannot by themselves establish a Selection-level D2 result.

### 6.4 Rival value for P24-4

A represented consideration can become functionally negligible and thereby behave as if invisible in ordinary evaluation. P24-4 visibility / admissibility work must therefore distinguish:

```text
basis absence
vs represented-but-negligible weighting
vs current online operativity
vs genuine candidate-generation / admissibility revision
```

### 6.5 Generative-reselectability boundary

The source's fixed-basis scope gives a clean lower-order rival:

```text
reweighting existing dimensions
!= basis extension
!= candidate-generator revision
!= comparison-rule revision
!= boundary / composition revision
```

The stronger cases remain routed to existing B13 / HEF owners; being outside this source model does not automatically make them SRT-specific.

### 6.6 Bearer boundary

The source presupposes agents and does not supply SRT's same-unit consequence-return, non-outsourcing, identity, or bearer-continuity criteria. It therefore cannot serve as bearer-admission evidence.

### 6.7 Recovery as support, not novelty

The source's recovery-nonidentity point is compatible with existing SRT history-bearing work, but should be used as external support / example rather than a parallel history theorem.

## 7. Suggested patch target

Primary patch / hook target:

```text
Philosophy/patches/SRT_Philosophy_PH_ATTN01_Representational_Weight_Engagement_Operativity_v0_1.md
Philosophy/hooks/PH_ATTN01_Representation_Weight_Engagement_Operativity_Integration_Hook.md
```

Primary empirical-rival target:

```text
Operations/Audits/SRT_ATTENTION_DYNAMICS_RIVAL_ADDITION_P24_3_P24_4_2026-08-26.md
```

Future owner landing, if separately authorized:

```text
Core/SRT_Core_24_Discriminating_Predictions.md
```

## 8. Final source disposition

```text
A — bounded non-canonical O-track category hygiene + rival hardening
D-track — not claimed by this source intake
Selection-core novelty — low
P24-3 / P24-4 rival value — very high
empirical calibration value — high
```

Do not cite attention, engagement, learned inattention, bounded reweighting, persistence or recovery nonidentity as uniquely SRT phenomena.
