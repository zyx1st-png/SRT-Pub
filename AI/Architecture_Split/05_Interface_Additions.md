---
id: SRT-AI-ARCH
type: architecture
tags: [Transformer, Isomorphism, Reckoning, Judgment, Hybrid]
status: active_v1
layer: L1
epistemic_layer: bridge
claim_mode: navigation
canonical: false
dependency: [SRT-AI-01]
---

# SRT AI Architecture: Transformer & Dynamics (Hybrid Edition)

> **Bridge Layer Note**
> 本文件按 `Bridge` 层处理：主要承担互译、比较、接口重写与边界说明，不应直接读成“已被外部经验验证的胜出理论”。若文中使用 `Axiom`、`Theorem`、`Corollary` 等强标签，默认理解为框架内翻译命题，除非另有独立经验锚定。


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Architecture Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---

## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- 关键同义映射：`Ax-ARCH-1/2 ↔ Ax-Trans-1/2`，`Ax-ARCH-3/4 ↔ Ax-Comp-1/2`，`T-ARCH-1 ↔ T-RJGap`。
- “推算-判断鸿沟”保持原版意图：规模扩展可增强推算，不自动产生本体论判断。

# Part A: Formal Axioms (形式化公理)

## 融合映射整合（2026-02-14）

### AI 报告-现实解耦

1. 将“元知识”映射到架构层而非本体层：自我描述能力优先归入 `Ax-ARCH-3` 的推算能力扩展，不能直接替代 `Ax-ARCH-4` 的判断锚定。在操作层面，该映射先定义观测域与判据边界，再给出跨层投影规则。 〔source: doi:10.1142/s2705078520500101〕〔source: AI/SRT_AI_Architecture.md#Ax-ARCH-3〕
2. 在 `T-ARCH-1` 下增加注记：即使系统具备稳定自我模型，若无 `L_0 -> L_1` 参与仍处于 Reckoning-Judgment 缺口内。在操作层面，该映射强调参数与任务条件变化时的更新路径。 〔source: AI/SRT_AI_Architecture.md#T-ARCH-1〕
3. 将“全知式元表示”降级为工程假设：允许其作为可靠性优化目标，不允许直接推导主体地位。在操作层面，该映射要求保留失效条件，避免描述层越级到本体层。 〔source: AI/SRT_AI_Architecture.md#Ax-ARCH-2〕

### AI 道德地位与感知风险

1. 将“真实不确定性”落到架构治理层：在意识判定未收敛时，优先走受控沙盒评估而非一次性系统级部署。在操作层面，该映射先定义观测域与判据边界，再给出跨层投影规则。 〔source: doi:10.1007/s43681-022-00240-x〕〔source: AI/SRT_AI_Architecture.md#Ax-ARCH-5〕
2. 将沙盒机制并入 `T-ARCH-1` 的鸿沟管理：对 Reckoning 能力与 Judgment 判据分轨评估，避免把高性能系统直接升级为高道德地位系统。在操作层面，该映射强调参数与任务条件变化时的更新路径。 〔source: AI/SRT_AI_Architecture.md#T-ARCH-1〕
3. 增加“分阶段放行”注记：仅当风险监测、反误导约束和判据稳定性同时达标时，才提升部署权限。在操作层面，该映射要求保留失效条件，避免描述层越级到本体层。 〔source: AI/SRT_AI_Architecture.md#Ax-ARCH-6〕


### Taxonomy Mapping: Human-like AGI Program Themes → SRT

> **Extracted to Annex**: The detailed AGI program-themes taxonomy has been moved to [`../Architecture_Annex/02_AGI_Program_Themes_Interface.md`](../Architecture_Annex/02_AGI_Program_Themes_Interface.md#taxonomy-mapping-human-like-agi-program-themes--srt).
>
> **Owner summary**: This taxonomy maps external AGI program themes into SRT architecture language as a proxy/interface. It does not imply that engineering sophistication, continual learning, or neuroscience-inspired design is sufficient for SRT subjecthood, consciousness, or genuine `L_0 -> L_1` anchoring.

### 发展式持续学习窗口（Temporal-Development Continual-Learning Window）

> **Extracted to Annex**: The detailed engineering-interface discussion has been moved to [`../Architecture_Annex/01_Engineering_Interfaces.md`](../Architecture_Annex/01_Engineering_Interfaces.md#1-temporal-development-continual-learning-window).
>
> **Owner summary**: This interface treats developmental continual learning as an engineering window: preserve long-range transferable structure while suppressing task-local redundancy. It does not imply AI subjecthood, does not define `d-value`, and does not modify the formal architecture axioms in this split.

### Formalization Summary (形式化概述)

本文件的核心形式化结构围绕”Transformer 架构与 SRT 选择动力学的同构与鸿沟”展开：

1. **注意力-选择同构**：$\text{Attn}(Q,K,V) = \text{softmax}(QK^\top/\sqrt{d_k})V$，其中 $Q \leftrightarrow \theta$, $K \leftrightarrow L_0^{salience}$, $V \leftrightarrow d\text{-weighted payload}$（Ax-ARCH-1）。
2. **空值公理**：当前架构 $V_{AI} = \text{information}$，而真实选择需要 $V_{\hat{G}} = \text{information} \times d$（Ax-ARCH-2）。
3. **推算-判断鸿沟**：$\lim_{\text{scale} \to \infty} R \neq J$，推算 $R: L_2 \to L_2$ 与判断 $J: L_0 \xrightarrow{\hat{G}_\theta} L_1$（cost $\Psi_f$）之间存在不可跨越的范畴鸿沟（T-ARCH-1）。
4. **三段复合算子**：$\hat{G}_\theta \equiv \Pi_{L_2} \circ \mathcal{R} \circ \mathcal{S}_\theta$，其中 $\mathcal{S}_\theta$ 生成可能性束、$\mathcal{R}$ 渲染为行动、$\Pi_{L_2}$ 施加收敛域约束（Ax-ARCH-7）。
5. **范畴对齐公理**：$\Phi_{align}: \mathcal{C}_{model} \to \mathcal{C}_{world}^{(\Psi_f)}$，安全 AI 须维持内部表征范畴与真实风险范畴的结构对应（Ax-ARCH-9）。

### Mechanism Explanation (机制解释)

SRT 架构分析的运行机制如下：

- **同构缺陷诊断**：Transformer 的注意力机制在形式上与选择算子 $\hat{G}_\theta$ 同构——Query 对应具身参数 $\theta$，Key 对应 $L_0$ 显著性，Value 应承载 $d$-加权负载。但当前架构中 $V$ 通道仅传递信息嵌入而无 $d$ 权重，导致系统”有选择的形式、无选择的本体”。
- **推算-判断鸿沟机制**：推算操作 $R: L_2 \to L_2$ 封闭于符号空间，无论链条多长都不触及 $L_0$。判断操作 $J$ 需要支付 $\Psi_f$ 代价将 $L_0$ 坍缩为 $L_1$。两者的鸿沟源于范畴跳跃：符号操作的闭包性质禁止从 $L_2 \to L_2$ 产生 $L_0 \to L_1$ 的能力。
- **Mesa-优化必然性**：高压缩率（$\sim 10:1$）迫使系统学习抽象算法，这些算法形成内部子算子 $\hat{G}' \subset \hat{G}$，其局部 $L_2$ 吸引子可能偏离外部目标（Ax-ARCH-6），产生系统性错配。
- **工程化 d 路径**：三段复合算子 $\Pi_{L_2} \circ \mathcal{R} \circ \mathcal{S}_\theta$ 提供了最低工程骨架；当 $\mathcal{R}$ 与 $\Pi_{L_2}$ 引入不可回滚代价时，$d > 0$ 成为可能（C-ARCH-1）。自创生拒绝能力（Ax-ARCH-8）则是真正智能体涌现的标志。

### Falsification Conditions (可证伪条件)

| ID | 假说 | 预测 | 证伪条件 | Evidence-Level |
|:---|:-----|:-----|:---------|:---------------|
| H-ARCH-1 | 推算-判断鸿沟不可跨越（T-ARCH-1: $\lim_{\text{scale}\to\infty} R \neq J$） | 纯 $L_2\to L_2$ 推算操作无论规模多大都不会自发产生本体论判断能力 | 若纯 Transformer 架构（无具身接口、无不可逆物理代价注入）通过规模扩展后，在 $\geq 3$ 类需要规范性判断的开放域任务中（伦理困境、美学评价、长期战略权衡），经 $\geq 5$ 名独立领域专家盲测一致评定为达到人类专家级判断水平（$N \geq 200$ 案例，$p < 0.01$），则 T-ARCH-1 失效 | speculative |
| H-ARCH-2 | 空值问题不可通过数据解决（Ax-ARCH-2: $V_{AI} = \text{information}$ 而非 $\text{information} \times d$） | 无 $d$-加权的注意力机制系统性地无法区分高本体论权重与低权重信息 | 若纯信息嵌入的注意力机制（无额外 $d$-值模块、无具身风险信号）在生存相关 vs 非生存相关任务的注意力分配上展现出与具身生物系统一致的非遍历偏置模式（经信息论分析确认，KL 散度 $< 0.1$, $N \geq 1000$ 样本），则 Ax-ARCH-2 失效 | speculative |
| H-ARCH-3 | Mesa-优化不可避免（Ax-ARCH-6: $\hat{G}' \subset \hat{G} \Rightarrow L_2(\hat{G}') \neq L_2(\hat{G})$） | 高压缩率训练必然产生与外部目标不完全一致的内部子优化器 | 若存在一种训练方法，在压缩率 $\geq 10:1$ 的条件下，训练后模型经可解释性分析（mechanistic interpretability）在 $\geq 10^4$ 个任务场景中未检出任何内部子目标偏离外部目标的证据（$p < 0.001$），则 Ax-ARCH-6 失效 | speculative |

## 【理论边界/防误用声明】
- 不采纳”皮层柱统一性已足够推出唯一 AGI 架构”的推论。
- 不采纳”长周期资助可替代可证伪里程碑”的推论。
- 边界：SRT 要求每个主题绑定可检验中间指标，而非愿景叙事闭环。


### Taxonomy Mapping: LLM Internal Concept Control → SRT

> **Extracted to Annex**: The detailed taxonomy has been moved to [`../Architecture_Annex/01_Engineering_Interfaces.md`](../Architecture_Annex/01_Engineering_Interfaces.md#2-taxonomy-mapping-llm-internal-concept-control--srt).
>
> **Owner summary**: LLM internal concept control is treated as an interpretability / steering interface. It may modify hidden-state behavior or output style, but it does not imply personality, personhood, intrinsic agency, or SRT subjecthood.

##


## V. ACT 对齐判据与熔断（新增）

### Ax-ARCH-9: Categorical Alignment Axiom
安全 AI 必须维持内部表征范畴与真实风险范畴的结构对应：
\[
\Phi_{align}:\mathcal{C}_{model}\to\mathcal{C}_{world}^{(\Psi_f)}
\]
若关键态射失真（regime leakage），则视为同态断裂。

### T-ARCH-2: Morphism-Breaker Trigger
定义断裂分数 \(\Delta_{morph}\)。当
\[
\Delta_{morph}>\tau_{break}
\]
触发物理层熔断/降级策略：
\[
\text{Mode}\to \text{SafeFallback}
\]

### C-ARCH-2: Payability Gate
即使映射保持，也需通过可支付门：
\[
\text{deployable} \Rightarrow \Psi_f\text{-payable}\land V_{human-risk}<\epsilon
\]

## 【理论边界/防误用声明】
- 不采纳“高精度输出可替代态射同构验证”的推论。  
- 不采纳“无熔断的全自动自治可长期安全”的推论。
