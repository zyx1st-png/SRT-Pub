---
source_id: SRC-2026-09-16-NEURO-IRANI-CERECEDA-AUDITORY-SALIENCY-TEMPORAL-COORDINATION
id: SRC-2026-09-16-NEURO-IRANI-CERECEDA-AUDITORY-SALIENCY-TEMPORAL-COORDINATION
title: "Representations of spatial saliency in auditory cortex are selectively organized through temporal coordination"
source_type: preprint_primary_full_text
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
domain: neuroscience_auditory_attention_saliency_temporal_coordination
primary_authors: "Martin Irani-Cereceda; Zhili Qu; Kamal Sen; Sepideh Sadaghiani; Howard J. Gritton"
publication: "bioRxiv preprint"
doi: "10.64898/2026.06.10.731488"
url: "https://doi.org/10.64898/2026.06.10.731488"
date_published: "2026-06-12"
date_added: "2026-09-16"
evidence_level: preprint_primary_full_text_mouse_laminar_electrophysiology
reliability_level: medium_high_for_reported_association_and_rate_vs_temporal_dissociation; limited_for_causal_gamma_mechanism_and_cross_domain_generalization
srt_relevance: high_as_source_specific_realization_of_existing_relational_neural_bridge_and_as_guardrail_against_gain_only_readings
integration_priority: medium_high
related_srt_claims:
  - neural_selection_before_representation
  - component_state_vs_organizational_state
  - transient_distributed_coordination
  - history_conditioned_future_selectability
  - salience_vs_d_value
  - NEURAL33
  - NEURAL34
tags: [auditory-cortex, saliency, gamma, theta-gamma, spike-field-coupling, temporal-coordination, firing-rate, spatial-tuning, reward-history, distributed-representation]
---

# SourceCard: Irani-Cereceda et al. — auditory spatial saliency through temporal coordination

## 1. One-line summary

Irani-Cereceda et al. report that behaviorally relevant sound locations in mouse primary auditory cortex are preferentially expressed through **gamma-band synchronization, spike-field coupling, theta-gamma coupling, improved response reliability, and sharper spatial tuning without a consistent population-level firing-rate gain**; the effect generalizes to neutral probe sounds presented from the reward-associated location during active task engagement.

For SRT, the paper is useful mainly as a **source-specific realization and guardrail** for already-owned neuroscience bridge claims: neural functional organization is not exhausted by component activity magnitude, and prior relevance history can alter how later matched-category sensory input is organized. It does not establish a new SRT construct.

---

## 2. Source boundary and evidence anchors

Primary source:

> Irani-Cereceda, M., Qu, Z., Sen, K., Sadaghiani, S. & Gritton, H. J. (2026), *Representations of spatial saliency in auditory cortex are selectively organized through temporal coordination*, bioRxiv preprint. DOI `10.64898/2026.06.10.731488`. Version posted 2026-06-12.

Evidence status:

```text
primary full-text preprint
not peer reviewed in the supplied version
```

Load-bearing source anchors from the supplied 25-page PDF:

- **p.1 Summary:** behaviorally relevant sound locations selectively increase response reliability, temporal precision and spike-field coupling to gamma oscillations even for unrewarded sounds; the authors frame gamma-mediated synchronization as a mechanism by which spatial relevance reshapes auditory encoding.
- **pp.3-4 / Fig.1 and Fig.2 setup:** head-fixed mice learned a rewarded 10 kHz tone at a fixed 90° location; neutral speech-envelope AM broadband-noise probes were then presented from four spatial locations in passive and active blocks. This design lets the authors ask whether spatial relevance generalizes to neutral sounds rather than simply tracking reward delivery or licking.
- **pp.5-7 / Fig.3:** active engagement increases alpha-beta and gamma power, but spatial location significantly modulates gamma rather than alpha-beta power. Gamma is strongest in superficial A1 channels and tracks stimulus temporal structure. Theta-gamma phase-amplitude coupling is stronger in the active block and spatially biased toward the rewarded location.
- **pp.7-9 / Fig.4:** spike-phase coupling in the gamma range increases during active engagement and is strongest for sounds at the rewarded location; the effect is absent in the passive block. Stronger gamma coupling is associated with higher trial-to-trial response reliability at the rewarded location.
- **pp.9-11 / Fig.5:** population firing-rate modulation is heterogeneous, with increases and decreases balancing at population level and no robust location-specific gain account. Stronger gamma coupling is instead associated with narrower receptive fields and tuning closer to the rewarded location.
- **pp.11-14 Discussion:** the authors interpret the result as temporal coordination / dynamic routing of distributed auditory representations rather than simple rate gain. They explicitly place the effect in value-driven saliency and top-down / predictive-coding-compatible frameworks.
- **pp.13-14 limitations:** selective attention versus general arousal is not fully disentangled; there is no direct behavioral readout of spatial discrimination improvement; the experiment does not establish whether the task-dependent gamma synchronization is generated locally in A1 or inherited from higher-order inputs. The authors call for cell-type-specific and causal circuit tests.

---

## 3. Core source claims

### 3.1 Behavioral relevance can be expressed through temporal coordination without consistent firing-rate gain

The strongest source-level dissociation is:

```text
behaviorally relevant location
-> stronger gamma / spike-field temporal coordination
-> higher trial reliability and sharper spatial tuning

while

consistent population-level firing-rate gain
= not observed
```

The paper therefore supports the bounded claim that local or population firing magnitude alone does not exhaust the neural variables relevant to context-sensitive sensory prioritization.

### 3.2 The relevant effect generalizes beyond the rewarded stimulus identity

The rewarded event is a pure tone, whereas the principal neutral probes are unrewarded AM broadband sounds. Neutral probes from the reward-associated spatial location nevertheless show enhanced temporal coordination in the active context.

Safe source-level reading:

```text
learned behavioral relevance of a spatial location
can alter later processing of neutral sensory events at that location
```

Blocked source overreach:

```text
reward history alone proves durable L2-like writeback
```

The paper shows history-conditioned saliency and later processing, not the full SRT history / sedimentation architecture.

### 3.3 Distributed representation can be reorganized relationally

The authors argue that auditory spatial information is represented in broadly tuned, overlapping populations rather than a sharply topographic cortical map. Their results support a mechanism in which temporally coordinated distributed ensembles can transiently prioritize behaviorally relevant locations.

Safe source-level abstraction:

```text
component activation magnitude
!=
complete organizational state
```

This is an implementation-level result, not an ontological proof that relations are prior to components.

### 3.4 Gamma is a candidate mechanism, not a demonstrated universal cause

The study is correlational / observational at the circuit-mechanism level. It does not causally perturb gamma synchronization and does not establish gamma as necessary or sufficient for the behavioral relevance effect.

Therefore:

```text
gamma synchronization = candidate circuit mechanism
not
proven universal selection mechanism
```

---

## 4. Evidence / method

The study uses laminar electrophysiology in mouse A1 during passive versus task-engaged auditory spatial conditions.

Key design features include:

1. **Reward-location learning** — a 10 kHz pure tone is associated with reward at one fixed spatial location.
2. **Neutral spatial probes** — unrewarded AM broadband sounds are presented from multiple locations, allowing reward/motor confounds to be reduced when comparing neutral probe processing.
3. **Laminar LFP + spike recording** — 4-shank, 32-channel arrays span cortical depth.
4. **Temporal coordination measures** — gamma power, theta-gamma phase-amplitude coupling and spike-field pairwise phase consistency are analyzed alongside firing rate.
5. **Representational quality measures** — trial-to-trial response similarity and spatial receptive-field metrics are related to coupling strength.

A total of 17 transgenic mice were used. No optogenetic manipulation was performed in these experiments despite the lines being selected for later optogenetic work.

---

## 5. Limits

The supplied preprint does **not** establish:

- peer-reviewed replication;
- causal necessity or sufficiency of gamma synchronization;
- a unique contribution of attention independent of arousal;
- a direct improvement in spatial discrimination behavior caused by the measured temporal coordination;
- whether the relevant gamma organization originates locally in A1 or arrives through top-down pathways;
- a general principle that all neural selection is temporally synchronized;
- that value-driven saliency is SRT `d-value`;
- that reward history is SRT `L2` by identity;
- that coherent functional ensembles satisfy the SRT One formation gate;
- that gamma, theta-gamma coupling, saliency, binding or dynamic routing are SRT Selection itself.

---

## 6. SRT relevance

### 6.1 Existing bridge support: organizational state beyond firing magnitude

This source independently realizes a distinction already made in NEURAL33:

```text
component / local activity variables
!=
organizational / relational state
```

The new source-specific value is modality and task context: in auditory spatial saliency, temporal organization predicts reliability / tuning even though a consistent population rate-gain account is absent.

This is useful support for the neuroscience-facing guard:

> **Selective neural organization need not be monotonic in local or population firing magnitude.**

It does not warrant a new neural-selection variable.

### 6.2 Existing bridge support: history-conditioned future organization

The reward-associated spatial location changes later neutral-probe processing. This is compatible with the already-owned NEURAL34 structure:

```text
past history
-> altered response / relational disposition
-> current opportunity / context
-> realized coordination
```

The paper adds an auditory saliency realization, not a new history ontology.

### 6.3 Guardrail value: salience / reward relevance are not `d-value`

The paper provides a clean example of reward-conditioned saliency and processing priority that can be described without establishing SRT stake / bearer / future-selectability burden.

Therefore it is useful as a negative control for:

```text
reward relevance != salience != d-value
```

The source itself does not discuss canonical SRT `d`.

### 6.4 Guardrail value: transient coherence is not One

The paper's language of coherent functional ensembles, temporal binding and dynamic routing does not show the SRT One requirement of recurrent role-bearing reconstitution / regenerative formation.

Safe use:

```text
transient synchrony + functional coherence
!= sufficient One evidence
```

This is SRT-side boundary work, not a conclusion of the source authors.

---

## 7. Owner-side novelty probe

```text
Candidate increment:
  auditory-saliency realization of relational temporal organization beyond firing-rate gain;
  reward-location history affecting later neutral-probe coordination;
  source-specific gamma / theta-gamma / spike-field example for existing bridge guards.

Likely owner(s):
  Neuroscience/patches/SRT_Neuro_NEURAL33_Distributed_Ripple_Relational_Reinstatement_v0_1.md
  Neuroscience/patches/SRT_Neuro_NEURAL34_History_Conditioned_Relational_Possibility_v0_1.md
  Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  _SRT_D_VALUE_CANONICAL.md only as a non-identity guard; no owner edit proposed.

Bounded probe:
  searched gamma / synchronization / temporal coordination / theta-gamma;
  searched firing-rate residual / relation-level organization;
  checked NEURAL33 organizational-state and relational-residual claims;
  checked NEURAL34 history-conditioned relational possibility and matched-state logic;
  checked current CompactCore gain / gating / stabilization wording.

Verdict:
  already owned + source-specific realization + guardrail support.

Residual after subtraction:
  no new SRT construct. The bounded residual is empirical breadth:
  an auditory spatial-saliency paradigm in which behavioral relevance is carried by temporal coordination,
  response reliability and tuning rather than a consistent population firing-rate gain,
  with neutral probes inheriting location-level relevance.

Inherited premises / constructive use:
  NEURAL33: component state != organizational state;
  NEURAL34: history can alter later relational realization probability;
  CompactCore: neural manifestation / anchoring proxy is not reducible to stronger activity;
  d owner: salience / reward remain non-identical to d-value.

Forbidden parallel construct:
  no new NEURAL number;
  no temporal-coordination scalar;
  no gamma = Selection identity;
  no saliency = verticality or d-value identity;
  no coherent ensemble = One identity.
```

---

## 8. Pipeline 1 disposition

```text
Verdict:
  B1 for future NEURAL33 / NEURAL34 evidence reinforcement and matched-history experiment design;
  B2 for gamma / saliency / One / d-value non-identity guardrails.

Contribution route:
  O-track = bounded realization / reverse-constraint support only;
  D-track = none / not claimed.

Current writeback:
  SourceCard + Material Log only.

No current landing target:
  do not edit Neural CompactCore, prediction table, canonical owner, or create a new PatchNote / Hook under the active synthesis-target freeze.
```

Revival triggers:

1. `NEURAL33` / `NEURAL34` or the Neural CompactCore is explicitly reopened for synthesis;
2. a peer-reviewed version or causal gamma / circuit manipulation materially changes the mechanism evidence;
3. the matched-current-input / different-history P4 workline is revised and needs an auditory saliency implementation / negative control;
4. a future `d-value` hardening pass needs a reward-salience negative control.

---

## 9. Suggested future use

If a future neuroscience synthesis is explicitly reopened, the safest native sentence is:

> **Selective neural organization can be realized through context-sensitive temporal coordination among distributed units, with changes in reliability and tuning even when no consistent population firing-rate gain is present.**

This should be used as a neuroscience bridge statement only. The source does not validate SRT ontology or establish gamma as the neural identity of Selection.
