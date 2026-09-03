---
id: SRT-CONSTITUTION-PHASE6-REFERENCE-AXIOMS-SECTION-AUDIT-20260902
type: audit
status: active
version: v1
date: 2026-09-02
layer: meta
epistemic_layer: governance
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_CONSTITUTION_PHASE6_CORE_ROLE_RECLASSIFICATION_PASS1_2026-09-02.md
  - Core_Law/SRT_Reference_Axioms.md
  - Core/SRT_Core_21_Formal_Axioms.md
  - Core/SRT_Core_21_Minimal_Axioms.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Core/SRT_Core_21c_Bridge_Hypotheses.md
  - _SRT_D_VALUE_CANONICAL.md
  - _SRT_PSI_F_CANONICAL.md
tags: [Constitution, Phase6, ReferenceAxioms, SectionAudit, EpistemicRole]
---

# Phase 6 — `SRT_Reference_Axioms.md` section-by-section role audit

> **性质**：只读审计。本文不改变 `SRT_Reference_Axioms.md` 的当前 canonical status，也不改任何 Axiom / theorem / formula。
>
> **目的**：回答一个比“这条公理对不对”更先的问题：在 Constitution v1 已不以形式公理为 floor 的前提下，Reference Axioms 中各条现在实际上属于 historical formalization、conceptual bridge、domain formalization、operational proxy 还是 legacy/superseded expression？

---

## 1. 总裁决框架

Reference Axioms 的旧架构是：

```text
L0 metaphysics
-> L1 Reference Axioms
-> Reference Ontology / domain bridges
```

Constitution v1 后，这条架构不能继续解释成：

```text
L0 / Reference formalization
-> constitutional authority
```

但 Reference Axioms 仍可能保留：

- formal-core encoding；
- historical theory state；
- conceptual bridge；
- domain hypothesis；
- proxy / modeling interface。

因此本审计只改**角色地图**，不改理论内容。

---

## 2. A1–A5：从 formal-core encoding 到 stronger theory

### A1 Selection Priority

**Current expression**：selection 在本体论上先于 manifest actuality，并给出 `Existence ≡ Selection(P)` 式。

**Current stronger owner**：`Core/SRT_Core_21_Minimal_Axioms.md P0-01` 已有 AM-A 精确化，明确 `G_theta` 只是 primitive actualisation 的 formal role-carrier，不以 operator output 循环解释 actualisation。

**Proposed role**：

```text
primary: historical formalization
secondary: conceptual bridge
```

**Disposition**：Reference A1 作为旧 L1 formal encoding 保留历史价值；当前 formal-core 引用应优先回 21A P0-01。它不再承担 Constitution floor。

---

### A2 Manifest Actuality / Anchoring Persistence

**Current expression**：已通过 EX-A 修正旧 `Existence iff ... DeltaF < 0`，明确自由能/Psi_f 只可作为持续锚定候选条件。

**Current stronger owner**：21A P0-01/P0-02 与 current L0 EX-A boundary。

**Proposed role**：

```text
primary: historical formalization
secondary: conceptual bridge
```

**Disposition**：KEEP AS synchronized formal-history surface；不作为第一次 actualisation 的定义源。

---

### A3 Causality as Projection

**Current expression**：因果被写成高维 selection process 对低维时空的 projection。

**Current owner status**：`Core/SRT_Core_21b_Constitutive_Theorems.md P1-T01` 已把较窄的 `horizontal causality inside L2` 固定为 P1，并明确不替代 vertical constitution。

**Proposed role**：

```text
primary: legacy/superseded expression (as unrestricted Reference Axiom)
secondary: conceptual bridge
```

**Reason**：当前 P1 owner 比 Reference A3 更窄、更有层级边界。Reference A3 的 unrestricted wording 不应因 `A3` 标签恢复更强 authority。

---

### A4 Embodiment Necessity

**Current expression**：任何有效 `G_theta` 必须具有有限 embodied parameters；不存在 view from nowhere。

**Proposed role**：

```text
primary: conceptual bridge
secondary: historical formalization
```

**Reason**：它与 Constitution 的 situatedness / no-God-view discipline 有强 resonance，但 Constitution 只要求 reader-side position disclosure，不由此证明所有 domain selection operator 必须满足 Reference A4 的具体 formal validity condition。

**Disposition**：KEEP AS stronger theory bridge；future domain checks required for specific embodiments。

---

### A5 Normative Closure / L2 fixed-point structure

**Current expression**：L2 被形式化为 stable fixed point，并向未来 selection 回写 constraint。

**Current owner relation**：21B P1-T03 保留 L2 downward constraint；具体 domain `C_L2` mechanism 留给 bridge/lab。

**Proposed role**：

```text
primary: historical formalization
secondary: conceptual bridge
```

**Disposition**：Reference fixed-point equation 不应自动代表所有 L2 realization；downward-constraint semantic role 回 21B，fixed-point form 作为模型化表达。

---

## 3. A6–A9：已经被后续 claim ladder 明确降级的一组

### A6 Information–Existence Equivalence

**Reference expression**：`ii(s)=min(i_diff,i_spec)`，以“存在程度”表述。

**Current owner status**：21C 已明确将 former Ax-F-04 归为 `P2/P3-B01`，不是 P0/P1。

**Proposed role**：

```text
primary: legacy/superseded expression (as axiom)
secondary: conceptual bridge / operational formalization
```

**Disposition**：owner inversion 已完成；Reference A6 的 axiom surface 不得恢复 P0/P1 权威。

---

### A7 Fitness Beats Truth / Pruning Criterion

**Reference expression**：借 Hoffman FBT，将 fitness 优先于 truth 扩展到 general selection，并给出 argmax fitness form。

**Current owner status**：21C `P3/P4-B02` 明确是 cross-theory bridge / empirical-comparative hypothesis。

**Proposed role**：

```text
primary: domain formalization
secondary: conceptual bridge
legacy/superseded expression: yes, specifically the Axiom status
```

**Disposition**：必须按 domain / evolutionary model 使用，不能作为 general SRT axiom。

---

### A8 Survival as Probability Localization

**Reference expression**：以 L0 probability-density packet 与 `theta_life` threshold 定义 life/survival，并给出 selection-strength gradient。

**Current observed status**：未在 21A/21B 当前 minimal/constitutive owner 中找到相应 primitive/theorem；其形式明显需要 state space、measure、life threshold 与 domain operationalization。

**Proposed role**：

```text
primary: domain formalization
secondary: operational proxy
legacy/superseded expression: candidate as general axiom
```

**Disposition**：不能继续作为 domain-free axiom 使用。是否保留为 biology/AI bridge，由后续 domain audit 决定。

---

### A9 Holographic Duality

**Reference expression**：`L1 bulk ≅ L0 boundary`，并把 d 与 entanglement area 对应。

**Current owner status**：21C 已明确 former Ax-F-07 = `P3/P4 strong physics/formal bridge`。

**Proposed role**：

```text
primary: domain formalization
secondary: conceptual bridge
legacy/superseded expression: yes, specifically the Axiom status
```

**Disposition**：只可作为 physics/formal bridge candidate，不能从 Constitution 或 general ontology 取得真值。

---

## 4. A10–A12：当前最需要后续作者裁决的一组

### A10 Non-Vanishing Continuation

**Reference expression**：operator trajectory information never fully disappears in L0；死亡后 generation-dependent information returns to latent potential；A10-C1 直接写“信息守恒于 L0”。

**Pressure from later hardening**：A13/PC-A 已明确：L0-abs inexhaustibility **不等于**其 content、cardinality 或 information amount 是 time invariant，并禁止裸 `H(L0_abs)` conservation reading。

因此存在一个真实 tension：

```text
A10:
information never fully disappears / information conserved in L0

vs

PC-A / A13:
non-exhaustion does not establish conserved L0 content or information amount
```

**Proposed role**：

```text
primary: historical formalization
secondary: conceptual bridge
legacy/superseded expression: OPEN CANDIDATE
```

**Disposition**：`AUTHOR-GATE LATER`。本审计不判 A10 false，也不自动删除；但它不能继续仅凭 Reference-Axiom 标签躲过 PC-A 后的重新说明义务。

**Specific future question**：A10 是否只想保留 `(3) OWN-HISTORY` 式“past occurrence is not erased”的薄历史直觉，还是坚持一个更强的 ontology-wide information-conservation thesis？两者必须拆开。

---

### A11 Ontological Fragility

**Reference expression**：`Stability ∝ 1/Psi_f`、`d ∝ ∂Entropy/∂Error`，并推出“只有 ontological fragility 才能 d>0”“纯软件 AI 若无法死亡则无法真正意识”。

**Pressure from current owners**：

- `_SRT_D_VALUE_CANONICAL.md` 已明确 `Def-d-canonical` 为 stake-coupled concern / irreversible-risk sensitivity 的 current core-facing anchor；`D_eff`、Fisher、error-like readings 均不得自动替代 canonical d；
- current AI routing increasingly把纯软件 AI 问题保留为 candidate/operational burden，而不是由单一 error sensitivity formula 直接封死。

**Proposed role**：

```text
primary: legacy/superseded expression (for the formulas as canonical definitions)
secondary: conceptual bridge
operational proxy: error/fragility readings only
```

**Disposition**：fragility/stakes intuition 可保留为 stronger conceptual bridge；`d ∝ error sensitivity` 不得继续作 canonical d definition；software-AI consciousness exclusion 需要独立 domain/bearer evidence。

---

### A12 Deep Continuity

**Reference expression**：跨尺度共享 selection–constraint–cost–history grammar；同时保留 `Complexity(G) ∝ Depth(d)`、物质/意识“慢/快”表达及 consciousness continuum conclusions。

**Current owner status**：21C 已把 scale consistency / ghost-operator universality 等明确放在 P3 bridge；严格 cross-scale identity 不再自动成立。

**Proposed role**：

```text
primary: conceptual bridge
secondary: domain formalization
legacy/superseded expression: strong matter/consciousness equivalence prose and unqualified continuum conclusions
```

**Disposition**：保留 shared-grammar comparison 候选；强 identity / continuum 结论只能在 domain deep well 另付证据。

---

## 5. A13–A16 与 Ax-L0-Bootstrap：已经部分自我修正的一组

### A13 Potential Inexhaustibility

**Current expression**：有限 L1/L2 manifestation/formal projection 不穷尽 L0-abs；明确不再主张 L0-abs content/cardinality/information amount time-invariant。

**Proposed role**：

```text
primary: conceptual bridge
secondary: historical formalization
```

**Disposition**：KEEP AS current boundary-bearing theory statement；不是 Constitution axiom，但与 `(1)/(4)` 的 non-preformation / non-exhaustion guards 可形成 commentary relation。

---

### Ax-L0-Bootstrap / Primitive Actualisation Boundary

**Current expression**：明确 actualisation kernel 由 P0-01 primitive 承载，fixed point/argmin/min-friction 不推导 first actualisation。

**Current owner status**：21A P0-01 是更直接 formal-core owner。

**Proposed role**：

```text
primary: historical formalization
secondary: conceptual bridge
```

**Disposition**：Reference copy 作为 compatibility/backlink surface；formal owner 优先回 21A。

---

### A15 Ghost-operator cross-scale compatibility candidate

**Reference file itself already says**：`P3 bridge A15`，不是 supplementary axiom；要求声明 state spaces、scale maps、observables、norms、tolerance 与 failure cases。

**Current owner status**：21C P3-B06/P3-B07。

**Proposed role**：

```text
primary: conceptual bridge
secondary: domain formalization
```

**Disposition**：KEEP; only taxonomy/navigation debt remains. Its old number `A15` must not be read as axiom hardness.

---

### A16 Psi_f as Generative Principle

**Reference expression**：all dynamics generated by inter-operator Psi_f; Fisher metric interaction form; “no Psi_f -> no dynamics -> no reality generation”.

**Current owner status**：21C explicitly classifies former Ax-F-12 as `P2/P3` canonical interpretation + Fisher-geometry borrowing. `_SRT_PSI_F_CANONICAL.md` also forbids bare Fisher identity and treats geometry as projection.

**Proposed role**：

```text
primary: legacy/superseded expression (as axiom/universal mechanism)
secondary: conceptual bridge
domain formalization / operational proxy: Fisher interaction forms
```

**Disposition**：the payability/friction generative intuition may remain a bridge; universal “all dynamics” and Fisher formal mechanism require domain/bridge status, not Reference Axiom authority.

---

### A14 Dual-Criterion Arrow of Time

**Reference expression**：time arrow = nested L2 record increment + integrated Psi_f payment ledger.

**Current relation**：21B P1-T02 owns a different, thinner ontological-time formalization; Reference A14 is a stronger dual-criterion model and is not automatically inherited by P1-T02.

**Proposed role**：

```text
primary: historical formalization
secondary: conceptual bridge / domain formalization
```

**Disposition**：`OWNER-GAP / AUTHOR-GATE LATER`。Future audit must decide whether A14 is a useful stronger model, a historical alternative, or a domain-specific realization. It does not gain P1 from the word “Axiom”.

---

## 6. Derived-Theorem index in Reference Axioms

The bottom theorem table contains `T-Scale`, `T-Causal`, `T-Holo`, `T-Phase`, `P3-Scale`, `T-Gen`.

**Disposition rule**：do not infer current hardness from the `T-*` label.

- scale compatibility -> current 21C P3 owners;
- causality -> current 21B P1-T01, with narrower boundary;
- holography -> 21C P3/P4;
- generative Psi_f -> 21C P2/P3;
- phase-transition / other formulas require their current owner / domain evidence.

Thus the theorem table is primarily:

```text
historical formalization / navigation
```

not an independent source of theorem-level authority.

---

## 7. Section disposition summary

| Item | Proposed primary role | Current action |
|---|---|---|
| A1 | historical formalization | defer to 21A formal owner |
| A2 | historical formalization | keep boundary; defer to 21A |
| A3 | legacy/superseded expression as unrestricted axiom | defer to 21B P1-T01 |
| A4 | conceptual bridge | retain; domain realization later |
| A5 | historical formalization | fixed-point form is model, downward role to 21B |
| A6 | legacy/superseded expression as axiom | 21C P2/P3 |
| A7 | domain formalization | 21C P3/P4 |
| A8 | domain formalization | owner/domain audit required |
| A9 | domain formalization | 21C P3/P4 |
| A10 | historical formalization; legacy candidate | author gate later |
| A11 | legacy/superseded formula + conceptual bridge | d/AI domain audit later |
| A12 | conceptual bridge | strong identity prose legacy candidate |
| A13 | conceptual bridge | keep as non-exhaustion boundary |
| Ax-L0-Bootstrap | historical formalization | defer to 21A P0-01 |
| A15 | conceptual bridge/domain formalization | already P3 bridge |
| A16 | legacy/superseded expression as axiom | 21C P2/P3; Fisher projection only |
| A14 | historical formalization | owner gap / author gate later |

---

## 8. Genuine author gates exposed by this audit

This pass deliberately does **not** ask the author to decide them yet, but records the future gates:

### Gate RA-1 — A10 continuation strength

Choose later between at least:

```text
thin:
past occurrence/history is not erased by later state restoration

strong:
trajectory information is ontologically conserved in L0 beyond bearer termination
```

Constitution `(3)` only licenses the thin question/guard; it does not decide the strong thesis.

### Gate RA-2 — A14 time model role

Is the dual-criterion `nested L2 record + Psi_f ledger` intended as:

```text
historical model
conceptual bridge
or current formal theory claim?
```

### Gate RA-3 — A8 life localization

Does probability-localization remain an active biology-domain hypothesis, or is it historical formalization with no current owner?

No gate requires immediate theory change; the next read-only target remains `SRT_Reference_Ontology.md`.
