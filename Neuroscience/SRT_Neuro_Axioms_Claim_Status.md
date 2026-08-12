---
id: SRT-NEURO-AXIOMS-CLAIM-STATUS
type: audit
tags: [Neuroscience, Claim Mode, Canonical Audit, Bridge]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: evidence
dependency: [SRT-NEURO-AXIOMS-001, Governance/SRT_CLAIM_LADDER]
---

# Claim Status Audit — `_SRT_Neuro_Axioms.md`

> Purpose: classify the claim status of `Neuroscience/_SRT_Neuro_Axioms.md` without rewriting or deleting its expanded discourse.

## 1. Verdict

`Neuroscience/_SRT_Neuro_Axioms.md` is best treated as a **canonical-facing hybrid neuroscience bridge**, not as an all-canonical definition source.

It may serve as the formal neuroscience entrance file, but its internal claims must be read through a claim ladder.

Compact verdict:

```text
File status: canonical-facing hybrid bridge
Not: pure canonical source
Risk: claim-mode mixing
Action: keep file, add explicit claim-status guardrails
```

## 2. Why it is not all-canonical

The file contains several claim types in one place:

1. stable SRT-to-neuroscience mappings;
2. formal-looking axioms;
3. theorem labels;
4. operational proxies;
5. hypotheses;
6. expanded theoretical discourse;
7. external-theory comparisons;
8. falsification notes.

Because of this mixture, the file-level `claim_mode: canonical` should not be interpreted as meaning that every proposition inside is canonical.

## 3. Recommended file-level interpretation

Until a direct frontmatter change is made, interpret the file as:

```yaml
claim_mode_effective: canonical_facing_bridge
```

Suggested future frontmatter, if repository vocabulary allows it:

```yaml
claim_mode: hybrid
canonical_scope: formal_mappings_only
```

or:

```yaml
claim_mode: bridge
canonical_facing: true
```

## 4. Claim status table

| Claim / section | Current label in file | Recommended status | Notes |
|---|---|---|---|
| Terminology alignment | Terminology Alignment | canonical-facing guardrail | Safe and necessary. It aligns neuro usage with Core_Law symbols. |
| Ax-NEURO-1 Neural `G_hat_theta` | Axiom | bridge axiom / stable mapping | Good as formal bridge if not treated as primitive ontology. |
| Ax-NEURO-2 Neural domain mapping | Axiom | bridge axiom / candidate mapping | Useful but depends on how `L0_neural`, ignition, and priors are operationalized. |
| Ax-NEURO-3 Divisive normalization | Axiom | bridge hypothesis / strong mechanism candidate | Too strong if written as universal necessity. Keep as constrained-selection mechanism unless proven more generally. |
| Ax-NEURO-4 Predictive coding update | Axiom | imported theory bridge | Stable as relation to predictive processing/FEP, not as SRT primitive. |
| H-NEURO-4b PE friction proxy | Hypothesis / operational proxy | lab-facing P3/P4 proxy | Correctly marked. Must not be promoted to theorem status. |
| Ax-NEURO-5 Metabolic friction | Axiom | bridge hypothesis / measurable proxy | Valuable but proportionality `Psi_f ∝ E_metabolic` needs empirical window. |
| H-NEURO-Ignition-1 | legacy T-NEURO-1 | hypothesis / operational gate family | Correctly demoted in text; should not be cited as theorem. |
| T-NEURO-2 Pathology Deviation | Theorem | candidate proposition / bridge model | `Pathology iff theta deviation` is too strong. Should become one modeling lens, not biconditional theorem. |
| T-NEURO-3 Meso-Operator | Theorem | bridge proposition / candidate mechanism | Good idea, but needs prerequisites and evidence before theorem status. |
| C-NEURO-1 L6b Resampling | Corollary | speculative corollary / research hypothesis | Keep as directional hypothesis. |
| T-NEURO-4 NCC Non-Equivalence | Theorem | conceptual constraint / bridge theorem candidate | Strong philosophically, but theorem status needs precise premises. |
| Part B expanded discourse | Context | contextual discourse | Should not be treated as canonical axiom source. |
| GWT/IIT/HOT comparison | Context / argument | comparative discourse | Good for positioning, not canonical definition. |
| Hard Problem discussion | Context / argument | philosophical bridge | Belongs to interpretation layer unless formally linked to core axioms. |

## 5. Minimal canonical subset

The following parts are closest to canonical-facing stability:

1. symbol alignment with `L_0 / L_1 / L_2`, `G_hat_theta`, `d-value`, and `Psi_f`;
2. the idea that neural systems can be modeled as embodied implementations of `G_hat_theta`;
3. the mapping of neural candidate manifolds to an accessible `L0_neural`;
4. the distinction between local neural proxies and full SRT variables;
5. the warning that NCC correlation is not identical with experience or anchoring.

Even these should be read as **bridge-level canonical-facing claims**, not P0/P1 primitive axioms.

## 6. Claims needing downgrade or guardrails

### 6.1 Divisive normalization

Current risk:

```text
selection dynamics necessarily converge to divisive normalization
```

Safer reading:

```text
Under metabolic and bandwidth constraints, divisive normalization is a strong candidate form of constrained neural selection.
```

**2026-08-12 floor result**：即使神经响应符合除法归一化，也不能直接推出认知／行为选择。当前有界桥为 `Core_14 P3-Scale-NB1`：候选身份映射、冻结读出、阈值／累积或采样规则、执行门、held-out 误差、rival 比较与具名干预必须同时声明。首个具名工作线 `NB1-MOFC-Lottery-v0` 已在 `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md` 定义为本地 P4 执行卡，但尚未正式锁定、预注册或执行。通过只建立任务局部 neural-to-behavioral compatibility，不建立机制同一、actualisation、agency、subjecthood 或 consciousness。

The energy–information objective `J=H-λE` does not uniquely derive divisive normalization unless the cost functional, feasible set, dynamics, and boundary conditions are specified and the resulting solution is proved to belong to that family.

### 6.2 Pathology deviation

Current risk:

```text
Pathology iff theta = theta_healthy + Delta theta
```

Safer reading:

```text
Many neuropsychiatric states can be modeled as deviations in theta-space, but this does not imply a full biconditional reduction of all pathology to a single parameter shift.
```

### 6.3 Meso-operator theorem

Current risk:

```text
glia/pruning as theorem-level meso-operator implementation
```

Safer reading:

```text
glial pruning is a candidate slow-timescale meso-selection mechanism affecting L2 constraints.
```

### 6.4 NCC non-equivalence

Current risk:

```text
NCC non-equivalence theorem
```

Safer reading:

```text
NCC non-equivalence is a conceptual bridge constraint: correlation or inducibility does not entail ontological identity with experience.
```

## 7. Relation to 2026-04 N1-N9 hardening

The new N1-N9 hardening layer should be used to refine `_SRT_Neuro_Axioms.md` rather than replace it.

Mapping:

| N-claim | Best target inside current neuro files |
|---|---|
| N1 neural systems as selection systems | `_SRT_Neuro_Axioms.md` Ax-NEURO-1; `SRT_Neural_Mechanisms_CompactCore.md` |
| N2 composite `G_hat_theta` | `SRT_Neural_Mechanisms_CompactCore.md` |
| N3 `Psi_f` as selection friction | `_SRT_Neuro_Axioms.md` H-NEURO-4b / Ax-NEURO-5; compact core §6 |
| N4 L2 sedimentation | compact core §4 |
| N5 d-value | compact core §9 |
| N6 consciousness as stable concern-weighted L1 | `SRT_Consciousness_Mechanisms_CompactCore.md` |
| N7 psychopathology | compact core §8 and consciousness compact core §9 |
| N8 experimental roadmap | compact core §10; `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md` for the first bounded P4 workline |
| N9 mainstream-theory distinction | compact core §10 and PR staging draft |

## 8. Recommended next edits to `_SRT_Neuro_Axioms.md`

When full-file editing is safe, perform these minimal edits:

1. Change or qualify frontmatter `claim_mode: canonical`.
2. Add a top warning:

```text
This file is canonical-facing, but not every claim inside is canonical. See `SRT_Neuro_Axioms_Claim_Status.md`.
```

3. Rename or annotate theorem labels:
   - `T-NEURO-2` -> `P-NEURO-Pathology-1` or `H-NEURO-Pathology-1`;
   - `T-NEURO-3` -> `P-NEURO-Meso-1`;
   - `T-NEURO-4` -> `C-NEURO-NCC-1` unless formal premises are supplied.
4. Mark Part B as contextual discourse, not canonical axiom source.
5. Link the N1-N9 compact-core integrations.

## 9. Current usage rule

Use `_SRT_Neuro_Axioms.md` as:

```text
formal neuroscience bridge + historical axiom/discourse container
```

Do not use it as:

```text
all-claims canonical definition source
```

For concise current neuroscience doctrine, prefer:

- `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`
- `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`
- `Neuroscience/SRT_Neuroscience_Hardening_N1_N9_v0_1.md`
