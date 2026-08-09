---
id: SRT-NEURO-NEURAL27-PROSPECTIVE-MEMORY-EVENT-BOUNDARY-HISTORICAL-EFFICACY
patch_id: PATCH-NEURO-NEURAL27-PROSPECTIVE-MEMORY-EVENT-BOUNDARY-HISTORICAL-EFFICACY
type: bridge_patch
status: active
version: v0_1
canonical: false
claim_level: P3-P4
claim_mode: evidence
layer: operations
epistemic_layer: os
domain: Neuroscience
source_ids: [SRC-2026-08-09-NEURO-RANGANATH-PROSPECTIVE-MEMORY-EVENT-BOUNDARIES]
created: 2026-08-09
target_future_doc:
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
  - Neuroscience/SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md
  - Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md
related_claims: [L2, NEURAL25, N10, N11, CG4, HEF2, HEF3, prediction_error_proxy]
tags: [memory, prospective-memory, event-boundary, hippocampus, anticipatory-gaze, sleep, curiosity, historical-efficacy, L2]
---

# NEURAL27 — Prospective memory, event boundaries, and historical efficacy

> **Boundary**: P3 neuroscience bridge with P4 experimental consequences. This patch does not redefine memory, `L2`, `G_hat_theta`, `Psi_f`, `d`, `T_dir`, real choice, subjecthood or consciousness.

## 1. Source anchor

Verified anchors:

- Reagh et al. (2020), *Nature Communications*, DOI `10.1038/s41467-020-17713-4`.
- Barnett et al. (2024 issue; online 2023), *Neuron*, DOI `10.1016/j.neuron.2023.10.010`.
- Schmidig et al. (2025), *Communications Psychology*, DOI `10.1038/s44271-025-00305-7`.
- Gruber, Gelman & Ranganath (2014), *Neuron*, DOI `10.1016/j.neuron.2014.08.060`.
- Gruber & Ranganath (2019), PACE framework, DOI `10.1016/j.tics.2019.10.003`.

The trigger was a user-supplied Charan Ranganath talk transcript. Rhetorical claims from the talk are not promoted unless they survive paper-level verification.

---

## 2. Why this matters for SRT

SRT already has three relevant bridge lines:

```text
N10: some single experiences can produce rapid L1 -> L2-like hardening
N11: history can deform future transition reachability
NEURAL25: retained representation != memory's causal role in future selection
```

NEURAL27 adds an empirical middle:

> **A past episode can be detected through how it changes a later prospective path before the remembered event is physically present again.**

The MEGA paradigm is especially useful because repeated viewing keeps much of the current sensory stream fixed while prior episode history differs.

```text
matched pre-event sensory stream
+ different prior episode history
-> different anticipatory gaze trajectory
```

This is close to NEURAL25's matched-current-state / different-history logic, but the published paradigm does not by itself establish a full SRT CG-4 result.

---

## 3. Main bridge claim

> **Memory should not be operationalized only as retained or reportable content. A history-bearing memory can also be assayed by whether prior experience changes the accessibility, timing, probability or direction of a later perceptual or action trajectory before the predicted event occurs.**

Short form:

> **The causal signature of memory is prospective: the past matters insofar as it changes what the system is prepared to do next.**

This is a P3 bridge, not a canonical definition of memory.

---

## 4. Remembering is reconstruction, not replay

The talk's "painting rather than photograph" metaphor is useful, but the stronger sentence "memory is not about the past at all" is too strong.

A safer decomposition is:

```text
past L1 event
-> surviving historical trace / constraint
-> retrieval under current context and goals
-> reconstructed present L1 about the past
```

Schematically:

\[
L_1^{recall}(t)=F(H_{past},\theta(t),C(t),G_{goal}(t))
\]

where `H_past` is only a local bridge label for a history-bearing state.

Guardrail:

```text
recall != literal reinstatement of the original L1 event
```

---

## 5. Event boundaries as update opportunities

Naturalistic fMRI studies show that hippocampal and posterior-medial-network responses increase around event boundaries, and boundary-specific hippocampal-cortical connectivity is associated with later memory.

SRT-safe reading:

> Event boundaries are candidate **history-update opportunities**: moments when an event model closes or context changes enough that recent traces become especially eligible for re-indexing or consolidation.

This can sharpen N10 at a higher explanatory scale:

```text
recent eligible trace
+ event-model boundary / update opportunity
+ consolidation process
-> increased chance of later history-sensitive control
```

But:

```text
event boundary != Real Choice Moment
event boundary != BTSP plateau
hippocampus != L2
```

A room transition, topic shift or film cut can be an event boundary without constituting an SRT-grade selection event.

---

## 6. Prediction error remains a proxy

Boundaries often coincide with changes in predictability or context. The packet therefore supports:

```text
prediction break / event-model mismatch
-> increased probability of boundary processing and memory update
```

It does **not** support:

```text
prediction error = Psi_f
surprise = d-value
event-model update = L2
```

Prediction error remains at most a local `Psi_f`-related proxy under a declared task window.

---

## 7. Anticipatory gaze as a historical-efficacy readout

In MEGA, the same clip is viewed again after prior exposure. Before the salient event occurs on repeated viewing, gaze becomes biased toward the event's future location.

Minimal formalization:

\[
P(G_{next}\mid I_t,H_1) \neq P(G_{next}\mid I_t,H_0)
\]

where:

- `I_t` = current pre-event sensory input;
- `H_0` = no episode-specific prior viewing;
- `H_1` = prior episode-specific viewing;
- `G_next` = next gaze target / trajectory.

The important point is prospective path divergence, not retrospective report.

A local non-canonical proxy can be written as:

\[
HCAE = E[GAD_{naive} - GAD_{repeat}]
\]

with `GAD` = gaze-to-event distance in a preregistered pre-event window.

`HCAE` is not an SRT primitive or canonical variable.

---

## 8. HEF / CG-4 mapping

| Level | NEURAL27 reading |
|---|---|
| HEF-0 | prior exposure can be externally recorded; insufficient |
| HEF-1 | current state may differ after exposure; insufficient |
| HEF-2 | episode history is actively used to alter a later pre-event gaze response; strongly supported as a functional readout |
| HEF-3 | history changes later path accessibility / transition probability; the evidence is HEF-3-shaped, but full admission still requires the causal-carrier and future-organization gates of the current operational protocol |
| HEF-4 | rule / boundary write-back is not established |

Therefore the safe conclusion is:

> MEGA provides a strong prospective **history-use** readout and a candidate path-bias assay; it should not be promoted directly to canonical `L2` or full CG-4.

---

## 9. Relation to NEURAL25

NEURAL25 separates:

```text
Acquisition
-> Availability
-> Authority
-> Expression
-> Write-back
```

NEURAL27 supplies a naturalistic readout for the middle of this chain:

- **Acquisition**: the first viewing supplies the event association.
- **Availability**: the association is available before the event reappears.
- **Authority**: it can bias where the eyes go next.
- **Expression**: anticipatory gaze is the observed path consequence.
- **Write-back**: prior exposure clearly matters later, but the specific history carrier and stronger reachability rewrite still require separate causal testing.

Thus:

```text
verbal recall
!= memory availability
!= control authority
!= anticipatory expression
!= L2-grade historical write-back
```

---

## 10. Relation to N10 and N11

### N10

NEURAL27 suggests a macro-level sequence compatible with rapid hardening work:

```text
continuous episode
-> event boundary / model transition
-> memory-update opportunity
-> consolidation
-> later anticipatory path bias
```

It does not identify the boundary response with any one cellular plasticity mechanism.

### N11

N11's bridge formula is:

```text
L2 = historically sedimented topology of selection reachability
```

NEURAL27 contributes a local behavioral readout shape:

```text
prior history
-> changed probability distribution over next gaze paths
```

This is a candidate example of history-conditioned transition deformation, not proof that every remembered episode is canonical `L2`.

---

## 11. Sleep and report/control dissociation

The MEGA sleep experiment matters because anticipatory gaze provides a no-report measure of memory use.

SRT-safe distinction:

```text
reportable memory strength
!= prospective control efficacy
```

Future experiments should measure both rather than treat verbal recognition as the sole ground truth for historical efficacy.

Do not infer that sleep universally improves prediction or that sleep itself equals `L2` consolidation.

---

## 12. Curiosity as active mismatch resolution

The curiosity work supports an adjacent loop:

```text
prediction / knowledge gap
-> appraisal
-> information seeking
-> exploratory sampling
-> enhanced memory under some conditions
```

The SRT-relevant point is that mismatch can change what information the system seeks next.

Guardrails:

```text
curiosity != d
curiosity != T_dir
prediction error != Psi_f
exploration != real choice
```

---

## 13. New claim cluster

### NEURAL27a — Prospective historical efficacy

A memory can be operationally detected through systematic pre-event changes in later perception/action trajectories.

### NEURAL27b — Boundary-gated update opportunity

Event boundaries are candidate moments for selective event-model closure, indexing and consolidation.

### NEURAL27c — Report/control dissociation

Verbal recollection and future-guiding control should be measured separately.

### NEURAL27d — History-difference replay test

Repeated naturalistic stimuli provide a practical way to hold the current sensory stream approximately fixed while varying episode-specific history.

All remain P3/P4.

---

## 14. P4 experimental extension

Use a non-invasive three-condition design:

1. first viewing / no episode history;
2. repeated viewing after ordinary retention interval;
3. repeated viewing after a condition designed to reduce episode-specific retention while matching current visual input as closely as possible.

Measure before the event:

- gaze distance to future event location;
- first saccade target;
- latency to enter the event region;
- fixation distribution;
- explicit recognition and confidence separately.

The strongest SRT-facing analysis asks whether episode history explains prospective gaze behavior beyond explicit report and generic familiarity.

A critical negative control should preserve familiarity while changing or scrambling the event-location relation. If generic familiarity explains the effect, the historical-path interpretation must be weakened.

---

## 15. Failure conditions

Weaken NEURAL27 if:

1. anticipatory gaze disappears after low-level visual/narrative and familiarity controls;
2. explicit recognition/confidence fully explains the prospective gaze effect;
3. history changes only current response magnitude but no path probability, switching, reversal or transfer measure;
4. event-boundary effects reduce to perceptual salience without later-memory relation under appropriate controls;
5. sleep-related anticipatory benefit fails to replicate;
6. curiosity effects reduce fully to reward/attention under matched novelty and uncertainty.

Do not rescue the bridge by calling every persistent state difference `L2`.

---

## 16. Do not infer

Do not write:

- memory is not about the past;
- memory is only prediction;
- memory = `L2`;
- event boundary = real choice moment;
- event boundary = BTSP plateau;
- hippocampus = `L2`;
- hippocampal activation = memory itself;
- prediction error = `Psi_f`;
- surprise = `d`;
- anticipatory gaze = `T_dir`;
- sleep = historical write-back;
- the current boundary-response literature already supplies a clinical Alzheimer diagnostic.

---

## 17. Integration sentence

Candidate de-materialized sentence for a future neural-mechanisms synthesis:

> **A neural history is functionally stronger than a retained record when it changes what the system is prepared to select before the relevant event arrives. Naturalistic event-memory paradigms make this distinction measurable: closely matched pre-event sensory streams can elicit different gaze trajectories after different episode histories, while boundary-specific hippocampal interactions identify candidate moments at which recent experience becomes available for later control.**

Do not merge into an owner document until the neuroscience synthesis queue is reopened.

---

## 18. Abstract

Event-boundary and anticipatory-gaze research provides a strong neuroscience bridge for SRT's historical-efficacy program. Naturalistic fMRI studies show that hippocampal and posterior-medial-network processes concentrate around event boundaries and that boundary-specific hippocampal-cortical interaction predicts later memory. The MEGA paradigm shows that prior exposure can bias gaze toward a future event location before the event appears, allowing memory to be measured as a history-conditioned prospective behavioral divergence rather than only as retrospective report. In SRT terms, this sharpens NEURAL25's separation of retained representation from future control efficacy, complements N10's write-back problem, and provides a local readout shape for N11's history-conditioned transition field. The evidence strongly supports active history use and an HEF-3-shaped path-bias window, but does not by itself establish full CG-4, canonical `L2`, or any identity between event boundaries, hippocampal activity, prediction error, sleep, curiosity or anticipatory gaze and SRT primitives.