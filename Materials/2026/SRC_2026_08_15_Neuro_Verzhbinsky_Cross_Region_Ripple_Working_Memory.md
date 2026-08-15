---
source_id: SRC-2026-08-15-NEURO-VERZHBINSKY-CROSS-REGION-RIPPLE-WORKING-MEMORY
id: SRC-2026-08-15-NEURO-VERZHBINSKY-CROSS-REGION-RIPPLE-WORKING-MEMORY
title: "Cross-region neuron co-firing mediated by ripple oscillations supports distributed working memory representations"
source_type: peer_reviewed_primary_neuroscience_article
domain: neuroscience_working_memory_ripples_distributed_representation_relational_reinstatement
authors: [Ilya A. Verzhbinsky, Jonathan Daume, Sophia Cheng, Ueli Rutishauser, Eric Halgren]
publication: Nature Neuroscience
date_published: 2026-08-12
date_added: 2026-08-15
doi: 10.1038/s41593-026-02403-z
url: https://www.nature.com/articles/s41593-026-02403-z
evidence_level: peer_reviewed_primary_open_access_full_text
reliability_level: high_for_human_intracranial_single_unit_and_LFP_association_with_declared_sampling_and_causality_limits
srt_relevance: very_high
integration_priority: very_high
related_srt_claims:
  - transient_distributed_coordination
  - component_state_vs_organizational_state
  - relational_reinstatement
  - history_conditioned_future_selectability
  - memory_reentry
  - momentary_selection_eligibility
  - phase_dependent_gating
  - large_scale_phase_scaffold
  - working_memory
  - NEURAL23
  - NEURAL28
  - NEURAL29
  - NEURAL31
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags:
  - ripples
  - working-memory
  - intracranial
  - single-unit
  - co-firing
  - distributed-representation
  - reinstatement
  - temporal-coordination
  - relational-state
  - memory-reentry
---

# SourceCard — Verzhbinsky et al.: cross-region ripple-mediated co-firing and working-memory reinstatement

## 0. Provenance and verification status

Primary source:

- Ilya A. Verzhbinsky, Jonathan Daume, Sophia Cheng, Ueli Rutishauser & Eric Halgren.
- *Cross-region neuron co-firing mediated by ripple oscillations supports distributed working memory representations*.
- **Nature Neuroscience**, published 12 August 2026.
- DOI: `10.1038/s41593-026-02403-z`.
- Version of record and full article were checked directly on the publisher page in the 2026-08-15 processing pass.

This is a peer-reviewed primary human intracranial study, not a review, commentary or preprint.

---

## 1. One-line summary

During a human working-memory task, brief co-occurring ~90-Hz ripple events across distant cortical and limbic sites mark privileged windows of cross-region single-neuron temporal coordination; the coordinated firing scales with memory load and preferentially reinstates stimulus-specific encoding relations during retrieval, especially on faster recognition trials.

---

## 2. Experimental design and measurement scope

The authors reanalyzed an open intracranial dataset from:

- `35` patients with medically refractory epilepsy;
- `43` recording sessions;
- bilateral recordings from hippocampus (`HIP`), amygdala (`AMY`), ventromedial prefrontal cortex (`vmPFC`), anterior cingulate cortex (`ACC`) and pre-supplementary motor area (`preSMA`);
- `1,927` microwire channels;
- `1,373` isolated single units.

Participants performed a modified Sternberg working-memory task:

```text
encoding: sequentially view 1 or 3 images
-> maintenance: retain the set across a delay
-> retrieval: judge whether a probe image belonged to the encoded set
```

Ripple detection used 70–100-Hz filtered LFP activity with a peak above `2.5 s.d.`, at least three oscillations and no sharp transient. Electrodes in the seizure-onset zone and epileptiform periods were excluded. Typical events were approximately `69–75 ms` long with center frequencies around `91 Hz` across sampled regions.

A co-ripple was defined when ripples in two recording sites overlapped for at least `25 ms`.

---

## 3. Source-backed evidence windows

### 3.1 Local-to-nonlocal transition, then little further distance attenuation

Median ripple co-occurrence within a microwire bundle at `<~5 mm` separation was approximately:

```text
13%  (IQR 7–22%)
```

Across different bundles it fell to approximately:

```text
5%  (IQR 4–6%)
```

but showed little further decline across the sampled nonlocal range:

```text
intrahemisphere: 71–203 mm
crosshemisphere: 35–223 mm
```

The crosshemisphere and intrahemisphere median co-ripple rates differed by only about `0.1 percentage points`.

Safe conclusion:

```text
local coordination > nonlocal coordination,
but within the sampled nonlocal range there was minimal additional distance-related attenuation.
```

Do **not** rewrite this as `brain coordination is distance independent` or as proof of whole-brain global binding.

### 3.2 Co-ripples mark genuine spike-timing coordination beyond independent rate increases

Across `31,489` analyzed unit pairs, co-firing within a 25-ms coincidence window was higher during co-ripple than no-ripple periods:

```text
median increase ~= 34%
```

The enhancement was present across AMY–cortex, HIP–cortex, AMY–HIP, ipsilateral cortico-cortical and contralateral cortico-cortical pairs.

Two rate-corrected controls were especially important:

1. observed co-firing exceeded the independent-rate null more strongly during co-ripples than no-ripples; the excess above null was about `56%` greater during co-ripples;
2. spike-time tiling coefficient (`STTC`) was about `117%` higher during co-ripples (`0.023`) than no-ripples (`0.011`).

Therefore:

```text
co-ripple effect
!= only both neurons firing more often
```

The data support an additional temporal-coordination component.

### 3.3 Cognitive load can increase coordination without increasing global mean firing

During maintenance, increasing memory load from one to three items increased co-ripple rate across the recorded set, while mean firing rate across all detected neurons showed no significant load increase (`P = 0.99`).

This creates an empirically useful dissociation:

```text
higher cognitive demand
!= necessarily higher global mean firing

higher cognitive demand
can involve
higher coordination demand
```

This does not imply that firing magnitude is irrelevant. During retrieval, mean firing as well as co-rippling increased with load in several analyses.

### 3.4 Task-related co-firing enhancement is concentrated in co-ripple windows

For cell pairs meeting the baseline co-firing threshold, cross-region co-firing relative to baseline increased during co-ripple periods by approximately:

```text
encoding:    +28%
maintenance: +29%
retrieval:   +24%
```

During no-ripple periods the corresponding changes were small or negative:

```text
encoding:    +1%
maintenance: -3%
retrieval:   -4%
```

Load-dependent co-firing was likewise concentrated in co-ripple windows:

```text
maintenance, load 3 vs load 1: +13%
retrieval,   load 3 vs load 1: +19%
```

versus approximately `-1%` and `-0.2%` during no-ripple periods.

This supports the interpretation of co-ripples as **brief privileged coordination windows**, not merely a continuously elevated high-frequency state.

### 3.5 Event coincidence is not reducible to continuous amplitude-envelope correlation

The paper compared ripple events with low-gamma and very-high-gamma activity and also analyzed cross-regional amplitude-envelope correlations. Ripple-band event co-occurrence showed the strongest and most consistent load modulation, while continuous amplitude-envelope correlations did not robustly scale with memory load.

Safe distinction:

```text
transient event coincidence
!=
continuous power covariation
```

This supports a transient-coordination interpretation, but it does not establish ripple as the unique frequency or universal binding mechanism. The authors explicitly discuss slower oscillations and theta–gamma phase-amplitude coupling as complementary or potentially competing coordination mechanisms.

### 3.6 Stimulus-specific encoding relations are preferentially reinstated during retrieval co-ripples

For each cross-region cell pair, the analysis asked whether two neurons that co-fired during encoding of a specific stimulus also co-fired during retrieval when the **same stimulus** was presented.

Across load-3 trials, repeated encoding-to-retrieval co-firing occurred at:

```text
co-ripple periods: 0.29% of cell-pair trials
no-ripple periods: 0.14%
```

The effect replicated across hippocampal–cortical, amygdala–cortical, ipsilateral and contralateral pairings and exceeded stimulus-label-shuffle and spike-time-shuffle controls.

The absolute percentages are low because the denominator is the high-dimensional product of cell-pairs and trials; the evidential point is the controlled relative enrichment, not the raw percentage alone.

### 3.7 Stronger relational reinstatement is associated with faster recognition

In high-load trials where the retrieval stimulus matched an encoded stimulus, repeated co-firing during co-ripples was higher for fast than slow responses:

```text
fast RT: 0.36%
slow RT: 0.23%
```

The paper therefore links:

```text
encoding-related distributed relation
-> retrieval-time relational reinstatement
-> behavioral efficiency
```

This is an association, not a causal intervention demonstrating that inducing a specific co-ripple will generate the representation or behavior.

---

## 4. What the source directly supports

### Strong source-level support

```text
co-ripples mark brief windows of enhanced long-distance temporal coordination;
co-ripple-associated co-firing scales with working-memory demand;
stimulus-specific cross-region co-firing relations can recur from encoding to retrieval;
this relation-level reinstatement is enriched during co-ripples and associated with faster recognition;
node firing magnitude alone does not exhaust the task-relevant neural state description.
```

### Reasonable mechanistic interpretation

```text
higher cognition can recruit transient distributed interactive coordination rather than relying only on a fixed sequential point-to-point pipeline;
organizational / relational variables carry explanatory information beyond local activation magnitude.
```

### Not established by this paper

```text
co-ripple = SRT selection;
co-ripple = L1;
co-ripple = consciousness;
co-ripple coalition = bearer / subject;
ripple = universal neural binding mechanism;
relations are ontologically prior to neurons;
all memory is relational reinstatement;
astrocytes cause ripple reinstatement;
large-scale phase scaffold -> ripple -> content is one demonstrated causal chain.
```

---

## 5. High-value SRT distinction: component state != organizational state

A minimal bridge pressure from the data is:

```text
local activity state
!=
complete functional organization state
```

Two periods can have similar local firing magnitudes yet differ in which cross-region neuron pairs are temporally coordinated. Therefore a neural implementation of SRT should leave room for relation variables in addition to component variables.

Non-canonical bridge notation:

\[
\sigma_{bridge}(t) = \big(X(t), R(t), \Theta(t)\big),
\]

where:

- `X(t)` = local / component activity variables;
- `R(t)` = transient effective relational organization;
- `Theta(t)` = timing / phase / physiological context variables that modulate which relations are currently realizable.

This is **not** a replacement definition for the owner neural manifold `sigma(t)` and must not be promoted to canonical notation without owner-level adjudication.

---

## 6. SRT bridge: memory re-entry as history-conditioned relational re-instantiation

The source directly supports encoding-to-retrieval reinstatement of stimulus-specific distributed co-firing relations. SRT can make a narrower P3 inference:

```text
past event
-> historical changes in the system
-> changed probability that a related distributed organization can be re-instantiated later
```

The important claim is **not**:

```text
memory is proven not to be stored
```

but:

```text
retrieval can be described functionally as present re-instantiation under historical constraint,
not as literal return of an identical past microstate.
```

Candidate local notation:

\[
P\!\left(R_m^{reentry}\mid C_t,H_m,E_t\right)
\]

where `H_m` denotes prior history relevant to memory `m`, `C_t` the current cue/context and `E_t` a bridge-level current eligibility state. None of these symbols redefine canonical SRT variables.

---

## 7. Four-line integration pressure with existing SRT neuroscience

This paper should not stand alone as a `ripple = selection` patch. Its highest value appears when cross-read with three existing lines:

```text
NEURAL31:
past experience -> historical eligibility / retrievability changes

existing large-scale phase scaffold:
local activity is embedded in large-scale cortical phase organization

NEURAL23:
continuous embodied / rhythmic constraint shaping -> momentary eligibility

NEURAL33 source pressure:
brief co-ripple window -> stimulus-specific distributed relational reinstatement
```

A bounded integration hypothesis is therefore:

```text
historical constraints
+ current embodied / phase state
-> momentary coordination eligibility
-> transient distributed relation realization
-> recognition / memory re-entry / later write-back
```

This is a **compatible multi-scale bridge hypothesis**, not one experimentally demonstrated causal chain.

---

## 8. Differential predictions opened by the source

The paper creates a mechanism-level prediction family that should be tested separately from phenomenon-level SRT predictions:

1. **History × current eligibility interaction**: historical strength and current physiological/phase eligibility should interact, not merely add, in predicting relation-level reinstatement.
2. **Relational residual**: after matching firing rate, ripple power, task difficulty and arousal, relation-level similarity should retain incremental behavioral prediction if organizational state is genuinely explanatory.
3. **Pre-ripple prediction**: pre-ripple body/phase state should predict which stimulus-specific relation will be reinstated, not only general reaction speed, if eligibility is content-selective rather than generic readiness.
4. **Component turnover tolerance**: same-content reinstatement may preserve relational organization despite incomplete overlap in participating components.
5. **Historical-eligibility manipulation**: manipulations of a memory-linked historical eligibility substrate may alter re-entry probability / latency / stability without necessarily erasing content coding.
6. **Retention != retrievability**: comparable retained trace strength can coexist with different current relation-level re-entry probabilities.

These predictions are formalized in the companion NEURAL33 experiment protocol rather than being treated as confirmed findings.

---

## 9. Failure / downgrade conditions

The SRT bridge should be narrowed if any of the following repeatedly hold under strong controls:

```text
relation-level variables add no predictive value after node firing / power / arousal are matched;
pre-ripple embodied or phase state predicts only generic readiness and not content-specific reinstatement;
encoding-to-retrieval similarity is fully explained by stable component identity without relation-level residual;
co-ripple reinstatement fails to replicate outside this Sternberg paradigm or outside the sampled clinical population;
interventions show that apparent relational reinstatement is an epiphenomenon of ordinary excitability changes.
```

Failure of a universal ripple account would **not** by itself refute SRT. It would refute or narrow the NEURAL33 implementation bridge.

---

## 10. Clinical / sampling boundary

The sample consists of epilepsy patients implanted for clinical monitoring, and electrode placement was determined by clinical need. Important working-memory regions such as posterior parietal cortex were not systematically sampled. High task accuracy also limited error-trial analyses.

Therefore:

```text
strong human intracranial mechanism evidence
!=
complete whole-brain map
!=
healthy-population causal proof
```

---

## 11. SRT-facing compression

The safest high-value compression is:

> **A cognitive neural state is not exhausted by how strongly its components are active; which distributed relations are transiently realized can carry stimulus-specific, behaviorally relevant structure. Prior history may matter partly by changing the probability that such an organization can be realized again under present conditions.**

Or, more compactly:

> **Memory is not the past returning; memory use can involve the present re-instantiation of a historically enabled organization.**

The second sentence is SRT bridge language, not a direct quotation or settled conclusion of the source.
