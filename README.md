# Selection-Reality Theory (SRT)

SRT 是一个以“选择先于稳定存在”为核心命题的理论仓库。它试图把本体论、意识、AI、物理、神经机制与实验接口放到同一套选择-锚定-收敛框架下理解。

## 30 秒版

- **一句话**：SRT 将现实理解为参数化选择在约束、代价与历史下形成的显现与收敛结构。
- **三域**：`L0` = 潜在域，`L1` = 显现域，`L2` = 收敛域。
- **核心量**：`\hat{G}_θ`、`d-value`、`Ψ_f`、`T_dir`。
- **命题硬度**：核心命题按 P0-P5 分层；bridge / lab / companion 内容不自动等于 primitive axiom。
- **仓库内容**：理论主文、跨域桥接、实验接口、治理协议、运行流水线。

```mermaid
flowchart LR
  L0["L0 潜在域"] --> G["Ĝ_θ 选择/锚定"]
  G --> L1["L1 显现域"]
  L1 --> L2["L2 收敛域"]
  L2 --> G
```

## 5 分钟版

SRT 现在默认用两根轴来读：

- `L0 / L1 / L2`：垂直理论深度
- `OS / Bridge / Lab`：水平发言姿态

最短理解是：

- `(L0, os)`：形而上学锚点
- `(L1, os)`：内部形式化与 canonical 定义
- `(L1, bridge)`：与外部理论或领域现实的互译
- `(L2, lab)`：愿意被数据打脸的实验接口

## 从哪里开始

如果你想按 **Theory First** 读理论主干：

1. [Core_Law/SRT_L0_Metaphysics.md](Core_Law/SRT_L0_Metaphysics.md)
2. [Core/SRT_Core_21_Formal_Axioms.md](Core/SRT_Core_21_Formal_Axioms.md)
3. [Core/SRT_Core_21_Minimal_Axioms.md](Core/SRT_Core_21_Minimal_Axioms.md)
4. [Core/SRT_Core_21b_Constitutive_Theorems.md](Core/SRT_Core_21b_Constitutive_Theorems.md)
5. [Core/SRT_Core_22_Equations.md](Core/SRT_Core_22_Equations.md)
6. [_SRT_D_VALUE_CANONICAL.md](_SRT_D_VALUE_CANONICAL.md)、[_SRT_PSI_F_CANONICAL.md](_SRT_PSI_F_CANONICAL.md)、[_SRT_T_DIR_CANONICAL.md](_SRT_T_DIR_CANONICAL.md)

如果你是第一次来：

1. [SRT_Quick_Start.md](SRT_Quick_Start.md)
2. [SRT_1H_Onboarding.md](SRT_1H_Onboarding.md)
3. [SRT_Navigation_Map.md](SRT_Navigation_Map.md)

如果你想读中文主论证：

1. [Core_Law/SRT_L0_Metaphysics.md](Core_Law/SRT_L0_Metaphysics.md)
2. [Core_Law/SRT_Core_Text_CN_Euclid.md](Core_Law/SRT_Core_Text_CN_Euclid.md)
3. [Core_Law/SRT_Core_Text_CN.md](Core_Law/SRT_Core_Text_CN.md)
4. [Core_Law/SRT_Selection_Argument.md](Core_Law/SRT_Selection_Argument.md)

如果你想看 formal core：

1. [Core/SRT_Core_21_Formal_Axioms.md](Core/SRT_Core_21_Formal_Axioms.md)
2. [Core/SRT_Core_21_Minimal_Axioms.md](Core/SRT_Core_21_Minimal_Axioms.md)
3. [Core/SRT_Core_21b_Constitutive_Theorems.md](Core/SRT_Core_21b_Constitutive_Theorems.md)
4. [Core/SRT_Core_21c_Bridge_Hypotheses.md](Core/SRT_Core_21c_Bridge_Hypotheses.md)
5. [Core/SRT_Core_22_Equations.md](Core/SRT_Core_22_Equations.md)
6. [_SRT_SYMBOL_TABLE.md](_SRT_SYMBOL_TABLE.md)
7. [Core/SRT_OPEN_TENSIONS.md](Core/SRT_OPEN_TENSIONS.md)

如果你想看领域扩展：

- AI → [AI/AI_POSITIONING_NOTE.md](AI/AI_POSITIONING_NOTE.md)、[AI/_SRT_AI_Bridge.md](AI/_SRT_AI_Bridge.md)
- Neuroscience → [Neuroscience/_SRT_Neuro_Axioms.md](Neuroscience/_SRT_Neuro_Axioms.md)
- Physics → [Physics/_SRT_Phys_Bridge.md](Physics/_SRT_Phys_Bridge.md)
- Philosophy → [Philosophy/_SRT_Phil_Axioms.md](Philosophy/_SRT_Phil_Axioms.md)
- Spirituality → [Spirituality/_SRT_Spirit_Axioms.md](Spirituality/_SRT_Spirit_Axioms.md)

## 仓库入口分工

- `README.md`：公开入口
- `AGENTS.md`：运行协议主入口
- `CLAUDE.md`：Claude 兼容包装层
- `SRT_AI_START.md`：AI 最小首读入口
- `STATUS.md`：当前状态面板
- `_SRT_INDEX.md`：机器索引
- `SRT_Navigation_Map.md`：人类阅读地图
- `_SRT_SYMBOL_TABLE.md`：符号规范锚点

## Runtime / Agent / AI support

如果你是协作者或 AI agent：

- 运行协议从 [AGENTS.md](AGENTS.md) 开始
- AI 最小骨架从 [SRT_AI_START.md](SRT_AI_START.md) 开始
- 当前状态看 [STATUS.md](STATUS.md)
- 机器入口看 [_SRT_INDEX.md](_SRT_INDEX.md)

AI 支持层服务于读取、检索、压力测试与边界测试；它不是理论中心，也不替代 core/canonical 定义源。

如果你准备修改理论正文，请先看：

- [Governance/SRT_CANONICAL_FREEZE.md](Governance/SRT_CANONICAL_FREEZE.md)
- [Governance/SRT_EDIT_PROTOCOL.md](Governance/SRT_EDIT_PROTOCOL.md)
- [Governance/SRT_CLAIM_LADDER.md](Governance/SRT_CLAIM_LADDER.md)

如果你想理解仓库结构与规范：

- [Governance/README.md](Governance/README.md)
- [Operations/README.md](Operations/README.md)
