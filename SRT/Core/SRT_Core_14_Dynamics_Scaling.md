---
id: SRT-CORE-14
type: dynamics
tags: [Scaling, Isomorphism, Fractal, Hybrid]
status: axiomatic_hybrid_v1
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
# Part A: Formal Axioms (形式化公理)


## I. Cross-Scale Isomorphism (跨尺度同构)

### Ax-Scale-01: Self-Similar Selection
**Formal Definition**: Selection operators across scales are isomorphic under renormalization.
$$\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}$$
* **Implication**: 量子坍缩、神经决策与社会选择共享同一拓扑逻辑。

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

## 【理论边界/防误用声明】
- 不采纳“适应度优先=真理无意义”的推论：SRT 主张的是资源约束下的近似策略，不是否定真值结构。
- 不采纳“界面可构造=可任意构造”的推论：外部阻抗地形通过 \(\Psi_f\) 客观限制可行结构。

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

**标准自由能** (Friston):
$$F = E - TS$$

**SRT扩展** (含利他项):
$$F = E - TS - d \cdot U_{\text{others}}$$

#### 1.3.2 d值效应的显著性

**低d** ($d \approx 1$):
$$F \approx E - TS \quad \text{(纯自私)}$$

最小化$F$ → 最大化自身生存/舒适。

**高d** ($d \gg 1$):
$$F \approx -d \cdot U_{\text{others}} \quad (E, TS \text{ negligible})$$

最小化$F$ → 最大化他者福祉 (甚至牺牲自我)。

**实例**:
- 母亲舍命救子 → $d_{\text{kin}} \to \infty$ (亲缘$d$)
- 利他主义者 → $d_{\text{universal}} \gg 1$
- 自恋者 → $d \approx 1$

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

#### 5.2.1 相位方程

$$\tau \frac{d\phi}{dt} = -\alpha_{\text{context}} \cdot \phi$$

**解析解**:
$$\phi(t) = \phi_0 \exp\left(-\frac{\alpha_{\text{context}} \cdot t}{\tau}\right)$$

**主观时间速率**:
$$v_{\text{subj}} = \frac{d\phi}{dt} = -\frac{\alpha}{\tau} \phi$$

#### 5.2.2 现象学对应

| $\phi$状态 | $\frac{d\phi}{dt}$ | 主观体验 | 实例 |
|:-----------|:-------------------|:---------|:-----|
| 高初值,快衰减 | 大负数 | "时间飞逝" | 心流、娱乐 |
| 低初值,慢衰减 | 小负数 | "时间正常" | 日常活动 |
| 被阻滞 (高$\Psi_f$) | ≈ 0 | "时间变慢" | 等待、痛苦 |
| 接近零 | ≈ 0 | "无时间感" | 深度冥想 |

#### 5.2.3 实验验证

**范式**: 延迟估计任务
1. 呈现刺激$S$
2. 等待$\Delta t$ (客观)
3. 要求估计$\Delta t$ (主观)

**预测**: $\Delta t_{\text{subj}} \propto \int_0^{\Delta t} |\frac{d\phi}{d\tau}| d\tau$

**操纵**: 改变$\alpha_{\text{context}}$ (如情绪、新颖性) → 验证公式。

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

SRT动力学**无法**完全解释:

1. **$\theta$的绝对起源**: 第一个$\hat{G}$如何涌现?
2. **$L_0$梯度的来源**: 为什么$\nabla F \neq 0$?
3. **时间箭头的本质**: 为什么$T_{\text{selective}}$不可逆?

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
| $F[\sigma]$ | 自由能 | Ax-Dyn-3 | 含利他项 |
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
- 不采纳“复杂度无条件单调上升”的推论。
- 不采纳“功能信息可替代热力学熵”的推论。
- 边界：SRT 仅支持“能流开放 + 选择记忆 + 摩擦可支付”条件下的复杂度漂移。


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
1. 本接口不意味着“心理层面可绕过物理可达边界”。
2. AT 的对象层因果阈值与 SRT 的认知层相变阈值是**映射关系**，非同一对象。
3. 使用本接口时必须同步报告适用尺度（微观/生物认知/社会制度）。

---

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

## Constructive Fracture Interface（建设性断裂接口，2026-03-02）

### Def-Scale-CF-1: Controlled Rupture Window
定义“建设性断裂”窗口：系统在局部连接断裂后，若满足重封闭与功能增强条件，则该断裂为结构重构步骤而非失稳失败。
\[
\mathcal{R}_{break}\to\mathcal{R}_{reseal}\quad \text{with}\quad \Delta \mathcal{F}_{function}>0
\]

### T-Scale-CF-1: Break-to-Build Gate
若机械/液压应力优先沿低黏附路径释放，且重封闭时间 \(\tau_{reseal}\) 低于功能失稳阈值 \(\tau_{fail}\)，则系统可通过“先裂后合”进入更高功能态：
\[
\tau_{reseal}<\tau_{fail}\ \Rightarrow\ \text{constructive morphogenesis}
\]

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
1. 不采纳“任何断裂都是进步”的推论；仅在重封闭与功能增益同时成立时定义为建设性断裂。
2. 不采纳“材料裂纹模型可无改造直接套用活体组织”的推论；活体系统需引入主动调控与反馈项。

## In-vitro 低 d 场景补充条款（2026-03-06，轻量）

### 微观门控与主体层 d 的分层说明
- in-vitro 神经网络中出现的跨区节律门控，允许被解释为局部微观选择门控（micro-d）存在的证据；
- 但该证据**不自动推出**主体层（organism-level）高 d 的意识整合。

## 【理论边界/防误用声明】
- 不采纳“出现跨区节律门控 = 已满足高 d 主体级认知整合”的推论。
- 不采纳“体外重组网络的协调性可直接等同于完整具身闭环意识”的推论。
- 适用边界：该类证据用于支持微观机制桥接，不替代行为层、具身层与长期稳定性的联合验证。

### [Lineage/Source]
- Axonal theta oscillations evoke bursting in target hippocampal subregions（preprint, 2026）
