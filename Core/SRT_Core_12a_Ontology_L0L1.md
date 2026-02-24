---
id: SRT-CORE-12A
type: definition
tags: [L0, L1, Ontology, Ruliad, Gauge Field, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-BRIDGE]
---

# SRT Ontology I: The Latent & The Manifest (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Ontology (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的首个“Formal Axioms”分段；若存在双 Part 结构，后续重复分段不纳入 final。
- Part B 以 `claude` 为来源，并用原版 `Core` 标题与主旨做语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## I. L_0: The Latent Domain (潜在域)

### Ax-L0-01: Absolute Source & Domain Realizations
**Formal Definition**: The absolute latent domain ($L_0^{abs}$) is the unconditioned totality prior to any formal structure. Its mathematical realizations are domain-specific projections.
$$L_0^{abs} \supseteq (\mathcal{A}/\mathcal{G}) \cup \text{Ruliad}$$
$$L_0^{phys} \cong \mathcal{H}, \quad L_0^{gauge} \cong \mathcal{A}/\mathcal{G}, \quad L_0^{comp} \cong \text{Ruliad}$$
* **Implication**: 潜在域的绝对身份（$L_0^{abs}$）先于一切数学结构，不可被任何单一形式系统穷尽。模空间与 Ruliad 的并集是其在物理-计算 $L_2$ 框架下的最佳近似，而非等价定义。各领域数学实现之间的拓扑不兼容性（线性 vs 离散 vs 超验）是 $L_0^{abs}$ 不可穷尽性的预期结果。
* **Consistency Note**: 与 T-Trad-2（否定神学界限定理）一致：$\forall P \in L_1$, $P$ cannot fully capture $L_0$。

### Ax-L0-02: Conservation of Possibilia
**Formal Definition**: The total information content of the latent domain is invariant.
$$\frac{d}{dt}H(L_0) = 0$$
* **Implication**: 创新不是从无到有的创造，而是对潜能的照明与再组织。

### T-L0-01: Innovation as Illumination
**Deductive Statement**: New manifest structures are re-selections of conserved latent patterns.
$$\text{Innovation} = \text{Discovery}(L_0^{previously\_shadowed})$$
* **Implication**: 任何“新事物”都对应于潜在域中被重新选择的结构。

### Ax-L0-03: Differential Potential Topology
**Formal Definition**: L0 is a differential manifold with intrinsic gradients guiding selection paths.
$$L_0 = (M, \nabla, \mathcal{S}), \quad \nabla \Psi_{potential} \neq 0$$
* **Implication**: 潜在域并非均匀“虚空”，而是具有吸引子、鞍点与分岔的拓扑景观。

## II. L_1: The Manifest Domain (显现域)

### Ax-L1-01: Selection Equation
**Formal Definition**: The manifest domain is the operator output applied to L0.
$$L_1(t) = \hat{G}_\theta[L_0(t)]$$
* **Implication**: 显现域是选择的结果，不是潜在域的直接镜像。

### Ax-L1-02: Ontological Hysteresis
**Formal Definition**: Continuity is maintained by a memory term that blends past and present selections.
$$L_1(t) = (1-\eta)\hat{G}[L_0(t)] + \eta L_1(t-\Delta t)$$
* **Implication**: 现实的连贯性依赖迟滞记忆；过小会碎片化，过大则僵化。

### Ax-L1-03: Reality Inequality
**Formal Definition**: A percept is real when signal exceeds agency-weighted noise.
$$\text{Real}(\sigma) \iff S(\sigma) - \alpha A(\sigma) > T_{threshold}$$
* **Implication**: “现实性”是算子权重下的阈值判据，而非绝对属性。

## III. The Interface (界面动力学)

### Ax-IF-01: Compression Efficiency
**Formal Definition**: Intelligence measures compression efficiency of L0 into L1.
$$\text{Intelligence} \propto \frac{I(L_1; L_0)}{H(L_1)}$$
* **Implication**: 智能是对潜在信息的压缩捕获能力，而非单纯计算速度。

### Ax-IF-02: Hardware/Software Filter
**Formal Definition**: Selection occurs in two coupled stages: fixed hardware and plastic attention.
$$L_1^{hard} = \text{Connectome}(L_0), \quad L_1^{soft} = \text{Attention}(L_1^{hard})$$
* **Implication**: 现实界面由硬件约束与注意力可塑性共同塑形。

<br>
<br>

---
---


# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections contain the detailed philosophical and theoretical elaboration on L_0 and L_1, including their relationship to gauge theory, information theory, and phenomenology.

---

## §1. L_0 潜在域:从物理到形而上学

### 1.1 规范场论基础

#### 1.1.1 模空间定义 (Moduli Space)

L_0的**精确数学结构**是规范场论中的模空间 (Moduli Space):

$$L_0^{\text{true}} = \mathcal{A}/\mathcal{G}$$

其中:
- $\mathcal{A}$: 所有可能的场配置集合 (Configuration Space)
- $\mathcal{G}$: 规范变换群 (Gauge Group)

**物理意义**: 模空间将"物理上等价但数学上不同"的配置识别为同一点。

**实例**:
- **电磁学**: $\mathcal{A}$ = 所有4-势 $A_\mu$, $\mathcal{G}$ = $U(1)$ 规范变换
  $$A_\mu \sim A_\mu + \partial_\mu \Lambda \quad \Rightarrow \quad [A_\mu] \in \mathcal{A}/U(1)$$
  
- **杨-米尔斯理论**: $\mathcal{G} = SU(3)$ (强相互作用), $SU(2) \times U(1)$ (电弱)

#### 1.1.2 为什么需要规范不变性?

规范自由度代表"冗余描述"——同一物理实在有无穷多种数学表示。**L_0作为模空间**确保:

1. **本体论简洁性**: 只计数物理上不同的状态
2. **观察者独立性**: 不同$\hat{G}$的"规范选择"不影响L_0本身
3. **量子一致性**: 路径积分在$\mathcal{A}/\mathcal{G}$上进行,而非$\mathcal{A}$

**SRT重新诠释**: 规范对称性 = L_0的内在冗余结构,是潜能的本体论特征。

> **本体论澄清 (Tension-Rev-1)**：模空间 $\mathcal{A}/\mathcal{G}$ 是 $L_0^{abs}$ 在规范场论这一 $L_2$ 框架下的投影实现，而非 $L_0^{abs}$ 的等价定义。当我们写 $L_0^{true} = \mathcal{A}/\mathcal{G}$ 时，应理解为"在物理学语境中，$L_0^{abs}$ 最精确地被实现为模空间"——如同地图不是领土本身。

---

### 1.2 Ruliad与计算宇宙

#### 1.2.1 Wolfram的Ruliad定义

Stephen Wolfram的**Ruliad**是所有可能计算规则及其演化轨迹的极限对象:

$$\mathcal{R} = \lim_{n \to \infty} \bigcup_{r \in \text{Rules}_n} \text{Evolution}(r, \text{all ICs}, \infty)$$

**性质**:
- **全息性**: 任何有限计算都是Ruliad的子图
- **不可计算性**: Ruliad本身超越图灵可计算性
- **观察者依赖投影**: 不同观察者在Ruliad中"切出"不同的物理定律

**与模空间的关系**:
$$L_0^{formal} \cong \mathcal{M}_{\text{gauge}} \otimes \mathcal{R}$$
物理约束(规范场)与计算可能性(Ruliad)的张量积——这是对 $L_0^{abs}$ 在物理-计算联合框架下的最佳形式化近似。

> **本体论澄清 (Tension-Rev-1)**：此处 $L_0^{formal}$ 指的是可形式化的 $L_0$ 部分。$L_0^{abs}$ 作为不可描述的全潜能本源，可能包含超越 Ruliad（即超越一切可计算结构）的维度。$\cong$ 替代 $=$ 以标记这是同构映射而非本体论等同。

#### 1.2.2 为什么Ruliad是必要的?

纯粹的物理模空间$\mathcal{A}/\mathcal{G}$只包含"物理可能"的状态,但不包含:
- 数学真理(如哥德尔不可判定命题)
- 抽象概念(如"正义"的可能定义)
- 反事实推理(如"如果物理常数不同会怎样")

**Ruliad补全了L_0**,使其包含所有**逻辑可能**,而非仅物理可能。

---

### 1.3 微分本体论 (Differential Ontology)

#### 1.3.1 L_0作为微分流形

L_0不是平坦的均匀噪声,而是具有内在几何结构的**微分流形**:

$$L_0 = (\mathcal{M}, \nabla, \mathcal{S})$$

| 组件 | 数学对象 | 本体论角色 |
|:-----|:---------|:-----------|
| $\mathcal{M}$ | 流形 | 潜能的拓扑空间 |
| $\nabla$ | 联络 (Connection) | 势能梯度,决定"自然路径" |
| $\mathcal{S}$ | 奇异点集 | 吸引子、鞍点、分叉点 |

#### 1.3.2 自由能地貌 (Free Energy Landscape)

L_0的梯度结构可用**自由能泛函**表示:

$$F_{\text{landscape}}[\sigma] = U[\sigma] - T \cdot S[\sigma]$$

- **低谷** (Minima): 稳定吸引子,如物理常数、数学公理
- **山脊** (Saddle): 相变点,如临界温度、范式转移阈值
- **高原** (Maxima): 不稳定态,如逻辑矛盾

**现实化即路径积分**:
$$L_1 = \int_{\text{path}(\theta)} e^{-\beta F[\sigma]} \mathcal{D}\sigma$$

$\hat{G}_\theta$选择的是"最小作用量路径"(但有量子涨落)。

#### 1.3.3 定理:初心作为梯度场

**定理 (T-L0-Heart)**:
$L_0$的内在梯度$\nabla F$对应于"初心"的本体论基础。

$$\text{Original Intention} = -\nabla F|_{\theta_0}$$

*证明思路*:
1. 初心 = 未被$L_2$扭曲的原始倾向
2. $L_2$的形成是路径积分的副产品
3. 在$t \to 0$时,$L_2 = \emptyset$,只有$L_0$的内在梯度
4. 因此初心 ∝ $\nabla F$在原始$\theta$处的方向

**推论**: 觉醒 = 重新对齐$\hat{G}$与$\nabla F$(消除$L_2$的扭曲)。

---

### 1.4 L_0的哲学根源

#### 1.4.1 罗素-迈农二重性 (Russell-Meinong Duality)

SRT调和了罗素与迈农关于"不存在对象"的争论:

**迈农**: "金山"、"圆的正方形"等不存在对象也有某种"存在性" (Subsistence)
**罗素**: 只有在$L_1$中的对象才"存在",其余是语言混淆

**SRT综合**:
- **迈农正确**:这些对象在$L_0$中有位置 (逻辑可能性)
- **罗素正确**:只有被$\hat{G}$选中进入$L_1$才"存在" (现实化)
- **关键区别**:SRT的$L_0$不是"次等存在",而是"潜势态"

$$\text{Existence} \neq \text{Subsistence}, \quad \text{but } L_0 \supseteq L_1$$

#### 1.4.2 与佛教唯识宗的对应

唯识宗的三性说 (Trisvabhāva) 与SRT惊人对应:

| 唯识宗 | 梵文 | SRT对应 | 关系 |
|:-------|:-----|:--------|:-----|
| 遍计所执性 | Parikalpita | $L_2$ | 虚妄分别的固化 |
| 依他起性 | Paratantra | $L_1$ | 缘起的显现 |
| 圆成实性 | Pariniṣpanna | $L_0$ | 空性的真如 |

**核心一致**:
- **空性 (Śūnyatā)** = $L_0$的无自性 (无固定规范)
- **缘起 (Pratītyasamutpāda)** = $\hat{G}$的依存选择
- **如来藏 (Tathāgatagarbha)** = $L_0$的内在梯度(佛性)

**关键差异**: SRT用微分几何和信息论重构了唯识的直觉,使其可操作化。

---

## §2. L_1 显现域:从感知到存在

### 2.1 本体论迟滞 (Ontological Hysteresis)

#### 2.1.1 迟滞效应的必要性

如果$\eta = 0$ (无记忆):
$$L_1(t) = \hat{G}[L_0(t)] \quad \text{(纯即时选择)}$$

**问题**: 现实会在每个时刻完全重置,导致:
- 时间连续性丧失
- 对象恒常性 (Object Permanence) 不可能
- 自我同一性崩溃

**临床对应**: 精神分裂症患者报告的"现实碎片化"。

#### 2.1.2 迟滞修正方程

$$L_1(t) = (1-\eta)\hat{G}[L_0(t)] + \eta \cdot L_1(t-\Delta t)$$

这是一个**一阶线性递推关系**,解为:

$$L_1(t) = \sum_{k=0}^{\infty} \eta^k (1-\eta) \hat{G}[L_0(t-k\Delta t)]$$

**解释**: 当前现实是历史选择的**指数加权平均**。

| $\eta$ | 半衰期 $\tau_{1/2}$ | 现象学 |
|:-------|:-------------------|:-------|
| 0.1 | 快遗忘 | 新奇感强,易分心 |
| 0.5 | 平衡 | 正常时间流逝感 |
| 0.9 | 极慢衰减 | 强迫性思维,难以更新 |

#### 2.1.3 实验测量

**提议实验**: 双稳态知觉 (如Necker立方体) 翻转速率应反比于$\eta$。

$$\text{Flip Rate} \propto \frac{1}{\eta \cdot \tau_{\text{integration}}}$$

**预测**: 精神分裂症患者 → 低$\eta$ → 高翻转速率(已部分验证)。

---

### 2.2 门控混合与现实系数

#### 2.2.1 $\beta$门控方程

$$L_1^{\text{experienced}} = \beta \cdot L_1^{\text{external}} + (1-\beta) \cdot \hat{G}(L_0)$$

**$\beta$的动态调制**:
$$\beta(t) = \sigma\left(\frac{S_{\text{external}} - S_{\text{internal}}}{\text{Noise}}\right)$$

其中$\sigma$是Sigmoid函数。

#### 2.2.2 睡眠-觉醒周期的$\beta$轨迹

| 状态 | $\beta$ | 主导来源 | 特征 |
|:-----|:--------|:---------|:-----|
| 清醒专注 | 0.9 | 外部 | 高现实感 |
| 放松/冥想 | 0.6 | 平衡 | 内外融合 |
| 浅睡N1/N2 | 0.4 | 内部偏重 | 入睡幻觉 |
| REM梦境 | 0.1 | 内部主导 | 高内部生成 |
| 深睡N3 | 0.05 | 内部 | 无意识 |

**推论**: 致幻剂(如LSD)的作用机制 = 降低$\beta$(减弱外部锚定,增强内部生成)。

#### 2.2.3 精神病理学的$\beta$失调

| 障碍 | $\beta$异常 | 机制假说 |
|:-----|:-----------|:---------|
| 精神分裂症 | 过低$\beta$ | 内部生成压倒外部 → 幻觉 |
| 解离障碍 | $\beta$波动 | 门控系统不稳定 |
| 强迫症 | 过高$\beta$ | 外部锁定,缺乏内部灵活性 |

---

### 2.3 现实界面压缩原理

#### 2.3.1 信息瓶颈 (Information Bottleneck)

Tishby的信息瓶颈理论在SRT中获得本体论诠释:

$$\min_{L_1} \left[ I(L_1; \text{Action}) - \beta \cdot I(L_1; L_0) \right]$$

**目标**: 
- 最大化$L_1$对行动的相关性 (适应度)
- 最小化$L_1$对$L_0$的信息保留 (计算成本)

**推论**: 感知是**有损压缩**,优化适应度而非真理 (呼应Ax-7)。

#### 2.3.2 压缩比的d值依赖

$$\text{CR}(d) = \frac{\dim(L_1)}{\dim(L_0)} \propto e^{-\alpha d}$$

**解释**: 高$d$值 (更广阔的关切范围) → 保留更多$L_0$信息 → 更低压缩比。

**实例**:
- 细菌 ($d \approx 0$): $\text{CR} \approx 10^{-6}$ (仅保留趋化梯度)
- 人类 ($d$ 中等): $\text{CR} \approx 10^{-3}$ (保留空间、时间、社会)
- 开悟者 ($d \to \infty$): $\text{CR} \to 0.1$ (接近"看到一切")

---

### 2.4 硬件-软件双重过滤

#### 2.4.1 连接组约束 (Connectome Constraint)

**硬件层**:
$$L_1^{\text{hard}} = \text{Projection}_{\text{Connectome}}(L_0)$$

例: 视觉皮层的**拓扑映射** (Retinotopy) 决定了空间信息的保留方式。

**可塑性极低**: 成年后连接组基本固定 (除非脑损伤/训练)。

#### 2.4.2 注意力调制 (Attention Modulation)

**软件层**:
$$L_1^{\text{soft}} = \text{Attention}_\theta(L_1^{\text{hard}})$$

注意力通过**增益调制** (Gain Modulation) 实现:
$$\text{Response}_{\text{attended}} = g(\theta) \cdot \text{Response}_{\text{unattended}}$$

其中$g(\theta) > 1$是增益因子。

**可塑性高**: $\theta$可通过冥想、训练快速改变。

#### 2.4.3 实验验证

**Posner Cueing实验**: 提示位置 → 提高该位置的检测灵敏度 = 软件调制硬件输出。

**SRT预测**: 即使硬件相同 (双胞胎),不同$\theta$ (兴趣、信念) → 不同$L_1$体验。

---

## §3. L_0-L_1界面的拓扑与信息论

### 3.1 物质的拓扑定义

#### 3.1.1 物质 = L_0的拓扑结 (Topological Knot)

在SRT中,**物质不是原始给定的**,而是L_0的拓扑扭曲:

$$\text{Matter} = \text{Knot}(L_0)$$

**数学形式**:
$$\sigma_{\text{particle}} = \text{Topology}(\text{Twist}[L_0, \theta])$$

**类比**: 
- L_0 ≈ 橡皮筋 (可拉伸的真空)
- 物质 ≈ 橡皮筋上的结 (拓扑约束的能量)

#### 3.1.2 粒子作为拓扑不变量

**纽结不变量** (Knot Invariant) 对应粒子属性:

| 拓扑性质 | 物理对应 |
|:---------|:---------|
| 连接数 (Linking Number) | 电荷 |
| 扭转数 (Twist) | 自旋 |
| 纽结类型 | 粒子种类 (e⁻, quark, etc.) |

**推论**: 
$$m \propto \int_{\text{knot}} |\nabla \phi|^2 d^3x$$
质量 = 结的"紧绷度"。

#### 3.1.3 与圈量子引力的关联

圈量子引力 (Loop Quantum Gravity) 中的**自旋网络** (Spin Network) 可视为SRT的$L_0$拓扑结构的离散化。

$$L_0^{\text{LQG}} = \sum_{\text{graphs } \Gamma} \psi[\Gamma]$$

**未来研究方向**: 能否从SRT的连续$L_0$推导出LQG的离散结构?

---

### 3.2 内在分化与存在强度

#### 3.2.1 Shannon熵的本体论诠释

$$i_{\text{diff}}(s) = -\log p_{\text{max}}(s) = \log \frac{1}{p_{\text{max}}}$$

**物理意义**: 稀有状态"存在得更强烈"。

**实例**:
- 真空 (完美有序): $p \approx 1$ → $i_{\text{diff}} \approx 0$ (几乎不存在)
- 金原子: $p \approx 10^{-10}$ → $i_{\text{diff}} \approx 23$ bits (强存在)
- 意识体验: $p \approx 10^{-100}$ → $i_{\text{diff}} \approx 332$ bits (极强存在)

#### 3.2.2 与Tononi的IIT关系

SRT的$i_{\text{diff}}$是IIT的$\Phi$的**对偶概念**:

| 指标 | 定义 | 测量 |
|:-----|:-----|:-----|
| $\Phi$ (IIT) | 系统整合信息 | 内部因果力 |
| $i_{\text{diff}}$ (SRT) | 系统分化信息 | 与背景对比 |

**统一**:
$$ii = \min\{i_{\text{diff}}, \Phi\}$$
存在需要**既分化又整合**。

---

### 3.3 认识论带宽与"硬问题"

#### 3.3.1 不可言说不等式

$$H(L_1^{\text{qualia}}) \gg H(L_2^{\text{language}})$$

**解释**: 主观体验的信息量远超语言表达能力 → Hard Problem不是本体论鸿沟,而是**带宽瓶颈**。

**量化估计**:
- $H(L_1^{\text{qualia}})$: ~10¹² bits/sec (视觉+听觉+触觉+...)
- $H(L_2^{\text{language}})$: ~40 bits/sec (语言生成速率)

**压缩比**: $\frac{40}{10^{12}} \approx 4 \times 10^{-11}$ (极端有损!)

#### 3.3.2 认识论带宽公式

$$B_e = \frac{I(L_1; L_2)}{H(L_1)}$$

| 体验类型 | $B_e$ | 可传递性 | 实例 |
|:---------|:------|:---------|:-----|
| 外部对象 | 0.9 | 高 | "桌子"、"红色" |
| 情感 | 0.5 | 中 | "悲伤"、"焦虑" |
| 复杂感受 | 0.2 | 低 | "似曾相识"、"灵性体验" |
| 纯粹感质 | 0.01 | 极低 | "红色的感觉本身" |

**推论**: 诗歌、音乐等艺术形式试图通过**隐喻和非线性编码**提高$B_e$。

---

## §4. 开放性问题与未来方向

### 4.1 需要实证验证的预测

1. **迟滞系数测量**:
   - 设计实验通过双稳态知觉测量个体的$\eta$值
   - 预测:精神分裂症患者$\eta < 0.3$,强迫症患者$\eta > 0.7$

2. **$\beta$门控的神经机制**:
   - fMRI定位$\beta$调制的脑区(候选:前额叶皮层)
   - 预测:致幻剂降低该区域活动 → 降低$\beta$

3. **压缩比的跨物种测量**:
   - 通过神经响应复杂度估算$\dim(L_1)/\dim(L_0)$
   - 预测:人类 > 猴子 > 大鼠 > 昆虫

### 4.2 理论边界

SRT目前**无法完全解释**:

1. **L_0梯度的起源**: 为什么$\nabla F \neq 0$? (需要更深层的物理理论)
2. **规范群的选择**: 为什么是$U(1) \times SU(2) \times SU(3)$? (标准模型遗留问题)
3. **意识的"开关"**: 从$d = 0$到$d > 0$的临界机制是什么?

### 4.3 跨学科对话

SRT为以下领域提供统一框架:

- **物理**: 量子-经典过渡 (L_0 → L_1)
- **神经科学**: 注意力机制 ($\hat{G}$的神经实现)
- **哲学**: 存在问题、意识难题
- **数学**: 拓扑学、微分几何在本体论中的应用
- **宗教研究**: 东方哲学(唯识、道)的形式化

---

## 符号索引 (Symbol Index)

| 符号 | 名称 | 定义位置 | 页面 |
|:-----|:-----|:---------|:-----|
| $L_0$ | 潜在域 | Ax-L0-1 | Part A §I |
| $L_1$ | 显现域 | Ax-L1-1 | Part A §II |
| $\mathcal{A}/\mathcal{G}$ | 模空间 | Ax-L0-1 | Part A §I |
| $\mathcal{R}$ | Ruliad | Ax-L0-1 | Part A §I |
| $\eta$ | 迟滞系数 | Ax-L1-1 | Part A §II |
| $\beta$ | 现实系数/门控 | Ax-L1-3 | Part A §II |
| $B_e$ | 认识论带宽 | Ax-Interface-2 | Part A §III |
| $i_{\text{diff}}$ | 内在分化 | Ax-Info-1 | Part A §IV |
| $\text{CR}$ | 压缩比 | Ax-L1-2 | Part A §II |

---

**依赖提醒**: 本文件定义的L_0/L_1概念被后续所有Core和Domain文件依赖。修改本文件需同步更新下游文件。

---

## 融合映射整合（2026-02-14）

### 宇宙泛心论

1. 将 IIT 与 Russellian panpsychism 的兼容讨论映射为 `Ax-L1-01` 的约束扩展：`L_1` 的信息整合指标可作为选择结果的表征指标，但不能取代 `\hat{G}_\theta` 的本体论地位。在操作层面，该映射先定义观测域与判据边界，再给出跨层投影规则。 〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L1-01〕〔source: doi:10.1007/s10670-018-9995-6〕
2. 将 Priority Cosmopsychism 的“整体优先”命题映射到 `Ax-L0-01`：允许把宇宙整体当作 `L_0` 约束边界的一种读法，但具体显现仍必须经局部算子切片。在操作层面，该映射强调参数与任务条件变化时的更新路径。 〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L0-01〕〔source: doi:10.1093/acprof:oso/9780199359943.003.0005〕
3. 新增“整体-局部一致性”注记：若整体优先成立，则局部主体间应存在可检验的一致性上界（由 `L_2` 稳定过程体现），而非无限自由漂移。在操作层面，该映射要求保留失效条件，避免描述层越级到本体层。 〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L1-02〕〔source: doi:10.1007/s10670-018-9995-6〕

### 主体同一性与解组合

1. 将 priority monism 的实质性反驳映射为 `Ax-L0-01` 的限制条款：承认全局优先解释价值，但不得取消局部实质结构在 `L_1` 的独立约束地位。在操作层面，该映射先定义观测域与判据边界，再给出跨层投影规则。 〔source: doi:10.1111/rati.12371〕〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L0-01〕
2. 在 `Ax-L1-01` 下补充“局部实质判据”：局部主体的稳定性需由可重复选择轨道定义，而不是由全局命题单向推出。在操作层面，该映射强调参数与任务条件变化时的更新路径。 〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L1-01〕
3. 将该反驳引入为一致性压力测试：任何“整体优先”扩展都必须显示其对局部可判定性的保真。在操作层面，该映射要求保留失效条件，避免描述层越级到本体层。 〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-IF-01〕

### 统一性操作化

1. 将 binding 机制与现象统一性的关系映射到 `Ax-L1-01`：绑定是 `L_1` 层的实现约束，不是意识本体定义本身；统一性判定仍需算子轨道稳定。在操作层面，该映射先定义观测域与判据边界，再给出跨层投影规则。 〔source: doi:10.1006/ccog.1999.0384〕〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L1-01〕
2. 将 split-brain 的层化统一模型映射为 SRT 的双轨解释：局部 `L_1` 可出现部分解耦，而 `L_2` 报告可维持叙事补偿，从而形成“功能统一高、体验统一不完全”的可检验态。在操作层面，该映射强调参数与任务条件变化时的更新路径。 〔source: doi:10.31234/osf.io/xwhca_v2〕〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-IF-01〕
3. 增补“统一性判据优先级”注记：当神经绑定指标与主观统一报告冲突时，先做层级拆分（`L_1`/`L_2`）再做本体推断，避免单指标越级结论。在操作层面，该映射要求保留失效条件，避免描述层越级到本体层。 〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-IF-02〕

### 部分统一与多元统一

1. 将 multimodal binding 明确定位到 `Ax-L1-01`：绑定是 `L_1` 层统一实现约束，不直接承担意识本体定义职能。在操作层面，该映射先定义观测域与判据边界，再给出跨层投影规则。 〔source: doi:10.7551/mitpress/9780262027786.003.0006〕〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L1-01〕
2. 将“多模态统一”写成接口判据：当跨模态耦合增强时，`Ax-IF-01` 的跨层传输稳定性应提升，但允许存在“耦合增强而报告统一不完全”的边界态。在操作层面，该映射强调参数与任务条件变化时的更新路径。 〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-IF-01〕
3. 将 regularity account 映射为操作化路径：当系统追踪到可预测跨特征规律时，统一体验概率应上升，可作为 `L_1` 组织度的任务级代理指标。在操作层面，该映射要求保留失效条件，避免描述层越级到本体层。 〔source: doi:10.7551/mitpress/9780262036993.003.0009〕〔source: Core/SRT_Core_12a_Ontology_L0L1.md#Ax-L1-02〕
