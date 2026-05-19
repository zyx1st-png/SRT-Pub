---
id: SRT-PHIL-ANNEX-10-MENTAL-REPRESENTATION
type: interface
tags:
  - Philosophy
  - Interface
  - Annex
status: active_v1
layer: bridge
epistemic_layer: bridge
claim_mode: navigation
canonical: false
parent: Philosophy/SRT_Philosophy_Foundations.md
date: 2026-03-08
---

> **Annex file** — extracted from [`SRT_Philosophy_Foundations.md`](../SRT_Philosophy_Foundations.md). Extracted current bridge/interface content; `canonical: false` means this file does not define Core primitives.

## Mental Representation Interface（2026-03-08）

这组接口最需要收紧的，不是简单在“表征存在 / 不存在”之间站队，而是把争论拆回负担结构：哪些证据只说明系统对某特征敏感，哪些证据才真的够资格支撑“这里形成了可被消费的内容载体”。它也顺手修正了神经科学里一个常见偷步: `可解码` 不自动等于 `强表征已成立`。

### Def-Phil-MR-1: Representation as Internal Surrogate with Action Relevance
在 SRT 中，将“心理表征”定义为：由算子生成、可在系统内被操作、并能使行为对外部目标保持相关性的内部代理结构。
\[
R \in \mathcal{V}_{int},\quad
R \xrightarrow{\hat G_\theta\text{-compute}} a_t,
\quad a_t\ \text{tracks distal target }X
\]

### Def-Phil-MR-2: Vehicle–Content–Format Triad
采用三分约束：
- **vehicle**：承载结构（神经群活动、同步机制、外部耦合构件等）；
- **content**：该结构所指向的对象/性质/命题；
- **format**：可计算组织方式（离散/连续、命题式/图像式/连接式）。
\[
\text{Rep}(R)=\langle V, C, F\rangle
\]
SRT 要求对三者分别建模，避免把“有相关神经活动”直接等同于“内容已确定”。

### Def-Phil-MR-2b: Representation-Evidence Dimensions Correction
将“某神经响应表征了 \(X\)”从单一是/否判断，收紧为一组需要分开估计的证据维度：
\[
\text{Evidence}_{rep}(R,X)=\langle \mathrm{Sens},\mathrm{Spec},\mathrm{Inv},\mathrm{Func}\rangle
\]
- **sensitivity**：神经响应 \(R\) 是否随特征 \(X\) 改变；
- **specificity**：\(R\) 对 \(X\) 的关系是否不会被大量替代特征轻易重写；
- **invariance**：当无关特征变化时，\(R\) 对 \(X\) 的关系是否保持；
- **functionality**：\(R\) 是否被下游系统真正使用，而不只是可被研究者离线读取。

\[
\text{StrongRep}(R,X)\Rightarrow \mathrm{Sens}(R,X)\land \mathrm{Spec}(R,X)\land \mathrm{Inv}(R,X\mid N)\land \mathrm{Func}(R\to Cn)
\]
其中 \(N\) 表示 nuisance / 非目标特征，\(Cn\) 表示 downstream consumer。关键点是：**可解码**、**可编码拟合**、**RSA 相似**、**统计相关** 往往首先支持的是 sensitivity，至多提供局部 specificity 线索，并不自动等于“强表征已成立”。

### T-Phil-MR-1a: Decoding-Is-Not-Yet-Representation Corollary
\[
\mathrm{Decode}(X\mid R)>0\ \not\Rightarrow\ \text{StrongRep}(R,X)
\]
对 SRT 来说，这条澄清非常重要：研究者从 \(R\) 中读出 \(X\)，说明 \(R\) 与 \(X\) 存在信息关系；但若尚未区分 specificity、invariance 与 downstream use，就更接近“我们发现了一个可读出的相关维度”，而不是“系统内部已建立稳定内容载体”。

### T-Phil-MR-1b: Representation Strength as Evidence Ladder
SRT 将表征证据视为一个阶梯，而非一次性盖章：
\[
L_1^{covariation}\rightarrow L_1^{feature\text{-}selective}\rightarrow L_1^{invariant}\rightarrow L_2^{consumer\text{-}usable}
\]
这意味着许多神经科学中的“representation”结果，更稳妥的口径其实是：
- 先证明神经响应对某特征敏感；
- 再证明这种关系在竞争特征中具有选择性；
- 再证明它跨 nuisance 维度保持；
- 最后再证明它被下游行为或神经回路实际消费。
只有走到后段，才更接近 `Def-Phil-MR-3` 所说的 producer-consumer 功能闭环。

### T-Phil-MR-1: Misrepresentation Admissibility Theorem
可错性是表征的必要判据：若系统永不可错，则其“内容”退化为事后并集描述而失去解释力。
\[
\text{Representational status} \Rightarrow \exists\,e:\ C(R)\neq W_e
\]
对应 Martinez 文脉中的 disjunction/error 问题：SRT 通过引入目标函数与功能约束过滤“什么都算对”的伪内容归因。

### Def-Phil-MR-3: Teleo-Functional Fidelity Gate
将 fidelity conditions 自然化为“生产者-消费者链条中的功能闭环”：
\[
P \to R \to Cn,
\quad \text{Content fixed by successful downstream use under function constraints}
\]
其中 \(P\) 为 producer，\(Cn\) 为 consumer。该条款兼容 teleosemantics，也兼容信息论/信号博弈的 sender–receiver 语义。

### T-Phil-MR-2: 4E Compatibility Boundary
SRT 采纳“表示-非表示并存”边界：
\[
\text{Need}(R) \propto \text{task underdetermination} - \text{online sensorimotor closure}
\]
当任务可由实时具身耦合闭环完成时，可弱化内部表征承诺；当存在跨时规划、反事实推演或离线组合时，表征层通常不可省略。

换句话说，这条 interface 真正加固的，不是“表征主义必胜”，而是一个更稳的中间立场：有些任务里，表征负担确实可以降到很低；但一旦系统要跨时保持、离线重组、反事实推演，单靠在线耦合通常又不够。

### T-Phil-MR-2b: Protocol-vs-Representation Discriminant

SRT 不把表征主义打成稻草人。强版本表征主义可以合理预测：若系统成功依赖内部内容载体，则 specificity、invariance 与 downstream consumer use 应比单纯在线耦合更能解释行为稳定性。

SRT 的差异点更窄也更硬：在某些任务中，系统性失真可能是可支付锚定协议，而不是 truth-tracking failure。若某种感知压缩、注意偏置、身体坐标扭曲或语义粗粒化能稳定降低 `\Psi_f`、保留行动相关性并改善后果返回，那么它应先被判为 protocol candidate，而不是立刻被判为错误表征。

| Discriminant | Representationalist expectation | SRT protocol expectation |
|---|---|---|
| Fidelity under task change | Higher content fidelity should improve performance across relevant variants. | Some lower-fidelity transforms should outperform faithful maps when they reduce payability burden or improve coupling. |
| Error profile | Distortion is mainly a mismatch between internal content and world state. | Distortion may be structured by action affordance, metabolic budget, risk exposure, or position-bound update cost. |
| Failure mode | Failure occurs when content stops tracking target structure. | Failure occurs when a protocol no longer pays its anchoring cost or hides downstream consequence return. |

**Boundary**: If consumer-usable representation evidence predicts success better than coupling efficiency and payability measures across a task family, the SRT protocol-first reading must be narrowed. If only decodability or sensitivity is present, representational status remains underdetermined.

### 分类映射表（Mental Representation Regimes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 强表征计算（离线推演主导） | 中~高 | Semi-open（高内部操作） | 可支付~高负载 |
| 具身闭环优先（低内部建模） | 中 | Open（在线耦合） | 低~中负载 |
| 混合策略（4E + 表征） | 中~高 | Open↔Semi-open | 可支付（任务依赖） |
| 反表征工程极简（最小内部模型） | 低~中 | Open（直接耦合优先） | 低负载；离线组合任务易失真 |

> **[R]** 代表文献：Fodor 1975 *The Language of Thought*（强表征计算主义，离线符号操作，R基线）；Gibson 1979 *The Ecological Approach to Visual Perception*（直接知觉/具身闭环，无内部模型，R基线）；Clark & Chalmers 1998 *Analysis*（延展心智，4E+表征分布，R混合基线）；Brooks 1991 *IEEE Transactions on Robotics and Automation*（工程上的反表征/极简表征取向：强调直接耦合与最小内部模型，R极简基线）。**[H]** 以 d 值/能流/Ψ_f 三维映射统一四种表征模式为本框架新增比较框架。

### [Lineage/Source]
- Manolo Martínez (2026), *Mental Representation*.
- 关键脉络：Brentano intentionality、teleosemantics（Millikan）、sender-receiver/信息论框架、4E 挑战。
- Stephan Pohl et al. (2026), *Nature Reviews Neuroscience*: *Clarifying the conceptual dimensions of representation in neuroscience*（doi:`10.1038/s41583-026-01030-8`）。

## 【理论边界/防误用声明】
1. 不采纳"有神经相关 = 已确定内容"的推论；内容归因必须经功能与任务约束验证。  
2. 不采纳"4E 成立 = 一切内部表征可删除"的推论；不同任务对内部代理依赖度不同。  
3. 不采纳"teleosemantics 成立 = 语义已完全解决"的推论；误表征、远距内容与格式差异仍需经验判定。
