# SRT Neuroscience Hardening N11: Transition Field, Subjective Time, and Action Readiness v0.1

> Status: bridge / lab working draft.  
> Canonical caution: this document does not modify SRT primitive axioms. It proposes a neuroscience-facing implementation and pressure-test layer for SRT.

## 0. Source anchor

Primary source:

- CLaE. (2026). *Mind as a Historically Shaped Transition Field: Subjective Time, Action Readiness, and the Measurement of Mental Dynamics*. Zenodo record supplied by user: https://zenodo.org/records/19779115

This note extracts SRT-relevant structure from the source and converts it into a bridge claim for SRT's neuroscience layer.

---

## 1. Why this material matters for SRT

The source paper proposes that mind should not be treated as a sealed inner domain containing mental contents. Instead, mind is described as a historically shaped transition field: a metastable dynamical domain whose current topology is continuously shaped by bodily regulation, environmental structure, memory history, and relational coupling.

This is highly compatible with SRT's existing L0-L1-L2 architecture:

```text
L0_accessible -> G_hat_theta -> L1 -> L2
```

The transition-field framework gives SRT a useful neuroscience-facing language for describing the *reachability* of selection. It shifts attention from isolated inner contents to the dynamic accessibility of possible next states.

In compact SRT terms:

```text
mind = historically shaped field of reachable transitions
selection = movement from candidate possibility into anchored trajectory
L2 = accumulated deformation of future reachability
```

---

## N11. Mind as a historically shaped selection-transition field

### Claim

At the neuroscience-facing level, SRT can model mind as a historically shaped selection-transition field. A mental state is not an isolated inner object. It is the momentary global configuration of a field that determines which perceptual, affective, cognitive, relational, and action trajectories are currently reachable.

This strengthens the SRT claim that L2 is not merely memory, habit, or prior belief. L2 is the historically accumulated deformation of future selectability.

### Core formulation

> Mind is not a container of contents; it is a historically shaped field of possible transitions.

SRT translation:

> Reality anchoring depends not only on what candidates exist in L0, but on which transitions from the current field configuration are reachable under theta, d-value, Psi_f, and L2 deformation.

---

## 2. Mapping transition-field terms to SRT

| Transition-field term | Meaning in source framework | SRT interpretation |
|---|---|---|
| Transition field | dynamically maintained domain of possible state transitions | L0_accessible as configured by embodied theta and L2 |
| Field topology | gradients, thresholds, attractors, and reachable paths | Psi_f landscape plus L2 deformation |
| Action-readiness density `r(t)` | density/accessibility of adaptive transition | local transition accessibility / selection readiness |
| Subjective time `tau(t)` | inverse index of transition accessibility | phenomenological signature of selection reachability |
| Attractor capture | trajectories trapped in restricted regions | high-friction basin or over-hardened L2 path |
| Self-mind map | accumulated deformation of transition field | L2 as historical sedimentation of prior selections |
| Relational coupling | second-person/social conditions shaping transition | social d-value and intersubjective theta constraints |

---

## 3. Subjective time as an index of selection reachability

The source formalizes subjective time as:

```text
tau(t) = 1 / r(t)
```

where `tau(t)` denotes subjective time and `r(t)` denotes action-readiness density or transition density.

SRT can interpret this as:

```text
subjective time dilates when adaptive transition becomes difficult or remote;
subjective time compresses when adaptive transition becomes coordinated and reachable.
```

This gives SRT a useful bridge between phenomenology and measurable dynamics.

The inverse relation is one transition-field model, not a general law of duration judgment. Action-conditioned timing adds a separate empirical window:

```text
observed subjective duration
=
action-compression pressure
+ coupling compensation
+ expectation / attention / event-change contributions
```

In four preregistered VR experiments, voluntary action produced compression pressure on perceived duration. Congruent live feedback in Experiments 1-2 may have partially compensated that compression relative to replayed or delayed feedback, but the kinematics-related duration effect did not replicate reliably in Experiments 3-4. The schematic above is therefore P3/P4 and non-canonical; it is not a fitted empirical law.

This result blocks five overreadings:

```text
sensorimotor coupling does not create time;
longer perceived duration does not always mean stronger agency;
subjective duration is not a direct selection counter;
subjective duration is not a direct Psi_f meter;
duration judgment does not validate SRT physical-time ontology.
```

Source trail: [Imaizumi et al. SourceCard](../Materials/2026/SRC_2026_07_16_Cognitive_Imaizumi_Sensorimotor_Time_Agency.md), [PH-AG04 patch](../Philosophy/patches/SRT_Philosophy_PH_AG04_Sensorimotor_Time_Agency_v0_1.md), and [PH-AG04 Integration Hook](../Philosophy/hooks/PH_AG04_Sensorimotor_Time_Agency_Integration_Hook.md).

### SRT-compatible reading

In SRT, a subject does not experience time as a neutral container. Time is experienced through the current accessibility of transition:

```text
low r(t) -> high transition remoteness -> time dilation / stuckness
high viable r(t) -> reachable transition -> time compression / flow
excessive r(t) -> saturation / overflow -> failed temporal integration
```

This maps directly onto SRT's concern with selection friction:

```text
r(t) inversely tracks local effective Psi_f for adaptive transition
```

A careful formulation is:

```text
r(t) ≈ transition accessibility under current theta, d, Psi_f, and L2
```

not:

```text
r(t) = Psi_f^{-1}
```

The latter would be too strong because `r(t)` includes bodily, environmental, relational, and historical conditions, while `Psi_f` is the broader cost of anchoring or transition.

---

## 4. N11 formal bridge

A minimal SRT extension can be written as:

```text
r_SRT(t) = F(L0_accessible(t), theta(t), d(t), Psi_f(t), L2(t), B(t), E(t), R(t))
```

where:

| Term | Meaning |
|---|---|
| `L0_accessible(t)` | currently reachable candidate space |
| `theta(t)` | embodied observer/system constraints |
| `d(t)` | concern-weighted consequence of possible transitions |
| `Psi_f(t)` | selection/anchoring friction |
| `L2(t)` | historically sedimented constraints |
| `B(t)` | bodily/autonomic regulation |
| `E(t)` | environmental affordance and predictability |
| `R(t)` | relational coupling and social safety/threat |

Then:

```text
tau_SRT(t) = 1 / r_SRT(t)
```

This should be treated as a bridge model, not as a canonical SRT axiom.

---

## 5. Relation to L2 hardening

The strongest SRT-compatible contribution of the transition-field model is its treatment of history.

The source framework argues that history does not merely influence the mind from outside. The field is shaped *as history*. Repeated experience progressively deforms the topology of reachable transitions: some paths become easier, some harder, some attractor-like, and some locally inaccessible.

This is nearly identical to the SRT understanding of L2:

```text
L2 = accumulated deformation of future selectability
```

SRT can therefore restate L2 as:

> L2 is the historically sedimented topology of selection reachability.

This improves the neuroscience layer because it avoids treating L2 as merely stored information. L2 becomes a dynamical terrain: a distribution of gradients, thresholds, basins, and path-dependencies that shape which future anchors become low-friction or high-friction.

---

## 6. Attractor capture and impaired action

The source paper interprets impaired action as attractor capture rather than weakness of an enclosed will. A person may retain abstract capacity, desire, and knowledge while still being unable to move into adaptive action because the transition path is locally inaccessible.

SRT can map this directly:

```text
abstract capability exists
but adaptive trajectory is not reachable from current field configuration
```

This gives SRT a precise account of action failure:

```text
action failure = failure of reachable L1 transition under current L2/Psi_f/d/theta configuration
```

### Contrast with depletion model

| Model | Explanation of impaired action | Prediction |
|---|---|---|
| Depletion model | inner resource is exhausted | gradual recovery as resources replenish |
| Attractor-capture model | field topology blocks transition | nonlinear recovery after threshold shifts |
| SRT model | adaptive L1 path is high-friction or inaccessible due to L2 basin capture | sudden reopening when theta, body, relation, or environment changes Psi_f landscape |

This is valuable for SRT because it gives an experimentally testable distinction. If action failure is caused by attractor capture, recovery should not always be monotonic. Small changes in bodily regulation, relational safety, environmental structure, symbolic framing, or action threshold may suddenly reopen a trajectory.

---

## 7. Measurement implication: r(t) is not a local neural signal

The source strongly argues that `r(t)` cannot be read directly from neuroimaging alone. This is not an anti-neuroscience claim. The point is that transition accessibility is a coupled variable emerging from brain, body, memory, environment, and relational regulation.

SRT should adopt this as a measurement principle:

```text
selection reachability cannot be localized to one neural signal
```

More formally:

```text
r(t) = F(N(t), A(t), M(t), E(t), R(t))
```

where:

| Variable | Meaning |
|---|---|
| `N(t)` | neural dynamics |
| `A(t)` | autonomic and bodily regulation |
| `M(t)` | memory-weighted field topology |
| `E(t)` | environmental conditions |
| `R(t)` | relational coupling |

SRT extension:

```text
G_hat_theta cannot be measured only by imaging L1 neural correlates.
It must be inferred from coupled transition dynamics.
```

---

## 8. Multimodal empirical window

The source proposes that longitudinal autonomic and bodily dynamics may provide a better window into transition accessibility than isolated neural snapshots.

SRT can use this to strengthen its experimental program.

Candidate measures:

| Dimension | Measures |
|---|---|
| Neural | EEG/MEG/fMRI network flexibility, control signals, salience/interoceptive networks |
| Autonomic | HRV, respiration, electrodermal activity, heart-rate dynamics |
| Bodily | temperature rhythm, posture, movement, fatigue, metabolic state |
| Sleep/circadian | sleep structure, latency, fragmentation, recovery patterns |
| Behavioral | initiation latency, transition frequency, task switching, avoidance/approach |
| Relational | co-regulation, social safety/threat, second-person responsiveness |
| Phenomenological | subjective time dilation/compression, stuckness, flow, self-coherence |

The relevant model is latent-variable estimation:

```text
r(t) ≈ F_hat(N(t), HRV(t), Resp(t), Sleep(t), EDA(t), Temp(t), Move(t), Beh(t), M(t), E(t), R(t))
```

For SRT, this can become an empirical route for estimating:

```text
transition accessibility
selection friction
L2 basin capture
concern-weighted hardening
```

---

## 9. Self-coherence and boundary

The source links self-coherence to continuity across field deformation, not to persistence of a fixed inner core. This is a useful bridge to SRT's treatment of subjecthood.

SRT-compatible formulation:

> The self is not an unchanged substance behind selection. It is the continuity of selection-field deformation across time.

The source also treats self-boundary as historically regulated permeability rather than a sealed wall. This is compatible with SRT's view that subjecthood depends on stabilized yet permeable constraints:

```text
self-boundary = historically regulated constraint on what can perturb, enter, or reorganize the selection field
```

This gives SRT a better way to describe dissociation, depersonalization, derealization, trauma fragmentation, and relational co-regulation.

---

## 10. New SRT claim cluster

### Claim N11a: L2 as transition-field deformation

L2 should be understood not merely as memory, habit, prior, or schema, but as the historically sedimented deformation of selection reachability.

```text
L2 = historical deformation of the future selection field
```

### Claim N11b: Subjective time tracks transition accessibility

Subjective time dilation and compression may index the current reachability of adaptive transition in some regimes, but they are multi-process reports rather than a monotonic transition-accessibility meter.

```text
tau(t) = 1 / r(t)
```

SRT bridge:

```text
r(t) ≈ adaptive L1-transition accessibility under theta, d, Psi_f, and L2
```

### Claim N11c: Impaired action is attractor capture

Many forms of impaired action are better described as attractor capture in a historically shaped field than as lack of will or simple depletion.

```text
failure to act = inaccessible transition, not empty capacity
```

### Claim N11d: Measurement must be multimodal and longitudinal

SRT's key variables should not be sought as single local neural signatures. They should be estimated from coupled neural, autonomic, bodily, behavioral, environmental, mnemonic, and relational dynamics.

```text
SRT variable ≠ single neural marker
SRT variable = latent structure inferred from coupled transition dynamics
```

---

## 11. Experimental predictions

### N11-P1: subjective time dilation should covary with reduced transition accessibility

When adaptive transition becomes harder to initiate or complete, subjective time may dilate after action, expectation, attention, and perceptual-change contributions are controlled.

Possible measures:

```text
initiation latency
behavioral transition frequency
self-report of stuckness
time-estimation distortion
HRV / respiration / EDA / movement patterns
```

SRT prediction:

```text
lower r(t) -> candidate pressure toward higher tau(t)
```

This prediction is weakened if action-conditioned duration fails to covary with transition accessibility across preregistered replications; no duration result alone licenses a `Psi_f` inference.

### N11-P2: recovery from attractor capture should be nonlinear

If impaired action reflects attractor capture rather than simple depletion, recovery should often show threshold-like transitions.

Prediction:

```text
gradual physiological change + sudden behavioral reopening
```

rather than:

```text
gradual resource recovery + gradual action recovery
```

### N11-P3: relational co-regulation should change transition accessibility

If relational coupling is part of the transition field, predictable social presence, recognition, voice, rhythm, or support should measurably alter action readiness and subjective time.

Prediction:

```text
safe relational coupling -> increased r(t) -> reduced stuckness / time dilation
threatening relational coupling -> decreased r(t) or maladaptive capture
```

### N11-P4: L2 basin formation should alter future subjective time

Training, trauma, repeated success, repeated failure, or repeated safety should deform the field. This should change not only behavior but temporal experience in relevant contexts.

Prediction:

```text
low-friction trained basin -> time compression / flow
high-friction threat basin -> time dilation / freezing / looping
```

---

## 12. Boundary cautions

1. `r(t)` should not be equated with one biomarker such as HRV.
2. `tau(t)=1/r(t)` should be treated as a bridge formalism, not a total reduction of phenomenology.
3. SRT should not collapse `r(t)` directly into `Psi_f^{-1}`. The relation is approximate and context-dependent.
4. The transition-field model is useful for SRT, but SRT remains broader because it includes the L0-L1-L2 ontology, Ghost Operator, d-value, selection friction, and cross-scale hardening.
5. The framework must remain falsifiable: if subjective time distortion does not covary with transition accessibility across repeated measures, the bridge model is weakened.
6. Action-conditioned duration is multi-process: the Experiments 1-2 coupling effect was not stably reproduced in Experiments 3-4.

---

## 13. One-paragraph abstract

The transition-field model of mind offers a strong neuroscience-facing bridge for SRT. It treats mind not as a sealed inner container but as a historically shaped field of reachable transitions, continuously coupled to body, memory, environment, and relation. Its central relation, `tau(t)=1/r(t)`, interprets subjective time as the inverse of action-readiness or transition density: time dilates when adaptive transition becomes remote and compresses when transition becomes reachable. SRT can absorb this as a bridge model in which `r(t)` indexes adaptive L1-transition accessibility under theta, d-value, Psi_f, and L2 deformation. The model strengthens SRT's treatment of L2 as historical deformation of future selectability, impaired action as attractor capture, and measurement as multimodal longitudinal inference rather than localization of a single neural signal. It should not be treated as proof of SRT ontology, but as a powerful interface for operationalizing selection reachability, subjective time, self-coherence, and action failure.
