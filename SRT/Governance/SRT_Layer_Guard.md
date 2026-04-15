---
id: SRT-LAYER-GUARD
type: governance
tags: [Governance, LayerGuard, QualityControl]
status: canonical_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
---

# SRT Layer Guard：层级守卫文档

> **用途**：每次写新 SRT 内容前，用这份文档做一次快速自检。
> 目标：防止 L1 内容悄悄成为"基础"，防止 L0 被科学文献稀释。

---

## 一、三层定义（30秒版）

| 层级 | 一句话 | 典型内容 | 典型文件 |
|:---|:---|:---|:---|
| **L0** | 选择的形而上描述。无依赖，不被证伪 | 四命题、本体论语言、认知透镜 | `Core_Law/SRT_L0_Metaphysics.md` |
| **L1** | 选择如何在各领域显现。形式化 + 领域映射 | 公式、符号、与IIT/FEP/GWT的对比、领域Bridge | `Core_Law/` 其余文件、各领域文件 |
| **L2** | 接口处的可证伪预测。实验设计 | 实验方案、操作化定义、可证伪性声明 | `SRT_EXP_*.md`、Lab Hypotheses |

---

## 一点五、二维坐标补充

本文件主要守的是**垂直轴**：`L0 / L1 / L2`。
但从 `2026-03-18` 起，贡献者还需要同步看**水平轴**：`OS / Bridge / Lab`。

最短理解：

- `layer` = 你在 SRT 的哪一层理论深度发言
- `epistemic_layer` = 你在以什么姿态发言

常见组合：

| 坐标 | 含义 |
|:---|:---|
| `(L0, os)` | 形而上根基 |
| `(L1, os)` | SRT 内部形式接口 |
| `(L1, bridge)` | 与外部理论或领域现实的互译 |
| `(L2, lab)` | 真正下注的实验与反证设计 |

注意：`L0 / L1 / L2` 与 `OS / Bridge / Lab` 不是二选一，而是同一张坐标图的两根轴。详见 `Governance/SRT_COORDINATE_SYSTEM.md`。

---

## 二、写作前的五个问题

在动笔之前，逐项回答：

**Q1：这个内容的成立，是否依赖某个科学理论的正确性？**
- 是 → 它是 **L1 或 L2**，不是 L0
- 否 → 可能是 L0，继续往下问

**Q2：这个内容能被实验证伪吗？**
- 能 → 它是 **L2**，放入实验文件
- 不能，但映射了某个形式系统 → 它是 **L1**
- 不能，纯本体论语言 → 它是 **L0**

**Q3：这个内容是在"解释 L0 命题的含义"，还是在"为 L0 命题提供证据"？**
- 解释含义（展开 / 类比 / 推论）→ 可以是 L0 内部内容
- 提供证据（引用论文 / 援引实验）→ 它是 **L1**，不属于 L0

**Q4：这个内容加了引用吗？**
- 加了 → 它**不是 L0**，因为 L0 无依赖
- 没加，但引入了公式符号 → 它是 **L1**
- 没加，纯语言 → 可能是 L0

**Q5：如果这个内容被证明是错的，L0 的四命题会受影响吗？**
- 会 → 这个内容正在承担不该承担的重量，需要重新定位
- 不会 → 层级定位正确

---

## 三、常见漂移模式及纠错方法

### 漂移模式 1：把 L1 概念写进 L0 语境
**症状**：L0 文件里出现了公式、算子符号、希尔伯特空间、IIT 等词
**纠错**：把该段移出 `SRT_L0_Metaphysics.md`，放进对应的 L1 文件，加层级声明

### 漂移模式 2：用科学文献"支持"L0 命题
**症状**：某处写道"量子测量证明了选择先于存在"
**纠错**：量子测量是 L0 命题在物理学领域的 L1 映射，不是证明。改写为"量子测量是 L0 命题在物理学中的一种实例"

### 漂移模式 3：L1 文件自称"最高权威"
**症状**：某文件的 frontmatter 没有 `dependency: [SRT-L0-METAPHYSICS]`，或宣称自己拥有"最高解释权"
**纠错**：加 `layer: L1` 标签，加 `dependency`，加层级说明 blockquote

### 漂移模式 4：L2 预测上升为 L0 命题
**症状**：某个实验结果被直接用来修改三域结构的定义
**纠错**：实验结果只能修改 L2 文件（预测）和 L1 文件（映射参数），不触及 L0

### 漂移模式 5：在 L0 文件里加"边界说明"引用其他理论
**症状**：`SRT_L0_Metaphysics.md` 里出现了与 Whitehead / Barad / 过程哲学的比较段落
**纠错**：这些比较属于 L1 接口内容，移入 `Philosophy/SRT_Philosophy_Foundations.md` 或七论的 [R]/[H] 脚注

---

## 四、快速定位规则（新内容归属表）

| 新内容类型 | 归属层 | 放在哪个文件 |
|:---|:---|:---|
| 对"选择"本体论意义的纯语言论述 | L0 | `SRT_L0_Metaphysics.md`（唯一） |
| 公式 / 符号定义 | L1 | 对应的 `Reference_*.md` |
| 与 IIT / FEP / GWT 的对比 | L1 | `Philosophy/SRT_Philosophy_Foundations.md` 或七论 |
| 神经科学实验设计 | L2 | `SRT_EXP_*.md` 或 `Neuro/` |
| 新的跨领域映射（如新增"量子计算"映射）| L1 | 对应领域 Bridge 文件 |
| 引用了论文的任何内容 | L1 或 L2 | 根据是否可证伪决定 |
| 灵性 / 传统智慧对照 | L1 | `Spirituality/` 文件 |
| 可操作化的心理学量表 | L2 | `SRT_EXP_*.md` |

---

## 五、Core_Law 文件的当前层级地图

```
Core_Law/
├── SRT_L0_Metaphysics.md          ← L0  唯一锚点，dependency: []
├── SRT_Reference_Axioms.md        ← L1  公理形式化
├── SRT_Reference_Ontology.md      ← L1  三域形式化 + 跨领域映射
├── SRT_Reference_Dynamics.md      ← L1  算子 + 摩擦方程
├── SRT_Reference_Scaling.md       ← L1  跨尺度同构定理
├── SRT_Constitution_Seven_Theses.md ← L1  哲学论题 + 框架比较
└── SRT_Constitution_One_Page_CN.md  ← L1 + OS  入门接口
```

---

## 六、每次 SRT 研究周期的检查节点

| 时机 | 检查内容 |
|:---|:---|
| 写新文件前 | 完成 Q1-Q5，确认层级，选择正确目标文件 |
| 修改 `SRT_L0_Metaphysics.md` 前 | 必须能证明改动不依赖任何科学发现或形式系统 |
| 引入新领域映射前（如加入"社会学接口"）| 新建 L1 Bridge 文件，不修改 L0 |
| 新的实验可证伪预测 | 只进 L2 文件，附明 L1 映射来源 |
| 与其他理论（IIT/FEP/GWT）做比较 | 进 L1 比较文件，附 [R]/[H] 区分 |
