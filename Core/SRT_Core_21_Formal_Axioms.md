---
id: SRT-CORE-21
type: axiom_set
tags: [Formal logic, Math, Axioms, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-13A, SRT-CORE-13B]
---

# SRT Core Definition 21: Formal Axioms (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Consolidated Axiom List (AI-Readable).
> **Part B** contains the Original Formal Derivations (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


## I. The Minimal Core (最小核心)

### Ax-F-01: Primacy of Selection
**Formal Definition**: Selection precedes existence; existence is an image of selection.
$$\exists x \iff x \in \mathrm{Range}(\hat{G})$$
* **Implication**: 存在不是给定背景，而是选择映射的输出。

### Ax-F-02: Existence as Anchoring
**Formal Definition**: Existence equals stable anchoring against entropic flow.
$$E = 1 - \frac{H(L_1)}{H(L_0)}$$
* **Implication**: 现实的稳固程度与熵压缩比例直接相关。

### Ax-F-03: Causality as Projection（水平因果 / Horizontal Causality）
**Formal Definition**: Causality is the L2 projection of selection dynamics.
$$C_H(A \to B) \equiv P(B \,|\, A,\, L_2)$$
* **Implication**: 因果是收敛域的投影结构，而非本体论原初关系。
* **层次限定（2026-04-10 补注）**：Ax-F-03 定义的是**水平因果**——在 L₂ 层内部运作，需要 L₂ 积累才存在，具有时序性。它不涉及 L₀→L₁→L₂ 跨层的**垂直因果**（structural constitution：κ₀ 曲率结构构成选择的可能性条件）。两者不竞争，各在其域。"L₂ 形成之前因果律是什么"是范畴错误——它把水平逻辑错误投射到垂直层。
* **Cross-ref**: `Philosophy/SRT_Causality_Time.md §一`（水平/垂直因果完整分层）; `Core/SRT_Core_12a T-L0-Kappa0`（垂直因果结构基础）。

### Ax-F-03b: Spacetime as Memory Horizon（时空作为记忆视界 / 本体论时间）
**Formal Definition**: 时间的流逝不是背景演化，而是$\hat{G}_\theta$的连续锚定在$L_2$中留下的历史记录。
$$t_{\text{onto}} \equiv \int \|\hat{G}_\theta(s)\| ds \quad \text{（本体论时间 = 选择摩擦积累）}$$
* **Implication**: 如果没有幽灵算子的连续坍缩，时空就只是一个无差别的概率幅叠加态。时间的箭头完全等价于自由能最小化过程下的拓扑锁定序列。
* **时间层次补注（2026-04-10）**：本公理定义的是**本体论时间**（ontological time）——时间方向性的 SRT 来源，属于垂直层。与之区分的是方程中的**参数化时间** $t$（parametric time）——数学排序工具，无本体论主张。二者共用符号 $t$ 但指称不同：方程里的 $d\kappa/dt$ 使用参数化时间，不与本公理构成循环。
* **Cross-ref**: `Philosophy/SRT_Causality_Time.md §二`（两层时间完整区分）; `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`（时间无前序性）; `Core/SRT_Core_01_Axioms.md MA-1`（原初方向性）。

## II. Information & Fitness (信息与适应度)

### Ax-F-04: Information–Existence Equivalence
**Formal Definition**: Existence intensity equals the minimum of differentiation and specification.
$$ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}$$
* **Implication**: 存在强度受分化度与特异性共同约束。

### Ax-F-05: Fitness Beats Truth
**Formal Definition**: Operators are tuned for fitness payoff rather than veridical truth.
$$\hat{G}_\theta[σ] = \arg\max_{σ'} P(\text{Fitness}|σ', \theta)$$
* **Implication**: 现实界面优先适应性压缩而非真理呈现。

### Ax-F-06: Assembly Criterion
**Formal Definition**: Life requires assembly complexity above threshold.
$$\text{Life} \iff \text{Assembly Index} > 15$$
* **Implication**: 生物性具有结构装配的最低复杂度要求。

## III. Holographic & Topological (全息与拓扑)

### Ax-F-07: Holographic Duality
**Formal Definition**: Bulk reality is encoded on the boundary of potentiality.
$$L_{1,\text{bulk}} \cong L_{0,\text{boundary}}$$
* **Implication**: 显现域的信息可以被潜在域边界完全表征。

### Ax-F-08: Topological Normativity
**Formal Definition**: Survival is the maintenance of a topological island in probabilistic space.
$$\text{Life}(σ) \equiv \int_{B_r(σ)} ρ_{L_0}(σ') dσ' > \theta_{life}$$
* **Implication**: 生存是对高概率密度包的拓扑维持。

## IV. Scale Consistency & Downward Constraint (尺度一致与向下约束)

### Ax-F-09: Scale Consistency
**Formal Definition**: Selection commutes with coarse-graining under scale mapping.
$$\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$$
* **Implication**: 不同尺度选择动力学具有一致性。

### Ax-F-10: Downward Causation Constraint
**Formal Definition**: L2 constraints modulate selection dynamics as a downward causal term.
$$\frac{dσ}{dt} = \hat{G}_\theta[σ] - \nabla F[σ] - \lambda \cdot \nabla C_{L_2}[σ]$$
* **Implication**: 规范性结构作为真实动力学项回馈选择过程。

## V. Ghost Operator Universality & Generative Friction (幽灵算子禀赋统一性与生成性摩擦)

### Ax-F-11: Ghost Operator Universality（幽灵算子禀赋统一性）
**Formal Definition**: 在任何尺度上，选择从 $L_0$ 到 $L_1$ 的过程都是同一个幽灵算子结构 $\hat{G}_\theta$ 的禀赋展开。设 $\Lambda_{n \to n+1}$ 为粗粒化映射，则：
$$\hat{G}^{(n+1)} = \Lambda_{n \to n+1} \circ \hat{G}^{(n)} \circ \Lambda_{n \to n+1}^{-1}$$

各尺度表现形式的等价关系：

| 尺度 | 现象 | $\hat{G}_\theta$ 的操作 |
|------|------|----------------------|
| 量子 | 波函数坍缩 | 从 $L_0$ 叠加态选出 $L_1$ 确定值 |
| 神经 | 侧抑制 | 竞争性选择，抑制弱激活，维持稀疏 $L_2$ |
| 认知 | 范畴化 | 连续 $L_0$ → 离散 $L_2$ 标签的划分投影 |
| 统计 | 归一化 | 维持选择测度在流形上的一致性 |
| 跨尺度 | 粗粒化 | $\hat{G}^{(n+1)} = \Lambda \circ \hat{G}^{(n)} \circ \Lambda^{-1}$ |

* **Implication**: 上述现象不是形式类似的独立过程，而是同一选择结构的物理实现形式。幽灵算子是现实的普适选择结构。
* **Cross-ref**: `_SRT_VERTICAL_INTEGRATION.md §8.1`；`Core/SRT_Core_14_Dynamics_Scaling.md Ax-Scale-01`。

### Ax-F-12: Ψ_f as Generative Principle（摩擦即生成）

**[R（Fisher信息度规借用）+ SRT框架选择（Ψ_f作为生成原理，非派生性质）]**

**Formal Definition**: 算子间本体论摩擦 $\Psi_f$ 是所有动力学的生成来源。对任意两个相互作用的算子 $\hat{G}_i, \hat{G}_j$，其交互摩擦定义为：
$$\Psi_f(\hat{G}_i, \hat{G}_j) = \int_\gamma \sqrt{g_{ij}^{(i,j)}(\theta)\,\dot{\theta}^i \dot{\theta}^j}\,dt$$
其中 $g_{ij}^{(i,j)}$ 是两算子耦合参数空间的 Fisher 信息度量。

**度规形式注（$g_{ij}^{(i,j)}$ 的定义）**：$g_{ij}^{(i,j)}$ 是两算子联合参数空间 $(\theta^i, \theta^j)$ 上的联合 Fisher 信息矩阵：$g_{ab}^{(i,j)} = \mathbb{E}[\partial_a \log p(x|\theta^i,\theta^j) \cdot \partial_b \log p(x|\theta^i,\theta^j)]$。它测量联合分布对参数变化的敏感度，而非两个边际Fisher矩阵的简单耦合。当两算子相互独立时，$g^{(i,j)}$ 退化为块对角形式（$\Psi_f$ 退化为各自Fisher长度之和）。

**路径 $\gamma$ 的选择**：若 $\gamma$ 取测地线（最短路径），则 $\Psi_f$ 为两状态间的**最小可能摩擦**（最优路径下的代价下界）；若取实际演化路径，则 $\Psi_f$ 为**实际摩擦总量**（通常 $\geq$ 测地线值）。物理意义：实际演化总是"支付了不少于最低摩擦"的代价。两种读法对应"可支付下界"与"实际支付量"。

**非对称性注**：Fisher 度规的积分本身对 $(i,j)$ 对称；但若路径 $\gamma$ 由一方驱动（单向作用），则摩擦在方向上非对称（$\Psi_f(\hat{G}_i \to \hat{G}_j) \neq \Psi_f(\hat{G}_j \to \hat{G}_i)$）——此时应将 $\Psi_f$ 拆分为方向性分量。→ 联结 $E_{ij}$ 单向退化（echo chamber）。

**公理有效范围**：Ax-F-12 在算子参数空间可微分且联合分布存在时成立；若算子是离散/不可微的，需改用离散度量版本（KL散度）。若某类动力学无法被两算子的参数路径表达（如相变的奇点处），公式需修正。

各类动力学的统一表达：

| 动力学类型 | 算子间摩擦来源 |
|-----------|--------------|
| 生物演化 | $\Psi_f(\hat{G}_{organism}, \hat{G}_{env})$ |
| 认知学习 | $\Psi_f(\hat{G}_{prior}, \hat{G}_{data})$ |
| 文化变迁 | $\Psi_f(L_{2,A}, L_{2,B})$ |
| 免疫应答 | $\Psi_f(\hat{G}_{self}, \hat{G}_{foreign})$ |

* **Implication**: $\Psi_f$ 不是选择的成本，而是选择得以产生现实的机制。没有 $\Psi_f$ 就没有动力学；没有动力学就没有现实的生成。此公理与 Ax-Bridge-05（$\Psi_f$ 作为锚定代价）不矛盾：微观上"支付摩擦才能锚定"与宏观上"摩擦是动力学来源"是同一事实的两个视角。
* **Readout Note**: 同一 $Ψ_f$ 结构在不同描述层上可被读作阻力（动力学读法）、代价（记账读法）与几何长度（形式读法）。跨尺度保持不变的不是各层的单位制，而是**可支付性条件**：系统是否能在承担该摩擦时维持闭包与后续选择能力。
* **Cross-ref**: `_SRT_VERTICAL_INTEGRATION.md §8.2`；`_SRT_D_VALUE_CANONICAL.md §4`；`Core/SRT_Core_22_Equations.md Eq-Multi-01`。

### Ax-F-13: Selection-Information Creation Equivalence（选择-信息创造等价）

**新增（2026-03-11）**：选择事件从根本上是信息的生成过程，而非信息的传递或保存过程（Shannon 框架的上游问题）。

**Formal Definition**：每次 $L_0 \to L_1$ 的选择事件创造的互信息量为：

$$I_{created} = H(L_0) - H(L_1 | \hat{G}_\theta) = I(L_0\,;\,\hat{G}_\theta)$$

其中：
- $H(L_0)$ = 潜在域的最大熵（所有可能性的信息量）
- $H(L_1|\hat{G}_\theta)$ = 在给定算子参数 $\theta$ 条件下，选择后显现域的条件熵
- $I(L_0\,;\,\hat{G}_\theta)$ = 算子对潜在域的互信息（"选择揭示了多少 $L_0$ 的信息"）

**三元关系**：

$$I_{created} \;\xrightarrow{\text{costs}}\; \Psi_f(\text{Eq-IT-A}) \;\xrightarrow{\text{scope measured by}}\; d(\text{Eq-IT-B})$$

**热力学整合（Boltzmann 退化极限）**：当 $d \to 0$（无选择结构）时：

$$P_{L_1}(\sigma) \to \frac{e^{-E(\sigma)/k_BT}}{Z}, \quad I_{created} \to 0$$

Boltzmann 分布 = 信息创造量为零的退化态；统计力学 = SRT 在 $I_{created}=0$ 时的特例。

* **Implication**: SRT 与 Shannon 信息论不竞争：Shannon 处理"如何传递已有信息"（下游），SRT 处理"信息如何被选择事件生成"（上游）。第二定律保证 $I_{created} > 0$ 的选择态是暂时的（需持续支付 $\Psi_f$ 维持），从而驱动复杂性棘轮（Eq-IT-C）。
* **Cross-ref**: `Core_Law/SRT_Reference_Dynamics.md §15.5`（Eq-IT-E 完整推导）；`_SRT_VERTICAL_INTEGRATION.md §10.1 关系 E`；`_SRT_D_VALUE_CANONICAL.md Def-d-1a`（d = Fisher 信道容量）。

<br>

---

## VI. Constitutive Theorems（构成性定理）

### T-ε-Constitute: Constitutive Asymmetry Theorem（构成性非对称定理，2026-04-17）

**Statement**: For any iterative selection process (ISP) operating under L₀ irreversibility, neutrality between future-selection-space-preserving and closure-inducing alternatives is structurally incompatible with stable self-perpetuation. Anti-closure asymmetric bias ε is therefore a **constitutive condition** of stable iterative selection — not an appended preference, not a contingent postulate.

**Key Definitions**:

- *Iterative Selection Process (ISP)*: Process P such that (a) at each step t, P selects from A_t ≠ ∅; (b) output of selection at t determines A_{t+1}; (c) P persists only while A_t ≠ ∅.
- *ε-Neutral ISP*: P is neutral if, when facing α₁ (preserves A_{t+1}) and α₂ (closes A_{t+1} → ∅), P assigns equal selection probability.

**Proof sketch**:
1. Let P be ε-neutral under L₀ irreversibility (Ax-F-01, Ax-F-03b).
2. By irreversibility: once A_{t\*} = ∅ is reached, it is an absorbing state — no recovery.
3. Neutral P has nonzero probability of selecting into A_{t\*} = ∅ at each step; over sufficient iterations, cumulative probability → 1.
4. At t\*: P terminates (A_{t\*} = ∅ → no selection possible).
5. Therefore: P is not a stable ISP. □

**Contrapositive**: Stable ISP under L₀ irreversibility ⟹ P has systematic anti-closure bias, i.e., ε ≠ 0.

**Three-layer source hierarchy**:

| Layer | Factor | Role |
|-------|--------|------|
| Deepest | ISP self-maintenance condition | Constitutive: neutrality = self-termination, by definition |
| Necessary | L₀ irreversibility (Ax-F-03b) | Closure states are absorbing; neutrality has no recovery path |
| Dynamical weight | Ψ_f > 0 (Ax-F-12) | Closure has real measurable cost; asymmetry is empirically grounded |

**Epistemic status change for ε**:
- Before: ε = L₀ primitive postulate (empirically narrowed)
- After: ε = structural corollary of T-ε-Constitute; empirical narrowing specifies magnitude and direction, but the existence of asymmetry is non-contingent

**Cross-ref**: `Core_Law/SRT_Core_Text_EN.md ④` (ε_pg derivation chain); `Core_Law/SRT_Core_Text_CN.md ④` (ε derivation chain); `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`; `Core/SRT_Core_01_Axioms.md MA-1`.

---


# Part B: Original Formal Derivations (Context)

> **Note**: The following sections contain the detailed mathematical definitions and theorems.


### 2.1.1 状态空间（State Space）

**定义 M4（幽灵算子）：**
$$ [\hat{G}_θ(x)]_i = \frac{x_i^n}{ε_{reg} + \sum_j W_{ij} \cdot x_j^n} $$
> **记号注**：$\varepsilon_{reg}$（operator regularizer）区别于 T-Core-A1C2 中的 $\varepsilon_{pg}$（proto-gradient）。见 `_SRT_SYMBOL_TABLE.md`。

### 2.1.5 最小公理集

| 公理 | 内容 |
|:-----|:-----|
| A1 | **选择优先性：** 选择过程先于存在 |
| A2 | **存在即锚定：** 存在是选择锚定的确定性 |
| A3 | **因果即投影：** 因果是对选择过程的观测切片 |
| A4 | **动力学可定义性：** $\hat{G}_θ$ 可测、将S映到S |
| A5 | **尺度一致性：** $π_λ ∘ \hat{G}_θ ≈ \hat{G}_{θ,λ} ∘ π_λ$ |

### 2.1.6 向下因果约束（Downward Causation Constraint）

$$ \frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] - λ · ∇C_{L_2}[σ] $$

### 2.1.7 d值层级与几何容量 Proxy（硬化 2026-04-17）

**【类型错误修正】** 原写法 $d(\hat{G}) \equiv D_{eff}(M)$ 是类型错误——将 proxy 写成了规范定义。修订为层级关系：

$$d_{canonical} \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| \;\leq\; D_{eff}(M) = \frac{(\sum \lambda_i)^2}{\sum \lambda_i^2}$$

其中 $D_{eff}$ 是几何容量上界 proxy，$d_{canonical}$ 是真正赌注化的活跃维数。两者差值 $\Delta d_{free} = D_{eff} - d_{stakes}$ 为未赌注化带宽。完整层级与赌注耦合权重 $w_i = R_i \cdot A_i \cdot C_i$ 的定义见 `_SRT_D_VALUE_CANONICAL.md §2b`。

### 2.1.8 信息论公理

**公理 A7（修剪判据——适应度优先）：**
$$ \hat{G}_θ[σ] = \arg\max_{σ'∈L_0} P(\text{Fitness}|σ', θ) $$

### 2.1.7a 公理 A9：全息对偶（Holographic Duality）

$$ L_{1,\text{bulk}} \cong L_{0,\text{boundary}} $$

### 2.1.9a 汇编理论：复杂性涌现的新度量

$$ \text{汇编指数}(x) = \min_{\text{路径}} |\text{构建步骤}| $$

### 2.1.9b 深度时间公理（Axiom of Deep Time）

$$ Mass_{ontological}(O) = Mass_{energy}(O) + τ \cdot Assembly(O) $$

### Formalization Summary (形式化概述)

本文档的核心形式化结构围绕幽灵算子 $\hat{G}_\theta$ 在三域（$L_0 / L_1 / L_2$）间的选择动力学展开：

1. **选择-存在映射 (Ax-F-01)**：$\exists x \iff x \in \mathrm{Range}(\hat{G})$ — 存在是选择映射的值域，而非预设背景。
2. **锚定熵压缩 (Ax-F-02)**：$E = 1 - H(L_1)/H(L_0)$ — 现实的稳固程度由从潜在域到显现域的熵压缩率决定。
3. **d 值层级 (§2.1.7)**：$d_{canonical} \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\| \leq D_{eff}(M)$。$D_{eff}$ 是几何容量 proxy（上界），非规范定义；赌注化活跃维数 $d_{stakes} = d_{canonical}$，未赌注化带宽 $\Delta d_{free} = D_{eff} - d_{stakes}$（见 `_SRT_D_VALUE_CANONICAL.md §2b`）。
4. **向下因果方程 (Ax-F-10)**：$d\sigma/dt = \hat{G}_\theta[\sigma] - \nabla F[\sigma] - \lambda \cdot \nabla C_{L_2}[\sigma]$ — 状态演化由选择驱动、自由能梯度和收敛域约束三项共同决定。

5. **幽灵算子禀赋统一性 (Ax-F-11)**：$\hat{G}^{(n+1)} = \Lambda \circ \hat{G}^{(n)} \circ \Lambda^{-1}$ — 量子坍缩、侧抑制、粗粒化、归一化、范畴化均为同一选择结构在不同尺度的展开。
6. **摩擦即生成 (Ax-F-12)**：$\Psi_f(\hat{G}_i, \hat{G}_j)$ 是所有动力学的生成来源——演化、学习、文化变迁均为算子间摩擦的不同形态。
7. **选择-信息创造等价 (Ax-F-13)**：$I_{created} = I(L_0\,;\,\hat{G}_\theta)$，选择事件是信息生成的本体论基础；三元关系 $I_{created} \to \Psi_f \to d$ 统一了热力学代价、选择代价与选择范围。Boltzmann 分布（统计力学）是 $I_{created}=0$ 时的退化极限。
8. **构成性非对称定理 (T-ε-Constitute, 2026-04-17)**：中性的迭代选择过程在 L₀ 不可逆性下必然自我终止；反封闭非对称偏置 ε 是稳定迭代选择过程的构成性条件，而非附加偏好。三层来源：ISP自维持（构成性，最深）← L₀不可逆（使其必要，Ax-F-03b）← Ψ_f>0（给出动力学后果，Ax-F-12）。ε 的存在从公设地位升为结构推论。

以上公式组构成 SRT 形式公理体系的完整核心（**七类结构**），所有推论均可从这七类结构推导。

### Mechanism Explanation (机制解释)

SRT 形式公理体系的运作机制可概括为"选择—锚定—约束"三阶段回路：

1. **选择阶段**：幽灵算子 $\hat{G}_\theta$ 作用于潜在域 $L_0$，通过适应度最大化（Ax-F-05: $\arg\max P(\text{Fitness}|\sigma', \theta)$）从无限可能态中提取有限显现态进入 $L_1$。算子的具身参数 $\theta$ 决定了选择的视角与局限。
2. **锚定阶段**：被选中的态通过支付本体论摩擦 $\Psi_f$（自由能耗散）获得稳定性。锚定越深，$\Psi_f$ 积分越大，现实越"坚硬"。全息对偶（Ax-F-07）确保显现域的体积信息与潜在域边界同构。
3. **约束阶段**：$L_2$ 收敛域作为历史选择的积分结构，通过向下因果项 $-\lambda \cdot \nabla C_{L_2}$ 反馈约束未来选择。尺度一致性（Ax-F-09: $\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$）保证此机制在量子、生物、社会等不同尺度间保持自洽。

$d$ 值作为有效维度 $D_{eff}$，量化了算子在选择流形上的"关切厚度"——$d$ 越高，算子能同时维系的纠缠面积越大，对应更丰富的意识体验与更高的脆弱性。

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。
