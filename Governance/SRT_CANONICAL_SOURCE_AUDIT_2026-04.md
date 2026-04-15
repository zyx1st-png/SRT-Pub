---
id: SRT-CANONICAL-SOURCE-AUDIT-2026-04
type: audit
tags: [Canonical, Audit, AI-Readability, Drift]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CANONICAL-REGISTRY, SRT-EXPLANATION-PROTOCOL, SRT-INDEX]
ai_role: canonical
ai_priority: 2
ai_do_not_use_for_definition: false
---

# SRT Canonical Source Audit (2026-04)

## 目的

本文件用于记录当前仓库中，**规范源（canonical source）与治理/导航/历史文本之间可能造成 AI 漂移或幻觉的冲突点**。

它不是新的理论定义源，而是：
- 帮助后续清理 canonical source 冲突；
- 帮助 AI/agent 区分“当前规范锚点”与“旧引用残留”；
- 帮助人工后续做低风险 patch。

---

## 当前最高优先规范源

对于当前仓库，核心概念默认优先级如下：

1. `CANONICAL_REGISTRY.md`
2. `_SRT_D_VALUE_CANONICAL.md`
3. `_SRT_PSI_F_CANONICAL.md`
4. `_SRT_T_DIR_CANONICAL.md`
5. `Core/SRT_Core_21_Formal_Axioms.md`
6. `Core/SRT_Core_22_Equations.md`
7. `Core_Law/SRT_L0_Metaphysics.md`

若旧文件、治理文件、bridge 文件或长文与以上锚点发生冲突，以此处顺序为准。

---

## 已识别冲突点

### A1. d-value canonical 锚点残留冲突

- **当前规范口径**：`CANONICAL_REGISTRY.md` 已将 `d-value` 的主锚点固定为 `_SRT_D_VALUE_CANONICAL.md`。
- **冲突来源**：`Governance/_SRT_EXPLANATION_PROTOCOL.md` 中仍写有 `d 值 canonical 定义锚定：AI/SRT_AI_01_Ontology.md` 的旧残留。
- **风险**：
  - AI 可能在不同上下文中抓取不同的“权威定义源”；
  - 旧的 AI Ontology 文件可能被误当作 d-value 的最终规范锚点；
  - 回答时更容易混入历史展开层语言，而不是当前 canonical 口径。
- **建议修正**：
  - 将 `Governance/_SRT_EXPLANATION_PROTOCOL.md` 中相关条目改为：`d 值 canonical 定义锚定：_SRT_D_VALUE_CANONICAL.md`。
- **优先级**：P1

---

## AI 读取时的临时判定规则

在上面的冲突完全清理前，AI/agent 应采用以下临时规则：

1. 若 `Governance` 文件与 `CANONICAL_REGISTRY.md` 冲突，优先相信 `CANONICAL_REGISTRY.md`。
2. 若某概念同时出现在：
   - canonical 文件
   - bridge 文件
   - 长文展开层
   - 历史中文主文
   则默认只有 canonical 文件能作为最终定义源。
3. `AI/SRT_AI_01_Ontology.md` 对 `d-value` 仍有重要展开价值，但**不再**单独承担其最终规范权。

---

## 后续清理建议

### 低风险清理顺序
1. 修 `Governance/_SRT_EXPLANATION_PROTOCOL.md` 的 d-value 锚点。
2. 扫描 `Governance/` 中是否还有旧 canonical 残留。
3. 扫描 `split / compact / bridge` 是否仍出现“替代规范源”的旧句式。
4. 后续考虑在 `_SRT_MANIFEST.yaml` 中显式增加：
   - `ai_role`
   - `ai_priority`
   - `ai_do_not_use_for_definition`
   - `canonical_of`
   - `supersedes`

---

## 当前结论

目前仓库在“AI 可读性”和“低漂移”方面已经有较强基础，但仍存在少量**旧 canonical 残留**。  
当前最值得优先修复的冲突，是：

- `d-value` 的规范锚点已收口到 `_SRT_D_VALUE_CANONICAL.md`；
- 但部分治理文件仍残留旧的 `AI/SRT_AI_01_Ontology.md` 口径。

在这类冲突清理完成前，AI/agent 不应仅凭单个治理文件来决定理论权威源。
