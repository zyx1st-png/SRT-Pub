# CLAUDE.md

本文件是 SRT 仓库给 Claude / Claude Code 的兼容包装层。

**运行规范以 [AGENTS.md](AGENTS.md) 为主。**
本文件不创建第二套独立 harness，只负责把 Claude 导向现有入口。

## 必读顺序

**Fresh-session read order 唯一以 [AGENTS.md](AGENTS.md) §Session Start 为准，本文件不复制或扩展必读列表。**（当前为 3 个 bootstrap 必读文件；`_SRT_INDEX.md`、`_SRT_SYMBOL_TABLE.md` 等均为按任务条件加载，条件同样由 AGENTS.md 定义。）

以下为**任务触发后的条件加载**，不属于基础 bootstrap：

- 公开/对外 framing → [README.md](README.md)
- 具体 pipeline、治理或运行留痕 → [Operations/README.md](Operations/README.md)、[Governance/README.md](Governance/README.md)、`memory/YYYY-MM-DD.md`（仅当存在时读，缺席属正常）、[HEARTBEAT.md](HEARTBEAT.md)（仅 heartbeat / automation 工作）
- `01_Source_Intuition/BOOK/` 下的书籍写作、修订、翻译、评审、结构调整或章节判断 → 必须额外读 [01_Source_Intuition/BOOK/TASTE.md](01_Source_Intuition/BOOK/TASTE.md)（书籍层面的气质、审美、语言禁忌与写作判断覆盖层，不替代理论 canonical 定义源）

理论推进、书籍写作、领域深挖、材料融合、public release 或仓库治理任务，先用 [_SRT_AGENT_RETRIEVAL_PROFILE.md](_SRT_AGENT_RETRIEVAL_PROFILE.md) 判定检索 profile。`canonical: false` 只表示不能替代定义源，不表示不值得读取。

## 权威层级

默认优先级：

1. [CANONICAL_REGISTRY.md](CANONICAL_REGISTRY.md)
2. [Core_Law/SRT_L0_Metaphysics.md](Core_Law/SRT_L0_Metaphysics.md)
3. [_SRT_D_VALUE_CANONICAL.md](_SRT_D_VALUE_CANONICAL.md)
4. [_SRT_PSI_F_CANONICAL.md](_SRT_PSI_F_CANONICAL.md)
5. [_SRT_T_DIR_CANONICAL.md](_SRT_T_DIR_CANONICAL.md)
6. [_SRT_SYMBOL_TABLE.md](_SRT_SYMBOL_TABLE.md)
7. [Core/SRT_Core_21_Formal_Axioms.md](Core/SRT_Core_21_Formal_Axioms.md)
8. [Core/SRT_Core_22_Equations.md](Core/SRT_Core_22_Equations.md)

以下文件不是最终定义源：

- bridge 文件
- split / annex 导航文件
- `Operations/` 运行日志
- `memory/` 短时上下文
- `01_Source_Intuition/BOOK/TASTE.md`

但这些文件可作为高价值检索上下文；是否读取由 [_SRT_AGENT_RETRIEVAL_PROFILE.md](_SRT_AGENT_RETRIEVAL_PROFILE.md) 与 [_SRT_CONTEXT_ROUTER.md](_SRT_CONTEXT_ROUTER.md) 决定。

## 禁改与编辑协议

修改前先读：

- [Governance/SRT_CANONICAL_FREEZE.md](Governance/SRT_CANONICAL_FREEZE.md)
- [Governance/SRT_EDIT_PROTOCOL.md](Governance/SRT_EDIT_PROTOCOL.md)

最小规则：

- 不把 bridge 当 canonical
- 不把运行日志当理论主文
- 不随手改 canonical 定义
- 不因为兼容 Claude 就复制一套新规则

## 留痕规则

- 更新当前状态 → [STATUS.md](STATUS.md)
- 运行层留痕 → `Operations/`
- 治理层留痕 → `Governance/`

## 快速路由

- 中文主论证 → [Core_Law/SRT_Core_Text_CN_Euclid.md](Core_Law/SRT_Core_Text_CN_Euclid.md)
- Formal core → [Core/SRT_Core_21_Formal_Axioms.md](Core/SRT_Core_21_Formal_Axioms.md), [Core/SRT_Core_22_Equations.md](Core/SRT_Core_22_Equations.md)
- 人类阅读地图 → [SRT_Navigation_Map.md](SRT_Navigation_Map.md)
- 机器入口 → [_SRT_INDEX.md](_SRT_INDEX.md)
- AI 最小首读入口 → [SRT_AI_START.md](SRT_AI_START.md)
- Agent 检索扩展 → [_SRT_AGENT_RETRIEVAL_PROFILE.md](_SRT_AGENT_RETRIEVAL_PROFILE.md)
- 书籍写作口味校准 → [01_Source_Intuition/BOOK/TASTE.md](01_Source_Intuition/BOOK/TASTE.md)
