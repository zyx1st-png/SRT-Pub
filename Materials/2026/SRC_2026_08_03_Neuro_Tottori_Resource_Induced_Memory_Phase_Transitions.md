---
source_id: SRC-2026-08-03-NEURO-TOTTORI-RESOURCE-INDUCED-MEMORY-PHASE-TRANSITIONS
title: "Theoretical analysis of resource-induced phase transitions in estimation strategies"
source_type: accepted_peer_reviewed_article_with_arxiv_fulltext
domain: theoretical_neuroscience_resource_rational_memory
url: "https://arxiv.org/abs/2511.10184"
doi: "10.1103/5ynb-7k4v"
authors: "Takehiro Tottori; Tetsuya J. Kobayashi"
publication: "Physical Review Letters"
date_preprint: "2025-11-13"
date_accepted: "2026-06-03"
date_added: "2026-08-03"
evidence_level: peer_reviewed_accepted_primary_fulltext
reliability_level: high_for_minimal_LQG_resource_limited_estimation_model
content_access: "Primary arXiv full text close-read plus APS accepted-paper metadata; Neuroscience News used only as discovery trail"
srt_relevance: very_high
integration_priority: high
related_srt_claims:
  - L2_history_writeback
  - memory_admission
  - encoding_stabilization_dissociation
  - resource_limited_selection
  - Psi_f_proxy_guardrail
  - d_value_proxy_guardrail
  - future_selectability
  - phase_transition
tags:
  - memory
  - resource_rationality
  - optimal_control
  - LQG
  - phase_transition
  - sensory_uncertainty
  - intrinsic_noise
  - Physical_Review_Letters
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
id: SRC-2026-08-03-NEURO-TOTTORI-RESOURCE-INDUCED-MEMORY-PHASE-TRANSITIONS
---

# SourceCard: Resource-Induced Phase Transitions in Estimation Strategies

## 1. One-line summary

Tottori and Kobayashi analytically show, in a minimal resource-limited linear-quadratic-Gaussian estimation model, that the optimal strategy can switch discontinuously between current-observation-only estimation and memory-based estimation; memory is favored only in an intermediate uncertainty regime, and the discontinuity depends on jointly optimizing observational encoding and memory stabilization.

## 2. Core source claims

Usable source-level claims:

1. The modeled organism estimates a fluctuating environmental state from a noisy current observation and an internal memory state.
2. The objective jointly penalizes estimation error and the control cost required to update memory.
3. At low effective resource availability, the optimal memory control gains vanish and the estimator relies only on the current observation.
4. Above a resource-dependent boundary, nonzero memory control gains can become optimal.
5. The switch can be discontinuous even though the model is linear and Gaussian.
6. Memory use is nonmonotonic in sensory uncertainty: it is unnecessary when current observations are highly reliable, useful at intermediate uncertainty, and ineffective when observations are excessively noisy.
7. The relevant scaling combines estimation investment, memory-control cost, and intrinsic memory noise through a ratio containing `Q/(M F)`.
8. Two distinct memory-control functions are required in the analysis: encoding observational information into memory and applying negative feedback that stabilizes the memory state.
9. The discontinuity arises from simultaneous optimization of these two gains rather than from optimizing encoding alone.
10. The model concerns optimal estimation under resource constraints; it does not model consciousness, subjecthood, intrinsic concern, or ontological selection.

## 3. Evidence and method

- Formal setting: continuous-time scalar Ornstein-Uhlenbeck environmental process.
- Observation: Gaussian noisy measurement with variance parameter `E`.
- Internal memory: stochastic state with intrinsic noise intensity `F`.
- Control: a linear memory update rule with an observational encoding gain and a stabilizing feedback gain.
- Objective: long-run average of weighted squared estimation error plus quadratic memory-control cost.
- Method: optimal stochastic control, observation-based Riccati analysis, analytical reformulation of the memory control function, phase-boundary discriminants, and comparison with numerical solutions.
- Key dimensionless parameters identified by the authors include sensory uncertainty `beta = E/D` and a resource or memory-accuracy parameter `delta = QD/(M F)`.
- Publication status: accepted by *Physical Review Letters* on 3 June 2026; the full arXiv manuscript was used for this card.

## 4. Main limits

1. The model is deliberately minimal, scalar, linear, Gaussian, stationary, and focused on estimation rather than action selection.
2. `Q`, `M`, and `F` are model parameters. They are not direct measurements of metabolic energy, canonical `Psi_f`, canonical `d`, or future selectability.
3. The internal memory state is not automatically an SRT subject, bearer, or `L_2` in the full ontological sense.
4. The model assumes a predefined estimator, state space, cost function, and optimization target; it does not explain the origin of selectability.
5. A discontinuous optimal-policy change in a model does not by itself establish a biological neural phase transition.
6. Cross-scale applicability to cells, animals, and cognitive systems remains a proposed generalization rather than a single experimentally demonstrated mechanism.
7. The paper does not supply consequence-return, non-substitutability, or stake-coupling evidence required for canonical `d`.

## 5. SRT relevance

The strongest SRT increment is a bounded **history-admission interface**:

```text
past information can improve estimation
  does not imply
maintaining and using history is always worth its cost
```

The source supports separating at least two local operations:

```text
history encoding
!=
history stabilization
```

This is useful for SRT because `L_2` is often discussed as historical sedimentation or stable constraint. The paper provides a formal warning that historical write-back should not be treated as a single undifferentiated process. A system may fail to use memory because it cannot justify encoding, because the memory cannot be stabilized against intrinsic noise, or because current evidence is already sufficient.

A safe bridge is:

```text
resource and uncertainty regime
+ encoding capacity
+ stabilization capacity
-> whether a history-bearing estimator becomes optimal
```

An unsafe identity is:

```text
memory-control cost = Psi_f
resource parameter = d-value
internal memory = canonical L2
```

## 6. Bidirectional gain card

### New interface

- `history-admission threshold`: a local criterion for when historical information becomes worth maintaining.
- `encoding/stabilization dual gate`: a distinction between writing observations into memory and preserving the resulting memory state.
- `intermediate-uncertainty window`: history can be most useful between the extremes of near-perfect current evidence and overwhelmingly noisy evidence.
- discontinuous strategy change as a candidate bridge for abrupt shifts between reactive and history-bearing control.

### Reverse correction to SRT

- Do not imply that repeated exposure automatically becomes `L_2`.
- Do not reduce memory cost to canonical `Psi_f`; the source cost is a declared quadratic control term.
- Do not infer stake, agency, or subjecthood from optimal memory use.
- Do not assume that more uncertainty monotonically increases reliance on history.
- Do not merge encoding, maintenance, retrieval, and behavioral use into one memory variable.

### Strengthened SRT content

- Stable historical constraint requires both acquisition and maintenance.
- Existing structure can be adaptive only within a resource and uncertainty regime.
- A reactive policy can be optimal without implying absence of latent capacity.
- History-bearing organization can appear through threshold behavior rather than smooth accumulation.

### SRT contribution back to the source

SRT can extend the source model by distinguishing:

```text
estimation benefit
from
bearer-specific consequence return and future choice preservation
```

A future SRT experiment should ask not only whether memory reduces estimation error, but whether the cost is paid by the same history-bearing system, whether consequences return to it, and whether memory preserves or compresses future reselection capacity.

### Residual pressure

If ordinary resource-rational estimation models fully predict when systems acquire, maintain, abandon, and switch historical strategies, SRT must specify what explanatory residue remains for `L_2`, `Psi_f`, and stake-bearing selection rather than relabeling the same control problem.

## 7. Suggested patch target

Primary patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL19_Resource_Gated_Memory_Admission_v0_1.md
```

Future synthesis targets:

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuro_Predictions_Table.md
Core/SRT_Core_14_Dynamics_Scaling.md
```
