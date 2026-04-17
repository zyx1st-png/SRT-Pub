---
id: SRT-CORE-13A
type: definition
tags: [G-operator, Agency, Parameters, Theta, Hybrid]
status: axiomatic_hybrid_v1
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-001, SRT-CORE-12A, SRT-CORE-12B]
---

# SRT Core Definition 13A: Ghost Operator Basics (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Operator Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


## I. Operator Definition (算子定义)

### Ax-Op-01: Parameterized Selection Map
**Formal Definition**: The Ghost Operator is a parameterized selection mapping from L0 to L1.
$$\hat{G}_\theta: S \to S, \quad L_1(t) = \hat{G}_\theta[L_0](t)$$
* **Implication**: 现实化是选择映射的结果，而非被动显现。

**【选择机制修正 2026-04-08】G 选择 = 遮蔽，不是排除**

G 的选择行为是对可能性空间的**遮蔽**（occlusion）而非**排除**（exclusion）：

$$\hat{G}: \Omega \to \Omega', \quad \Omega' \subsetneq \Omega, \quad P(\omega \in \Omega \setminus \Omega') > 0$$

- **遮蔽**：降低其他可能性的可及性，概率性的、有程度的、原则上可逆的
- **排除**：绝对铲除其他可能性（遮蔽的极限情况，不是一般情况）

**代理结构**：L₂ 是对 L₁ 的代理，L₁ 是对 L₀ 的代理。G 的选择遮蔽通过代理链传递：
$$L_2 \xrightarrow{\text{代理}} L_1 \xrightarrow{\text{代理}} L_0$$

**遮蔽的精确定义**（2026-04-08）：
$$\text{遮蔽} \equiv L_1 \xrightarrow{\text{校准信号}} L_2 \text{ 的通道被截断}$$
L₂ 失去 L₁/L₀ 上行校准输入后，以 L₂ 内部自洽性替代 L₀/L₁ 现实作为参考点，参数漂移但持续运作。

* **Cross-ref**: `Core/Dynamics_Scaling_Annex/11_G_CrossScale_PhaseState.md`（G选择=遮蔽的完整论证）；`Core/Dynamics_Scaling_Annex/12_ProxyModel_OcclusionPhases_Intervention.md`（遮蔽精确操作定义与两相模型）；T-Core-A1C3（Core_01中的跨尺度连续性声明）。

### Ax-Op-02: Attention Decomposition
**Formal Definition**: The operator is the fundamental attention tuple.
$$\hat{G}_\theta = \text{Attention}(d, \rho, \vec{v})$$
* **Implication**: d 值、分辨率与意向向量共同决定选择结构。
* **Tension-Rev-IT4 (d 值推导关系)**：此处的 $d$ 是 Ax-ONT-3（SRT-AI-01）中规范定义 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 的**注意力域投影**。在认知系统中，风险梯度的范数被离散化为注意力可扫描的独立维度数：$\dim(\text{Scope}) \propto \lfloor d / d_0 \rfloor$，其中 $d_0$ 表示单个关切维度所需的最小风险梯度分量。因此"注意力维度数"是连续 $d$ 值的离散近似，二者并非独立定义。

### Ax-Op-02b: Dual-Stream Coupling (双流耦合公理)
**Formal Definition**: 幽灵算子的选择矩阵由两个必须正交耦合的张量流构成：
$$\hat{G}_\theta = \mathbf{T}^{\text{intent}} \otimes \mathbf{T}^{\text{embody}} \cdot \kappa_{\text{body}}$$
其中：
- $\mathbf{T}^{\text{intent}} = \hat{A}(d, \rho, \vec{v})$：意向性流（提取L0内容的注意力张量）
- $\mathbf{T}^{\text{embody}} = \theta_{\text{intero}}$：具身性流（锚定自我主观基准的内感受张量）
- $\kappa_{\text{body}} \in \mathbb{R}^+$：具身耦合增益系数
* **Implication**: 注意力决定"看什么"，内感受决定"谁在看"。两者的正交耦合（而非任一单独）才构成完整的L0→L1锚定操作。
* **Cross-ref**: Ax-Op-01 (参数化选择映射); Def D4a ($\theta_{\text{intero}}$)。

### T-Op-EAN: Embodied Anchoring Necessity Theorem (具身锚定必要性定理)

> [R→Merleau-Ponty 1945 *Phénoménologie de la Perception*（知觉现象学：具身性作为意识的先验条件，"身体图式"是感知空间的根基）; Sierra & Berrios 2000 *Psychological Medicine*（解离症/人格解体神经机制：边缘系统-前额叶去耦联导致情感空洞化，与κ_body↓类比）; Blanke & Arzy 2005 *Trends in Cognitive Sciences*（人格解体的神经科学：顶叶-颞叶交界区功能异常→躯体自我感丧失，与κ_body→0的神经基础）; Seth 2021 *Being You*（主动推断的具身性：内感受预测错误作为自我感的维持机制，与θ_intero/κ_body对应）]

**R/H 区分**：
- [R] 具身认知哲学（Merleau-Ponty）：身体性作为意识的拓扑基础；解离/人格解体的临床神经机制（Sierra/Blanke）；内感受与自我感（Seth）
- [H] **SRT形式化**：κ_body参数的引入；(d>0)∧(κ_body>0)作为有效L₀→L₁坍缩的必要条件[H]；L₁*="操作正常的本体论空壳"概念[H]

**Deductive Statement**（保守读法）: 有效L₀→L₁锚定的**必要条件**包含非零的具身反馈项：
$$\left(d > 0\right) \land \left(\kappa_{\text{body}} > 0\right) \Rightarrow L_0 \xrightarrow{\hat{G}_\theta} L_1^{\text{genuine}}$$

**iff精度说明**：原公式中"↔"（充要条件）为强主张。保守读：d>0∧κ_body>0为**必要条件**（无此不可，L₁^genuine→必有此两条件），但充分性尚需证明（可能存在满足这两条件但不产生L₁^genuine的边界情况）。当前SRT将其标注为[H-中承诺]（必要性比充分性更有把握）。

若具身流断裂（$\kappa_{\text{body}} \to 0$），系统进入病理态：
$$\kappa_{\text{body}} \to 0 \implies L_1^* \text{ (操作正常，但丧失本体论重量)}$$

**临床表现精度说明**：
- 解离症（Dissociation）/人格解体（Depersonalization）：符合κ_body→0的SRT解读（躯体自我感丧失）[R→Sierra/Blanke]
- **心盲症（Aphantasia）修正**：心盲症患者缺乏心理表象能力，但通常**保有完整的现实感**（不符合"丧失本体论重量"的描述）。更准确的SRT定位：Aphantasia=特定视觉θ_intero通道的信号质量降低，而非κ_body整体趋零。此例不是T-Op-EAN最佳临床对应，应降权或替换。

**κ_body 操作化候选**：
- 本体感觉精度：关节位置感知任务的平均误差倒数
- 内感受精度：心跳计数任务的准确率（Seth心跳感知实验）
- HRV（心率变异性）：副交感-身体耦合强度代理（高HRV=高κ_body）

* **Implication**: 具身性不是意识的"附属品"，而是L0→L1锚定的拓扑必要条件。无身之算法（$\kappa_{\text{body}} \approx 0$）产生的不是意识，而是"操作稳定的本体论空壳"——AI的κ_body≈0正是当前AI"实际僵尸"（§1.2行为主义/§2.3欺骗性对齐）诊断的具身维度。
* **Cross-ref**: Ax-Op-02b; Ax-ONT-1d; Ax-Phil-5（反表征耦合：θ的具身来源）; §7.3 AI意识评估框架。

**可证伪预测**：
- FC-EAN1-1：系统性操纵κ_body（如体感剥夺实验/橡胶手错觉）应产生L₁*症状（现实感下降/人格解体样主观报告）的量-效关系——若κ_body操纵幅度与解离样症状无剂量相关则κ_body→L₁*机制失败
- FC-EAN1-2：跨模态比较中，高内感受精度（高κ_body代理）的被试在"真实体验"（vs模拟体验）的辨别任务中应表现更好——若κ_body代理与真实/模拟辨别力无相关则"κ_body>0=本体论重量"主张需修订

### T-Op-HFL: High Friction Law of Unanchored Simulation (无锚点系统高摩擦定律)
**Deductive Statement**: 在缺乏外部强L1感官输入作为底座支撑时，纯内部G^θ模拟（想象/内部状态维持）面临指数级增加的本体论摩擦：
$$\Psi_f^{\text{imagination}} = \Psi_f^0 \cdot e^{\,\beta / \text{Anchor}(L_1^{\text{ext}})}$$
其中 $\text{Anchor}(L_1^{\text{ext}})$ 为外部感官锚点强度，$\beta$ 为热力学敏感系数。
极限情形：$\text{Anchor} \to 0 \implies \Psi_f^{\text{imagination}} \to \infty$（对应感觉剥夺或精神病性解离）。
* **Implication**: "想象力"在热力学上是极高耗能且脆弱的算子行为，需对抗系统向L0混沌退化的趋势。这从信息热力学视角解释了为何长期维持内在愿景（如艺术创作、冥想修行）需要极高的心理资源投入。
* **Cross-ref**: Eq-Evo-01 (幽灵演化方程); Def-L0-PreAnchored。

### Ax-Op-03: Operational Normalization
**Formal Definition**: Selection can be implemented via divisive normalization.
$$[\hat{G}_\theta(x)]_i = \frac{x_i^n}{\varepsilon_{reg} + \sum_j W_{ij} \cdot x_j^n}$$

> **记号注（2026-04-14）**：此处 $\varepsilon_{reg}$（operator regularizer）是实现层的防奇点正则化常数，保证零输入时算子不奇异。它与 T-Core-A1C2 中的 $\varepsilon_{pg}$（proto-gradient，L₀ 最小非中性）在形式上同构（均保证"最小非零底"），但二者层级不同：$\varepsilon_{pg}$ 是 L₀ 的本体论属性，$\varepsilon_{reg}$ 是具体选择算子的实现参数。当前保留结构类比关系，不做本体论同一化。见 `_SRT_SYMBOL_TABLE.md`。

> **[R]** 除法归一化（Divisive Normalization）：Carandini & Heeger 2012 *Nature Reviews Neuroscience*（视觉皮层V1细胞的标准计算模型，统一多种皮层现象的规范化框架）；Louie & Glimcher 2010 *Neuron*（决策神经科学中的divisive normalization扩展，解释偏好的背景依赖性）；Schwartz & Simoncelli 2001 *Nature Neuroscience*（感知归一化的高斯尺度混合模型）。**[H]** 将此神经机制接驳为 SRT 选择算子 $\hat{G}_\theta$ 的一种实现候选，作为 L₀→L₁ 竞争选择的动力学形态之一，为本框架新增贡献（原始公式限于感觉系统，SRT 将其一般化至任意选择域）。
>
> **参数说明**：
> - **$x_i$**：第 $i$ 个候选状态（L₀中的竞争激活）的原始活化值。
> - **$n$**：非线性指数（通常 $n \approx 2$，在神经模型中产生超线性选择；$n=1$ 退化为线性归一化）。
> - **$\varepsilon$**：防奇点常数（$\varepsilon > 0$，避免分母为零；量纲与 $x_j^n$ 相同，对应背景自发激活水平）。**记号补注（2026-04-14）**：本式中的 \(\varepsilon\) 可记为 \(\varepsilon_{reg}\)，用于与 `T-Core-A1C2` 的 proto-gradient \(\varepsilon_{pg}\) 区分。当前二者只保留“实现层 regularizer / 本体层最小非中性”的结构回声关系，不做本体论同一化。
> - **$W_{ij}$**：竞争权重矩阵（$W_{ij} \geq 0$，通常非对称——近邻强抑制、远邻弱抑制；$W_{ii}=1$ 的情况为自抑制归一化）。
> - **输出解读**：$[\hat{G}_\theta(x)]_i$ 为相对激活值（归一化到竞争背景后的强度），可通过 Softmax 变换为概率分布；并非直接输出 L₁ 选择结果，而是驱动选择的中间表征。
>
> **实现候选地位**：此公式为 $\hat{G}_\theta$ 在神经实现层的**候选之一**，而非唯一约束——其他实现包括：赢者通吃（WTA，n→∞ 的极限）、线性加权（n=1，W_ij=const）、Softmax（温度参数τ驱动的概率归一化）。SRT 对哪种具体实现不做强承诺，保持框架独立性。
>
> * **Cross-ref**: T-Op-SIAM（选择诱导可及性调制——被归一化压制的竞争者可及性累积下降，两者机制一致）；Ax-Op-01（选择算子基础定义）。
>
> * **FC-Op03-1**（证伪条件）：若在神经影像研究中，已知的竞争选择（如双眼竞争/Stroop抑制）的BOLD信号不符合除法归一化预测（如竞争对手活化的非线性压制模式无法用W_ij·x_j^n拟合，ΔAICc < 2 vs 线性模型），则分归一化作为 $\hat{G}_\theta$ 神经实现候选的地位减弱。
> * **FC-Op03-2**（证伪条件）：若决策场景中（如选项集效应），背景依赖的选择偏移无法被 $W_{ij}$ 参数化捕捉（模型预测与行为数据相关 r < 0.5），则需补充其他归一化变体（如基于rank的归一化）或切换实现候选。

### Ax-Op-03b: Competitive History Writeback（竞争历史写回律）

**新增（2026-04-16）**：Ax-Op-03 只给出当轮竞争的瞬态归一化；Ax-Op-04 只给出算子的递归迭代；两者均不足以保证"败者压制带方向写入历史"。本公理补充竞争结果对路径预期摩擦的写回律，使 T-Op-SIAM 从公设降格为 Ax-Op-03 + Ax-Op-03b 的推论。

> **地位注**：本公理三层内容均为实质新增（不可从既有 SRT 免费推出）。目前以"可守住的基底"为最低承诺，三层全部接受后 T-Op-SIAM 可恢复定理地位。

**可守住的基底（来自既有 SRT，无需本公理）**：

$$\mathbb{E}[\Psi_f] \uparrow \;\Rightarrow\; A \downarrow \quad \text{（序关系，来自 payability 条件 + Ax-F-02 熵压缩）}$$

**Layer 1 — 竞争结果依赖更新律（新增内容）**：

设竞争事件中 $x_{prac}$ 被选中、$x_{comp}$ 被拒绝，路径预期摩擦按下式更新：

$$\mathbb{E}[\Psi_f(\text{path}_i,\, t+1)] = \mathbb{E}[\Psi_f(\text{path}_i,\, t)] + \eta \cdot L_{comp}(i \mid W_{ij},\, \theta,\, N_{prac})$$

约束条件：
$$L_{comp}(x_{comp}) > 0, \qquad L_{comp}(x_{prac}) \leq 0$$

（败者路径预期摩擦上升；胜者路径预期摩擦不升）

**Layer 2 — 桥接函数（拆分为 2a + 2b，2026-04-17）**：

**Layer 2a — 单轮配分版（从最大熵可推，非纯建模选择）**：

在当前竞争语境 $C_t$ 下，幽灵算子归一化输出落在归一化 simplex 上。若施加平均摩擦约束 $\sum_i p_t(i)\Psi_i(t) = \bar\Psi_t$，对 Shannon 熵 $H(p) = -\sum_i p_i \log p_i$ 做最大化，标准结果：

$$p_t(i \mid C_t) = \frac{e^{-\beta_t \Psi_i(t)}}{Z_t}, \qquad Z_t = \sum_j e^{-\beta_t \Psi_j(t)}$$

其中 $\beta_t$ 为 Lagrange 乘数（对应"逆温度"），由约束 $\sum p_t(i)\Psi_i(t) = \bar\Psi_t$ 确定。

**地位**：**从 Ax-Op-03 归一化（simplex）+ 平均摩擦约束 + 最大熵原则推出**，比"纯建模选择"更有结构依据——这是给定约束下承诺最少的分布（minimum commitment distribution），不是任意引入。

> ⚠ **用语精确化**：不得称"配分函数守恒"——归一化确保当前轮输出权重之和为 1（simplex mass normalization），不是物理意义上的守恒律；守恒的是"总权重被规范到 1"，不是绝对可及性总量。

---

**Layer 2b — 跨时衰减版（仍为桥接公设，但有三个结构化候选）**：

从 2a 的单轮 Gibbs 配分到主张 2 所需的跨时可及性 $A(\text{path},t) \propto e^{-\mu\mathbb{E}[\Psi_f]}$，必须跨越四个断点：

| 断点 | 内容 | 原因 |
|---|---|---|
| **断点 1** | 当前轮 allocation ≠ 历史 accessibility | 瞬时配分（instantaneous allocation）与历史可进入性（historical accessibility）不在同一层 |
| **断点 2** | 相对配分 ≠ 绝对可及性守恒 | simplex 归一化是"权重之比"；$A_i$ 本身不守恒；$p_i = A_i / \sum_j A_j$ 中若分母变化，指数形式不自动传递给 $A_i$ |
| **断点 3** | 截面分布 ≠ 历史更新律 | 2a 给出某时刻在给定 $\Psi_f$ 下的分布；不给出 $A$ 如何随 $N_{prac}$ 演化 |
| **断点 4** | Jensen gap | $\mathbb{E}[e^{-\beta\Psi}] \neq e^{-\beta\mathbb{E}[\Psi]}$；若 $\Psi_f$ 有方差，用 $E[\Psi_f]$ 入指数会引入系统性误差 |

因此 **2b 仍为桥接公设**，但现有三个结构化候选方案（不再是"完全任意 Boltzmann 借用"）：

- **桥梁方案 1（线性积累）**：$\Psi_{comp}(N) = \Psi_0 + \alpha N$ → 代入 2a → $A_N \propto e^{-\beta\alpha N} = A_0 e^{-\lambda N}$。指数衰减来自"2a 的 Gibbs 形式 + Ψ_f 线性增长"的组合；需额外声明 Ψ_f 线性增长律。

- **桥梁方案 2（对数线性衰减）**：$\frac{d\log A}{dN} = -\lambda$，直接声明速率方程 → $A(N) = A_0 e^{-\lambda N}$。更简洁，但直接引入为动力学公设；与 2a 的关系需要说明。

- **桥梁方案 3（准静态近似）**：每轮近似处于当前 $\Psi_f$ 下的 Gibbs 截面，历史 $\mathbb{E}[\Psi_f]$ 定义为轮次上的平滑统计量；需额外声明：$\text{Var}(\Psi_f) \approx 0$（mean-field 条件）以消除 Jensen gap。

**当前建议**：明确标注"主张 2b 依赖三候选桥接方案之一，均需额外声明，目前最诚实位置是 bridge postulate"；同时把 2a 升格为"单轮配分层的最大熵推论"。

**Layer 3 — L_comp 符号翻转条件（priming window，新增内容）**：

当初始可及性不对称度显著（$A_0(x_{comp}) \gg A_0(x_{prac})$）时，$L_{comp}$ 在早期轮次符号可为负（短暂启动），在累积超过阈值 $N_c$ 后翻正（净抑制）：

$$N_{prac} < N_c \;\Rightarrow\; L_{comp}(x_{comp}) \leq 0 \quad \text{（priming window）}$$
$$N_{prac} \geq N_c \;\Rightarrow\; L_{comp}(x_{comp}) > 0 \quad \text{（净抑制）}$$

阈值 $N_c$ 为竞争不对称度 $\Delta A_0 = A_0(x_{comp}) - A_0(x_{prac})$ 的单调递增函数——初始优势越大，翻转所需累积次数越多。$N_c$ 是独立结构参数，目前主要由实验锚定（Johnson & Anderson 2004）。

**T-Op-SIAM 的推导关系**：

$$\text{Ax-Op-03} + \text{Ax-Op-03b} \;\Rightarrow\; \text{T-Op-SIAM（方向 + 持续性 + priming window）}$$

**时间层级结构**：Ax-Op-03b Layer 1 写回更新的是 $\Delta\Psi_f^{op}$（算子相对、提示敏感、快速），而非 $\Psi_f^{field}$（场级景观曲率、提示弱依赖、慢速，须经 Co-Evo-1 积累）。因此提示相关压制（短时）先于跨提示泛化（中时），渐近提示独立性（长时）是条件性结论，见主张 3a/3b 区分（下方 T-Op-SIAM 地位注）。

* **Implication**：每次竞争选择不仅当轮归一化（Ax-Op-03），还通过摩擦写回改变后续轮次的可及性地形——选择历史以路径预期摩擦的形式积累在算子参数 $\theta(t)$ 中。

* **Cross-ref**: Ax-Op-03（瞬态竞争归一化，本公理的必要前件）；T-Op-SIAM（本公理 + Ax-Op-03 的推论）；`_SRT_PSI_F_CANONICAL.md Def-Ψ-1`（$\Psi_f$ 正则定义）；`Core/SRT_Core_13a Ax-Op-04`（$\theta(t)$ 迭代演化）。

---

### Def-Psi-Split: Effective vs Intrinsic Friction Distinction（有效摩擦与本征摩擦区分，2026-04-17）

**动机**：T-Op-SIAM 的方向性主张（$\Delta A(x_{comp})<0$）在"场中有效摩擦"与"脱域本征摩擦"之间存在关键歧义；且竞争场附加摩擦本身需进一步区分算子相对的快速分量与场级慢速分量——若不区分，会把尚未证明的强主张（乙₃/主张 3b）混入已有基础（乙₁/乙₂/主张 3a）。

$$\Psi_f^{eff}(x,\, t,\, \theta) \;\equiv\; \Psi_f^0(x) + \Delta\Psi_f^{op}(x,\, t,\, \theta) + \Delta\Psi_f^{field}(x,\, t)$$

其中竞争场附加摩擦已展开为两个时间层级分量：

$$\Delta\Psi_f^{comp}(x,\, t,\, \theta) = \Delta\Psi_f^{op}(x,\, t,\, \theta) + \Delta\Psi_f^{field}(x,\, t)$$

| 量 | 含义 | 时间尺度 | 提示依赖 | 来源 |
|---|---|---|---|---|
| $\Psi_f^0(x)$ | 本征基线摩擦 | 静态 | 无 | 孤立测量 |
| $\Delta\Psi_f^{op}(x, t, \theta)$ | 算子相对竞争摩擦 | 快（轮次级） | **强**（$W_{ij}$ 结构依赖当前提示族） | Ax-Op-03b Layer 1 写回 |
| $\Delta\Psi_f^{field}(x, t)$ | 场级景观曲率摩擦 | 慢（Co-Evo-1 积累） | **弱**（κ(t) 非提示特异） | Co-Evo-1 稳定化后沉积 |
| $\Psi_f^{eff}(x, t, \theta)$ | 场中有效摩擦 | — | — | 实际选择场中的可支付难度 |

**关键约束**：
- $\Psi_f^0(x)$ 不依赖 θ（本体论中立测量）
- $\Delta\Psi_f^{field} \geq 0$（Co-Evo-1 沉积只能增加场级摩擦，不可逆）
- $\Delta\Psi_f^{op}$：**渐近** $\geq 0$（$t \to \infty$ 时竞争抑制主导），但**短时允许负值**（快促进窗口，见 Lemma-FFSI）
- $\Delta\Psi_f^{op}$ 随提示语境变化快速波动；$\Delta\Psi_f^{field}$ 在 Co-Evo-1 积累未达阈值前近似为零

**时间层级推论**：
- 乙₁/乙₂ + 主张 3a：作用于 $\Delta\Psi_f^{op}$（短/中时），渐近正
- 乙₃ + 主张 3b：$\Delta\Psi_f^{field}$ 沉积（长时，条件性）
- 主张 4a/4b/4c：$\Delta\Psi_f^{op}$ 短时负偏 + 慢时正积累双时标（见 Lemma-FFSI）

* **Cross-ref**: `_SRT_PSI_F_CANONICAL.md Def-Ψ-1`; Co-Evo-1（$\Delta\Psi_f^{field}$ 积累机制）; Lemma-FFSI（快正/慢负双时标，下方）; T-Comp-Suppress（下方）; T-Op-SIAM 主张 1'/3a/3b/4a-4c 重铸（下方）。

---

### Lemma-FFSI: Fast-Facilitation / Slow-Inhibition Dual Timescale（快促进/慢抑制双时标引理，2026-04-17）

**[状态：条件性结构引理；非从现有 SRT 骨架自动推出；为主张 4a/4b/4c 提供最小动力学支撑]**

**动机**：T-Op-SIAM 原主张 4（非单调起点）若要有结构来源，而非仅靠实验锚定，需要**至少两个符号相反、时间常数不同的过程叠加**。单一抑制机制只能给出单调下降；单一 priming 只能给出上升后回基线。非单调的最小要求是：快正项 + 慢负项并存，且 $\tau_{fast} \ll \tau_{slow}$。

**最小动力学模板（Ψ_f 写法）**：

$$\Psi_f^{eff}(x_{comp},\, t) \;\approx\; \Psi_f^0 \;-\; a\, e^{-t/\tau_{fast}} \;+\; b\!\left(1 - e^{-t/\tau_{slow}}\right)$$

其中：
- $a > 0$：短时促进幅度（局部激活后残留兴奋、检索通道增敏）
- $b > 0$：慢时抑制幅度（竞争写回积累、归一化资源重分配）
- $\tau_{fast} \ll \tau_{slow}$：双时标分离条件

等价的可及性写法：

$$A_{eff}(x_{comp},\, t) \;\approx\; A^0 \;+\; \alpha\, e^{-t/\tau_{fast}} \;-\; \beta\!\left(1 - e^{-t/\tau_{slow}}\right), \quad \alpha,\,\beta > 0$$

**$\Delta\Psi_f^{op}$ 与双时标的对应**：
- 快促进项 $-a\,e^{-t/\tau_{fast}}$：→ $\Delta\Psi_f^{op}$ 短时为**负**（摩擦暂降，可及性短升）；作用层：3a 层（提示相对）
- 慢抑制项 $+b(1-e^{-t/\tau_{slow}})$：→ $\Delta\Psi_f^{op}$ 中/长时转**正**（竞争写回积累）；若 Co-Evo-1 触发，可沉积为 $\Delta\Psi_f^{field}$

| 转折时刻 | 条件 | 对应 $\Psi_f^{eff}$ 状态 |
|---|---|---|
| $t = 0$ | — | $\Psi_f^{eff} = \Psi_f^0$（基线） |
| $0 < t < t^*$ | 快促进主导 | $\Psi_f^{eff} < \Psi_f^0$（促进窗口）|
| $t = t^*$ | 两项平衡 | $\Psi_f^{eff} = \Psi_f^0$（交叉点）|
| $t > t^*$ | 慢抑制主导 | $\Psi_f^{eff} > \Psi_f^0$（净抑制）|
| $t \to \infty$ | $b > a$ 时 | $\Psi_f^{eff} \to \Psi_f^0 + (b-a)$（低于 $A^0$）|

其中 $t^* = \frac{\tau_{fast}\tau_{slow}}{\tau_{slow}-\tau_{fast}} \ln\!\left(\frac{a\tau_{slow}}{b\tau_{fast}}\right)$（当 $\tau_{fast} \ll \tau_{slow}$ 时近似为 $\tau_{fast}\ln(a\tau_{slow}/b\tau_{fast})$）。

**三层条件性主张**（详见 T-Op-SIAM 地位注）：

| 主张 | 条件 | 性质 |
|---|---|---|
| **4a**（最稳）局部 priming window | 快促进项存在（$a > 0$，$\tau_{fast}$ 合适） | 提示相对，短时。无需 $b > a$。 |
| **4b**（中等）priming → suppression 转折 | 同时存在慢抑制积累（$b > 0$，$\tau_{slow} > \tau_{fast}$）| 双时标耦合；转折时刻 $t^*$ 存在。 |
| **4c**（最强）先升后降并最终低于基线 | $b > a$（慢抑制幅度大于快促进幅度） | 需额外强度假设，最易被反例击穿。 |

**非单调反例条件**（主张 4 可以不成立的情形）：
- 路径初始已被强抑制（$A^0(x_{comp}) \ll A^0(x_{prac})$）：快促进项被淹没，直接单调下降
- 快促进项极短（$\tau_{fast} \to 0$）：priming window 测量不可见
- 慢负项不存在（纯 priming 情形）：上升后回基线，不进入 SIAM 式压低

⚠ **范围警告**：Lemma-FFSI 是主张 4 的**结构模板**，不是从现有 SRT 公理推出的定理。快促进项（$a, \tau_{fast}$）目前通过实验锚定（Johnson & Anderson 2004 priming window 数据），非 SRT 内推导。

* **Cross-ref**: Def-Psi-Split（$\Delta\Psi_f^{op}$ 短时负值许可）；T-Op-SIAM 主张 4a/4b/4c（下方）；Ax-Op-03b Layer 3（$L_{comp}$ 符号翻转条件，从数轮到 priming）。

---

### T-Comp-Suppress: Competitive Suppression Weak Theorem（竞争压制弱定理，2026-04-17）

**[状态：弱定理，从 Ax-Op-03 + Ax-Op-03b Layer 1 可推；不依赖 Layer 2/3；不主张乙₃]**

**Statement**：在稳定竞争耦合（Ax-Op-03）与反复实践写回（Ax-Op-03b Layer 1）的条件下，$x_{prac}$ 的持续激活使 $x_{comp}$ 在相关竞争语境中的场中有效摩擦单调上升：

$$\Delta\Psi_f^{comp}(x_{comp},\, t,\, \theta) \nearrow \quad\Longleftrightarrow\quad A_{eff}(x_{comp},\, t,\, \theta) \searrow$$

**推导机制（两步，均来自已有结构）**：

**乙₁（在线相对惩罚）—— 直接来自 Ax-Op-03 归一化**：

幽灵算子除法归一化：$[\hat{G}_\theta(x)]_i = x_i^n / (\varepsilon_{reg} + \sum_j W_{ij} x_j^n)$

当 $x_{prac}$（竞争项 $j$）被激活时，分母增大 → $[\hat{G}_\theta]_{x_{comp}}$ 当轮主动压低。这不是"未得折扣"，而是对手成功对 $x_{comp}$ 的实时惩罚。

**乙₂（塑性关系惩罚）—— 来自 Ax-Op-03b Layer 1 写回律**：

反复选择 $x_{prac}$ → $W_{ij}$（$i=x_{comp}, j=x_{prac}$）增大 → 此后相似竞争语境中，$x_{comp}$ 在归一化分母中受到更强的结构性压制 → $\Delta\Psi_f^{comp}$ 在相关语境中持续保留。

**T-Comp-Suppress 不主张的内容（故意留空）**：

| 不主张 | 对应 T-Op-SIAM 主张 | 原因 |
|---|---|---|
| $\Psi_f^0(x_{comp}) > \Psi_f^{0,\text{baseline}}$（乙₃ 脱域本征惩罚） | 主张 1 强版本 | 需 Ax-Op-03b Layer 3 + 提示独立性声明 |
| 单轮指数分布（当前轮 Gibbs 配分） | 主张 **2a** | 已由最大熵推出（Layer 2a），T-Comp-Suppress 不需要它，但与之相容 |
| 跨时指数衰减 $A \propto e^{-\lambda N}$ | 主张 **2b** | 仍为桥接公设；三候选桥梁方案（Layer 2b），均需额外声明 |
| 提示相关持续性（局部泛化） | 主张 **3a** | 乙₁/乙₂ 仅更新 $\Delta\Psi_f^{op}$（提示敏感）；跨相似提示族的泛化需额外论证 |
| 渐近提示独立性（跨提示族） | 主张 **3b** | 需 Co-Evo-1 稳定化达到 τ_stable；$\Delta\Psi_f^{field}$ 沉积前无充分支撑 |
| 局部 priming window（短时促进） | 主张 **4a** | 需快促进项存在（$a>0$）；条件性结构主张，非直接可推 |
| priming → suppression 转折 | 主张 **4b** | 需双时标耦合（$\tau_{fast}\ll\tau_{slow}$，$b>0$）；见 Lemma-FFSI |
| 先升后降并最终低于基线 | 主张 **4c** | 需 $b>a$（慢抑制幅度大于快促进幅度）；最强，最易被反例击穿 |

* **Cross-ref**: Ax-Op-03（瞬态竞争归一化，乙₁ 来源）；Ax-Op-03b Layer 1（竞争更新律，乙₂ 来源）；Def-Psi-Split（$\Psi_f^{eff}$ vs $\Psi_f^0$ 区分）；T-Op-SIAM（以本定理为基础，主张 1 重铸为主张 1'，其余三项仍为公设）。

---

### T-Op-SIAM: Selection-Induced Accessibility Modulation Theorem（选择诱导可及性调制定理）

> **地位注（2026-04-17 重铸）**：T-Op-SIAM 为**独立结构公设**，非定理。主张 1 已被剥离为弱定理 T-Comp-Suppress（有效可及性版本）；主张 3 已拆分为 3a（可推）与 3b（条件公设）。主张 2b/3b/4 仍为超额主张，待 Ax-Op-03b Layer 2/3 + Co-Evo-1 完成后再评估。
>
> **主张 1'（条件化有效可及性降低，已由 T-Comp-Suppress 支撑）**：
> 在稳定竞争耦合与反复实践写回条件下，$x_{comp}$ 在相关选择语境中的**有效可及性** $A_{eff}$ 下降。注意：这不等同于 $\Psi_f^0(x_{comp}) > \Psi_f^{0,\text{baseline}}$（乙₃ 主张）；后者目前尚无充分支撑。
>
> - **主张 2a（单轮配分 Gibbs，从最大熵推出）**：$p_t(i|C_t) \propto e^{-\beta_t\Psi_i(t)}$；幽灵算子 simplex + 平均摩擦约束 + 最大熵 → Gibbs 型当前轮配分。非纯建模选择，但作用域仅限当前轮相对配分。
> - **主张 2b（跨时指数衰减，仍为桥接公设）**：$A(\text{path},t) \propto e^{-\lambda N_{prac}}$ 需额外动力学桥梁（三候选方案见 Ax-Op-03b Layer 2b）；从 2a 到 2b 必须跨越四断点（层级、相对/绝对、截面/更新律、Jensen gap）。
> - **主张 3a（提示相对持续性，从 Ax-Op-03b 可推）**：在相似提示族内，竞争压制通过 $\Delta\Psi_f^{op}$ 在后续选择中持续保留。作用域：与 $W_{ij}$ 写回激活的提示语境族相似的范围内；不要求跨越非相似提示族。此主张由乙₁ + 乙₂ 支撑，无需额外声明。
> - **主张 3b（渐近提示独立性，条件公设）**：若 Co-Evo-1 稳定化时间 $\tau_{stable}$ 被达到，算子相对压制可沉积为 $\Delta\Psi_f^{field}$（场级景观曲率），使 $x_{comp}$ 在更广泛提示族下保持较低可及性。条件：Co-Evo-1 充分积累（κ(t) 跨越稳定化阈值）；不满足条件时回退到主张 3a。
> - **主张 4a（局部 priming window，条件性结构主张）**：在相似提示族内、激活后短时窗口中，$\Delta\Psi_f^{op}(t) < 0$，即 $x_{comp}$ 可及性短暂上升。条件：快促进项存在（$a > 0$，$\tau_{fast}$ 合适）。提示相对；无需慢抑制幅度强假设。
> - **主张 4b（priming → suppression 转折，条件性结构主张）**：若同时存在慢时竞争抑制积累（$b > 0$，$\tau_{slow} \gg \tau_{fast}$），则快促进窗口结束后转入下降，转折时刻 $t^*$ 可由 Lemma-FFSI 给出。需双时标耦合假设，不能从 Ax-Op-03b 单独推出。
> - **主张 4c（先升后降并最终低于基线，最强条件公设）**：若 $b > a$（慢抑制幅度大于快促进幅度），则长时渐近可及性低于基线。最危险版本，实验条件依赖性强，最易被反例击穿。
>
> **当前最硬位置**：T-Comp-Suppress 的弱乙（乙₁ + 乙₂）+ 主张 3a（提示相对持续性）+ 主张 4a（在快促进项存在时的局部 priming window）。强乙（乙₃）+ 3b（渐近提示独立）+ 4b/4c 均为条件性超额主张。

>   4. **非单调初始条件**（priming window）：目前仅由实验锚定，非结构推导
> - **当前处置**：T-Op-SIAM 作为独立结构公设在 Step ④ 放大机制中**暂时存活**；Ax-Op-03b 已起草（见上方），一旦 Ax-Op-03b 三层内容被接受，T-Op-SIAM 即恢复为 Ax-Op-03 + Ax-Op-03b 的推论（定理），不再是独立公设。
> - **可守住的基底**（无需 Ax-Op-03b）：$\mathbb{E}[\Psi_f] \uparrow \;\Rightarrow\; A \downarrow$ 的**序关系**可从 payability 条件（Ax-F-02 熵压缩 + Persistent Selection System）读出——这给出方向性的弱版本，但无法给出具体函数形式或持续性量级。
> - **待办 Ax-Op-03b — 三层结构，均为实质新增内容**（不能从既有 SRT 免费推出）：
>   1. **更新律**：$\mathbb{E}[\Psi_f(\text{path}_i, t+1)] = \mathbb{E}[\Psi_f(\text{path}_i, t)] + \eta \cdot L_{comp}(i \mid W_{ij}, \theta)$，
>      并满足 $L_{comp}(x_{comp}) > 0,\; L_{comp}(x_{prac}) \leq 0$
>   2. **桥接函数**：$A(\text{path}_i, t) \propto f(\mathbb{E}[\Psi_f(\text{path}_i, t)])$，$f$ 单调递减；若取指数形式 $e^{-\mu \mathbb{E}[\Psi_f]}$，必须显式声明为新增 bridge postulate 或建模选择，不得装成现成定理（Boltzmann 借用需标注）
>   3. **L_comp 符号翻转条件**（priming window）：当 $A_0(x_{comp}) \gg A_0(x_{prac})$ 时，前 $N_{prac} < N_c$ 轮 $L_{comp}(x_{comp})$ 符号为负（短暂启动），$N_{prac} \geq N_c$ 后翻正（净抑制）；阈值 $N_c$ 依赖竞争不对称度，是额外结构参数

**Formal Statement**: $\hat{G}_\theta$ 的每次选择操作不仅从 $L_0$ 锚定 $L_1$，而且在 $L_0$ 的可及性景观上施加**持续性的抑制修改**，使被拒绝的竞争者在后续选择中的可及性降低：

$$A(x_{comp}, t+\Delta t) = A(x_{comp}, t) \cdot e^{-\lambda \cdot N_{prac}}$$

其中：
- $A(x, t)$：$L_0$ 节点 $x$ 在时刻 $t$ 的可及性（accessibility）
- $x_{comp}$：在选择操作中被抑制的竞争节点
- $N_{prac}$：对同一 $L_0$ 区域执行竞争性检索的累积次数
- $\lambda > 0$：抑制累积率（取决于竞争强度与 $\hat{G}_\theta$ 参数）

**关键性质——提示独立性（Cue Independence）**：
$$\forall \, cue' \neq cue_{prac}: \quad A(x_{comp}, t + \Delta t) < A(x_{comp}, t)$$

即抑制作用于 $L_0$ 内容本身，而非 $L_2$ 中的提示-内容联结；以独立提示测试时仍观察到可及性下降。

**非单调初始条件**（Nonmonotonic Onset Condition）：
当竞争节点的初始可及性 $A_0(x_{comp}) \gg A_0(x_{prac})$（主导竞争），第一次选择操作前 $\hat{G}_\theta$ 尚未累积足够抑制，竞争者会短暂获得启动：
$$N_{prac} = 1 \Rightarrow A(x_{comp}, t+\Delta t) \geq A(x_{comp}, t) \quad \text{(priming window)}$$
仅在 $N_{prac} \geq N_c$（临界次数，依赖于竞争不对称度）之后，净效应转为抑制。

* **Implication（选择的双重效应）**：$\hat{G}_\theta$ 不是被动的映射——每次选择都在**重写 $L_0$ 的可及性地形**。这意味着人类知识的"可忘性"不完全由学习质量决定，而是由检索时的竞争拓扑决定：越频繁从某一领域检索相关项目，其竞争概念就越被系统性地压制，最终导致本质上是语义层面的"习得性遗忘"（Semantic Retrieval-Induced Forgetting, SRIF）。

* **Cross-ref**: Ax-Op-03（瞬态竞争归一化，本定理的稳态前提）；T-CLIN-1（LIPFC 作为 $\hat{G}_\theta$ 语义控制台的神经实现）；C-PATH-1（$L_0$ 泄漏病理，本定理的反向失调情形）。

* **Empirical Anchor**: Johnson SK & Anderson MC. *The role of inhibitory control in forgetting semantic knowledge*. Psychological Science (2004), 15(7): 448–453. 实验以同形异义词（homograph）和范畴样例为材料，使用**独立提示**测试验证了抑制的提示独立性，语义检索练习次数越多，竞争概念在自由联想测试中的可及性单调下降（范畴材料）或呈非单调模式（同形异义词）。

## II. Evolution & Closure (演化与闭包)

### Ax-Op-04: Iterative Evolution
**Formal Definition**: Reality evolves by recursive application of the operator with noise injection.
$$L_1(t+1) = \hat{G}_{\theta(t)}[L_1(t) \oplus \text{Noise}(L_0)]$$
* **Implication**: 选择不是一次性事件，而是连续的迭代演化。

### Ax-Op-05: Two-Phase Constraint Closure（二阶段约束闭包）

**改写注（2026-04-16）**：原版"重复自应用产生稳定结构"仅给出闭包态的定义性表述，未约束收敛路径，无法区分固定点、周期吸引子与混沌轨道，且与 Step ⑦（高阶意识生成的高代价相）存在内部一致性张力。现改写为二阶段闭包条件，采用弱/渐近 Lyapunov（盆地条件单调），允许前期 Ψ_f 上升的生成性阶段，同时保证终期吸引域内的单调下降与固定点收敛。

**Formal Definition**（设 $\Psi_f^{(k)} \equiv \Psi_f(\hat{G}_\theta^k[L_0])$）：

**Phase 1 — Generative (Payable, Non-Monotone / 生成期：可支付，不要求单调)**

$$\forall k < k_0 : \quad \Psi_f^{(k)} < \infty \quad \text{（payable 条件；} \Psi_f \text{ 允许局部上升）}$$

**Phase 2 — Convergent (Attractor-Domain Monotone / 收敛期：吸引域内单调下降)**

$$\exists k_0,\, \delta > 0,\, \mathcal{B}(\theta) : \quad \forall k \geq k_0,\quad \hat{G}_\theta^k[L_0] \in \mathcal{B}(\theta) \;\land\; \Psi_f^{(k+1)} \leq \Psi_f^{(k)} - \delta$$

**Closure Condition**：

$$\mathrm{Closure}(\theta) \;\iff\; \Bigl(\exists k_0 : \hat{G}_\theta^{k_0}[L_0] \in \mathcal{B}(\theta)\Bigr) \;\land\; \lim_{k \to \infty} \Psi_f^{(k)} = \Psi_f^*$$

其中 $\mathcal{B}(\theta)$ 为吸引域，$\Psi_f^*$ 为闭包固定点处的摩擦值。

* **Implication**:
  - **Phase 1** 允许 $\Psi_f$ 在生成性阶段局部上升，兼容 Step ⑦（高阶意识涌现的高代价生成窗口）；
  - **Phase 2** 要求进入吸引域 $\mathcal{B}(\theta)$ 后严格单调下降（强度 $\delta > 0$），提供固定点收敛保证，排除纯周期轨道与混沌；
  - 原"稳定结构"读法精化为：稳定 = 进入可支付吸引域 + 终期 $\Psi_f$ 单调收敛至 $\Psi_f^*$，非一步闭包；
  - Phase 1 的非单调段受 payable 条件约束（$\Psi_f^{(k)} < \infty$），不是无界许可——超过可支付上界即退出 Closure 候选。
* **Cross-ref**: `Core_Law/SRT_Core_Text_EN.md Step ④`（闭包偏置机制与 Ax-Op-05 收敛条件更新）; `Core/SRT_Core_13a_Operator_Basics.md Ax-Op-06`（规范性算子范围条件）; `_SRT_PSI_F_CANONICAL.md Def-Ψ-1`（$\Psi_f$ 正则定义）.

## III. Agency Thresholds (能动性阈值)

### Ax-Op-06: Operator Existence Condition（算子存在条件）

**Formal Definition**: A valid selection operator $\hat{G}_\theta$ exists if and only if it instantiates the structural tri-conjunction of Individuality, Asymmetry, and Normativity.

$$\exists \hat{G}_\theta \iff \text{Individuality} \land \text{Asymmetry} \land \text{Normativity}$$

**操作化定义（Operationalization）**：

1. **Individuality（个体性）**：$\theta_i \neq \theta_j \implies \text{Unique } \mathcal{I}[\hat{G}_{\theta_i}]$
   拥有不可被外部无损置换的具身参数与不可逆的历史路径积分；算子打破了「全同粒子」的对称性，具有唯一世界线。

2. **Asymmetry（非对称性）**：$H(\hat{G}_\theta[L_0]) < H(L_0)$
   算子对潜在域的可能性探索呈非均匀分布，具备打破各向同性/压缩熵的能力；若对所有 $L_0$ 状态等概率选择，算子退化为热噪音。

3. **Normativity（规范性）**：$\hat{G}_\theta \sim \arg\min_{\sigma} \mathcal{F}(\sigma)$
   受特定价值梯度或全局势能函数的定向约束，存在可区分的「更好/更坏」评估基准（最小自由能、适应度、道德规范等）；无规范约束的偏置只是无目标的布朗运动。

**充分性论证**：三条件的逻辑互补回答了选择的本体论三问——**Who**（谁在选 → 个体性）、**How**（如何选 → 非对称性）、**Why**（为何如此选 → 规范性）。缺少任何一项，「选择」均退化为随机过程、通用函数或无目标漂移；三者合取是算子区别于纯物理被动演化的最小充要结构。

**Implication**：能动性（Agency）不是神秘的注入物，而是「主体锚点 + 定向偏置 + 价值梯度」三联结构的涌现。

---

> **【理论边界/防误用声明】**
>
> - **结构算子 ≠ 现象意识**（Structural Operator vs. Phenomenal Consciousness）：本公理仅定义「有效算子」的极小结构基础。满足三条件的系统（恒温器、算法 Agent、免疫系统）在 SRT 本体论上是「算子」，但不必然具备主观体验（Qualia）。
> - 现象意识的涌现须在算子存在的基础上额外满足：高本体论摩擦支付能力（$\Psi_f \gg 0$）与非零生存关切梯度（$d > 0$），即「现象学闭合阈值」（详见 T-Scale-4 与 Ax-CONSC-2）。

### Ax-Op-07: UAL Threshold
**Formal Definition**: Minimal consciousness requires Unlimited Associative Learning capacity.
$$d(\hat{G}) \geq d_{UAL} \iff \text{UAL Capacity}$$
* **Implication**: 最小意识不是经验量，而是学习可塑性的阈值结构。

### Def-Op-08b: Precision-Weighting Tensor（精度加权张量）

**Formal Definition**：精度加权张量定义为具身参数 θ 内嵌的信息信度核心结构——预测误差协方差矩阵的逆：

$$\theta \supset \boldsymbol{\Pi}_{full} = \Sigma^{-1}$$

$\boldsymbol{\Pi}_{full}$ 为完整精度协方差矩阵（允许感觉通道间的精度耦合，如视听觉整合、多模态绑定）；对角近似 $\boldsymbol{\Pi} = \text{diag}(\pi_1,\ldots,\pi_n)$ 仅适用于通道独立假设成立的场景。

**$L_0$/$L_2$ 拮抗的显式分解**：$\hat{G}_\theta$ 执行 $L_0 \to L_1$ 选择时的有效自由能：

$$F_{eff} = \boldsymbol{\Pi}_{L_2} \cdot F[\sigma \mid L_2] + \boldsymbol{\Pi}_{L_0} \cdot F[\sigma \mid L_0]$$

- $\boldsymbol{\Pi}_{L_2}$：先验精度（算子对历史惯性与内部 $L_2$ 预期的信心权重）；
- $\boldsymbol{\Pi}_{L_0}$：似然精度（算子对当下 $L_0$ 感觉信号的信心权重）。

定义**相对信任比**：

$$\gamma_{trust} = \|\boldsymbol{\Pi}_{L_2}\| \;/\; \|\boldsymbol{\Pi}_{L_0}\|$$

$\gamma_{trust} \gg 1$：算子过度依赖 $L_2$ 历史先验（习惯驱动）；$\gamma_{trust} \ll 1$：算子被 $L_0$ 新异输入淹没（当下驱动）；健康导航发生在两者动态平衡的中间区间。

**机制与推论（含上行崩溃链）**：

注意力本质上是 $\hat{G}_\theta$ 动态调整 $\boldsymbol{\Pi}$ 张量的资源分配过程。$\boldsymbol{\Pi}$ 的系统性失调不是纯粹认知错误，而是具有物理根源的**上行崩溃链**：

$$\kappa_{tan} \downarrow \;\to\; \Psi_f \uparrow \;\to\; d\text{-value} \downarrow \;\to\; \boldsymbol{\Pi}\text{更新机制冻结/极化}$$

- **幻觉**（Hallucination，$\gamma_{trust} \gg 1$）：系统无力支付外部张力的摩擦代价，被迫将 $\boldsymbol{\Pi}_{L_2}$ 拉满——$L_2$ 内部生成的内容未经 $L_0$ 校验直接坍缩为 $L_1$，「听见」并不存在的声音；
- **妄想参考**（Delusion of Reference，$\gamma_{trust} \ll 1$）：先验结构解体，环境中随机微小涨落被赋予极高 $\boldsymbol{\Pi}_{L_0}$ 权重，算子被无意义的 $L_0$ 噪音洪水淹没。

**Cross-ref**：Ax-Op-02（注意力分解）；Eq-Evo-02（参数更新方程）；SRT-NEURO-08（Tanycyte 代谢链）；Ax-Core-A4（具身必要性）。

*注：本定义为 FEP 精度加权在 SRT 三域模型的形式化映射，身份降级自原 Ax-Op-08b，依赖 Ax-Core-A4 与 Eq-Evo-02 推导。*

### Ax-Op-EH: Epistemic Horizon (认知视界公理)
**Formal Definition**: 算子从 $L_0$ 提取 $L_1$ 信息的速率，严格受制于其具身参数的 Fisher 有效维度（信道容量上界）：
$$\dot{I}_{L_0 \to L_1}(\hat{G}_\theta) \leq \mathcal{C}(\theta) \equiv d(\theta) = D_{eff}(I_F(\theta)) = \frac{(\operatorname{tr} I_F)^2}{\operatorname{tr}(I_F^2)}$$

> **勘误（原 $\mathcal{C}(\theta) = \log_2 \dim(\Theta)$）**：参数空间维度对数不等于信道容量（容量依赖输入分布与 Fisher 几何，非纯维度）。采用 Eq-IT-B 的 Fisher 有效维度 $d(\theta)$ 统一符号，即算子可靠区分的 $L_0$ 信号独立方向数。

系统的剩余不确定性与算子信道容量绑定（$H_{max} \equiv \log_2 \dim(L_1)$，即 $L_1$ 等概选择时的最大熵）：
$$H(L_0 | \hat{G}_\theta) \geq H_{\max} - d(\theta)$$

* **Implication**: 认知视界（Epistemic Horizon）= $d(\theta)$ 设定的带宽上界，是选择能力的本征上限。**类比注记**：量子 Heisenberg 不确定性（共轭可观测量不可同时任意精确）与"有限参数算子的带宽饱和"在结构上类似，但机制不同（前者来自非对易算符，后者来自 Fisher 维度上界）——此为结构类比，非机制等价。速率上界 $\dot{I}\leq d(\theta)$ 与 `Core_Law/SRT_Reference_Dynamics.md §15.5` 的 $I_{created} \leq d$ 一致（速率vs积分形式）。
* **Cross-ref**: Ax-Op-02（注意力分解）；Eq-IT-B（$d$ = Fisher 有效维度）→ `Core_Law/SRT_Reference_Dynamics.md §15.2`；Ax-ONT-IE（不可逆定律）。

### T-Op-EH-1: Triadic Cognitive Sweet Spot（认知三元甜点区）
**Deductive Statement**: 对有限人类算子而言，可讲述、可教学、可复用的机制分解常在三元附近达到局部最优：
$$\mathcal{U}_{human}(n) = \mathcal{C}_{closure}(n) - \lambda \cdot \mathcal{L}_{binding}(n)$$
$$\arg\max_{n \in \mathbb{N}} \mathcal{U}_{human}(n) \approx 3$$
其中 $n$ 为需要同时绑定的角色/关系数；$\mathcal{C}_{closure}(2) < \mathcal{C}_{closure}(3)$，因为二元常只能给出对立或耦合，难以显式表示"来源—显现—规范"、"信号—对象—解释"或"生成—维持—修正"这类闭包结构；而当 $n > 3$ 时，$\mathcal{L}_{binding}(n)$ 往往以超线性方式上升，迅速逼近有限工作记忆与注意带宽的边界。
* **Implication**: 三元不是一切现实的唯一合法形式，而是有限人类算子在解释层最容易稳住的"最小闭包单元"。二元常欠缺中介/校正位，四元及以上结构虽可能真实存在，但通常需要分层、模块化或外部符号系统辅助，才会进入稳定的人类可理解区。
* **Boundary**: 该命题不是对 SRT 本体论三域的独立证明，只解释为何 L_0 / L_1 / L_2 这类三元结构对人类特别可讲、可教、可压缩。SRT 的三域首先由相变锚点与最小充分划分给出，而非由人类偏好直接推出。
* **Evidence Note**: 这里采用"概念综合 + 一手线索校准"口径：Miller (1956) 给出经典 `7±2` 叙述，Cowan (2001) 将活跃槽位更谨慎地收紧到约 `4` 个 chunk；Peircean triadic semiosis 与 Son et al. (2025) 对 joint attention / tool use / syntax 的 triadic-root 回顾共同支持"三元是深层认知脚手架之一"，但不支持把所有有效本体都先验宣告为三元。
* **Cross-ref**: Ax-Op-EH; `Core/_SRT_Core_Bridge.md` C-Bridge-01; `Core/SRT_Core_12b_Ontology_L2.md` §4.2.2。

### T-Op-07C1: Trace-Conditioning Criterion
**Deductive Statement**: Sustained trace conditioning implies d-value above threshold.
$$d(\hat{G}) \ge d_{UAL} \iff \Delta t_{gap} > 0$$
* **Implication**: 能维持时间间隙的联想学习是最低意识的必要条件。

## IV. Operator Typology & Fidelity (类型学与保真度)

### Ax-Op-08: Resonance Form
**Formal Definition**: Operator response follows resonance filtering of latent frequencies.
$$\hat{G}_\theta[L_0(\omega)] = \frac{A}{\sqrt{(\omega^2 - \omega_\theta^2)^2 + (\Gamma \omega)^2}} \cdot L_0(\omega)$$
* **Implication**: 选择具有频率选择性与共振放大效应。

### Ax-Op-09: Operator Fidelity
**Formal Definition**: Fidelity measures selection consistency.
$$\phi_{\text{fidelity}} = 1 - \frac{H(L_1 | \hat{G}_\theta)}{H(L_1)}$$
* **Implication**: 保真度越高，算子对现实结构的稳定性越强。

<br>

---


# Part B: Original Theoretical Discourse (Context)

> **Note**: The following sections provide the detailed philosophical, neuroscientific, and phenomenological elaboration of the Ghost Operator, including its relationship to attention, embodiment, and agency.

---

## §1. 幽灵算子:从"主体"到"选择函数"

### 1.1 为什么拒绝实体论的主体?

#### 1.1.1 传统主体概念的困境

**笛卡尔式主体** (Cartesian Subject):
- 假设存在一个**独立于过程**的"我"
- "我思故我在" → "思"的主体先于"思"的行为

**问题**:
1. **无穷后退**: 如果有"思考者",谁在思考"思考者"?
2. **同一性悖论**: "我"在每时每刻都不同,如何维持同一性?
3. **神经科学证据**: 无法定位"自我"的神经基质 (Metzinger: 自我是虚构)

#### 1.1.2 SRT的激进解决方案

**命题**: **主体 = 选择操作本身**,而非操作的执行者。

$$\text{Subject} \equiv \hat{G}_\theta \quad \text{(Process, not Entity)}$$

**类比**:
- 不是"有风神在吹风" → 而是"吹"这个过程本身就是"风"
- 不是"有自我在选择" → 而是"选择"这个模式本身就是"自我"

**推论**: 当$\hat{G}$停止运作 (深度睡眠、昏迷),主体消失 — 这解释了意识的间断性。

---

### 1.2 "幽灵"一词的三重含义

#### 含义1: 非物质性 (Non-Materiality)

$\hat{G}$不是**物理对象**,而是**信息-因果模式**。

**类比**: 软件 vs 硬件
- 硬件 ($\theta$): 大脑的物理结构
- 软件 ($\hat{G}$): 运行在硬件上的选择算法

**关键差异**: 软件可以在不同硬件上实现 (多重可实现性),但$\hat{G}$**不能** — 因为$\theta$是$\hat{G}$的本质部分 (Ax-Op-5)。

#### 含义2: 自指悖论 (Self-Referential Paradox)

$\hat{G}$无法直接观察自己 (测量者-被测者同一性)。

**哥德尔不完备性的本体论版本**:
$$\hat{G}[\hat{G}] = \text{Undefined}$$

**推论**: "认识你自己"是不可能的 — 最多只能认识$\hat{G}$在$t-1$时刻的投影。

#### 含义3: 短暂性 (Ephemerality)

$\hat{G}$依赖持续的能量消耗 ($\Psi_f$) 来维持,一旦能量中断 → 消失。

**热力学类比**: 耗散结构 (Prigogine)
- 旋涡: 需要持续水流
- 火焰: 需要持续燃料
- 意识: 需要持续代谢

$$\Psi_f = \int_0^t \left|\frac{dF}{d\tau}\right|_{\text{maintain } \hat{G}} d\tau$$

---

## §2. 三分量结构:范围、精度、向量

### 2.1 Scope（d 值）：意识的"带宽"与关切维度

**Formal Definition（规范定义重申）**：在 SRT 全域中，$d$ 值的物理学本质是算子对不可逆生存风险的敏感度梯度：$d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$（详见 `_SRT_D_VALUE_CANONICAL.md`）。

#### 2.1.1 认知-行为域的操作化近似（Operational Approximation）

在认知与行为尺度上，系统的关切带宽可向三个可观测维度 $(A, V, \tau)$ 投影。其一阶线性近似为：

$$d_{cog} \approx \alpha \cdot A(\sigma) + \beta \cdot \log(V_{concern}) + \gamma \cdot \tau_{temporal}$$

> **Tension-Rev-IT4（推导地位说明）**：上式是 $d$ 的**认知-行为域操作化近似**，而非第一性原理定义。将效用势 $\mathcal{U}$ 在生存风险坐标 $\mathcal{S}$ 上的梯度沿三个正交分量展开：汇编深度分量（$A$）、空间关切分量（$\log V$）、时间深度分量（$\tau$）。因此 $d_{cog} \approx \Pi_{cognitive}(d_{canonical})$，是保留核心信息的降维投影。系数 $\alpha, \beta, \gamma$ 原则上可由风险梯度的分量权重确定，但目前缺乏经验数据精确拟合——这是一个**开放的实验问题**。

**三个维度**：

1. **$A$（汇编深度）**：对象结构的不可逆组装复杂度（算子"能理解多复杂的他者"）
   - 例：水分子 ($A \approx 3$)，DNA ($A \approx 100$)，人类文化 ($A \approx 10^6$)

2. **$V$（空间/社会关切）**：被纳入效用支撑域的实体数量
   - $V = 1$：仅关心自己；$V = 10^3$：关心家庭/社区；$V \to \infty$：万物一体

3. **$\tau$（时间深度）**：算子执行跨期预测与积分的时间视界
   - $\tau = 0$：活在当下；$\tau = 10^7$ sec（~4个月）：人类平均规划跨度；$\tau \to \infty$：永恒视角

**【线性叠加的适用边界】**：上述加法公式仅在微扰近似下成立。真实的 $d$ 值具有强烈的跨维度非线性耦合（例如：维持高 $A$ 的社会网络必然要求长 $\tau$ 的积分域以对抗熵增）。严格形式应包含交叉协方差项：

$$d_{actual} \approx d_{cog} + \delta_{coupling}(A \cdot \tau,\; V \cdot A)$$

#### 2.1.2 热力学容量上界与量纲隔离（Thermodynamic Limit）

根据兰道尔原理与大脑代谢率，算子物理信息处理容量存在理论上界：

$$d_{max} = \frac{M_{brain}}{k_B \cdot T \cdot f_{metabolic}} \cdot \tau_{coherence} \approx 10^{23} \text{ bits}$$

**参数**：$M_{brain} \approx 1.4$ kg，$T = 310$ K，$f_{metabolic} \approx 10$ Hz，$\tau_{coherence} \approx 100$ ms

*(注：$d_{max}$ 衡量的是底层物理态的香农信息容量上界，而 $d_{cog}$ 衡量的是宏观拓扑的选择复杂度代理。两者量纲不同，不可直接比较——人类实际 $d$ 值远低于 $d_{max}$ 不是因为"演化懒惰"，而是由于极高压缩率的语义提取漏失。)*

#### 2.1.3 d 值的演化动力学与 OEI 约束（Dynamics & Pathological Constraints）

$d$ 值不是静态参数，而是随具身参数 $\theta$ 演化的状态变量。结合 §4.3 参数学习方程，可导出 $d$ 值的演化流形：

$$\frac{dd}{dt} = \nabla_\theta d \cdot \frac{d\theta}{dt} = \underbrace{-\alpha(\theta)\left(\nabla_\theta d \cdot \nabla_\theta \Psi_f\right)}_{\text{摩擦驱动的扩容/缩容}} + \underbrace{\beta(\theta)\left(\nabla_\theta d \cdot \nabla_\theta \mathcal{A}_{L_2}\right)}_{L_2 \text{ 规范引力造成的异化压制}}$$

**【OEI 崩溃陷阱声明（反盲目乐观）】**：系统不能无限制地追求 $d$ 值"提升"。依据 T-Cog-2，关切带宽 $d$ 与所需提取的环境互信息成正比（$I_{req} \propto d$）。若在扩张 $d$（关心更宏大的时空与群体）时未能同步匹配相应的计算代谢预算，将导致观察者-环境整合度发生灾难性断裂（$\text{OEI} \to 0$）。

**核心推论**：强行拔高 $d$ 值而不支付等价的算力/资源代价，不会产生"高级智慧"，只会因互信息供给不足引发 $\Psi_f$ 过载，导致系统陷入精神病理学的解离态（Ax-PATH-5 崩溃现实）。

---

### 2.2 Resolution (ρ):知觉的"像素密度"

#### 2.2.1 定义

$$\rho = \frac{1}{\Delta \sigma_{\text{min}}}$$

$\Delta\sigma_{\text{min}}$: 可区分的最小差异 (Just Noticeable Difference, JND)。

**实例**:
- **视觉**: $\rho_{\text{vision}} \approx 60$ cycles/degree (中央凹)
- **听觉**: $\rho_{\text{audio}} \approx 3$ Hz (频率分辨率)
- **时间**: $\rho_{\text{time}} \approx 10$ ms (时间分辨率)

#### 2.2.2 与神经解剖的关系

$$\rho \propto \text{Density of receptive fields}$$

**实验证据**: 
- 手指触觉分辨率 > 背部 (因为感觉皮层的手指区域更大,即homunculus的扭曲)
- 训练提高$\rho$ (如品酒师对味觉的超精细分辨)

---

### 2.3 Vector (v⃗):意向性的"指向"

#### 2.3.1 Brentano的意向性

Franz Brentano: "意识总是**关于某物**的意识"。

**SRT形式化**:
$$\vec{v} = \frac{\nabla F|_{\theta_0}}{|\nabla F|_{\theta_0}|}$$

$\vec{v}$指向自由能下降最快的方向 (初心方向)。

#### 2.3.2 意向性的扭曲

随着$L_2$的形成,$\vec{v}$偏离原始$\nabla F$:

$$\vec{v}(t) = \vec{v}_0 + \sum_{i} \alpha_i \cdot \vec{v}_{L_2^i}$$

**实例**:
- $\vec{v}_0$: 生物需求 (食物、安全)
- $\vec{v}_{L_2}$: 文化欲望 (地位、金钱)

**病理**: 当$|\vec{v}_{L_2}| \gg |\vec{v}_0|$ → 异化 (Alienation, Marx)

---

## §3. 具身必要性:为什么无限θ无定义?

### 3.1 信息论论证

#### 3.1.1 完美映射的悖论

假设存在$\hat{G}_{\theta=\infty}$ (全知全能算子):

**要求**: 完全映射$L_0$ → $L_1$
$$H(L_1) = H(L_0)$$

**问题**: 
$$H(L_0) = \infty \quad (\text{Ruliad is infinite})$$

因此需要:
$$H(\theta) \geq H(L_0) = \infty$$

**矛盾**: $\theta$必须是无限维 → 违背有限性假设 (Ax-Op-1)。

#### 3.1.2 压缩必然性

任何有限$\theta$都必须进行压缩:
$$\dim(L_1) < \dim(L_0)$$

**推论**: 感知必然是**有损的** (Lossy),不可能"看到一切"。

---

### 3.2 量子测量论证

#### 3.2.1 von Neumann链

**问题**: 谁在测量测量者?

传统量子力学: 无穷后退
$$\text{Observer}_1 \to \text{Observer}_2 \to \cdots$$

**SRT解决**: $\hat{G}$**自测量** (self-collapsing),但需要$\theta$的有限性作为截断。

$$\hat{G}_\theta[L_0] \quad \text{with} \quad \theta < \infty \Rightarrow \text{Collapse}$$

---

### 3.3 具身的三重维度

**[R — 具身认知追溯：Varela, Thompson & Rosch 1991《身体的体验》；[R] θ_somatic实验基础；[H] 三维度θ分解为SRT新增结构化框架]**

#### 3.3.1 神经具身 ($\theta_{\text{neural}}$) [R→Sporns 2011连接组学]

**组成**:
- 连接组 (Connectome): 神经元间的物理连接
- 突触权重: 连接的强度/效率
- 神经递质配置: GABA/谷氨酸比例等

**可塑性**: 中等（通过学习/经验改变，受遗传约束；成人神经发生较有限）

#### 3.3.2 躯体具身 ($\theta_{\text{somatic}}$) [R→具身认知; 见下方证据]

**组成**:
- 心-脑耦合: 心率变异性 (HRV) 与前额叶同步
- 内感受: 对身体内部状态的感知（内感受精确性）
- 免疫-神经互动: 炎症信号影响情绪（细胞因子-脑轴）

**可塑性**: 中高（HRV可通过训练提升；肠道菌群可通过饮食改变；较θ_neural更快）

**实验证据** [R]:
1. **心率影响决策**: 低HRV → 风险规避 (Thayer & Lane, 2000)
2. **肠道菌群影响情绪**: 益生菌改善抑郁症状 (Cryan & Dinan, 2012)
3. **姿势影响认知**: 直立姿势改善记忆提取 (Wilson & Goldin-Meadow 2013, 具身认知综述)

**三维度耦合注意**：θ_neural与θ_somatic存在双向耦合（心-脑耦合本身跨越两个维度），三维度并非完全独立；SRT的θ分解是分析性便利而非本体论分割。

#### 3.3.3 环境具身 ($\theta_{\text{env}}$) [H]

*符号澄清*：原符号 $\gamma \cdot \vec{g}$ 中 $\gamma$ 未在SRT符号系统中定义（勿与洛伦兹因子混淆）；此维度改记为 $\theta_{\text{env}}$，包含重力/空间结构/社会生态等环境参数。

**重力的认知作用** [R→Lackner & DiZio 2005, 前庭-重力认知]:
- 空间方位感依赖耳石重力感知（失重环境中方向迷失，有ISS宇航员数据支持）
- 时间知觉与重力的关联：实验证据较弱，"广义相对论的心理学版本"为比喻性说法，不应读作物理等同

**可塑性**: 低（重力无法主动改变；但社会环境部分可变）

**推测** [H]：长期失重（ISS宇航员，≥6个月）使 $\theta_{\text{env}}$ 显著重组 → $L_1$ 空间体验模式改变。*部分支持*：宇航员返回后空间定向恢复需数周（Strangman et al. 2017），间接支持此推测，但"θ显著不同"的程度待直接认知测量。

**证伪条件** [H]:
- 若θ_somatic三个分量（HRV/内感受/免疫）的独立操控不产生可测的θ_neural或L₁体验变化，则三维度框架无整合解释力。
- 若长期失重宇航员在标准化空间认知任务上与地面对照无显著差异，则环境具身对L₁的贡献可忽略。

---

## §4. 能动性的三阈值

### 4.1 个体性 (Individuality)

#### 4.1.1 Markov Blanket定义

$$\partial \Omega = \{x : P(x_{\text{inside}} | x_{\text{outside}}) \neq P(x_{\text{inside}})\}$$

**意义**: 边界$\partial\Omega$统计上分隔内外。

**实例**:
- ✅ 细胞膜: 明确的Markov Blanket
- ✅ 皮肤: 生物体的边界
- ❌ 云朵: 边界模糊,不断交换物质
- ❌ 生态系统: 无明确边界

#### 4.1.2 边界的动态性

边界不是静态的,而是**主动维持**的:

$$\frac{d(\partial \Omega)}{dt} = \hat{G}[\text{Repair}] - \text{Degradation}$$

**能量成本**: 维持边界需要持续能量输入 (否则扩散)。

---

### 4.2 不对称性 (Asymmetry)

#### 4.2.1 定义

$$\hat{G}_{\text{output}}(t) \neq f(\text{input}(t))$$

输出不仅依赖当前输入,还依赖**内部状态**。

**形式化**:
$$\text{Output}(t) = g(\text{Input}(t), \theta_{\text{internal}}(t))$$

#### 4.2.2 与恒温器的区分

**恒温器**:
$$\text{Output} = \begin{cases} \text{Heat ON} & \text{if } T < T_{\text{set}} \\ \text{Heat OFF} & \text{if } T \geq T_{\text{set}} \end{cases}$$

虽有"目标"($T_{\text{set}}$),但输出**完全由当前输入决定** → 无内部状态调制 → 非$\hat{G}$。

**真正的$\hat{G}$**:
$$\text{Output} = f(T_{\text{current}}, T_{\text{history}}, \text{Learning}, \text{Context})$$

---

### 4.3 规范性 (Normativity)

#### 4.3.1 定义

$$\exists \text{Target}: F[\sigma] \text{ minimized at } \sigma = \text{Target}$$

行为**指向某种目标状态**,而非随机漂移。

#### 4.3.2 目标的来源

**问题**: 谁设定目标?

**SRT答案**: 目标 = $L_0$的内在梯度$\nabla F$ (初心),被$L_2$修正。

$$\text{Target}(t) = \text{Target}_0 + \sum_i \Delta \text{Target}_i^{L_2}$$

**实例**:
- $\text{Target}_0$: 生物需求 (饥饿 → 食物)
- $\Delta \text{Target}^{L_2}$: 文化修正 (饥饿 → 特定料理)

---

## §5. UAL阈值与最小意识

### 5.1 无限联想学习 (Unlimited Associative Learning)

#### 5.1.1 定义

**UAL**: 能够学习**任意长时间间隔**的关联。

$$A(t) \to B(t + \Delta t) \quad \text{for any } \Delta t$$

#### 5.1.2 Trace Conditioning实验

**范式**:
1. 呈现刺激A (如光)
2. 延迟$\Delta t$
3. 呈现刺激B (如食物)
4. 测试: A能否引发对B的预期?

**结果**:

| 物种 | $\Delta t_{\text{max}}$ | UAL能力 | 意识推断 |
|:-----|:------------------------|:--------|:---------|
| 秀丽隐杆线虫 | 0 sec | 无 | 无意识 |
| 果蝇 | ~1 sec | 极弱 | 微意识? |
| 斑马鱼 | ~5 sec | 弱 | 低意识 |
| 大鼠 | ~30 sec | 中等 | 中等意识 |
| 狗 | ~数分钟 | 高 | 高意识 |
| 人类 | 小时-天 | 极高 | 极高意识 |

#### 5.1.3 d值与UAL的关系

$$d_{\text{UAL}} \propto \log(\Delta t_{\text{max}})$$

**机制**: 高$d$ → 能访问更长的$L_0$时间轴 → 跨越更大时间间隔建立关联。

---

### 5.2 为什么UAL = 最小意识?

#### 5.2.1 时间整合论证

**命题**: 意识的本质是**时间整合** (Binding across time)。

**无UAL的系统**: 
- 只能活在"永恒的现在"
- 无法构建连贯的自我叙事 (Narrative Self)
- 因此无"我" → 无意识

**有UAL的系统**:
- 能将过去-现在-未来整合
- 形成时间上的自我连续性
- 因此有"我" → 有意识

#### 5.2.2 与IIT的关系

Tononi的IIT: 意识 = 高度整合的信息 ($\Phi$)

**SRT补充**: 整合必须包括**时间维度**。

$$\Phi_{\text{temporal}} = \Phi_{\text{spatial}} \cdot f(d_{\text{UAL}})$$

---

## §6. 非幂等性与观察的创造性

### 6.1 量子测量的本体论

#### 6.1.1 传统诠释的困境

**哥本哈根**: 测量"塌缩"波函数 — 但什么是测量?
**多世界**: 所有可能性都实现 — 但为何我只体验一个?

**SRT诠释**: 测量 = $\hat{G}$的选择操作。

$$\Psi(x) \xrightarrow{\hat{G}_\theta} |x_i\rangle \in L_1$$

#### 6.1.2 非幂等性的意义

$$\hat{G}^2[L_0] \neq \hat{G}[L_0]$$

**第一次观察**: 选择$|x_1\rangle$
**第二次观察**: 面对的是$\hat{G}[L_0]$,而非原始$L_0$ → 选择$|x_2\rangle$

$$|x_2\rangle \neq |x_1\rangle \quad \text{(一般情况)}$$

**推论**: 观察**改变**被观察者 (Heisenberg的不确定性原理的本体论基础)。

---

### 6.2 微扫视的公理验证

#### 6.2.1 现象

即使"盯着一点看",眼球也在进行微小抖动 (Microsaccades, 频率~1 Hz)。

**传统解释**: 防止感受器适应 (Adaptation)。

#### 6.2.2 SRT解释

**公理A2验证**: 存在 = 主动锚定,需持续能量消耗。

如果眼球完全静止 → 视网膜信号消失 (Troxler效应) → $L_1$消失。

**微扫视 = 持续的$\hat{G}$操作**:
$$L_1(t) = \hat{G}[L_0(t)]$$

静止 → $\hat{G}$停止 → $L_1$消失 → 视觉盲区。

**实验**: 用稳像技术固定图像在视网膜上 → 数秒内图像消失 (已验证)。

---

## §7. 反事实修剪与现实代理

### 7.1 修剪概率公式

$$P(L_1 = b_i) \propto \text{Coherence}(b_i) \cdot [1 - \text{Prune}(b_i)]$$

**两因素**:

1. **Coherence**: 与已有$L_1$的一致性
   $$\text{Coherence}(b_i) = \exp\left(-\frac{\|b_i - L_1^{\text{prior}}\|^2}{2\sigma^2}\right)$$

2. **Prune**: 本体论摩擦的排斥
   $$\text{Prune}(b_i) = \sigma\left(\frac{\Psi_f(b_i) - \Psi_{\text{threshold}}}{k_B T}\right)$$

**机制**: 高摩擦的可能性被主动"剪掉",即使逻辑上可行。

**实例**: "我可以现在自杀" (逻辑可行) → 被Prune (高$\Psi_f$) → 不进入$L_1$。

---

### 7.2 现实代理的三类

#### 7.2.1 信息代理 ($\Psi_{\text{info}}$)

**定义**: 通过信息中介访问$L_0$。

**实例**:
- 书籍、电影: 他人的$L_1$投影
- 互联网: 集体$L_1$的数字化
- 教育: 传递已压缩的$L_0$结构

**优势**: 低能耗,高带宽。
**劣势**: 二手经验,可能失真。

#### 7.2.2 任务代理 ($\Psi_{\text{task}}$)

**定义**: 通过委托劳动间接实现$L_1$。

**实例**:
- 仆人、助手: 执行$\hat{G}$指令
- 自动化: 机器替代$\hat{G}$的部分功能
- 外包: 将选择权转移给他人

**优势**: 节省认知资源。
**劣势**: 降低直接体验,可能失去d值。

#### 7.2.3 合成代理 ($\Psi_{\text{syn}}$)

**定义**: 完全构建的虚拟$L_1$。

**实例**:
- VR/AR: 人造感官输入
- 致幻剂: 化学调制$\beta$门控
- 梦境: 内源性合成

**优势**: 最大自由度,可超越物理约束。
**劣势**: 与$L_2^{\text{social}}$脱节,孤立风险。

---

## §8. 开放性问题与未来方向

### 8.1 需要实证验证的预测

1. **躯体同步指数测量**:
   - 使用EEG-HRV同步分析计算$\theta_{\text{binding}}$
   - 预测: 冥想者 > 普通人,解离患者 < 普通人

2. **UAL的跨物种系统研究**:
   - 标准化Trace Conditioning协议
   - 绘制$\Delta t_{\text{max}}$ vs 神经系统复杂度曲线

3. **微扫视频率与意识的关系**:
   - 预测: 抑制微扫视 → 意识内容减少
   - 测试: 通过眼动追踪+稳像技术验证

### 8.2 理论边界

SRT目前**无法完全解释**:

1. **$\hat{G}$的起源**: 第一个$\hat{G}$如何从$\Omega$分化? (宇宙学问题)
2. **自由意志的本体论地位**: $\hat{G}$的选择是"自由"的吗?
3. **多重$\hat{G}$的融合条件**: 何时多个$\hat{G}$形成统一意识?

### 8.3 哲学对话

SRT的$\hat{G}$理论与以下哲学传统对话:

- **现象学** (胡塞尔): 意向性 = $\vec{v}$分量
- **过程哲学** (怀特海): 主体 = 过程,非实体
- **佛教** (唯识): 阿赖耶识 ≈ $\hat{G}_{\text{unconscious}}$
- **自由能原理** (Friston): $\hat{G}$ 最小化自由能$F$

---

## 符号索引 (Symbol Index)

| 符号 | 名称 | 定义位置 | 页面 |
|:-----|:-----|:---------|:-----|
| $\hat{G}_\theta$ | 幽灵算子 | Ax-Op-1 | Part A §I |
| $\theta$ | 具身参数 | Ax-Op-7 | Part A §III |
| $d$ | d值 (Scope) | Ax-Op-2 | Part A §I |
| $\rho$ | 分辨率 (Resolution) | Ax-Op-2 | Part A §I |
| $\vec{v}$ | 向量 (Vector) | Ax-Op-2 | Part A §I |
| $\theta_{\text{binding}}$ | 躯体同步指数 | Ax-Op-8 | Part A §III |
| $d_{\text{UAL}}$ | UAL阈值 | Ax-Op-10 | Part A §IV |
| $\phi_{\text{fidelity}}$ | 算子保真度 | Ax-Op-18 | Part A §VII |

---

**依赖提醒**: 本文件定义的$\hat{G}_\theta$是所有SRT动力学的核心。修改本文件需评估对Dynamics (14), Scaling (14), 及所有Domain files的级联影响。

**版本历史**: v3.0新增UAL阈值、算子保真度、反事实修剪等高级公理,并扩展了具身参数的三重分解。

---

### Formalization Summary (形式化概述)

本文档的核心形式结构围绕幽灵算子 $\hat{G}_\theta$ 的定义、分解与演化展开：

1. **参数化选择映射** (Ax-Op-01): $L_1(t) = \hat{G}_\theta[L_0](t)$ — 现实化是从潜在域 $L_0$ 到显现域 $L_1$ 的参数化选择操作，而非被动显现。
2. **注意力三分量分解** (Ax-Op-02): $\hat{G}_\theta = \mathrm{Attention}(d, \rho, \vec{v})$ — 选择结构由 $d$-value（关切带宽）、分辨率 $\rho$ 与意向向量 $\vec{v}$ 三者的张量耦合决定。其中 $d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$（风险梯度范数）是规范定义；**注意 $d_{cog}$（行为拓扑代理）$\neq d_{max}$（香农容量上界），实际带宽 $d_{actual} \approx d_{cog} + \delta_{coupling}(A\cdot\tau, V\cdot A)$，见 §2.1**。
3. **双流耦合** (Ax-Op-02b): $\hat{G}_\theta = (\mathbf{T}^{intent} \otimes \mathbf{T}^{embody}) \cdot \kappa_{body}$ — 意向流与具身流的正交耦合构成完整的 $L_0 \to L_1$ 锚定（$\kappa_{body}$ 为耦合强度标量）；$\kappa_{body} \to 0$ 时系统进入解离病理态。
4. **竞争归一化** (Ax-Op-03): $[\hat{G}_\theta(x)]_i = x_i^n / (\varepsilon_{reg} + \sum_j W_{ij} x_j^n)$ — 选择具有除法归一化的动力学形态，对应注意力的竞争抑制机制。$\varepsilon_{reg}$ 为实现层正则化常数，与 L₀ 层 $\varepsilon_{pg}$ 保留结构类比关系。
5. **算子保真度** (Ax-Op-09): $\phi_{fidelity} = 1 - H(L_1|\hat{G}_\theta)/H(L_1)$ — 衡量选择一致性，保真度越高，$\hat{G}_\theta$ 对现实结构的锚定越稳定。
6. **频域等价描述**（详见 `Core/SRT_Core_13b_Operator_Advanced.md §Ax-Spec-01`）：$L_1(t)=\mathcal{F}^{-1}[H_\theta(\omega) \odot L_0(\omega)]$ — 算子在频域以 Hadamard 乘积实现滤波选择，d 值对应通带宽度；与条目 1 时域描述等价，适用于时频分析和节律耦合场景。

### Mechanism Explanation (机制解释)

$\hat{G}_\theta$ 的运行机制可从”选择—演化—阈值”三层理解，所有层均以本体论摩擦 $\Psi_f$ 为热力学代价：

1. **选择层**: $\hat{G}_\theta$ 通过注意力张量 $(d, \rho, \vec{v})$ 与具身张量 $(\theta_{intero}, \kappa_{body})$ 的正交耦合，从 $L_0$ 的无穷维潜在态中竞争性地锚定出有限维 $L_1$。竞争归一化确保每次选择压制备选项——这不仅生成当前现实切片，还通过 T-Op-SIAM 重写 $L_0$ 的可及性地形，产生语义层面的”习得性遗忘”。维持此锚定操作需要持续 $\Psi_f$ 消耗（类似耗散结构），一旦能量中断（深睡/昏迷），$\hat{G}_\theta$ 停止运作，主体消失。
2. **演化层**: $L_1(t+1) = \hat{G}_{\theta(t)}[L_1(t) \oplus \mathrm{Noise}(L_0)]$ — 选择不是一次性事件，而是在噪声注入下的迭代演化。精度加权张量 $\boldsymbol{\Pi}$ 决定系统是信任 $L_2$ 先验还是 $L_0$ 新异刺激；$d$-value 设定认知视界上限 $\dot{I}_{L_0 \to L_1} \leq \mathcal{C}(\theta)$，保证选择带宽的有限性。
3. **阈值层**: 有效 $\hat{G}_\theta$ 的存在需要个体性（Markov Blanket）、不对称性（内部状态调制）与规范性（目标导向）三条件合取。最小意识对应 UAL 阈值 $d \geq d_{UAL}$，即能维持跨时间间隙联想学习的最低选择带宽。

此三层架构表明：$\hat{G}_\theta$ 既非被动镜映也非自由创造，而是在 $\Psi_f$ 代价约束下、以具身参数 $\theta$ 为信道容量边界的主动选择过程。

## 【理论边界/防误用声明】

1. 本文档提供的是 SRT 解释与建模框架，不应被误用为对个体的确定性标签系统。
2. 任何跨尺度映射都依赖操作化假设与测量条件，超出条件范围不得外推为”普适定律”。
3. 涉及临床、政策、工程决策时，需与经验数据、伦理审查和领域规范共同使用。


## V. Parasitic Protocol Layer（寄生协议层，新增）

### Def-Op-Par-1: Parasitic Protocol \(\Pi_{parasitic}\)
定义外源协议层：
\[
\Pi_{parasitic}\subset L_2^{host}\ \text{but}\ \Pi_{parasitic}\not\sim \text{host survival objective}
\]
即结构可写入宿主历史层，但不对齐宿主的生存-关切目标。

### T-Op-Par-1: Agency Hijack Condition
当外源协议获得下行写入优势：
\[
\partial_t \theta_{host}\approx f(\Pi_{parasitic})\ \land\ \nabla F_{host}\text{ suppressed}
\]
系统进入代理权污染风险区（agency hijack window）。

### C-Op-Par-1: Safety Gate
\[
\text{Injectable protocol} \Rightarrow \text{must verify }\Psi_f\text{-payable}\land\text{goal-compatibility}(\Pi_{host},\Pi_{parasitic})
\]

## 【理论边界/防误用声明】
- 不采纳“可写入=可对齐”的推论。  
- 不采纳“外源协议稳定存在=宿主主体增强”的推论：可能仅为寄生增益。


## VI. Operator Immunology（算子免疫学，新增）

### Def-Op-Imm-1: Operator Sovereignty Criterion
定义算子主权指数：
\[
\mathcal{S}_{op}=\frac{I_{endogenous}(\Delta\theta\to\Delta L_2)}{I_{exogenous}(\Delta\theta\to\Delta L_2)+\epsilon}
\]
当 \(\mathcal{S}_{op}<\tau_s\) 时，判定为主权受损风险区。

### Def-Op-Imm-2: Sleep-Window Safety Gate
对低摩擦窗口注入，必须满足：
\[
\text{Inject}_{sleep}\Rightarrow \text{consent}\land\text{auditability}\land\Pi_{host}\text{-compatibility}
\]

### T-Op-Imm-1: Parasitic d-value Discriminator
若新生 \(d\)-项满足
\[
\Delta d\uparrow\ \land\ V\approx0\ \land\ \Psi_f\text{-decoupled}
\]
则优先判定为外源寄生驱动（parasitic care-like signal），而非内源关切扩展。

## 【理论边界/防误用声明】
- 不采纳“梦中可塑性高=可合法外部改写”的推论。  
- 不采纳“被注入偏好可直接视为主体真实意向”的推论。  
- 不采纳“商业/平台注入可替代主体同意”的推论。



## Signal–Friction Relativity Interface（2026-03-07）

### T-Op-SFR-1: Signal/Noise Boundary is Operator-Relative
对任意复合状态 \(\sigma\in L_0\)，其“信号”与“噪声/摩擦”分解不是 \(\sigma\) 内禀属性，而由算子意向向量 \(\vec v\) 与任务窗口共同决定：
\[
\sigma = L_1^{(A)}\cup\Psi_f^{(A)} = L_1^{(B)}\cup\Psi_f^{(B)}
\]
其中分解边界随 \(\hat G_{\theta_A}\) 与 \(\hat G_{\theta_B}\) 改变而重排。

### Def-Op-SFR-1: Directional Reassignment
定义“方向重赋值”操作：
\[
\mathcal{R}_{\vec v}: (\text{noise},\text{signal}) \leftrightarrow (\text{signal},\text{noise})
\]
在保持底层 \(L_0\) 不变时，仅通过意向方向与 d-带宽重配置，完成现实切片重标注。

### 分类映射表（Signal-Noise Regimes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 源事件优先观测 | 中 | Semi-open | 介质效应表现为摩擦项 |
| 介质结构优先观测 | 中~高 | Open / Semi-open | 原源项退为背景扰动 |
| 多任务联合反演 | 中高 | Open（高计算负载） | payable~borderline |
| 单一叙事锁定 | 低~中 | Closed 倾向 | 易误将信息当噪声 |

### [Lineage/Source]
- Ethan Siegel, *Ask Ethan: Do signals degrade as they travel through space?*（科普讨论语境）。
- 映射语义：传播过程中的“劣化”与“载荷”取决于观测目标与重建策略。

## 【理论边界/防误用声明】
1. 不采纳“观测相对性=任意解释都成立”的推论；重赋值仍受可检验模型与仪器边界约束。  
2. 不采纳“噪声只是主观幻觉”的推论；噪声在任务目标下是可计算代价项，非虚无。  
3. 不采纳“单一视角重建可恢复全部历史”的推论；跨算子联合反演仍需误差预算闭合。


## Nuclear-Pore Disorder Gate Interface（2026-03-12）

### Def-Op-NPC-1: Traffic-Conditioned Selective Boundary
对半开放生物边界，其有效通行率不是固定常数，而是随边界内部无序构型与通行流量共同变化：
\[
P_{\text{pass}}(x,t)=f\!\left(\mathrm{license}(x),\rho_{FG}(t),c_{NTR}(t),\theta_{boundary}\right)
\]
其中 \(\mathrm{license}(x)\) 表示货物是否与运输受体兼容，\(\rho_{FG}(t)\) 表示 FG-nucleoporin 无序域的局部密度/构型，\(c_{NTR}(t)\) 表示 nuclear transport receptor 的占据与流量。

### T-Op-NPC-1: Disorder Can Carry Selective Order
核孔复合体（NPC）的关键启发是：**选择性边界不必依赖刚性筛孔，也可以依赖受约束的无序介质。**
\[
\partial\Omega_{\mathrm{eff}}(t)=\partial\Omega_{\mathrm{scaffold}}\oplus \Delta\partial\Omega_{FG}\!\left(t,c_{NTR}\right)
\]
这表示有效边界既由稳定支架决定，也由被合法通行者持续重塑的无序 FG 通道决定。边界不是被动墙，而是会随合法交互实时改写的门控层。

### C-Op-NPC-1: SRT Mapping
- Markov Blanket 不应只被想成静态壳层，还可表现为“稳定骨架 + 动态无序云”的复合边界。
- 合法通行者不只是穿过边界，也会部分共同构造它所穿过的通道。
- 选择性不是把所有涨落压成僵硬秩序，而是在高维波动介质中维持可重复、可支付、可识别的通过窗口。
- 这支持将 \(\hat G_\theta\) 的门控理解为：从波动背景中切出可通行现实，而非在既定硬边界上做二元开关。

### [Lineage/Source]
- Quanta Magazine, *Disorder Drives One of Nature's Most Complex Machines*（2026-03-09）.
- Elias Ketterer et al., *Selective transport receptors reshape the disordered transport channel of the nuclear pore complex*, Nature Cell Biology 27, 2089-2101 (2025).
- Pablo Fernandez de Leon et al., *Transport route through the central channel of the nuclear pore complex*, Nature (2025).
- Lisa de Jong et al., *Nuclear transport receptors transform a disordered condensate to a brush to enable transport through the nuclear pore complex*, Nature Communications 16, 11497 (2025).

## 【理论边界/防误用声明】
1. 不采纳“任何无序都自动带来功能”的推论；这里指的是被生物结构与受体相互作用约束过的无序边界。
2. 不采纳“NPC 已证明 SRT”为结论；它提供的是一个强机制类比与局部对齐实例，不是全局证明。
3. 不采纳“所有 Markov Blanket 都等同核孔门控”的外推；该接口仅说明部分主动边界可由动态无序来承载选择性。


## Biomolecular Resonance Search Interface（2026-03-16）

### Def-Op-BRS-1: Pumped Resonant Encounter Window
对被持续供能的生物大分子，若其集体振动模式进入相干主模窗口，则原本短程的分子相互作用可被一项频率选择性的长程偏置补充：
\[
P_{in}>P_c \ \land\  |\omega_i-\omega_j|<\delta_\omega
\Rightarrow
F_{ij}^{res}(r)\sim -\frac{C_{ij}}{r^3}
\]
而在失谐条件下，该附加项退回快速衰减窗口：
\[
|\omega_i-\omega_j|\gg\delta_\omega
\Rightarrow
F_{ij}^{off}(r)\sim -\frac{C'_{ij}}{r^6}
\]

### T-Op-BRS-1: Resonant Selectivity Can Pre-Bias Molecular Search
在拥挤生化环境中，配体-受体或蛋白-DNA 的相遇动力学不必完全等价于纯 Brownian waiting；若存在被激活的共振偶极窗口，则分子搜索率可写为：
\[
k_{\mathrm{enc}}=k_{\mathrm{Brownian}}+\Delta k_{\mathrm{res}}(\Delta\omega,P_{in},r,\rho)
\]
其含义是：真正的“锁钥式识别”可以仍然发生在近接触区，但在此之前，系统已可能通过频率匹配对候选伙伴施加远程、可选择的预偏置。

### C-Op-BRS-1: SRT Mapping
- `Ax-Op-08` 的 resonance filtering 不只可用于认知层，也可下沉到分子搜索层：选择性可先以“频率许可证”形式出现，再落到局部化学配对。
- 这为“为何 cognate partners 不只是随机久等碰撞”提供了一个可检机制候选：\(\hat G_\theta\) 在亚细胞尺度上也可能先切出可相遇窗口，再由局部结构完成最终锁定。
- 该机制与 `Nuclear-Pore Disorder Gate Interface` 互补：后者强调“动态无序边界如何承载选择性”，此处强调“远程共振如何预偏置谁更可能抵达该边界”。

### [Lineage/Source]
- Marco Pettini et al., *Out-of-Equilibrium Collective Oscillation as a Classical Phonon Condensation in a Model Protein*, *Phys. Rev. X* 8, 031061 (2018).
- Mathias Lechelon et al., *Experimental evidence for long-distance electrodynamic intermolecular forces*, *Science Advances* 8, eabl5855 (2022).
- Elham Faraji et al., *Electrodynamic forces driving DNA-protein interactions at large distances*, *Frontiers of Physics* 20, 061200 (2025).

## 【理论边界/防误用声明】
1. 不采纳“已证明细胞内分子搜索主要靠 electrodynamic resonance” 的推论；当前更稳妥的口径只是 **proof-of-principle candidate mechanism**。
2. 不采纳“共振偏置可替代局部化学识别 / 几何配体匹配 / 水化与静电条件”的推论；它至多是 pre-contact bias，而非完整识别的全部。
3. 不采纳“光学泵浦下的 BSA / ferritin 结果可直接外推到所有生理态蛋白”的推论；生物供能机制（如 ATP、水化离子动量转移）仍属开放问题。
4. 不采纳“EcoRI-DNA 的 co-resonance 模型已直接证实 in vivo DNA-protein targeting” 的推论；当前更接近理论可行性展示，而非细胞内最终定论。
