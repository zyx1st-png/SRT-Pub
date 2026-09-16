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
reliability_level: medium_for_reported_task_associations; low_medium_for_rate_vs_temporal_separation; limited_for_causal_gamma_history_or_consciousness_inference
srt_relevance: moderate_as_guardrail_against_rate_gain_gamma_selection_history_one_and_consciousness_overread
integration_priority: low_medium
related_srt_claims:
  - attentional_prioritization_vs_mean_firing_gain
  - temporal_coordination_not_selection
  - NEURAL33_boundary
  - NEURAL34_match_failure
  - salience_reward_not_d_value_identity
  - one_formation_boundary
  - consciousness_synchrony_guardrail
tags: [auditory-cortex, saliency, gamma, theta-gamma, spike-field-coupling, temporal-coordination, firing-rate, spatial-tuning, task-engagement, guardrail]
---

# SourceCard: Irani-Cereceda et al. — auditory spatial saliency through temporal coordination

## 1. Archive summary

Irani-Cereceda et al. report that, during an active auditory task in mice, sounds presented from the currently reward-associated spatial location show stronger gamma-range temporal coordination, spike-field coupling, response reliability and sharper spatial tuning, while a consistent population-level mean firing-rate gain is not observed. The effect extends from the rewarded pure tone to unrewarded AM broadband probe stimuli presented from the same location and is not reported during passive listening.

For SRT this is retained as a **B2 guardrail-only source**, not as reinforcement of `NEURAL33` or `NEURAL34`. The experiment does not isolate durable history-conditioned organization, does not meet the current `NEURAL34` matched-state hierarchy, does not separate salience from reward/stake well enough to serve as a `d-value` negative control, and does not test One formation or consciousness.

---

## 2. Source boundary and load-bearing anchors

Primary source:

> Irani-Cereceda, M., Qu, Z., Sen, K., Sadaghiani, S. & Gritton, H. J. (2026), *Representations of spatial saliency in auditory cortex are selectively organized through temporal coordination*, bioRxiv preprint. DOI `10.64898/2026.06.10.731488`. Version posted 2026-06-12.

Evidence status:

```text
primary full-text preprint
not peer reviewed in the supplied version
mouse A1 laminar electrophysiology
17 mice
no causal gamma / optogenetic manipulation in the reported experiments
```

Load-bearing anchors from the supplied 25-page PDF:

- **p.1 Summary:** behaviorally relevant sound locations are associated with increased response reliability, temporal precision and gamma-related spike-field coupling even for unrewarded sounds; the authors interpret this as temporal coordination rather than a simple firing-rate gain account.
- **pp.3-4 and Methods pp.15-16:** training establishes the auditory go/no-go lick/reward contingency, but the spatial reward rule relevant to this recording paradigm is implemented in the active recording blocks. The rewarded 10 kHz sound is fixed at the 90° contralateral location; unrewarded AM broadband probes are presented across multiple locations. The AM probes are not novel neutral stimuli in the strong sense: they are familiar unrewarded/no-go stimuli.
- **p.3 / recording design:** active and passive block order is counterbalanced, but the principal results are reported by pooled condition rather than by a residual/carry-over analysis testing whether active exposure changes a later matched passive state.
- **pp.5-7 / Fig.3:** active engagement is associated with alpha-beta and gamma changes; spatial location modulates gamma measures, and theta-gamma coupling is stronger in the active condition around the rewarded location.
- **pp.7-9 / Fig.4:** gamma-range spike-field coupling is stronger during active engagement and is strongest around the rewarded location; stronger coupling is associated with higher trial-to-trial reliability.
- **pp.9-11 / Fig.5:** firing-rate changes are heterogeneous and the population analysis does not show a consistent location-specific mean gain; neurons with stronger gamma coupling are also more narrowly spatially tuned.
- **pp.13-14 / stated limitations:** attention and arousal are not fully disentangled; there is no direct spatial-discrimination behavioral readout; the source of the task-dependent gamma organization may be local or inherited from higher-order inputs; causal necessity/sufficiency of gamma is not established.

---

## 3. What the source supports

### 3.1 Active task prioritization is associated with temporal coordination

Safe source-level statement:

```text
within the active task,
current spatial relevance / reward association
is associated with stronger temporal coordination,
response reliability and tuning changes,
without an observed consistent population mean firing-rate gain.
```

This is an association statement. The study does not establish that gamma coordination causes the prioritization effect.

### 3.2 The spatial priority generalizes across stimulus identity within the active task

The rewarded event is a 10 kHz tone, whereas the probe stimuli are unrewarded AM broadband sounds. The probes presented from the rewarded location show the same direction of enhanced temporal coordination.

Safe compression:

```text
current task-defined spatial priority
can generalize from the rewarded stimulus
across unrewarded probe identity.
```

Blocked reading:

```text
pre-existing learned reward-location history
-> durable later relational disposition
```

The supplied design does not establish that stronger history claim. It does not isolate a matched later state after the reward-location rule is removed, and it does not analyze persistent carry-over in a way that would support `NEURAL34`-style history attribution.

### 3.3 The firing-rate result is a bounded null-style dissociation, not an equivalence proof

The paper reports no consistent population-level location-specific mean firing-rate gain. That supports a useful caution against reducing task-related prioritization to mean rate alone.

It does **not** establish:

```text
firing-rate information = absent;
firing-rate model = equivalent across conditions;
temporal coordination causally replaces firing rate.
```

No equivalence test or matched decoding comparison is reported in the supplied manuscript.

---

## 4. Design limitations that matter for SRT use

The following are load-bearing for interpretation rather than minor caveats:

1. **Reward location is never swapped.** The rewarded sound remains at the 90° contralateral location, which is also a strongly driven location for right A1. Behavioral relevance is therefore not cleanly separated from location-specific sensory drive.
2. **Arousal is not fully separable from spatial relevance.** The pupil analysis includes a location effect and a location-by-condition interaction in the small pupil subset; the authors themselves discuss transient arousal at salient spatial input.
3. **Active versus passive is not a matched-state history comparison.** Task state, arousal and oscillatory power differ, so the design does not satisfy even `NEURAL34` Match-1 (`mean firing / power / task / arousal matched`).
4. **No durable history residual is measured.** Counterbalanced active/passive order does not by itself establish carry-over, and the paper does not report a dedicated post-active passive residual analysis.
5. **The firing-rate conclusion is based on absence of a robust population gain effect.** No equivalence test or decoding-based demonstration shows that rate information is absent or interchangeable.
6. **Some inferential claims are narrower than the prose summary suggests.** The rewarded-location PPC effect is frequency-bounded, the passive/active contrast is partly argued through significant-versus-nonsignificant results rather than a direct interaction test, and the manuscript does not provide a direct behavioral readout of improved spatial discrimination.
7. **Trial density is limited.** The supplied Methods report a small number of probe repetitions per speaker/envelope combination, and the stated rewarded-trial count is not obviously reconcilable with the described insertion frequency without additional clarification.

These limitations do not erase the reported association; they lower the strength of any mechanistic or SRT-specific inference.

---

## 5. SRT guardrails

### 5.1 `NEURAL33`: adjacent example, not evidence reinforcement

`NEURAL33` explicitly states that its useful increment is **not generic synchrony**. Its stronger package combines distributed co-ripple coordination, single-neuron timing, working-memory load, relation repetition and behavioral association, with a relation-level residual beyond component magnitude.

This preprint instead provides local A1 LFP/spike-field temporal coordination plus tuning/reliability associations. It is therefore best treated as an adjacent mature-neuroscience example for the modest guard:

> **Task-related attentional prioritization need not appear as a consistent population mean firing-rate gain.**

It does not add the stronger `NEURAL33` relational reinstatement burden.

### 5.2 `NEURAL34`: current design fails the matched-state burden

The current `NEURAL34` protocol requires, at minimum:

```text
Match-1 = mean firing / power / task / arousal matched
```

The Irani-Cereceda active/passive comparison does not satisfy that condition. It therefore cannot be counted as evidence that history retains relation-specific predictive value after current-state controls.

The owner-side evidence base also already includes Duncan et al. 2023 as a more direct learned-priority example in which a neutral probe exposes selection-history priority. The probe-priority motif is therefore not a new residual created by this source.

### 5.3 Reward / salience cannot be used here as a `d-value` negative control

The source does not license either identity:

```text
salience = d-value
reward = d-value
```

But it is also **not a clean negative control for `d-value`**, because the mice are water-restricted and reward/stake-related variables covary with the salient location/task rule. The experiment does not independently hold stake/reward constant while varying salience.

The existing CompactCore distinction remains sufficient:

> **Salience makes a signal noticeable; d-value makes a signal matter.**

No new `d-value` guardrail or revival path is created here.

### 5.4 Temporal coordination does not test One formation

The relevant One owner defines One through a relatively separable **Selection-mediated vertical reconstitution path** in which prior Selection-generated vertical organization materially enters later Selection conditions and is recurrently regenerated.

An already formed organism's transient neural ensemble coordination is downstream of that admission problem. Therefore:

```text
transient gamma / spike-field coherence
!= evidence for One formation
```

This source does not need a Bearer-like "role-bearing" gloss to make that point.

### 5.5 Temporal binding here is not consciousness evidence

The manuscript contains no consciousness contrast, no report/no-report manipulation directed at phenomenality, and no evidence that its gamma coordination is sufficient for unified experience.

Accordingly it must **not** be used as support for phase-synchrony / coherence claims in `Ax-CONSC-MECH-3` or `T-FIELD-1` without a separate consciousness-specific evidential bridge.

---

## 6. Owner-side subtraction

```text
Potential-looking increment:
  auditory spatial prioritization
  + gamma / theta-gamma / spike-field coordination
  + unrewarded probe generalization
  + no consistent population mean firing-rate gain.

Subtraction:
  generic oscillatory coordination is a mature N3 neighbor;
  NEURAL33 already owns the stronger component-state != organizational-state burden;
  NEURAL34 already owns the matched-state history test and already contains Duncan et al. 2023 for learned-priority / probe logic;
  CompactCore already owns gain as one candidate mechanism rather than the identity of attention or salience;
  CompactCore already owns salience != d-value;
  One owner already blocks one-shot / downstream mechanism from One formation;
  consciousness/field owners already make synchrony claims, so this source requires a non-promotion guard rather than reinforcement.

Residual after subtraction:
  one source-specific auditory example showing that active task prioritization can covary with temporal coordination and representational reliability without an observed consistent mean population firing-rate gain.

Verdict:
  B2 guardrail-only.
  No A-conversion route is currently identified.
```

---

## 7. Pipeline 1 disposition

```text
Verdict:
  B2 = guardrail-only.

Current writeback:
  SourceCard + Material Log only.

O-track:
  no owner reinforcement claim;
  bounded source-specific boundary / mature-neighbor example only.

D-track:
  none / not claimed.

No current landing target:
  no new NEURAL number;
  no PatchNote / Hook;
  no Neural CompactCore edit;
  no prediction-table edit;
  no canonical owner edit.
```

### Revival triggers

Material remains parked unless one of the following named events occurs:

1. **reward-location swap / counterbalancing replication** appears, or a reanalysis directly separates location-specific sensory drive from task relevance;
2. **persistent carry-over / residual analysis** is reported after the reward-location rule is removed, with current task/arousal/power substantially matched;
3. `NEURAL33` / `NEURAL34` is explicitly reopened **after** the first-well Case-B constraint and third-well HOLD are revisited, and a new dataset satisfies the relevant relation/history discriminator rather than only generic synchrony;
4. a peer-reviewed or causal circuit version materially changes the mechanism evidence enough to reopen the source classification.

A future `d-value` hardening pass alone is **not** a revival trigger for this source, because reward/stake and salience are not independently manipulated here.

---

## 8. Safe future citation

If this paper is cited in future neuroscience prose, the safe use is narrow:

> **In one mouse A1 preprint, active task-related spatial prioritization was associated with stronger gamma-related temporal coordination, response reliability and sharper tuning without an observed consistent population mean firing-rate gain.**

Do not extend that sentence into `history -> relational disposition`, `gamma = Selection`, `salience = d-value`, `coherence = One`, or `synchrony = consciousness` without independent evidence.
