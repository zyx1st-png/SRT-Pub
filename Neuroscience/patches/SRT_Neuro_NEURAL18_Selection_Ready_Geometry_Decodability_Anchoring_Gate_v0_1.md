---
patch_id: PATCH-NEURO-NEURAL18-SELECTION-READY-GEOMETRY-DECODABILITY-ANCHORING-GATE
source_ids:
  - SRC-2026-07-27-NEURO-POSANI-RARELY-CATEGORICAL-HIGHLY-SEPARABLE-NATURE
domain: neuroscience_population_coding
claim_level: bridge
canonical_status: domain_bridge_patch_added
status: patch
target_documents:
  - "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
  - "Neuroscience/SRT_Neuro_Predictions_Table.md"
  - "Neuroscience/SRT_Neuro_Axioms_Claim_Status.md"
related_claims:
  - neural_manifold
  - selection_ready_geometry
  - candidate_capacity
  - decodability_anchoring_dissociation
  - L0_accessible
  - L1_anchoring
  - L2_writeback
  - G_hat_theta
  - d_value
  - Psi_f
  - consciousness_proxy_guardrail
tags:
  - mixed_selectivity
  - population_geometry
  - dimensionality
  - linear_separability
  - decodability
  - cortical_hierarchy
  - IBL
  - Nature
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_patch
id: PATCH-NEURO-NEURAL18-SELECTION-READY-GEOMETRY-DECODABILITY-ANCHORING-GATE
---

# SRT Neuroscience Patch NEURAL18: Selection-Ready Geometry and the Decodability–Anchoring Gate v0.1

> **Status**: high-priority neuroscience population-coding bridge and guardrail patch.  
> **Canonical caution**: this patch does not define `L_0`, `L_1`, `L_2`, `G_hat_theta`, `d-value`, `Psi_f`, subjecthood, consciousness, or neural dimensionality. It separates measurable representational capacity from actual selection and anchoring.

## 0. Source anchor

Primary source:

- Lorenzo Posani, Shuqi Wang, Samuel P. Muscinelli, Liam Paninski, and Stefano Fusi. "Rarely categorical, highly separable representations along the cortical hierarchy." *Nature* (2026). DOI: `10.1038/s41586-026-10668-4`.

Source card:

```text
Materials/2026/SRC_2026_07_27_Neuro_Posani_Rarely_Categorical_Highly_Separable_Nature.md
```

## 1. Why this matters for SRT

SRT often describes the neural system as maintaining candidates and stabilizing one trajectory into a behaviorally or consciously effective `L_1`. Population neuroscience, however, can easily tempt an invalid shortcut:

```text
variable can be decoded from neural activity
  -> the system selected that variable
  -> the variable is consciously represented
```

The source directly weakens that shortcut. Cortical populations can support many arbitrary linear dichotomies because their responses are diverse and high-dimensional. A successful external decoder therefore establishes a capacity of the recorded representation, not automatically the animal's own causal readout, behavioral commitment, conscious access, or historical write-back.

The key SRT correction is:

```text
selection-ready representational capacity
  != actual reality anchoring
```

## 2. Source result in compressed form

The source reports a scale-dependent organization:

```text
within many individual cortical regions:
  rare categorical clustering
  high response diversity

across cortical modules / whole cortex:
  stronger categorical organization
  partial alignment with anatomy

higher cortical hierarchy:
  more independently encoded conditions
  higher response diversity
  higher representational dimensionality
  high linear separability
```

This means local diversity and large-scale organization are not competing descriptions. They apply at different scales.

## 3. Main SRT bridge claim

### Claim NEURAL18

Cortical representational geometry should be treated as a **selection-ready capacity layer** rather than as selection, anchoring, or consciousness itself.

A minimal operational tuple for region or population `r` is:

\[
C_r^{geom}=\left(D_{\alpha,r},\;MIC_r,\;PR_r,\;Sep_r\right)
\]

where:

- `D_alpha` is response-profile diversity;
- `MIC` is the number of independently discriminable conditions;
- `PR` is participation-ratio dimensionality;
- `Sep` is the fraction of tested dichotomies that are linearly separable.

This tuple is an analyst-facing capacity summary. It is not a canonical SRT state variable and is not identical to `L_0^{accessible}`.

The admissible bridge is:

```text
high C_geom
  -> many potentially implementable distinctions / readouts
  -> broad selection readiness under the tested task
```

The inadmissible identity is:

```text
high C_geom
  == large L0
  == G_hat_theta selection
  == L1 anchoring
  == consciousness
```

## 4. Decodability–anchoring gate

Before a decoded neural variable can be used as evidence for an SRT anchoring claim, the following levels must be separated:

```text
L0: statistically decodable from recorded activity
L1: causally accessible to a downstream biological circuit
L2: behaviorally selectable or action-guiding
L3: stabilized across time / distractors / competing candidates
L4: concern-weighted or consequence-sensitive
L5: written back into future selection dynamics
L6: consciously reportable or otherwise supported as thick L1 anchoring
```

These labels are local laboratory levels, not replacements for canonical SRT layers.

### Gate rule

```text
R_DA(x) = 1
only when the claim level for decoded variable x is explicitly declared
and evidence appropriate to that level is provided.

If evidence is limited to cross-validated decoding:
  x is admissible only as representational-capacity evidence.
```

Suitable added evidence can include:

- causal perturbation of the putative readout pathway;
- trial-by-trial prediction of behavior beyond stimulus variables;
- state-dependent gating;
- action or report consequences;
- persistence under distraction;
- reversal or reopening cost;
- concern or bodily-relevance modulation;
- delayed memory or learning effects;
- subsequent change in future choice geometry or policy.

## 5. Selection is not necessarily dimensional collapse

A common but overly strong reading of `L_0 -> L_1` is:

```text
many possibilities -> one reality
therefore
high-dimensional neural activity -> low-dimensional neural activity
```

NEURAL18 rejects this inference.

The corrected statement is:

> SRT selection narrows effective commitment, action, report, and consequence-bearing trajectories; it does not require the neural population state carrying that commitment to become low-dimensional, categorical, or localized.

Therefore:

\[
\text{selection reduction}\neq\text{neural dimensionality reduction}
\]

A stable `L_1` candidate can be implemented by a high-dimensional distributed pattern. Conversely, a low-dimensional neural manifold can contain unresolved competition or automatic processing without thick anchoring.

## 6. Relationship to `G_hat_theta`

A fitted linear classifier is not automatically a neural implementation of `G_hat_theta`.

The classifier demonstrates:

```text
there exists a separating hyperplane in the sampled representation
```

SRT's neural selection architecture additionally requires a biologically implemented chain such as:

```text
candidate competition
-> gain / precision / concern-dependent bias
-> gating
-> stabilization
-> action, report, memory, or other consequence
```

A non-canonical schematic connection is:

\[
P(c_t\mid C^{geom},\theta,L_2)
\propto
\exp\left[
\beta_d\,d(c_t)
-\beta_{\psi}\,\Psi_f(c_t)
+b_{L_2}(c_t)
\right]
\]

This equation is only a bridge scaffold. It does not claim that `d-value`, `Psi_f`, or `L_2` have already been independently identified in the source dataset.

Its purpose is to make the division of labor explicit:

```text
C_geom describes what distinctions are available in principle.
d / Psi_f / L2 / gating describe which distinction becomes effective now.
```

## 7. Relationship to `L_0`, `L_1`, and `L_2`

### 7.1 `L_0^{accessible}`

The source offers possible proxies for the breadth and geometry of currently encoded candidate distinctions, but:

```text
MIC, PR, alpha-diversity, and separability
  != L0-accessible by definition
```

`L_0^{accessible}` also depends on causal access, state, body, task, history, and available downstream routes.

### 7.2 `L_1`

`L_1` anchoring must not be inferred from high decoding performance. A condition can be strongly represented without becoming the selected perception, action, judgment, or conscious content.

### 7.3 `L_2`

The paper's anatomical and regional organization is compatible with historically formed constraints, but anatomy or module identity is not automatically `L_2`. The stronger SRT bridge requires evidence that prior selection or learning changes future path availability, transition cost, persistence, or reopening.

## 8. Multiscale correction

The source supports the following multiscale guardrail:

```text
non-categorical within a region
  can coexist with
categorical organization across regions or modules
```

SRT should therefore avoid asking whether the cortex is simply categorical or non-categorical. The better questions are:

1. At what spatial and temporal scale is clustering tested?
2. Are clusters fixed, task-dependent, state-dependent, or history-dependent?
3. Does anatomical specialization constrain the available readouts without determining the current selected content?
4. Does local diversity preserve flexibility while global organization restrict routing?

## 9. Experimental predictions

### H-NEURAL18a: geometry–anchoring dissociation

When sensory input and population decodability are matched, manipulating concern or future consequence should alter behavioral commitment, persistence, memory, and later choice more than it alters raw linear separability.

Candidate design:

```text
same stimulus geometry
x neutral vs self-relevant / bodily relevant / future-constraining meaning
```

Measures:

- population separability;
- choice and reaction time;
- persistence under distractors;
- autonomic response;
- confidence or report;
- delayed memory;
- reversal cost;
- next-session choice bias.

SRT-favoring result:

```text
similar decodability
+ different anchoring / persistence / write-back
```

### H-NEURAL18b: preserved representation, disrupted use

Perturbing a gating or readout pathway should be able to preserve information in upstream population activity while disrupting action, report, stable maintenance, or learning.

SRT-favoring result:

```text
upstream variable remains decodable
but downstream anchoring consequences disappear
```

### H-NEURAL18c: trained-path efficiency versus alternative-path friction

Repeated training should not be evaluated only by improved decoding of the trained distinction. SRT predicts an efficiency-flexibility tradeoff in some regimes:

```text
trained path latency / error decreases
while incompatible reselection or rule reversal cost increases
```

The stronger result requires a cost increase for alternatives beyond ordinary accuracy improvement.

### H-NEURAL18d: dynamic categorical structure

If clustering participates in selection rather than only anatomy, cluster structure should vary with task rule, concern, state, or learned history even when the recorded region and sensory stimuli are held constant.

## 10. Differential prediction card

### Phenomenon

A neural population supports high cross-validated decoding of many task variables and arbitrary dichotomies.

### Nearby explanation

Mixed selectivity and high-dimensional geometry provide flexible linear readout and memory capacity.

### SRT added variables

- actual readout accessibility;
- `d-value` or concern-linked consequence;
- `Psi_f` or anchoring/reselection cost;
- `L_2` history and write-back;
- gating and stabilization.

### SRT-specific prediction

Among equally decodable distinctions, concern, switching cost, and learned history should predict which distinction becomes stable, action-guiding, persistent, and future-shaping.

### Failure condition

If geometry, stimulus statistics, reward, salience, uncertainty, and standard learning variables fully explain action, report, persistence, switching, delayed memory, and future policy, then the SRT-specific neural increment should be narrowed.

## 11. Boundary cautions

- Do not write that the paper proves "selection before representation."
- Do not write that mixed selectivity is `L_0`.
- Do not write that alpha-diversity measures freedom, consciousness, subjectivity, or ontological possibility.
- Do not identify a linear SVM or analytic readout with `G_hat_theta`.
- Do not infer animal use from analyst decoding alone.
- Do not infer `d-value` from encoded stimulus importance or task relevance alone.
- Do not infer `Psi_f` from geometric distance, classifier margin, dimensionality, or trial difficulty alone.
- Do not identify anatomical modules with `L_2` without history-dependent transition evidence.
- Do not assume that successful selection must reduce neural dimensionality.
- Do not treat early sensory categorical structure as proof of innate semantic kinds.
- Keep source scope visible: mouse cortex, IBL task, selected variables, linear encoding/decoding, and population-level analyses.

## 12. What would narrow or defeat this patch

This patch should be narrowed if any of the following occur:

1. Linear decodability plus ordinary task, reward, salience, and uncertainty variables fully predict causal use, behavioral choice, persistence, and learning, leaving no residual role for concern, anchoring friction, or history-specific reopening costs.
2. Proposed `d-value` manipulations change only arousal or reward and add no predictive value after those controls.
3. Proposed `Psi_f` measures collapse entirely into task difficulty, prediction error, uncertainty, or motor switching cost.
4. `L_2`-style alternative-path friction is not observed beyond standard learning and habit effects.
5. Causal readout perturbations do not produce any dissociation between represented information and behavioral or report-level use.

If these conditions hold broadly, NEURAL18 remains only a general decoding-hygiene note rather than an SRT-specific selection bridge.

## 13. Integration target text

Recommended compact-core insertion:

> **Selection-ready geometry is not selection.** High-dimensional, diverse cortical representations can make many experimental distinctions linearly decodable. This establishes a capacity for potential readout, not that a distinction is causally used, behaviorally selected, consciously anchored, or written into `L_2`. `L_0 -> L_1` therefore describes narrowing of effective commitment and consequence-bearing trajectories, not a necessary collapse from high- to low-dimensional neural activity.

Recommended prediction-table insertion:

```text
Phenomenon: high-dimensional mixed selectivity / broad decodability
SRT addition: decodability-anchoring gate
Prediction: matched decodability can coexist with different persistence,
behavioral commitment, concern sensitivity, reversal cost, and L2 write-back
Failure: standard geometry/readout models fully explain all downstream effects
```

Recommended claim-status insertion:

```text
NEURAL18 is a bridge/guardrail claim.
MIC, PR, alpha-diversity, separability, and decoder accuracy are not direct
measures of L0, L1, L2, G_hat_theta, d-value, Psi_f, subjecthood, or consciousness.
```

## 14. Integration status

Added as a standalone high-priority neuroscience bridge patch.

```text
SourceCard created
Patch created
Neuroscience hardening index updated
Material log registered
Compact-core / prediction-table / claim-status textual merge remains pending
```

Future synthesis should fold NEURAL18 into any N1-N12 successor as the population-geometry capacity layer and the primary decoding-to-anchoring guardrail.
