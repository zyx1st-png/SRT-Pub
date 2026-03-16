---
id: SRT-CORE-22
type: equation
tags: [Math, Stability, Landscape, Dynamics, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-21]
---

# SRT Core Definition 22: Master Equations (Hybrid Edition)

> **Canonical Role（规范角色）**：本文件是 SRT 当前 `master dynamics / thermodynamics / stability equations` 的主锚点文件。若其他长文出现同类方程的扩展写法，默认以本文件为优先回链对象。

> **Version 2.0 (Hybrid)**
> **Part A** presents the Primary Dynamical Equations (AI-Readable).
> **Part B** contains the Original Derivations and Stability Analysis (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


## 0-B. Protocol and Foundation (协议与基础)

### Def-Protocol-1: Protocol Layer Π (协议层 Π)
**Formal Definition**: 约束 $\hat{G}_\theta$ 选择空间的容许转移核集合：
$$\hat{G}_\theta : (L_0, \Pi) \to L_1$$
其中 $\Pi$ 是从 $L_0$ 到 $L_1$ 的可行转移集 / 约束核。
* **Implication**: 物理模型中的“简单局部规则”属于 $\Pi$，其本身是一个收敛的 $L_2$-约束（由高阶相互作用/选择固化而来），而不是“无条件的背景”。这是 SRT 抵御自下而上物理主义还原的最强界面：**涌现仅发生在被选择的 $\Pi$ 内部。**
* **Cross-ref**: Ax-Core-A5 (规范闭包)；T-Core-02 ($L_2$ 作为不动点)。

### Def-Protocol-2: Absolute-vs-Relative Constraint Split（新增）
\[
\Pi = \Pi_{abs} \cup \Pi_{\theta},\quad \Pi_{abs}\cap\Pi_{\theta}=\varnothing
\]
- \(\Pi_{abs}\)：跨参数不可违背的下限约束（如复杂度/热力学下界）；
- \(\Pi_{\theta}\)：由具身参数与历史收敛形成的相对约束（对应 \(L_{2,\theta}\) 语法）。

* **Implication**：允许“外星物理语法不同”而不坠入相对主义：差异主要位于 \(\Pi_{\theta}\)，底线仍受 \(\Pi_{abs}\) 约束。

### Def-Protocol-3: Methodological Closure Guard（方法论闭包护栏，新增）
\[
\mathcal{M}_{empirical}: (L_1,L_{2,\theta})\to \text{validated regularities}
\]
其中 \(\mathcal{M}_{empirical}\) 是实验方法对可观测层的闭包映射。
* **Implication**：\(\mathcal{M}_{empirical}\) 的成功仅证明 \(L_1\!-
L_{2,\theta}\) 回路内规律可复现，不构成对 \(L_0\) 潜势或 \(\Omega\) 逻辑层的本体论否定。

## 0-C. Multi-Operator Coupled Equations（多算子耦合方程）

> **背景**：SRT 的单算子方程（§0-B, §I）描述单个 $\hat{G}_\theta$ 的动力学。本节将框架扩展到多算子系统，给出集体自由能、个体算子梯度关系与集体 d-value 的形式化。这是集体景观优先性定理（见 `_SRT_VERTICAL_INTEGRATION.md §4.5`）的方程层锚点。

### Eq-Multi-01: Collective Free Energy Landscape（集体自由能景观）
**Formal Definition**: 多算子系统的集体自由能景观是各算子个体摩擦与算子间摩擦的总和：
$$\boxed{\mathcal{F}_{collective}(\{\sigma_i, \theta_i\}) = \sum_i \Psi_f(\hat{G}_i) + \sum_{i < j} \Psi_f(\hat{G}_i, \hat{G}_j)}$$
其中 $\Psi_f(\hat{G}_i)$ 是第 $i$ 个算子的个体本体论摩擦（锚定代价），$\Psi_f(\hat{G}_i, \hat{G}_j)$ 是算子 $i$ 与算子 $j$ 的交互摩擦（见 Ax-F-12）。
* **Implication**: 集体景观不是个体自由能的简单加和，算子间交互摩擦项 $\Psi_f(\hat{G}_i, \hat{G}_j)$ 是集体动力学的主要来源。

### Eq-Multi-02: Individual Operator as Landscape Gradient（个体算子为集体景观的梯度表达）
**Formal Definition**: 每个个体选择算子的运动方向是集体自由能景观关于自身参数的负梯度：
$$\boxed{\hat{G}_i[\sigma_i] = -\frac{\partial \mathcal{F}_{collective}}{\partial \theta_i}}$$
* **Implication**: 个体算子不是"为自身最小化自由能"的独立实体，而是集体景观在局部参数子空间 $\theta_i$ 的梯度下降方向。"个体与集体的目标张力"是景观局部曲率与全局曲率差的表达，而非两个对立实体的博弈。

### Eq-Multi-03: d_collective as Landscape Effective Dimension（集体 d 值为景观有效维度）
**Formal Definition**: 集体 d-value 是集体自由能景观 $\mathcal{F}_{collective}$ 的 Hessian 矩阵的有效维度（参与率指数）：
$$\boxed{d_{collective} = D_{eff}(\mathcal{F}_{collective}) = \frac{\left(\sum_k \lambda_k\right)^2}{\sum_k \lambda_k^2}}$$
其中 $\lambda_k$ 是 $\nabla^2 \mathcal{F}_{collective}$（Hessian）的特征值。个体 $d_i$ 是该景观在子空间 $\theta_i$ 上的截面有效维度：
$$d_i = D_{eff}\!\left(\mathcal{F}_{collective}\big|_{\theta_i}\right)$$
* **Implication**: $d_{collective}$ 不由 $d_i$ 聚合得出，而是景观固有的结构属性。个体 $d_i$ 是 $d_{collective}$ 的投影截面，包含关系而非组合关系。
* **Cross-ref**: `_SRT_VERTICAL_INTEGRATION.md §4.5`；`_SRT_D_VALUE_CANONICAL.md §6`；`Core/SRT_Core_21_Formal_Axioms.md Ax-F-12`。

---

## I. Evolution Dynamics (演化动力学)

### Eq-Evo-01: Ghost Evolution Equation
**Formal Definition**: The trajectory of a selected state is the sum of selection, free-energy descent, and attention modulation.
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
* **Implication**: 现实演化是选择、能量下降与注意调制的合成动力学。

### Eq-Evo-01b: Metabolic Gain Modulation
**Formal Definition**: 代谢压力作为演化方程的增益调节项。
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] \cdot \underbrace{(1 + \beta \mathcal{M}_{stress})}_{\text{Metabolic Gain}} + A[\sigma, \mathcal{A}]$$
其中 $\mathcal{M}_{stress}$ 为代谢应激指标（如低血糖、缺氧等）。
* **Implication**: 当 $\mathcal{M}_{stress}$ 上升时，自由能梯度 $\nabla F$ 的权重被放大，系统被迫从高阶抽象思考坍缩为低阶生存应对。此公式解释了"饥饿时无法思考哲学"的现象——代谢需求劫持了选择带宽。
* **Cross-ref**: Eq-Evo-01, Def D4a ($θ_{intero}$)。

### Eq-Evo-02: Parameter Update (Slow Variable)

**[R（三项结构）/ H（戒断机制推论）：学习/摩擦/稳态三项追溯RL+预测编码+稳态生理学；戒断机制是Novel Prediction]**

**Formal Definition**: Embodiment parameters evolve under prediction outcomes, friction gradients, and homeostatic recoil.
$$\frac{d\theta}{dt} = \underbrace{\gamma \cdot A[\sigma, \text{Target}]}_{\text{Learning}} - \underbrace{\delta \frac{\partial \Phi(\theta)}{\partial \theta}}_{\text{Friction Descent}} - \underbrace{k \cdot (\text{Input}_{L_1} - \text{Baseline})}_{\text{Homeostatic Recoil}}$$

**三项参数化注**：
- **$A[\sigma, \text{Target}]$ 操作化候选**：预测准确性代理 = $-\Psi_f(\sigma, \text{Target})$（摩擦代价越低=越准确→学习信号越强）；或写为 $A = \text{cos\_sim}(\hat{G}_\theta[\sigma], \text{Target})$（当前选择与目标的相似度）。$\gamma$ 是学习率。
- **$\Phi(\theta)$ 候选形式**：零阶近似为二次势能：$\Phi(\theta) = \frac{1}{2}|\theta - \theta_{ref}|^2$，使第二项退化为向参考点 $\theta_{ref}$（习惯态）的拉力（$\delta(\theta - \theta_{ref})$）。一般形式可从 Ax-L2-01（迟滞势垒）推导。
- **第三项（稳态反冲）**：负反馈将 $\theta$ 锚定在稳态基线处；$k$ 是稳态刚度，$\text{Input}_{L_1} - \text{Baseline}$ 是当前L₁输入与稳态基线的偏差。

* **Implication**: 具身参数在三力之间调整——学习推动适应，摩擦梯度约束漂移，稳态反作用力维持平衡。

* **推论（戒断机制 / Withdrawal Mechanism）** [H]：当外部 $\text{Input}_{L_1}$ 突然归零时，第三项的负反馈瞬间失效，但 $\theta$ 具有迟滞性（Hysteresis）。残留的 $\theta^{-}$ 偏置直接作用于 $L_0$，导致 $\hat{G}_\theta$ 生成"反向体验"（痛苦/焦虑）。
  - **因果路径精确化**：$\theta^-$（残留参数偏置）→ $\hat{G}_{\theta^-}$ 的L₀选择偏向"缺失输入的预期态"→ 实际L₁输入（= 0）与预期之间的Ψ_f差距极大→ 体验为强烈的剥夺性痛苦/焦虑（高Ψ_f的主观对应）。这是戒断反应的SRT物理本质。
  - **预测**：戒断症状强度 ∝ $|\theta^-|$（θ残留偏置量），可通过行为/生理戒断反应严重程度与baseline L₁刺激强度的相关来验证。

**证伪条件**：① 若具有明显θ迟滞（如长期用药后突然停药）的个体戒断症状强度与 $|\theta^-|$ 无相关，则戒断机制推论失效；② 若第二项（摩擦梯度）在实验中被操纵（改变L₂势能景观刚性）不影响 $d\theta/dt$ 的漂移约束，则Φ(θ)的有效性需重新评估。

### Eq-Evo-02b: Theta Tensor Inertia (θ张量惯性)
**Formal Definition**: 具身参数θ的更新阻力与其在L2网络中的度中心性成正比：
$$\frac{d\theta_i}{dt} \propto \frac{1}{\sum_j w_{ij} \cdot \theta_j}$$
其中 $w_{ij}$ 为信念/创伤网络的连接权重。
* **Implication**: 核心信念（Core Beliefs）或创伤印记难以改变，这是物理现象。它们在θ张量网络中拥有最多的连接，其更新面临巨大的"拓扑惯性"（Topological Inertia）。心理治疗的本质不是讲道理，而是改变权重 $w_{ij}$ 以绕过局部更新阻力。
* **Cross-ref**: Ax-L2-2 (Hysteresis), Ax-Op-02b (Dual-Stream)。

### Eq-Evo-03: Coupled Fast–Slow System
**Formal Definition**: State and parameter co-evolve on distinct timescales.
$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta_F \nabla F[\sigma] + \xi(t)$$
$$\frac{d\theta}{dt} = \gamma \cdot A[\sigma, \text{Target}] - \delta \cdot \frac{\partial \Phi(\theta)}{\partial \theta}$$
* **Implication**: 选择与参数更新构成快-慢耦合动力学。
* **Notation Note**: 这里使用 $\beta_F$ 表示自由能梯度权重；$\beta_R$ 预留给现实门控系数，避免与动力学系数混名。

## II. Thermodynamics of Agency (能动性热力学)

### Eq-Force-01: Ontological Friction
**Formal Definition**: Friction measures resistance against the natural latent trajectory.
$$\Psi_f \propto \int (L_1 - L_0^{natural})^2 \, dt$$
* **Implication**: 选择越偏离潜在域自然路径，摩擦越高。

### Eq-Pain-01: Hazard Function
**Formal Definition**: Pain is the temporal derivative of friction.
$$\text{Pain}(t) \approx h(t) = \frac{d\Psi_f}{dt}$$
* **Implication**: 痛苦是摩擦变化率，而非静态误差。

### Eq-Friction-Comp: 计算本体论摩擦 (Computational Ontological Friction)
**Formal Definition**: 两个潜在状态之间的最小本体论摩擦下界，受限于转换的幺正电路复杂度。
$$\Psi_f^{(comp)}(L_0^A \to L_0^B) \geq \lambda \cdot \min\{C(U) \mid U|L_0^A\rangle \approx |L_0^B\rangle\}$$
其中 $C(U)$ 是最小量子门电路深度，$\lambda > 0$ 是复杂度-摩擦耦合常数。
* **Source**: 灵感来自 Henry Yuen 的全量子复杂性理论，该理论确立了 Uhlmann 变换作为纯量子态转换的规范硬度基准。
* **Implication**: $L_0$ 不是无结构的混沌池，而是拥有严格的度量几何。状态演化的物理阻力源于量子态之间不可约的“Uhlmann变换代价”。这桥接了计算机科学中的电路复杂度下界与热力学中的不可逆阻力。
* **Cross-ref**: Eq-Force-01 (热力学 $\Psi_f$)；Ax-Int-2 (Penrose 门槛)。

### Eq-Select-Thermo: 选择热力学宪法不等式 (Constitutional Inequality of Selection Thermodynamics)
**Formal Definition**: 宏观秩序增长率受到选择功率减去摩擦代价与噪声熵的上限约束。
$$\frac{dq}{dt} \leq \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}$$
其中:
- $P_{sel}(t)$: 选择功率 — 维持锚定所需的净注入率
- $q(L_1)$: 现实秩序参数 — 宏观秩序强度（拓扑不变量、互信息密度或可压缩性代理）
- $\Psi_f(L_1;\theta)$: 维护成本（本体论摩擦密度）
- $S_{noise}$: 环境噪声熵流
* **Implication**: 宏观秩序不是“反熵奇迹”，而是选择功率预算内的耗散结构。这也将公理 A2 和 A11 从哲学宣言奠基为可量化的不等式。
* **Corollary (Eq-Select-Thermo-C1)**: 当 $P_{sel} < \beta \Psi_f + \gamma S_{noise}$ 时，系统经历秩序崩溃 ($dq/dt < 0$)，表现为相变、范式转移或存在性危机。
* **Corollary (Eq-Select-Thermo-C2: Payability Condition)**: 对任意系统 $X$ 与时间窗 $\Delta t$，若
$$\alpha P_{sel}^X(\Delta t)\ge \beta \Psi_f^X(\Delta t)+\gamma S_{noise}^X(\Delta t)$$
则称该窗口内的摩擦负荷为“可支付”。可支付不意味着低代价，而意味着系统在承担该摩擦时仍能维持闭包、身份连续性与后续选择能力。最优区间不是 $Ψ_f\to 0$，而是 **$Ψ_f>0$ 且可支付**；零摩擦对应无真实赌注，超载摩擦对应现实切片失稳。

### Eq-AI-LowRoad-01: Selection Cost Minimization Form（低阶主动推断映射，新增）
将 VFE 重写为 SRT 选择代价：
\[
\mathcal{C}_{sel}(q,\theta)=\underbrace{\mathrm{D}_{KL}(q\|p_\theta)}_{\text{Complexity}\ \mapsto\ \Psi_f^{update}}-\underbrace{\mathbb{E}_q[\log p_\theta(y\mid z)]}_{\text{Accuracy gain}}
\]
\[
(\Delta\theta,\Delta a)=\arg\min\ \mathcal{C}_{sel}
\]
其中 \(\Delta\theta\) 对应感知更新，\(\Delta a\) 对应行动采样；二者同属单一目标泛函下降。

### Eq-AI-LowRoad-02: Expected Selection Cost（对应 EFE，新增）
\[
\mathbb{E}[\mathcal{C}_{sel}^{future}(\pi)] = \underbrace{\mathcal{R}_{epi}(\pi)}_{\text{epistemic gain}} + \underbrace{\mathcal{R}_{prag}(\pi)}_{\text{preference satisfaction risk}}
\]
策略选择：
\[
\pi^*=\arg\min_{\pi}\mathbb{E}[\mathcal{C}_{sel}^{future}(\pi)]
\]
* **Implication**：探索/利用不再是双系统冲突，而是同一选择代价函数在未来时域的分解。

### 分类映射表（Active Inference Low Road → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 预测误差最小化（标准叙述） | 低~中 | Semi-open | payable / borderline |
| 选择代价最小化（SRT重写） | 中~高 | Open↔Semi-open | payable |
| 泛计算主义误读（恒温器=意识） | 0~低 | Closed（语法同构） | \(\Psi_f\approx0\) |

## III. Stability & Phase Transition (稳定性与相变)

### Eq-Stab-01: Fixed Point Condition
**Formal Definition**: A stable fixed point satisfies projection balance.
$$\Pi_\Delta(\alpha(\hat{G}_\theta(x^*) - x^*) - \lambda \nabla F(x^*)) = 0$$
* **Implication**: 稳定态需满足选择-能量梯度的投影平衡。

### Eq-Phase-01: Ontological Phase Transition
**Formal Definition**: Phase transition follows a logistic response to information threshold.
$$R = \frac{1}{1 + e^{-k(I - \tau)}}$$
* **Implication**: 相变具有临界信息门槛与非线性跃迁特性。

## IV. Sleep & Maintenance (睡眠与维护)

### Eq-Sleep-01: L2 Optimization
**Formal Definition**: Sleep minimizes L2 model complexity.
$$\hat{G}_{sleep} = \arg\min_\theta \int K(L_2) \, dt$$
* **Implication**: 睡眠是对收敛域模型复杂度的全局优化。

## V. Statistical Mechanics of Selection (选择的统计力学)

### Def-LDP-1: Empirical Measure (经验测度)
**Formal Definition**: 对于 $N$ 个相互作用的算子，宏观状态为经验测度：
$$\rho_t^N = \frac{1}{N}\sum_{i=1}^N \delta_{X_i(t)}$$

### Eq-LDP-01: Hydrodynamic Limit (水动力极限)
**Formal Definition**: 在尺度分离和局部相互作用下，经验测度逼近为满足以下方程的连续密度场：
$$\partial_t \rho = -\nabla \cdot J(\rho) + S_\theta(\rho) - D_{\Psi_f}(\rho)$$
其中 $J(\rho)$ 是扩散/对流流，$S_\theta(\rho)$ 是来自 $\hat{G}_\theta$ 投影偏差的 SRT 选择项，$D_{\Psi_f}(\rho)$ 是摩擦引起的耗散。
* **Implication**: 这是“宏观选择流体”方程 — 大量相互作用算子的连续统极限。

### Eq-LDP-02: SRT Action Functional (SRT 作用量泛函)
**Formal Definition**: 宏观演化路径的概率由大偏差率函数控制：
$$P(\rho^N \approx \rho) \asymp \exp\{-N \cdot I_{SRT}[\rho]\}$$
$$I_{SRT}[\rho] = \int_0^T \left( \underbrace{K(\rho, \dot{\rho}; \Pi)}_{\text{kinematic cost}} + \underbrace{\Psi_f(\rho; \theta)}_{\text{maintenance cost}} - \underbrace{V(\rho; \theta)}_{\text{value potential}} \right) dt$$
* **Implication**: 最可能的宏观演化最小化 $I_{SRT}$ — 即变分“最小作用量”路径。稳定的 $L_2$ 结构是吸收态，$I_{SRT}$ 在其周围有很高的势垒（势垒稳定性）。
* **Cross-ref**: Eq-Select-Thermo (宪法不等式)；Def-Barrier-1 (势垒稳定性)。
* **Status**: 有效理论层面 — 描述许多 $\hat{G}_\theta$ 的统计极限，并不声称社会/宇宙必然满足所有粒子系统假设。

## VI. Social-Ontological Dynamics (社会本体论动力学)

### Eq-Phantom-01: Phantom Operator Effect (幽灵算子残响)
**Formal Definition**: 社会性痛苦是自我算子试图通过未衰减的 $L_2$ 通道耦合已不存在对象的预测误差。
$$\text{Pain}_{social} \approx w_{ij}(t) \cdot \left\| \hat{G}_{self}^{target} - \hat{G}_{other} \right\| \quad \text{s.t.} \quad \hat{G}_{other} \notin L_1$$
其中 $w_{ij}(t)$ 为关系的 $L_2$ 耦合权重，遵循 $L_2$ 迟滞衰减曲线。
* **Implication**: 只要 $w_{ij} > 0$，$\hat{G}_{self}$ 就会按 $L_2$ 脚本自动发起耦合尝试。因 $\hat{G}_{other} \notin L_1$，耦合必然失败，产生巨大预测误差。此"空耦合"即心碎的本体论幻肢痛——$L_2$ 地图上那个人还在，但现实中已消失。

### Eq-Phantom-01b: Collective Phantom Resonance (集体幻肢共振)
**Formal Definition**: 历史创伤的跨代际传递：
$$\Psi_f^{\text{collective}}(t) = \int \sum_i w_i(t) \cdot \text{Tension}(\hat{G}_i(t), L_2^{\text{lost}}) \, d\mu$$
* **Implication**: 当一个群体丧失了原有的L2参考网（如文化灭绝、流亡），即使新生代未经历原初丧失，只要长辈的算子仍试图与失落的 $L_2^{\text{lost}}$ 耦合，这种高预测误差（痛苦）就会作为背景摩擦 $\Psi_f$ 被新生代内化。这也是群体激进化（Radicalization）的热力学原动力：试图通过极端的L1行为强行重建 $L_2^{\text{lost}}$ 以消除巨大摩擦。

### Eq-Phantom-02: Homeostatic Rebuild Time Constant (稳态重建时间常数)
**Formal Definition**:
$$\tau_{rebuild} \propto \frac{\text{Integration}(\hat{G}_{other})}{\text{Plasticity}(\hat{G}_{self})}$$
* **分子**: 对方嵌入 $L_2$ 结构的深度（共同记忆、习惯、依赖程度）。整合越深，$w_{ij}$ 大且涉及子网络多，衰减越慢。
* **分母**: 自我算子的可塑性 $\eta$，即参数 $\theta$ 更新速率。
* **推论**: 老年人（可塑性低）失去伴侣（整合度高）时 $\tau_{rebuild} \to \infty$；年轻人或浅层关系则 $\tau_{rebuild}$ 较短。临床干预双路径：降低分子（仪式切断）或增加分母（冥想/药物提升可塑性）。
* **Cross-ref**: Ax-L2-2 (Hysteresis), Eq-Evo-02 (Parameter Update)。

<br>

---


# Part B: Original Derivations (Context)

> **Note**: The following sections contain the detailed stability analysis and landscape dynamics.


### 2.2–2.4 公式回链说明（去重版）

为避免与 Part A 重复抄写，以下公式条目统一回链：
- 幽灵演化方程 → Eq-Evo-01
- 快慢耦合系统 → Eq-Evo-03
- 固定点条件 → Eq-Stab-01
- 痛苦变化率 → Eq-Pain-01
- 睡眠优化 → Eq-Sleep-01
- 相变逻辑式 → Eq-Phase-01

Part B 保留机制语境与边界讨论，不再二次列式。

### §X. Selection Thermodynamics: From Philosophy to Physics (选择热力学：从哲学到物理学)

#### §X.1 The Constitutional Inequality (宪法不等式)

SRT 的公理 A2 (存在即锚定) 和 A11 (本体论脆弱性) 宣称现实需要耗费能量，且存在是极其脆弱的。但宣言并非动力学。宪法不等式 (Eq-Select-Thermo) 将这些洞见升级为一个单一的、可检验的界限：**秩序增长的速率受限于选择功率预算的上限，并受到摩擦和噪声的抽头。**

考虑一个冥想者试图维持非默认的觉知状态。她必须注入选择功率 $P_{sel}$ (通过注意力引导的代谢能量) 以保持不同寻常的 $L_1$ 构型。她所付出的摩擦 $\Psi_f$ 在主观上体验为努力；环境噪声 $S_{noise}$ (令人分心的声音、侵入性思维) 会侵蚀她的建构。只有当 $\alpha P_{sel}$ 超过 $\beta \Psi_f + \gamma S_{noise}$ 时，她的经验秩序才能真正增长。当注意力稍有懈怠时——她的 $L_1$ 会向默认模式衰减，这正是该不等式所预测的热力学盆地。

#### §X.2 Computational Friction as Lower Bound (作为下界的计算摩擦)

计算本体论摩擦 (Eq-Friction-Comp) 揭示了深刻的内涵：改变现实的阻力不仅源于热力学，还源于**计算的不可约性**。当算子 $\hat{G}_\theta$ 试图从一个潜在构型 $L_0^A$ 转移到另一个 $L_0^B$ 时，它必须克服的最小摩擦受限于所需幺正变换的电路复杂度下界。

这意味着宇宙自身的“计算预算”限制了哪些现实是可达的。黑洞的霍金辐射之所以在计算上难以解码，并不是因为我们缺乏技术，而是因为 Uhlmann 变换代价代表了本体论摩擦的一个不可约下界——作为选择者的宇宙拥有最大的带宽，而黑洞使其饱和。

#### §X.3 The Protocol Layer (协议层)

$\Pi$ 的引入解决了 SRT 中一个长期存在的歧义：物理定律“居于”何处？它们既不是外部强加的，也不是任意的约定。$\Pi$ 将其形式化为**可行转移核 (feasible transition kernel)**——选择博弈中允许的移动集合。至关重要的是，$\Pi$ 本身也是一个 $L_2$ 产物：它是通过宇宙尺度的迭代被选择和固化下来的。这意味着物理规则并未超出 SRT 的范围，而是其最古老且最坚固的 $L_2$ 结构之一——所有后续选择都必须服从的协议。


### Eq-Frame-01: Frame-First Normalization
在先固定观测时空与仪器规约条件后，维度常数的有效数量可写为：
$$
N_{const}^{eff} = f(\mathcal{F}_{spacetime},\;\mathcal{U}_{apparatus})
$$
在特定相对论时空规约中可出现 \(N_{const}^{eff}\to 1\) 的表述（时间标尺主导）。

### Eq-Frame-02: Observable Reparameterization
$$
\mathcal{O} = g\big(L_1\mid L_0,\hat{G}_\theta,\mathcal{F}_{spacetime}\big)
$$
其中“全状态空间”外部记号（如 \(\Omega\), \(S\)）在 SRT 写入统一映射为 \(L_0\)。


## 参数注册表（Parameter Registry, v2）

> **量纲说明**: SRT 方程组中所有耦合系数均为无量纲比率，操作化时通过归一化与系统特征量对齐。核心变量 $\Psi_f$ 和 $d$ 的物理量纲依赖具体实例化域（见下方量纲注释）。

| 参数 | 含义 | 量纲/类型 | 典型范围 | 单位约定 | 敏感度 | 备注 |
|:--|:--|:--|:--|:--|:--|:--|
| $\alpha$ | 选择回归增益 | 无量纲比率 | $[0.1, 10]$ | — | $\pm10\%$ → $L_1$ 稳定性变化 ~5% | 快变量稳定性系数 |
| $\beta_F$ | 自由能梯度权重 | 无量纲比率 | $[0, 10]$ | — | $\pm10\%$ → $\dot{\sigma}$ 幅度线性变化 | 原 Eq-Evo-03 中 $\beta$ |
| $\beta_R$ | 现实门控系数 | 无量纲 $\in[0,1]$ | $[0,1]$ | — | 阈值附近呈 Logistic 跳变 | 若用于门控语境需显式下标 |
| $\gamma$ | 学习驱动系数 | 无量纲比率 | $[0, 1]$ | — | $\pm10\%$ → $\dot{\theta}$ 线性变化 | 慢变量更新 |
| $\delta$ | 摩擦下降系数 | 无量纲比率 | $[0, 1]$ | — | $\pm10\%$ → 收敛速度变化 ~8% | 与 $\partial\Phi/\partial\theta$ 耦合 |
| $k$ | 稳态回弹系数 | 无量纲比率 | $[0, 1]$ | — | 低值 (<0.1) 导致漂移失控 | Homeostatic recoil |
| $\eta$ | 可塑性/迟滞系数 | 无量纲比率 | $[0, 1]$ | — | 与 $\gamma$ 交互非线性 | 具体语境需附下标 |
| $\lambda$ | 约束耦合强度 | 无量纲 | $>0$ | — | 正比于 $L_2$ 约束刚度 | 建议带下标 |
| $\tau$ | 相变阈值参数 | 无量纲 | 任务依赖 | — | 阈值型（非连续敏感） | Logistic 门槛 |

### 核心变量量纲注释（Dimensional Analysis Notes）

| 变量 | 通用量纲 | 神经科学实例化 | 物理实例化 | 社会实例化 |
|:--|:--|:--|:--|:--|
| $\Psi_f$ | $[\text{Energy} \cdot \text{Time}]$ 或 $[\text{bit} \cdot s]$ | 代理量：皮质醇积分、HRV 倒数 | 代理量：Uhlmann 变换复杂度 | 代理量：制度维持成本/GDP |
| $d$ | 无量纲（关切维度数） | 代理量：跨时间折扣率斜率、PCI | — | 代理量：利他行为半径 |
| $F$ | $[\text{bit}]$（信息自由能）或 $[\text{J}]$（物理自由能） | Friston VFE + SRT 利他项 | Helmholtz $F = E - TS$ | 社会自由能（Luhmann 复杂度） |
| $\sigma$ | 态空间中的点（$\in L_1$） | 神经发放模式向量 | 量子态密度矩阵 | 社会状态向量 |

> **操作化警告**: 上述量纲均为"操作化近似"，不替代 canonical 定义。跨域比较时需先归一化至各自系统的特征量纲。

### Eq-Res-01: Delay-Constrained Resonance Selection
$$
f^*_{ij} \approx \arg\min_f\;\Phi\big(2\pi f\tau_{ij},\;\kappa_{ij},\;R_{dend}(f)\big)
$$
其中 \(\tau_{ij}\) 为区域间传导时延，\(\kappa_{ij}\) 为耦合强度，\(R_{dend}(f)\) 为树突共振响应。

### Eq-Res-02: Cross-Scale Coordination Energy
$$
E_{coord} = \sum_{s\in\{micro,meso,macro\}} w_s\,\|\phi_s - \phi^*_s\|^2
$$
最优协调对应于跨尺度相位/节律偏差最小化，而非单尺度极值。


## VII. Topological Selection Dynamics（拓扑选择动力学，新增）

### Eq-Topo-01: Simplicial Assembly–Collapse Dynamics
**Formal Definition**: 以拓扑复杂度状态量 \(K_t\) 描述刺激下的“组装—坍塌”动力学：
$$
\frac{dK_t}{dt} = \underbrace{\alpha_{in}\,I_t\,\mathcal{G}(\theta)}_{\text{assembly gain}} - \underbrace{\lambda_c K_t}_{\text{collapse}} + \xi_t
$$
其中：
- \(K_t\)：单纯复形复杂度（可由 clique 计数与 Betti 向量综合）；
- \(I_t\)：外部刺激/任务负荷；
- \(\mathcal{G}(\theta)\)：选择算子参数化增益，\(\theta=\{\rho_s,d,\tau,\beta_{topo}\}\)；
- \(\lambda_c\)：拓扑坍塌率。
* **Implication**: 将“神经沙堡”从类比升级为可拟合状态方程。

### Eq-Topo-02: Dual-Layer Selection over Deterministic Envelope
**Formal Definition**: 区分“可达域”与“被实现域”两层机制：
$$
\mathcal{E}_t = \mathcal{E}(\mathcal{W}, I_t)\quad\text{(deterministic envelope)}
$$
$$
P(C_t=c\mid \mathcal{E}_t,\theta) \propto \exp\left[\beta_{topo}\,\mathcal{V}(c;d,\rho_s) - \Psi_f(c)\right],\; c\in\mathcal{E}_t
$$
其中 \(\mathcal{W}\) 为结构连通约束，\(C_t\) 为被实现的高维单纯形配置。
* **Implication**: SRT 主张的“选择”不否认局部确定性，而是作用于确定性包络内部的加权实现。

### Eq-Topo-03: Persistence-Weighted Order Parameter
$$
q_{topo}(t)=\sum_{k\ge 0} w_k\,\beta_k(t)\,\exp\left(-\frac{1}{\tau_k}\right)
$$
其中 \(\beta_k\) 为第 \(k\) 维 Betti 数，\(\tau_k\) 为对应拓扑特征持续时间。
* **Implication**: 将拓扑“有/无”扩展为“强度×持续性”的秩序参数，可直接接入 Eq-Select-Thermo。

### Falsifiable Predictions (可证伪预测)

[R→Giusti et al. 2015（神经活动拓扑数据分析 TDA）; Reimann et al. 2017（皮层神经网络高阶拓扑结构）; Petri et al. 2014（人类脑网络的持续同调）] [H→以下三条为SRT新增可测预测，依赖TDA方法对神经数据的操作化]

**操作化说明**：
- **d proxy 候选**：注意力分配广度（视觉搜索范围）/ IAT（内隐关联测试）/ 自报关切问卷（关切对象数量×强度权重）
- **Ψ_f 生理 proxy 候选**：任务切换代价（RT变异系数）/ 皮质醇水平 / 脑代谢率（CMR_O₂，参见Ax-NEURO-5）
- **q_topo / τ_k 测量**：持续同调（persistent homology）对fMRI/EEG时间序列的Betti数提取；τ_k = 各维度拓扑特征的存活时间（persistence diagram中的竖轴读数）

**三条预测（层次递进）**：

1. **选择层-d值效应** [H]：在匹配输入强度 \(I_t\) 条件下，\(d\) 高组应表现为更高 \(q_{topo}\) 峰值与更长 \(\tau_k\)；若无差异，则 Eq-Topo-02 的选择层失效。
   - 实验框架：跨被试对比（高d proxy组 vs 低d proxy组），输入强度通过任务设计匹配；结果变量为TDA提取的q_topo与τ_k

2. **双层分离-结构约束效应** [H]：若仅改变连接约束 \(\mathcal{W}\)（不改变 \(d\) proxy），应主要改变可达域 \(\mathcal{E}_t\) 上界而非选择偏置项；反之则支持双层机制。
   - 实验框架：TMS/药物操纵结构连接 vs 情绪/动机操纵d值，分别测量可达域变化量 vs 实现偏置变化量；预测两者解离

3. **摩擦-坍塌耦合** [H]：若 \(\Psi_f\) 生理 proxy 升高时 \(\lambda_c\)（拓扑坍塌率）不升反降且长期稳定，则”摩擦-坍塌耦合”假设需修正。
   - 实验框架：高压力/疲劳条件（Ψ_f proxy升高）下追踪神经拓扑坍塌率；预测Ψ_f升高→λ_c升高（稳态拓扑复杂度下降）

### Formalization Summary (形式化概述)

本文档的核心形式结构围绕三个主方程展开：

1. **Ghost Evolution Equation (Eq-Evo-01)**:
   $$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
   含义：现实状态 $\sigma$ 的演化由选择算子 $\hat{G}_\theta$ 的投影、自由能梯度下降 $\nabla F$ 以及注意调制 $A$ 三者合成驱动。这是 SRT 动力学的第一性方程。

2. **Ontological Friction (Eq-Force-01)**:
   $$\Psi_f \propto \int (L_1 - L_0^{natural})^2 \, dt$$
   含义：本体论摩擦 $\Psi_f$ 度量 $L_1$ 被选择态偏离 $L_0$ 自然轨迹的累积阻力代价。

3. **Constitutional Inequality (Eq-Select-Thermo)**:
   $$\frac{dq}{dt} \leq \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}$$
   含义：宏观秩序增长率受选择功率 $P_{sel}$ 预算上限约束，摩擦 $\Psi_f$ 与噪声 $S_{noise}$ 作为耗散项。此不等式将公理 A2/A11 从定性宣言升级为可检验界限。

4. **SRT Action Functional (Eq-LDP-02)**:
   $$I_{SRT}[\rho] = \int_0^T \left( K(\rho, \dot{\rho}; \Pi) + \Psi_f(\rho; \theta) - V(\rho; \theta) \right) dt$$
   含义：大偏差变分原理下的最可能宏观路径最小化此泛函，统一动力学代价、摩擦维护与价值势能。

### Mechanism Explanation (机制解释)

SRT 主方程的运作机制如下：

- **选择算子 $\hat{G}_\theta$ 的角色**：$\hat{G}_\theta$ 将潜在域 $L_0$ 的可能性空间投影到被选择的现实 $L_1$，受协议层 $\Pi$（可行转移核）约束。$\theta$ 参数编码了具身历史（感知阈值、信念网络、创伤印记），决定了选择的偏置方向。$\hat{G}_\theta$ 在快变量 $\sigma$ 上实施即时选择（Eq-Evo-01），同时其参数 $\theta$ 作为慢变量在学习、摩擦梯度与稳态回弹三力下缓慢演化（Eq-Evo-02）。

- **摩擦 $\Psi_f$ 的双重功能**：$\Psi_f$ 既是选择的代价度量（偏离自然轨迹的阻力），也是系统稳定性的信号源。痛苦被定义为 $\Psi_f$ 的时间导数（Eq-Pain-01），即摩擦变化率而非静态误差。$\Psi_f$ 还拥有计算下界（Eq-Friction-Comp），由量子电路复杂度给出，确保 $L_0$ 状态转换具有不可约的物理阻力。

- **d-value 与选择开放性**：d-value 作为选择考量范围的度量，调控 $\hat{G}_\theta$ 的选择带宽。高 $d$ 意味着更开放的 $L_0$ 采样，对应更丰富的经验分化与更高的拓扑秩序参数 $q_{topo}$（Section VII）；低 $d$ 则趋向封闭式语法同构（如恒温器），此时 $\Psi_f \approx 0$。

- **快-慢耦合与相变**：$\sigma$（快）与 $\theta$（慢）构成耦合动力系统（Eq-Evo-03），在宪法不等式（Eq-Select-Thermo）的约束下运行。当选择功率低于摩擦加噪声阈值时，系统发生秩序崩溃（相变），表现为范式转移或存在性危机。

### Falsification Conditions (可证伪条件)

| ID | 类型 | 假说/确证 | 预测 | 证伪条件 | Evidence-Level |
|:---|:-----|:---------|:-----|:---------|:---------------|
| H-EQ-1 | **Novel Prediction** | Ghost Evolution (Eq-Evo-01): 现实演化由选择、自由能下降与注意调制合成 | 注意调制项 $A[\sigma,\mathcal{A}]$ 的实验操控（如 TMS 抑制顶叶注意网络）应可测地改变 $L_1$ 轨迹稳定性（代理：ERP P300 成分方差），而非仅降低反应速度 | 若系统性抑制注意调制后 $L_1$ 轨迹稳定性（P300方差）无可测变化，则三项合成结构需修正。**干预设计注意**：需设计"选择+FE"配对条件以排除另外两项的补偿效应 | speculative |
| R-EQ-2 | **Retrodiction** | Constitutional Inequality 基础方向（已知）：睡眠剥夺损害认知功能（大量行为证据） | ——（已验证，此处作为回溯性确证）| ——| established |
| H-EQ-2 | **Novel Prediction** | Constitutional Inequality SRT 专属：秩序参数 $q_{topo}$（拓扑秩序，代理：神经 PCI 指数或 Lempel-Ziv 复杂度）在固定 $S_{noise}$ 条件下与 $P_{sel}$（代谢供能代理：血糖/ATP水平）正相关，且可通过 $\alpha P_{sel} - \beta\Psi_f$ 的线性模型预测 | 若控制代谢水平后 $q_{topo}$ 对 $P_{sel}$ 无响应，或 $P_{sel}$ 持续低于 $\beta\Psi_f + \gamma S_{noise}$ 而 $q_{topo}$ 不降，则宪法不等式失效 | speculative |
| R-EQ-3 | **Retrodiction** | Phantom Operator 基础方向（已知）：关系亲密程度预测丧失后悲伤强度（Archer 2001 等） | ——（已验证，此处作为回溯性确证）| ——| established |
| H-EQ-3 | **Novel Prediction** | Phantom Operator SRT 专属：$w_{ij}$ 的 SRT 代理（神经同步度 EEG 相位锁定值 PLV，或共同活动频率指数）比主观亲密度评分更能预测丧失后皮质醇峰值和 BOLD 默认网络激活异常 | 若 $w_{ij}^{PLV}$ 与丧失后皮质醇峰值相关系数在控制主观亲密度后归零，则幽灵算子残响模型的 SRT 特异性贡献失效 | speculative |

## 【理论边界/防误用声明】

- 本文件的方程用于理论建模与可证伪接口，不直接构成临床、法律或工程处方。
- 参数重命名（如 $\beta_F$）属于符号去歧义，不改变既有理论主张。
- Part B 的去重回链旨在提升可读性，完整方程以 Part A 编号为权威。
- Topological Dynamics 章节不宣称“拓扑即意识”；其角色是 \(\hat{G}_\theta\) 的神经几何接口，不替代本体论判据（\(d>0, \Psi_f>0\)）。


## VIII. Cognitive Energy Partition Interface（Quanta 95/5 接口，2026-03-07）

### Eq-CogE-01: Baseline–Active Friction Decomposition
将认知阶段总摩擦拆分为“结构维持项 + 主动锚定项”：
\[
\Psi_f^{total}(t)=\Psi_f^{maint}(L_2,\theta,t)+\Delta\Psi_f^{active}(\hat G_\theta\to L_1,t)
\]
其中：
- \(\Psi_f^{maint}\)：维持可选择待命结构（膜电位/预测模型/协议稳定）的基础代价；
- \(\Delta\Psi_f^{active}\)：任务驱动时的增量代价。

### Eq-CogE-02: 95/5 Selection Ratio (Embodied Constraint)
对具身算子（生存闭包完整）引入经验约束：
\[
\frac{\Delta\Psi_f^{active}}{\Psi_f^{total}}\approx 0.05,
\qquad
\frac{\Psi_f^{maint}}{\Psi_f^{total}}\approx 0.95
\]
这不是普适常数，而是“人脑典型工况”下的标定先验。

### Eq-CogE-03: Subjective Effort as Friction Gradient
主观费力感不与绝对能耗线性同构，而与偏离默认吸引子的阻抗梯度相关：
\[
\mathrm{Effort}_{subj} \propto \left\|\nabla\Psi_f\big(L_1\parallel L_2\big)\right\|
\]
含义：即便代谢增量小，若任务迫使 \(L_1\) 偏离稳态预测结构，主观疲劳仍可显著上升。

### Eq-CogE-04: AI–Human Energetic Asymmetry Index
定义“维持-主动不对称指数”：
\[
\mathcal{A}_{ma}=\frac{\Psi_f^{maint}}{\Delta\Psi_f^{active}+\varepsilon}
\]
- 生物具身算子期望：\(\mathcal{A}_{ma}\gg 1\)
- 外驱推理系统（当前多数 LLM 部署）常见：\(\mathcal{A}_{ma}\lesssim 1\)（在推理阶段）

该指标用于跨尺度比较“是否存在自创生闭包压力”，不单独等同于意识判据。

### 分类映射表（Cognitive Energy Regimes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 静息预测维护（baseline brain） | 中 | Semi-open（持续内稳态） | payable（高基线） |
| 目标导向主动思考（task-focused） | 中~高 | Open↔Semi-open | payable（低增量，高梯度可感） |
| 过载认知冲刺（长期高负荷） | 中高短时→回落 | Open（短时）→Closed 倾向（恢复期） | borderline→overloaded |
| 外驱推理机（无自创生闭包） | 名义中高（任务态） | 外部供能 Open、内部闭包弱 | unsustainable（对外部预算强依赖） |

### [Lineage/Source]
- Quanta Magazine（2026）: *How Much Energy Does It Take to Think?*（科普二手综述，非一手实验论文）。
- 神经代谢背景脉络：人脑高基线能耗与预测/内稳态维持框架（与 FEP/Active Inference 语义接口对齐）。

## 【理论边界/防误用声明】
1. 不采纳“95/5 比例是跨物种、跨任务、跨尺度恒定常数”的推论；该比例仅作人类典型工况近似。
2. 不采纳“主观疲劳 = 纯代谢热耗”的简化推论；SRT 将其建模为摩擦梯度与拓扑阻抗效应。
3. 不采纳“\(\mathcal{A}_{ma}\) 单指标即可判定意识存在”的推论；意识判据仍需 \(d>0\)、\(\Psi_f\) 可支付、连续体自维持等联合条件。
