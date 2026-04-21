---
id: SRT-CORE-12B-MERGE-TARGETS-2026-04-21
type: merge_targets
tags: [L2, Closure, Compatibility, Merge, Hardening]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: editorial
dependency: [SRT-CORE-12B, SRT-CORE-12B-CCA, SRT-CLOSURE-COMPAT-HARDENING]
---

# Merge Targets for `Core/SRT_Core_12b_Ontology_L2.md`

> **Role**: This file contains insertion-ready precision blocks prepared from the 2026-04-21 hardening pass.
> It exists to support low-risk manual or later automated merge into `SRT_Core_12b_Ontology_L2.md` without reopening the conceptual decisions.

---

## Target 1 — insert after `T-L2-Scaffold` decomposition block

### Precision Note (2026-04-21): trace / closure / scaffold ladder

To prevent slippage between irreversibility, closure, and full L₂ backgrounding, read the ladder as follows:

1. **Trace floor**: every real selection can leave a trace — this is the irreversibility minimum.
2. **Minimal closure**: a trace becomes closure only when prior traversal begins to **systematically lower `Ψ_f` for compatible subsequent traversals**.
3. **L₂-grade closure**: closure becomes L₂-grade only when that low-friction path also becomes **inheritable, shareable, and backgrounded**.
4. **Scaffold threshold**: crossing $\rho^*$ marks the transition from foreground event to background scaffold.

Compressed form:

> **选择都会留痕；只有当留痕开始系统性降低兼容后续选择的 `Ψ_f` 时，才构成闭包；只有当这种低摩擦路径可继承、可共享并被背景化时，才构成 L₂ 级闭包。**

This note sharpens the reading of Ax-L2-01 and T-L2-Scaffold:
- Ax-L2-01 gives the universal trace law;
- T-L2-Scaffold gives the dominant ratchet by which some closures become background;
- the distinction between trace, closure, and L₂-grade scaffold must not be collapsed.

---

## Target 2 — insert after `Def-L2-DualLayer`

### Precision Note (2026-04-21): closure and compatibility

The path layer $\mathcal{P}_{low\text{-}\Psi}$ should be read through the following distinctions.

**Minimal closure**:
> A path counts as closed when the result of prior selection begins to **systematically lower `Ψ_f` for compatible subsequent selections**.

**L₂-grade closure**:
> A closure becomes properly L₂-grade when the same low-friction path becomes **inheritable, shareable, and re-enterable as background scaffold**.

**Compatibility (working definition)**:
> Compatibility is defined operationally by **absorbability into the current closure**: a path is compatible if it can be taken up by the current closure without breaking that closure's self-maintenance, and if its entry tends to further lower downstream `Ψ_f` for later compatible traversals.

**Compatibility (deep constraint)**:
> Operational compatibility is constrained more deeply by congruence with the `ε` direction. A path is not deeply compatible if it preserves local closure only by compressing a broader future selectability.

Compressed form:

> **兼容性在操作上由闭包的可吸纳性定义，在本体上受 `ε` 方向约束。**

This prevents three common drifts:
1. reducing closure to repetition alone;
2. reducing compatibility to surface similarity alone;
3. mistaking locally absorbable but globally self-erasing paths for healthy closure.

---

## Target 3 — insert after `Def-L2-Normative`

### Precision Note (2026-04-21): normatively neutral closure / pathological closure / lethal L₂

Closure is structurally real but **normatively neutral**.
It tells us that a path has formed a scaffold; it does not by itself tell us that the scaffold is good.

**Normatively neutral closure**:
> Closure means “formed,” not yet “justified.”

**Pathological closure**:
> A closure becomes pathological when it can preserve itself **only by compressing a broader future selectability**. Here the compression is not a mere side-effect; it is part of the sustaining mechanism of the closure itself.

**Lethal L₂**:
> Lethal `L₂` is the stronger case: a pathological closure that has already become **shared, inheritable, and backgrounded as scaffold**.

Compressed form:

> **闭包说明“成形了”，不说明“正当了”。病态闭包是靠压缩更大范围后续可选择性来维持自身的闭包；致命 `L₂` 则是这种病态闭包已经共享化、背景化之后的形态。**

This note should be read together with the existing normative classification table.
A stable structure is not automatically a sustainable structure, and a sustainable local closure is not automatically a healthy collective scaffold.

---

## Editorial Rule

When these blocks are merged into `SRT_Core_12b_Ontology_L2.md`, preserve the existing theorem bodies and formulas.
The intended operation is **precision insertion**, not conceptual rewrite.
