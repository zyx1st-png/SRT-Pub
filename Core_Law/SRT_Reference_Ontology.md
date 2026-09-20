---
id: SRT-REF-ONTOLOGY
type: definition
tags: [CoreLaw, Ontology, Canonical]
layer: L1
status: axiomatic_hybrid_v1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-L0-METAPHYSICS, SRT-REF-AXIOMS]
---

# SRT_Reference_Ontology.md

> **层级说明**：本文件属于 **L1（接口层）**，是 L0 形而上命题的形式化展开。
>
> **阅读顺序**：L0 形而上学命题 → 本文件（形式化映射）→ 各领域 Bridge 文件（具体应用）
>
> **权威分工**：
> - "潜在域 / 显现域 / 稳定域"的**形而上意义**：见 [`Core_Law/SRT_L0_Metaphysics.md`](SRT_L0_Metaphysics.md)
> - "选择有代价"的**形而上意义**：见 [`Core_Law/SRT_L0_Metaphysics.md`](SRT_L0_Metaphysics.md)
> - 本文件的职责：将上述命题**形式化**为可计算符号（L₀/L₁/L₂的方程定义、算子、κ参数等）
>
> **污染防线**：§2（规范场论）、§3（拓扑）、§4（信息论）是 L0 命题的**领域映射**，不是 L0 命题本身。
> 如果这些领域的科学理论被修正，L0 命题不受影响，但本文件对应部分需要更新。

---

## §1 Selection 的三类模型分面 (Triadic Model Aspects)

> **本节定位（2026-09-14）**：`L_0/L_1/L_2` 继续作为强有用的形式坐标，但它们不再被本文件定义成三个独立本体容器。L0 形而上意义由 `SRT_L0_Metaphysics.md` 与 Generative Ontology Spine 控制。

### §1.1 L₀ — Open / Non-Preclosed Aspect

**定义 O1**：在一个声明模型 `M` 中，`L_0^M` 表示相对于当前 determinate manifestation 尚未被该 model-cut 穷尽 / 封闭的可达或生成状态结构。

```text
L0^M = model-relative openness / accessibility construct;
!= absolute warehouse of completed possible objects.
```

历史记号 `L_0^{abs}` 不再作为 positive canonical primitive source。若旧桥接或比较文献继续使用它，只能表示“任何有限形式模型都不能穷尽 primitive Selection openness”的极限性速记，不能承载集合库存、全信息量或先在容器证明。

**定义 O1b（相对可达域）**：`L_0^{rel,M}(t)` 可以继续作为给定 formed operator / constraints 时的可访问状态空间：

$$L_0^{rel,M}(t+1)=f_M(L_1^M(t),\hat G_\theta,\text{constraints})$$

它是模型构造，不是 primitive ontology。

---

### §1.2 L₁ — Determinate Manifest Aspect

**定义 O2**：`L_1^M(t)` 表示 Selection 在模型 `M` 中的 determinate manifest / operative slice。

若采用 operator realization，可写：

$$L_1^M(t)=\mathrm{Realized}_M(\hat G_\theta, t)$$

而不是把该式读成 prior operator 产生 ontically different existence。迟滞、门控、单纯复形、topological-hole 等公式均为更强 realization / observation models。

---

### §1.3 L₂ — Retained Historical-Efficacy Aspect

**定义 O3**：`L_2` 的一般负担是先前 Selection 的差异继续实际约束后来 Selection。

```text
L2-side
= retained / sedimented historical efficacy of prior Selection.
```

固定点、attractor、迟滞累积、hardness 与可塑性阈值是某些强 stabilization models，不是普遍 ontology definition。对一个声明模型可以另定义 `L_{2,M}^{fp}` 等子类。

---

### §1.4 κ — 条件性稳定化参数 (Conditional Stabilization Degree)

> `κ` 是强 realization / model coordinate，不是 primitive Selection 的阶段计。它只在一个已声明的 `L_0^{rel,M}` / operator model 中有定义。`κ_c1/κ_c2`、spectral-gap、fixed-point 等相变解释不得被写成 L1/L2 作为独立本体物质的 universal birth theorem；意识对应尤其需要独立 bridge / empirical gate。

**定义 O3d (稳定化程度)**:

$$κ \in [0, 1], \quad κ = \frac{\text{Selection Crystallization Degree of } \hat{G}_\theta \text{ on } L_0^{rel}}{\text{Maximum Possible Crystallization}}$$

κ 的操作性近似（与已有参数的关系）：

$$κ \approx \frac{\eta}{1 + \lambda_1(L_0^{rel})/\lambda_1(L_1)}$$

其中 $\lambda_1$ 为对应域的谱隙（第一非零特征值）。κ 与 η 单调相关但不等同：
η 是单次选择的记忆权重（局部参数），κ 是系统在稳定化谱上的整体位置（全局参数）。

**两个相变临界值**:

| 临界值 | 物理含义 | 数学特征 | 本体论对应 |
|:-------|:---------|:---------|:-----------|
| $κ_{c1}$ | 秩序创生转变 | $\lambda_1(L_1) \ll \lambda_1(L_0^{rel})$，谱隙突然打开 | $L_0^{rel}$ → $L_1$ 边界 |
| $κ_{c2}$ | 收敛结晶转变 | $\hat{G}_\theta[σ] = σ$，不动点涌现，$dL_2/dt \to 0$ | $L_1$ → $L_2$ 边界 |

**κ 区间与系统状态地图**:

| κ 区间 | 对应层域 | 典型系统状态 | 跨领域实例 |
|:-------|:---------|:------------|:-----------|
| $κ \approx 0$ | $L_0^{rel}$ 主导 | 最大可能性，无稳定结构 | 量子叠加态 / 深麻醉 / 梦境起始 |
| $0 < κ < κ_{c1}$ | 相变前区间 | 亚临界涨落，不稳定显现 | 临界麻醉 / 意识边缘 / 灵感涌现期 |
| $κ = κ_{c1}$ | **L₁ 诞生点** | 谱隙打开，拓扑切断，局域化结构涌现 | 意识觉醒 / 量子坍缩 / 范式确立 |
| $κ_{c1} < κ < κ_{c2}$ | $L_1$ 区间 | 当下显现，动态维持，尚未固化 | 正常意识流 / 信念形成期 / 文化实践 |
| $κ = κ_{c2}$ | **L₂ 诞生点** | 不动点涌现，历史积累结晶 | 习惯固化 / 信仰凝固 / 制度化完成 |
| $κ > κ_{c2}$ | $L_2$ 主导 | 固化规范，高硬度，低可塑性 | 物理定律 / 深层文化信念 / 强迫症状 |

**定理 O-T3 (可塑性的相变诠释)**:

修改 $L_2$ 结构的本质，是将系统 κ 从 $κ > κ_{c2}$ 区域推回至 $κ < κ_{c2}$，
穿越相变势垒：

$$\Delta E_{required} \propto \text{Hardness}(L_2) \cdot (κ - κ_{c2})$$

这为 Ax-L2-04 的可塑性阈值条件提供了动力学基础：
$P_{L_2} > 1$ 的充要条件等价于系统有足够能量穿越 $κ_{c2}$ 处的相变势垒。

**操作化候选**（精确化ΔE_required的测量路径）：
- Hardness(L₂) 代理：信念坚定度量表（certainty scale）× 重复强化历史（习惯执行频率）
- ΔE_required 代理：认知重评实验中引发信念更新所需的反证证据数量/强度
- κ估计：谱隙λ₁代理 → EEG静息态功率谱（低频带宽/高频带宽比）

**可证伪预测**：
- FC-κ-1：高固化L₂（强迫症状/高确定性信念）被试的ΔE_required（信念更新代价）应显著高于低固化对照，且差值与κ-κ_c2估计值正相关——若无相关则"可塑性代价∝硬度×(κ-κ_c2)"的定量预测失败
- FC-κ-2：冥想训练（Cor-Med-H3：海马↑/杏仁核↓）应导致κ_c2向更低值漂移（固化门槛降低），体现为纵向信念更新速度加快——若无加速则κ_c2可塑性框架与结构可塑性证据脱节

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

**领域实现候选 O-T1（现实化的路径积分表述；保留旧编号）**:

$$L_1 = \int_{path(θ)} Structure(L_0) = \oint_γ ω_{L_0}$$

本式只在已给定可积结构、路径 $\gamma$、联络与测度的相对投影中成立。它可以建模某类 realization 的累积结构，不定义 primitive actualisation，不证明数学积分必然成为事件，也不是跨领域唯一机制。

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

## §5 不可穷尽与模态通达 (Non-Exhaustion & Modal Access)

### §5.1 $L_0^{abs}$ 不可穷尽边界

**公理 A13（保留旧编号）**：任何有限 $L_1/L_2$ 显现或形式投影都不能穷尽 $L_0^{abs}$；选择可以历史性地改变 $L_0^{rel}$ 的可达结构。

本条不把 $L_0^{abs}$ 处理为时间中的内容／基数不变量，也不把创新定义为对预成完成形式的发现。AM-A 下，受约束 actualisation 的最小 kernel 由 P0-01 作为 primitive 承载；仍开放的是各领域如何实例化它，而不是等待一个 universal fixed-point 公式把 primitive 消除。

### §5.2 模态通达关系

**定义 O11**:

$$w' \text{ accessible from } w \iff \int_{path(w→w')} Ψ_f(\hat{G}_θ) · dσ < E_{max}$$

**推论 O-C1 (通达半径)**:

$$R_{accessible} = \frac{E_{available}}{\bar{Ψ}_f} \propto d^{1.5}$$

---

## §6 领域隐喻对照表 (Cross-Domain Metaphor Table)

| 领域 | L₀ 投影实现 | L₁ 隐喻 | L₂ 隐喻 |
|:-----|:-----------|:--------|:--------|
| **物理学** | 希尔伯特空间 *(投影)* | 本征态 | 指针态 |
| **认知科学** | 可能性空间 *(投影)* | 注意焦点 | 习惯/信念 |
| **社会科学** | 文化潜能 *(投影)* | 社会实践 | 制度规范 |
| **灵性传统** | 空性/道/梵 *(最接近 $L_0^{abs}$ 的直觉指向)* | 当下体验 | 业力/轮回 |

> **注**：所有 L₀ 列中的条目均为 $L_0^{abs}$ 在该领域 $L_2$ 框架下的相对投影，而非 $L_0^{abs}$ 本身。

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
| $κ$ | 稳定化程度（仅 $L_0^{rel}$ 域有效）| §1.4 O3d |
| $κ_{c1}$ | 秩序创生相变临界值 | §1.4 |
| $κ_{c2}$ | 收敛结晶相变临界值 | §1.4 |

---

## §7 现象学不可约残差与不完备性（新增）

### 定义 O12：Qualia Residual（质感残差）

定义描述映射：
\[
\mathcal{D}: L_1^{experience} \to L_2^{description}
\]
定义残差：
\[
R_q = L_1^{experience} - \mathcal{D}^{-1}(L_2^{description})
\]
若 \(R_q\neq 0\)，表示存在不可被符号描述完全回收的现象学成分。

### 定理 O-T4：描述不完备性边界（Gödel-like Boundary）

对任意有限形式系统 \(\mathfrak{F}\subset L_2\)，存在体验态 \(e\in L_1\) 使得：
\[
\mathfrak{F}\vdash \text{structure}(e)\quad \text{but}\quad \mathfrak{F}\nvdash \text{qualia}(e)\text{ equivalence}
\]
* **Implication**：SRT 方程可建模“如何生成与约束体验”，但不等价于“替代该体验本身”。

## §8 算子个体化相变（Operator Individuation Phase Transition, 新增）

### 定义 O13：Shared-to-Individual Ledger Split
在共具身初态，母胎共享部分选择账本：
\[
\mathcal{L}_{shared}=\{d,\Psi_f,E_{maint}\}_{mat\leftrightarrow inf}
\]
当满足独立结算条件（呼吸/代谢/内稳态闭环）时发生账本分裂：
\[
\mathcal{L}_{shared}\xrightarrow[]{\kappa_{split}>\kappa_c}\mathcal{L}_{mat}\oplus\mathcal{L}_{inf}
\]

### 定理 O-T5：个体化临界定理
若
\[
\frac{\partial}{\partial t}\Big(\frac{E_{self-maint}^{inf}}{E_{external-support}^{mat}}\Big)>0\ \land\ B_{self}>\tau_B
\]
则 \(\hat{G}_{inf}\) 从嵌套子程序跃迁为独立算子，具备独立 \(d\) 与 \(\Psi_f\) 结算池。
* **Implication**：主体间性先于个体性，但个体性可通过动力学相变严格定义。

## §9 跨位置对象与偶发性边界

### O14（历史符号用法，C-A 撤回）

旧版曾把 $\Omega$ 定义为所有局部算子共享的 Non-Entity Global Operator。该定义现已撤回：bare $\Omega$ 依 `_SRT_SYMBOL_TABLE.md` 只表示 **Ontological Consistency**，不得再表示投影源、本源地平线或宇宙级最优。SRT 当前不以单一全局算子解释局部算子的谱系；跨尺度连续性须按 A12／A15 在具名结构、映射与失败条件下逐对建立。

### 定理 O-T6：Pure Contingency of Manifest States
对任意 \(s\in L_1\) 与 \(r\in L_{2,\theta}\)：
\[
\neg\Box s\ \land\ \neg\Box r
\]
即其存在不具自足必然性，需持续选择支付维持：
\[
\text{Maintain}(L_1)\Rightarrow \int \Psi_f\,dt>0
\]

### 定理 O-T7：\(L_1\) 非自足定理（Theorem of \(L_1\) Contingency）
\[
F[L_1] > 0\quad \text{for any finite instantiated slice }L_1
\]
因此 \(L_1\) 不包含其自身存在的充分理由，只能作为被持续“赋予”的显现态：
\[
L_1(t+\Delta t)=\hat G_\theta[L_0(t)]\ \text{(iterative donation of existence)}
\]

### Hyp-O8（撤回／停驻）：$L_0^{abs}$ 与全局算子极限同一

该假设因符号冲突、无穷极限未定义及位置无关对象负担而撤出当前正面理论。未来若重开，须另立作者门、不得使用 bare $\Omega$，并先给出有限算子到所提对象的 epistemic bridge 与失败条件。

### O15（C-A 撤回／停驻）：Truth–Goodness–Beauty as L0 Optimal Manifolds

> **C-A（2026-08-12）**：下列段落保留为历史高承诺假设，不再是当前 definition，也不得承重 canonical 推导。它把真／善／美写成 $L_0^{abs}$ 中的位置无关评价最优对象，正是 C-A 不予准入的 universe-wide semantic／evaluative optimum。复活条件见 `_SRT_PARKED_INDEX.md`。

> **[R]** 柏拉图理念论（Republic ~375 BC）：真善美为超越具体事物的普遍形式（Εἶδος）。新柏拉图主义的"至善"（Plotinus）。**[H — 高承诺框架假设]** 以下 SRT 形式化为高风险主张：将柏拉图理念操作化为 L₀ 中的优化流形，使神学/美学/伦理学与 SRT 本体论结构接轨。

\[
\mathcal{M}_{TGB}\subset L_0^{abs},\quad \mathcal{M}_{TGB}=\arg\min_{\mathcal{M}}\big(\Psi_f(\mathcal{M})+\lambda_F F(\mathcal{M})\big)
\]

**符号说明**：
- $F(\mathcal{M})$：**[操作化缺口]** 候选定义：① Friston 变分自由能（$F = \text{KL}[q(\theta)||p(\theta)] - \ln p(\text{data})$，越高=与数据越不一致）；② 热力学自由能（$F = U - TS$，越高=更不稳定）；③ 信息整合度的倒数（$F = 1/\Phi$，$\Phi$ 为 IIT 中的整合信息量）。三种候选预测不同的 $\mathcal{M}_{TGB}$ 结构，需实验区分。
- $\lambda_F$：$\Psi_f$ 与 $F$ 的权衡参数（量纲由 $F$ 定义决定），当前状态 = 自由参数（**待定，非可伪**）。
- $\mathcal{M}_{TGB}$：**单一流形还是三个？** 当前写法将真善美合并为一个流形族。SRT 的保守版本：三者各有独立优化目标（$\mathcal{M}_T, \mathcal{M}_G, \mathcal{M}_B$），但在 L₀ 中存在交集（$\mathcal{M}_T \cap \mathcal{M}_G \cap \mathcal{M}_B \neq \emptyset$）——此交集为柏拉图"至善"的 SRT 对应。

其中 $\mathcal{M}_{TGB}$ 表示在信息几何上具有**高一致性**（内部 $\Psi_f$ 低）/**高可整合性**（$\Phi$ 高 / $|Aut(L_2)|$ 大）的最优流形族。

**⚠️ 可证伪性问题（关键张力）**：M_TGB ⊂ L₀^abs 将真善美定位于不可直接观测的 L₀ 层——若 L₀ 不可测，此定义在当前形式下**无法直接证伪**。SRT 的处理策略：以 L₁ 代理间接测试：若高对称性/高整合性的 L₁ 结构（艺术作品、数学证明、伦理行为）在跨文化普遍性上与 M_TGB 预测的"低 Ψ_f + 低 F"结构一致，则间接支持此定义；反之若跨文化差异系统性高（美的标准完全文化特定），则定义需退化为"L₂吸引子"而非"L₀流形"。

**证伪条件（间接，[H]）**：
- 若数学美感（数学家对证明优雅性的评价）与 MDL/对称性度量无相关（控制熟悉度后），则"美=低 Ψ_f 流形"假设失效。
- 若跨文化伦理共识（真善）不比随机选取的文化规范更与 Ψ_f 最小化结构一致，则定义需降级为框架隐喻而非操作化假设。

### 定理 O-T8：Embodied Bliss Asymptote（具身至福渐近定理，新增）
对任何具身算子 \(\hat G_\theta\) 若保持 \(L_1\) 显现连续：
\[
\Psi_f(t)\ge \Psi_{min}^{+}>0
\]
因此“绝对至福”在具身态只可渐近：
\[
\lim_{t\to\infty}\Psi_f(t)=\Psi_{min}^{+}\neq0
\]
* **Implication**：SRT 允许“趋近完满”，但拒绝“运行中零摩擦且仍保持个体显现”的自相矛盾写法。

### 定义 O16：Non-Redundant Persistence Criterion（非冗余持续判据；EX-A 更新）
对任意尺度对象 \(X\) 定义：
\[
\text{Persist}(X\mid\theta)\iff \Psi_f^{maint}(X,\theta)>0
\]
即对象是否需要非零摩擦才能维持其稳定显现，不由它是否可还原决定。EX-A 下，这只判别持续对象性，不判别一个确定事件是否已经实际发生。

### 定理 O-T9：Scale-Orthogonal Coexistence（尺度正交共存定理，新增）
\[
X_{macro}=\hat G_{\theta_{macro}}[L_0],\quad X_{micro}=\hat G_{\theta_{micro}}[L_0]
\]
若二者由同一 \(L_0\) 在不同 \((d,\rho)\) 下投影，则可并存而不互斥：
\[
X_{macro}\perp_{scale} X_{micro}
\]
* **Implication**："table" 与 “particles arranged tablewise” 是正交切片，不是互相消灭关系。

### 定义 O17：Anti-Semantic-Evasion Principle（反语义逃避原则，新增）

a) 反廉价本体赋值：
\[
\text{Exist}_{lang}(X\mid L_2)\ \not\Rightarrow\ \text{Exist}_{dyn}(X\mid\Psi_f^{maint}>0)
\]

b) 跨尺度连通约束：
\[
\forall X_{macro},\exists\,\pi_\lambda:\ X_{micro}\xrightarrow[]{\pi_\lambda}X_{macro},\quad
\mathcal{C}_{link}(X)=\mathbb{I}[\Psi_f\text{-consistent}] = 1
\]
即不同尺度对象不能仅以词汇分区隔离，必须在粗粒化映射与摩擦预算上可连通。

c) 双重存在标准（语言层 vs 动力学层）：
\[
\text{Exist}_{L_2}^{label}\ \text{is permissive},\qquad
\text{Exist}_{L_1}^{anchor}\ \text{is constrained by}\ \Psi_f
\]

### 定义 O18：Real Pattern Compressibility Criterion（真实模式可压缩性判据，新增）
对给定尺度参数 \((\theta,\rho)\) 与对象候选 \(X\)，定义条件复杂度代理：
\[
K_\theta(X)\equiv K(X\mid\theta,\rho)
\]
定义模式现实度：
\[
\mathcal{R}_{pat}(X\mid\theta,\rho)=\frac{1}{1+K_\theta(X)}\cdot \mathbb{I}[\Psi_f^{maint}(X,\theta)<\infty]
\]
若 \(\mathcal{R}_{pat}>0\)，则该模式在相应尺度具“可操作实在性”。

### 定理 O-T10：Compressibility–Friction Coupling（可压缩性-摩擦耦合定理，新增）
\[
\Psi_f^{maint}(X,\theta)\propto K_\theta(X)
\]
在同一任务边界下，表征越可压缩，维持其显现边界所需摩擦支付越低，因此在 \(L_1/L_2\) 中越稳定。

### 定义 O19：Underdetermination as Potential Interface（欠定性即潜能接口）

给定感觉切片 $y_t \in L_1$，其前像集合定义为：

$$\mathcal{P}(y_t) = \{x \in L_0 \mid D_{KL}(\hat{G}_\theta(x) \,\|\, y_t) < \varepsilon(\rho)\}$$

其中 $D_{KL}$ 为 KL 散度，$\varepsilon(\rho)$ 为随算子分辨率 $\rho$ 降低而增大的容差函数（$\rho \downarrow \Rightarrow \varepsilon \uparrow \Rightarrow |\mathcal{P}| \uparrow$）。

**本体论自由度（$DOF_{onto}$）**：欠定性的连续谱量化：

| $DOF_{onto}$ | 状态 | 算子行为 | 典型案例 |
|:-------------|:-----|:---------|:---------|
| $\approx 0$ | 决定论锁定 | 被动读出，无选择空间 | 简单物理反射、刚体碰撞 |
| 低（1–10）| 局部歧义 | 模式识别，二选一/多选一 | 鸭兔错觉、多义词 |
| 高（$10^n$）| 高度欠定 | 主动投影，重度依赖 θ | 罗夏墨迹、复杂社会情境 |
| $\to\infty$ | 全潜能态 | 自由创作/虚无锚定 | 纯粹 $L_0$ 接入、梦境起始 |

**动力学预测**：本体论摩擦 $\Psi_f$ 随 $DOF_{onto}$ 对数增长——欠定性越高，锚定代价越大。

当 $DOF_{onto} \gg 1$ 时，系统处于欠定接口：对象边界需由算子选择与**自创生闭包**（Autopoietic Closure，见 Ax-ONT-1b）共同生成，而非从输入中直接读出。自创生闭包意指当前 $L_1$ 的锚定反馈维持 θ，形成稳定回路，将从 $\mathcal{P}$ 中选出的 $x$ 锁定为「现实」。

**创造力的 SRT 定义（$\mathcal{C}$）**：

$$\mathcal{C} \propto \frac{|\mathcal{P}(y_t)|}{P(\sigma \mid L_2)}$$

创造力 = 算子突破 $L_2$ 惯性（默认选择路径），在庞大前像集合中锚定低概率但自洽的 $x$ 的能力。前像集合越大（欠定性越高）、选中状态偏离既有规范（$L_2$）越远，创造性越高。若无欠定性，每个刺激只对应唯一现实，系统将永远锁死在 $L_1 = L_2$ 的惰性回路，艺术、科学假说与进化皆不可能。

**Implication**：欠定性定义了系统的演化带宽。高欠定性接口允许算子执行「本体论实验」——通过改变 θ 探索 $L_0$ 中未被 $L_2$ 覆盖的深层结构。**欠定性不是感官的贫瘠，而是现实的肥沃。**

### 定义 O20：Friction-Minimizing Grouping Principle（最小摩擦分组原则，新增）
对候选分组 \(\mathcal{G}=\{G_k\}\) 定义目标泛函：
\[
\mathcal{J}(\mathcal{G}\mid\theta,\rho,d)=\sum_k\Big(\mathcal{L}_{pred}(G_k)+\lambda_1\Psi_f^{maint}(G_k)+\lambda_2\mathcal{C}_{switch}(G_k)\Big)
\]
\[
\mathcal{G}^*=\arg\min_{\mathcal{G}}\mathcal{J}(\mathcal{G}\mid\theta,\rho,d)
\]
对象组合的本体论标准不是“几何均匀连通”或“无语境压缩最短”，而是在给定任务与关切下的可维持最小代价。

### 定理 O-T11：Compositional Stability under Care-Weighted Grouping（新增）
\[
\partial_d\,\mathcal{J}(\mathcal{G}\mid\theta,\rho,d)<0\ \Rightarrow\ \text{grouping robustness}\uparrow
\]
当分组与系统关切梯度 \(d\) 同向时，整体对象边界在跨时预测中更稳定（如斑马整体优于条纹碎片）。

### 定义 O21：Consensus Friction in L2 Formation（共识摩擦，新增）

> [R→Schelling 1960 *The Strategy of Conflict*（协调均衡/Schelling点：多主体在无沟通条件下收敛到L₂共识的博弈论基础——共识摩擦≈协调失败代价）; Clark & Brennan 1991 "Grounding in Communication" *Perspectives on Socially Shared Cognition*（共同基础理论：跨主体理解需要"着地"过程，每次着地失败=Ψ_f^consensus增量）; Tomasello 1999 *The Cultural Origins of Human Cognition*（共享意向性：人类L₂共识的发育基础，黑猩猩缺乏共享意向性→无法建立低Ψ_f^consensus的文化积累）; Levinson 2000 *Presumptive Meanings*（语用推断：默认意义系统降低日常交流的共识摩擦代价）]

对多算子集合 \(\{\hat G_{\theta_i}\}_{i=1}^n\) 定义协议偏差代价：
\[
\Psi_f^{consensus}=\sum_{i<j} w_{ij}\,D\big(\mathcal{S}_{Px}^{(i)},\mathcal{S}_{Px}^{(j)}\big)
\]

> **符号说明**：$\mathcal{S}_{Px}^{(i)}$ 为算子i的"对象-属性感知结构"（Object-Property Perception Structure），即算子i在当前任务下对相关对象集合的属性分配/边界划分的完整描述（参见 `Core_Law/SRT_Reference_Ontology.md` §定义O12-O15 对象归属定理组）。

> **D度量候选**（需按情境选择）：
> - **离散感知结构**（如概念分类/范畴边界）：$D = 1 - \text{Jaccard}(\mathcal{S}^{(i)}, \mathcal{S}^{(j)})$ 或对称KL散度
> - **连续表征空间**（如语义嵌入/fMRI激活模式）：$D = 1 - \text{CKA}(\mathcal{S}^{(i)}, \mathcal{S}^{(j)})$（中心核对齐，尺度不变）
> - 默认：对称KL散度（$D_{KL}^{sym} = D_{KL}(P\|Q) + D_{KL}(Q\|P)$），满足非负性与对称性

> **w_ij参数化**：$w_{ij} = w_{ji} \geq 0$（对称权重，反映算子i和j之间的协作依赖强度）；通常归一化为 $\sum_{i<j} w_{ij} = 1$ 以使Ψ_f^consensus在算子对数变化时可比。在实践中w_ij可代理为协作频率/组织依赖度/沟通带宽等。

其中 \(D\) 衡量对象-属性结构协议差异。\(\Psi_f^{consensus}\) 越高，协作失败与跨主体误解成本越高。

* **R/H 区分**：
  - [R] 共识失败成本的博弈论/通信理论基础（Schelling/Clark&Brennan）；人类共享意向性的发育证据（Tomasello）
  - [H] **SRT形式化**：将跨主体协议差异形式化为加权对距离和 Ψ_f^consensus，并将其纳入SRT的本体论摩擦体系——使"共识"成为可量化的摩擦成本而非社会学描述

* **操作化候选**（Ψ_f^consensus的实验代理）：
  - 协作解题任务：两人（或多人）在物体命名/分类任务上的初始分歧率（歧义率 = Jaccard差异的行为代理）
  - 跨文化概念调查：不同文化组对同一刺激集的属性评分的平均Wasserstein距离（Word & Language Survey等数据集）
  - 神经层：fMRI跨被试表征相似度（ISC, Inter-Subject Correlation）的反转值（ISC↓ = Ψ_f^consensus↑）

* **可证伪预测**：
  - FC-Cons1-1：在协作任务中，算子对之间的初始对象分类分歧率（D代理）应与协作总任务时间（效率代理）正相关（r > 0.4）——高共识摩擦=更多着地时间消耗（Clark&Brennan grounding cost机制）；若无相关则Ψ_f^consensus对协作效率的预测力不成立
  - FC-Cons1-2：跨文化协作中，文化间概念差异（通过跨语言嵌入距离量化）应预测协作错误率（误解/重做次数）；若文化概念距离与协作错误率无关则跨主体表征差异-误解联结失败

### 定理 O-T12：L2 Convergence under Shared Constraint（新增）
若算子族共享近似参数簇 \(\theta_i\approx\theta_j\) 且处于共同任务环境：
\[
\frac{d}{dt}\Psi_f^{consensus}<0\ \Rightarrow\ L_2\ \text{attractor emerges}
\]
即“看见同一对象”可由摩擦最小化收敛解释，无需预设绝对指称实体。

### 定理 O-T13：Hierarchical Persistence Candidate（层级持续候选；EX-A 更新）
对任意层级 \(\lambda\) 的模式 \(X_\lambda\)，若存在吸引盆：
\[
\exists\,\mathcal{A}_\lambda:\ \nabla \Psi_f(X_\lambda)=0,\quad \nabla^2\Psi_f(X_\lambda)\succ 0
\]
则该层级在对应分辨率下具持续对象性候选：
\[
\text{Persist}(X_\lambda\mid\rho_\lambda,\theta)=1
\]
因此宏观对象与微观组成在不同 \(\rho\) 下可并行持续，不构成互斥。吸引盆只支持该层级的维持，不能反向定义第一次显现实在性。

## 【理论边界/防误用声明】
- 不采纳“形式化失败=反科学神秘主义”推论：不完备性是层级边界，不是否定建模价值。  
- 不采纳“任何主观报告都不可检验”推论：可检验的是结构/动力学关联，不是体验的可替代性。  
- 不采纳“出生时刻=唯一个体化时刻”的机械化推论：SRT 采用多指标临界条件。  
- 不采纳“\(\Omega\)=宇宙内超级实体/人格化造物主”的推论：\(\Omega\) 在 SRT 中是操作逻辑，不是对象实体。  
- 不采纳“\(L_0^{abs}\)-\(\Omega\) 极限同一假设已被证明”的推论：其当前为研究态桥接假设。  
- 不采纳“至福=现实终止的规范性处方”推论：O-T8 仅给出具身动力学边界，不导出伦理命令。  
- 不采纳“存在仅当可被某科学语言变量绑定”之扁平推论（蒯因式强化版本）：在 SRT 中，显现实在性首先由 \(L_0\to L_1\) primitive actualisation 准入；锚定支付处理其持续，语言变量是后验 \(L_2\) 编码。
- 不采纳“可还原=可消除”的推论：还原关系不取消在该尺度上的摩擦支付与显现合法性。  
- 本文件承认描述层与体验层的不可约差异，但不允许以此逃避可证伪义务。


## §10 主动推断高阶道路的本体论重写（新增）

### 定义 O22：External-State Construction Clause
在 SRT 中，“外部状态”不是先验给定对象，而是：
\[
\eta_{ext}(\theta,t):=\hat{G}_\theta[L_0]\ \text{在边界条件下的投影产物}
\]

### 定理 O-T14：Projection-First Ontology
\[
\text{No }\hat{G}_\theta\Rightarrow \text{no determinate }\eta_{ext}\text{ in }L_1
\]
即：先有选择投影，再有可指称外部态。

### 定义 O23：Blanket Payability Condition
\[
\text{Agenthood} \iff B_{MB}\land d>0\land \Psi_f\text{-payable}
\]

## 【理论边界/防误用声明】
- 不采纳“外部状态先于一切选择边界而独立完备给定”的推论。  
- 不采纳“统计边界足以推出意识本体”的推论。  

<!-- Selection-totality scope marker (2026-09-14): primitive ontology is owned by SRT_L0_Metaphysics.md / SRT_Generative_Ontology_Spine.md; this file remains a formal / realization interface. -->
