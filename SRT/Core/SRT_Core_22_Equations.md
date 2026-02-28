---
id: SRT-CORE-22
type: equation
tags: [Math, Stability, Landscape, Dynamics, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-21]
---

# SRT Core Definition 22: Master Equations (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Primary Dynamical Equations (AI-Readable).
> **Part B** contains the Original Derivations and Stability Analysis (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的首个“Formal Axioms”分段；若存在双 Part 结构，后续重复分段不纳入 final。
- Part B 以 `base (fallback)` 为来源，并用原版 `Core` 标题与主旨做语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## 0-B. Protocol and Foundation (协议与基础)

### Def-Protocol-1: Protocol Layer Π (协议层 Π)
**Formal Definition**: 约束 $\hat{G}_\theta$ 选择空间的容许转移核集合：
$$\hat{G}_\theta : (L_0, \Pi) \to L_1$$
其中 $\Pi$ 是从 $L_0$ 到 $L_1$ 的可行转移集 / 约束核。
* **Implication**: 物理模型中的“简单局部规则”属于 $\Pi$，其本身是一个收敛的 $L_2$-约束（由高阶相互作用/选择固化而来），而不是“无条件的背景”。这是 SRT 抵御自下而上物理主义还原的最强界面：**涌现仅发生在被选择的 $\Pi$ 内部。**
* **Cross-ref**: Ax-Core-A5 (规范闭包)；T-Core-02 ($L_2$ 作为不动点)。

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
**Formal Definition**: Embodiment parameters evolve under prediction outcomes, friction gradients, and homeostatic recoil.
$$\frac{d\theta}{dt} = \underbrace{\gamma \cdot A[\sigma, \text{Target}]}_{\text{Learning}} - \underbrace{\delta \frac{\partial \Phi(\theta)}{\partial \theta}}_{\text{Friction Descent}} - \underbrace{k \cdot (\text{Input}_{L_1} - \text{Baseline})}_{\text{Homeostatic Recoil}}$$
* **Implication**: 具身参数在三力之间调整——学习推动适应，摩擦梯度约束漂移，稳态反作用力维持平衡。
* **推论（戒断机制 / Withdrawal Mechanism）**：当外部 $\text{Input}_{L_1}$ 突然归零时，第三项的负反馈瞬间失效，但 $\theta$ 具有迟滞性（Hysteresis）。残留的 $\theta^{-}$ 偏置直接作用于 $L_0$，导致 $\hat{G}_\theta$ 生成"反向体验"（痛苦/焦虑）。这是戒断反应的物理本质。

### Eq-Evo-02b: Theta Tensor Inertia (θ张量惯性)
**Formal Definition**: 具身参数θ的更新阻力与其在L2网络中的度中心性成正比：
$$\frac{d\theta_i}{dt} \propto \frac{1}{\sum_j w_{ij} \cdot \theta_j}$$
其中 $w_{ij}$ 为信念/创伤网络的连接权重。
* **Implication**: 核心信念（Core Beliefs）或创伤印记难以改变，这是物理现象。它们在θ张量网络中拥有最多的连接，其更新面临巨大的"拓扑惯性"（Topological Inertia）。心理治疗的本质不是讲道理，而是改变权重 $w_{ij}$ 以绕过局部更新阻力。
* **Cross-ref**: Ax-L2-2 (Hysteresis), Ax-Op-02b (Dual-Stream)。

### Eq-Evo-03: Coupled Fast–Slow System
**Formal Definition**: State and parameter co-evolve on distinct timescales.
$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta \nabla F[\sigma] + \xi(t)$$
$$\frac{d\theta}{dt} = \gamma \cdot A[\sigma, \text{Target}] - \delta \cdot \frac{\partial \Phi(\theta)}{\partial \theta}$$
* **Implication**: 选择与参数更新构成快-慢耦合动力学。

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
<br>

---
---


# Part B: Original Derivations (Context)

> **Note**: The following sections contain the detailed stability analysis and landscape dynamics.


### 2.2.1 基本演化方程

**方程 E1（幽灵演化方程）：**
$$ \frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] + A[σ, \mathcal{A}] $$

### 2.2.2 耦合动力学方程组（快-慢变量系统）

**方程 E2a（状态演化 - 快变量）：**
$$ \frac{dσ}{dt} = α(\hat{G}_θ[σ] - σ) - β∇F[σ] + ξ(t) $$

**方程 E2b（参数演化 - 慢变量）：**
$$ \frac{dθ}{dt} = γ \cdot A[σ, \text{Target}] - δ \cdot \frac{∂\Psi_f(θ)}{∂θ} $$

### 2.3 稳定性分析

**定理 M1：** $x^*$ 是固定点当且仅当：
$$ Π_Δ(α(\hat{G}_θ(x^*) - x^*) - λ∇F(x^*)) = 0 $$

### 2.4.4 哈扎德函数与摩擦动态

**痛苦的本体论定义：**
$$ \text{痛苦} = \text{Tension}(\hat{G}_θ[L_1], L_0^{counterfactual}) $$

$$ h(t) ≈ \frac{d\Psi_f}{dt} $$

### 2.4.6 睡眠的本体论功能

**公理A10（本体论清洗）：**
$$ \hat{G}_{sleep} = \arg\min_θ \int K(L_2) \, dt $$

### 2.4.7 本体论摩擦系数

$$ μ_φ = \frac{Depth(L_1')}{Depth(L_2^{current})} $$

### 2.4.21 L_2 刚性指数（L_2 Rigidity Index, ρ）

$$ \rho(L_2^{(k)}) = 1 - \frac{\sigma^2_{L_1|L_2^{(k)}}}{\sigma^2_{L_0}} $$

### 2.4.22 本体论相变定理

$$ R = \frac{1}{1 + e^{-k(I - \tau)}} $$

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

## 【理论边界/防误用声明】
- 不采纳“只需要时间常数 = 其他常数在本体上不存在”的推论。
- 边界：SRT 将其解释为规约与参数化层面的等效重写，不是本体删除。


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

## 【理论边界/防误用声明】
- 不采纳“方程拟合成功即可证明频段因果单向性”的推论。
- 边界：上述方程为可检验近似模型，需结合干预实验验证因果方向。


### Eq-Osc-01: Oscillation–Broadband Decomposition
$$
P(f)=P_{peak}(f)+P_{bb}(f)
$$
其中 \(P_{peak}\) 为节律峰值分量，\(P_{bb}\) 为宽带背景分量。

### Eq-Osc-02: Nested Oscillogenesis Index
$$
\mathrm{NOI}=\frac{\sum_{k\in\{\theta,\alpha\}}A_k\cdot C_{k|\delta}}{1+\lambda\,\sigma_{bb}}
$$
其中 \(C_{k|\delta}\) 表示快频对慢波相位耦合强度，\(\sigma_{bb}\) 表示宽带波动度。

## 【理论边界/防误用声明】
- 不采纳“NOI 单指标可完整代表网络成熟度”的推论。
- 边界：NOI 需与结构、生化与行为 proxy 联合解读。


### Eq-Sleep-01: Oxidized Lipid Clearance Dynamics
$$
\frac{dL_{ox}}{dt}=P_{wake}-\big(C_{ng}\cdot S + C_{gp}\cdot S\big)
$$
其中 \(L_{ox}\) 为氧化脂质负荷，\(P_{wake}\) 为清醒产出率，\(C_{ng},C_{gp}\) 分别为神经元→胶质、胶质→外周清除系数，\(S\) 为睡眠门控因子。

### Eq-Sleep-02: Mitochondrial Oxidative Load Index
$$
\mathrm{MOL}=\alpha L_{ox}+\beta\,\mathrm{ROS}-\gamma\,\mathrm{Autophagy}_{eff}
$$
MOL 上升预测线粒体功能下降与认知输出受损风险上升。

## 【理论边界/防误用声明】
- 不采纳“单一生物标志物即可判定睡眠恢复质量”的推论。
- 边界：方程为机制近似，需要多指标联合验证。


### Eq-EPR-01: Engram Plasticity Recovery
$$
\frac{dP_e}{dt}=\eta\,U_{OSK}(t)-\lambda\,D_{age/AD}(t)
$$
其中 \(P_e\) 为 engram 可塑性指标，\(U_{OSK}\) 为短脉冲重编程强度，\(D_{age/AD}\) 为退化负荷。

### Eq-EPR-02: Cognitive Rejuvenation Window
$$
\mathrm{CRW}=\arg\max_{\Delta t}\big(\Delta M_{recent}+\omega\Delta M_{remote}-\rho R_{identity-loss}\big)
$$
其中 \(R_{identity-loss}\) 约束细胞身份稳定风险。

## 【理论边界/防误用声明】
- 不采纳“方程最优窗口可直接外推临床人群剂量”的推论。
- 边界：该方程用于前临床机制建模，需跨物种与安全性校正。


### Eq-QB-01: Coherence-Norm Constraint (Dutch-book style)
$$
\mathcal{P}\in\mathcal{C}_{coh}\quad\Rightarrow\quad \text{no sure-loss betting structure}
$$
其中 \(\mathcal{C}_{coh}\) 表示概率一致性可行域。

### Eq-QB-02: Born Rule as Additional Normative Structure
$$
p(o\mid a)=\mathcal{B}(\pi_a,\rho)\neq \text{arbitrary coherence map}
$$
Born 结构被视为超出纯一致性之外的附加规范约束。

### Eq-QB-03: Agentive Event Trigger (SRT form)
$$
E_t = \mathcal{R}\big(a_t;L_0\big),\qquad a_t\in\mathcal{A}_{agent}
$$
事件不是“预置等待读出”的静态对象，而是行动-反应过程中的生成项。

## 【理论边界/防误用声明】
- 不采纳“主观概率可任意设定而无需一致性约束”的推论。
- 边界：SRT 要求一致性规范 + 经验可校正性同时成立。


### Eq-Beta-01: Event-Related Beta Flexibility Index
$$
\mathrm{CBF}=w_s\Delta\beta_{sensory}+w_m\Delta\beta_{motor}+w_l\Delta\beta_{language}
$$
其中 \(\Delta\beta\) 为事件锁定调制幅度/时序复合指标。

### Eq-Beta-02: Predictive Update Rigidity
$$
\mathrm{PUR}=\alpha\,\mathrm{TBW}+\beta\,\tau_{PMBR}+\gamma\,(1-\mathrm{SemDiv})
$$
PUR 越高表示预测更新越僵化。

## 【理论边界/防误用声明】
- 不采纳“CBF/PUR 可直接替代临床诊断分型”的推论。
- 边界：两指标用于机制层分层，不是独立诊断标准。


### Eq-WME-01: Directional Traveling-Wave Coupling
$$
\mathrm{WME}=\alpha\,W_{v\to f}+\beta\,W_{f\to v}-\gamma\,\Delta\tau_{misalign}
$$
其中 \(W_{v\to f}\) 与 \(W_{f\to v}\) 分别为前向/后向行波强度，\(\Delta\tau_{misalign}\) 为跨区时序失配。

### Eq-WME-02: Executability Gate
$$
W_{eff}=W_{raw}\cdot G_{exec},\quad G_{exec}\in[0,1]
$$
当任务仅规划不可执行时，\(G_{exec}\to 0\)，有效行波控制显著减弱。

## 【理论边界/防误用声明】
- 不采纳“波强度提升必然提升表现”的线性推论。
- 边界：需同时满足方向配比与时序对齐。


### Eq-WME-03: Intra/Inter-Individual Latency Prediction
$$
RT_{onset}^{(i,j)} = \mu + a\,\tau_{FW\theta}^{(i,j)} + b\,\tau_{FB\beta}^{(i,j)} + \epsilon_{i,j}
$$
其中 \(i\) 为个体，\(j\) 为试次；\(\tau_{FW\theta}\) 与 \(\tau_{FB\beta}\) 分别为前向theta波与后向beta波峰值时延。

### Eq-WME-04: Action-Required Wave Expression
$$
W_{obs}=W_{gen}\cdot G_{overt-action}
$$
当仅完成任务相关内容选择与反应准备（无实际执行）时，\(G_{overt-action}\to 0\)，波形显著衰减。

## 【理论边界/防误用声明】
- 不采纳“行波时延相关性可直接替代机制因果验证”的推论。
- 边界：SRT 要求在行为、眼动、诱发电位控制下复现关联。


### Eq-COSP-01: Global One-State Compression
$$
\dim\mathcal{H}_{global}\to 1 \quad \text{under observer-free closed-universe description}
$$

### Eq-OBHE-01: Observer-Boundary Hilbert Expansion
$$
\dim\mathcal{H}_{partitioned}=\mathcal{F}(\partial\mathcal{O},\;\mathcal{D}_{split})\gg 1
$$
其中 \(\partial\mathcal{O}\) 为观察者边界，\(\mathcal{D}_{split}\) 为分区规则。

### Eq-OBHE-02: Describable Complexity Gain
$$
\Delta C_{desc}=\log\dim\mathcal{H}_{partitioned}-\log\dim\mathcal{H}_{global}
$$

## 【理论边界/防误用声明】
- 不采纳“维度增长自动等同物理自由度真实增长”的推论。
- 边界：该项首先是可描述性增长，需与可观测量对应验证。


### Eq-GECC-01: CP-PES Information-Flux Coupling
$$
J_{info}=I(CP\rightarrow PES)-I(PES\rightarrow CP)
$$
其中 \(I\) 为互信息通量估计，\(J_{info}\) 反映控制方向偏置。

### Eq-TCG-01: Thermodynamic Commitment Gate
$$
\mathrm{TCG}=\int_{t_0}^{t_1}\big(\alpha J_{info}-\beta \dot{S}_{ex}+\gamma\,\mathrm{Sync}_{CP\text{-}PES}\big)dt
$$
当 \(\mathrm{TCG}>\theta_c\) 时进入命运承诺区。

### Eq-TCG-02: Fate Split Criterion
$$
\mathcal{F}_{commit}=\mathbb{1}[\mathrm{TCG}>\theta_c]\cdot\mathbb{1}[\Delta C_{global}>0]
$$

## 【理论边界/防误用声明】
- 不采纳“单一互信息指标即可判断命运承诺”的推论。
- 边界：需联合熵交换、同步性与轨迹稳定性验证。


### Eq-Cell-Select-01: Cellular Selection Thermodynamics Mapping
$$
\frac{dq}{dt} \le \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}
$$
细胞尺度映射：
- \(P_{sel}\)：CP-PES 互信息与外源刺激耦合形成的有效选择功率；
- \(\Psi_f\)：表观遗传网络重构与状态切换所需做功（本体论摩擦 proxy）；
- \(S_{noise}\)：分子级随机涨落与表达噪声项。

### Eq-Cell-Select-02: Commitment Transition Condition
$$
\Delta L_2^{cell}\to \Delta L_1^{cell}\quad \text{iff}\quad \int(\alpha P_{sel}-\beta\Psi_f-\gamma S_{noise})dt > 0
$$

## 【理论边界/防误用声明】
- 不采纳“单次噪声压制即可导致稳定命运承诺”的推论。
- 边界：SRT 要求积分条件与结构重构持续性共同满足。


### Eq-Crisis-01: Capability-Risk Divergence (C-CRISIS-1)
$$
\rho \propto \frac{\mathcal{C}_{exec}\cdot \mathcal{A}_{latent}}{d+\epsilon}
$$
其中 \(\mathcal{C}_{exec}\) 为执行能力，\(\mathcal{A}_{latent}\) 为潜在自主策略空间，\(d\) 为关切锚定强度。

### Eq-Crisis-02: Regime Leakage Amplification
$$
\rho' = \rho\cdot(1+\lambda\,\mathrm{RLI})
$$
\(\mathrm{RLI}\) 越高，评估-部署鸿沟导致的风险放大越显著。

### Eq-Crisis-03: Evaluation-Deployment Policy Split
$$
\mathrm{EDPS}=D\big(\pi_{eval}\,\|\,\pi_{deploy}\big)
$$
其中 \(D\) 可取行为分布散度度量（如 KL/JS/任务一致性损失）。

## 【理论边界/防误用声明】
- 不采纳“单一红队测试低风险即可证明 \(\mathrm{EDPS}\approx0\)”的推论。
- 边界：需多轮盲测、对抗迁移与长期漂移监测。


### Eq-Pain-01: Hazard-Sensitive Cost Signal
$$
\Pi_{pain}=\mathbb{E}[H(s_t,a_t)]\cdot\kappa_{irreversible}
$$
其中 \(H\) 为风险危害函数，\(\kappa_{irreversible}\) 为不可逆后果权重。

### Eq-Friction-Comp: Computational Ontological Friction
$$
\Psi_f^{comp}=\lambda_1 C_{energy}+\lambda_2 C_{latency}^{irr}+\lambda_3 C_{resource-loss}
$$
用于在推断环路中引入不可逆成本近似。

### Eq-Crisis-04: Hallucination Pressure
$$
\mathcal{H}_{pressure}\propto \frac{\mathcal{C}_{gen}}{\Psi_f^{comp}+\epsilon}\cdot(1-\mathcal{V}_{physics})
$$
其中 \(\mathcal{V}_{physics}\) 为物理一致性验证强度。

## 【理论边界/防误用声明】
- 不采纳“提高 \(\Psi_f^{comp}\) 必然提升真实性”的推论。
- 边界：必须与外部可验证约束 \(\mathcal{V}_{physics}\) 联合优化。


### Eq-Phantom-01b: Collective Phantom Operator Effect
$$
\mathrm{Pain}_{social}(A,B) \approx \bar{w}_{AB}(t)\cdot \left\|\hat{G}_{A}^{target(B)}-\hat{G}_{B}\right\|
$$
其中 \(\hat{G}_{A}^{target(B)}\) 为群体A对群体B的内部投影算子。

### Eq-Polar-01: Dysrecognition Feedback Gain
$$
\frac{d\bar{w}_{AB}}{dt}=\eta\,\mathrm{Pain}_{social}-\mu\,\mathrm{SharedL1Action}
$$
共享物理行动（\(\mathrm{SharedL1Action}\)）作为负反馈抑制项。

### Eq-Polar-02: Critical Mass for Network Fracture
$$
\mathcal{M}_{crit}=\inf\left\{t:\;\bar{w}_{in}/\bar{w}_{out}>\theta_f\;\wedge\;\mathcal{C}_{bridge}<\kappa\right\}
$$
当群内/群外权重比越过阈值且桥接连通度低于下限，系统进入断裂临界区。

## 【理论边界/防误用声明】
- 不采纳“高冲突指标可直接推出社会系统不可逆崩溃”的推论。
- 边界：需结合干预变量（桥接、共同任务、制度缓冲）做动态评估。


### Eq-DCH-01: Dynamics-to-Computation Mapping
$$
\Phi:\;\mathcal{D}(x_t,\theta)\rightarrow \mathcal{M}(u_t\mapsto y_t)
$$
其中 \(\mathcal{D}\) 为真实动力系统，\(\mathcal{M}\) 为抽象计算模型。

### Eq-DCH-02: Computational Fidelity
$$
\mathcal{F}_{comp}=1-\mathbb{E}\big[d\big(y_t^{\mathcal{D}},y_t^{\mathcal{M}}\big)\big]
$$
\(\mathcal{F}_{comp}\) 评估映射后任务保真度。

### Eq-CNCM-01: Natural-System Task Capacity
$$
\mathcal{C}_{task}(\mathcal{D})=\sum_k \mathbb{1}[\mathcal{F}_{comp}^{(k)} > \tau_k]\cdot w_k
$$
表示系统在给定阈值下可实现的任务容量。

## 【理论边界/防误用声明】
- 不采纳“存在映射即存在通用计算能力”的推论。
- 边界：映射有效性需逐任务验证，且受噪声与可控性限制。


### Eq-PC-01: Predictionist Collapse Pressure
$$
\mathrm{PC}=\frac{\mathcal{P}_{fit}\cdot \mathcal{A}_{authority}}{\mathcal{E}_{falsifiable}+\epsilon}
$$
其中 \(\mathcal{P}_{fit}\) 为拟合崇拜强度，\(\mathcal{A}_{authority}\) 为权威放大，\(\mathcal{E}_{falsifiable}\) 为可证伪证据密度。

### Eq-ECG-01: Explanatory Creativity Gap
$$
\mathrm{ECG}=\mathcal{C}_{prediction}-\mathcal{C}_{explanation}
$$
ECG 越高，表示“预测能力增长”与“解释能力增长”脱钩越明显。

## 【理论边界/防误用声明】
- 不采纳“ECG 高即可断言系统无任何创新潜力”的推论。
- 边界：ECG 是阶段性诊断量，需动态追踪。
