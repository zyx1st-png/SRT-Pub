# CLAUDE.md

本文件是 SRT 仓库给 Claude / Claude Code 的兼容包装层。

**运行规范以 [AGENTS.md](AGENTS.md) 为主。**
本文件不创建第二套独立 harness，只负责把 Claude 导向现有入口。

## 必读顺序

最小运行读法：

1. [AGENTS.md](AGENTS.md)
2. [SRT_AI_START.md](SRT_AI_START.md)
3. [STATUS.md](STATUS.md)
4. [_SRT_INDEX.md](_SRT_INDEX.md)
5. [_SRT_SYMBOL_TABLE.md](_SRT_SYMBOL_TABLE.md)

如需公开/对外 framing，再读：

6. [README.md](README.md)

如进入具体 pipeline、治理或运行留痕，再补读：

7. [Operations/README.md](Operations/README.md)
8. [Governance/README.md](Governance/README.md)
9. `memory/YYYY-MM-DD.md`（today + yesterday）
10. [HEARTBEAT.md](HEARTBEAT.md)（仅 heartbeat / automation 风格工作）

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
