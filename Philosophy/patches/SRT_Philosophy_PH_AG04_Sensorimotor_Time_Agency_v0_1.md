---
id: SRT-PH-AG04-SENSORIMOTOR-TIME-AGENCY
type: material_patch
status: patch_v0_1
layer: bridge
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3/P4
canonical: false
patch_id: SRT-PH-AG04-SENSORIMOTOR-TIME-AGENCY
source_ids:
  - SRC-2026-07-16-COGNITIVE-IMAIZUMI-SENSORIMOTOR-TIME-AGENCY
domain: Philosophy of Mind / Cognitive Agency / Embodied Cognition / Subjective Time
target_future_doc:
  - Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
  - Neuroscience/SRT_Neural_Mechanisms.md
  - Neuroscience/SRT_Consciousness_Mechanisms.md
  - future subjective-time bridge document
related_claims:
  - selection is broader than agency
  - controlled transition-readiness
  - authorial coupling versus body ownership
  - theta as coupling protocol
  - embodied Psi_f perturbation
  - subjective duration as action-conditioned manifestation
  - shared agency boundary
  - d-value and L2 writeback requirements
tags: [agency, sensorimotor-coupling, subjective-time, body-ownership, authorship, prediction, embodiment, self-other]
---

# PH-AG04 — Sensorimotor Coupling, Subjective Time, and Agency Dissociation

## 1. Source anchor

Primary source:

- Shu Imaizumi, Giuseppe Lai, Anil K. Seth, and Keisuke Suzuki, *Sensorimotor Coupling Modulates Perceived Time and Agency Across Visual Perspectives*, *Collabra: Psychology* 12(1), 2026.
- DOI: `10.1525/collabra.164266`.
- Four preregistered VR experiments; full 28-page user-supplied paper close-read.
- SourceCard: `../../Materials/2026/SRC_2026_07_16_Cognitive_Imaizumi_Sensorimotor_Time_Agency.md`.

The paper manipulates delay, live versus replay kinematics, first- versus third-person visual perspective, anatomical configuration, action versus no action, and whether attention is directed onto or near a virtual hand. It measures duration judgment, sense of agency, and body ownership.

## 2. Why this matters for SRT

SRT already distinguishes causal transition, selection, controlled selection, agency, consciousness, subjecthood, and shared agency. The present evidence sharpens a further distinction that must be explicit inside the agency layer:

```text
control coupling
!=
authorial attribution
!=
body ownership
!=
reflective self-ownership
```

The experiments show that participants can experience control over a third-person avatar or an externally located virtual hand without equivalently experiencing the hand as part of their body. They also show that subjective duration and agency can covary in some conditions and dissociate in others.

This patch adds a P3/P4 bridge:

> **During online action, sensorimotor coupling is a candidate implementation of controlled transition-readiness, but its outputs divide into partially independent dimensions: control, authorship, body ownership, and action-conditioned duration. None of these dimensions alone establishes stake-bearing subjecthood or shared agency.**

The bridge does not redefine `G_hat_theta`, `Psi_f`, `d-value`, `L0/L1/L2`, or physical time.

## 3. Main SRT bridge claims

### PH-AG04.1 — Agency ownership must not default to body ownership

The phrase “self-coupled ownership” is ambiguous. It may refer to:

- ownership of the bodily carrier;
- authorship of the action;
- control over an outcome;
- reflective or narrative endorsement;
- responsibility for consequences.

The article provides direct evidence that body ownership and sense of agency respond differently to perspective and anatomical configuration. Therefore:

```text
sense of agency > 0
not implies
body ownership > 0
```

For SRT, conscious agency should use **authorial / control ownership** unless bodily ownership is specifically intended.

### PH-AG04.2 — Online control can extend beyond the represented body

Synchronous action–feedback relations can support agency over an avatar seen from a third-person perspective or over a visually external object. A normal first-person body image is not always necessary for control coupling.

This supports a bounded coupling-protocol reading:

```text
theta_action
~
protocol organizing motor output, predicted return, actual feedback, and correction
```

It does not show that all cognition is non-representational, and sensorimotor coupling is not identical to `G_hat_theta`.

### PH-AG04.3 — Subjective duration is not a direct meter of agency or coupling

Experiments 1 and 2 found relatively longer perceived duration under stronger sensorimotor coupling, but Experiments 3 and 4 did not reliably reproduce the kinematics effect on duration. Agency remained sensitive to coupling manipulations in conditions where duration did not.

Therefore:

```text
subjective duration
!=
monotonic agency index
!=
monotonic coupling index
```

A safer model is that action execution, feedback congruence, prediction, attention, perceptual change, and retrospective inference jointly contribute to duration experience.

### PH-AG04.4 — Congruent feedback may compensate action-related time compression

The no-action baseline in Experiment 2 shows that voluntary action itself compresses perceived duration relative to no movement. Live congruent feedback makes duration relatively longer than replay feedback but does not necessarily raise it above the no-action baseline.

The stable bridge is therefore:

```text
action execution -> compression pressure
sensorimotor congruence -> partial counter-pressure
observed duration -> net result of multiple processes
```

Do not state that synchronous coupling simply “creates temporal dilation.”

### PH-AG04.5 — Sensorimotor mismatch is a perturbation of embodied anchoring, not `Psi_f` itself

Delay, replay kinematics, and randomized spatial mappings can be used as experimental perturbations of embodied re-anchoring. They may increase correction demand or reduce effective control.

However:

```text
feedback mismatch
!=
Psi_f^emb
```

A `Psi_f^emb` bridge requires independent cost-sensitive measures such as correction latency, control error, adaptation rate, aftereffect, metabolic demand, or persistent loss of reachable action.

### PH-AG04.6 — Third-person synchronous action is not shared agency

A third-person avatar whose movements are driven by the participant can be an external actuator. Similar modulation across perspectives supports a domain-general or self–other-overlapping predictive computation, but not necessarily another subject.

```text
externally located controlled object
!=
autonomous other
!=
shared agency
```

Shared agency still requires reciprocal constraint, independent goals, mutual prediction, role structure, joint commitment, norm repair, or another durable intersubjective `L2` scaffold.

### PH-AG04.7 — The study does not test `d-value` or subjecthood

The task has low consequence, limited irreversibility, and no systematic manipulation of threat to viability or future option structure. It therefore does not distinguish prediction error from stake-bearing relevance.

```text
agency report
not implies
d > 0
not implies
subjecthood
```

The evidence belongs at the controlled-action and conscious-report bridge layers, not at the subjecthood threshold.

## 4. Mapping table

| Empirical construct | SRT bridge use | Boundary |
|---|---|---|
| synchronous live feedback | effective online control coupling | not `G_hat_theta` definition |
| 500 ms feedback delay | perturbation of prediction/action return | not a scalar `Psi_f` measure |
| replayed other kinematics | reduced self-specific action–feedback fit | not proof of other-agency processing |
| first-person perspective | bodily self-location cue | not necessary for control coupling |
| third-person avatar | externalized control target / possible self–other prediction overlap | not shared agency |
| normal anatomy | body-form congruence | not necessary for every agency experience |
| randomized anatomy | spatial mapping perturbation | not absence of all coupling |
| sense of agency rating | explicit control/authorship report | vulnerable to expectations and suggestibility |
| body ownership rating | bodily carrier attribution | not equivalent to authorship |
| duration judgment | action-conditioned temporal experience | not physical time or direct selection count |
| no-action baseline | separates action compression from coupling effect | not an unconditioned metaphysical time baseline |

## 5. Formal bridge

### 5.1 A multidimensional action-self vector

Let an online action episode be described by:

\[
\mathbf{A}_t=
\left(
C_t,
U_t,
B_t,
R_t
\right)
\]

where:

- `C_t`: control efficacy — can the system modulate the outcome?
- `U_t`: authorial attribution — is the outcome attributed to one’s action?
- `B_t`: body ownership — is the carrier experienced as part of one’s body?
- `R_t`: reflective integration — is the action available for report, endorsement, responsibility, or revision?

The article supports non-identity among these components:

\[
C_t \not\equiv U_t \not\equiv B_t \not\equiv R_t
\]

The notation is diagnostic only and is not a new canonical agency definition.

### 5.2 Sensorimotor coupling state

Let:

- `m_t`: motor command / executed motion;
- `\hat{s}_{t+\delta}`: predicted sensory return;
- `s_{t+\delta}`: actual sensory return;
- `\Delta`: externally introduced delay;
- `K`: kinematic match;
- `M`: spatial/body-form mapping;
- `Q`: corrective controllability.

A schematic coupling state is:

\[
C_{sm,t}=F\!\left(
\operatorname{match}(\hat{s}_{t+\delta},s_{t+\delta}),
\Delta,
K,
M,
Q
\right)
\]

This is a bridge scaffold. The paper does not estimate a universal coupling scalar.

### 5.3 Multi-process subjective duration

A bounded schematic is:

\[
\Delta T_{subj}
=
-\beta_{act}A_{exec}
+\beta_{sm}C_{sm}
+\beta_{exp}E_{exp}
+\beta_{att}A_{att}
+\beta_{chg}N_{change}
+\varepsilon
\]

where:

- `A_exec`: action-related compression pressure;
- `C_sm`: sensorimotor congruence contribution;
- `E_exp`: prospective expectation and retrospective causal inference;
- `A_att`: attentional allocation;
- `N_change`: accumulated salient perceptual change.

This equation is not fitted by the source paper and must not be quoted as an empirical law. Its role is to prohibit one-factor readings.

### 5.4 Embodied-friction measurement gate

A candidate embodied re-anchoring cost vector is:

\[
\mathbf{F}^{emb}_t=
\left(
L_{corr},
E_{ctrl},
R_{adapt},
H_{after},
C_{met},
O_{lost}
\right)
\]

with:

- `L_corr`: correction latency;
- `E_ctrl`: residual control error;
- `R_adapt`: adaptation / recalibration rate;
- `H_after`: aftereffect or hysteresis after perturbation removal;
- `C_met`: physiological or metabolic cost;
- `O_lost`: loss of reachable future options.

Only after such measures are linked to the perturbation should a `Psi_f^emb` interpretation be considered.

## 6. New claim cluster

### PH-AG04-A — Control can be externally located

A system may experience agency over an external tool, avatar, cursor, or remote effector when its action–feedback loop is sufficiently controllable and predictable.

### PH-AG04-B — Bodily self and action self are dissociable

Body ownership provides one route to self-related agency but is neither identical to nor always necessary for authorial control.

### PH-AG04-C — Temporal experience is action-structured but not agency-reducible

Voluntary action alters subjective duration, yet the temporal result is not reducible to the explicit sense of controlling the action.

### PH-AG04-D — Generic prediction does not erase domain distinctions

A common predictive architecture may operate across self-body, tool, avatar, and perceived other. SRT should preserve distinctions among the controlled carrier, consequence bearer, autonomous other, and shared coordination structure.

### PH-AG04-E — Time effects require replication before theoretical load-bearing

The kinematics effect on duration appeared in Experiments 1–2 but not clearly in Experiments 3–4. It may serve as an experimental window, not a hardened SRT prediction.

### PH-AG04-F — Subjective report and structural control require separate evidence

Sense-of-agency ratings are useful but may reflect task expectations. Structural evidence should include counterfactual control, correction, adaptation, and perturbation-sensitive performance.

## 7. Experimental / operational consequences

### 7.1 Replication ladder

A direct replication should pre-register separate hypotheses for:

1. action-related time compression;
2. live-feedback compensation;
3. delay effect;
4. kinematic replay effect;
5. perspective null effect;
6. agency / body-ownership dissociation.

Use larger multisite samples and report both estimation uncertainty and Bayes factors.

### 7.2 Separate control, authorship, and ownership

Use independent measures:

- objective controllability and intervention success;
- explicit authorship judgment;
- body ownership rating;
- intentional binding or causal attribution;
- confidence and metacognitive access;
- responsibility assignment under consequence.

### 7.3 Add stake and reversibility

Cross:

\[
\text{coupling mismatch}
\times
\text{stake}
\times
\text{reversibility}
\]

Examples:

- no consequence;
- reversible reward loss;
- persistent loss of later action options;
- errors borne by self versus another participant.

Measure whether equal sensory mismatch produces different correction, exploration, retention, and option-preservation dynamics.

### 7.4 Test `L2` writeback

Measure:

- recalibration across blocks;
- aftereffects when normal feedback returns;
- retention after hours or days;
- transfer to a new effector or visual perspective;
- path dependence after repeated mismatch.

This distinguishes immediate `L1` report from stabilized history-dependent change.

### 7.5 Replace simulated other with genuine other

Compare:

1. prerecorded avatar;
2. live but mechanically yoked avatar;
3. adaptive agent with independent policy;
4. human partner with reciprocal goals and communication;
5. joint task requiring norm repair and role coordination.

This can test the transition from external control coupling to shared agency.

## 8. Boundary cautions

1. Do not claim the article proves SRT.
2. Do not claim subjective time is generated solely by sensorimotor coupling.
3. Do not infer physical-time ontology from duration estimation over 1.8–2.2 seconds.
4. Do not equate sense of agency with body ownership.
5. Do not equate a controlled third-person avatar with an autonomous other.
6. Do not call delay, replay, or mapping mismatch `Psi_f` without cost-sensitive measurements.
7. Do not infer `d-value`, consciousness, or subjecthood from agency ratings alone.
8. Do not treat the time result as fully replicated across all four experiments.
9. Preserve demand-characteristic and phenomenological-control cautions for subjective reports.
10. Preserve the possibility that some offline or counterfactual tasks require internal representations beyond live coupling.

## 9. Integration hook

Future target:

```text
Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md
```

Suggested insertion after the agency ladder and before conscious agency:

> SRT should distinguish control coupling, action authorship, body ownership, and reflective self-integration. Sensorimotor congruence can produce control over an externally located avatar without producing equivalent bodily ownership. Conscious agency therefore requires self-related authorial integration, not necessarily ownership of the bodily carrier used in a given task. Subjective duration may covary with this coupling, but it is a multi-process action-conditioned experience and not a direct measure of agency, selection, or embodied friction.

Do not include:

```text
agency = body ownership
subjective duration = selection cost
feedback mismatch = Psi_f
third-person synchrony = shared agency
sensorimotor coupling proves selection-before-existence
```
