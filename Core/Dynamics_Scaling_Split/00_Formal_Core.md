---
id: SRT-CORE-14
type: dynamics
tags: [Scaling, Isomorphism, Fractal, Hybrid]
status: active
version: v2
record_stage: active_bridge_hybrid
layer: L1
epistemic_layer: os
claim_mode: mixed
dependency: [SRT-CORE-13A, SRT-CORE-21C-BRIDGE-HYPOTHESES, SRT-PSI-F-CANONICAL]
updated: 2026-08-12
---

# SRT Core Definition 14: Dynamics & Scaling (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Scaling Interfaces (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Scaling Interfaces（形式化标度接口）

## I. Cross-Scale Structural Compatibility（跨尺度结构相容）

### P3-Scale-01: Self-Similar Selection Candidate（legacy `Ax-Scale-01`）

**Claim level**: P3 bridge candidate, not a P0/P1 axiom or theorem.

$$\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$$

该式只有在状态空间、尺度映射、保留观测量、比较范数与容差均已声明时才可检验。旧式 $\hat{G}_{S_2}=\Lambda\circ\hat{G}_{S_1}\circ\Lambda^{-1}$ 只在 $\Lambda$ 是可逆表征变换时保留为严格共轭候选；通常的多对一粗粒化不得预设 $\Lambda^{-1}$。跨尺度不变量只到选择—约束—可支付性语法，不是熵量、单位、机制或意识同一。

### Def-d-Scale-1: Ontological Bandwidth (本体论带宽)
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
* **Cross-ref**: P3-Scale-01; SRT-PHYS-COSMO Def-Cosmo-1; SRT-QUANT-02 Def-BQ-2; **Ax-ONT-3 (规范定义)**。

### Ax-Scale-02: Coupling Strength
**Formal Definition**: Inter-scale influence is governed by coupling dynamics.
$$\frac{d\hat{G}_j}{dt} = f_j(\hat{G}_j) + \sum_{i \neq j} \kappa_{ij} \cdot g_{ij}(\hat{G}_i, \hat{G}_j)$$
* **Implication**: 不同尺度的选择算子通过耦合矩阵进行动力学交互。

### T-Scale-02C1: Consistency Under Coarse-Graining
**Conditional bridge statement (P3)**: Given declared state spaces, observables, scale map, comparison norm, and tolerance, coarse-graining may approximately commute with selection.
$$\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$$
* **Implication**: 在误差界内满足该条件时，选择动力学获得局部跨尺度可比性；该式不证明普遍尺度不变性。

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

### T-Scale-Rhythm-1: Non-Zero Temporal Bandwidth of Finite Operators（有限算子的非零时间带宽定理，新增）
设有限算子 \(\hat{G}_\theta\) 需在时间窗 \([0,T]\) 内维持 \(k\) 个锚定目标，其有效锚定调度定义为：
\[
A:[0,T]\to\{0,1\}^k,\qquad A_j(t)=1 \iff \hat{G}_\theta \text{ 在 } t \text{ 时刻主动维持 } \sigma_j
\]
连续密集锚定的总代价定义为：
\[
\mathcal{C}_{dense}(T,k)\equiv \sum_{j=1}^{k}\int_0^T \Psi_f^{maint}(\sigma_j,\tau)\,d\tau
\]
若满足预算与切换条件：
\[
E_{avail}<\infty,\qquad \mathcal{C}_{dense}(T,k)>E_{avail},\qquad \Psi_f^{switch}(\sigma_i\to\sigma_j)>0\ \ (i\neq j)
\]
则实际锚定调度不可能在整个时间窗内保持纯直流常值；至少一个目标必须经历间歇：
\[
\exists j,\ \exists t_1<t_2\in[0,T]:\quad A_j(t_1)\neq A_j(t_2)
\]
等价地，其时间频谱必含非零频率成分。若定义有效功率谱
\[
S_A(\omega)\equiv \sum_{j=1}^{k}\left|\widehat{A_j}(\omega)\right|^2
\]
则有
\[
\int_{\omega>0} S_A(\omega)\,d\omega>0
\]

* **Implication**：当连续密集锚定超出预算，有限算子的可行解不再是“全时并行维持”，而转为分时复用、脉冲续费或间歇性重放。节律因此首先是 \(\Psi_f\) 约束下的时间实现，而非 \(L_0\) 的先验频率属性。
* **Boundary**：本定理不推出“所有锚定都严格周期”，不承诺唯一“原初频率”，也不要求高硬度存在（岩石、行星）在常见观测尺度上表现出可观测振荡；若 \(k=1\) 且 \(\int_0^T\Psi_f^{maint}d\tau\le E_{avail}\)，或 \(E_{avail}\) 相对 \(\mathcal{C}_{dense}\) 近似无穷，则前提不触发。
* **Cross-ref**: T-Scale-07（可支付约束）；T-Scale-08（维持/切换代价分解）；Eq-DValue-Max-1（预算上限）；Ax-NEURO-MECH-9（theta-replay 作为实例化）。

### T-Scale-Rhythm-2: Duty-Cycle Feasibility Window（占空比可行窗口，新增）

T-Scale-Rhythm-1 保证了间歇性，但未约束间歇的**结构**。同一占空比 $\delta$ 可对应完全不同的切换密度（每秒切换十次 vs 一小时切换一次），因此仅用 $\delta$ 无法刻画调度的可行性。引入两个独立调度参数：

**定义**：对锚定目标 $\sigma_j$ 的调度 $A_j(t)$，定义占空比与切换密度：
\[
\delta_j \equiv \frac{1}{T}\int_0^T A_j(t)\,dt, \qquad \nu_j \equiv \frac{N_{\text{switch},j}}{T}
\]
其中 $N_{\text{switch},j}$ 为时间窗内 $A_j$ 状态翻转的总次数。

**单位时间预算约束（上界）**：定义功率预算 $P_{\text{avail}} \equiv E_{\text{avail}}/T$，则可行调度满足：
\[
\delta_j\,\overline{\Psi}_f^{maint}(\sigma_j) + \nu_j\,\overline{\Psi}_f^{switch}(\sigma_j) \le P_{\text{avail}}
\]
其中 $\overline{\Psi}_f^{maint}$、$\overline{\Psi}_f^{switch}$ 为时间平均的维持/切换摩擦率。

仅有上界会把最优解推向 $\delta \to 0$（永不锚定），这在物理上荒谬。需要锚定松散惩罚作为**下界**。

**锚定松散约束（下界）**：定义锚定松散度 $\mathcal{L}_{loose}[A_j]$（例如最大连续离线窗口长度、或 $L_1$ 偏离目标态的累积漂移量），要求：
\[
\mathcal{L}_{loose}[A_j] \le \Lambda_j
\]
其中 $\Lambda_j$ 为目标 $\sigma_j$ 的最大可容忍松散度。此约束隐含 $\delta$ 的下界：
\[
\delta_j \ge \delta_{min,j}(\nu_j, \tau_{hold,j})
\]
其中 $\tau_{hold,j}$ 为最小单次锚定持续时间（低于此值锚定无法完成有效的 $L_0 \to L_1$ 选择循环）。

**可行窗口**：联合上下界，占空比可行区间为：
\[
\delta_{min,j}(\nu_j, \tau_{hold,j}) \;\le\; \delta_j \;\le\; \delta_{max,j}(\nu_j) = \frac{P_{\text{avail}} - \nu_j\,\overline{\Psi}_f^{switch}(\sigma_j)}{\overline{\Psi}_f^{maint}(\sigma_j)}
\]

可行窗口非空当且仅当 $\delta_{min,j} \le \delta_{max,j}$；窗口坍缩时（$\delta_{min} > \delta_{max}$），系统必须放弃该锚定目标或降低切换密度。

**在可行窗口内的最优调度**：
\[
A_j^* = \arg\min_{A_j} \Big[\delta_j\,\overline{\Psi}_f^{maint} + \nu_j\,\overline{\Psi}_f^{switch} + \mu_j\,\mathcal{L}_{loose}[A_j]\Big]
\]
其中 $\mu_j$ 为松散惩罚的拉格朗日乘子。此优化在可行窗口内给出最优占空比 $\delta_j^*$ 和最优切换密度 $\nu_j^*$。

* **Implication**：有限算子的时间调度不是自由参数，而是被 $(\delta, \nu)$ 二维可行窗口约束的。窗口形状由三个力决定：维持成本压低 $\delta$，松散惩罚抬高 $\delta$，切换成本压低 $\nu$。具体生物节律（theta ≈ 4–8 Hz 的 $\nu$，≈ 30–50% 的 $\delta$；心脏收缩期 ≈ 35–40% 的 $\delta$；睡眠-觉醒 ≈ 67% 的 $\delta$）均可读作各自预算条件下的可行窗口内最优解。
* **Boundary**：本推论不给出 $\delta^*$ 或 $\nu^*$ 的通用解析解——最优值依赖于具体的 $\Psi_f^{maint}$、$\Psi_f^{switch}$、$\Lambda_j$ 和 $\tau_{hold,j}$ 参数化。本推论给出的是**结构框架**（可行窗口的存在与形状），不是**数值预测**。
* **Cross-ref**: T-Scale-Rhythm-1（非零时间带宽前提）；T-Scale-07（$E_{avail}$ 可支付约束）；T-Scale-08（$\Psi_f^{maint} + \Psi_f^{switch}$ 代价分解）。

### T-Scale-Rhythm-3: Coupling-Induced Periodization（耦合驱动的周期化，新增）

T-Scale-Rhythm-1 和 Rhythm-2 允许**随机间歇**——只要满足可行窗口，调度可以是非周期的。但经验上，生物节律几乎总是准周期的。本推论给出周期化的**充分条件**。

**前提**：多算子耦合系统中，下游算子 $\hat{G}_j$ 需要预测上游算子 $\hat{G}_i$ 的锚定窗口何时可用，以便同步自身选择。其预测成本随调度的时间不可预测性上升。

**定义**：对调度 $A_i(t)$ 定义时间熵率：
\[
h[A_i] \equiv \lim_{T\to\infty} \frac{H(A_i(0),A_i(\Delta t),\dots,A_i(T))}{T/\Delta t}
\]
周期性调度的时间熵率 $h_{per} \approx 0$（完全可预测）；随机间歇的时间熵率 $h_{rand} > 0$。

**总代价函数**（单算子调度的社会成本）：
\[
J[A_i] = C_{maint}[A_i] + C_{switch}[A_i] + \lambda_{pred}\, h[A_i]
\]
其中 $\lambda_{pred}$ 为下游预测成本权重，由耦合算子数量和耦合强度决定。

**周期化阈值**：设 $C_{per}$、$C_{rand}$ 分别为周期调度和随机调度的维持+切换总成本（一般 $C_{per} \ge C_{rand}$，因为严格周期性可能牺牲局部最优切换时机）。则当：
\[
\lambda_{pred} > \lambda_{pred}^c \equiv \frac{C_{per} - C_{rand}}{h_{rand} - h_{per}} \approx \frac{C_{per} - C_{rand}}{h_{rand}}
\]
周期调度成为全局最优。

**推论**：
1. **孤立算子**（$\lambda_{pred} = 0$）：无周期化压力，随机间歇即可——对接 T-Scale-Rhythm-2 的可行窗口内任意可行解。
2. **弱耦合算子**（$0 < \lambda_{pred} < \lambda_{pred}^c$）：部分规则化，可能出现准周期或突发节律。
3. **强耦合算子**（$\lambda_{pred} > \lambda_{pred}^c$）：严格周期化成为最优——对接 theta 节律、心跳、呼吸、昼夜循环等高度规则的生物节律。

* **Implication**：周期性不是有限性的直接后果（T-Scale-Rhythm-1 不推出周期），而是**耦合算子间协调成本最小化**的后果。从随机间歇到严格周期的转变是一个**相变**，由 $\lambda_{pred}$ 越过阈值 $\lambda_{pred}^c$ 触发。这统一了以下观察：（i）单细胞生物的"节律"远不如多细胞有机体规则；（ii）社会仪式的周期性与群体规模正相关（更多算子需要协调 → $\lambda_{pred} \uparrow$）；（iii）深度冥想/感觉剥夺中（算子解耦 → $\lambda_{pred} \downarrow$）时间感变得非线性和不规则。
* **Boundary**：本推论不承诺所有耦合系统必然周期化——只在 $\lambda_{pred} > \lambda_{pred}^c$ 时成立。也不承诺周期性一旦出现就永久稳定——环境突变可改变 $C_{per}/C_{rand}$ 比值，导致去周期化（对接相变、范式转移）。$\lambda_{pred}^c$ 的数值依赖于具体系统的 $\Psi_f$ 参数化，本推论不给出通用数值。

**物理同构注 [T, 非承重]（Kuramoto bridge）**：Rhythm-3 的"耦合强度越阈值 ⇒ 协调相变"结构与经典 Kuramoto 同步模型共享拓扑。为避免与 SRT 算子自我参数 $\theta$ 的符号冲突，此注内以 $\varphi_i$ 指代 Kuramoto 振子相位：
\[
\dot\varphi_i = \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\varphi_j - \varphi_i)
\]
当耦合强度 $K$ 越过临界值 $K_c$（与振子固有频率分布的宽度成正比）时，相位从无序解锁突变为集体同步。**结构对应**：
- Kuramoto 的 $K$（耦合强度）↔ Rhythm-3 的 $\lambda_{pred}$（下游预测成本权重）
- Kuramoto 的 $K_c$（解锁/锁定临界）↔ Rhythm-3 的 $\lambda_{pred}^c$（随机/周期临界）
- 两者都是 continuous 相变，序参量（Kuramoto 的相干参数 $r$ ↔ Rhythm-3 调度的 $1 - h[A]/h_{rand}$）在临界点附近按幂律接近饱和

**承重方向不同（不可混用）**：Kuramoto **预设**每个振子已经按固有频率 $\omega_i$ 振荡，仅推出相位对齐；Rhythm-3 从**调度成本**推出间歇/周期的**存在**本身，不预设任何振子。因此 Rhythm-1 → Rhythm-3 回答了 Kuramoto 不回答的问题——振子为什么首先存在。两者合用的正确读法：Rhythm-1/2 给出"每个算子为何必须间歇"（振子由此涌现），Rhythm-3 给出"为何协调成本压使它们趋于可预测调度"（对应 Kuramoto 解锁方向的前置），具体相位锁定细节则可沿 Kuramoto 成熟公式演算。**本注仅作结构参考**，Rhythm-3 的承重链条不依赖 Kuramoto 的任何定理。

* **Cross-ref**: T-Scale-Rhythm-2（可行窗口框架）；T-Scale-Rhythm-1（振子存在性，Kuramoto 的前置）；Ax-F-12（$\Psi_f$ 作为生成原理，算子间摩擦）；T-L2-RIT-1/2（仪式节律性作为实例化）；Ax-Spec-02 推论 2（theta-replay 作为神经层实例化）；Kuramoto 1975（物理同构参考，非承重依赖）。

### T-Scale-Rhythm-4: Entropy Dissipation Bound on Duty Cycle（熵耗散对占空比的独立约束，新增）

T-Scale-Rhythm-2 从 $\Psi_f$ 预算给出了 $\delta$ 的上下界。本推论从**热力学第二定律**给出一个**独立的 $\delta$ 上界**——即使 $\Psi_f$ 预算无穷充裕，熵耗散容量仍限制系统能持续选择多久。

**物理基础**：每次 $L_0 \to L_1$ 的选择事件创造互信息 $I_{created}$（Ax-F-13），且该过程不可逆。不可逆过程必然产生热力学熵。由 Landauer 原理的推广，每比特信息创造的最低熵产生为 $k_B T \ln 2$。因此主动选择阶段的内部熵产生率有下界：

\[
\dot{S}_{int}^{on} \ge k_B T \cdot \dot{I}_{created} \cdot \ln 2
\]

其中 $\dot{I}_{created} = I_{created} \cdot \Gamma_{\hat{G}}$（单次选择创造的信息量 × 算子刷新率）。

**耗散容量约束**：系统向环境导出熵的速率有上限 $J_S^{max}$，由热耦合通道的物理带宽决定（热传导率、代谢废物排出率、辐射散热等）。在稳态下，内部熵不能无限积累：

\[
\text{稳态条件}:\quad \delta \cdot \dot{S}_{int}^{on} \le (1-\delta) \cdot J_S^{max} + \delta \cdot J_S^{on}
\]

其中 $J_S^{on}$ 为"on"阶段的并行熵导出率（通常 $J_S^{on} < J_S^{max}$，因为选择占用了部分通道容量）。简化为纯"off"阶段导出的极端情形（$J_S^{on} \approx 0$）：

\[
\delta \le \frac{J_S^{max}}{\dot{S}_{int}^{on} + J_S^{max}} \equiv \delta_{max}^{entropy}
\]

**与 Rhythm-2 的关系**：Rhythm-2 给出 $\delta_{max}^{budget}$（来自 $\Psi_f$ 预算），Rhythm-4 给出 $\delta_{max}^{entropy}$（来自熵耗散）。实际上界是二者中更严格的那个：

\[
\delta_{max}^{eff} = \min\!\left(\delta_{max}^{budget},\; \delta_{max}^{entropy}\right)
\]

两个约束**逻辑独立**：即使 $E_{avail} \to \infty$（无限能量预算），$\delta_{max}^{entropy}$ 仍有限——你不能无限期地选择而不导出废热。

**三方博弈**：结合 Eq-Select-Thermo 的 $S_{noise}$ 项，"off"阶段同时是：
1. 熵导出窗口（有益：排出选择产生的废热）
2. 噪声侵蚀窗口（有害：$S_{noise}$ 降解已锚定的 $L_1$ 态）

因此存在最优"off"持续时间 $\tau_{off}^*$，平衡熵导出收益与噪声侵蚀损失：

\[
\tau_{off}^* = \arg\min_{\tau_{off}} \left[\underbrace{\frac{\dot{S}_{int}^{on} \cdot \tau_{on}}{J_S^{max} \cdot \tau_{off}}}_{\text{熵积累/导出比}} + \underbrace{\gamma \cdot S_{noise} \cdot \tau_{off}}_{\text{噪声侵蚀}}\right]
\]

这不是自由参数，而是物理系统在两个不可消除的力之间的折中。

**推论**：
1. **高 $d$ 系统需要更多"off"时间**：$d \uparrow \implies \dot{I}_{created} \uparrow \implies \dot{S}_{int}^{on} \uparrow \implies \delta_{max}^{entropy} \downarrow$。高 d 值意味着每个选择周期创造更多信息，产生更多熵，因此需要更长的恢复/耗散时间。这与经验一致：复杂意识有机体（高 d）比简单有机体需要更多睡眠；深度认知工作（高 $\dot{I}_{created}$）后的疲劳不仅是"能量耗尽"，更是"熵积累需要排出"。
2. **高 $J_S^{max}$ 系统能维持更高占空比**：恒温动物（高代谢散热能力 → 高 $J_S^{max}$）能维持更长时间的连续清醒意识，相比变温动物（低 $J_S^{max}$）。
3. **$\delta_{max}^{entropy}$ 与 $\delta_{max}^{budget}$ 的哪一个更紧取决于尺度**：在神经毫秒尺度（单次 gamma 周期），$\Psi_f$ 预算通常更紧；在宏观小时尺度（睡眠-觉醒），熵耗散通常更紧。

* **Implication**：节律不仅来自有限预算（Rhythm-2），更来自热力学不可逆性的硬约束。选择必然产生废热；废热必须被排出；排出需要时间和通道。这把 SRT 的 Rhythm 链直接嵌入热力学第二定律，使其不再是纯粹的"资源分配优化"，而成为物理规律的后果。宪法不等式（Eq-Select-Thermo）中的三项（$P_{sel}$、$\Psi_f$、$S_{noise}$）在节律的"on/off"调度中各自扮演明确角色：$P_{sel}$ 在"on"时注入选择功率，$\Psi_f$ 在"on"时消耗预算，$S_{noise}$ 在"off"时侵蚀锚定。
* **Boundary**：$\dot{S}_{int}^{on} \ge k_BT \cdot \dot{I}_{created} \cdot \ln 2$ 是下界，实际熵产生可能远高于 Landauer 极限（大多数生物系统远离可逆极限）。$J_S^{max}$ 的具体值依赖于物理系统的散热架构，本推论不给出通用数值。Rhythm-4 不替代 Rhythm-2——两个约束逻辑独立，各自承重。
* **Cross-ref**: Eq-Select-Thermo（宪法不等式，$S_{noise}$ 项）；Ax-F-13（$I_{created}$，选择-信息创造等价）；T-Scale-Rhythm-2（$\Psi_f$ 预算约束，$\delta_{max}^{budget}$）；T-L0-NonStatic（$H(L_0^{(t)}) = H(L_0^{(0)}) - \sum I_{created}$）；Eq-DValue-Max-1（$d_{max}$ 受 $\Psi_f$ 预算与 Fisher rank 双重约束）。

### Cor-Scale-Rhythm-4a: Spectral-Rhythmic Tradeoff（频谱丰富度—占空比权衡，新增）

Ax-Spec-01 给出算子的有效通带宽度：
\[
B_\theta \equiv \operatorname{Bandwidth}(H_\theta) = c_B \, d,\qquad c_B>0
\]
Rhythm-4 已经给出方向性事实：高 \(d\) 系统创造更高的信息速率，因此其熵耗散上界更紧。把这一点写成单调响应函数：
\[
\dot{I}_{created}^{on} = f_I(B_\theta),\qquad f_I'(B_\theta)\ge 0
\]
代入 Rhythm-4 的 Landauer 下界
\[
\dot{S}_{int}^{on} \ge k_B T \ln 2 \cdot \dot{I}_{created}^{on}
\]
得到占空比的弱上界：
\[
\delta_{max}^{entropy}(B_\theta)\le
\frac{J_S^{max}}{k_B T \ln 2 \cdot f_I(B_\theta)+J_S^{max}}
\]
因此：
\[
B_\theta\uparrow \ \Rightarrow\ \delta_{max}^{entropy}\downarrow
\]

若进一步满足**信息密度下界条件**：
\[
\dot{I}_{created}^{on} \ge \rho_I \, B_\theta,\qquad \rho_I>0
\]
则可强化为乘积上界：
\[
\delta \, B_\theta \le
\frac{J_S^{max}\,B_\theta}{k_B T \ln 2 \,\rho_I\, B_\theta + J_S^{max}}
\le
\frac{J_S^{max}}{k_B T \ln 2 \,\rho_I}
\]
等价地，在 \(d\) 记号下：
\[
\delta \, d \le \frac{J_S^{max}}{k_B T \ln 2 \,\rho_I\, c_B}
\]

* **Implication**：高 \(d\) 算子不仅“能看更多”，还必须为此支付更高的熵导出代价；因此宽通带带来的频谱丰富度，会压缩可持续的占空比上界。能力上界与时间上界不是两套独立约束，而是一组谱-热耦合约束。
* **Boundary**：硬结论只到弱式 tradeoff：\(B_\theta\uparrow \Rightarrow \delta_{max}^{entropy}\downarrow\)。乘积上界需要额外的 \(\rho_I\) 下界条件，当前应视为条件强化版，而非无条件定理。该推论不推出具体优选频率，只推出“可持续频谱丰富度”与“可持续 on-time”之间存在对冲。
* **Cross-ref**: Ax-Spec-01（\(d \leftrightarrow\) 通带宽度）；T-Scale-Rhythm-4（熵耗散占空比上界）；Ax-F-13（选择-信息创造等价）。

### T-Scale-Rhythm-5: Nested Hierarchical Rhythms（嵌套层级节律，新增）

Rhythm-1–4 与 Cor-4a 刻画了单一尺度上的间歇结构。本节给出一个**条件性 P3/P4 嵌套模型**：只有当相邻尺度满足 P3-Scale-01／T-Scale-02C1 的具名相容映射，并另加能量守恒与物理嵌入的辅助桥接命题时，Rhythm-1 才能递归应用。它不是由 L0/L1 公理单独推出的普遍定理。

#### Lemma-Scale-Budget-Embed-1（尺度预算嵌入引理）

**命题**：若子层算子 $\hat{G}_\theta^{(n-1)}$ 在父层 $\hat{G}_\theta^{(n)}$ 的单次 on-phase 内嵌入运行，则子层可用功率-时间积不超过该 on-phase 的剩余功率-时间积扣除父层自身 overhead：
\[
E_{avail}^{(n-1)} \le P_{avail}^{(n)} \cdot \tau_{on}^{(n)} - C_{overhead}^{(n)}
\]

**依据**：能量守恒 + 子层物理嵌入父层——子层既不能在父层 on-phase 之外以父层的能量预算运行，也不能并行占用父层 overhead 所消耗的功率。

**负担类型**：辅助桥接命题（Bridge Lemma，[C]/[S] 混合），**非 L0/L1 公理**。上界取不等式而非等式，保留实现自由度：具体系统可能有额外损耗使 $E_{avail}^{(n-1)}$ 严格小于上界。

---

**尺度层级设定**：设系统具有 $N+1$ 层尺度 $S_0 \subset S_1 \subset \cdots \subset S_N$，其中 $S_N$ 为最粗尺度。本模型额外假定每个相邻尺度对都已经声明状态空间、粗粒化映射、保留观测量、比较范数与容差，并在该容差内满足 T-Scale-02C1。该相容性是模型前件，不由 P0/P1 保证，也不要求粗粒化映射可逆。

**on-phase 内部的预算继承**：$S_n$ 层算子按 Rhythm-2 以占空比 $\delta_n$、切换密度 $\nu_n$ 运行。由 Rhythm-2 的 $\nu$ 定义（总翻转次数/时间；一个完整 on-off cycle 含 2 次翻转），cycle 周期为 $T_{cycle}^{(n)} = 2/\nu_n$，单次 on-phase 时长为：
\[
\tau_{on}^{(n)} = \delta_n \cdot T_{cycle}^{(n)} = \frac{2\delta_n}{\nu_n}
\]
相应的 cycle 角频率为 $\omega_n \equiv 2\pi / T_{cycle}^{(n)} = \pi\, \nu_n$（本定理中 $\omega_n$ 指 cycle 角频率，非切换角频率）。在 on-phase 内，$\hat{G}_{\theta}^{(n)}$ 需维持 $k_n$ 个子目标 $\{\sigma_{n,1},\dots,\sigma_{n,k_n}\}$。由 Lemma-Scale-Budget-Embed-1，子层可用预算为：
\[
E_{avail}^{(n-1)} \le P_{avail}^{(n)} \cdot \tau_{on}^{(n)} - C_{overhead}^{(n)} = \frac{2\delta_n}{\nu_n} \cdot P_{avail}^{(n)} - C_{overhead}^{(n)}
\]
其中 $C_{overhead}^{(n)}$ 是 $S_n$ 层自身的锚定维持成本。

**递归触发条件**：若子层密集锚定代价超出子层预算：
\[
\mathcal{C}_{dense}^{(n-1)}(\tau_{on}^{(n)}, k_n) \equiv \sum_{j=1}^{k_n} \int_0^{\tau_{on}^{(n)}} \Psi_f^{maint}(\sigma_{n,j},\tau)\,d\tau > E_{avail}^{(n-1)}
\]
则 T-Scale-Rhythm-1 在 $S_{n-1}$ 层被触发：子目标 $\{\sigma_{n,j}\}$ 必须在 $\tau_{on}^{(n)}$ 内间歇调度，产生频率 $\omega_{n-1} > \omega_n$ 的子节律。

**频率分离定理**：由 $\tau_{on}^{(n)} = 2\delta_n / \nu_n$ 且子节律必须在父层 on-phase 内完成至少一个完整 cycle，子层 cycle 角频率满足：
\[
\omega_{n-1} \ge \frac{2\pi}{\tau_{on}^{(n)}} = \frac{\pi\,\nu_n}{\delta_n} = \frac{\omega_n}{\delta_n}
\]
（末步代入 $\omega_n = \pi\,\nu_n$。）由于 $\delta_n < 1$，频率严格分离：
\[
\omega_{n-1} > \omega_n \quad \forall n
\]
更一般地，$N$ 层嵌套产生频率层级：
\[
\omega_0 > \omega_1 > \cdots > \omega_N, \qquad \frac{\omega_{n-1}}{\omega_n} \ge \frac{1}{\delta_n}
\]

**递归终止条件**：嵌套在层 $m$ 处终止，当且仅当以下任一条件成立：
1. $k_m = 1$（单目标，无需分时）
2. $\mathcal{C}_{dense}^{(m-1)} \le E_{avail}^{(m-1)}$（预算充裕，可密集锚定）
3. $\tau_{on}^{(m)}$ 小于最小可行切换时间 $\tau_{switch}^{min}$（物理切换速率饱和）

**嵌套深度上界**：设每层占空比 $\delta_n \ge \delta_{min} > 0$，且最粗尺度周期为 $T_N = 2\pi/\omega_N$，最细尺度切换时间为 $\tau_{switch}^{min}$，则：
\[
N \le \left\lfloor \frac{\ln(T_N / \tau_{switch}^{min})}{\ln(1/\delta_{min})} \right\rfloor
\]

**推论**：
1. **频率比由占空比决定**：嵌套层间的频率比 $\omega_{n-1}/\omega_n \ge 1/\delta_n$ 不是任意的，而是由该层的可行占空比决定。theta-gamma 耦合中观察到的约 4–8:1 频率比对应 $\delta \approx 0.12$–$0.25$，与神经元的有效占空比相容。
2. **Phase-amplitude coupling (PAC) 是本条件模型的自然后果**：若子节律依定义只能在父节律的 on-phase 内运行，其振幅在 on-phase 内非零、off-phase 内（近似）为零——这构成一种 PAC。该结论依赖前述嵌入与门控前件，不证明经验系统中的 PAC 都由此产生。
3. **嵌套深度反映系统复杂度**：高 d 系统因 $k_n$ 更大（更多子目标）、$E_{avail}^{(n-1)}$ 更紧张（Cor-4a），更容易在每层触发递归，因而倾向于更深的嵌套层级。这预测：意识复杂度与可观测的嵌套节律层数正相关。
4. **嵌套坍缩 = 功能降级**：若某层的预算突然减少（如麻醉、缺氧），使 $E_{avail}^{(n-1)}$ 低于单目标维持成本，则该层及其所有子层的嵌套节律同时消失——对应临床上观察到的意识丧失时多层级节律同步坍缩（PCI 骤降）。

* **Implication**：在相邻尺度相容、预算嵌入、子目标多重性与切换条件全部成立的具名模型内，Rhythm-1 的递归应用可以产生分层嵌套节律。自然界所有嵌套节律是否都由此机制产生仍是 P4 问题。
* **Boundary**：本定理推出嵌套的存在性与频率分离的方向，但不推出各层的具体频率值（这取决于物理系统的具体 $\Psi_f$ 参数化）。频率比的下界 $1/\delta_n$ 是必要条件而非充分条件——实际频率比可能远大于此下界。递归终止条件 3（物理切换速率饱和）的 $\tau_{switch}^{min}$ 依赖于物质基底（离子通道翻转时间、化学反应速率等），本定理不给出通用数值。不主张所有嵌套节律都是"自上而下"生成的——自下而上的涌现节律同样存在，但本定理表明自上而下的预算分配机制足以产生嵌套结构。
* **Cross-ref**: P3-Scale-01／T-Scale-02C1（条件性跨尺度相容）；T-Scale-Rhythm-1；T-Scale-Rhythm-2；Cor-Scale-Rhythm-4a；T-Scale-Rhythm-3；SRT_Clin_00_IIT_PCI；Glossary Phase-Amplitude Coupling 条目。

### Formalization Summary (形式化概述)

本文件的核心形式化结构围绕以下关键公式展开：

1. **跨尺度结构相容候选** (P3-Scale-01): $\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$ — 只有在声明状态空间、尺度映射、保留观测量、比较范数与容差后，才检验局部跨尺度可比性；严格共轭只适用于可逆表征变换。
2. **本体论带宽定义** (Def-d-Scale-1): $d \equiv \max\text{-bandwidth}(\hat{G}_\theta \text{ against } \Psi_f)$ — d 值是算子在面对本体论摩擦时，能将 $L_0$ 压缩、锚定并维持为 $L_1$ 的最大处理带宽，与规范定义 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 统一。
3. **主动力学方程** (Ax-Master-01): $d\rho_{L_1}/dt = -(i/\hbar)[\hat{H}, \rho] - \hat{G}_\theta[\rho - \rho_{target}] + \mathcal{D}[\rho]$ — 现实密度矩阵的演化由自由展开（酉流）、选择锚定（$\hat{G}_\theta$ 项）与退相干三项共同驱动。
4. **语义边界维持** (Ax-Auto-01): $d\theta/dt = -\alpha \nabla_\theta \Psi_f + \text{Learning}$ — 自我参数 $\theta$ 的演化是摩擦梯度下降与学习更新的持续平衡。
5. **边界划定成本** (T-Scale-08): $F_{boundary}(\tau) = \mathcal{L}_{class}(\tau) + \lambda_1 \Psi_f^{maint}(\tau) + \lambda_2 \Psi_f^{switch}(\tau)$ — 在连续梯度上强制离散边界的总代价由分类误差、维持摩擦和切换代价三项组成。
6. **非零时间带宽** (T-Scale-Rhythm-1): 当连续密集锚定超过可用预算时，有限算子的有效锚定调度必含非零频率成分，分时/脉冲化成为通用可行解。
7. **占空比可行窗口** (T-Scale-Rhythm-2): 有限算子的时间调度由占空比 $\delta$（锚定时间比例）与切换密度 $\nu$（翻转频率）二维参数刻画；维持成本给出 $\delta$ 上界，松散惩罚给出 $\delta$ 下界，切换成本给出 $\nu$ 上界，三力合围形成可行窗口。
8. **耦合驱动的周期化** (T-Scale-Rhythm-3): 当下游预测成本权重 $\lambda_{pred}$ 超过阈值 $\lambda_{pred}^c$ 时，随机间歇被周期性调度取代——周期性是多算子协调成本最小化的相变结果，非有限性的直接推论。
9. **熵耗散占空比约束** (T-Scale-Rhythm-4): $\delta \le J_S^{max}/(\dot{S}_{int}^{on} + J_S^{max})$ — 独立于 $\Psi_f$ 预算的第二上界，来自热力学第二定律：选择产生的内部熵必须在"off"阶段排出，排出速率有限。实际 $\delta_{max} = \min(\delta_{max}^{budget}, \delta_{max}^{entropy})$。高 d → 高 $\dot{I}_{created}$ → 高 $\dot{S}_{int}^{on}$ → 更低 $\delta_{max}^{entropy}$，预测高 d 系统需要更多恢复时间。
10. **频谱—占空比权衡** (Cor-Scale-Rhythm-4a): Ax-Spec-01 的通带宽度与 Rhythm-4 的熵耗散上界联合推出：高 d / 宽通带提升调度的频谱丰富度上限，同时压低可持续占空比；在信息密度下界成立时，\(\delta \cdot \operatorname{Bandwidth}(H_\theta)\) 与 \(\delta\cdot d\) 都被 \(J_S^{max}\) 封顶。
11. **嵌套层级节律候选** (T-Scale-Rhythm-5, P3/P4 conditional): 在跨尺度相容、预算嵌入与各层触发条件均成立时，Rhythm-1 可递归产生子节律；相关频率界只在该具名模型内成立。

### Mechanism Explanation (机制解释)

本文件描述的动力学与标度机制通过以下方式运作：

- **跨尺度结构相容候选**: 不同尺度的 $\hat{G}_\theta$ 只有在具名尺度映射下满足 P3-Scale-01／T-Scale-02C1 时才获得局部可比性。旧 `\Delta S=H(L_0)-H(L_1)` 与普遍最小作用式不再承担证明；共同项只到选择—约束—可支付性语法。
- **三项竞争动力学**: 主方程中的酉流项代表 $L_0$ 的自由展开趋势，$\hat{G}_\theta$ 锚定项代表算子的主动选择压力（将 $\rho$ 拉向 $\rho_{target}$），退相干项 $\mathcal{D}[\rho]$ 代表环境引起的信息丢失。三者的竞争平衡决定了 $L_1$ 的稳定性与可预测性。在被动选择退化形式（Cor-Master-01a）中，当约束梯度远大于算子锚定力时，系统进入约束主导的滑行模式。
- **摩擦驱动的适应度优先机制**: 由于有限算子无法无损编码 $L_0$（$\Psi_f^{Truth} \gg \Psi_f^{Fitness}$），系统在演化上优先选择低摩擦可维持界面（适应度追踪），而非高保真真相重建。偏差-方差热力学（T-Scale-05）进一步表明，总维持成本中方差的边际代价远高于偏差，导致系统倾向”高偏差-低方差”的稳定对象表征。
- **$\Psi_f$ 作为统一约束**: 本体论摩擦 $\Psi_f$ 贯穿所有机制，既作为 $\theta$ 演化的梯度信号驱动语义边界维持，又作为边界划定的成本项约束对象个体化，还作为适应度-真相权衡的判据。d 值在三个尺度上的不同现象学（量子相干性、生物关切、宇宙拓扑紧致度）均是 $\hat{G}_\theta$ 对抗 $\Psi_f$ 的最大带宽的投影实现。
- **预算超载下的时分复用**: 当 \(\mathcal{C}_{dense}(T,k)>E_{avail}\) 时，系统不能以纯直流方式并行维持全部目标，必须通过间歇、分时或重放来重新分配锚定窗口；theta-replay、注意切换与宏观睡眠-觉醒循环都可读作这一机制在不同尺度上的实例化。
- **占空比-切换密度可行窗口**: 间歇调度不由单一参数（占空比 $\delta$）刻画——同一 $\delta$ 可对应极不同的切换密度 $\nu$。维持成本与松散惩罚夹出 $\delta$ 的上下界，切换成本限制 $\nu$，三力合围产生 $(\delta, \nu)$ 二维可行区域。窗口坍缩时系统必须放弃锚定目标或降低切换频率。
- **耦合驱动的周期化**: 孤立算子可随机间歇；但当多算子耦合时，下游需要预测上游的锚定窗口，预测成本与调度的时间熵率 $h[A]$ 成正比。当预测成本权重 $\lambda_{pred}$ 超过阈值 $\lambda_{pred}^c = (C_{per}-C_{rand})/h_{rand}$ 时，周期性调度成为全局最优——这是从间歇到节律的相变。
- **熵耗散作为独立约束**: 选择的不可逆性产生内部熵（$\dot{S}_{int}^{on} \ge k_BT \cdot \dot{I}_{created} \cdot \ln 2$），必须在"off"阶段通过有限带宽的热耦合通道排出。这给出 $\delta$ 的独立上界 $\delta_{max}^{entropy}$，不可通过增加 $E_{avail}$ 绕过。"off"阶段同时是熵导出窗口（有益）和噪声侵蚀窗口（有害，$S_{noise}$），二者的折中决定最优 $\tau_{off}^*$。高 d 系统因 $\dot{I}_{created}$ 更高而需要更长恢复时间——这是 SRT 对"为什么复杂意识有机体需要更多睡眠"的热力学解释。
- **谱-热对冲**: Ax-Spec-01 赋予高 d 算子更宽的频谱通带，但 Rhythm-4 同时规定更宽的有效通带会抬高信息创造率与熵产生率，从而压低可持续占空比。结果不是”高 d = 永远更强”，而是”高 d = 更丰富但更难持续”。
- **嵌套层级节律候选**: 在相邻尺度相容、子层物理嵌入父层 on-phase 且各层预算超载条件成立时，Rhythm-1 可递归产生子节律；PAC 与频率界是条件模型输出，不是跨尺度语法单独保证的普遍定理。

## 【理论边界/防误用声明】
- 不采纳”适应度优先=真理无意义”的推论：SRT 主张的是资源约束下的近似策略，不是否定真值结构。
- 不采纳”界面可构造=可任意构造”的推论：外部阻抗地形通过 \(\Psi_f\) 客观限制可行结构。

<br>

---


# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections provide the detailed philosophical, physical, and phenomenological elaboration of SRT's master dynamics and scale-invariance principles.

---
