---
id: SRT-NEURO-NEURAL25-MEMORY-HISTORICAL-SELECTION-BIAS
type: bridge_patch
status: active
version: v0_1
canonical: false
claim_level: P3-P4
claim_mode: evidence
layer: operations
epistemic_layer: os
domain: Neuroscience
source_ids: [SRC-2026-08-09-NEURO-LU-STRATEGY-COMPETITION-MEMORY-CONTROL]
created: 2026-08-09
target_future_doc:
  - Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
  - Core/SRT_Core_24_Discriminating_Predictions.md
  - 03_Bridges/SRT_Selection_Event_CompactCore.md
tags: [memory, L2, strategy-competition, selection-authority, path-efficacy, history, hysteresis]
---

# NEURAL25 — Memory as historical selection bias, not stored content alone

> **Status / boundary**: P3 neuroscience bridge with P4 experimental consequences. This patch does not redefine memory, `L2`, `G_hat_theta`, real choice, subjecthood or consciousness. It records a narrower claim that survives the Lu et al. strategy-learning evidence and is useful for SRT hardening.

## 1. Source anchor

Primary verified anchor:

- Lu et al. (2023), *Instinct to insight: Neural correlates of ethological strategy learning*, bioRxiv, DOI `10.1101/2023.09.11.557240`.
- COSYNE 2025 update: *Instinct vs Insight: Neural Competition Between Prefrontal and Auditory Cortex Constrains Sound Strategy Learning*.

The circulated later-*Science Advances* summary is treated as a retrieval lead only until its final bibliographic record is independently verified. This patch therefore relies on the preprint and conference-update claims that are independently recoverable.

---

## 2. Surviving bridge claim

The strong sentence

> `memory = selection weight`

is too strong and should not enter SRT.

The defensible bridge is:

> **Memory is not exhausted by stored representation of a past object or event. In at least some action-guiding memory systems, its causal efficacy includes historically induced weighting of future candidate paths, candidate accessibility, switching cost and control authority.**

A shorter SRT-facing form is:

> **What matters causally about memory is not only what from the past remains representable, but how the past continues to bias what can win next.**

This preserves representational content while refusing to identify memory with content storage alone.

---

## 3. Three separations forced by the evidence

### 3.1 Representation is not authority

A neural population may carry decodable information about a candidate or past state without that information currently controlling behavior.

```text
representation present
!=
behavioral control authority
```

The Lu task is useful because auditory-cortex signals related to correct sound use can appear before the sound strategy dominates overt behavior.

### 3.2 Authority is not expression

A candidate can have non-zero control weight yet lose a particular trial to another strategy.

```text
candidate control weight
!=
realized behavioral expression on every trial
```

### 3.3 Expression is not historical write-back

Executing a path once does not yet establish durable memory/hardening. Historical efficacy requires that the outcome changes future reachability, transition probability, switching cost, threshold or candidate generation.

```text
one behavioral output
!=
L2-like historical restructuring
```

This matches the current CG-4 / HEF guardrail.

---

## 4. Minimal bridge model

For an action-guiding memory trace or historically supported strategy `i`, use a temporary bridge decomposition:

\[
M_i(t) = \{R_i(t), A_i(t), W_i(t), K_{i\to j}(t)\}
\]

where:

- `R_i`: representational availability/content strength;
- `A_i`: accessibility — probability that the candidate enters effective competition;
- `W_i`: current effective control weight / selection authority;
- `K_{i->j}`: transition or switching cost away from this path toward an alternative.

This is **not** a canonical SRT equation. It is an experimental decomposition.

The key dissociation is:

\[
R_i \not\equiv W_i
\]

and the stronger SRT-facing hypothesis is:

\[
H_i \uparrow
\Rightarrow
A_i \uparrow,\quad
K_{i\to j} \uparrow,\quad
A_j \downarrow
\]

under declared task conditions, where `H_i` is history depth / hardening proxy.

The last relation is the important one: history may do more than make one response stronger; it may make alternatives harder to enter.

---

## 5. Relation to `L2`

Current neuroscience-facing SRT treats `L2` as historically sedimented selection constraint rather than mere memory storage. NEURAL25 sharpens this in two directions.

### 5.1 `L2` as background landscape

Past selections can alter the future transition field without being reinstantiated as an explicit current option.

### 5.2 `L2` as reinstantiated expert

A historical scaffold can be reactivated into a live candidate that competes with a newly learned candidate for current control.

This suggests a useful bridge distinction:

```text
L2_background
vs
L2_reinstantiated
```

Do not promote these labels to canonical symbols. They are local explanatory handles.

The win-stay strategy is best treated as a candidate example of `L2_reinstantiated`: prior successful location history is carried forward into a concrete next-search recommendation.

---

## 6. Mapping to the selection-event audit

| Gate | NEURAL25 reading |
|---|---|
| CG-0 / DMF | previous-location and current-sound differences enter effective channels |
| CG-1 / NER | internal states register candidate strategies non-equivalently |
| CG-2 / PEF | only when a strategy changes actual arm-entry probability does it obtain path efficacy |
| CG-3 / CBP | relatively weak in this task because an initial wrong arm can still be corrected; do not overclaim complete real-choice evidence |
| CG-4 / HEF | strongest future test: does history alter later accessibility, switching cost or recovery after perturbation? |

The source therefore supports a particularly clean **CG-1 / CG-2 dissociation**:

> decodable strategy-related state does not automatically imply path-effective control.

---

## 7. Discriminating prediction: matched current state, different history

Ordinary strategy-competition and reinforcement-learning models can already represent competing policy weights. NEURAL25 should therefore not claim novelty from competition alone.

The stronger SRT test is:

> **If a memory has hardened into a history-bearing selection constraint, then history depth should predict alternative-path accessibility, switching cost and hysteresis even after current reward, strategy reliability, current performance and immediate strategy-weight proxies are matched.**

### Proposed design

Create two groups with different depths of prior win-stay training but adapt training so that before introducing the novel sound strategy they are matched as closely as possible on:

- current win-stay performance;
- current reward contingency;
- current fitted strategy weight;
- immediate mPFC previous-location decoder strength.

Then introduce the same sound cue and test whether deeper history predicts:

1. slower entry of the auditory candidate into effective control;
2. larger switching cost;
3. lower alternative-path accessibility;
4. stronger recovery of the old strategy after transient perturbation;
5. stronger hysteresis after attempted reversal.

This directly instantiates Core 24 P24-3:

```text
local trained-path efficiency
+
alternative-path constraint
+
hysteresis
```

rather than ordinary memory-strength improvement alone.

---

## 8. Failure condition

This bridge must be weakened if, after controlling current reward, reliability, performance, fitted strategy weight and immediate representation strength, history depth does **not** predict any residual difference in:

- alternative-path accessibility;
- switching cost;
- perturbation recovery;
- hysteresis;
- future candidate-entry probability.

Under that result, the relevant phenomenon should be treated as ordinary memory / habit / policy weighting unless another independently testable historical-effect variable is identified before seeing the result.

Do not rescue the claim by adding unconstrained latent-history parameters after failure.

---

## 9. What this source does not license

Do **not** write:

- `memory is not representation`;
- `memory = selection weight`;
- `mPFC = L2`;
- `auditory cortex = L0`;
- `strategy competition proves SRT`;
- `mPFC inhibition generally improves learning`;
- `habit replay is itself a real choice moment`.

Safer replacements:

- memory representation and memory control efficacy are separable;
- some memories act as historically induced biases over future selection;
- a habit may be a historical candidate inside a new selection competition without the habit replay itself constituting a new real choice moment;
- learning curves may conflate acquisition, candidate availability, control authority, behavioral expression and historical write-back.

---

## 10. Five-stage learning decomposition

For future neuroscience work, separate:

```text
Acquisition
-> Availability
-> Authority
-> Expression
-> Write-back
```

1. **Acquisition** — is a new mapping or candidate structure formed?
2. **Availability** — can it enter the effective competition set?
3. **Authority** — can it causally control a real path?
4. **Expression** — does it win this trial and become actual behavior?
5. **Write-back** — does this realized path alter later accessibility, cost or transition structure?

This decomposition is the main reusable increment from NEURAL25.

---

## 11. Future integration sentence

Candidate de-materialized sentence for a future `SRT_Neural_Mechanisms_CompactCore.md` synthesis:

> **Memory should not be reduced to retained content: a history-bearing neural structure matters to selection insofar as it changes which candidates are easy to reactivate, which can obtain behavioral control, how costly switching becomes, and whether those asymmetries persist after perturbation.**

Do not merge this sentence until the final source bibliographic status and the compact-core synthesis queue are reviewed.
