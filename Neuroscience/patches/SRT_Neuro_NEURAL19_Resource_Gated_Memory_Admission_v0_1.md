---
patch_id: PATCH-NEURO-NEURAL19-RESOURCE-GATED-MEMORY-ADMISSION
source_ids:
  - SRC-2026-08-03-NEURO-TOTTORI-RESOURCE-INDUCED-MEMORY-PHASE-TRANSITIONS
domain: theoretical_neuroscience_resource_rational_memory
claim_level: bridge
canonical_status: non_canonical
status: patch
target_documents:
  - "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
  - "Neuroscience/SRT_Neuro_Predictions_Table.md"
  - "Core/SRT_Core_14_Dynamics_Scaling.md"
related_claims:
  - L2_history_writeback
  - history_admission
  - memory_encoding
  - memory_stabilization
  - resource_limited_selection
  - uncertainty_regime
  - Psi_f_proxy_guardrail
  - d_value_proxy_guardrail
tags:
  - memory
  - resource_rationality
  - phase_transition
  - optimal_control
  - LQG
  - history_writeback
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_patch
id: PATCH-NEURO-NEURAL19-RESOURCE-GATED-MEMORY-ADMISSION
---

# SRT Neuroscience Patch NEURAL19: Resource-Gated Memory Admission v0.1

> **Status**: bounded neuroscience / dynamics bridge.  
> **Canonical caution**: this patch does not define `L_2`, `Psi_f`, `d-value`, memory, or agency. It extracts a local history-admission model and preserves the source variables as source variables.

## 0. Source anchor

Primary source:

- Takehiro Tottori and Tetsuya J. Kobayashi. "Theoretical analysis of resource-induced phase transitions in estimation strategies." Accepted by *Physical Review Letters* (2026). DOI: `10.1103/5ynb-7k4v`; arXiv: `2511.10184`.

Source card:

```text
Materials/2026/SRC_2026_08_03_Neuro_Tottori_Resource_Induced_Memory_Phase_Transitions.md
```

## 1. Why this matters for SRT

SRT often describes repeated selections as sedimenting into a history-bearing constraint domain. That formulation can hide an unjustified monotonic assumption:

```text
more exposure or more uncertainty
-> more memory
-> stronger L2
```

The source shows why this shortcut is unsafe. In a minimal estimation model, memory is worthwhile only in a bounded resource and uncertainty regime. Moreover, acquiring observational information and stabilizing the memory state are distinct control functions whose joint optimization can produce an abrupt strategy transition.

The useful SRT question becomes:

> Under what conditions is historical write-back locally admissible, maintainable, and worth its cost?

## 2. Source variables and non-identity map

| Source object | Source role | Bounded SRT bridge | Must not be identified with |
|---|---|---|---|
| `x_t` | fluctuating environmental state | currently relevant external process | `L_0` as such |
| `y_t` | noisy current observation | current evidence available to the estimator | manifest reality in general |
| `z_t` | internal memory state | local history-bearing state | canonical `L_2` by definition |
| `Phi_zy` | observational encoding gain | history-write gate candidate | `G_hat_theta` |
| `Phi_zz` | stabilizing feedback gain | history-maintenance gate candidate | persistence or agency in general |
| `Q` | estimation-error weight | declared task investment / accuracy pressure | canonical `d` |
| `M v_t^2` | quadratic memory-control cost | local implementation cost | canonical `Psi_f` |
| `F` | intrinsic memory noise | maintenance challenge | ontological friction |
| `E` | observation noise | current-evidence uncertainty | value hiddenness or `T_dir` |

The mapping is functional and local. No source parameter inherits canonical status.

## 3. Main SRT bridge claim

### Claim NEURAL19

A history-bearing control mode should be treated as requiring at least two separable local admissions:

```text
encoding admission:
  can current evidence be written into a persistent state?

stabilization admission:
  can that state be maintained against internal noise at payable local cost?
```

Therefore:

```text
history encoding
!=
history stabilization
!=
history-guided behavioral use
```

Repeated input alone is not sufficient for stable `L_2`-like constraint formation.

## 4. Formal bridge

The source optimizes a long-run objective of the form:

\[
J=\lim_{T\to\infty}\frac{1}{T}\,\mathbb E\int_0^T
\left[Q(x_t-\hat{x}_t)^2+M v_t^2\right]dt.
\]

Its relevant dimensionless controls include:

\[
\beta=\frac{E}{D},\qquad
\delta=\frac{QD}{MF}.
\]

For SRT purposes, these remain source-level coordinates. A safe local bridge is to define only an admission predicate:

\[
A_{hist}^{local}=1
\quad\text{when a declared model shows that}\quad
J_{memory}<J_{reactive}
\]

with nonzero encoding and stabilization gains.

This does **not** define a universal SRT threshold. It records that a history-bearing strategy can be conditionally admitted rather than presumed.

## 5. New claim cluster

### NEURAL19a — history admission is regime-dependent

A memory-bearing strategy can be locally suboptimal even when memory capacity exists. Current evidence quality, intrinsic memory noise, and control cost jointly determine whether history is used.

### NEURAL19b — writing and maintaining history are separable

A system may encode poorly, stabilize poorly, or fail at both. Experiments should not infer one failure from another.

### NEURAL19c — memory value can be nonmonotonic in uncertainty

Very reliable current evidence reduces the need for memory; extreme observation noise can make memory uninformative; intermediate uncertainty can maximize its value.

### NEURAL19d — history-mode transitions can be abrupt

An abrupt reactive-to-memory switch is possible without invoking a nonlinear neural ontology. SRT should treat phase-transition language as a model-dependent bridge until biological evidence demonstrates the corresponding transition.

## 6. Experimental and operational consequences

### H-NEURAL19a: resource-by-uncertainty interaction

Manipulate sensory reliability and memory-maintenance burden independently. A simple monotonic prediction should fail if history use peaks at intermediate uncertainty and sufficient maintenance capacity.

Measures:

- reliance on previous trials or delayed cues;
- current-evidence weighting;
- memory accuracy and decay;
- energetic or effort proxies;
- policy switching latency.

### H-NEURAL19b: acquisition–retention dissociation

Use matched acquisition with different post-encoding stabilization demands, or matched retention with different encoding quality. SRT-facing analyses should report both gates.

### H-NEURAL19c: abrupt policy reweighting

Across a gradually varied resource proxy, test whether the weight assigned to history changes smoothly or discontinuously. A discontinuity is source-compatible but not required by SRT.

### H-NEURAL19d: history benefit versus future choice

Compare memory that improves immediate estimation with memory that also preserves later reversal and reselection. This separates task performance from future selectability.

## 7. Boundary cautions

1. `M v_t^2` is not canonical `Psi_f`.
2. `Q`, `Q/(MF)`, or `delta` is not canonical `d`.
3. A stochastic estimator with memory is not thereby a subject or bearer of stake.
4. A model-optimal memory state is not canonical `L_2` without history, constraint, consequence, and scale checks.
5. The paper does not solve the origin of selectability.
6. Phase-transition language must remain tied to the declared model and control regime.
7. SRT must show residual explanatory or predictive value beyond resource-rational control theory.

## 8. Integration hook

```text
Neuroscience/hooks/NEURAL19_Resource_Gated_Memory_Admission_Integration_Hook.md
```

## 9. One-paragraph abstract

NEURAL19 introduces a bounded history-admission bridge from a resource-limited optimal-estimation model. Its stable increment is that historical control should not be presumed from repetition or uncertainty: encoding current evidence into memory and stabilizing the memory state are separable gates, and memory use can become optimal only within a bounded resource–uncertainty regime. The bridge supports experiments that dissociate acquisition, maintenance, and later behavioral use, while explicitly blocking identities between source cost and `Psi_f`, resource weighting and `d`, internal memory and canonical `L_2`, or optimal estimation and subjecthood.
