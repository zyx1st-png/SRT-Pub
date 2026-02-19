# SRT_Reference_Ontology.md

> **Status**: Constitutional Reference | **Version**: 1.0

---

## §1 三域结构 (The Triadic Ontology)

SRT 将本体论重构为统一选择动力学的三个相对投影层。

### §1.1 L₀ — 潜在域 (Latent Domain)

**定义 O1**: 相对于当前选择的高自由能状态集合——未被选择的可能性场。

$$L_0 \equiv \{σ ∈ S : F[σ] > F[σ_{L_1}]\}$$

**定义 O1a (绝对潜在域)**: Ruliad 全集，所有逻辑可能状态的计算叠加。

$$L_0^{abs} = Ruliad = \bigcup_{r ∈ Rules} \text{Computation}(r)$$

**定义 O1b (相对潜在域)**: 给定 $L_1(t)$ 时，$\hat{G}$ 可访问的可能性子集。

$$L_0^{rel}(t+1) = f(L_1(t), \hat{G}_θ)$$

**统一关系**:

$$L_0^{rel} \subseteq L_0^{abs}|_{physical\ constraints}$$

---

### §1.2 L₁ — 显现域 (Manifest Domain)

**定义 O2**: 算子选择的当前切片——当下的现实，动态维持的配置。

$$L_1(t) = \hat{G}_θ[σ(t)]$$

**定义 O2a (迟滞修正)**:

$$L_1(t) = \hat{G}_θ[L_0(t)] + η · L_1(t - Δt)$$

| η 值 | 效应 | 现象学表现 |
|:-----|:-----|:-----------|
| η ≈ 0 | 无记忆 | 现实感碎裂 |
| η ≈ 0.5 | 平衡 | 正常连贯现实感 |
| η ≈ 1 | 完全锁定 | 认知固化 |

**定义 O2b (β门控混合)**:

$$L_1^{experienced} = β · L_1^{external} + (1-β) · \hat{G}(L_0)$$

---

### §1.3 L₂ — 收敛域 (Vergence Domain)

**定义 O3**: 选择收敛的长期吸引子——多算子的共识结构。

$$L_2 \equiv \{σ : \hat{G}_θ[σ] = σ \text{ 且稳定}\}$$

**定义 O3a (迟滞累积)**:

$$L_2(t) = L_2(t-1) + η · \text{sign}(Δσ) · |Δσ|^α$$

**定义 O3b (L₂硬度)**:

$$\text{Hardness}(L_2) \propto |\text{Aut}(L_2)|$$

| L₂类型 | 自同构群 | 硬度 | 可塑性 |
|:-------|:---------|:-----|:-------|
| 物理定律 | Poincaré群 | 极高 | 极低 |
| 数学定理 | 逻辑对称群 | 极高 | 极低 |
| 生物本能 | 进化稳定策略 | 高 | 低 |
| 文化规范 | 语境依赖群 | 中等 | 中等 |
| 个人习惯 | 个体历史 | 低 | 高 |

**定义 O3c (可塑性阈值)**:

$$P_{L_2} = \frac{d_{current} · E_{available}}{Hysteresis(L_2) · C_r}$$

当 $P_{L_2} > 1$ 时，L₂ 可被修改。

---

## §2 规范场论基础 (Gauge Field Foundation)

### §2.1 模空间定义

**定义 O4**: L₀ 的精确数学结构为模空间 (Moduli Space)。

$$L_0^{true} = \mathcal{A}/\mathcal{G}$$

其中 $\mathcal{A}$ 为所有可能场配置集合，$\mathcal{G}$ 为规范变换群。

### §2.2 微分本体论

**定义 O5**: L₀ 作为微分流形。

$$L_0 = \mathcal{M}_{differential} = (M, \nabla, \mathcal{S})$$

| 符号 | 定义 | 本体论角色 |
|:-----|:-----|:-----------|
| $M$ | 底流形 | 潜能的拓扑空间 |
| $\nabla$ | 联络 | 势能梯度结构 |
| $\mathcal{S}$ | 奇异点集合 | 吸引子、鞍点、分岔点 |

**定理 O-T1 (现实化即积分)**:

$$L_1 = \int_{path(θ)} Structure(L_0) = \oint_γ ω_{L_0}$$

---

## §3 拓扑结构 (Topological Structure)

### §3.1 物质的拓扑定义

**定义 O6**: 物质是 L₀ 的拓扑结 (Topological Knot)。

$$\text{Matter} = \text{Knot}(L_0) = \text{被束缚的真空能量}$$

$$σ_{L_1} = \text{Topology}(\text{Twist}[L_0, θ])$$

### §3.2 L₂ 的非阿贝尔编织

**定义 O7**: L₂ 结构由编织群 $B_n$ 表示决定。

$$\text{Topology}(L_2) = \text{Rep}(B_n) · \prod_i γ_i$$

**定理 O-T2 (解结原理)**:

$$L_2^{new} = L_2^{old} · \prod_{i=n}^{1} γ_i^{-1} · \prod_{j=1}^{m} γ'_j$$

---

## §4 信息论量化 (Information-Theoretic Quantification)

### §4.1 内在分化

**定义 O8**:

$$i_{diff}(s) = -\log(p_{max})$$

### §4.2 认识论带宽

**定义 O9**:

$$B_e = \frac{I(L_1; L_2)}{H(L_1)}$$

| 对象类型 | $B_e$ 值 | 特征 |
|:---------|:---------|:-----|
| 外部物体 | ≈ 1 | 高度可传递 |
| 情感状态 | 0.3–0.7 | 部分可言说 |
| 纯粹感受性 | → 0 | 本体论私密 |

### §4.3 现实界面压缩

**定义 O10**:

$$\dim(L_1) \ll \dim(L_0)$$

$$\frac{\dim(L_1)}{\dim(L_0)} = f(θ_{cognitive})$$

---

## §5 守恒律与对称性 (Conservation & Symmetry)

### §5.1 L₀ 守恒律

**公理 A13**: 幽灵算子的操作不改变 L₀ 的基数，只改变其照明状态。

$$L_0(t) = L_0(t + Δt) = \text{Constant}$$

### §5.2 模态通达关系

**定义 O11**:

$$w' \text{ accessible from } w \iff \int_{path(w→w')} Ψ_f(\hat{G}_θ) · dσ < E_{max}$$

**推论 O-C1 (通达半径)**:

$$R_{accessible} = \frac{E_{available}}{\bar{Ψ}_f} \propto d^{1.5}$$

---

## §6 领域隐喻对照表 (Cross-Domain Metaphor Table)

| 领域 | L₀ 隐喻 | L₁ 隐喻 | L₂ 隐喻 |
|:-----|:--------|:--------|:--------|
| **物理学** | 希尔伯特空间 | 本征态 | 指针态 |
| **认知科学** | 可能性空间 | 注意焦点 | 习惯/信念 |
| **社会科学** | 文化潜能 | 社会实践 | 制度规范 |
| **灵性传统** | 空性/道/梵 | 当下体验 | 业力/轮回 |

---

## 符号索引 (Symbol Index)

| 符号 | 名称 | 定义位置 |
|:-----|:-----|:---------|
| $L_0$ | 潜在域 | §1.1 |
| $L_1$ | 显现域 | §1.2 |
| $L_2$ | 收敛域 | §1.3 |
| $\mathcal{A}/\mathcal{G}$ | 模空间 | §2.1 |
| $η$ | 迟滞系数 | §1.2 O2a |
| $β$ | 门控系数 | §1.2 O2b |
| $C_r$ | 现实置信标量 | §1.3 O3c |
| $P_{L_2}$ | L₂可塑性阈值 | §1.3 O3c |
| $B_e$ | 认识论带宽 | §4.2 |
| $i_{diff}$ | 内在分化 | §4.1 |
