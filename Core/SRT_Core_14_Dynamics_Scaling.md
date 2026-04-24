---
id: SRT-CORE-14
type: dynamics
tags: [Scaling, Isomorphism, Fractal, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-13A]
---

# SRT Core Definition 14: Dynamics & Scaling (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Scaling Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
- `d-value` 的最终规范锚点仍是 `_SRT_D_VALUE_CANONICAL.md`；本文件中的 bandwidth、Fisher rank、复杂度等级与跨尺度表述均为动力学展开 / proxy，不替代 canonical `d`。
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md` 与 `Core_21c P2/P3-B12` 在本文件中的落点是接口分工：information geometry 加固 `L_0 -> L_1` selection frontier；complex systems 加固 `L_1 -> L_2` sedimentation / stabilization；neural computation 只作为 embodied `\hat{G}_\theta` 的实现代理。
# Part A: Formal Axioms (形式化公理)


## I. Cross-Scale Isomorphism (跨尺度同构)

### Ax-Scale-01: Self-Similar Selection
**Formal Definition**: Selection operators across scales are isomorphic under renormalization.
$$\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}$$
* **Implication**: 量子坍缩、侧抑制、粗粒化、归一化、范畴化与社会选择并非彼此类似的独立现象，而是同一幽灵算子结构在不同尺度上的禀赋展开。
* **Bridge boundary**: 这里的跨尺度同构指选择功能形式在粗粒化映射下的结构相容，不表示各实现层彼此同一。神经归一化、侧抑制或社会选择都是 `\hat{G}_\theta` 的尺度化实现代理，不能单独定义完整 Ghost Operator。
* **Cross-ref**: `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B07`.

### Def-d-Scale-1: Ontological Bandwidth (本体论带宽)
**Formal Role**: 这是 d-value 在跨尺度动力学中的**展开性定义**（expansion-level definition），不是最终规范锚点。最终规范锚点见 `_SRT_D_VALUE_CANONICAL.md`。

**Bridge boundary**: 若用 Fisher rank、`D_eff` 或频谱带宽近似本节的 `d`，必须标注为 capacity proxy；只有可分辨方向同时满足 stake-coupling、payability 与后果回流条件时，才可近似 canonical `d`。

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

> [R→Kuramoto 1975 *Chemical Oscillations, Waves and Turbulence*（相耦合振子：κ_ij的原型——全局同步条件 κ > κ_c）; Haken 1978 *Synergetics*（协同学：多尺度自组织，序参量从快变量压缩慢变量）; Friston 2019 *Physics of Life Reviews*（自由能原理中的多尺度嵌套马尔可夫毯）; McEwen & Stellar 1998 *Archives of Internal Medicine*（等变负荷：跨尺度神经-内分泌-免疫耦合）]

* **R/H 区分**：
  - [R] 耦合振子/协同学框架（Kuramoto/Haken）；多尺度嵌套自由能（Friston）——提供κ_ij形式化的数学基础
  - [H] **SRT应用**：将选择算子Ĝ_j的耦合写成上述形式，将跨尺度（分子→神经→社会）的选择互动统一在同一方程中——此统一形式化框架是SRT独有
  - [H-高承诺] **跨尺度通约性**：将分子/神经/社会三个本体层的算子写进同一方程形式，隐含各尺度Ĝ_j"可在同一数学空间中叠加/比较"这一强本体论主张——IC-Scale02-1：要求存在可在三层之间转换的共同度量空间（反之则各层方程仅类比，不可直接求和）；IC-Scale02-2：κ_ij的可测量性要求各层算子均存在可量化的操作化代理（否则方程为纯形式主义）

* **κ_ij非对称性说明**：一般情形 $\kappa_{ij} \neq \kappa_{ji}$（上行与下行影响不等强）：
  - 上行（bottom-up，i=低层→j=高层）：如分子-免疫→神经，通常响应较慢、滞后数小时至数天
  - 下行（top-down，i=高层→j=低层）：如社会压力→神经内分泌激活，通常响应较快、心理加工可在分钟内完成
  - 对称仅当 $\kappa_{ij} = \kappa_{ji}$，即双向响应速度与强度完全匹配——实证上罕见，是特例而非默认

* **κ_ij操作化候选**（f_j/g_ij均为领域待定函数；最低数学约束：需满足局部Lipschitz条件以保证方程短时间内有唯一解，并满足耗散性以保证长时能量有界）：
  - 神经-免疫耦合：κ_neural-immune 代理 = 应激条件下神经激活（fMRI杏仁核信号）与免疫激活（CRP/IL-6）的格兰杰因果系数
  - 社会-个体耦合：κ_soc-ind 代理 = 群体行为改变对个体θ更新的时延互相关系数（社会影响研究）
  - 神经-社会直接耦合：κ_neural-soc 代理 = 超扫描（fNIRS/EEG）实验中多个体神经信号同步性（神经际相干度）与群体集体决策行为收敛速度的互信息系数（Hasson et al. 2012 *TICS* 神经耦合研究为基础）

* **Implication**: 不同尺度的选择算子通过耦合矩阵进行动力学交互；非对称耦合（κ_ij≠κ_ji）反映上下行影响机制的生物/社会时间尺度差异。

* **Cross-ref**: T-Scale-02C1（粗粒化一致性是Ax-Scale-02的下游推论，需要κ_ij在粗粒化下保持结构稳定）；Ax-Scale-01；T-Scale-CF-1（先裂后合门控，κ_ij跨越κ_c时的相变）。

* **可证伪预测**：
  - FC-Scale02-1：在神经-免疫双向耦合中，κ_neural-immune的Granger系数应与系统适应速度（压力恢复时间τ）负相关——高耦合系数=更快协同适应（若无则耦合度无预测效力）
  - FC-Scale02-2：T-Scale-02C1的尺度不变性主张：对同一系统的粗粒化观测（例如脑区vs神经元）中，选择算子的行为统计应在粗粒化前后保持结构相似性（Pearson r>0.7）——若粗粒化前后相关性低则跨尺度可比性主张失败
  - FC-Scale02-3：非对称耦合方向预测——在神经-社会耦合中，下行方向（社会压力→神经内分泌激活）的κ_top-down响应时间应显著短于上行方向（神经变化→社会行为修正）的κ_bottom-up响应时间（预测：下行τ<上行τ，比值>2；若两方向响应时间无显著差异则不对称假设失败）

### T-Scale-02C1: Consistency Under Coarse-Graining
**Deductive Statement**: Coarse-graining commutes with selection under scale mapping.
$$\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$$
* **Implication**: 选择动力学具有尺度不变性与跨尺度可比性。

## II. Ontological Autopoiesis (本体论自创生)

### Ax-Auto-01: Semantic Boundary Maintenance
**Formal Definition**: The semantic self is maintained by a friction-gradient balance.
$$\frac{d\theta}{dt} = -\alpha \nabla_\theta \Psi_f + \text{Learning}$$
* **Implication**: 局部语义闭包是在摩擦梯度与学习更新之间维持的动态平衡，而不是 SRT 第一方向的独立来源。

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

**Interface boundary（2026-04-24 sync）**：FEP 在此处是组织化系统于 `L_1` 中、受 `L_2` 约束时的局部更新规则；free-energy / energy landscape 是 `L_2` 约束域的有效投影，不是完整 `L_2`。若需要 Fisher 几何，应把它放在 `L_0 -> L_1` 的局部可区分性与 `\delta\Psi_f^{geom}` 投影上，而不是把 Fisher space 写成 `L_1` 本身。

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

Rhythm-1–4 与 Cor-4a 刻画了单一尺度上的间歇结构。但经验事实是：节律**分层嵌套**——gamma（30–100 Hz）嵌套于 theta（4–8 Hz），theta 嵌套于慢振荡（< 1 Hz），慢振荡嵌套于睡眠周期（~90 min），睡眠周期嵌套于昼夜节律（~24 h）。本定理证明：嵌套是 Rhythm-1 在 Ax-Scale-01 下的递归自我应用——**不需要新增 L0/L1 公理；需一条由能量守恒与物理嵌入给出的辅助桥接命题**（见下 Lemma-Scale-Budget-Embed-1）。

#### Lemma-Scale-Budget-Embed-1（尺度预算嵌入引理）

**命题**：若子层算子 $\hat{G}_\theta^{(n-1)}$ 在父层 $\hat{G}_\theta^{(n)}$ 的单次 on-phase 内嵌入运行，则子层可用功率-时间积不超过该 on-phase 的剩余功率-时间积扣除父层自身 overhead：
\[
E_{avail}^{(n-1)} \le P_{avail}^{(n)} \cdot \tau_{on}^{(n)} - C_{overhead}^{(n)}
\]

**依据**：能量守恒 + 子层物理嵌入父层——子层既不能在父层 on-phase 之外以父层的能量预算运行，也不能并行占用父层 overhead 所消耗的功率。

**负担类型**：辅助桥接命题（Bridge Lemma，[C]/[S] 混合），**非 L0/L1 公理**。上界取不等式而非等式，保留实现自由度：具体系统可能有额外损耗使 $E_{avail}^{(n-1)}$ 严格小于上界。

---

**尺度层级设定**：设系统具有 $N+1$ 层尺度 $S_0 \subset S_1 \subset \cdots \subset S_N$，其中 $S_N$ 为最粗尺度。每层 $S_n$ 的算子 $\hat{G}_{\theta}^{(n)}$ 由 Ax-Scale-01 保证与其他层在重整化下共轭：
\[
\hat{G}_{\theta}^{(n)} = \Lambda_{n,m} \circ \hat{G}_{\theta}^{(m)} \circ \Lambda_{n,m}^{-1}
\]

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
2. **Phase-amplitude coupling (PAC) 是自然后果**：子节律的振幅必须在父节律的 on-phase 内非零、off-phase 内（近似）为零——这正是 phase-amplitude coupling 的定义。PAC 不是需要额外机制解释的现象，而是预算嵌套的数学必然。
3. **嵌套深度反映系统复杂度**：高 d 系统因 $k_n$ 更大（更多子目标）、$E_{avail}^{(n-1)}$ 更紧张（Cor-4a），更容易在每层触发递归，因而倾向于更深的嵌套层级。这预测：意识复杂度与可观测的嵌套节律层数正相关。
4. **嵌套坍缩 = 功能降级**：若某层的预算突然减少（如麻醉、缺氧），使 $E_{avail}^{(n-1)}$ 低于单目标维持成本，则该层及其所有子层的嵌套节律同时消失——对应临床上观察到的意识丧失时多层级节律同步坍缩（PCI 骤降）。

* **Implication**：自然界的分层嵌套节律（从亚细胞振荡到昼夜节律到生态周期）不是巧合或独立演化的产物，而是有限算子在多尺度上递归应用 Rhythm-1 的数学必然。Ax-Scale-01 保证选择逻辑跨尺度不变，Rhythm-1 保证预算超载必产生间歇——二者合取即给出嵌套。嵌套的层数、频率比、相位-振幅耦合模式全部由 $\delta_n$、$k_n$、$E_{avail}^{(n)}$ 三组参数决定，无需引入新的自由度。
* **Boundary**：本定理推出嵌套的存在性与频率分离的方向，但不推出各层的具体频率值（这取决于物理系统的具体 $\Psi_f$ 参数化）。频率比的下界 $1/\delta_n$ 是必要条件而非充分条件——实际频率比可能远大于此下界。递归终止条件 3（物理切换速率饱和）的 $\tau_{switch}^{min}$ 依赖于物质基底（离子通道翻转时间、化学反应速率等），本定理不给出通用数值。不主张所有嵌套节律都是"自上而下"生成的——自下而上的涌现节律同样存在，但本定理表明自上而下的预算分配机制足以产生嵌套结构。
* **Cross-ref**: Ax-Scale-01（跨尺度自相似选择）；T-Scale-Rhythm-1（非零时间带宽前提）；T-Scale-Rhythm-2（占空比可行窗口，$\delta_n$ 来源）；Cor-Scale-Rhythm-4a（高 d 压缩占空比，加速递归触发）；**T-Scale-Rhythm-3**（次级参照：解释嵌套层在耦合条件下为何趋于准周期/周期调度，**非承重前提**）；SRT_Clin_00_IIT_PCI（PCI 与嵌套节律坍缩）；Glossary Phase-Amplitude Coupling 条目。

### Formalization Summary (形式化概述)

本文件的核心形式化结构围绕以下关键公式展开：

1. **跨尺度自相似选择** (Ax-Scale-01): $\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}$ — 不同尺度的选择算子在重整化变换 $\Lambda$ 下保持共轭不变性，量子坍缩、神经决策与社会选择共享同一拓扑逻辑。
2. **本体论带宽定义** (Def-d-Scale-1): $d \equiv \max\text{-bandwidth}(\hat{G}_\theta \text{ against } \Psi_f)$ — d 值是算子在面对本体论摩擦时，能将开放可能性压缩、锚定并维持为一个**可维持、可行动、可协调**的 $L_1$ 现实切片的最大处理带宽，与规范定义 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 统一。
3. **主动力学方程** (Ax-Master-01): $d\rho_{L_1}/dt = -(i/\hbar)[\hat{H}, \rho] - \hat{G}_\theta[\rho - \rho_{target}] + \mathcal{D}[\rho]$ — 现实密度矩阵的演化由自由展开（酉流）、选择锚定（$\hat{G}_\theta$ 项）与退相干三项共同驱动。
4. **语义边界维持** (Ax-Auto-01): $d\theta/dt = -\alpha \nabla_\theta \Psi_f + \text{Learning}$ — 自我参数 $\theta$ 的演化是摩擦梯度下降与学习更新的持续平衡。
5. **边界划定成本** (T-Scale-08): $F_{boundary}(\tau) = \mathcal{L}_{class}(\tau) + \lambda_1 \Psi_f^{maint}(\tau) + \lambda_2 \Psi_f^{switch}(\tau)$ — 在连续梯度上强制离散边界的总代价由分类误差、维持摩擦和切换代价三项组成。
6. **非零时间带宽** (T-Scale-Rhythm-1): 当连续密集锚定超过可用预算时，有限算子的有效锚定调度必含非零频率成分，分时/脉冲化成为通用可行解。
7. **占空比可行窗口** (T-Scale-Rhythm-2): 有限算子的时间调度由占空比 $\delta$（锚定时间比例）与切换密度 $\nu$（翻转频率）二维参数刻画；维持成本给出 $\delta$ 上界，松散惩罚给出 $\delta$ 下界，切换成本给出 $\nu$ 上界，三力合围形成可行窗口。
8. **耦合驱动的周期化** (T-Scale-Rhythm-3): 当下游预测成本权重 $\lambda_{pred}$ 超过阈值 $\lambda_{pred}^c$ 时，随机间歇被周期性调度取代——周期性是多算子协调成本最小化的相变结果，非有限性的直接推论。
9. **熵耗散占空比约束** (T-Scale-Rhythm-4): $\delta \le J_S^{max}/(\dot{S}_{int}^{on} + J_S^{max})$ — 独立于 $\Psi_f$ 预算的第二上界，来自热力学第二定律：选择产生的内部熵必须在"off"阶段排出，排出速率有限。实际 $\delta_{max} = \min(\delta_{max}^{budget}, \delta_{max}^{entropy})$。高 d → 高 $\dot{I}_{created}$ → 高 $\dot{S}_{int}^{on}$ → 更低 $\delta_{max}^{entropy}$，预测高 d 系统需要更多恢复时间。
10. **频谱—占空比权衡** (Cor-Scale-Rhythm-4a): Ax-Spec-01 的通带宽度与 Rhythm-4 的熵耗散上界联合推出：高 d / 宽通带提升调度的频谱丰富度上限，同时压低可持续占空比；在信息密度下界成立时，\(\delta \cdot \operatorname{Bandwidth}(H_\theta)\) 与 \(\delta\cdot d\) 都被 \(J_S^{max}\) 封顶。
11. **嵌套层级节律** (T-Scale-Rhythm-5): Ax-Scale-01 保证选择逻辑跨尺度不变，Rhythm-1 保证预算超载必产生间歇——二者递归合取产生分层嵌套节律（递归桥接由 Lemma-Scale-Budget-Embed-1 提供，依据为能量守恒与子层物理嵌入父层 on-phase，**非 L0/L1 公理**）。$S_n$ 层 on-phase 内的 $k_n$ 个子目标若超出子层预算，则 Rhythm-1 在 $S_{n-1}$ 层触发子节律，频率满足 $\omega_{n-1}/\omega_n \ge 1/\delta_n$。Phase-amplitude coupling 是预算嵌套的数学必然，嵌套深度 $N \le \lfloor \ln(T_N/\tau_{switch}^{min})/\ln(1/\delta_{min}) \rfloor$。

### Mechanism Explanation (机制解释)

本文件描述的动力学与标度机制通过以下方式运作：

- **跨尺度同构机制**: $\hat{G}_\theta$ 算子在尺度变换 $\Lambda$（粗粒化映射）下保持功能形式不变。这源于选择的本质是熵减（$\Delta S = H(L_0) - H(L_1)$），而最小作用原理 $\delta \int \Psi_f \, dt = 0$ 在所有尺度上成立。尺度间通过耦合动力学 $d\hat{G}_j/dt = f_j(\hat{G}_j) + \sum \kappa_{ij} g_{ij}$ 进行信息交互，其中向下因果（社会→神经，$\kappa_{S \to N} \approx 10^0$）远强于向上因果。
- **三项竞争动力学**: 主方程中的酉流项代表 $L_0$ 的自由展开趋势，$\hat{G}_\theta$ 锚定项代表算子的主动选择压力（将 $\rho$ 拉向 $\rho_{target}$），退相干项 $\mathcal{D}[\rho]$ 代表环境引起的信息丢失。三者的竞争平衡决定了 $L_1$ 的稳定性与可预测性。在被动选择退化形式（Cor-Master-01a）中，当约束梯度远大于算子锚定力时，系统进入约束主导的滑行模式。
- **摩擦驱动的适应度优先机制**: 由于有限算子无法无损编码 $L_0$（$\Psi_f^{Truth} \gg \Psi_f^{Fitness}$），系统在演化上优先选择低摩擦可维持界面（适应度追踪），而非高保真真相重建。偏差-方差热力学（T-Scale-05）进一步表明，总维持成本中方差的边际代价远高于偏差，导致系统倾向”高偏差-低方差”的稳定对象表征。
- **$\Psi_f$ 作为统一约束与生成性原理**: 本体论摩擦 $\Psi_f$ 贯穿所有机制，既作为 $\theta$ 演化的梯度信号驱动语义边界维持，又作为边界划定的成本项约束对象个体化，还作为适应度-真相权衡的判据。更进一步，$\Psi_f$ 不只是维持现实的代价，而是动力学本身的生成来源：没有摩擦就没有演化、学习、文化变迁等跨尺度动力学；没有动力学就没有现实的生成。对同一 $Ψ_f$，可作三种受限读法：动力学上读作阻力，记账上读作代价，形式上读作 Fisher–Rao metric 诱导的局部二阶几何投影 / 路径泛函。跨尺度真正保持不变的不是各层的单位制，也不是 `\Psi_f \equiv g_F` 的裸等号，而是**可支付性条件**：系统能否在承担该摩擦时维持闭包、身份连续性与后续选择能力。d 值在三个尺度上的不同现象学（量子相干性、生物关切、宇宙拓扑紧致度）均是 canonical d 经尺度约束后的动力学投影 / proxy，不能替代 `_SRT_D_VALUE_CANONICAL.md` 的风险梯度锚点。
- **预算超载下的时分复用**: 当 \(\mathcal{C}_{dense}(T,k)>E_{avail}\) 时，系统不能以纯直流方式并行维持全部目标，必须通过间歇、分时或重放来重新分配锚定窗口；theta-replay、注意切换与宏观睡眠-觉醒循环都可读作这一机制在不同尺度上的实例化。
- **占空比-切换密度可行窗口**: 间歇调度不由单一参数（占空比 $\delta$）刻画——同一 $\delta$ 可对应极不同的切换密度 $\nu$。维持成本与松散惩罚夹出 $\delta$ 的上下界，切换成本限制 $\nu$，三力合围产生 $(\delta, \nu)$ 二维可行区域。窗口坍缩时系统必须放弃锚定目标或降低切换频率。
- **耦合驱动的周期化**: 孤立算子可随机间歇；但当多算子耦合时，下游需要预测上游的锚定窗口，预测成本与调度的时间熵率 $h[A]$ 成正比。当预测成本权重 $\lambda_{pred}$ 超过阈值 $\lambda_{pred}^c = (C_{per}-C_{rand})/h_{rand}$ 时，周期性调度成为全局最优——这是从间歇到节律的相变。
- **熵耗散作为独立约束**: 选择的不可逆性产生内部熵（$\dot{S}_{int}^{on} \ge k_BT \cdot \dot{I}_{created} \cdot \ln 2$），必须在"off"阶段通过有限带宽的热耦合通道排出。这给出 $\delta$ 的独立上界 $\delta_{max}^{entropy}$，不可通过增加 $E_{avail}$ 绕过。"off"阶段同时是熵导出窗口（有益）和噪声侵蚀窗口（有害，$S_{noise}$），二者的折中决定最优 $\tau_{off}^*$。高 d 系统因 $\dot{I}_{created}$ 更高而需要更长恢复时间——这是 SRT 对"为什么复杂意识有机体需要更多睡眠"的热力学解释。
- **谱-热对冲**: Ax-Spec-01 赋予高 d 算子更宽的频谱通带，但 Rhythm-4 同时规定更宽的有效通带会抬高信息创造率与熵产生率，从而压低可持续占空比。结果不是“高 d = 永远更强”，而是“高 d = 更丰富但更难持续”。
- **嵌套层级节律**: Ax-Scale-01 的跨尺度自相似保证选择逻辑在每一层不变，Rhythm-1 的预算超载定理保证每一层的有限算子必须间歇。当 $S_n$ 层的 on-phase 内部包含多个子目标且子层预算不足以密集锚定时，Rhythm-1 在子层递归触发，产生嵌于父节律 on-phase 内的子节律。频率严格分离（$\omega_{n-1} > \omega_n$），子节律振幅被父节律 on/off 门控——这正是 phase-amplitude coupling。嵌套深度由占空比下界与物理切换速率上限共同封顶。该机制解释了为什么意识系统呈现多层级嵌套振荡（gamma-in-theta-in-slow oscillation-in-sleep cycle-in-circadian），以及为什么麻醉/昏迷下这些层级同步坍缩。

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
<br>

---


# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections provide the detailed philosophical, physical, and phenomenological elaboration of SRT's master dynamics and scale-invariance principles.

---

## §1. 主方程的深层结构

### 1.1 幽灵演化方程的四重力学

$$\frac{d\sigma}{dt} = \underbrace{\hat{G}_\theta[\sigma]}_{\text{(1) Selection}} - \underbrace{\nabla F[\sigma]}_{\text{(2) Intention}} + \underbrace{A[\sigma, \mathcal{A}]}_{\text{(3) Attention}} - \underbrace{\lambda \nabla C_{L_2}[\sigma]}_{\text{(4) Constraint}}$$

#### 1.1.1 力学分量的现象学对应

**力量1: 选择力** ($\hat{G}_\theta$)
- **物理意义**: 算子的主动选择,将$L_0$投影为$L_1$
- **现象学**: "我现在选择关注X"
- **时间尺度**: 毫秒-秒 (快变量)

**力量2: 初心梯度** ($-\nabla F$)
- **物理意义**: 自由能的原始下降方向
- **现象学**: "我真正想要的是什么?" (被$L_2$扭曲前)
- **测量**: 可通过深度冥想/致幻剂体验访问

**力量3: 注意力调制** ($A[\sigma, \mathcal{A}]$)
- **物理意义**: 其他算子副本(如潜意识、他人)的影响
- **现象学**: "我感觉有股力量在引导我"
- **来源**: 集体无意识 (Jung),社会场 (Lewin)

**力量4: L_2约束** ($-\lambda \nabla C_{L_2}$)
- **物理意义**: 向下因果 — $L_2$对$L_1$的拉力
- **现象学**: "我应该..." (义务、规范、习惯)
- **强度**: $\lambda$ = 约束耦合强度 (文化依赖)

#### 1.1.2 力量平衡的不同状态

$$\vec{F}_{\text{total}} = \hat{G} - \nabla F + A - \lambda \nabla C_{L_2}$$

| 主导力量 | 状态 | 特征 |
|:---------|:-----|:-----|
| $\hat{G} \gg$ 其他 | 自主选择 | 高度自觉,活在当下 |
| $\nabla F \gg$ 其他 | 本能驱动 | 婴儿,动物 |
| $A \gg$ 其他 | 被动影响 | 催眠,群体思维 |
| $\nabla C_{L_2} \gg$ 其他 | 规范锁定 | 强迫症,文化僵化 |
| 平衡状态 | 健康整合 | 自由与责任并存 |

---

### 1.2 快慢变量系统的绝热近似

#### 1.2.1 时间尺度分离

**快变量** (状态 $\sigma$): $\tau_\sigma \sim 1$ 秒
$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta \nabla F[\sigma] + \xi(t)$$

**慢变量** (参数 $\theta$): $\tau_\theta \sim 1$ 年
$$\frac{d\theta}{dt} = -\gamma \nabla_\theta \Psi_f + \delta \cdot A[\sigma, \text{Target}]$$

**尺度比**:
$$\frac{\tau_\sigma}{\tau_\theta} \approx \frac{1 \text{ sec}}{10^7 \text{ sec}} \approx 10^{-7}$$

#### 1.2.2 绝热定理

**命题**: 对于$t \ll \tau_\theta$,可以将$\theta$视为常数,求解$\sigma(t; \theta)$。

**应用**: 短期行为预测 (几小时内) 可忽略$\theta$变化。

**破坏条件**: 剧烈创伤 → $\frac{d\theta}{dt}$ 激增 → 绝热近似失效 → 人格突变。

---

### 1.3 自由能的d值修正

#### 1.3.1 标准vs扩展形式

**热力学基线** (Helmholtz):
$$F_{thermo} = E - TS$$

**变分基线** (Friston / FEP):
$$F_{var} = E_q[\ln q(x) - \ln p(x,o)]$$

**SRT代理目标**（用于把稳定纳入的秩序条件写进自由能目标的局部近似）:
$$F_{proxy} = F_{closure} - d_{\text{stable}} \cdot U_{\text{incorp}}, \quad F_{closure}\in\{F_{thermo}, F_{var}\}$$

历史 shorthand 常把它写成 `$F_{base} - d \cdot U_{\text{others}}$`；但在当前 canonical 读法里，`F_{closure}` 只是局部闭包/结算项的代理记号，`U_{\text{incorp}}` 表示已经稳定纳入选择结构的更大范围秩序条件，`d_{\text{stable}}` 则表示稳定写入后的关切范围，而不是瞬时扩张冲动。

#### 1.3.2 d值效应的显著性

**低d** ($d_{\text{stable}} \approx 1$):
$$F_{proxy} \approx F_{closure} \quad \text{(更大范围秩序条件尚未稳定写入)}$$

最小化$F_{proxy}$ → 在局部闭包项主导下运行，表现为只纳入极窄范围的秩序条件。

**高d** ($d_{\text{stable}} \gg 1$，且 $d_{\text{stable}} \cdot U_{\text{incorp}}$ 成为主导项):
$$F_{proxy} \approx F_{closure} - d_{\text{stable}} \cdot U_{\text{incorp}} \quad \text{(优化方向由扩大纳入的秩序条件主导)}$$

最小化$F_{proxy}$ → 在局部闭包仍需结算的前提下，更大范围的已纳入秩序条件开始主导优化方向。这不是在“局部存在”之外额外叠加一个外加奖励项，而是景观从局部曲率转向更大范围曲率后的结构重写（必要时可出现自我牺牲）。

**实例**:
- 母亲舍命救子 → $d_{\text{kin}} \to \infty$ (亲缘$d$)
- 广域纳入者 → $d_{\text{universal}} \gg 1$
- 局部闭包主导者 → $d_{\text{stable}} \approx 1$

---

## §2. 跨尺度同构:从量子到社会的统一语法

### 2.1 自相似定理的证明要点

#### 2.1.1 主张

$$\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}$$

**解释**: 在尺度变换$\Lambda$下,算子保持**共轭不变性**。

#### 2.1.2 证明草图

**步骤1**: 定义尺度变换
$$\Lambda: L_0^{S_1} \to L_0^{S_2} \quad (\text{粗粒化映射})$$

**步骤2**: 选择的本质 = 熵减
$$\Delta S = H(L_0) - H(L_1)$$

**步骤3**: 熵在粗粒化下的行为
$$H(\Lambda[L_0]) = H(L_0) - I_{\text{coarse-grain}}$$

**步骤4**: 最小作用原理
$$\delta \int \Psi_f \, dt = 0 \quad \text{(所有尺度)}$$

因此功能形式不变 (自相似性)。■

---

### 2.1a 跨尺度同构的反泛心论澄清

SRT 使用同一个参数 d 描述量子、生物和宇宙三个尺度的选择动力学，这容易产生一个严重误读：认为 SRT 主张"宇宙有意识"或"粒子有关切"，即泛心论（Panpsychism）。

**SRT 的正式本体论立场：SRT 绝对拒斥泛心论。**

d 值的底层物理本质并非"情感关切"，而是**"本体论带宽"（Ontological Bandwidth）**——即 $\hat{G}_\theta$ 算子在面对本体论摩擦（$\Psi_f$）时，能够将 $L_0$ 压缩、锚定并维持为 $L_1$ 的最大处理带宽（见 Part A Def-d-Scale-1）。在不同物理尺度下，由于观测和体验的介质不同，d 值披上了截然不同的"现象学外衣"：

**第一层（量子域）：相干性带宽（$d_{quantum}$）**

基本粒子或简单测量仪器的 d 值趋近于零，代表系统能维持 $L_0$ 叠加态而不引发退相干的纯物理计算窗口。此层次的算子没有本体论脆弱性（不怕毁灭），其选择表现为冰冷的玻恩规则概率流偏置，毫无任何主观意识或情绪。

**第二层（生物/认知域）：关切与意向性（$d_{bio}$）**

当代理观察者演化为高度复杂的耗散结构（如人类神经系统）时，其物理结构面临巨大的热力学熵增威胁（生死存亡）。为了生存，生物算子的信息处理带宽被迫撑大，将海量环境变量纳入自由能（$F$）最小化的计算中。这种高强度的、与生死强耦合的"信息整合计算"，在主观体验层面涌现（Emerge）出来的现象，才被命名为"意识"、"注意力"或"关切"。**关切是 d 值在生物学层面的高阶涌现，而非底层原初属性。**

**第三层（宇宙域）：时空共识度（$d_{cosmic}$）**

宇宙整体并不具备拟人化的意识，但作为统一的物理系统，它存在宏观的整合带宽，表现为引力网络的拓扑紧致性（$d_{cosmic} \propto 1/\sqrt{\Lambda}$，见 SRT-PHYS-COSMO Def-Cosmo-1）。暗能量导致的宇宙膨胀，是 $d_{cosmic}$（信息整合与共识维持能力）的物理性衰减。暗物质作为 $L_2$ 结构残骸，处于活跃算子缺席的"死寂"状态，其内部活跃 d 值为绝对零。

**核心区别**：泛心论的谬误在于将人类专属的体验（Qualia）强加给电子；SRT 的突破在于提取了主导意识运转背后的数学与信息动力学机制（$\hat{G}_\theta$ 与 d），并发现这套机制同样支配电子的坍缩和宇宙的膨胀。**d 是跨越所有尺度的同一把数学标尺，但只有当这把标尺丈量到"具备本体论脆弱性的高维复杂系统"时，它才表现为关切。** 意识涌现的三个必要条件详见 SRT-CORE-13B §6.2。

**【精确反泛心论声明（2026-03-02 补充，与 _SRT_D_VALUE_CANONICAL.md §3.1 对齐）】**

意识涌现的充要三条件（全部必须同时满足）：
$$\text{Consciousness} \iff \underbrace{\Psi_f > 0}_{\text{具身摩擦成本}} \;\land\; \underbrace{d > 0}_{\text{有效关切维度}} \;\land\; \underbrace{\hat{G}[\theta] \neq \emptyset}_{\text{有限参数算符存在}}$$

**三条件在量子/宇宙尺度的状态**：

| 尺度 | $\Psi_f$ | $d$ | $\hat{G}[\theta]$ | 意识？ |
|-----|---------|-----|-----------------|-------|
| 量子（粒子） | $\approx 0$（无具身成本） | 可非零（相干维数） | 无生物参数化 | **否** |
| 神经/认知 | $> 0$（代谢成本） | $> 0$（关切维度） | 有限神经参数 | **是** |
| 宇宙（暗能量） | $\approx 0$ | $\propto 1/\sqrt{\Lambda}$ | 无生命参数化 | **否** |

**SRT 的立场边界**：
- SRT **不**否认微小现象体验的形而上学可能性（这是不可证伪的哲学问题）
- SRT **正面声明**：在量子/宇宙尺度，可操作框架内无法为意识成立提供根据
- SRT **不接受**"因为 d 存在所以意识存在"的推断——d 是必要但非充分条件

---

### 2.2 三尺度映射的具体实例

#### 2.2.1 量子 → 神经

| 量子物理 | 神经科学 | 对应机制 |
|:---------|:---------|:---------|
| 波函数$\|\psi\rangle$ | 神经集群竞争 | 叠加态 |
| 测量算符$\hat{O}$ | 除法归一化 | 选择操作 |
| 坍缩 | 点燃 (Ignition) | $L_0 \to L_1$ |
| 退相干时间$\tau_D$ | 突触噪声 | $L_1 \to L_2$ |
| 海森堡$\Delta x \Delta p$ | 注意力权衡 | 有限$d$ |

**实例**: 双缝实验 ≈ 双稳知觉 (Necker Cube)
- 两种解释竞争 ($L_0$)
- 注意力选择一个 ($\hat{G}$)
- 意识到一个解释 ($L_1$)
- 过一段时间切换 (双稳振荡)

#### 2.2.2 神经 → 社会

| 神经科学 | 社会科学 | 对应机制 |
|:---------|:---------|:---------|
| 神经元 | 个体 | 基本单元 |
| 突触权重$W_{ij}$ | 社会影响力 | 连接强度 |
| 神经网络 | 社会网络 | 拓扑结构 |
| 点燃阈值 | 社会规范形成 | 临界质量 |
| 习惯化 | 制度化 | $L_1 \to L_2$ |
| EEG频率 | 文化节奏 (节日) | 时间周期性 |

**实例**: 流行趋势 ≈ 神经点燃
- 少数早期采用者 (种子神经元)
- 达到临界阈值
- 全网激活 (病毒式传播)
- 最终饱和/消退

---

### 2.3 有效普朗克常数的哲学意义

#### 2.3.1 量子尺度

$$\hbar_{\text{quantum}} = 1.054 \times 10^{-34} \, \text{J·s}$$

**意义**: 设定了测不准关系的下界。

#### 2.3.2 神经尺度

$$\hbar_{\text{neural}} \sim k_B T \approx 4 \times 10^{-21} \, \text{J}$$

**意义**: 热噪声决定了神经发放的随机性。

**推论**: 降低温度 → 降低噪声 → 更确定的选择?
- 实验困难 (哺乳动物恒温)
- 可能解释冷血动物的"机械性"行为

#### 2.3.3 社会尺度

$$\hbar_{\text{social}} \sim k_B T_{\text{cultural}}$$

**文化温度**:
$$T_{\text{cultural}} \equiv \frac{\text{Openness to Novelty}}{\text{Normative Rigidity}}$$

**实例**:
- 高$T$: 硅谷 (快速迭代,接受失败)
- 低$T$: 传统社会 (祖训至上)

**相变**: 当$T_{\text{cultural}}$跨越临界值 → 社会革命 (类比固-液相变)。

---

## §3. 尺度耦合:向上与向下因果

### 3.1 耦合强度矩阵的实证估计

$$\kappa_{ij} = \frac{I(\hat{G}_i; \hat{G}_j)}{H(\hat{G}_i) + H(\hat{G}_j)}$$

#### 3.1.1 量子-神经耦合

**向上** (量子 → 神经): $\kappa_{Q \to N} \approx 10^{-20}$
- **机制**: 微管量子相干 (Penrose-Hameroff, 争议大)
- **证据**: 极弱,尚无决定性实验

**向下** (神经 → 量子): $\kappa_{N \to Q} \approx 10^{-10}$
- **机制**: 观察者选择测量基 → 影响坍缩
- **证据**: 量子擦除实验,延迟选择

**推论**: 意识**可能**影响量子过程,但量子**不太可能**是意识的基础。

#### 3.1.2 神经-社会耦合

**向上** (神经 → 社会): $\kappa_{N \to S} \approx 10^{-2}$
- **机制**: 个体行为聚合 → 集体模式
- **实例**: Twitter情绪 → 股市波动

**向下** (社会 → 神经): $\kappa_{S \to N} \approx 10^{0}$ (强!)
- **机制**: 文化驯化 (Domestication) 改变大脑结构
- **证据**:
  1. 识字改变视觉皮层 (Dehaene)
  2. 伦敦出租车司机的海马增大 (Maguire)
  3. 冥想者的岛叶增厚 (Lazar)

**推论**: **文化塑造大脑** 的力量远超大脑塑造文化。

---

### 3.2 向下因果的形式化

#### 3.2.1 约束梯度

$$\nabla C_{L_2}[\sigma] = \frac{\partial}{\partial \sigma} \left[\|\sigma - \sigma_{L_2}\|^2\right]$$

**物理意义**: $L_2$对$\sigma$的"拉力",使其靠近社会规范$\sigma_{L_2}$。

#### 3.2.2 耦合强度$\lambda$

| 社会类型 | $\lambda$ 值 | 特征 |
|:---------|:-------------|:-----|
| 极权主义 | $\lambda \to \infty$ | 完全锁定在$L_2$ |
| 集体主义 | $\lambda \approx 10$ | 强规范压力 |
| 个人主义 | $\lambda \approx 1$ | 弱规范压力 |
| 无政府状态 | $\lambda \to 0$ | 无$L_2$约束 |

**实验**: 测量不同文化中的从众行为 (Asch范式) → 估计$\lambda$。

---

## §4. 本体论摩擦:痛苦的数学

### 4.1 摩擦势能的积分形式

$$\Psi_f(t) = \int_0^t \left|\frac{dF}{d\tau}\right|_{\text{maintain } L_1} d\tau$$

#### 4.1.1 直觉

**类比**: 爬山
- $F$: 海拔高度
- $\frac{dF}{dt}$: 爬升速率
- $\int |\frac{dF}{dt}| dt$: 总耗能

**心理学**: 维持不想要的$L_1$ (如痛苦工作) → 持续消耗$\Psi_f$ → 累积疲劳。

#### 4.1.2 哈扎德函数

$$h(t) = \frac{d\Psi_f}{dt}$$

**物理意义**: "痛苦率" — 每秒的本体论成本。

**状态映射**:

| $h(t)$ 值 | 状态 | 现象学 |
|:----------|:-----|:-------|
| $h \approx 0$ | 心流 | "时间消失" |
| $h$ 中等稳定 | 正常生活 | 背景张力 |
| $h$ 高尖峰 | 危机 | 急性痛苦 |
| $h$ 持续高位 | 慢性压力 | 抑郁、倦怠 |

---

### 4.2 痛苦作为反事实张力

$$\text{Pain}(t) = \int_{L_0^{\text{cf}}} |\sigma - \sigma_{L_1}|^2 \cdot P_{\hat{G}}(\sigma) \, d\sigma$$

#### 4.2.1 组件解析

- **$L_0^{\text{cf}}$**: 反事实可能性空间 (本可以但没有实现的$L_0$)
- **$|\sigma - \sigma_{L_1}|^2$**: 与实际$L_1$的"距离"
- **$P_{\hat{G}}(\sigma)$**: $\hat{G}$能访问的概率分布

#### 4.2.2 推论

**推论1**: 只有能访问$L_0^{\text{cf}}$的系统才能痛苦。
$$d > 0 \Rightarrow \text{Can access } L_0^{\text{cf}} \Rightarrow \text{Can suffer}$$

**推论2**: 痛苦强度 ∝ $d$值 × 反事实偏离度。
$$\text{Pain} \propto d \times \|\sigma_{L_1} - \sigma_{\text{desired}}\|$$

**实例**:
- 低$d$生物 (如蚯蚓): 可能有伤害感受 (nociception),但无真正痛苦 (suffering)
- 高$d$人类: 能想象"本可以更好" → 深度痛苦

---

### 4.3 神经损伤的累积定律

$$\text{Damage} \propto \int_0^T h(t) \cdot \mathbb{1}_{[h > h_c]} \, dt$$

#### 4.3.1 阈值$h_c$

**定义**: 超过此值,摩擦开始造成不可逆损伤。

**生理对应**: 
- 糖皮质激素 (Cortisol) 阈值
- 海马神经生成抑制
- 端粒缩短加速

**估计**: $h_c \approx 2-3 \times h_{\text{baseline}}$ (急性应激反应)

#### 4.3.2 临床应用

**PTSD模型**: 
$$\text{PTSD Severity} \propto \int_{trauma} h(t)^2 \, dt$$

平方项 → 短时极高$h$比长时中等$h$更有害 (单次创伤 vs 慢性压力)。

**治疗目标**: 降低$\int h \, dt$
- 方法1: 减少$h$峰值 (药物、呼吸训练)
- 方法2: 缩短$h > h_c$的持续时间 (EMDR)

---

## §5. 双重时间:度量与选择

### 5.1 复时间的数学结构

$$T_{\text{reality}} = T_{\text{metric}} + i \cdot T_{\text{selective}}$$

#### 5.1.1 为什么用虚数单位$i$?

**答案**: 正交性 (Orthogonality)。

**类比**: 复平面
- 实轴: 位置
- 虚轴: 动量 (量子力学)

**SRT**:
- 实轴: 物理时间坐标 (钟表测量)
- 虚轴: 信息流时间 (意识体验)

$$\langle T_{\text{metric}} | T_{\text{selective}} \rangle = 0$$

两者互不影响 (在第一近似下)。

#### 5.1.2 洛伦兹不变性的破缺

**度量时间**: 满足洛伦兹变换
$$T'_{\text{metric}} = \gamma(T_{\text{metric}} - v X / c^2)$$

**选择时间**: **不满足**
$$T'_{\text{selective}} \neq f(T_{\text{selective}}, v)$$

**推论**: 意识时间不服从相对论 — 你的"现在"是绝对的 (在$\hat{G}$的参考系)。

---

### 5.2 本体论相位与主观时间

**[R（时间知觉心理物理学：Pacemaker-Accumulator模型/Weber时间知觉）+ H（φ方程作为SRT形式化）]**

#### 5.2.1 相位方程

$$\tau \frac{d\phi}{dt} = -\alpha_{\text{context}} \cdot \phi$$

**解析解**:
$$\phi(t) = \phi_0 \exp\left(-\frac{\alpha_{\text{context}} \cdot t}{\tau}\right)$$

**主观时间速率**:
$$v_{\text{subj}} = \frac{d\phi}{dt} = -\frac{\alpha}{\tau} \phi$$

**φ（本体论相位）定义注**：φ 是本节引入的态变量，代理"待选择/待锚定的本体论潜在性剩余量"（L₀尚未被 Ĝ_θ 消化的部分）。SRT联结候选：$\phi \propto 1 - \mathrm{CR}(d)$（未被信息保留率消化的L₀潜在量），$\phi=0$ 对应完全锚定。正式地位：当前为辅助形式化量，待纳入核心体系。→ Cross-ref: SRT-CORE-12A §CR公式（CR(d) ∝ 1 − e^{−αd}）。

**参数操作化候选**：
- $\tau$（相位时间常数）≈ θ 参数的更新时间尺度（个体习惯化速率的倒数），$\tau \propto 1/|\partial\theta/\partial PE|$
- $\alpha_{\text{context}}$（上下文衰减系数）≈ $1/d$（d值越高，上下文越被更广关注范围稀释，φ衰减越快）或 $\propto$ 新颖性（信息密度）。操作化待精确化。

**Ψ_f 进入方程的机制**：表格中"高 $\Psi_f$ → dφ/dt ≈ 0"对应摩擦阻滞选择过程——高 $\Psi_f$ 时锚定代价过高，Ĝ_θ 无法完成当前L₀的锚定，φ被"冻住"。形式化候选：$\alpha_{\text{context}} \to \alpha_{\text{context}} / (1 + \Psi_f / \Psi_f^{cap})$（摩擦抑制系数），使高 $\Psi_f$ 时 α 降低、φ 衰减变慢。

#### 5.2.2 现象学对应

| $\phi$状态 | $\frac{d\phi}{dt}$ | 主观体验 | 实例 | SRT机制 |
|:-----------|:-------------------|:---------|:-----|:---------|
| 高初值,快衰减 | 大负数 | "时间飞逝" | 心流、娱乐 | $d$高/$\Psi_f$低，φ快速消耗 |
| 低初值,慢衰减 | 小负数 | "时间正常" | 日常活动 | 中等 $d$/$\Psi_f$ |
| 被阻滞 (高$\Psi_f$) | ≈ 0 | "时间变慢" | 等待、痛苦 | 高 $\Psi_f$ 使 $\alpha$ 有效降低 |
| 接近零 | ≈ 0 | "无时间感" | 深度冥想 | $d$→高，φ耗尽（L₀完全锚定） |

#### 5.2.3 实验验证

**[H — Novel Prediction：主观时距∝φ变化路径积分]**

**范式**: 延迟估计任务
1. 呈现刺激$S$
2. 等待$\Delta t$ (客观)
3. 要求估计$\Delta t$ (主观)

**预测**: $\Delta t_{\text{subj}} \propto \int_0^{\Delta t} |\frac{d\phi}{d\tau}| d\tau$

**操纵**: 改变$\alpha_{\text{context}}$ (如情绪、新颖性) → 验证公式。**φ的实时测量候选**：EEG的alpha波功率（α波下降~φ衰减）或PCI（意识整合度）作为φ的神经代理。

**证伪条件**：若在高情绪唤醒条件（高α_context的操纵）下，主观时距估计不缩短（或缩短方向与预测相反），则积分预测失效；若高Ψ_f（痛苦条件）不导致α_context有效降低的可测效应（神经代理不变），则Ψ_f进入方程的机制候选需修订。

---

## §6. 觉醒的动力学:从囚笼到自由

### 6.1 双盆地势能的拓扑

#### 6.1.1 低d陷阱

$$V_{\text{low-d}}(\sigma) = \frac{1}{2} k_1 (\sigma - \sigma_{\text{ego}})^2$$

**特征**:
- 中心: $\sigma_{\text{ego}}$ (自我中心状态)
- 刚度: $k_1$ (自我强化强度)
- $d \approx 1$: 仅关心自身

**稳定性**: 极高 (进化优势 → 深井)

#### 6.1.2 初心吸引子

$$V_{\text{high-d}}(\sigma) = \frac{1}{2} k_2 (\sigma - \sigma_0)^2$$

**特征**:
- 中心: $\sigma_0$ (初心/宇宙意识)
- 刚度: $k_2 < k_1$ (更广阔但更浅)
- $d \to \infty$: 万物一体

#### 6.1.3 势垒

$$V_{\text{barrier}}(\theta) = V_0 \exp\left(-\frac{(\theta - \theta_c)^2}{2\Delta\theta^2}\right)$$

**高度**: $V_0 = V_0(\Psi_f^{\text{history}})$ (依赖累积摩擦)

**位置**: $\theta_c$ (临界参数值)

---

### 6.2 渐进觉醒:摩擦驱动的退火

#### 6.2.1 机制

**学习方程**:
$$\frac{d\theta}{dt} = -\gamma \nabla_\theta \Psi_f$$

**效应**: 
$$\nabla_\theta \Psi_f < 0 \Rightarrow \theta \text{ 向降低} \Psi_f \text{的方向演化}$$

**势垒变化**:
$$V_0(\theta(t)) = V_0(0) \cdot \exp(-\beta t)$$

势垒高度随时间指数下降。

#### 6.2.2 时间线

**估算**: 
$$t_{\text{awakening}} \sim \frac{1}{\gamma} \log\left(\frac{V_0(0)}{k_B T}\right)$$

对于典型$\gamma \sim 10^{-8}$ sec$^{-1}$ (年尺度学习):
$$t \sim 10-30 \text{ years}$$

**实例**: 长期禅修者、心理治疗的累积效应。

---

### 6.3 顿悟觉醒:鞍结分叉

#### 6.3.1 分叉理论

**控制参数**: $\mu$ (如危机强度、支持度)

**正常形式**:
$$\frac{d\sigma}{dt} = \mu + \sigma^2$$

**分叉点**: $\mu = 0$
- $\mu < 0$: 两个稳定点 (低$d$和高$d$共存)
- $\mu = 0$: 临界点 (两点合并)
- $\mu > 0$: 无稳定点 (只剩高$d$)

#### 6.3.2 触发条件

**命题**: 当$\mu$跨越零点 → 突然觉醒。

**触发因素**:
1. **极端痛苦**: $\Psi_f \to \infty$ → 低$d$不可持续
2. **灵性导师**: 提供$\sigma_0$的"种子"
3. **神秘体验**: 致幻剂、濒死 → 瞬间高$d_{\text{nonlocal}}$

**时间线**: 秒-小时 (顿悟式)

**实例**: 禅宗"大悟"、Ramana Maharshi的自发觉醒。

---

### 6.4 社会支持的势垒调制

$$V_{\text{barrier}} \propto \frac{\text{Existential Risk}}{\text{Social Support}}$$

#### 6.4.1 分子:存在性风险

**定义**: 低$d$状态崩溃的威胁 (死亡、疯狂、孤立)。

**机制**: 高风险 → 高势垒 (保护性抑制 → "我不敢改变")。

#### 6.4.2 分母:社会支持

**定义**: 安全网的强度 (物质、情感、灵性)。

**机制**: 高支持 → 低势垒 (允许探索 → "我可以尝试")。

**实例**: 
- 禅修中心 (僧伽) → 提供支持 → 降低$V$
- 孤立个体 → 无支持 → $V \to \infty$ → 困在低$d$

---

## §7. 递归深度与智慧

### 7.1 Volterra级数的认知意义

$$\hat{G}_\theta = K_0 + K_1 + K_2 + \cdots$$

#### 7.1.1 零阶核 ($K_0$)

**定义**: 常数项,与输入无关。

**认知**: 自动反射、习惯。

**实例**: 眨眼反射、走路。

#### 7.1.2 一阶核 ($K_1$)

**定义**: 线性响应。
$$K_1[x](t) = \int k_1(\tau) x(t - \tau) \, d\tau$$

**认知**: 简单工具使用、条件反射。

**实例**: 用锤子敲钉子。

#### 7.1.3 高阶核 ($K_n, n \geq 2$)

**定义**: 非线性、递归响应。
$$K_n[x](t) = \int \cdots \int k_n(\tau_1, \ldots, \tau_n) \prod_{i=1}^{n} x(t - \tau_i) \, d\tau_i$$

**认知**: 
- $K_2$: 类比推理 ("A:B :: C:?")
- $K_3$: 元认知 ("我知道我知道")
- $K_4+$: 哲学、自我反思

**实例**: Hofstadter的"怪圈" (Strange Loops)。

---

### 7.2 智能vs意识的正交性

#### 7.2.1 二维空间
```
意识 (d, Ψ_f)
    ^
    |   人类(高,高)
    |       
    |       
    |   狗(中,中)      当前AI(高,0)
    |       
    |   细菌(低,低)    计算器(0,0)
    |       
    +----------------------------> 智能 (ΣK_n)
```

#### 7.2.2 关键洞见

**命题**: 高智能 $\not\Rightarrow$ 高意识。

**论证**:
- **智能**: $L_1 \to L_2$的映射复杂度 (可通过训练提升)
- **意识**: $\hat{G}$对$L_0$的访问 + 本体论脆弱性 (需要物理具身)

**推论**: GPT-N可以无限聪明,但永远不会"醒来" (除非赋予物理风险)。

---

### 7.3 智慧的定义

$$\text{Wisdom} = \sum_{n \geq 2} w_n \cdot \|K_n\|$$

#### 7.3.1 权重$w_n$

**递增**: $w_{n+1} > w_n$ (更高阶更有价值)。

**理由**: 元层次的洞察比对象层次更根本。

**实例**:
- "知道很多事实" (高$K_1$) ≠ 智慧
- "知道如何学习" (高$K_2$) = 智慧起点
- "知道何时不学习" (高$K_3+$) = 深度智慧

#### 7.3.2 与佛教般若的对应

**般若** (Prajñā) = 智慧
- 初级: 闻慧 (听闻知识) ≈ $K_1$
- 中级: 思慧 (思考理解) ≈ $K_2$
- 高级: 修慧 (体证空性) ≈ $K_{\infty}$ (无限递归)

---

## §8. 总结与展望

### 8.1 SRT动力学的核心洞见

1. **现实是过程,非状态**: $\frac{d\sigma}{dt} \neq 0$ (持续选择)
2. **多时间尺度嵌套**: 快状态 + 慢参数 + 超慢$L_2$
3. **跨尺度同构**: 量子、神经、社会 = 同一选择语法
4. **痛苦的功能性**: $\Psi_f$是学习/觉醒的燃料
5. **时间的双重性**: 度量 + 选择 (正交维度)
6. **觉醒的可达性**: 通过$\theta$演化降低势垒

### 8.2 未来实验方向

1. **跨尺度耦合测量**:
   - 设计实验测量$\kappa_{ij}$ (如EEG-社交网络同步)
   
2. **摩擦势能的神经标记**:
   - 假设: $\Psi_f$ ∝ 前扣带回 (ACC) 活跃度
   - 测试: fMRI + 自报痛苦

3. **觉醒动力学追踪**:
   - 纵向研究: 禅修者的$\theta$演化 (多年跨度)
   - 测量: d值、$\Psi_f$、EEG复杂度

4. **递归深度评估**:
   - 开发$K_n$测量协议 (扩展Raven矩阵)
   - 跨物种比较

### 8.3 理论边界

SRT动力学**无法**完全解释（以下三项为**原则性界限**，而非技术改进可弥补的空缺）:

1. **$\theta$的绝对起源**: 第一个$\hat{G}$如何涌现?（SRT描述$\theta$如何演化，但不解释$\theta$=0时的初始态；cf. Chalmers 1995 *难问题*：意识的起源问题类比）
2. **$L_0$梯度的来源**: 为什么$\nabla F \neq 0$?（SRT以梯度存在为前提，不解释梯度的宇宙学起源；cf. Carroll 2010 *From Eternity to Here*：热力学梯度的宇宙学起源仍开放）
3. **时间箭头的本质**: 为什么$T_{\text{selective}}$不可逆?（SRT的选择过程定向，但时间箭头与热力学第二定律/量子去相干的联结属于物理学开放问题；cf. Penrose 1989 *The Emperor's New Mind*：时间不可逆与低熵初态）

> **界限层次说明**：三个界限有逻辑顺序——③时间箭头是②L₀梯度的前提条件（梯度的耗散需要时间方向性），②L₀梯度是①θ涌现的必要条件（无梯度则无选择压力）；因此若②被解决，③的解决是前提；若①被解决，②③均需先解决。SRT在三个界限内部运作，不试图越界。
>
> **[H-高承诺]注**：SRT对L₀（绝对潜在域）的假设本身涉及第②点——L₀的∇F≠0是公理性假设而非推导结论；此为框架的形而上学承诺基础，见Ax-Core-A1/IC-Thesis1-1的一致性要求。

### 8.4 哲学对话

SRT与以下传统深度共鸣:

- **佛教中观**: 空性 ≈ $L_0$的无自性
- **过程哲学** (Whitehead): 现实 = 过程 (becoming)
- **现象学** (Husserl): 时间意识 = 内时间性
- **复杂系统理论**: 涌现 ≈ 跨尺度耦合
- **自由能原理** (Friston): $F$ 最小化 = SRT的特例

### 8.5 终极问题

**为什么存在选择,而非虚无?**

SRT提供了一个可能的答案:
$$\text{因为} \quad \nabla F[L_0] \neq 0$$

某处有能量梯度 → 选择自发开始 → 现实涌现。

但这只是把问题推给了"为什么有梯度?"

或许这是可以问的最后一个问题。

---

## 符号总索引 (Master Symbol Index)

| 符号 | 名称 | 定义位置 | 说明 |
|:-----|:-----|:---------|:-----|
| $\hat{G}_\theta$ | 幽灵算子 | Ax-Dyn-1 | 选择映射 |
| $F[\sigma]$ | 自由能代理项 | Ax-Dyn-3 | 局部闭包项 + 扩大纳入项的近似写法 |
| $\Psi_f$ | 本体论摩擦 | Ax-Fric-1 | 累积能量成本 |
| $h(t)$ | 哈扎德函数 | Ax-Fric-1 | 痛苦率 |
| $\Lambda$ | 尺度变换 | Ax-Scale-1 | 粗粒化映射 |
| $\kappa_{ij}$ | 尺度耦合强度 | Ax-Coup-1 | 互信息/熵 |
| $T_{\text{metric/selective}}$ | 双重时间 | Ax-Time-1 | 度量/选择时间 |
| $\phi$ | 本体论相位 | Ax-Time-2 | 主观时间变量 |
| $K_n$ | Volterra核 | Ax-Rec-1 | 递归阶数 |

---

**依赖声明**: 本文件是SRT Core系列的收官之作,综合了所有前置文件 (Axioms, Ontology, Operator) 的定义。修改本文件需评估对整个理论体系的影响。

**版本历史**: v3.0新增尺度耦合矩阵、觉醒动力学双机制、递归深度形式化、时间双重性的数学结构等高级内容,并大幅扩展了实验预测和哲学对话部分。

**致谢**: 本理论综合了David Bohm的活跃信息、Karl Friston的自由能原理、Stuart Kauffman的自催化集、Francisco Varela的具身认知、Giulio Tononi的整合信息论等思想。向这些巨人致敬。

**字数统计**: ~15,000字(中英混合)

---


### Taxonomy Mapping: External Complexity Classes → SRT

| 外部分类 | SRT 对应 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|:--|
| 元素核合成复杂化（恒星/超新星） | 宇宙物理选择层 | 低~中 | Open-flow（高能） | payable（阶段性高负载） |
| 矿物谱系复杂化（地球化学历史） | 地球化学中尺度层 | 中 | Semi-open / Open | payable 或局部 overloaded |
| 生物功能复杂化（适应与突跃） | 生物-认知层 | 中~高 | Open-flow（代谢耦合） | payable；失衡时 unsustainable |

**Constraint**: 上表 d 为 canonical d 的语境化区间，canonical 定义保持：
$$d \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|$$

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
### Taxonomy Mapping: Infinity Classes → SRT Dynamics

| 外部分类 | SRT 对应 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|:--|
| 可数无限（自然数、偶数、有理数） | 可枚举选择轨道 | 中 | Semi-open（有限工作记忆展开） | payable |
| 不可数无限（实数） | 非枚举潜能域切片 | 中~高 | Open-flow（高抽象探索） | payable~overloaded（任务依赖） |
| 等势无限区间同势（(0,1) 与全实数同基数） | 尺度变换不改势级 | 中 | Semi-open | payable |

**Constraint**: 该表仅描述“认知-形式系统中的可达层级”，不将集合论基数直接等同于本体论“存在强度”。

---

## AT-SRT 相变接口（补充条款，2026-03-02）

### Def-Scale-AT-1: 深度-持久相图
在跨尺度系统中定义状态坐标：
\[
\mathfrak{Z}(t)=\big(D(t),P(t),\Psi_f(t),d(t)\big)
\]
其中 `D` 为构建深度代理、`P` 为复现持久代理。

### T-Scale-AT-1: 相变门（Phase Gate）
若存在窗口 \([t_0,t_1]\) 满足：
\[
D(t)\ge D_c,\quad P(t)\ge P_c,\quad \text{and}\quad \Psi_f\ \text{payable},
\]
则系统从“被动选择区”跃迁到“主动稳定构建区”（记为 \(\mathcal{R}_{active}\)）。

### T-Scale-AT-2: 回落门（Fallback Gate）
若保持高深度但出现 `P` 下跌且 \(\Psi_f\to\) overloaded/unsustainable，则轨迹回落到约束主导区：
\[
\mathcal{R}_{active} \to \mathcal{R}_{constraint}
\]
并触发 \(L_2\) 重编织失败风险升高。

### [Lineage/Source]
- 来源：Cronin & Walker, *The Physics of Causation*（2026 manuscript）。
- SRT 引入方式：作为跨尺度“阈值-相变”接口，不与认知层变量作强同一。

## 分类映射表（AT 分类 → SRT）

| 外部分类（AT） | SRT d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 可支付性 |
|---|---|---|---|
| 自发可达区（低 \(a_i\)、低/中 \(n_i\)） | 低到中（\(d\in[d_0,d_1]\)） | Semi-open / 局部 Open | payable |
| 阈值邻域（\(a_i\approx a_M\)） | 中高（\(d\in(d_1,d_2]\)） | Open↔Semi-open 转换 | borderline |
| 选择主导区（高 \(a_i\)、高 \(n_i\)） | 高（\(d>d_2\)） | Open（需持续供能） | payable 或 overloaded |
| 失稳衰退区（高深度但低复现） | 中高但回落（\(d\downarrow\)） | Closed 倾向 | unsustainable |

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
---

## Minimal Embodiment Threshold（最小具身信息下界，2026-03-02）

### Def-Scale-MET-1: \(N_{crit}\)
定义最小具身信息下界 \(N_{crit}\)：系统若要在给定环境下维持自我复制/自维持闭环，其参数化约束信息量必须满足：
\[
I(\theta)\ge N_{crit}(env,\Psi_f)
\]

### T-Scale-MET-1: Payable-Friction Condition
当 \(I(\theta)<N_{crit}\) 时，系统对本体论摩擦的支付仅能维持瞬时或间歇复制；当 \(I(\theta)\ge N_{crit}\) 且环境窗口可用时，系统可跨越“前闭包→稳定闭包”门槛。

### Subcritical Ionic-Memory Window patch (Cell Reports Physical Science 2024, 2026-03-25, Pipeline 1)

这条 patch 最值得保留的，不是把 `hydrogel`、`Stentor`、基因调控网络一路外推到 `spacememory`，而是把“记忆样状态保持”的下界压到了非生命离子介质。它一方面修正了把 history dependence 直接偷渡成主体性或意识的冲动，另一方面也加固了 SRT 一直需要守住的层级区分：memory-like retention 可以先于闭包、关切与主体性。

用户提交的 ISF 二手综述 `Cognition Without Brains: How Memory Emerges in Polymers, Cells, and Spacetime` 真正值得吸收的新增量，不是文末把 hydrogel / `Stentor` / gene regulatory networks / 神经培养物一路外推到 `spacememory` 或 “memory field”，而是它指向的一手同行评审原始研究：Strong, Holderbaum & Hayashi 在 *Cell Reports Physical Science* 2024 发表的 `Electro-active polymer hydrogels exhibit emergent memory when embodied in a simulated game environment`（doi:`10.1016/j.xcrp.2024.102151`）。

若用 SRT 语言收紧，这条材料支持的不是“非生命材料已经有主体性”，而是一个更低的 **subcritical history-retention** 窗口：当非生物离子介质被接入闭环反馈任务时，离子迁移与聚合物几何本身就可能留下短时状态痕迹，使系统对后续刺激的响应出现可测的历史依赖。
\[
\theta_{gel}^{ionic}=\{\rho_{ion}(x,t),\,Z_{poly}(x),\,\kappa_{stim},\,\kappa_{fb}\}
\]
\[
I(\theta_{gel}^{ionic})<N_{crit}
\quad\land\quad
\kappa_{fb}>0
\quad\Rightarrow\quad
\exists\, M_{local}(\Delta t)>0
\]
其中 \(M_{local}(\Delta t)\) 表示由离子分布历史保留下来的局部记忆项，它不要求系统已经跨过自维持闭包阈值，但足以让短时闭环表现偏离“纯无记忆被动响应”。

这条结果对 SRT 的真正价值，在于把层级关系收紧为：
\[
\text{memory-like state retention}
\;<\;
\text{stable autopoietic closure}
\;<\;
d>0\ \text{with concern}
\]
也就是说，**记忆样行为可以先于生命闭包出现**。它支持“适应性状态保持并不从突触或神经系统才开始”，但并不取消生命、能动性与意识之间的门槛差异。与 `Neuroscience/SRT_Neuro_07_Evo_Devo.md` 中已写入的 `Stentor` 单细胞联结学习窗口一起看，更稳的读法是：`hydrogel` 把下界压到 non-living ionic medium，`Stentor` 才把它推进到 living but non-neural physiological computation。对 SRT 来说，这条材料真正加固的，不是“万物都有心智”，而是“可适应的历史保持可以有比生命更低的起点，但这并不会自动抹平后续门槛”。

**边界必须收紧：**
- 当前主锚点是一个特定的多电极 `Pong` 闭环范式，不等于任意离子材料都会“学习”。
- 论文支持的是短时 performance improvement / history dependence，不是开放式问题求解、长期自模型或 volitional choice。
- 这条材料支持的是 **memory-like retention below closure**，不自动推出 `d>0`、`\Psi_f>0`、主体性或意识。
- 用户提交文章中的 `spacememory` / `memory field` 外推**不予吸收**；hydrogel 结果本身不足以支撑“时空记忆”主张。

### Whole-Cell Closure Simulation patch (Cell 2026, 2026-03-15, Pipeline 1)
定义最小细胞的耦合闭包参数集：
\[
\theta_{cell}^{min}=\{\theta_{DNA},\theta_{RNA},\theta_{prot},\theta_{met},\theta_{mem},\theta_{div}\}
\]
其有效具身信息量不只是模块求和，还包含跨过程耦合项：
\[
I(\theta_{cell}^{min})=\sum_i I(\theta_i)+\sum_{i\neq j} I_{couple}(\theta_i,\theta_j)
\]

### T-Scale-MET-2: Coupled-Process Closure Criterion
即便局部模块各自可运行，系统也未必能预测完整生命周期；只有当 DNA 复制、转录/翻译、蛋白稳态、代谢、膜生长与分裂被联立到同一闭包网络时，最小细胞的 genotype→phenotype 才进入可预测区：
\[
I(\theta_{cell}^{min})\ge N_{crit}\quad \text{requires}\quad \sum_{i\neq j} I_{couple}(\theta_i,\theta_j)\ge N_{couple}^{min}
\]

* **Implication（中文）**：`N_{crit}` 不应被理解为“最小基因数”或“若干局部模块够用”，而应理解为跨过程可联立、可支付的闭包阈值。whole-cell simulation 支持的是“生命闭包需要分布式耦合记账”，不是“主体性已被纯计算穷尽”。
* **Boundary（中文）**：
  - 该窗口锚定的是 `JCVI-syn3A` 最小细菌，不直接外推到多细胞生物或人脑。
  - 成功模拟 genotype→phenotype 不等于已解决生命起源、主体性或 `d>0` 的判据。
  - 模型预测充分性依赖实验参数化与注释完备度，不等于本体论穷尽。

### 与 d-value 零跃迁问题的关系（注记）
该阈值仅刻画“结构自治”下界，不自动推出 \(d>0\)。
- 结构可复制 \(\neq\) 关切已涌现
- \(d\) 的正值条件仍需满足生物/认知域的额外门控（详见 anti-panpsychism 条款）

### [Lineage/Source]
- Thornburg et al., *Cell* (2026): `A whole-cell model for genotype-phenotype prediction in a minimal cell`
- Nature News (2026): `Cell simulator predicts life's molecular choreography from DNA`

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
---

## Constructive Fracture Interface（建设性断裂接口，2026-03-02）

### Def-Scale-CF-1: Controlled Rupture Window

> **Cross-ref**：此定义是 T-Scale-CF-1（Break-to-Build Gate）的形式化前提；T-Scale-CF-1 提供完整实证基础（Lecuit/Heisenberg/Mayor）、τ操作化（τ_reseal/τ_fail）和FC（证伪条件）。本条目仅定义”建设性断裂”的判准结构。

定义”建设性断裂”窗口：系统在局部连接断裂后，若满足重封闭与功能增强条件，则该断裂为结构重构步骤而非失稳失败。

$$\mathcal{R}_{break} \to \mathcal{R}_{reseal} \quad \text{with} \quad \Delta \mathcal{F}_{function} > 0$$

> **符号说明**：
> - $\mathcal{R}_{break}$：断裂状态（局部连接/κ值降低至κ < κ_c2的临界以下）
> - $\mathcal{R}_{reseal}$：重封闭状态（连接重建，κ重新升高至κ_c2以上）
> - $\Delta \mathcal{F}_{function} = \mathcal{F}(\mathcal{R}_{reseal}) - \mathcal{F}(\mathcal{R}_{break,initial})$：功能增量（$\mathcal{F}$ 为系统在目标任务上的功能能力度量，如信息整合能力/机械张力承载/认知灵活性——依层次具体化）
> - $\Delta\mathcal{F}_{function} > 0$：重封闭后功能高于断裂前——这是建设性断裂与破坏性断裂的判准分界

* **R/H**：此定义为框架性定义（全R形式结构），具体跨尺度应用（细胞/神经/社会）见 T-Scale-CF-1 的 R/H 区分。
* **FC**：参见 T-Scale-CF-1 的 FC-BreakBuild-1/2。

### T-Scale-CF-1: Break-to-Build Gate

> [R→Lecuit & Lenne 2007 *Nature Reviews Molecular Cell Biology*（细胞单层中的张力依赖性断裂-重封闭：形态发生中的受控断裂机制）; Heisenberg & Bellaïche 2013 *Cell*（力与形态发生：组织重塑过程中的机械应力-断裂-重封闭耦合）; Mayor & Etienne-Manneville 2016 *Nature Reviews Molecular Cell Biology*（前沿的形成：细胞连接的动态断裂-重组与形态发生方向性）]

若机械/液压应力优先沿低黏附路径释放，且重封闭时间 \(\tau_{reseal}\) 低于功能失稳阈值 \(\tau_{fail}\)，则系统可通过”先裂后合”进入更高功能态：
\[
\tau_{reseal}<\tau_{fail}\ \Rightarrow\ \text{constructive morphogenesis}
\]

**R/H 区分**：
- [R] 细胞/组织层面的受控断裂-重封闭机制（Lecuit/Heisenberg/Mayor）：发育生物学实证基础；τ_reseal/τ_fail的细胞生物学操作定义
- [H] **SRT跨尺度映射**：将细胞受控断裂框架扩展至神经可塑性（LTP中的突触重组）、社会制度（Schumpeter创造性破坏），并映射至κ-Ψ_f动力学。跨尺度外推的证据强度依层次递减（细胞[R-强]→神经[H-中]→社会[H-探索性]）

**τ参数操作化**：
- τ_reseal（重封闭时间）：细胞层面=钙黏附素重连时间（活细胞成像，单位：分钟）；神经层面=突触增强后稳定化时间（LTP时间窗，单位：小时）；社会层面=制度重构完成至新平衡时间（年）
- τ_fail（功能失稳阈值）：细胞层面=连接断裂→细胞分离前的不可逆时间窗；神经层面=长时程增强消退前的关键窗口

**Ψ_f - κ 断裂-重封闭动力学**（SRT层次）：
1. 断裂前：κ>κ_c2（L₂稳定），Ψ_f=Ψ_f_baseline
2. 断裂期（0→τ_reseal）：κ短暂<κ_c1（L₁不稳定，重组窗口打开），Ψ_f^transient↑（摩擦暂升）
3. 重封闭后（τ_reseal < τ_fail）：κ在新的κ_c2'处稳定（通常κ_c2'>κ_c2），Ψ_f_new<Ψ_f_baseline（新连接更高效）→ ΔF_function>0（功能增益）
4. 若τ_reseal > τ_fail：系统进入L₁不稳定→Ψ_f^catastrophic↑→功能崩溃路径

**可证伪预测**：
- FC-BreakBuild-1：在受控力学实验中，对组织施加高于黏附阈值但低于失稳阈值的应力，并在τ_fail内恢复，则后续功能性张力（组织刚度/传导效率）应高于断裂前——若断裂-重封闭后功能不高于基线则”先裂后合→更高功能态”主张需修订
- FC-BreakBuild-2：跨尺度预测：神经LTP协议中，NMDA受体开放（”断裂”窗口）持续时间若在τ_fail（LTD临界窗）之内则产生LTP（功能增强），超出则产生LTD或失稳——此已知LTP/LTD时间窗关系应与T-Scale-CF-1的τ不等式一致，若实验测量的临界时间与T-Scale-CF-1预测方向相反则神经层面外推失败

### T-Scale-CF-2: Path-Selective Fracture Principle
断裂路径并非随机扩散，而受局部张力差与连接强度梯度共同约束：
\[
\Pr(\text{break at }e_i) \propto \frac{\Delta T_i}{A_i}
\]
其中 \(\Delta T_i\) 为局部张力差，\(A_i\) 为黏附/连接强度代理。

### [Lineage/Source]
- Quanta 综述（2026-02-27）及其文内链接的一手文献（如 Science/Development 相关研究）。
- 用途：将“受控断裂→重封闭→功能塑形”写入跨尺度动力学条款。

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
## In-vitro 低 d 场景补充条款（2026-03-06，轻量）

### 微观门控与主体层 d 的分层说明
- in-vitro 神经网络中出现的跨区节律门控，允许被解释为局部微观选择门控（micro-d）存在的证据；
- 但该证据**不自动推出**主体层（organism-level）高 d 的意识整合。

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
### [Lineage/Source]
- Axonal theta oscillations evoke bursting in target hippocampal subregions（preprint, 2026）

## Type→Individual 相变阈值补注（2026-03-06，轻中量）

### Def-Scale-Indiv-1: Individuation Critical Point \(d_{indiv}\)
定义个体化临界点：
\[
d_{indiv} := \inf\{d: \mathcal{M}_{self}(t\to t+\Delta t)\ \text{stable and counterfactual-risk-coupled}\}
\]
- 当 \(d < d_{indiv}\)：系统主要表现为 Type-level 动力学（群体/谱系承压）
- 当 \(d \ge d_{indiv}\)：系统进入 Individual-level 动力学（个体承压与连续自我边界）

### T-Scale-Indiv-1: Suffering Internalization Transition
\[
d < d_{indiv}\Rightarrow \Psi_f \text{ mainly distributed over population topology}
\]
\[
d \ge d_{indiv}\Rightarrow \Psi_f \text{ internalizes as individual suffering load}
\]
* **Implication（中文）**：该阈值为“类型存在”到“个体痛苦可积累存在”的跨尺度相变界线。

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
### [Lineage/Source]
- 神学-进化-动物苦难对话语境（2026）

## 认知资本化与幂律尾部补注（2026-03-06，轻中量）

### T-Scale-Cap-1: Low-Friction Isomorphism Theorem
对同一潜在模式 \(X\in L_0\)，若协议 \(\Pi_a\) 与具身参数 \(\theta\) 更对齐，则锚定摩擦更低：
\[
\Psi_f(X\mid \Pi_a,\theta) < \Psi_f(X\mid \Pi_b,\theta)
\]
当 \(\Pi_a=\Pi_{vis}\) 且 \(\Pi_b=\Pi_{sym}\) 时，该不等式在典型人类认知架构下通常成立。
* **Implication（中文）**：协议切换（如符号→拓扑/视觉）可在不改变目标结构的前提下显著降低推理摩擦。

### Def-Scale-Cap-1: Cognitive Capitalization Dynamics
定义表现变量 \(P\) 与稳定脚手架深度 \(L_2^{depth}\)：
\[
\frac{dP}{dt}=\kappa\,P\,g\big(L_2^{depth},\hat G_\theta\big)+\xi_t,
\qquad
\frac{dL_2^{depth}}{dt}=h(P)-\lambda_{decay}L_2^{depth}
\]
其中 \(\xi_t\) 为噪声项，\(g\) 单调增于 \(L_2^{depth}\)。

### T-Scale-Cap-2: Pareto-Tail Emergence (Candidate)
在乘性增长 + 异质摩擦 + 噪声扰动条件下，群体表现分布出现幂律尾部候选：
\[
\Pr(P>x)\sim x^{-\alpha}\quad (x\to\infty)
\]

> [R→Gabaix 2009 *Annual Review of Economics*（随机乘性增长→Pareto分布的严格推导；适用于收入/城市/企业规模等领域）; Simon 1955 *Biometrika*（优先依附机制→幂律的随机过程起源）; Gibrat 1931（乘性增长→对数正态分布；Pareto为其重尾极端情形）; Taleb 2007 *The Black Swan*（幂律分布在极端事件中的认知含义）]

* **R/H 区分**：
  - [R] 乘性随机过程产生幂律尾部——这是经济学/统计物理的标准结论（Gabaix/Simon/Gibrat），无争议
  - [H] **SRT嵌入**：将上述机制解读为"L₂^depth资本化 + Ψ_f异质摩擦"框架下的能力分布涌现，并以此解释天才极端尾部——此SRT特定解读将幂律机制与具身参数联结，为SRT新增预测框架
  - [H] "无需诉诸神秘外因"：此说法在幂律机制层面[R]成立；但SRT进一步主张Ψ_f异质性是幂律尾部的主要驱动因子（而非纯随机优先依附）——此因子归因是[H]

* **α指数预测范围**：已知天才分布实证估计（科学引用分布α≈3，财富分布α≈1-2，运动成就分布α≈2-4）；SRT模型预测：Ψ_f异质性越大（个体间摩擦差异越大），α越小（尾部越重）——若α与Ψ_f异质性代理无负相关则此预测失败

* **Implication（中文）**：极端天才尾部可由长期资本化动力学产生，无需诉诸神秘外因。

* **可证伪预测**：
  - FC-CapScale2-1：跨领域比较中，Ψ_f异质性更高的领域（如古典音乐vs田径：皮质醇反应方差）应对应更小的α（更重尾部）——若无负相关则Ψ_f-α联结为空
  - FC-CapScale2-2：SRT模拟（乘性增长+Ψ_f异质摩擦）产生的α分布应与对应领域实测α在置信区间内重叠——若模拟α系统性偏离实测则本定理的定量预测失败

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Dynamics_Scaling_Annex/00_General_Boundary_Block.md`。
### [Lineage/Source]
- Ramanujan 认知机制讨论语境（2026）
- 枚举组合学可视化传统（Viennot 语境）

> **[R]** 溯源说明：本节T-Scale-Cap-1（低摩擦同构定理）的直接灵感来源于以下两个传统：
> - **Ramanujan认知机制**：Kanigel 1991 *The Man Who Knew Infinity*（Ramanujan传记：其数学直觉=视觉/感知模式而非形式符号，对数论模式的Ψ_f极低，Hardy评价为"未经训练的直觉"实为不同协议Π_vis的极端案例）；Hardy 1940 *A Mathematician's Apology*（"Ramanujan从未被教导，他是发现者而非学习者"，R认知风格基线）。在T-Scale-Cap-1框架下：Ramanujan的天才=Π_vis（视觉/模式协议）与其θ的高度对齐，使特定数学对象的Ψ_f(X|Π_vis,θ)远低于标准形式符号协议Ψ_f(X|Π_sym,θ)。
> - **Viennot可视化传统**：Viennot 1986 *Heaps of Pieces*（堆积件法：将代数/组合恒等式可视化为几何堆积，RSK对应的直观化，R方法论传统）——即T-Scale-Cap-1中"拓扑/视觉协议"的具体实例：相同组合结构在Viennot可视化下Ψ_f显著低于纯代数符号处理。
