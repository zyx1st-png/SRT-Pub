# SRT Neuroscience Hardening N10: BTSP and Single-Experience Hardening v0.1

> Status: bridge / lab working draft.  
> Canonical caution: this document does not modify SRT primitive axioms. It proposes a neuroscience-facing implementation and pressure-test layer for SRT.

## 0. Purpose

This note extends the neuroscience hardening sequence after N1-N9 by adding a candidate micro-mechanism for fast L1-to-L2 sedimentation: behavioral timescale synaptic plasticity (BTSP).

The goal is not to claim that BTSP proves SRT. Rather, BTSP is treated as a concrete neuroscience-facing mechanism that supports one of SRT's core bridge hypotheses:

> A single sufficiently consequential experience can cross from transient L1 anchoring into L2-like structural sedimentation when selection traces, behavioral relevance, and local plasticity triggers converge within a viable time window.

In compact SRT terms:

```text
high-d L1 event + eligibility trace + local trigger -> L2 micro-hardening
```

---

## N10. BTSP is a candidate micro-hardening mechanism for fast L1-to-L2 sedimentation

### Claim

Behavioral timescale synaptic plasticity (BTSP) provides a candidate neural mechanism for rapid, single-experience hardening. Unlike classic Hebbian/STDP rules that emphasize millisecond-scale coincidence, BTSP operates over behavioral timescales of seconds. This allows a recent sequence of neural activity to be retroactively or prospectively captured by a plasticity-triggering event such as a dendritic plateau potential.

In SRT terms, BTSP suggests that the nervous system can maintain a temporary field of selectable traces and then harden a subset of them when an event becomes behaviorally consequential enough to trigger local structural change.

### Core formulation

> BTSP shows how a lived episode can become more than transient activity: a recent selection trajectory can be written into synaptic structure after a single experience.

### SRT mapping

| BTSP concept | Neuroscience-facing role | SRT interpretation |
|---|---|---|
| Eligibility trace | Recent activity remains modifiable across seconds | unresolved L1-adjacent selection trace |
| Dendritic plateau potential | local trigger for synaptic modification | micro-scale anchoring / hardening event |
| Single-trial place-field formation | rapid stabilization of spatial representation | L1 experience entering L2-like constraint |
| Behavioral timescale window | seconds-wide credit-assignment interval | temporal range of selectable traces |
| Synaptic weight change | durable change in future firing/selectability | L2 sedimentation of prior selection |

### Why this matters for SRT

BTSP strengthens a key SRT bridge hypothesis: L2 formation is not only slow repetition. Repetition can harden selections, but high-consequence or well-timed single experiences may also sediment rapidly if the system marks the relevant traces and then triggers plasticity.

This is important for explaining:

1. rapid spatial learning;
2. one-shot memory formation;
3. trauma-like over-hardening after a single high-d event;
4. sudden skill or schema acquisition after a decisive episode;
5. why some experiences vanish while others immediately reshape the future selection landscape.

### Distinction from classic Hebbian/STDP framing

Classic Hebbian/STDP mechanisms emphasize tight temporal coincidence between pre- and postsynaptic activity. BTSP loosens this requirement by allowing synapses active seconds before or after a triggering plateau event to be modified.

SRT should not describe BTSP as merely another reward-learning rule. Its significance is broader: it supplies a mechanism by which a behaviorally situated episode can be converted into a structural constraint on future selectability.

Compact distinction:

```text
STDP: millisecond coincidence -> local association
BTSP: behavioral-timescale trace + plateau trigger -> episode-scale hardening
SRT: concern-weighted selection + friction payment -> L1-to-L2 sedimentation
```

---

## 1. Formal sketch

A minimal SRT-compatible BTSP-inspired update rule can be written as:

```text
Delta w_i = eta * e_i(t) * K(t - t_p) * D(d, Psi_f)
```

where:

| Term | Meaning |
|---|---|
| `Delta w_i` | synaptic weight change for input `i` |
| `eta` | learning-rate / plasticity gain |
| `e_i(t)` | eligibility trace of recently active input `i` |
| `t_p` | time of plateau / triggering event |
| `K(t - t_p)` | behavioral-timescale temporal kernel |
| `D(d, Psi_f)` | SRT modulation term: concern-weighted importance and selection-friction condition |

Interpretation:

```text
A trace becomes hardenable only if it remains eligible within the behavioral window and is captured by a local trigger under sufficient concern-weighted relevance.
```

This allows SRT to distinguish three cases:

| Case | Expected result |
|---|---|
| Active trace without trigger | transient activation, weak or no hardening |
| Trigger without relevant trace | nonspecific or unstable modification |
| Eligible trace + trigger + high d-value | strong L1-to-L2 micro-hardening |

---

## 2. Relation to d-value

BTSP does not by itself define d-value. However, it gives a plausible implementation site where d-value-like variables may modulate hardening probability.

SRT hypothesis:

> High d-value events increase the probability, gain, persistence, or downstream consolidation of BTSP-like hardening.

Possible routes:

1. neuromodulatory gating;
2. affective or threat-related amplification;
3. attentional gain;
4. interoceptive state effects;
5. action-consequence coupling;
6. future selectability impact.

Thus, d-value should not be reduced to plateau potential itself. Rather, plateau potential is one possible local trigger, while d-value is the system-level concern weighting that biases which triggers matter, which traces are preserved, and which changes later consolidate.

---

## 3. Relation to Psi_f

BTSP also gives a useful way to operationalize part of `Psi_f`.

In SRT, `Psi_f` is the cost of anchoring a candidate into manifest commitment or structural sedimentation. In a BTSP-compatible neural setting, this cost may appear as the threshold or difficulty of moving from transient activity to lasting synaptic change.

Possible proxies:

| SRT friction component | BTSP-facing proxy |
|---|---|
| candidate conflict | competing active traces |
| anchoring threshold | plateau-generation threshold |
| temporal closure | width and shape of eligibility kernel |
| historical inertia | existing synaptic/L2 basin resistance |
| affective or bodily load | neuromodulatory/interoceptive modulation |

Hypothesis:

```text
Lower Psi_f within a trained or primed basin should make BTSP-like hardening easier.
Higher Psi_f for incompatible alternatives should make reversal or counter-hardening more difficult.
```

---

## 4. Experimental implications

### Flagship prediction N10-P1: single-event hardening is d-modulated

If BTSP is a micro-hardening mechanism, then one-shot neural and behavioral learning should be stronger when the event has higher d-value, even after controlling for salience, attention, and task difficulty.

Test:

```text
single-trial learning task
x manipulated d-value / self-relevance / consequence
x neural proxy of rapid plasticity or representational shift
```

Expected SRT result:

```text
high d-value -> stronger rapid representational hardening
```

### Flagship prediction N10-P2: hardening requires trace-trigger capture

SRT predicts that neither trace activity nor trigger alone is sufficient for robust L2-like sedimentation. Strong hardening should require a match between recent eligible traces and a trigger event.

Expected result:

```text
eligible trace + trigger > trace alone
eligible trace + trigger > trigger alone
```

### Flagship prediction N10-P3: trauma as pathological one-shot over-hardening

A high d-value threat event may produce excessive L2 sedimentation after a single episode. In SRT terms, trauma is not merely strong memory; it is a restructuring of the future selection landscape in which threat-related candidates become lower-friction anchors.

Compact expression:

```text
high-d threat L1 -> over-weighted L2_threat basin
```

### Flagship prediction N10-P4: reversal requires counter-hardening, not only information correction

If a harmful L2 basin was formed through high-d rapid hardening, explicit information alone should often be insufficient. Intervention must generate new low-friction embodied L1 anchors capable of competing with or rewriting the hardened basin.

Expected implication:

```text
corrective information < embodied safety/action re-anchoring
```

---

## 5. Boundaries and cautions

1. BTSP should not be presented as proof of SRT ontology.
2. BTSP is currently best established in hippocampal spatial-learning contexts, especially CA1 place-field formation, and should not be assumed to explain all forms of fast learning.
3. SRT should treat BTSP as one candidate implementation of L1-to-L2 micro-hardening, not as the only mechanism.
4. d-value is not identical to salience, reward, attention, or plateau potential.
5. Psi_f is not identical to a cellular threshold; cellular thresholds may instantiate only one local component of broader selection friction.

---

## 6. Citation anchors

- Quanta Magazine, "A New Type of Neuroplasticity Rewires the Brain After a Single Experience" (2026-04-24).  
  https://www.quantamagazine.org/a-new-type-of-neuroplasticity-rewires-the-brain-after-a-single-experience-20260424/

- Bittner, K. C., Milstein, A. D., Grienberger, C., Romani, S., & Magee, J. C. (2017). Behavioral time scale synaptic plasticity underlies CA1 place fields. *Science*, 357(6355), 1033-1036.  
  https://doi.org/10.1126/science.aan3846

---

## 7. One-paragraph abstract

Behavioral timescale synaptic plasticity (BTSP) provides a strong neuroscience-facing candidate mechanism for SRT's L1-to-L2 hardening problem. Unlike classic millisecond-scale Hebbian/STDP rules, BTSP allows recent neural activity across seconds to be captured by a dendritic plateau event and converted into durable synaptic change, enabling single-experience learning such as rapid place-field formation. In SRT terms, eligibility traces correspond to unresolved selectable traces, plateau potentials correspond to local hardening triggers, and synaptic weight changes correspond to micro-L2 sedimentation. BTSP does not prove SRT and should not be equated with SRT ontology, but it supports the bridge hypothesis that sufficiently consequential lived episodes can rapidly reshape future selectability when trace, trigger, d-value, and selection-friction conditions converge.
