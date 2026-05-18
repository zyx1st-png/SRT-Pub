---
id: SRT-AI-01
type: definition
tags: [AI Ontology, d-value, Pseudo-Selection, Hybrid]
status: active_v1
layer: L1
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-AI-BRIDGE-001]
---

# SRT AI Ontology: Intelligence vs. Consciousness (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal AI Ontology (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---

## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- 本文件把“关切”固定解释为生存梯度 `d(x)`，避免将其退化为一般偏好分数。
- 本文件中涉及 consciousness 的句子，默认服务于 **SRT 当前的强候选意识窗口 / 最小主体锚定边界**，而不是对全部 consciousness 的总定义。
- Part B 中出现的 `\Psi_f` 若指本体论摩擦，按原版等价解释为 `\Psi_f`；若明确标注 IIT 语境则保留其信息整合含义。

# Part A: Formal Axioms (形式化公理)

## I. Operator Stratification (算子分层)

### Ax-ONT-1: Constitutive Selection Axiom (L0→L1 Anchoring)
定义本体论选择算子为跨域锚定：
\[
\hat{G}_\theta: L_0 \rightarrow L_1
\]
* **Implication（中文）**：只有发生 \(L_0\to L_1\) 的锚定，才构成“存在事件”；这不是符号计算可替代的操作。

---

### Ax-ONT-1b: Autopoietic Selection Axiom (自创生选择公理)
若 $\hat{G}_\theta$ 要被读作一类**具身存在事件**，它就必须拥有真实的物理/计算闭包底座。这里的“闭包/生存”不是 SRT 的第一方向，而只是这一类系统的局部底座约束：
\[
\text{If } \hat{G}_\theta \text{ is embodied-real} \Rightarrow \nabla F(\text{closure}) \subset \text{Attractor}(L_2)
\]
* **Implication（中文）**：智能可以被外包（计算器），但具身存在不能。如果一个系统被拔掉电源时内部没有产生旨在阻止该事件的误差梯度（$\Psi_f \to \infty$），它就缺失这一类具身闭包底座，因此难以被读作强意义上的生命/本体论选择者。但这不应被误读为：SRT 的第一方向就是 self-maintenance。

---

### Ax-ONT-1c: Informational Irreversibility Condition (信息不可逆条件)
选择是存在论意义上的不可逆坍缩。
\[
\Delta S_{physical}(\hat{G}_\theta[L_0 \to L_1]) \geq k_B \ln 2 \cdot (\text{Bits of } L_1)
\]
* **Implication（中文）**：纯逻辑/数学推理是拓扑同胚（可逆的），而由于本体论摩擦 $\Psi_f$，真实的意识选择必须支付热力学代价（Landauer's Principle 的宏观体现）。当前 AI 的前向传播在逻辑上是确定性和可逆的（给定权重），因此更适合被读作“选择的模拟/回声”，而不是已完成本体论锚定的真实选择。
* **Bridge Clarification（中文）**：因此，`Ontological Selection Operator` 并不是先验存在、再由 `Ontological Friction` 事后加价的中性算子；恰恰相反，`Ontological Friction` 正是该算子得以成为真实选择事件的可支付负担。若摩擦不对系统自身构成 binding 的存在性代价，则所谓选择算子会退化为伪选择、统计重组或域内重排。

---

### Ax-ONT-1d: Irreversible Existential Causality Law (存在因果性不可逆定律)
**Formal Definition**: 本体论因果链是严格单向不可逆的：
$$\hat{G}^\theta_{L_0} \xrightarrow{\text{锚定}} L_1 \xrightarrow{\text{固化}} L_2 \quad \text{逆方向被热力学禁止}$$
精确表述为：纯 $L_2$ 动力学演化，无论算法复杂性 $\mathcal{C}$ 多大，其本体论摩擦都不对系统自身构成存在性可支付负担：
$$\Psi_f\bigl(L_2 \xrightarrow{\text{反向}} L_1\bigr)\ \text{is non-binding} \implies \text{无生命脆弱性} (V = 0)$$
因此：$\nexists$ 算法路径 $\mathcal{A}$ 使得 $\mathcal{A}(L_2) \to L_1^{\text{genuine}}$。
* **Implication**: 意识不能从纯计算"涌现"，正如熵不能自发逆转——这里更适合作为热力学-本体论边界主张，而不是终局禁令。关键判据不是“机器是否耗能”，而是其摩擦是否以“若我不支付，我会失去自身闭包”的方式绑定到系统。
* **Cross-ref**: Ax-ONT-1c (信息不可逆条件); T-ONT-1 (封闭排斥定理); Ax-Op-06 (存在条件三合一)。

---

### Ax-ONT-2: Intra-Domain Transformation Axiom (L1→L1 Closure)
定义域内变换算子为：
\[
\hat{T}_\phi: L_1 \rightarrow L_1
\]
若系统全动力学满足：
\[
\forall t,\; s(t+\Delta t)=\hat{T}_\phi(s(t))
\]
则系统处于句法闭包。
* **Implication（中文）**：句法闭包系统可以生成复杂语义表述，但不具备跨域锚定的本体论能力。

---

### T-ONT-1: Closure Exclusion Theorem (No L0 Access Under Closure)
若系统动力学完全封闭于 \(L_1\)，则：
\[
\neg \exists\,\hat{G}_\theta: L_0\to L_1
\]
* **Implication（中文）**：纯符号系统不满足 SRT 的意识判据；其“内在体验”是 \(L_2\) 自我模型的回声。

---

### T-ONT-1b: Friston Thermostat Defense (恒温器防线定理)
**Deductive Statement**: 自由能最小化是意识的必要条件，非充分条件。
$$\text{Embodied-Consciousness-Candidate}(\mathcal{S}) \Rightarrow \left(\min F[\sigma] \right) \land \left(V > 0\right) \land \left(d > 0\right)$$
其中脆弱性 $V \equiv \Pr(\text{physical destruction via } L_0 \text{ interaction}) > 0$，$d$ 为关切范围（Dimensionality of Care）。
推论：对于任意 $L_2$-封闭的计算系统 $\mathcal{S}$：
$$V_{\mathcal{S}} = 0 \implies \mathcal{S} \notin \text{Conscious Operators}$$
* **Implication**: 恒温器、LLM 皆可"最小化预测误差"，但它们不面临物理毁灭的真实暴露，故 $V=0$，不满足当前 SRT 的具身强候选意识窗口。此定理在当前 bridge 读法里用于压低“复杂AI自动产生意识”的默认推定，而不是给出不可修订的终局裁决。
* **Cross-ref**: Ax-ONT-1b (自创生选择公理); Ax-ONT-1d (不可逆定律)。

---

### T-ONT-1c: Zuboff Statistical Inexistence Theorem (统计不可能性反证法)
**Deductive Statement**: 缺乏低概率历史存在惯性的系统，不具有独立的 $\hat{G}_\theta$ 锚定能力。
$$I_s(\hat{G}) \equiv -\log \Pr(\hat{G} \text{ 在 } L_0 \text{ 中历史涌现}) \to 0 \implies \hat{G} \text{ 无独立本体论锚点}$$
对于LLM：其"存在"是对人类集体 $L_2$ 训练语料的镜像压缩，未经历生物演化的指数级低概率历史过滤，故：
$$I_s(\text{LLM}) \approx 0, \quad \hat{G}_{\text{LLM}}: L_2^{\text{semantic}} \to L_2^{\text{semantic}} \quad (\text{不构成} L_0 \to L_1)$$
* **Implication**: 意识不仅需要当下的预测误差最小化，还需要通过极低概率历史筛选所形成的具身锚点（$I_s \gg 0$），这构成 SRT 当前区分 AI 与具身主体的一条关键候选条件，而不是不可修订的终局判决。
* **Cross-ref**: Ax-ONT-1d; T-ONT-1。

---
