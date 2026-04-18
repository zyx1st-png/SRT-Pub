---
id: SRT-REPO-OPT-2026-04
type: framework
tags: [Governance, Optimization, AI-Readability, Execution]
status: planning_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-STATUS, SRT-INDEX, SRT-GOVERNANCE-README, SRT-OPERATIONS-README]
---

# SRT 仓库优化执行计划（2026-04 修订版）

## 0. 目的

本文件用于把当前一轮“仓库优化方案”改写成**适配现状的执行版**。

目标不变：

1. 降低 AI 会话 token 消耗
2. 降低入口漂移与权威混淆
3. 收口运行协议，减少多模型各自摸索
4. 补齐对外总入口

但执行顺序与局部设计，必须服从当前仓库的真实结构，而不是按理想化空仓库重排。

---

## 1. 当前仓库现实约束

### 1.1 入口层已经存在，不应重复造轮子

当前根目录已形成一组实际在用的入口：

- `AGENTS.md`：运行协议主入口
- `STATUS.md`：会话状态面板
- `_SRT_INDEX.md`：机器索引
- `SRT_Navigation_Map.md`：人类阅读地图
- `SRT_Quick_Start.md`：通用 onboarding
- `SRT_AI_START.md`：AI 最小首读入口
- `SRT_1H_Onboarding.md`：人类深一点的入门包

因此后续优化原则是：

- **减少入口重叠**
- **不新增功能重复的入口文件**

而不是为了“形式完整”再造第二套。

### 1.2 根目录过厚，但不宜一步硬切

当前根目录非隐藏文件数量较高，且多份入口、注册表、专题入口与历史单文并存。

因此第一轮应采取：

- **先降权**
- **再搬家**

不做大规模物理迁移。

### 1.3 manifest 目前还不能直接升格为一级权威入口

`_SRT_MANIFEST.yaml` 当前仍有旧路径/缺项残留，例如：

- `_SRT_ATOMIC_MAP.md`
- `_SRT_DOC_ENGINEERING_GUIDE.md`
- `SRT_INTERNAL_OPTIMIZATION_PLAN_2026Q1.md`
- `_SRT_SIGNAL_PIPELINE.md`

这意味着 manifest 在清理前更适合作为“待修的机器清单”，而不是第一轮就抬成稳定根入口。

### 1.4 STATUS 确实过重

`STATUS.md` 当前兼做：

- 会话入口
- 最近状态摘要
- 历史增量面板
- 材料审查留痕聚合点

这会让它在“应短读”的角色上超载。

### 1.5 运行噪声分层还不够硬

当前 `Operations/` 中仍包含高可见度的 raw session / compilation / residual 文件。

这不是说它们无用，而是说明：

- 运行留痕层与理论检索层还没有被足够明确地区分

### 1.6 frontmatter 主 schema 已经成形

当前仓库广泛使用：

- `layer`
- `epistemic_layer`
- `claim_mode`
- `dependency`

因此本轮应：

- 延续现有主 schema
- 只加少量兼容字段
- 避免再造一套平行状态体系

---

## 2. 本轮明确采纳的决策

### 2.1 采纳：冻结层与编辑协议

应新增：

- `Governance/SRT_CANONICAL_FREEZE.md`
- `Governance/SRT_EDIT_PROTOCOL.md`
- `Governance/SRT_HARNESS_TESTS.md`

这是低风险高收益项。

### 2.2 采纳：新增 `README.md`

根目录缺公开入口，这一项应尽快补。

### 2.3 采纳：新增 `CLAUDE.md`

但其角色必须是：

- Claude 兼容包装层
- 显式声明 `AGENTS.md` 为运行协议主源
- 不创建第二套独立 harness

### 2.4 采纳：`STATUS.md` 瘦身

方向正确，应执行。

### 2.5 采纳：raw session 归档

方向正确，应执行，但以“低风险迁移 + 回链说明”为原则。

### 2.6 采纳：Quick Reference 试点

值得做，但先从高传播、高误读风险文档开始，不做全库铺开。

### 2.7 采纳：入口角色表

应在 `README.md`、`AGENTS.md`、`CLAUDE.md` 中明确以下分工：

- `README.md`：对外总入口
- `AGENTS.md`：运行协议主入口
- `CLAUDE.md`：Claude 兼容入口
- `STATUS.md`：当前状态面板
- `_SRT_INDEX.md`：机器索引
- `SRT_Navigation_Map.md`：人类阅读地图
- `SRT_AI_START.md`：AI 最小首读入口
- `_SRT_SYMBOL_TABLE.md`：符号规范锚点

---

## 3. 本轮明确不采纳或暂缓的设计

### 3.1 暂不新增 `STATUS_SHORT.md`

原因：

- 仓库已经有 `SRT_AI_START.md`
- 若立即再加 `STATUS_SHORT.md`，只会再次增加入口数量

执行原则：

- 先瘦身 `STATUS.md`
- 再判断是否仍需要短版状态页

### 3.2 不让 `CLAUDE.md` 成为第二 AI 首读中心

当前更稳的结构是：

- `AGENTS.md` 管运行协议
- `SRT_AI_START.md` 管 AI 最小骨架
- `CLAUDE.md` 只负责把 Claude 导向这两者

### 3.3 暂不把“根目录只保留 8 个文件”作为第一轮硬目标

第一轮只做：

- 根目录分层说明
- 一级入口降权
- 二级入口回链整理

等引用关系和 manifest 稳定后，再考虑物理下沉。

### 3.4 暂不把 `_SRT_MANIFEST.yaml` 抬成一级权威入口

先修 manifest，再决定是否升格。

### 3.5 不新增与现有 AI 字段冲突的新枚举

当前仓库已出现：

- `ai_role`
- `ai_priority`
- `ai_do_not_use_for_definition`

因此如果补 AI metadata，应兼容现有字段，不另起冲突枚举。

---

## 4. 修订后的执行顺序

## Phase 0：边界冻结

新增：

- `Governance/SRT_CANONICAL_FREEZE.md`
- `Governance/SRT_EDIT_PROTOCOL.md`

写清：

- canonical 不可直接改写层
- 可改但需 cross-check 的核心主文
- 运行/导航/状态文件的修改边界
- 本轮明确不做事项

## Phase 1：Harness 收口

新增/轻改：

- 新建 `CLAUDE.md`
- 轻改 `AGENTS.md`

目标：

- 明确 `AGENTS.md` 是运行协议主源
- 明确 `CLAUDE.md` 只是兼容包装
- 把 AI 首读路由收口到 `SRT_AI_START.md`

推荐最短 AI 首读顺序：

1. `AGENTS.md`
2. `SRT_AI_START.md`
3. `STATUS.md`
4. `_SRT_INDEX.md`
5. `_SRT_SYMBOL_TABLE.md`

`Operations/README.md` 与 `Governance/README.md` 保持为进入具体 pipeline 时再读。

## Phase 2：索引/manifest/registry 收口

本 phase 应前移，早于根目录瘦身。

处理对象：

- `_SRT_INDEX.md`
- `SRT_Navigation_Map.md`
- `CANONICAL_REGISTRY.md`
- `ANNEX_REGISTRY.md`
- `LONGFORM_SPLITS.md`
- `_SRT_MANIFEST.yaml`

目标：

- 明确谁是 machine index
- 明确谁是 human map
- 明确谁是 canonical registry
- 清理 manifest 的旧路径和漂移残留
- 其他文件只链接，不重复解释彼此职责

## Phase 3：README 与根目录最小工作面

新增：

- `README.md`

第一轮不大量搬家，只做：

- README 公开入口
- 根目录角色说明
- 一级/二级入口分层
- 不常驻文件的“降权而不迁移”

## Phase 4：STATUS 瘦身

处理对象：

- `STATUS.md`
- `Governance/_SRT_CHANGELOG_2026.md`

目标：

- `STATUS.md` 只保留状态面板、最近摘要、活跃待办
- 历史长滚动继续下沉到 changelog / history

## Phase 5：运行噪声归档

新增：

- `Archive/raw_sessions/`
- `memory/README.md`

处理对象：

- `Archive/raw_sessions/SRT_SESSION_RAW_TRANSCRIPT_*.md`
- `Archive/raw_sessions/SRT_SESSION_DIALOGUE_COMPILATION_*.md`
- 其他 raw / residual 运行留痕

同时补写：

- `Operations/README.md` 中“运行层不是理论权威层”的说明

## Phase 6：Quick Reference 试点

首批仅处理：

- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_22_Equations.md`
- `Core_Law/SRT_L0_Metaphysics.md`
- `Core_Law/SRT_Core_Text_CN_Euclid.md`
- `AI/SRT_AI_01_Ontology.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `Philosophy/SRT_Philosophy_Foundations.md`
- `Neuroscience/SRT_Neural_Mechanisms.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Physics/SRT_Physics_Cosmology.md`

固定模板：

```md
## Quick Reference
- Role:
- Core claim:
- Canonical status:
- Depends on:
- Used by:
- Safe edits:
- Do not change:
```

## Phase 7：Harness Tests

新增：

- `Governance/SRT_HARNESS_TESTS.md`

用途：

- 固定一组最小问答
- 测试 AI 是否仍误把日志当主文
- 测试 canonical / bridge / compact core 是否混淆

---

## 5. metadata 补充规则

本轮允许补充但不强推全库铺开的字段：

- `last_hardened`
- `canonical_source`
- `edit_risk`
- `summary_ready`

AI 字段若继续扩展，应优先兼容现有：

- `ai_role`
- `ai_priority`
- `ai_do_not_use_for_definition`

不建议本轮新增：

- 与 `dependency` 平行的 `depends_on`
- 与 `claim_mode` / `epistemic_layer` 平行的新状态主字段

---

## 6. 第一批直接开工文件

优先只动这些文件：

- `README.md`
- `CLAUDE.md`
- `AGENTS.md`
- `STATUS.md`
- `_SRT_INDEX.md`
- `SRT_Navigation_Map.md`
- `_SRT_MANIFEST.yaml`
- `Operations/README.md`
- `memory/README.md`
- `Governance/SRT_CANONICAL_FREEZE.md`
- `Governance/SRT_EDIT_PROTOCOL.md`
- `Governance/SRT_HARNESS_TESTS.md`

本轮暂不碰理论正文主链定义。

---

## 7. 验收标准

完成本轮后，应至少满足：

1. 新 AI 首读时，不再需要同时吞 `STATUS + INDEX + Navigation + Quick_Start` 才能定位权威入口。
2. `AGENTS.md`、`CLAUDE.md`、`SRT_AI_START.md` 之间不再出现双 harness 竞逐。
3. `STATUS.md` 明显变短，历史滚动不再挤占会话入口。
4. raw session 从 `Operations/` 主工作面降权。
5. `_SRT_MANIFEST.yaml` 不再含明显失效路径。
6. AI 能稳定答出：
   - L0 唯一锚点
   - d-value canonical 去哪看
   - Ψ_f canonical 去哪看
   - 运行协议主入口是哪篇
   - 人类阅读地图是哪篇
   - 机器索引是哪篇
   - AI 最小首读入口是哪篇

---

## 8. 当前结论

这轮优化可以做，而且值得做。

但最稳的版本不是“从零搭新骨架”，而是：

- 承认仓库已经形成的真实入口生态
- 保留其中稳定的部分
- 削掉重复职责
- 先清权威关系，再做物理迁移

简化说：

- **保留 `AGENTS.md`**
- **利用 `SRT_AI_START.md`**
- **新增 `README.md` 与 `CLAUDE.md`**
- **瘦身 `STATUS.md`**
- **前移 manifest/index 清理**
- **最后再处理大规模入口压缩**
