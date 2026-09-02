---
id: SRT-CONSTITUTION-PHASE6-CORE-ROLE-RECLASSIFICATION-PASS1-20260902
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
  - Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md
  - Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md
  - Governance/SRT_CANONICAL_FREEZE.md
  - CANONICAL_REGISTRY.md
tags: [Constitution, Phase6, Core, CoreLaw, EpistemicRole, Audit]
---

# Phase 6 — Core/Core_Law epistemic-role reclassification audit, Pass 1

> **性质**：只读角色审计。本文不修改任何既有 Core/Core_Law 文件的 canonical status、claim level、定义、方程或引用优先级。
>
> **授权边界**：`SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md` Phase 6 明确要求先做 file-by-file role map，并明确规定“Any substantive canonical rewrite is a later C-class decision and must be separately authorized.”
>
> **解释边界**：本文的 `proposed role` 是下一阶段治理/架构重构的建议，不是现时 authority override。直到后续单独作者裁决与高风险编辑完成，当前 `CANONICAL_REGISTRY.md`、`SRT_CANONICAL_FREEZE.md` 和各文件 frontmatter 继续决定实际引用行为。

---

## 1. Phase 6 分类表

本审计沿用 execution plan 的七类角色：

```text
constitutional source/commentary
conceptual bridge
domain formalization
operational proxy
historical formalization
manuscript dependency
legacy/superseded expression
```

允许一个文件同时有 primary / secondary roles。目录名 `Core` / `Core_Law` 不决定 epistemic role。

额外使用两个**非理论角色标签**帮助阅读：

```text
navigation / registry
protected-current-authority
```

它们不替代七类理论角色，只记录工程状态。

---

## 2. 总体发现

### F1. 旧架构的核心问题不是“Core_Law 太高”，而是多种知识角色共居同一 canonical surface

当前主干文件常把下列内容放在同一文件：

```text
author-origin philosophical intuition
canonical metaphysical commitment
formal encoding
cross-domain mapping
operational proxy
governance usage rule
historical hardening note
```

新 Constitution 的重构意义不是把这些全部删除，而是取消：

```text
formal/canonical owner
-> therefore constitutional floor
```

这一旧推论。

### F2. 新 Constitution 与旧 Core 的关系应是“问题入口 -> 理论对象化”，不是“旧 L0 -> Constitution 推导”

新的 v1 core 使用 reader-executable perspective operations。旧 Core/Core_Law 文件因此应被重新理解为：对这些问题做出的不同强度、不同年代、不同域依赖的理论对象化。

### F3. `canonical` 与 epistemic role 必须继续分开

当前 registry 已经区分 governance-canonical、theory-canonical、operational proxy 与 bridge hypothesis。Phase 6 不废弃这个成果，而是进一步把它从“文件优先引用等级”扩展到“文件在 Constitution/Domain 架构中的知识角色”。

---

## 3. Priority 1 — Constitution / Seven Theses / Core Text / L0 prose

### 3.1 `Core_Law/SRT_L0_Metaphysics.md`

**Current self-role**：unique L0 metaphysical anchor；自称所有上层形式化/领域映射的上游约束面。

**Observed composition**：

- 强哲学 source/commitment：selection-first、存在非预给定、选择不必预设选择者；
- 构造性理论承诺：primitive actualisation、anchoring、Stable ISP 的层级关系；
- 历史/时间理论：不可撤回性、ontological time；
- 后期 hardening：`kappa_0`、`epsilon`、Gate 0、术语/层级修订记录；
- 形式 owner 回链与 historical supersession notes。

**Proposed primary role**：`constitutional source/commentary`。

**Proposed secondary roles**：

```text
conceptual bridge
historical formalization
```

**Not proposed**：把整文件继续作为 Constitution v1 的唯一上游地基。

**Reason**：v1 Constitution 已不从 L0 四命题推导；但 L0 中大量 author-origin intuition 与后续理论 hardening 仍是解释 SRT 为何发展成当前形式的重要 source/commentary。

**Future action**：`ROLE-SPLIT CANDIDATE`。未来若作者授权，可把“source/commentary”与“stronger theory commitments / historical formalization”在导航和引用层分开；不建议当前直接删改正文。

**Protection**：`SRT_CANONICAL_FREEZE.md` A 类。任何 substantive 改写需单独高风险授权。

---

### 3.2 `Core_Law/SRT_Constitution_Seven_Theses.md`

**Current self-role**：L1 Constitution digest，且明确要求每条 Thesis 从 L0 四命题推导。

**Constitution-v1 conflict shape**：新 Constitution 的身份恰好取消了这一派生结构。

**Proposed primary role**：`legacy/superseded expression`。

**Proposed secondary role**：`constitutional source/commentary`。

**Specific supersession**：

```text
Seven Theses as active Constitution authority
-> superseded by SRT Constitution v1
```

不等于：

```text
all Seven Theses prose is false or useless
```

其中关于 selection-first、operator-bound access、objectivity/convergence、friction、subjectivity 等段落仍可作为旧架构如何理解 SRT 的历史/解释性材料。

**Future action**：未来可把 frontmatter/status/registry role 改为 legacy constitutional commentary；不建议把全文删除。

---

### 3.3 `Core_Law/SRT_Core_Text_CN_Euclid.md`

**Current self-role**：中文自足主论证候选；显式区分 A/O/D/S/C/H/E 七类负担；当前仍写为依赖 L0。

**Proposed primary role**：`conceptual bridge`。

**Proposed secondary role**：`historical formalization`。

**Reason**：它不是 Constitution reader operation，而是一条从公设/观察/定义向 SRT 强理论结论推进的 argument architecture。其价值在于把理论负担显式化，而不是作为 Constitution floor。

**Important pressure**：其 A1 “方向公设”及下游 normative conclusions 必须在未来与 Constitution `(6)` 的“评价判断不免检”重新对照；这不预判 A1 错误，只改变其进入理论的说明义务。

**Future action**：保持正文不动；Phase 6 后续单独标出哪些步骤是 conceptual bridge，哪些是 historical formalization，哪些需要 domain evidence。

---

### 3.4 `Core_Law/SRT_Core_Text_CN.md`

**Current self-role**：`legacy_v1` 中文自足论证原版；仍保留读者入口价值。

**Proposed primary role**：`legacy/superseded expression`。

**Proposed secondary role**：`conceptual bridge`。

**Reason**：文件自身已经承认不再承担唯一入口；其“公设 -> 推导 -> 解释力”仍代表 SRT 一个重要历史 argument form，但不再是 Constitution 或理论总入口。

**Future action**：保留历史可读性；未来导航应将它排在 v1 Constitution 与当前 active argument bridge 之后。

---

### 3.5 `Core_Law/SRT_Selection_Argument.md`

**Current self-role**：selection-first 第一命题的哲学辩护与 objection handling。

**Proposed primary role**：`conceptual bridge`。

**Proposed secondary role**：`constitutional source/commentary`。

**Reason**：它适合回答“为什么要认真考虑 selection-first”，但其量子、意识、规范性、秩序等展开包含比 Constitution 更强的理论/领域主张。它应作为 argument/commentary，而不是由“哲学辩护”直接取得 Constitution authority。

**Future action**：后续按六个 Constitution probe 标记其段落：哪些是 source resonance，哪些是 stronger theory claim，哪些属于 domain-facing bridge。

---

## 4. Priority 2 — Core 21 P0/P1/P2-P4 structure

### 4.1 `Core/SRT_Core_21_Formal_Axioms.md`

**Current self-role**：split Core 21 的 index；已经明确“file role != claim hardness”。

**Proposed primary role**：`historical formalization`（index）。

**Secondary engineering role**：`navigation / registry`。

**Reason**：该文件自身已经完成一次重要降混层工作。Phase 6 不需要把它恢复成理论正文；它最适合继续做旧 formal-core 架构的索引和 claim-hardness 路由。

**Future action**：低优先级。主要是未来把“P0 primitive”改读为“formal-core primitive within that model”，避免被误作 Constitution primitive。

---

### 4.2 `Core/SRT_Core_21_Minimal_Axioms.md`

**Current self-role**：P0 primitive axioms only；包含 selection-first、L0/L1/L2、operator、Psi_f、d 等 formal vocabulary 与 primitive actualisation kernel。

**Proposed primary role**：`historical formalization`。

**Proposed secondary role**：`conceptual bridge`。

**Reason**：P0 在 claim ladder 内仍可表示“这个 formal core 不再向下证明的 primitive”，但新 Constitution 明确禁止把 formalization 当 constitutional floor。因此：

```text
P0 primitive inside current formal core
!=
Constitution primitive
```

**Future action**：不改 P0 数学；未来在 role note/registry 中明确这是“formal-model primitive set”，而不是 v1 Constitution 的上游公理集。

---

### 4.3 `Core/SRT_Core_21b_Constitutive_Theorems.md`

**Current self-role**：P1 internal consequences once P0 is granted。

**Proposed primary role**：`conceptual bridge`。

**Proposed secondary role**：`historical formalization`。

**Reason**：P1-T01 causality projection、P1-T02 ontological time、P1-T03 L2 downward constraint、P1-T04 information creation 都是强理论结构，不是 Constitution reader probe；它们的“constitutive”只在当前 formal core 的前提系统内部成立。

**Future action**：逐 theorem 进入后续 Domain/bridge audit，而不是整文件继续由“P1”获得跨域 ontological immunity。

---

### 4.4 `Core/SRT_Core_21c_Bridge_Hypotheses.md`

**Current self-role**：P2/P3/P4 bridge / interpretation / empirical threshold bundle。

**Proposed primary role**：`conceptual bridge`。

**Proposed secondary roles**：

```text
domain formalization
operational proxy
```

**Reason**：当前文件已经基本符合新架构，其 own-use rule 明确禁止 bridge claims 回升 P0/P1。

**Future action**：`KEEP ROLE / ROUTING CLEANUP`。优先清理下游引用错误，而不是改本文件理论。

---

## 5. Priority 3 — Core 22 equations

### 5.1 `Core/SRT_Core_22_Equations.md`

**Current self-role**：master dynamics / thermodynamics / stability equations anchor；内部已经混合 primary equations、collective equations、bridge/proxy equations。

**Proposed primary role**：`domain formalization`。

**Proposed secondary roles**：

```text
operational proxy
historical formalization
```

**Reason**：方程层是 Domain 支付答案的一种工具，不再反向定义 Constitution。文件自身已明确许多 Fisher/Hessian/neural 表达只是 proxy / bridge，这与新 Constitution 架构高度兼容。

**High-pressure examples**：

- `Def-Protocol-*`：理论模型结构，不是 Constitution；
- collective free-energy landscape：cross-scale/domain formalization；
- `D_eff` / Hessian effective dimension：capacity proxy；
- Fisher-induced Psi_f：local projection/proxy。

**Future action**：后续应逐 equation block 标 primary formal model / bridge / proxy，而不是把整个 `Core_22` 统一读作 theory-canonical equation truth。

**Protection**：canonical freeze A 类；不得在本 Phase 6 audit 中改方程。

---

## 6. Priority 5 — d / Psi_f / T_dir

### 6.1 `_SRT_D_VALUE_CANONICAL.md`

**Current self-role**：repo-wide d usage anchor；同时承担 semantic definition、scalar default、proxy gates、cross-domain usage rules。

**Proposed primary role**：`conceptual bridge`。

**Proposed secondary roles**：

```text
operational proxy
historical formalization
```

**Key split**：

```text
stake / concern / consequence-return semantic burden
-> conceptual bridge

D_eff / Fisher / d-vector / d-gate
-> operational proxy

bare-d scalar canonical default / cross-file usage rule
-> governance stabilization, not ontological proof
```

**Reason**：d 不进入 Constitution 定义。它可以成为 domain/bearer theory 对 `(3)/(5)/(6)` 等问题的一种 stronger answer，但必须重新支付 same-unit consequence、stake coupling、scale/boundary 等条件。

**Future action**：未来优先做 semantic-anchor vs proxy split audit，不先重写公式。

---

### 6.2 `_SRT_PSI_F_CANONICAL.md`

**Current self-role**：Psi_f semantic anchor + formal working form + cross-scale working invariant；并明确 Fisher/geometry/metabolic readings 是 projection/proxy。

**Proposed primary role**：`conceptual bridge`。

**Proposed secondary roles**：

```text
operational proxy
domain formalization
historical formalization
```

**Key split**：

```text
payability / resistance intuition
-> conceptual bridge

Fisher-Rao / path / metabolic / experimental readings
-> domain formalization or operational proxy

repo-wide default main reading
-> governance stabilization
```

**Reason**：Constitution 不需要 Psi_f 才能运行；Psi_f 是 SRT 对“约束/支付/稳定”等下游问题的一种理论对象化，不应再作为 Constitution admission 条件。

**Future action**：后续 domain deep well 决定哪些 Psi_f realizations productive，哪些只是 translation/proxy。

---

### 6.3 `_SRT_T_DIR_CANONICAL.md`

**Current self-role**：已经自降为 v0 operational proxy / governance-canonical working object；但同文件仍含较强“价值内嵌于选择”“秩序方向”等历史哲学主张。

**Proposed primary role**：`operational proxy`。

**Proposed secondary roles**：

```text
conceptual bridge
legacy/superseded expression
```

**Reason**：Def-T-1 的 readability/reorientation functional 是可操作工作对象；而早期“选择内在指向秩序/价值内嵌”段落与当前 L0 Gate 0、Constitution `(6)` 的边界之间存在明显历史层差，不能因同文件而获得同等 authority。

**Future action**：高优先级做 intra-file role split；保留 T_dir proxy owner，同时把旧 strong-value prose 明确标为 historical/bridge unless independently re-adjudicated。

---

## 7. Reference layer — highest mixed-role pressure

### 7.1 `Core_Law/SRT_Reference_Axioms.md`

**Current self-role**：L1 formal axioms mapping from L0；包含 axioms、equations、domain-like interpretations。

**Proposed primary role**：`historical formalization`。

**Proposed secondary roles**：

```text
conceptual bridge
domain formalization
```

**Reason**：该文件典型体现旧架构“L0 -> Reference formalization -> domain”。A1/A2、causality-as-projection、embodiment、L2 closure、information-existence 等强弱不一，却共居 `axiom_set` surface。新 Constitution 不允许它继续充当 constitutional floor。

**Follow-up**：逐 Axiom 审计已写入 `Operations/Audits/SRT_CONSTITUTION_PHASE6_REFERENCE_AXIOMS_SECTION_AUDIT_2026-09-02.md`。该 pass 暴露 A10 continuation strength、A14 time-model role、A8 life-localization 三个未来 author gates，但没有执行任何理论改写。

---

### 7.2 `Core_Law/SRT_Reference_Ontology.md`

**Current self-role**：L1 formal ontology mapping；同时包含 set/equation definitions、topological projections、physics/math/spirituality realization table、neural/phenomenal readings。

**Proposed primary role**：`historical formalization`。

**Proposed secondary roles**：

```text
domain formalization
conceptual bridge
```

**Reason**：它比 Reference Axioms 更明显地把“形式定义”和“跨域 realization”装在同一 ontology 文件中。`L0^{abs}`、free-energy definition、simplicial-complex realization、spirituality projection 等不能继续因“Reference Ontology”文件名而获得统一本体 authority。

**Future action**：`HIGHEST-PRIORITY ROLE SPLIT AUDIT`。后续应逐 section 识别：historical formalization / allowed domain model / bridge analogy / legacy expression。

---

## 8. Manuscript / publication carve-out

本 Pass 不给上述文件自动贴 `manuscript dependency`，除非后续找到具体 active manuscript dependency edge。

但 programme-level carve-out 已冻结：

- Frontiers 1837760 已发表，作为 domain artifact / historical formalization context；
- *Costly Selective Closure* / Adaptive Behavior 已投稿，受 manuscript carve-out 保护；
- 新 role map 不追溯改写其 framing、公式或依赖，除非期刊提出明确要求。

因此即使某 canonical owner 未来被重分类，也必须区分：

```text
repository future role
!=
retroactive manuscript rewrite
```

---

## 9. Pass-1 disposition table

| File | Proposed primary role | Secondary role(s) | Priority | Current edit disposition |
|---|---|---|---|---|
| `Core_Law/SRT_L0_Metaphysics.md` | constitutional source/commentary | conceptual bridge; historical formalization | HIGH | protected / no edit |
| `Core_Law/SRT_Constitution_Seven_Theses.md` | legacy/superseded expression | constitutional source/commentary | HIGH | role change later |
| `Core_Law/SRT_Core_Text_CN_Euclid.md` | conceptual bridge | historical formalization | MED-HIGH | no edit |
| `Core_Law/SRT_Core_Text_CN.md` | legacy/superseded expression | conceptual bridge | MED | no edit |
| `Core_Law/SRT_Selection_Argument.md` | conceptual bridge | constitutional source/commentary | MED-HIGH | no edit |
| `Core/SRT_Core_21_Formal_Axioms.md` | historical formalization index | navigation | LOW | keep / routing cleanup later |
| `Core/SRT_Core_21_Minimal_Axioms.md` | historical formalization | conceptual bridge | HIGH | protected / no edit |
| `Core/SRT_Core_21b_Constitutive_Theorems.md` | conceptual bridge | historical formalization | HIGH | protected / no edit |
| `Core/SRT_Core_21c_Bridge_Hypotheses.md` | conceptual bridge | domain formalization; operational proxy | LOW-MED | mostly keep |
| `Core/SRT_Core_22_Equations.md` | domain formalization | operational proxy; historical formalization | HIGH | protected / no edit |
| `_SRT_D_VALUE_CANONICAL.md` | conceptual bridge | operational proxy; historical formalization | HIGH | protected / split audit later |
| `_SRT_PSI_F_CANONICAL.md` | conceptual bridge | operational proxy; domain formalization; historical formalization | HIGH | protected / split audit later |
| `_SRT_T_DIR_CANONICAL.md` | operational proxy | conceptual bridge; legacy expression | HIGH | protected / intra-file split audit |
| `Core_Law/SRT_Reference_Axioms.md` | historical formalization | conceptual bridge; domain formalization | VERY HIGH | section audit completed; no edit |
| `Core_Law/SRT_Reference_Ontology.md` | historical formalization | domain formalization; conceptual bridge | VERY HIGH | no edit; section audit next |

---

## 10. What this Pass changes / does not change

### Changes now

Only one thing changes at the audit level:

> We now have a proposed file-role map that can guide the next read-only section audits.

### Does not change now

```text
canonical priority
claim level
formal definitions
equations
file paths
published/submitted manuscript framing
```

All substantive canonical changes remain separately author-gated.

---

## 11. Next read-only passes

Recommended order:

1. **Reference Ontology section audit** — separate ontology-language, historical formalization, domain realization and analogy.
2. **L0 intra-file audit** — identify source/commentary core vs stronger theory/historical-formalization blocks.
3. **d / Psi_f / T_dir intra-file audit** — semantic burden vs formalization vs proxy vs governance usage.
4. **Core 21A/21B theorem-to-Constitution coverage map** — identify which formal claims answer which Constitution probe and which remain independent domain hypotheses.
5. Only after those maps exist should the author be asked for any actual canonical role change.
