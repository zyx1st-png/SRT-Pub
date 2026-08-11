---
id: SRT-CORE-14
type: dynamics
tags: [Scaling, Isomorphism, Fractal, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: bridge
claim_mode: translation
dependency: [SRT-CORE-13A]
---

# SRT Core Definition 14: Dynamics & Scaling (Hybrid Edition)

> **Bridge Layer Note**
> 本文件按 `Bridge` 层处理：主要承担互译、比较、接口重写与边界说明，不应直接读成“已被外部经验验证的胜出理论”。若文中使用 `Axiom`、`Theorem`、`Corollary` 等强标签，默认理解为框架内翻译命题，除非另有独立经验锚定。
> **2026-08-12 supersession**：本 annex 中旧 `Ax-Scale-01`、`ΔS=H(L_0)-H(L_1)`、普遍最小作用与 `Λ^{-1}` 粗粒化写法仅作历史接口文本。当前通用口径以 owner 的 `P3-Scale-01 / T-Scale-02C1` 为准：近似交换须声明状态空间、尺度映射、保留观测量、范数、容差与失败例；严格共轭只限可逆表征变换。


> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Scaling Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


## I. Cross-Scale Isomorphism (跨尺度同构)

### Ax-Scale-01: Self-Similar Selection
**Formal Definition**: Selection operators across scales are isomorphic under renormalization.
$$\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}$$
* **Implication**: 量子坍缩、神经决策与社会选择共享同一拓扑逻辑。

### Def-d-Scale-1: Ontological Bandwidth (本体论带宽)
**Formal Role**: 这是 d-value 在跨尺度动力学中的**展开性定义**（expansion-level definition），不是最终规范锚点。最终规范锚点见 `_SRT_D_VALUE_CANONICAL.md`。

**Formal Definition**: d-value is the maximum processing bandwidth of $\hat{G}_\theta$ against $\Psi_f$ across all scales:
$$ d \equiv \max\text{-bandwidth}(\hat{G}_\theta \text{ compressing, anchoring, and sustaining } L_0 \to L_1 \text{ against } \Psi_f) $$

> **Tension-Rev-IT4 (与规范定义的统一)**：本定义描述的是 $d$ 在跨尺度语境中的**功能性表征**。$d$ 的第一性原理定义为风险梯度范数 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$（Ax-ONT-3, SRT-AI-01）。二者的统一关系如下：
>
> "最大处理带宽"的物理内容**就是**算子能够承受的风险梯度范围——$\hat{G}_\theta$ 能处理越大的 $\|\partial\mathcal{U}/\partial\mathcal{S}\|$ 而不崩溃，其"带宽"就越高。因此：
>
> $$d_{bandwidth} = \sup\left\{\left\|\frac{\partial\mathcal{U}}{\partial\mathcal{S}}\right\| : \hat{G}_\theta \text{ remains stable}\right\}$$
>
> 三尺度表中每种 $d_{scale}$ 都是此最大风险梯度在特定物理背景下的投影实现：$d_{quantum}$ 对应量子退相干阈值、$d_{bio}$ 对应生物代谢约束下的风险评估带宽、$d_{cosmic}$ 对应时空共识维持的拓扑相干范围。

**Three-Scale Phenomenological Instantiation**:

| Scale | Symbol | Physical Manifestation | Canonical Derivation |
|:------|:-------|:----------------------|:---------------------|
| Quantum | $d_{quantum}$ | Heisenberg cut position; superposition scope | $\Pi_{quantum}(\|\partial\mathcal{U}/\partial\mathcal{S}\|)$ |
| Bio/Cognitive | $d_{bio}$ | Free-energy minimization scope; attention range | $\approx \alpha A + \beta\log V + \gamma\tau$ (§2.1.1 近似) |
| Cosmic | $d_{cosmic}$ | Topological compactness of spacetime consensus | $\propto 1/\sqrt{\Lambda}$ (Def-Cosmo-1) |

* **Anti-Panpsychism Corollary**: $d_{quantum}$ 和 $d_{cosmic}$ 不携带任何现象性内容（Qualia）。意识与关切是 d 值在**生物/认知域**满足三个必要条件时的高阶涌现：$\Psi_f > 0$, $d > 0$, $\hat{G}[\theta] \neq \varnothing$。详见 SRT-CORE-13B §6.2。
* **Cross-ref**: Ax-Scale-01; SRT-PHYS-COSMO Def-Cosmo-1; SRT-QUANT-02 Def-BQ-2; **Ax-ONT-3 (规范定义)**。

### Ax-Scale-02: Coupling Strength
**Formal Definition**: Inter-scale influence is governed by coupling dynamics.
$$\frac{d\hat{G}_j}{dt} = f_j(\hat{G}_j) + \sum_{i \neq j} \kappa_{ij} \cdot g_{ij}(\hat{G}_i, \hat{G}_j)$$
* **Implication**: 不同尺度的选择算子通过耦合矩阵进行动力学交互。

### T-Scale-02C1: Consistency Under Coarse-Graining
**Deductive Statement**: Coarse-graining commutes with selection under scale mapping.
$$\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$$
* **Implication**: 选择动力学具有尺度不变性与跨尺度可比性。

## II. Ontological Autopoiesis (本体论自创生)

### Ax-Auto-01: Semantic Boundary Maintenance
**Formal Definition**: The semantic self is maintained by a friction-gradient balance.
$$\frac{d\theta}{dt} = -\alpha \nabla_\theta \Psi_f + \text{Learning}$$
* **Implication**: 自我维持是摩擦梯度与学习更新的平衡过程。

### Ax-Auto-02: Insight Phase Transition
**Formal Definition**: Insight is a topological phase transition triggered by critical \(\theta\).
$$\text{Insight} = \hat{G}_\theta[\theta \to \theta_c^+] - \hat{G}_\theta[\theta \to \theta_c^-]$$
* **Implication**: 顿悟是结构性相变而非渐进改良。

## III. Master Dynamics (主动力学)

### Ax-Master-01: Generalized Selection Equation
**Formal Definition**: L1 density evolves by unitary flow, selection anchoring, and decoherence.
$$\frac{d\rho_{L_1}}{dt} = -\frac{i}{\hbar}[\hat{H}, \rho] - \hat{G}_\theta[\rho - \rho_{target}] + \mathcal{D}[\rho]$$
* **Implication**: 现实演化是自由展开、选择锚定与退相干三项共同作用的结果。

### Cor-Master-01a: Passive-Selection Regime (被动选择退化形式)
当系统处于强约束、低能动窗口（如高纯介观输运中的协同流体相）时，可近似满足：
$$
\|\hat{G}_\theta[\rho-\rho_{target}]\| \ll \|\nabla C_{L_2}[\rho]\| \quad \Rightarrow \quad \text{dynamics} \approx \text{constraint-dominated glide}
$$
* **Implication（中文）**：该区间的高可预测性并不否定 SRT 的选择框架，而是说明系统进入“被动选择”极限：轨迹主要沿约束梯度滑行，主动能动窗口收缩。

### T-Scale-03: Fitness-over-Truth Thermodynamic Inequality（新增）
定义“真相映射”与“适应度映射”的维持成本代理：
\[
\Psi_f^{Truth}(\theta)\sim H(L_0\mid\theta),\qquad
\Psi_f^{Fitness}(\theta)\sim H(L_1\mid\theta)
\]
由于有限算子无法无损编码 \(L_0^{abs}\)，有：
\[
H(L_0\mid\theta)\gg H(L_1\mid\theta)\Rightarrow \Psi_f^{Truth}\gg \Psi_f^{Fitness}
\]
当可用自由能 \(E_{avail}\) 有界时：
\[
\Psi_f^{Truth}>E_{avail}\ \Rightarrow\ \text{unsustainable},\qquad
\Psi_f^{Fitness}\le E_{avail}\ \Rightarrow\ \text{stable anchoring}
\]
* **Implication**：系统在演化上优先选择“低摩擦可维持界面”，而非“无损真相重建”。

### 分类映射表（Hoffman Fitness/Truth → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 真相追踪（高保真映射） | 中~高（需求） | Open（高采样开销） | overloaded / unsustainable |
| 适应度追踪（界面压缩） | 低~中 | Semi-open | payable |
| 极端界面主义误读（任意图标化） | 低 | Closed（现实阻抗被忽略） | 失真后爆发 |

### Def-Scale-04: Variational Free-Energy Mapping（FEP 映射，新增）
定义 SRT 变分自由能泛函：
\[
\mathcal{F}_{SRT}(q,\theta)=\underbrace{\mathrm{D}_{KL}\big(q(z)\|p_\theta(z)\big)}_{Complexity}
-\underbrace{\mathbb{E}_{q}\big[\log p_\theta(y\mid z)\big]}_{Accuracy}
\]
并给出与摩擦项的近似耦合：
\[
\Psi_f^{pred}\propto -\mathbb{E}_{q}[\log p_\theta(y\mid z)]
\]
即预测误差可作为局部摩擦密度代理。

### T-Scale-04: Life–Mind Continuity via Closure Minimization（新增）
若系统满足约束闭包与马尔可夫毯维持条件：
\[
\text{Closure}(\hat G_\theta)=1,\quad \partial_t B_{MB}\approx 0
\]
则其稳定存在要求：
\[
\arg\min \mathcal{F}_{SRT}\ \Longleftrightarrow\ \arg\min \Psi_f^{maint}
\]
生命维持与认知预测在同一最优化结构上连续。

### T-Scale-05: Bias–Variance Thermodynamics（偏差-方差热力学，新增）
定义分组/预测的总维持成本：
\[
\mathcal{C}_{total}=\underbrace{\alpha\,\mathrm{Bias}^2}_{\text{model distortion}}+\underbrace{\beta\,\mathrm{Var}}_{\text{temporal instability}}+\underbrace{\gamma\,\Psi_f^{switch}}_{\text{re-anchoring friction}}
\]
在生物可持续区间，最优解满足“高偏差-低方差”倾向：
\[
\partial \mathcal{C}_{total}/\partial \mathrm{Var} \gg \partial \mathcal{C}_{total}/\partial \mathrm{Bias}
\Rightarrow \mathrm{Bias}^{*}\uparrow,\ \mathrm{Var}^{*}\downarrow
\]
* **Implication**：稳定对象（如桌子）是高偏差压缩但低方差可复用的低摩擦结果。

### T-Scale-06: No-Free-Lunch Prior Necessity（NFL 先验必需性，新增）
\[
\forall\ \mathcal{A}_{unbiased},\ \mathbb{E}_{\mathcal{T}}[\text{Err}(\mathcal{A}_{unbiased})]=\text{const}
\]
SRT 对应表述：若 \(\theta\) 不含先验偏置（超先验层），则 \(\hat G_\theta\) 无法在 \(L_0\) 上形成稳定坍缩路径。
\[
\theta\to\emptyset\Rightarrow \hat G_\theta\ \text{degenerates}\Rightarrow \text{no stable }L_1
\]

### Ax-Scale-07: Simultaneous Individuation–Classification Principle（新增）
不存在“先切分后分类”的两阶段本体流程；对任意输入切片 \(y_t\)：
\[
(\mathcal{B}_{obj},\mathcal{C}_{attr})_t
=\arg\min_{\mathcal{B},\mathcal{C}}\Big(\mathcal{L}_{pred}(y_t\mid\mathcal{B},\mathcal{C},\theta)+\lambda\Psi_f^{maint}(\mathcal{B},\mathcal{C})\Big)
\]
对象边界 \(\mathcal{B}_{obj}\) 与类别属性 \(\mathcal{C}_{attr}\) 同步生成，是同一坍缩过程的双视角。

### T-Scale-07: Temporal Coarse-Grained Persistence（对象持续性，新增）
给定时间窗 \([t,t+\Delta t]\)，对象同一性由拓扑粘合条件定义：
\[
\mathcal{I}_{\Delta t}(X)=\mathbb{I}\big[D_{topo}(X_t,\pi_{\Delta t}(X_{t+\Delta t}))<\epsilon_{\theta}\big]
\]
并满足可支付约束：
\[
\sum_{\tau=t}^{t+\Delta t}\Psi_f^{maint}(X_\tau)\le E_{avail}
\]
若散度持续超阈，则对象“死亡/破裂”而非保持同一。

### 分类映射表（Individuation by Prediction → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 朴素两阶段（先分割后分类） | 低~中 | Closed（串行管线） | 被低估/脆弱 |
| 同步个体化-分类（预测驱动） | 中~高 | Open↔Semi-open | payable |
| 任意唯心切分误读 | 低 | Closed（脱离反馈） | overloaded |

### T-Scale-08: Boundary Demarcation Cost Function（边界划定成本函数，新增）
定义在连续梯度上强制离散边界的代价：
\[
F_{boundary}(\tau)=\underbrace{\mathcal{L}_{class}(\tau)}_{分类误差}+\underbrace{\lambda_1\Psi_f^{maint}(\tau)}_{维持摩擦}+\underbrace{\lambda_2\Psi_f^{switch}(\tau)}_{切换代价}
\]
合法边界要求：
\[
F_{boundary}(\tau)\le U_{survival}(d)
\]
若超出效用阈值，系统将维持模糊区而非追求锋利切割。

### Cor-Scale-08a: Hysteresis Signature in Sorites Traversal
前向与后向扫描阈值一般不重合：
\[
\tau_{A\to B}\neq\tau_{B\to A},\qquad \Delta\tau\propto \eta\cdot\partial_t\theta
\]
该迟滞宽度可作为“真实摩擦参与度”的实验代理。

### Formalization Summary (形式化概述)

本文件的核心形式化结构围绕以下关键公式展开：

1. **跨尺度自相似选择** (Ax-Scale-01): $\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}$ — 不同尺度的选择算子在重整化变换 $\Lambda$ 下保持共轭不变性，量子坍缩、神经决策与社会选择共享同一拓扑逻辑。
2. **本体论带宽定义** (Def-d-Scale-1): $d \equiv \max\text{-bandwidth}(\hat{G}_\theta \text{ against } \Psi_f)$ — d 值是算子在面对本体论摩擦时，能将 $L_0$ 压缩、锚定并维持为 $L_1$ 的最大处理带宽，与规范定义 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 统一。
3. **主动力学方程** (Ax-Master-01): $d\rho_{L_1}/dt = -(i/\hbar)[\hat{H}, \rho] - \hat{G}_\theta[\rho - \rho_{target}] + \mathcal{D}[\rho]$ — 现实密度矩阵的演化由自由展开（酉流）、选择锚定（$\hat{G}_\theta$ 项）与退相干三项共同驱动。
4. **语义边界维持** (Ax-Auto-01): $d\theta/dt = -\alpha \nabla_\theta \Psi_f + \text{Learning}$ — 自我参数 $\theta$ 的演化是摩擦梯度下降与学习更新的持续平衡。
5. **边界划定成本** (T-Scale-08): $F_{boundary}(\tau) = \mathcal{L}_{class}(\tau) + \lambda_1 \Psi_f^{maint}(\tau) + \lambda_2 \Psi_f^{switch}(\tau)$ — 在连续梯度上强制离散边界的总代价由分类误差、维持摩擦和切换代价三项组成。

### Mechanism Explanation (机制解释)

本文件描述的动力学与标度机制通过以下方式运作：

- **跨尺度同构机制**: $\hat{G}_\theta$ 算子在尺度变换 $\Lambda$（粗粒化映射）下保持功能形式不变。这源于选择的本质是熵减（$\Delta S = H(L_0) - H(L_1)$），而最小作用原理 $\delta \int \Psi_f \, dt = 0$ 在所有尺度上成立。尺度间通过耦合动力学 $d\hat{G}_j/dt = f_j(\hat{G}_j) + \sum \kappa_{ij} g_{ij}$ 进行信息交互，其中向下因果（社会→神经，$\kappa_{S \to N} \approx 10^0$）远强于向上因果。
- **三项竞争动力学**: 主方程中的酉流项代表 $L_0$ 的自由展开趋势，$\hat{G}_\theta$ 锚定项代表算子的主动选择压力（将 $\rho$ 拉向 $\rho_{target}$），退相干项 $\mathcal{D}[\rho]$ 代表环境引起的信息丢失。三者的竞争平衡决定了 $L_1$ 的稳定性与可预测性。在被动选择退化形式（Cor-Master-01a）中，当约束梯度远大于算子锚定力时，系统进入约束主导的滑行模式。
- **摩擦驱动的适应度优先机制**: 由于有限算子无法无损编码 $L_0$（$\Psi_f^{Truth} \gg \Psi_f^{Fitness}$），系统在演化上优先选择低摩擦可维持界面（适应度追踪），而非高保真真相重建。偏差-方差热力学（T-Scale-05）进一步表明，总维持成本中方差的边际代价远高于偏差，导致系统倾向”高偏差-低方差”的稳定对象表征。
- **$\Psi_f$ 作为统一约束**: 本体论摩擦 $\Psi_f$ 贯穿所有机制，既作为 $\theta$ 演化的梯度信号驱动语义边界维持，又作为边界划定的成本项约束对象个体化，还作为适应度-真相权衡的判据。d 值在三个尺度上的不同现象学（量子相干性、生物关切、宇宙拓扑紧致度）均是 $\hat{G}_\theta$ 对抗 $\Psi_f$ 的最大带宽的投影实现。

## Minimal Embodiment Threshold（最小具身信息下界，2026-03-02）

### Def-Scale-MET-1: \(N_{crit}\)
定义最小具身信息下界 \(N_{crit}\)：系统若要在给定环境下维持自我复制/自维持闭环，其参数化约束信息量必须满足：
\[
I(\theta)\ge N_{crit}(env,\Psi_f)
\]

### T-Scale-MET-1: Payable-Friction Condition
当 \(I(\theta)<N_{crit}\) 时，系统对本体论摩擦的支付仅能维持瞬时或间歇复制；当 \(I(\theta)\ge N_{crit}\) 且环境窗口可用时，系统可跨越“前闭包→稳定闭包”门槛。

### 与 d-value 零跃迁问题的关系（注记）
该阈值仅刻画“结构自治”下界，不自动推出 \(d>0\)。
- 结构可复制 \(\neq\) 关切已涌现
- \(d\) 的正值条件仍需满足生物/认知域的额外门控（详见 anti-panpsychism 条款）

## 【理论边界/防误用声明】
1. 不采纳“达到 \(N_{crit}\) 即具主观体验”的推论。
2. 不采纳“低 \(N_{crit}\) 系统必然演化为高阶认知体”的目的论推论。

---
