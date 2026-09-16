---
id: SRT-NEURO-OBJECTIFICATION-SCALE-STABILITY-BENCHMARK
type: experiment_protocol
status: active
version: v0_1
record_stage: protocol_only_no_execution
date: 2026-09-16
layer: operations
epistemic_layer: experimental
claim_mode: hypothesis
claim_level: P3-P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
dependency:
  - Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md
  - Neuroscience/patches/SRT_Neuro_NEURAL33_Distributed_Ripple_Relational_Reinstatement_v0_1.md
  - Core/SRT_Core_14_Dynamics_Scaling.md
  - Operations/Audits/SRT_CONSTITUTION_PHASE8A_NEUROSCIENCE_BASELINE_DATA_ACCESS_AUDIT_2026-09-03.md
  - Materials/2026/SRC_2026_09_16_Neuro_Kiyooka_Scale_Dependent_Functional_Networks.md
  - Materials/2026/SRC_2026_09_16_Neuro_Oomoto_Wake_Sleep_Anesthesia_Open_Dataset.md
tags: [Neuroscience, Objectification, Scale, CoarseGraining, Network, OpenData, Benchmark, N3, N5, Robustness]
---

# SRT Neuroscience Objectification–Scale Stability Benchmark v0.1

> **Role**: bounded non-canonical open-data benchmark protocol. It operationalizes an existing Neuroscience Framework question: how stable is a neural inference when reasonable, explicitly declared objectification choices are changed on the same underlying recording?
>
> **Hard boundary**: this protocol is **not** NEURAL34, does **not** reopen Phase 8, does **not** reverse the 2026-09-03 `DATA-ACCESS-0 = NO-GO`, and does not establish an SRT-specific neural mechanism. It creates a separate empirical benchmark with its own question and failure conditions.

---

## 1. Root question

The benchmark asks:

> **When the same biological recordings are converted into different reasonable signal, node and graph objects, how stable are the resulting claims about brain-state-dependent network organization?**

The target is not the truism that coarse-graining loses information. The target is inferential stability:

```text
same recording source
+ predeclared reasonable objectification alternatives
-> does the scientific conclusion survive?
```

A useful local notation is:

\[
I = F(X; \pi, \phi, E, W),
\]

where, only for this benchmark:

- `X` = underlying recording;
- `pi` = node / grain construction;
- `phi` = signal representation / preprocessing branch;
- `E` = edge / network construction rule;
- `W` = temporal window / state epoch rule;
- `I` = a declared inferential output such as state contrast in modularity.

These symbols are protocol-local and create no SRT canonical variables.

---

## 2. Why this question is separately warranted

The current Neuroscience Reconstruction Framework already treats the following as non-trivial:

```text
recording boundary
cell / ensemble grouping
event window
pair / graph construction
averaging / normalization
state-space / decoder construction
```

Kiyooka et al. 2026 provide a concrete empirical pressure: at single-cell scale, sleep and isoflurane anesthesia show higher functional-network modularity than wakefulness in their analysis, while after mesoscale coarse-graining the state difference is not consistently retained; the spatial organization of modules also differs across scales.

The Oomoto et al. 2026 Data Descriptor exposes the underlying large-scale single-cell data and multiple processed representations, making a robustness benchmark feasible rather than merely conceptual.

The new work therefore does **not** claim:

```text
SRT predicted scale dependence first
or
ordinary network neuroscience lacks multiscale methods.
```

It asks whether SRT's objectification discipline is experimentally productive when applied to a strong open dataset.

---

## 3. Relation to existing owners

### 3.1 Neuroscience Framework

Primary owner relation:

```text
N3 relational / distributed organization
+
N5 measurement / objectification
```

The benchmark tests whether a reported organization is robust to how the public neural object is formed.

### 3.2 NEURAL33

NEURAL33 already states a bounded component/organization distinction. This benchmark does not reproduce ripple-mediated relational reinstatement. It extends the pressure orthogonally:

```text
component description != organizational description
and, separately,
organizational description may depend on declared grain.
```

No new NEURAL number is created here.

### 3.3 Core 14

Core 14 allows conditional testing of cross-scale structural consistency only after state spaces, observables, scale maps, comparison norms and tolerances are declared.

This benchmark is a neuroscience-domain realization of that discipline. It does not test universal scale invariance and does not restore old strict-conjugacy or unqualified entropy claims.

### 3.4 Phase 8 / NEURAL34

The existing Phase-8 charter requires relation-specific PRE / history / common-future structure that this dataset does not provide.

Therefore:

```text
this benchmark has a new question identity;
it cannot inherit Phase-8 confirmatory status;
it cannot be reported as a successful NEURAL34 data-access reopening.
```

---

## 4. Data source lock

Primary dataset:

```text
Oomoto I, Kiyooka D, Oizumi M, Murayama M. 2026.
Scientific Data.
DOI: 10.1038/s41597-026-08202-2

RIKEN CBS Data Sharing Platform
current version located at intake: v3.0 / 2026-07-08
DOI: 10.60178/cbs.20260708-001
```

Before execution, create an immutable execution manifest containing:

1. exact dataset DOI/version;
2. downloaded filenames and checksums;
3. record-level license;
4. session / animal / state metadata;
5. code commit hash;
6. preprocessing choices;
7. exclusions and reasons.

If the repository version changes, do not silently replace the locked dataset.

---

## 5. Phase 0 — replication gate

No SRT-facing interpretation is allowed before a basic source-replication gate.

Minimum gate:

1. load the processed dataset successfully;
2. reproduce basic neuron count / sampling / state metadata;
3. reconstruct one published Kiyooka network result or the closest method-faithful implementation possible from released code/methods;
4. document deviations;
5. verify that the result is not created by an obvious implementation error.

Possible outcomes:

```text
R0-PASS:
  source result broadly reproduced -> proceed.

R0-PARTIAL:
  direction reproduced but method ambiguity remains -> exploratory only.

R0-FAIL:
  substantial unexplained mismatch -> stop SRT-facing benchmark;
  report replication failure / ambiguity first.
```

---

## 6. Phase 1 — minimal objectification matrix

The first pass is deliberately small to avoid a researcher-degrees-of-freedom explosion.

### 6.1 Signal representation

Use the released alternatives where available:

```text
S1 = ΔF/F
S2 = deconvolved activity estimate
S3 = Gaussian-smoothed deconvolved estimate
```

Do not treat these as equivalent measurements by default.

### 6.2 Cell inclusion

At minimum:

```text
C1 = declared QC-passing population
C2 = published / method-faithful activity inclusion rule
```

If the source does not supply a distinct published inclusion branch, predeclare one conservative sensitivity alternative before inspecting state effects.

### 6.3 Node grain

At minimum:

```text
G1 = single cells
G2 = local spatial aggregates
G3 = mesoscale aggregates compatible with source geometry
```

Aggregation must be deterministic from predeclared spatial rules; do not choose parcels after seeing the desired state effect.

### 6.4 Edge construction

Primary edge family:

```text
standard pairwise functional association used consistently across states
```

Use a fixed-density or otherwise explicitly matched graph construction as the primary comparison so trivial edge-count differences do not determine modularity.

A small predeclared density grid may be used as sensitivity analysis. Do not choose one density post hoc because it maximizes the target interaction.

### 6.5 Temporal window

State epochs must follow released annotations / declared state criteria. Window length and overlap must be fixed before state-effect inspection.

---

## 7. Primary outcomes

### 7.1 State × grain interaction

For each independent session/animal unit, compute the primary network statistic `Q` under the declared graph model.

Define a state contrast at grain `g`:

\[
\Delta Q_g = Q_{state,g} - Q_{wake,g}.
\]

The key target is not whether one `ΔQ_g` is significant in isolation, but whether the estimated state effect is stable across `g`.

Primary contrasts are kept separate:

```text
Wake <-> NREM
Wake <-> Isoflurane
```

Do not make NREM <-> isoflurane the main causal contrast unless cohort/session/time-of-day and protocol structure justify it.

### 7.2 Inference-stability record

For each predeclared objectification cell, record:

```text
effect direction
standardized magnitude
uncertainty interval
session / animal consistency
whether the qualitative scientific conclusion changes
```

The desired output is a stability map, not a single winning graph.

---

## 8. Secondary outcome — matched measured component summaries

Only after Phase 1 is locked and run, an exploratory secondary analysis may ask whether different network organization remains after matching windows on **measured component summaries**.

Candidate matching variables may include, subject to actual availability:

```text
population mean activity
population activity variance
active fraction
state-duration / time covariates
available EEG / EMG or other released physiological covariates
```

Then test whether relational/network organization differs across matched windows.

Required wording:

```text
matched measured component summaries
```

Forbidden wording:

```text
identical neural state
same complete microphysical state
history-only difference
```

This secondary analysis cannot establish NEURAL34 because uncontrolled latent physiological and circuit variables remain possible.

---

## 9. Statistical unit and leakage guards

1. do not treat thousands of neuron pairs as independent biological replicates;
2. primary uncertainty must respect animal/session hierarchy;
3. graph thresholds, aggregation rules and preprocessing branches must be selected without using the target state contrast;
4. if data-driven communities are learned, do not reuse the same data for unconstrained community selection and confirmatory state testing without nested separation;
5. report the full predeclared sensitivity grid, including null and reversed cells;
6. do not discard an objectification branch because it weakens SRT-facing interpretation.

---

## 10. Interpretation matrix

### Result A — robust across reasonable objectifications

```text
state effect stable across signal / grain / graph choices
```

Interpretation:

> the reported organization is comparatively robust to the tested objectification choices.

SRT consequence:

- objectification is still methodologically relevant;
- but this dataset does **not** support a strong claim that the state inference is analyst-cut dependent within the tested range.

### Result B — magnitude changes but conclusion survives

Interpretation:

> the effect is quantitatively scale sensitive but qualitatively stable.

SRT consequence:

- report grain dependence explicitly;
- do not overstate ontological instability.

### Result C — conclusion changes / disappears / reverses

Interpretation:

> the scientific inference is materially conditional on the declared objectification.

SRT consequence:

- this strongly supports the Framework requirement to expose node/grain/graph construction;
- it still does not prove SRT ontology or show that one grain is metaphysically privileged.

### Result D — preprocessing dominates / replication unstable

Interpretation:

> the dataset does not currently sustain the desired system-level inference robustly enough.

SRT consequence:

- treat as reverse constraint;
- stop theory promotion and document the methodological failure.

---

## 11. Hard falsification / anti-HARKing conditions

This benchmark counts as informative even if it works against the motivating intuition.

The stronger objectification-dependence reading is weakened if:

1. the principal state contrast remains directionally and quantitatively stable across the reasonable predeclared matrix;
2. source replication fails and no stable network result can be established;
3. apparent grain sensitivity is fully explained by trivial graph density / node count / sample-size effects after matched controls;
4. different results arise only from obviously non-comparable or pathological preprocessing choices;
5. a claimed matched-component residual disappears under richer available physiological controls.

No negative outcome may be redefined post hoc as support for "deeper hidden objectification".

---

## 12. Consciousness / Bearer / One guard

Regardless of result:

```text
network modularity != consciousness
wake/sleep/anesthesia label != direct phenomenality measurement
module != One
module != Bearer
neuron != Bearer by default
scale sensitivity != proof of pre-object ontology
```

The benchmark is a downstream neuroscience/objectification test only.

---

## 13. Execution authorization state

```text
Protocol written: YES
Dataset intake verified at metadata level: YES
Dataset downloaded: NO
Code written: NO
Analysis executed: NO
Preregistration: NO
Confirmatory claim: NONE
Canonical writeback authorization: NO
NEURAL34 reopening: NO
```

Next legitimate execution step, if separately authorized, is Phase 0 data manifest + source-result replication. This file itself does not claim an empirical result.
