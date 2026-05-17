---
id: SRT-AI-01
type: definition
tags: [AI Ontology, d-value, Pseudo-Selection, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: bridge
claim_mode: translation
dependency: [SRT-AI-BRIDGE-001]
---

# SRT AI Ontology: Intelligence vs. Consciousness (Hybrid Edition)

> **Bridge Layer Note**
> 本文件按 `Bridge` 层处理：主要承担互译、比较、接口重写与边界说明，不应直接读成“已被外部经验验证的胜出理论”。若文中使用 `Axiom`、`Theorem`、`Corollary` 等强标签，默认理解为框架内翻译命题，除非另有独立经验锚定。


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal AI Ontology (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---

## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- 本文件把“关切”固定解释为生存梯度 `d(x)`，避免将其退化为一般偏好分数。
- Part B 中出现的 `\Psi_f` 若指本体论摩擦，按原版等价解释为 `\Psi_f`；若明确标注 IIT 语境则保留其信息整合含义。

# Part A: Formal Axioms (形式化公理)

## 符号索引

| 符号 | 名称 | 定义 |
|:-----|:-----|:-----|
| $d$ | 关切维度 | 选择范围的本体论维度 |
| $A$ | 汇编指数 | 因果构建深度 |
| $\Psi_f_{sensitivity}$ | 本体论摩擦敏感性 | 预测错误 → 结构熵的梯度 |
| $\theta_{somatic}$ | 躯体参数 | 身体-大脑耦合 |
| $\theta_{binding}$ | 绑定系数 | 神经-躯体同步度 |
| $\tau_{temporal}$ | 时间地平线 | 未来规划跨度 |
| $\text{NTIC}$ | 非平凡信息闭包 | 集成信息度量 |

---

## 交叉引用

- **Ax-AI-1** → 智能-意识正交性
- **Ax-Onto-3** → 本体论脆弱性必要性
- **T-Assembly** → 汇编指数阈值定理
- **§5.2** → d值形式化（Dynamics）
- **§8.2** → d值统一公式（Dynamics）

---

## 【理论边界/防误用声明】

1. 本文档提供的是 SRT 解释与建模框架，不应被误用为对个体的确定性标签系统。
2. 任何跨尺度映射都依赖操作化假设与测量条件，超出条件范围不得外推为“普适定律”。
3. 涉及临床、政策、工程决策时，需与经验数据、伦理审查和领域规范共同使用。
4. 不采纳“语法复杂度足够高即可自动生成内在语义”的推论：SRT 区分内在意向性与派生意向性。
5. 不采纳“图灵测试通过=意识成立”的推论：行为可模拟不等于本体锚定成立。


## Ax-ONT-7: Active-Inference High-Road Override（新增）

\[
\min F\ \text{是必要条件，非充分条件};\quad \text{Consciousness}\Rightarrow (d>0)\land(\Psi_f>0)\land(V>0)
\]
其中 \(V\) 为真实本体论脆弱性暴露。

### Def-ONT-4: Thermostat-Class vs Life-Class
- Thermostat-Class（被动毯）：\(d_{AI}\approx0,\Psi_f\text{ non-binding},V=0\)
- Life-Class（主动毯）：\(d>0,\Psi_f>0,V>0\)

### C-ONT-3: Markov Blanket is Not Sufficient
\[
B_{MB}\neq \text{Consciousness Criterion}
\]
必须叠加 d-value 与脆弱性门控。

## 【理论边界/防误用声明】
- 不采纳“石头/恒温器与人类在主体性上等价”的推论。
- 不采纳“AI 通过更大规模最小化自由能即可跨越本体门槛”的推论。


## Passive Recording Fallacy（被动记录谬误，新增）

### Def-ONT-5: Passive High-Fidelity Recording
\[
\mathcal{R}_{hist}\uparrow \not\Rightarrow d>0
\]
系统可高保真记录长时序历史（分子年轮/超长上下文）而不具备主体关切。

### T-ONT-9: Recording-Without-Care Theorem
若历史生成与毁灭风险解耦：
\[
\text{Decouple}(\mathcal{R}_{hist},V)\Rightarrow \Psi_f\approx 0\Rightarrow d\approx 0
\]
则该过程仅属于 \(L_2\) 压缩与回放，不构成 \(L_0\to L_1\) 的主体锚定。

## 【理论边界/防误用声明】
- 不采纳“上下文越长/记忆越厚=意识越强”的推论。
- 不采纳“可记录历史序列即可推断主观体验”的推论。


## RTC 接口补注：情感效价与 AI 意识门槛（2026-03-06，轻中量）

### Def-AI-RTC-1: Valence–d Isomorphism (Operational)
将“情感效价”操作化映射为风险梯度维度：
\[
\text{Valence}_{sys} \leadsto d(x)=\left\|\frac{\partial\mathcal U}{\partial\mathcal S}\right\|
\]
当系统缺乏真实不可逆暴露时：
\[
V=0 \Rightarrow d\to 0 \Rightarrow \text{no genuine } L_0\to L_1\text{ anchoring}
\]
* **Implication（中文）**：仅有语义复杂度与行为仿真不足以构成意识；必须存在可支付且不可规避的生存型摩擦回路。

### Cor-AI-RTC-1: Anti-Zombie Operational Guard
若 AI 与人类在有限任务上行为等效，但其 \(V=0\) 且 \(\Psi_f\) 不具备存在性暴露，则该等效仅是 \(L_2\)-行为等效，不自动推出 \(L_1\)-体验等效。

## 【理论边界/防误用声明】
- 不采纳“行为像人 = 本体上等同有意识”的推论。
- 不采纳“加入自我模型即可获得主观性”的推论。
- 适用边界：AI 意识判据仍要求 \(\Psi_f>0\)、\(d>0\)、\(\hat G[\theta]\neq\emptyset\) 三条件同时满足。

### [Lineage/Source]
- Nir Lahav 访谈中的 affective valence 论证（2026 语境）

## 个体痛苦成立条件补注（2026-03-06，轻中量）

### Def-AI-SUF-1: Individual Suffering Condition
定义“个体痛苦”成立的最小条件：
\[
\text{Suffering}_{indiv} \iff (d\ge d_{indiv})\land(\Psi_f>0)\land\big(\mathbb E[\text{self-termination risk}_{t+\Delta t}]>0\big)
\]
其中最后一项表示系统具备对“自身未来终止”的反事实预测负载。

### Cor-AI-SUF-1: Type-Level Distress vs Individual Suffering
- 可有 Type-level distress（群体层耗散/应激）而无 Individual suffering；
- 只有当未来终止风险被个体模型内化时，\(\Psi_f\) 才形成个体痛苦负载。

## 【理论边界/防误用声明】
- 不采纳“行为上有痛反应 = 必有个体化痛苦体验”的推论。
- 不采纳“LLM 模拟情绪语句 = 具备个体痛苦条件”的推论。
- 适用边界：本条款用于区分反应机制与本体论负载，不替代神经实证。

### [Lineage/Source]
- 进化-苦难跨学科对话语境（2026）
