---
patch_id: PATCH-NEURO-NEURAL23-EMBODIED-RHYTHMIC-ELIGIBILITY
source_ids:
  - SRC-2026-06-27-NEURO-YOUNG-BRAIN-BODY-SYNCHRONY-CONSCIOUSNESS
domain: neuroscience_consciousness_interoception_brain_body_rhythms
claim_level: bridge
authority_level: bridge_support
canonical_status: non_canonical
status: active
target_documents:
  - "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
  - "Neuroscience/SRT_Neuro_Predictions_Table.md"
  - "Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md"
related_claims:
  - embodied_selection_implementation
  - momentary_selection_eligibility
  - phase_dependent_gating
  - selection_weight_opportunity_friction
  - G_hat_theta_implementation_bridge
  - d_value_stake_channel_boundary
  - Psi_f_payability_proxy_boundary
  - consciousness_bearer_unit
  - subjecthood_unit_binding
tags: [brain_body, synchrony, interoception, respiration, heartbeat, gastric, phase_gating, eligibility, consciousness, embodiment]
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_patch
id: PATCH-NEURO-NEURAL23-EMBODIED-RHYTHMIC-ELIGIBILITY
---

# SRT Neuroscience Patch NEURAL23: Embodied Rhythmic Eligibility v0.1

> **Status**: bounded P3 neuroscience implementation bridge with P4 experimental consequences.  
> **Canonical caution**: this patch does not define `L_0`, `L_1`, `L_2`, `G_hat_theta`, `d`, `Psi_f`, `T_dir`, consciousness, subjecthood, or the origin of selectability. It introduces a domain-level candidate mechanism for how bodily rhythms may modulate momentary access to neural selection.

## 0. Source anchor

- Asa Young, Marissa Ericson, and Jonathan W. Schooler. “I sync, therefore I am: brain-body synchrony in typical and disordered consciousness.” *Neuroscience of Consciousness* 2026(1): niag028. DOI: `10.1093/nc/niag028`.
- SourceCard: `Materials/2026/SRC_2026_06_27_Neuro_Young_Brain_Body_Synchrony_Consciousness.md`.

## 1. Why this matters for SRT

Current neural SRT separates accessible candidates, competition, gain, gating, stabilization, manifest anchoring, and later `L1 -> L2` hardening. The reviewed brain-body literature adds a missing implementation question:

> Is the probability that a candidate enters or wins the selection process continuously modulated by the organism's current rhythmic state before manifest anchoring occurs?

The strongest bridge evidence is not merely that respiration changes response time. Reviewed decision-model results indicate that respiratory phase can alter evidence-accumulation parameters such as decision boundary or starting point. This motivates a bounded distinction between:

```text
what is accessible
and
what is momentarily eligible for selection
```

without inserting a new canonical layer between `L_0` and `L_1`.

## 2. Main bridge claim

### Claim NEURAL23 — momentary embodied eligibility

For a candidate neural/perceptual/action state `x`, introduce a bridge-level eligibility function:

\[
E_t(x) \in [0,1],
\]

where `E_t(x)` represents the momentary probability-shaping contribution of current embodied temporal state to candidate admission, competition, or stabilization.

A schematic implementation is:

\[
E_t(x)
=
F_E\!\left(
\phi_H(t),
\phi_R(t),
\phi_G(t),
C_{BH}(t),
C_{BR}(t),
C_{BG}(t),
A(t),
\theta,
x
\right),
\]

with cardiac phase `phi_H`, respiratory phase `phi_R`, gastric phase `phi_G`, selected coupling measures `C`, arousal/state variable `A`, and implementation parameters `theta`.

The resulting SRT-facing bridge is:

\[
P(x \to L_1)
=
F_{sel}\!\left(
W(x),
E_t(x),
\Psi_{proxy}(x,t),
\theta,
L_2
\right).
\]

Every term here is bridge/lab notation. `E_t` is not a new canonical variable, `Psi_proxy` is not canonical `Psi_f`, and the equation does not redefine `G_hat_theta`.

## 3. Selection weight, opportunity, and friction

NEURAL23 recommends a neuroscience-facing decomposition:

```text
selection weight
!= selection opportunity
!= selection friction
```

### Selection weight

`W(x)` asks why a candidate is prioritized: salience, prior, goal, threat, reward, or stake-related meaning may contribute.

### Selection opportunity

`E_t(x)` asks whether the candidate has a favorable momentary admission window under current brain-body timing and state.

### Selection friction

`Psi_proxy(x,t)` asks what burden, conflict, switching cost, recovery demand, or support requirement accompanies stabilization in the declared experiment.

This separation protects against the shortcut:

```text
high d -> automatic conscious access
```

A high-stake candidate may have high weight while its momentary opportunity is poor, or may enter rapidly but require high downstream recovery cost.

## 4. Pre-anchoring eligibility versus post-anchoring plasticity eligibility

NEURAL23 should remain explicitly distinct from N10/BTSP eligibility traces.

```text
NEURAL23:
L0_accessible
-> momentary selection eligibility
-> neural competition / gating / stabilization
-> L1

N10 / BTSP:
L1 event / activity history
-> plasticity eligibility trace
-> trigger / plateau
-> L2 write-back
```

Compact guardrail:

```text
eligibility to become current reality
!=
eligibility to enter history
```

This distinction creates a testable separation between conscious/access priority and long-term sedimentation rather than assuming they covary monotonically.

## 5. Continuous constraint shaping and discrete anchoring

The source pressures an overly event-like reading of neural selection. Brain-body phase, gain, threshold, and cross-frequency coupling can change continuously before a discrete report, decision, or stable percept appears.

A safer neural implementation picture is:

```text
continuous constraint shaping
-> momentary eligibility profile
-> competition / gating
-> relatively discrete anchoring commitment
```

Thus:

```text
discrete selection event
!=
discrete implementation dynamics
```

This prevents SRT from searching for a single `selection neuron`, anatomical chooser, or one universal collapse instant.

## 6. Bodily information versus bodily coordination

The review supports keeping two possible functions separate:

```text
body as represented interoceptive information
!=
body as shared temporal constraint for coordination
```

The second function is especially relevant to SRT because a variable can shape what becomes selectable without itself becoming the selected content.

A bounded SRT bridge is:

> Some bodily rhythms may function as temporal coordination infrastructure for distributed selection processes, even when their role is not exhausted by explicit interoceptive representation.

The reviewed literature does not yet establish whether stress-related coupling increases primarily improve interoceptive awareness, distributed coordination, both, or neither.

## 7. Synchrony guardrail

Physiological synchrony remains a domain-specific mechanism term. It must not be promoted back into a cross-domain SRT primitive.

```text
synchrony
!= coordination quality
!= selection
!= anchoring
!= d-value
!= Psi_f
!= consciousness
!= subjecthood
```

More precisely:

```text
synchrony is one possible coordination mechanism;
coordination can also be implemented by alternation, inhibition, routing,
anti-phase organization, multiplexing, asymmetric coupling, or other dynamics.
```

This patch therefore does **not** revive the earlier cross-domain `selective resynchronization` construct. Current repository terminology continues to use `选择性再组织 / selective reorganization` for general cross-level processes, while `synchrony` is reserved for measurable domain-specific coupling where appropriate.

## 8. Relation to `d`

The source does not measure stake-coupled irreversible-risk sensitivity or consequence return. Therefore:

```text
brain-body coupling != d
HEP amplitude != d
interoceptive precision != d
arousal != d
```

A permitted P3 interpretation is narrower:

> Interoceptive and brain-body coupling may be one implementation channel through which organism-level stake changes neural selection weighting or eligibility.

A stronger claim requires showing that the manipulated variable changes consequence-sensitive selection for the same bearer and alters future selection capacity.

## 9. Relation to `Psi_f`

Coupling magnitude is not a friction measure.

The same coupling increase may be:

- adaptive and temporary;
- compensatory under demand;
- rigid and pathological;
- epiphenomenal;
- correlated with a third state variable.

Therefore the stronger SRT-facing experimental object is:

```text
coupling state
x task/stake condition
x load
x budget
x recovery
x future transition capacity
```

rather than `coupling -> Psi_f`.

The authors' optimal-coupling conjecture is better translated into a P4 SRT question about **adaptive coupling repertoire and switchability**, not a universal optimum scalar.

## 10. Bearer-unit and consciousness boundary

Heartbeat-locked neural measures can contain consciousness-relevant information, including in disorders of consciousness. The permitted bridge is:

```text
body-referenced neural dynamics contain consciousness-relevant information
```

not:

```text
body coupling constitutes consciousness
```

The evidence makes the whole organism a serious candidate bearer unit relative to cortex-only default assumptions, but it does not by itself derive the bearer unit.

Interpersonal synchrony is even more strongly bounded:

```text
A <-> B coupling
!=
new bearer AB
```

Collective or dyadic subjecthood would still require a specified unit plus closure, consequence return, memory/history, boundary maintenance, and future-selectability evidence under the existing subjecthood interface.

## 11. Claim cluster

- **NEURAL23a — momentary eligibility:** bodily phase can be modeled as a candidate modifier of momentary selection opportunity before `L1` anchoring.
- **NEURAL23b — candidate specificity:** phase effects may interact with stimulus, affective meaning, task, or action type rather than acting as one global excitability scalar.
- **NEURAL23c — two eligibility gates:** selection eligibility and plasticity eligibility must be experimentally separated.
- **NEURAL23d — coordination without representation:** bodily rhythms may coordinate distributed processes without their role being exhausted by explicit body-state content.
- **NEURAL23e — coupling non-monotonicity:** more coupling is not automatically better selection, greater consciousness, or healthier organization.
- **NEURAL23f — adaptive repertoire:** pathology may involve reduced accessibility between coupling configurations or high switching/recovery cost rather than only abnormal mean coupling.
- **NEURAL23g — distributed implementation:** measurable brain-body dynamics support a distributed implementation reading of `G_hat_theta`, not a fixed biological selector.

## 12. P4 experimental consequences

### H-NEURAL23a: phase x stake interaction

Hold physical stimulus properties as constant as possible while manipulating consequence-bearing meaning or future-task stakes. Model:

\[
Outcome
\sim
Phase
+
StakeProxy
+
Phase\times StakeProxy
+
ArousalControls
+
DecisionControls.
\]

Primary interest is the preregistered `Phase x StakeProxy` interaction, not the already-plausible main effect of phase.

Candidate outcomes:

- drift-diffusion decision boundary / starting point;
- accuracy and reaction time;
- confidence;
- EEG / HEP measures;
- later memory;
- post-task recovery.

Failure condition:

If arousal, interoceptive precision, ordinary decision-model parameters, or standard autonomic variables fully explain the interaction and SRT stake variables add no incremental prediction, narrow the bridge.

### H-NEURAL23b: matched coupling, different recovery

Match or statistically control coupling magnitude across conditions, then test whether load, recovery half-life, behavioral rigidity, and later adaptation differ.

Prediction:

```text
same coupling magnitude
can coexist with
different payability / recovery profiles
```

Failure condition:

If coupling magnitude alone robustly predicts the relevant outcomes across replications, the added payability decomposition has limited value in that domain.

### H-NEURAL23c: state-switch accessibility

Estimate transitions among brain-body coordination states rather than only mean synchrony. Test whether anxiety/stress-related pathology is better predicted by:

- coupling magnitude alone;
- state repertoire size;
- transition entropy;
- exit latency from threat-related states;
- recovery after perturbation.

SRT-compatible result:

Reduced transition accessibility or elevated switching cost predicts persistence beyond mean coupling.

### H-NEURAL23d: selection eligibility versus write-back eligibility

Use a task with repeated phase-tagged stimuli and delayed memory. Test whether phase effects on immediate access/decision and later memory can dissociate.

A dissociation would support keeping:

```text
pre-anchoring eligibility
!=
post-anchoring plasticity eligibility
```

without claiming that either measure is canonical `d` or `Psi_f`.

## 13. Brain-in-a-vat pressure test

The source motivates but does not settle a distinction between:

### Input-equivalence model

Artificial reproduction of body-like input statistics is sufficient for the relevant consciousness organization.

### Closed-loop embodiment model

The relevant organization depends on a live loop in which action changes bodily state, bodily state changes future selection conditions, and consequences return to the same bearer.

A future SRT test should compare open-loop replay with consequence-bearing closed-loop perturbation while controlling sensory statistics. This is a P4/P5 research seed, not evidence from the reviewed paper.

## 14. Boundary cautions

1. This is a review article; most component findings originate in cited studies and should be traced to originals before fine-grained causal claims.
2. Many reviewed phenomena concern cognition, affect, or interoception indirectly related to consciousness.
3. HEP prediction does not establish HEP constitution of consciousness.
4. Respiratory phase effects on decision parameters do not establish a universal bodily selector.
5. Cross-frequency synchrony is not a universal measure of coordination.
6. The optimal-coupling window is an ancillary conjecture.
7. Stress-related coupling increase is not automatically adaptive.
8. Pairwise or triadic statistical directionality does not locate the full causal architecture.
9. Interpersonal synchrony does not establish collective subjecthood.
10. `E_t(x)` is bridge notation only and must not enter the canonical symbol table absent a separate hardening decision.
11. `d`, `Psi_f`, `T_dir`, `L_2`, and `G_hat_theta` retain their current authorities.
12. The earlier ML selective-resynchronization NO-GO result is not rescued or overridden by this biological literature.

## 15. Integration hook

`Neuroscience/hooks/NEURAL23_Embodied_Rhythmic_Eligibility_Integration_Hook.md`

## 16. Abstract

NEURAL23 introduces momentary embodied eligibility as a P3 neuroscience implementation bridge: cardiac, respiratory, gastric, and cross-system temporal state may change when and how candidate states enter neural competition, gating, and stabilization before `L1` anchoring. The patch distinguishes selection eligibility from N10-style plasticity eligibility, bodily information from bodily coordination, and physiological synchrony from selection, `d`, `Psi_f`, consciousness, and subjecthood. Its main P4 differential prediction is a preregistered `body phase x stake` interaction with explicit arousal, decision-model, recovery, and future-transition controls. The patch does not modify canonical SRT and does not revive selective resynchronization as a cross-domain construct.
