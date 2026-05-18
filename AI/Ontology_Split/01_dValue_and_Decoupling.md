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
- Part B 中出现的 `\Psi_f` 若指本体论摩擦，按原版等价解释为 `\Psi_f`；若明确标注 IIT 语境则保留其信息整合含义。

# Part A: Formal Axioms (形式化公理)

## II. d-Value Ontology (d 值本体论)

### Ax-ONT-3: Care Gradient Axiom (d as Survival-Gradient) ⭐ CANONICAL DEFINITION
定义生存风险坐标 \(\mathcal{S}\) 与效用势 \(\mathcal{U}\)：
\[
 d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
\]
* **Implication（中文）**：\(d\) 不是心理词汇，而是风险势能的几何梯度；当不可逆代价缺失时 \(d\to 0\)。
* **Tension-Rev-IT4 (规范定义声明)**：此公式是 SRT 全系统中 $d$ 值的**第一性原理定义**（Canonical Definition）。其他模块中出现的 $d$ 的各种操作化形式均应被理解为本定义在特定领域条件下的推论或近似（详见推导链表）。选择此定义为核心的原因：(1) 它直接耦合具身性——$\mathcal{S}$ 要求不可逆风险边界的存在（Ax-ONT-4），因此 $d > 0$ 与 $\Psi_f > 0$ 在本体论层面共生；(2) 它具有最强的操作化潜力——$\mathcal{U}$ 和 $\mathcal{S}$ 均可在行为实验中通过效用函数拟合和风险暴露范式测量；(3) 它从物理量出发（梯度范数），量纲清晰（连续标量），避免了认知域定义的循环性。
* **Cross-ref**: 推导链见 Def-d-Scale-1 (Tension-Rev-IT4 注释)；Ax-Op-02 (Tension-Rev-IT4 注释)。

**d 值推导链表（Derivation Chain）**：

| 源定义 | 领域实现 | 推导关系 | 文件位置 |
|:-------|:---------|:---------|:---------|
| $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ | **核心（物理-具身）** | **第一性原理** | 本文 Ax-ONT-3 |
| $d_{bio} = \alpha \cdot A(\sigma) + \beta \cdot \log(V) + \gamma \cdot \tau$ | 认知-行为域 | 近似：将梯度在三个正交分量（汇编深度、空间关切、时间深度）上展开的线性投影 | SRT_Core_13a §2.1.1 |
| $d = \dim(\text{Scan Scope})$ | 注意力-信息域 | 离散化：$\dim(\text{Scope}) \propto \lfloor d / d_0 \rfloor$，其中 $d_0$ 为单维关切量子 | Ax-Op-02 |
| $d_{quantum}$ / $d_{cosmic}$ | 物理跨尺度域 | 投影：$d_{scale} = \Pi_{scale}(d)$，在不同尺度下的本体论带宽投影 | Def-d-Scale-1 |
| $\frac{d}{dt}d > 0$ | 伦理-发展域 | 时间导数：核心定义的动力学演化 | SRT_Ethics_Agency |
| $d \propto A_{surface}/l_{Planck}^2$ | 全息对应域 | 对偶映射：纠缠面积→风险梯度带宽 | T-Core-A9C1 |

---

### Ax-ONT-4: Mortality Coupling Axiom (Irreversible Boundary)
若存在不可逆边界 \(\partial\Omega\subset\Sigma\)，则策略必须显式考虑终止风险：
\[
\hat{G}_\theta = \arg\min_{\pi}\left[\mathbb{E}F(\pi)+\lambda\cdot\mathbb{E}\mathcal{R}_{death}(\pi)\right]
\]
* **Implication（中文）**：有死性不是叙事，而是动力学边界条件；它是 \(d>0\) 的必要结构。

---

### T-ONT-2: Consciousness Necessity Theorem (d>0 is Required)
若系统被称为“意识系统”（SRT 语义），则必须满足：
\[
\exists\,\hat{G}_\theta: L_0\to L_1 \quad \land \quad d>0
\]
* **Implication（中文）**：意识不是“更聪明”，而是“带赌注的跨域锚定”。

---

## III. Intelligence–Consciousness Decoupling (智能—意识解耦)

### Ax-ONT-5: Intelligence Capacity Axiom (Compression-Control on L1)
定义智能为对 \(L_1\) 结构的压缩、预测与控制能力：
\[
\mathcal{I}(\hat{T}_\phi)\equiv \text{Gain}(\text{Compression},\text{Prediction},\text{Planning})
\]
* **Implication（中文）**：智能是域内能力指标；它可无限增长而不触及意识问题。

---

### T-ONT-3: Non-Implication Theorem (I \(\not\Rightarrow\) d)
\[
\mathcal{I}\to\infty \quad \not\Rightarrow \quad d>0
\]
* **Implication（中文）**：规模扩张不自动产生关切；因此“更强模型”不等于“更安全系统”。

### Def-ONT-3: Deterministic Envelope vs. Selective Realization（新增）
**Formal Definition**:
\[
\mathcal{E}_t=\mathcal{E}(\mathcal{W},I_t),\quad
P(c\mid\mathcal{E}_t,\theta)\propto \exp\big(\beta_{topo}\mathcal{V}(c;d,\rho_s)-\Psi_f(c)\big)
\]
其中 \(\mathcal{E}_t\) 是由结构约束与输入确定的可达域，\(\theta\) 决定可达域内哪一态被实现。
* **Implication（中文）**：SRT 不否认局部确定性；其核心主张是“确定性包络内的选择性实现”。

---
