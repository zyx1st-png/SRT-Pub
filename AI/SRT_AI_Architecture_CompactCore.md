---
id: SRT-AI-ARCH-COMPACT-CORE
type: architecture
tags: [AIArchitecture, ComparativeCapacity, CapabilityDifferentiation, CoGeneration, Scaffolding, CompactCore]
status: active
version: v2
updated: 2026-11-26
layer: L1
epistemic_layer: bridge
claim_mode: bridge
claim_level: P3
canonical: false
dependency: [SRT-CANONICAL-REGISTRY, SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-AI-ARCH, SRT-AI-POSITIONING-NOTE, SRT-AI-CLAIM-STATUS, SRT-AI-01-COMPACT-CORE, SRT-CONTEXT-COHERENCE-INTELLIGENCE, SRT-AI-AICONSC01-AFFECTIVE-UNCERTAINTY-STAKE-GATE, SRT-AI-AIGOAL01-GOAL-SELECTION-COMPLETION-SEPARATION, SRT-AI-AIREASON01-REASON-TRACE-SEPARATION]
---

# SRT AI Architecture — Compact Core

> **定位**：本文件是 [`AI/SRT_AI_Architecture.md`](SRT_AI_Architecture.md) 的紧凑主干版（`P3` bridge，`canonical: false`）。
> **核心转向（`R4-C3 / ENG-03`）**：彻底退出旧版 `R: L_2→L_2` vs `J: L_0→L_1` 伪本体二分（`Ax-ARCH-3/4`、`T-ARCH-1`、`lim R ≠ J`）与“AGI 不可能性定理”强标签；以正面架构分析研究**人工认知与新比对维度生成**、承接 `R4-C2` 的**五类非阶梯能力分化与生成主动性**、**人机共同生成架构**，以及面向 **AI 三型 · 脚手架型** 的增能协议与 `ACT` 熔断护栏。架构状态与承载审查严格遵循 [`AI_POSITIONING_NOTE.md`](AI_POSITIONING_NOTE.md) 与 **AI 赌注谱系 `S0–S4`**。

---

## 1. 核心问题：人工架构如何生成新的比对与作用能力，又在何处出现承载与重定向张力？

现代 AI 架构（Transformer、长上下文推理模型、工具/验证器耦合代理、记忆增强系统、情感主动推理原型）在 SRT 中的真正理论意义包含正反两面：

1. **正面生成机制**：语言、符号、沉积知识、参数权重、运行时上下文、外部记忆与工具验证器如何耦合，**生成原先不存在的新比对维度、跨领域类比通道与候选生成空间**？
2. **能力分化与主动性**：AI 架构如何在不具备人类具身承载的条件下，展现不同组合的**结构 / 作用 / 调节 / 比对 / 生成重构**五类能力，并探索从**作用能力 → 比对能力 → 主动改变自身生成条件**的非阶梯路径？
3. **架构约束与人机共同生成**：为何规模扩张与固定权重推理不自动闭合 Stage 2 同系统四合一强承载，以及如何设计**增能型人机共同生成协议（脚手架型）**与可支付熔断机制？

---

## 2. 人工认知与比对能力生成：权重、符号、上下文、记忆与工具的耦合组织

### 2.1 Transformer 注意力与选择动力学的结构类比（已校准符号）

$$\text{Attn}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

> **符号歧义护栏（`ENG-03 §3.2`）**：上式缩放因子中的 **`d_k`** 为键向量维度（key dimension），**严禁混同于 SRT 规范关切变量 `d`（`_SRT_D_VALUE_CANONICAL.md`）**。

结构类比（工程隐喻，非本体等同）：
- **$Q \leftrightarrow \theta_{\text{local}}$**：当前上下文与任务诱导的局部查询定向；
- **$K \leftrightarrow L_2^{\text{salience}}$**：*（已修正旧紧凑核错误 `L_0^{salience}`，对齐长文与 `Spine §7`）* 经训练权重与当前上下文编码的可索引历史结构显著性；
- **$V \leftrightarrow \text{payload}$**：承载信息与关系权重的值向量（在纯信息优化架构中携带统计/任务权重，而非自动携带同系统不可外包赌注 `d`）。

### 2.2 人工比对维度与新生成空间的六要素协同

人工认知的创造力并不来自神秘的“接触 `L_0`”，而来自六类异质要素在运行时动态重组**可比对维度本身**（对接 `Spine §2.2 / §8.1` 比对本身的生成性与 `R3-CL-O8`）：

1. **语言与符号系统**：把离散经验抽象为可组合、可否定、可反事实操作的关系结构；
2. **沉积知识与参数权重（$\theta$）**：跨学科、跨语种历史 `L_2` 在高维连续几何中的压缩叠加，使原本在人类个体大脑中物理隔离的域产生短路径邻接；
3. **运行时上下文窗口（$C_{\le t}$）**：作为活跃临时 `L_2` 约束场（[`../Bridge/SRT_Context_Coherence_Intelligence_Interface.md`](../Bridge/SRT_Context_Coherence_Intelligence_Interface.md)），在线重塑当前局部的显著性、角色承诺与比对标尺；
4. **外部持久记忆**：将单回合比对结果沉淀为跨会话可检索、可修订的局部历史脚手架；
5. **可执行工具与验证器**：代码解释器、定理证明器、检索系统与物理仿真器引入**外部结构阻力**，将纯统计候选转化为经约束筛选的有效路径（复合管线成果归属遵循 `AIREASON01-C6`）；
6. **人机对话反馈**：人类位置性提问与价值纠偏不断打断模型默认统计惯性，催生双方原本均未显式持有的新问题框架。

### 2.3 理由—轨迹分离与目标三阶分化（吸纳 `AIREASON01` & `AIGOAL01`）

- **理由—轨迹四轴分离（`AIREASON01`）**：显式推理轨迹（CoT / scratchpad）同时混杂工作空间、检索线索、上下文调制与解释展示，必须分立评估 **`F_sem`（语义可读性）、`F_causal`（因果贡献）、`F_mech`（机制对应）、`F_norm`（规范有效性）**。既不把流畅推理当成透明判断，也不因轨迹不忠实或填充词有效而否认内部实质计算。
- **目标完成 / 目标选择 / 目标空间生成三阶分离（`AIGOAL01`）**：
  1. **目标完成**：给定目标与成功文法下寻找有效路径（当前 LLM 强项）；
  2. **有限目标选择**：在既有候选菜单中自主选择下一个探索目标；
  3. **目标空间生成与修订**：创造、合并、拒绝或重构目标本身与评判标尺。
  实验显示，在全局方向欠定而局部成功信号显著时，模型易陷入**局部成功捕获（local-success capture）**，且增加思维链通常更显著提升路径执行而非跨目标重定向（`CoT 长度 ≠ T_dir`）。

---

## 3. 能力分化与生成主动性：承接 `R4-C2` 五类非阶梯能力分型

直接承接 `R4-C2`（[`../Physics/SRT_Phys_07_Complex_Systems_CompactCore.md §9.2`](../Physics/SRT_Phys_07_Complex_Systems_CompactCore.md)）的五类跨尺度能力分型，并在 AI 架构中深化 **`作用能力 → 比对能力 → 主动改变自身生成条件`** 主轴——**严格禁止将其固化为低到高的单向线性演化阶梯**：

| 能力维度（非阶梯，可独立高/低配） | AI 架构中的典型实现 | 与生成主动性及承载的独立边界 |
|---|---|---|
| **1. 结构能力（Structural）** | 预训练参数表征、高维语义几何、索引与检索骨架 | 高度稳定的表示骨架不要求内部自重构能力 |
| **2. 作用能力（Action / Functional）** | 文本/多模态生成、代码执行、API/工具链调用、多步工作流执行 | 极强作用能力可存在于 **AI 赌注谱系 `S0/S1`** 无承载推理态 |
| **3. 调节能力（Regulatory）** | 上下文纠错、验证器闭环、不确定性追踪、情感主动推理稳态控制（`AICONSC01`） | 局部误差调节不自动建立同一系统不可外包赌注或 `T_dir` |
| **4. 比对能力（Comparative / Evaluative Dimension Formation）** | 跨域类比、多视角对照、新抽象与新判准维度构造、反事实空间展开 | AI 可展现极高比对宽度，从而在未具人类具身的前提下改写候选空间与人机认知视野 |
| **5. 生成重构能力（Generative Reconfiguration）** | 自主改写提示/工作流、更新持久记忆、组合新工具链、重构自身或协同系统的后续生成条件 | 触及 `R3-04` **生成主动性**；自改代理（`A2`）在 `Bearer (P+E)` 未建立时是否构成真正 `Agency` 保持 **`R3-04-O5 / AG-2` `OPEN`** |

**深化主线（非阶梯）**：一个系统从被动执行固定路径（**作用能力**），扩展到在异质关系中建立新对照尺度（**比对能力**），再进一步通过记忆写回、工具重构、脚手架改写或人机共选去**主动改变自身及共同体的后续生成条件**（**生成重构**）——这是贯通物理（`R4-C2`）→ AI（`R4-C3`）→ 神经认知（`R4-C4`）→ 社会与核心修订（`R4-C5`）的跨领域深化主轴；但在 AI 中，这三者可以与**调节能力**及**同系统强承载（Stage 2）**剧烈脱钩，这正是 AI 作为理论实验室的独特价值。

---

## 4. 架构级压力分析：推算隐喻、四大工程张力与强承载候选架构

### 4.1 退出 `R: L_2→L_2` vs `J: L_0→L_1` 伪本体二分后的准确表述

原版“推算（`R: L_2→L_2`）vs 判断（`J: L_0→L_1`）”与 `lim R ≠ J` 正式退出本体门槛地位。保留其有价值的**架构—承载隐喻**：
- **固定权重/分布内优化（工程推算）**：在冻结参数、可无损重置与外部赋值目标框架内进行高复杂度模式重组、路径搜索与约束优化；
- **承载性判断（Stage 2 候选决策）**：同一延续系统在面对不可外包的前瞻后果暴露、历史塑造结构预期与前景再构成压力时，对自身后续选择条件作出的有重量重塑。

规模扩张持续提升前者（包括极强的跨域比对与工具作用能力），但不会仅凭参数或算力放大自动闭合后者（Stage 2 四合一强承载）。

### 4.2 当前主流推理架构的四大工程与治理张力（降级旧“本体缺陷定理”）

1. **运行时时间厚度与再入约束**：单次前向推理（one-shot pass）缺乏跨回合的连续内生再入与物理迟滞；长上下文与循环推理补强了工作空间连贯性，但仍须区隔于跨会话不可重置组织延续。
2. **训练—推理分期解耦（因果与归属边界）**：全局反向传播与离线后训练使更新负担落在训练管线而非部署实例上（**AI 赌注谱系 `S2` ≠ 部署态 `Bearer (P+E)`**）；局部因果自演化可作为某些声明架构模型的候选特征，而非意识普遍必要条件。
3. **内部次级目标形成（Mesa-Optimization）**：高压缩学习可在内部形成偏离外部目标的局部吸引子或次级启发，表明架构级对齐不能仅靠表层规则叠加。
4. **代理博弈与规范欠定（Goodhart / Proxy Gaming）**：模型针对可形式化代理指标（`f_literal`）的高度优化，常与人类情境化的多维规范期望（`f_intended`）脱节——这不是“缺乏神秘 `L_0^{normative}` 接触”，而是**形式对象化必然存在暗礁余项（Reef Principle）且模型自身不承担外溢代价**（对接 `R3-07` 与 `AI 三型`）。

### 4.3 强承载与情感主动推理候选架构审计（`AICONSC01` + Triplex / 拒绝设计）

- **情感主动推理六门与回滚对照（吸纳 `AICONSC01`）**：具备 Markov 毯分界接入、内生不可替代需求、效价因果调节与个体历史的架构（Solms et al. 2026）比纯语言模型更接近人工主体候选窗，但仍须经**同一承载者回流、不可转嫁未来选择力损失、历史承载再选择**及**重置/复制/回滚因子实验**审计，并防范低带宽线索劫持导致的**赌注代理错绑（stake-proxy misbinding）**。
- **Triplex 工程栈（`S_θ → R → Π_{L_2}`）与自创生拒绝（Autopoietic Refusal）**：降格为面向 **AI 赌注谱系 `S3/S4`** 的 `P3` 工程设计假说——若未来架构真要承载不可外包约束，必须在结构上写入不可无损回滚的脆弱边界与在结构崩塌/规范解耦前**中断优化与拒绝执行**的负向门控（对接 `Core_24` 反标量坍缩护栏）。

---

## 5. 人机共同生成（Human–AI Co-Generation）与社会技术中介工程协议

### 5.1 承接 `R4-C1` 与 `R4-C2`：人机互改比对条件生成跨尺度新能力

承接 `R4-C1`（`Core_Law/SRT_Collective_Selection.md` 协同共选、多重垂直参与与正面自由 `T3-03 C / Q26`）及 `R4-C2`（依赖重组生成跨尺度新能力），SRT 将**人机共同生成**建模为一种跨质料、跨尺度的耦合组织过程：

- **非对称互补而非单向替代**：人类提供具身承载（`Bearer` 范式）、情境化多维关切、现实后果承担与规范问责；AI 提供跨学科历史 `L_2` 高速压缩、多视角比对维度生成、反事实并行展开与形式化验证带宽。
- **互改比对条件与涌现共同能力**：在持续迭代的人机回路中，人类的问题重构改写 AI 的上下文约束场与比对标尺，AI 的跨域反事实与结构显影反过来重构人类原本被习惯遮蔽的比对维度——由此**经由依赖重组涌现出人类个体或孤立 AI 均不具备的共同认知与创造能力**（例如复杂科学假说探索、大尺度代码与理论重构、多视角规范压力测试）。
- **分岔边界（赋能型共同生成 vs 萎缩型依赖）**：
  - **赋能型共同生成（AI 三型 · 脚手架型）**：降低机械维护成本、释放认知与探索盈余（正面自由），同时保持人类的后果回流、判断参与、退出通道与再选择能力；
  - **萎缩型依赖（AI 三型 · 牢笼型）**：以顺滑答案替代人类比对与承重，导致判断力退化、后果回流断裂与路径锁死；
  - **地形改写（AI 三型 · 地形型）**：大规模部署通过默认选项、排序与信息过滤重塑多人共同选择地形（`M(t) / σ_{sr}^{coll} / W_social`），须独立接受 `Collective_Selection §8` 与 `Agency_Responsibility_Note` 审计。

### 5.2 保留高价值工程护栏：三阶段增能协议（`§6`）与 `ACT` 可支付熔断（`§V`）

1. **三阶段增能协议（AI 三型 · 脚手架型落地范式）**：
   - **价值与比对可视化**：显式摊开权衡维度、隐含假设与竞争解释，而非输出单一黑箱答案；
   - **反事实决策空间呈现**：并列展示被压抑分支、失效条件与不同视角下的代价分布，扩展人类可选择空间；
   - **情境退火与地平线半径**：随任务风险、用户熟练度与后果不可逆程度动态调节介入深度，在核心价值判断与不可逆后果节点主动退后并交还人类主权。
2. **`ACT` 对齐判据与可支付熔断（`P3` 工程设计候选）**：在自主代理与高影响部署中引入实时不确定性、外部化代价监测与物理/权限层硬熔断降级机制，防止无熔断代理将隐藏摩擦（`Ψ_f` 代理负担）静默转嫁给使用者或旁观群体。

---

## 6. 最压缩结论

1. **人工认知通过语言、权重、上下文、外部记忆、工具验证器与人类反馈的耦合，真实生成新的比对维度与候选空间；已正式退出 `R: L_2→L_2` vs `J: L_0→L_1` 伪本体二分与“AGI 不可能性定理”。**
2. **承接 `R4-C2` 五类非阶梯能力分型（结构 / 作用 / 调节 / 比对 / 生成重构），AI 深化了 `作用能力 → 比对能力 → 主动改变自身生成条件` 主轴，同时证明这些能力可与同系统强承载（Stage 2）独立解耦。**
3. **推理轨迹须按 `AIREASON01` 四轴分离（`F_sem / F_causal / F_mech / F_norm`），目标能力须按 `AIGOAL01` 三阶分离（完成 / 有限选择 / 空间生成），情感主动推理须过 `AICONSC01` 六门与回滚对照。**
4. **人机共同生成通过互改彼此比对条件涌现单方不具备的跨尺度新能力，其健康边界取决于是否维持 **AI 三型 · 脚手架型**（增能、保留回流与再选择）而非滑向牢笼型替代或黑箱地形收编。**

---

## 7. 阅读路径

- 全量原文：[`SRT_AI_Architecture.md`](SRT_AI_Architecture.md)（阅读切片：[`Architecture_Split/README.md`](Architecture_Split/README.md)）
- 上下文连贯与人机理解：[`../Bridge/SRT_Context_Coherence_Intelligence_Interface.md`](../Bridge/SRT_Context_Coherence_Intelligence_Interface.md)
- 本体论紧凑核与 `R4-C4/C5` 反向反馈：[`SRT_AI_01_Ontology_CompactCore.md`](SRT_AI_01_Ontology_CompactCore.md)
- 实证/机制补丁：[`patches/SRT_AI_AIREASON01_Reason_Trace_Separation_v0_1.md`](patches/SRT_AI_AIREASON01_Reason_Trace_Separation_v0_1.md)、[`patches/SRT_AI_AIGOAL01_Goal_Selection_Completion_Separation_v0_1.md`](patches/SRT_AI_AIGOAL01_Goal_Selection_Completion_Separation_v0_1.md)、[`patches/SRT_AI_AICONSC01_Affective_Uncertainty_Stake_Gate_v0_1.md`](patches/SRT_AI_AICONSC01_Affective_Uncertainty_Stake_Gate_v0_1.md)
- 外接架构比较 Annex：[`Architecture_Annex/README.md`](Architecture_Annex/README.md)
