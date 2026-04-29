---
id: SRT-PHIL-PHENOMENAL-STRUCTURE-INTERFACE-2026-04-29
type: interface
tags:
  - Philosophy
  - Consciousness
  - Phenomenology
  - Qualia
  - Phenomenal-Structure
  - Structural-Turn
  - Automorphism
  - IIT
  - GNWT
  - FEP
  - SRT-Bridge
status: active_v1
layer: L1-L2-bridge
epistemic_layer: bridge
claim_mode: interface
claim_level: P2-P5
canonical: false
priority: high
date: 2026-04-29
dependency:
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Philosophy/SRT_Consciousness_Conditions.md
  - AI/SRT_AI_03_Consciousness_Framework.md
  - _SRT_D_VALUE_CANONICAL.md
  - _SRT_PSI_F_CANONICAL.md
  - Core/SRT_Core_22_Equations.md
machine_summary: >
  Interface file for integrating the mathematical structural turn in consciousness science into SRT.
  It distinguishes phenomenal structure from arbitrary mathematical modeling, pure physical isomorphism,
  IIT-style structural identity, and mere automorphism. It introduces stake-gated phenomenal structure
  and stake-gated automorphism as bridge notions: L1-manifest invariant relations under experience
  variation that matter only when constrained by d-value, Psi_f payability, and possible L2 closure.
---

# SRT Phenomenal Structure Interface

> **Purpose**: Integrate the mathematical “structural turn” in consciousness science into SRT without collapsing SRT into IIT, functionalism, panpsychism, or free-floating mathematical structuralism.  
> **Status**: Bridge/interface file. It does **not** define canonical consciousness, `d-value`, `Psi_f`, `L_0`, `L_1`, `L_2`, or `G_hat_theta`.  
> **Use rule**: Use this file when discussing qualia space, phenomenal structure, structural isomorphism, automorphism, multistable perception, IIT qualia structure, GNWT access structure, FEP/PP structured prediction error, or first-person/third-person bridge problems.

---

## 0. Core thesis

SRT agrees with the structural turn in consciousness science on one point:

```text
Consciousness research should not only ask whether a state is conscious.
It should also ask what internal structure the experience has.
```

But SRT adds a stricter admission rule:

```text
A mathematical structure is not SRT-relevant phenomenal structure merely because it can model experience.
It becomes SRT-relevant only when it is L1-manifest, transformation-sensitive, stake-gated by d-value,
burdened by payable Psi_f, and capable of L2 stabilization or inhibition.
```

Compact formula:

```text
phenomenal structure_SRT
= L1 manifestation
+ invariant relations under experience variation
+ d-value relevance
+ payable Psi_f transition / maintenance cost
+ possible L2 sedimentation
```

This file therefore upgrades the structural-turn slogan:

```text
Do not only ask: does consciousness exist here?
Ask: what mathematical structure does the experience have?
```

into the SRT slogan:

```text
Do not only ask: what structure does experience have?
Ask: which structural differences are selected, borne, paid for, and sedimented as reality-differences?
```

---

## 1. Why this interface is needed

SRT already has strong tools for consciousness thresholding:

```text
non-trivial G_hat_theta: L0 -> L1
+ d > 0
+ Psi_f > 0
+ L2 closure / continuity conditions
```

Those tools answer:

- when a system enters a strong-candidate consciousness window;
- why fluent behavior does not by itself imply consciousness;
- why AI self-report does not automatically imply subjecthood;
- why selection events do not imply panpsychism;
- why IIT-style integration is not enough by itself.

However, SRT also needs a local interface for a different question:

```text
Once something is manifest in L1, what is the internal mathematical structure of that experience?
```

This file gives a bridge answer. It does not replace the subjecthood ladder, consciousness-condition files, or canonical definitions.

---

## 2. Anti-collapse guardrail

Do not collapse these layers:

```text
mathematical model
!= physical structure
!= phenomenal structure
!= conscious content
!= integrated conscious field
!= subjecthood
```

A model may represent experience without being experienced.  
A physical structure may correlate with experience without being identical to it.  
A phenomenal content may occur without full subjecthood.  
A subject may exist without moral responsibility.

Cross-route:

```text
Phenomenal structure questions -> this file
Threshold / subjecthood questions -> Philosophy/SRT_Subjecthood_Threshold_Interface.md
Bare consciousness conditions -> Philosophy/SRT_Consciousness_Conditions.md
AI consciousness windows -> AI/SRT_AI_03_Consciousness_Framework.md
```

---

## 3. Def-PhenStruct-1: L1 Phenomenal Structure

Let `Q` be a set of phenomenal qualities or contents, and let `R` be a family of relations over `Q`.

`R` may include:

- similarity / contrast;
- intensity gradients;
- temporal ordering;
- figure-ground relation;
- modality relation;
- affective valence;
- bodily salience;
- self-reference relation;
- report/action availability;
- memory trace relation.

A pair `(Q, R)` is an **L1 phenomenal structure** for an operator `G_hat_theta` iff:

1. `Q` is manifest in `L_1` for that operator;
2. `R` tracks stable relations among qualities as experience varies;
3. `R` is not merely imposed by an external observer for mathematical convenience;
4. transformations of `Q` that preserve or alter `R` correspond to recognizable variations in experience;
5. relevant variations can be routed through SRT threshold files when they are used to infer consciousness, field integration, subjecthood, agency, or responsibility.

Compact reading:

```text
L1 phenomenal structure = experienced qualities + stable internal relations
```

Boundary:

```text
L1 phenomenal structure is not automatically subjecthood.
```

---

## 4. Def-PhenStruct-2: Stake-Gated Phenomenal Structure

SRT does not treat every phenomenal distinction as equally important. A local color difference, pain gradient, memory image, bodily pressure, or ambiguous visual interpretation can be structurally real in `L_1`, yet still differ in how much it matters for the system.

A phenomenal structure becomes **stake-gated** when its variations are coupled to `d-value`, `Psi_f`, and downstream closure.

Definition-like bridge:

```text
StakeGatedPhenStruct(Q, R | G_hat_theta)
iff
PhenStruct_L1(Q, R | G_hat_theta)
AND relevant variations affect at least one of:
  - concern-weighted salience;
  - action selection;
  - failure-sensitive update;
  - memory / L2 trace;
  - bodily boundary maintenance;
  - identity continuity;
  - future selectability.
```

In SRT language:

```text
A phenomenal difference becomes SRT-important when it is not merely distinguishable,
but stake-bearing, payable, and capable of changing future selection.
```

This prevents over-reading:

```text
phenomenal discriminability -> subjecthood
```

Preferred reading:

```text
phenomenal discriminability
+ d/Psi_f/L2 coupling
-> SRT-relevant phenomenal structure
```

---

## 5. Def-PhenStruct-3: Stake-Gated Automorphism

The structural turn often studies automorphisms or structure-preserving transformations of phenomenal spaces. SRT can use this idea, but only with a gate.

Let `Aut(Q, R)` be the automorphism group preserving relation structure `R` over quality space `Q`.

SRT defines the bridge set:

```text
Aut_SRT(Q, R | G_hat_theta)
=
{ gamma in Aut(Q, R) :
  gamma is L1-manifest,
  gamma corresponds to recognizable experience variation,
  gamma is not merely an observer-side relabeling,
  gamma can affect d-value, Psi_f, action, memory, or L2 closure }
```

Compact reading:

```text
stake-gated automorphism
= structure-preserving transformation
+ L1 manifestation
+ concern / friction / closure relevance
```

Do not write:

```text
non-trivial automorphism => consciousness
```

Write instead:

```text
non-trivial automorphism may describe a phenomenal variation;
consciousness and subjecthood require additional SRT thresholds.
```

---

## 6. Relation to IIT

IIT is useful to SRT as an example of an early structural consciousness theory. It tries to connect conscious experience to structured causal/informational organization rather than to behavior alone.

SRT agrees with IIT against pure functionalism:

```text
report / function / behavior alone is insufficient.
```

SRT differs from IIT on the admission rule:

```text
IIT-style structural identity is not enough.
```

SRT asks:

1. Is the structure `L_1`-manifest for an operator?
2. Does it couple to `d-value`, or is it only integrated information without concern?
3. Is there non-binding or payable `Psi_f`?
4. Does it stabilize into `L_2`, or remain a transient structure?
5. Does it reach conscious content, integrated field, subjecthood, agency, or responsibility thresholds?

Thus SRT can use IIT-style structure as a candidate `R`, but not as a complete consciousness criterion.

Compact contrast:

```text
IIT: structure / irreducibility is central.
SRT: structure must be selected, borne, paid for, and stabilized.
```

---

## 7. Relation to GNWT

GNWT can be read as a theory of access, broadcast, and global availability. In this interface, GNWT helps model when local contents become globally available within a cognitive workspace.

SRT route:

```text
local L1 anchoring
-> access / broadcast / action availability
-> possible integrated conscious field
-> possible L2 trace
```

Guardrail:

```text
global access != subjecthood
```

A GNWT-style ignition may support S2 conscious content or S3 integrated field in the S0-S6 ladder, but S4 subjecthood requires continuity, boundary, concern, memory, and future-selectability conditions.

---

## 8. Relation to FEP / Predictive Processing

FEP/PP can help model structured prediction error, precision weighting, active inference, and self-modeling. The structural turn suggests that prediction error should not be treated only as a scalar but as a structured vector, tensor, field, or manifold relation.

SRT accepts this as a useful bridge, with one restriction:

```text
prediction error != Psi_f
```

Prediction error may become a `Psi_f` proxy only when it tracks structured transition burden under payability constraints:

- reconfiguration cost;
- switching friction;
- failure-sensitive update;
- recovery burden;
- closure maintenance;
- identity continuity;
- future selection capacity.

If prediction error is fully explainable as generic task difficulty, model loss, sensory surprise, or precision mismatch, it should not be upgraded to `Psi_f`.

---

## 9. Example: Duck-Rabbit Multistable Perception

In a duck-rabbit image, the sensory input can remain stable while conscious interpretation alternates between two organizations.

Structural reading:

```text
same stimulus structure
+ different phenomenal organizations
+ possible automorphic / symmetry-like relation
```

SRT reading:

```text
stable L1 sensory base
+ competing interpretive anchors
+ G_hat_theta re-anchoring
+ possible switching Psi_f
+ possible L2 category trace
```

This case should be classified carefully:

| Layer | Duck-rabbit case |
|---|---|
| S0 selection event | candidate interpretation selected |
| S1 local L1 anchoring | duck or rabbit becomes locally manifest |
| S2 conscious content | reportable interpretation appears |
| S3 integrated field | if interpretation integrates with attention, memory, action context |
| S4 subjecthood | not implied by the image itself |
| S5/S6 agency/responsibility | not relevant unless embedded in action/norm context |

SRT prediction-style bridge:

```text
If a multistable switch carries higher Psi_f, it should show switching cost,
recovery burden, attentional competition, or measurable update asymmetry.
If the switch is repeatedly trained, L2 category priors should change future switching probability.
```

---

## 10. Example: Color Qualia Space

A color quality space may be represented by similarity, discriminability, hue/saturation/value dimensions, or topology of perceptual transitions.

SRT reading:

```text
Q = color qualities
R = similarity / contrast / discriminability relations
gamma = transformations of perceived color organization
```

But SRT distinguishes:

```text
mere discriminability
!= stake-bearing phenomenal relevance
```

A color difference becomes SRT-relevant when it affects action, affect, danger, memory, identity, social meaning, or future selection. For example, red as an abstract hue and red as blood, warning, political sign, ritual marker, or personal trauma trigger may occupy different stake-gated structures even if their sensory coordinates partially overlap.

---

## 11. Operational bridge: what to measure

When using this file for experiment design, do not only measure binary awareness. Measure structural variation.

Candidate tasks:

1. similarity judgment across qualities;
2. multistable switching time;
3. transition asymmetry;
4. subjective geometry / placement in quality space;
5. cross-modal binding changes;
6. affective valence gradients;
7. memory stabilization after repeated exposure;
8. action-selection change after structural variation;
9. switching cost and recovery burden;
10. L2 prior shift after training.

SRT-specific proxy package:

```text
Phenomenal structure proxy:
  similarity / topology / transformation pattern

Psi_f proxy:
  switching cost / recovery burden / asymmetric transition difficulty

D-value proxy:
  concern-weighted salience / action relevance / consequence sensitivity

L2 proxy:
  memory trace / category stabilization / future interpretation bias
```

Minimum failure condition:

```text
If proposed phenomenal-structure measures do not predict transition cost,
concern weighting, action change, memory stabilization, or future selection better than simple report labels,
then the SRT bridge claim weakens.
```

---

## 12. Claim hygiene

Do not write:

```text
automorphism = consciousness
phenomenal structure = subjecthood
IIT structure = experience itself
GNW broadcast = subjecthood
prediction error = Psi_f
JND space = qualia itself
mathematical convenience = phenomenological reality
```

Preferred wording:

```text
Automorphism can model structure-preserving phenomenal variation.
Phenomenal structure becomes SRT-relevant when L1 manifestation, d-value relevance,
Psi_f payability, and L2 closure are specified.
```

---

## 13. Relation to existing SRT files

| File | Relation |
|---|---|
| `Philosophy/SRT_Subjecthood_Threshold_Interface.md` | Keeps selection, content, field, subjecthood, agency, and responsibility separated. |
| `Philosophy/SRT_Consciousness_Conditions.md` | Provides bare consciousness / activity / social coordination layers. |
| `AI/SRT_AI_03_Consciousness_Framework.md` | Provides AI strong-candidate consciousness window and anti-behaviorist guardrails. |
| `_SRT_D_VALUE_CANONICAL.md` | Defines stake-coupled concern; this file only uses `d-value` as a gate. |
| `_SRT_PSI_F_CANONICAL.md` | Defines payability burden; this file only uses `Psi_f` as transition / maintenance friction gate. |
| `Core/SRT_Core_22_Equations.md` | Provides bridge equations for Fisher-induced local cost, stake-gated d proxy, and L1-L2 writeback. |
| `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` | Future target for neuro-facing operationalization of phenomenal-structure measures. |

---

## 14. Minimal conclusion

The structural turn gives SRT a missing local tool:

```text
how to describe the internal structure of L1 experience.
```

SRT gives the structural turn a missing admission rule:

```text
which structures count as selected, borne, paid-for, and historically consequential.
```

Final compact line:

> Kleiner-style structural consciousness science asks what mathematical structure experience has. SRT asks which experiential structures become reality-relevant through selection, stake, friction, and sedimentation.
