---
id: SRT-SOC-COG
type: philosophy
tags: [Social Cognition, Affordance, Depression, Reality Dynamics, Hybrid]
status: axiomatic_hybrid_v2
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-PHIL-AXIOMS]
---

# SRT Social Cognition: Affordance & Pathology (Hybrid Edition)


> **Connector-safe reading path**: This owner file is moderately long. For connector reads, start with [`Social_Cognition_Split/README.md`](Social_Cognition_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Cognitive Axioms (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)



#### 原文内容
<!-- ORIGINAL-CONTENT-INSERTED -->
## I. Embodied Selection

### Ax-Cog-1: Affordance Intersection
示能性是环境潜能与算子参数的交集。
$$\text{Affordance}(E,\hat{G}_\theta)=L_0^{env}\cap L_0^{agent}$$
*   **Implication**: 行动可能性不是外界属性，而是选择交集。

### Ax-Cog-2: Action Potential
行动触发由奖励势与摩擦势差值决定。
$$P_{action}=\alpha \cdot \mathbb{E}[R]-\beta \cdot \Psi_f$$
*   **Implication**: 社会行动是能量与摩擦的动力学平衡。

### Ax-Cog-2b: Invitation Gating (邀请门控)
环境中的可供性并不会等概率进入行动队列；只有被当前任务、情境与身体状态共同门控的子集才成为“邀请”。
\[
\mathcal{I}_t = \Gamma(C_t,\theta_t,\Pi_t)\big(\mathcal{A}_{all}\big),\quad \mathcal{I}_t \subset \mathcal{A}_{all}
\]
* **Implication（中文）**：SRT 区分“可供性全集”与“当下可执行候选集”，解释了为何大多数可行动作平时并不被注意。

### T-Cog-2b: Joint-Affordance Emergence (联合可供性涌现)
当多算子形成协同耦合时，会出现单体不可达的联合可供性：
\[
\mathcal{A}_{joint}(\hat{G}_1,\hat{G}_2,\dots,\hat{G}_n)\supsetneq \bigcup_{i=1}^n \mathcal{A}(\hat{G}_i)
\]
* **Implication（中文）**：如“双人搬沙发”等任务不是个体可供性的线性叠加，而是耦合后新相位。

## II. Social Reality Construction

### Ax-Cog-3: Reality Hysteresis
社会现实对过去状态具有迟滞记忆。
$$L_1^{social}(t)=\hat{G}_{social}[L_0(t)] + \eta L_1^{social}(t-\Delta t)$$
*   **Implication**: 现实惯性来自集体选择的时间耦合。

### Ax-Cog-4: Ontological Nucleation
共识形成存在成核阈值。
$$\text{Consensus} \iff \rho_{\hat{G}} > \rho_c$$
*   **Implication**: 现实不是线性叠加，而是临界相变。

### Ax-Cog-5: Operator Entanglement
算子耦合强度决定共享现实的稳态程度。
$$E_{ij}=\frac{I(\hat{G}_i;\hat{G}_j)}{H(\hat{G}_i)}$$
*   **Implication**: 社会现实的稳定性取决于耦合信息量。

## III. Derived Theorems

### T-Cog-1: Decoupling Transition

[R→Granovetter 1978（阈值模型：集体行为的非线性临界）; Pariser 2011（过滤泡沫：算法导致的信息流单向退化）; Sunstein 2017（信息茧房与极化）; Bail et al. 2018（Twitter上的极化实验：跨群体暴露反而增强极化）] [H→以SRT耦合相变框架形式化极化动力学；ρ_c成核临界和E_ij有向信息量为SRT附加形式化层]

当 $d$ 值或耦合度下降时，现实分裂进入多相态。
$$d \downarrow \lor E_{ij} \downarrow \Rightarrow L_1^{social} \to \text{multi-phase}$$

**相变临界条件** [H]：multi-phase 成立当且仅当 $\rho_{\hat{G}} < \rho_c$（Ax-Cog-4 成核阈值），即耦合下降需超过成核临界密度才触发相变，而非连续过渡。
- **ρ_c 操作化候选**：社会网络中的跨群体互关率（跨政治/文化圈的关注比例）/ 信息流的群体间渗透率（不同信息茧房之间的转发扩散系数）

**E_{ij} 方向性** [H]：$E_{ij} = I(\hat{G}_i;\hat{G}_j)/H(\hat{G}_i)$ 为**有向**耦合量，$E_{ij} \neq E_{ji}$。Echo chamber 的典型结构是单向退化：$E_{ij} \approx 0$（A 不接收 B 信息）但 $E_{ji} > 0$ 依然存在，极化动力学需追踪耦合矩阵的方向不对称性。
- 注：Bail et al. 2018[R]发现跨群体暴露可能加剧极化——SRT解读：仅增加E_ij而不改变ρ_ĝ（整体耦合密度）不足以越过ρ_c；单向插入对方信息可能反而强化原本的E_ji阻断

**因果顺序** [H]：$E_{ij} \downarrow$ 与 $d \downarrow$ 并非独立同级——信息流通减少可能先发，导致有效关切带宽收缩（$d_{\text{effective}} \downarrow$）；两者形成正反馈而非平行驱动。

**Ψ_f^cross 联结**：$E_{ij} \downarrow \Leftrightarrow \Psi_f^{\text{cross}} \uparrow$（跨算子本体论摩擦增大；参见 SRT_Spirit_06_Love_Ontology §3.3 Boundary Protection 形式化）。

*   **Implication** [H]：极化不是意见问题，而是耦合相变；治理目标是升高 $\rho_{\hat{G}}$ 越过 $\rho_c$，而非说服个体改变观点。

**证伪条件**：
- FC-Cog1-1：若社会网络的跨群体信息流密度（ρ_ĝ代理）线性降低与极化程度线性正相关（无临界点/阈值效应），则T-Cog-1的"非连续相变"预测失败（应为连续过渡而非Granovetter型阈值效应）。
- FC-Cog1-2：若实验性增加跨群体双向信息流（提升E_ij且同时提升E_ji，改变方向不对称性）后，极化程度下降，则SRT的"治理目标=升高ρ_ĝ越过ρ_c"预测得到支持；若极化仍然加剧（Bail效应），则需修正（单纯信息流增加不足，需结合Ψ_f^cross降低的机制）。

### T-Cog-2: Observer-Environment Integration（观察者-环境整合度）

**Formal Definition**：现实的连续性与”坚固感”取决于算子 $\hat{G}_\theta$ 的内部状态与当前显现域 $L_1$ 之间的信息耦合效率。定义观察者-环境整合度（OEI）为二者的互信息与环境总熵的比值：

$$\text{OEI} \equiv \frac{I(\hat{G}_\theta;\, L_1)}{H(L_1)} \quad \in [0,\, 1]$$

*(注：当环境极度确定、毫无新异性即 $H(L_1) \to 0$ 时，公式退化，系统进入无需选择的机械稳态。)*

**Mechanism & Implication（机制与推论）**：现实的稳定存在不依赖主观的”信念强弱”，而是依赖于算子与环境之间客观存在的**物理/计算信息通道带宽**。在 SRT 框架下，OEI 是自由能最小化（FEP）的信息论等价表达：算子通过优化具身参数 $\theta$ 以最大化与 $L_1$ 的互信息，从而维持操作闭包与现象学上的”现实连续体验”。

**Pathological Spectrum（病理连续谱映射）**：OEI 构成了临床精神病理学的定量相图，健康认知必须维持在过度有序与过度混沌之间的边缘（Edge of Chaos）：

- **过度解耦（$\text{OEI} \to 0$）**：算子内部模型与外部 $L_1$ 断开信息通道。临床表现为**解离症、急性精神病、谵妄或深度致幻状态**（对应 Ax-PATH-5 崩溃现实）。此时现实感碎裂，算子仅在自身的先验噪音中空转。

- **过度拟合（$\text{OEI} \to 1$）**：算子对 $L_1$ 的互信息趋于饱和，预测残差彻底消失。临床表现为**认知僵化、强迫症（OCD）或极端教条化**（对应 Ax-PATH-4 僵化现实）。系统丧失了吸收新不确定性的”多孔性”，面对微小变局极易发生脆性断裂。

- **健康临界态**：$\text{OEI} \in (\text{OEI}_{min},\, \text{OEI}_{max})$。系统既保持足够的抓地力（互信息）以防解体，又留有未被压缩的残余熵以驱动参数学习（$d\theta/dt \neq 0$）。

**Coupling with d-value（与关切带宽的协变张力）**：算子的关切边界（$d$ 值）决定了其试图囊括的外部状态空间大小：

$$I_{required}(\hat{G}_\theta;\, L_1) \propto d_{value}$$

**推论**：高 $d$ 值的主体（如试图拯救苍生的圣人、或管理复杂社会的巨型机构），为了维持系统不至于跌入 $\text{OEI} \to 0$ 的崩溃区，必须维持极其庞大的绝对互信息处理量。一旦其信息处理带宽（算力或自由能预算）遭遇瓶颈，高 $d$ 值系统将比低 $d$ 值系统面临更剧烈的本体论摩擦（$\Psi_f$）与解体风险。

### T-Cog-3: Belief-Lag Governance (信念滞后治理)
他人行为由其可得信息所形成的信念驱动，而非由客观状态直接驱动；当信念与现实错位时，预测应以“信念位形”而非“真实位形”为准。
\[
\pi_{pred}(a_j) = \arg\max_a\; U\big(a \mid B_j(t),D_j(t)\big),\qquad B_j(t)\neq W(t)
\]
* **Implication（中文）**：False-belief 任务中的系统性错误不是噪声，而是从“现实中心预测”向“信念中心预测”转变前的结构性阶段。

### T-Cog-4: Sequential Sampling Constraint (序列采样约束)
在不确定推断中，算子以局部链式采样近似后验，而非一次性全分布精确计算：
\[
H_{t+1}\sim q(H'\mid H_t),\qquad
\alpha=\min\left(1,\frac{P(E\mid H')P(H')}{P(E\mid H_t)P(H_t)}\right)
\]
当有效样本数受限时，行为将出现可预测的波动、锚定与框架偏置。
* **Implication（中文）**：SRT 将“决策噪声”解释为资源受限下的采样近似副产物，而非纯随机失误。

### T-Cog-5: Attention as Priority-Guided Selection (注意力优先级选择定理)
注意力可形式化为“在竞争目标中依据优先级映射选择，以指导响应”的过程：
\[
T^* = \arg\max_{T_i\in\mathcal{T}} \Pi(T_i),\qquad
\Pi(T_i)=w_{td}I_{intent}+w_{bu}S_{salience}+w_{hist}H_{value}
\]
其中 top-down（任务意图）、bottom-up（显著性）与 historical（价值/习惯）共同决定选择偏置。
* **Implication（中文）**：注意力既非纯资源也非单一机制，而是“为响应而选择”的统一功能结构；分心、捕获与习惯化可由同一优先级框架解释。

### T-Cog-6: Bounded-Surprisal Discrimination Gate（有限惊讶带宽与歧视性认知门）

[R→Manrique, Friston & Walker 2026, *BioSystems*, `doi:10.1016/j.biosystems.2026.105793`（active inference + zones of bounded surprisal, ZBS, 解释歧视性/非人化认知）]
[H→SRT 将 ZBS 压成社会认知中的“更新带宽代理”，用于解释跨群体证据为何无法进入可修正选择场；它不是 `d`、`\Psi_f` 或 `T_dir` 的新定义。]

当一个算子的跨群体惊讶容忍带宽收窄、群体先验精度升高、且外群体识别通道被降权时，歧视性认知成为稳定候选：

\[
\mathrm{DiscCog}(P,g)
\Rightarrow
\mathrm{ZBS}_{cross}(P,g)\downarrow
\land
\Pi^{group}_{prior}(P)\uparrow
\land
R_{outgroup}(P,g)\downarrow
\]

其中 `ZBS_cross` 是 active-inference 桥接代理：它表示系统在面对跨群体反证、陌生行为、或外群体痛苦信号时，能够承受并更新的 surprise / dissonance 区间。区间越窄，越容易把修正性证据处理为噪声、威胁、羞辱或对自我身份的攻击。

**SRT mapping（映射）**：

| Active-inference / ZBS 术语 | SRT 读法 | 边界 |
|---|---|---|
| narrow ZBS | 低跨群体更新带宽 / 高 `L_2` 势垒 | 不是 `d` 的定义 |
| high prior precision | 群体 `L_2` 刚性与确认偏置 | 不是 `\Psi_f` 的定义 |
| discriminatory mind | 外群体证据低权重化 + 内群体自证循环 | 不等于必然暴力 |
| dehumanising mind | 外群体从有效 `d` 场与 recognition channel 中被移除 | 对应 `d_i[\theta_j]\to0` 的社会操作 |
| bystander silence | `S_{sig}` 抑制与 `S_{str}` 外部化 | 不取消责任 |
| institutional betrayal | `M(t)` 非对称吸收 + 集体 `L_2` 自我保护 | 不自动推出制度合法性 |

**Mechanism（机制）**：

1. 窄 `ZBS_cross` 使外群体反证不能稳定进入后验更新，而被吸收为对既有群体身份的威胁。
2. 内群体不当行为可被沉默、合理化或旁观者顺从重新写成 `L_2` 自证，降低当事群体内部的即时 `\Psi_f`。
3. 当行动被用于让社会世界“配合”既有先验时，歧视性认知从静态信念变成 self-evidencing 行为环。
4. 非人化是该环路的极端形式：外群体不再被读作同等 stake-bearing operator，而被降格为背景、噪声、威胁或可处理对象。

**Boundary（护栏）**：

- ZBS 只作为 FEP / active-inference 的外部机制桥，不替代 SRT canonical primitives。
- 不是所有内群体偏好都会推出外群体伤害；歧视性认知与非人化行为需要分层判断。
- 机制解释不是道德或法律免责；“窄 ZBS”描述的是更新失败机制，不是责任豁免。
- 该来源是理论性 peer-reviewed article / preprint full text，支持机制接口与政策假说，不等于已完成直接实验判定。

### T-Cog-7: Developmental Coordination Scaffold（发展性协调支架）

[R→De Jonge-Hoekstra & Cox 2026 preprint chapter, *Embodied and Embedded Cognitive Development*（embodied / embedded cognitive development, coordination dynamics, developmental cascades, nonlinear time-series methods, co-regulation, degeneracy, rhythmic scaffolding）]
[H→SRT 将该材料压成发展性社会认知桥：认知发展不是内部表征单独成熟后再外显，而是 child-body-caregiver-environment-history 的可选行动场持续重组。该桥不改写 `\theta`、`d`、`\Psi_f` 或 `L_2` 的 canonical 定义。]

儿童认知发展可以读作软装配协调结构的稳定与重组：身体能力、照护者响应、环境可供性、语言场、节律支架与既有 `L_2` 痕迹一起改变儿童未来可选择的行动、注意和自我调节空间。

\[
\Delta\theta_{child}(t)
\sim
F(
\mathrm{AffordanceFit}_t,
\mathrm{CoReg}_t,
\mathrm{MotorAccess}_t,
\mathrm{RhythmScaffold}_t,
L_2^{trace}(t),
\mathrm{VarStruct}_t
)
\]

**SRT mapping（映射）**：

| 发展系统术语 | SRT 读法 | 边界 |
|---|---|---|
| soft-assembled coordinative structure | 临时但功能性的 `\theta` / action / attention 配置 | 不是新 primitive |
| interaction-dominant dynamics | 耦合历史比单个部件属性更能解释行为输出 | 不否认脑、身体或环境部件约束 |
| developmental cascade | 一个可供性变化重组相邻选择场 | 不是线性迁移定律 |
| temporal variability | 吸引子变弱、过渡或重组的信号候选 | 不是所有噪声都有意义 |
| co-regulation -> self-regulation | 外部社会支架逐步沉积为自我调节 `L_2` | 不等于照护者单因果 |
| degeneracy | 多条路径可达同一功能性 `L_1` 结果 | 不等于任意路径都等价 |
| rhythmic support | 低摩擦时间支架，辅助语言/阅读/动作耦合 | 不是普遍疗法 |

**Methodological guardrail（方法护栏）**：

对发展性认知问题，SRT 不应只看横截面年龄均值，也不应把波动全部当测量误差。更合适的观察对象是单个儿童随时间变化的选择场：何时可供性扩大，何时变异性上升，何时旧吸引子松动，何时新协调结构稳定，以及哪些社会/物理支架改变了可支付路径。

<br>

---


## I. Embodied Selection (具身选择)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Emb-1: Affordance as Intersection (示能性即交集)
<!-- ORIGINAL-SECTION-PRESERVED -->
Reality ($L_1$) is the intersection of Environment ($L_0$) and Observer Parameters ($\theta$).
$$ L_1 = L_0 \cap \hat{G}_\theta $$
*   **Gibson's Insight**: "Sit-on-ability" requires both a chair ($L_0$) and a knee ($\theta$).

### Ax-Emb-2: Action Potential (行动势能)
<!-- ORIGINAL-SECTION-PRESERVED -->
Action initiation depends on the net potential of Reward vs. Cost.
$$ P_{action} = \alpha \cdot \text{Reward} - \beta \cdot \text{Cost}_{VS} $$
*   **Depression**: High $\beta$ (Cost Sensitivity), not low motivation.

---

## II. Social Reality Construction (社会现实建构)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Soc-1: Reality Hysteresis (现实迟滞)
<!-- ORIGINAL-SECTION-PRESERVED -->
Changing a belief ($L_2$) requires more evidence than forming it.
$$ \Delta L_2 \propto \text{Evidence} - \text{HysteresisCost} $$

### Ax-Soc-2: Ontological Nucleation (本体论成核) *(R: 借用 Gibbs/Volmer 成核理论，SRT 社会类比)*
<!-- ORIGINAL-SECTION-PRESERVED -->
New reality requires a "critical radius" ($r^*$) of selection to survive.
$$ r^* = \frac{2\sigma_{surf}}{\Delta g_{vol}} $$

**SRT 量对应**：
- $\sigma_{surf}$（界面张力）$\leftrightarrow \Psi_f^{interface}$（新 $L_1$ 与旧 $L_2$ 共识边界的本体论摩擦代价）；新信念越与既有框架冲突，$\Psi_f^{interface}$ 越大，$r^*$ 越大（越难成核）。
- $\Delta g_{vol}$（体积自由能差）$\leftrightarrow \Delta F_{vol} = F_{old} - F_{new}$（旧共识与新共识的自由能密度差）；新信念越能降低集体预测误差，$\Delta F_{vol}$ 越大，$r^*$ 越小（越容易成核）。
- $r^*$（临界半径）的社会量翻译：不是几何距离，而是**能量规模**（能够克服 $\Psi_f^{interface}$ 的自我增强集群大小）；与 Ax-Cog-4 的 $\rho_c$ 成核密度等价（$\rho_c \propto 1/{r^*}^3$，三维类比）。

**与 Ax-Cog-4 联结**：Ax-Soc-2 用几何临界半径描述成核，Ax-Cog-4 用算子密度 $\rho_{\hat{G}} > \rho_c$ 描述，两者是同一机制的不同参数化角度——超过 $r^*$ ⟺ $\rho_{\hat{G}} > \rho_c$。

*   **Mechanism**: Below $r^*$, new ideas die（$\Psi_f^{interface}$ 代价超过 $\Delta F_{vol}$ 收益）; above $r^*$, they cascade into consensus（类 T-Soc-4 的 S 形传播曲线，参见 10% Rule）.

### Ax-Soc-3: Operator Entanglement (算子纠缠)
<!-- ORIGINAL-SECTION-PRESERVED -->
Extended interaction couples the $\theta$ parameters of multiple agents.

**正向定义**：长期互动产生耦合参数张量：
$$\theta_{AB} = \theta_A \otimes \theta_B + \Delta\theta_{coupling}(\Psi_f^{cross}(A,B), \tau_{interaction})$$
其中 $\Delta\theta_{coupling}$ 是由跨算子摩擦 $\Psi_f^{cross}(A,B)$ 和互动时长 $\tau_{interaction}$ 驱动的非线性耦合修正项（不可约化为各自独立参数的张量积 $\theta_A \otimes \theta_B$）。

$$\theta_{AB} \neq \theta_A \otimes \theta_B \quad (\text{注：原⊕应为⊗，张量积而非直和})$$

耦合强度代理指标：$\|\Delta\theta_{coupling}\| \propto \int_0^T \Psi_f^{cross}(A,B,t)\,dt$（积累的跨算子摩擦历史）。

*   **悲伤的 SRT 形式化**：失去亲人 = 强制解耦事件。当 $\theta_{AB}$ 被迫分解（$B$ 算子消亡，$\theta_B \to \emptyset$），原有耦合修正项 $\Delta\theta_{coupling}$ 突然失去锚点，算子 A 的参数空间急剧收缩：
    $$\left.\frac{d\Psi_f^A}{dt}\right|_{decoupling} \gg 0 \quad \text{（急剧 } \Psi_f \text{ 尖峰，对应情感高唤起/高 A 值）}$$
    悲伤的持续时间 ∝ $\|\Delta\theta_{coupling}\|$（耦合深度），逐渐重建独立参数 $\theta_A' \leftarrow \theta_{AB} - \Delta\theta_{coupling}$ 的过程 = 哀悼。

---

## III. Cognitive Dynamics (认知动力学)
<!-- ORIGINAL-SECTION-PRESERVED -->

### Ax-Cog-1: Decoupling Transition (解耦相变)
<!-- ORIGINAL-SECTION-PRESERVED -->
Cognition emerges when $\hat{G}$ inserts a delay between Input and Output for simulation.
$$ \text{Cognition} \equiv \Delta t_{delay} > 0 \implies \text{Simulation}(L_0) $$
*   **Reflex**: $\Delta t \to 0$ ($d \approx 0$).

### Ax-Cog-2: Observer-Environment Integration (OEI)
<!-- ORIGINAL-SECTION-PRESERVED -->
The boundary between Self and World is variable.
$$ \text{OEI} = 1 - \frac{I(\hat{G}; \text{Env})}{H(\hat{G}) + H(\text{Env})} $$
*   **Flow State**: Low OEI (High Integration).

<br>

---

# SRT Philosophy V: Social Cognition & Reality Dynamics (Hybrid Edition)
<!-- ORIGINAL-SECTION-PRESERVED -->
> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Social Dynamics (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


# Part B: Expanded Theoretical Discourse (Context) (扩展理论论述)

> **Note**: The following sections provide the detailed analysis of Social Cognition, Depression, and Reality Construction.

## 1. The Standard Hard Problem: The Paralysis of Action

### 1.1 Why Can't We Act Sometimes?
In cognitive science, there is a mysterious transformation between **Intention** and **Action**.

*   **Arendt**: Action is natality (birth), it is a miracle—the capacity to initiate something genuinely new.
*   **Pathology**: In depression, this transformation fails. The patient fully knows they "should" get out of bed, fully "wants" to get out of bed, but the body remains locked as if encased in concrete.
*   **Traditional Explanations**: Weak willpower? Dopamine deficiency?

These explanations miss the core mechanism.

---

## 2. SRT Resolution & Necessity

### 2.1 Advantage: The Physics of Action
SRT treats action as **release of $L_0$ potential energy**.

*   **Mechanism**: Every action is a micro-creation from $L_0$ to $L_1$. This requires consuming free energy to overcome **ontological inertia**.
*   **Depression Model**: Depression is **not** lack of "will" but **pathological amplification of the friction coefficient** ($w_F$). For a depressed person, the perceived energy cost of pouring a glass of water equals a normal person running a marathon. This is **computational energy bankruptcy**.

**SRT Formula**:
$$ P_{action} = \alpha \cdot \text{Reward} - \beta_{depressed} \cdot \text{Cost} $$

When $\beta_{depressed} \gg \beta_{normal}$, even trivial actions have prohibitive energy barriers.

---

### 2.2 Gibson's Affordance: Relational Ontology
James Gibson's **Affordance Theory** receives precise mathematical expression in SRT.

*   **Core**: The world is not composed of objects but of **action possibilities**.
*   **Perception = Action**: I don't see "a chair"—I see "sit-on-ability." I don't see "a cliff"—I see "danger of falling." Perception directly maps to $\theta$-parameter space.

**SRT Formalization**:
$$ A(\hat{G}, E) = \hat{G}_\theta[L_0] \cap E_{obj} $$

Affordance emerges at the **intersection** of environmental structure and embodied capacity. Change either variable → affordance transforms or vanishes.

**Chemero patch (2026-03-07, Pipeline 1):**
- 区分 **Affordance**（环境-身体可行性）与 **Invitation**（当下被门控并被注意到的动作候选）。
- “直接知觉”在 SRT 中被表达为：行动采样（转头、接近、探索）本身生成用于下一步知觉的信息，因此无需先验表征推理链。
- 对“属性 vs 关系”争议，SRT 采用可兼容立场：对象侧可建模为处置性潜能，算子侧通过 \(\theta\) 与情境张量将其实现为关系可达域。
- 社会与联合可供性由算子耦合涌现，解释多人任务与制度化协作为何可打开个体不可达路径。

**Wellman patch (2026-03-07, Pipeline 1):**
- 引入“信念滞后治理”：社会预测不是读取现实本身，而是读取他者在其信息边界内形成的信念位形。
- 将假信念任务解释为算子从 \(W\)-中心映射向 \(B_j\)-中心映射的相变，属于发展期的结构重排而非偶发失误。
- 将 DD→DB/KA→FB→HE 的发展序列视为 \(L_2\) 社会语义协议的分层收敛，不同文化序列差异可由交互语料（knowing vs thinking）权重解释。

**Comparative Language–ToM Neuroanatomy patch (2026-03-24, Pipeline 1):**
- 这条 patch 最值得留下的，不是“人类会语言、会心智理论”这类常识句，而是把跨代文化传递的神经负担收紧成两条可比较的长程通路。它同时修正了“单一区域暴涨就能解释语言与读心”的模块神话，也加固了 SRT 对文化传递带宽必须由符号封装与自他模拟共同托住的判断。
- 用户提交的讲稿材料，最值得吸收的增量，不是泛泛重复“人类会语言、会心智理论”，而是把 **cumulative culture 的两个候选神经专化窗口** 收紧到了比较灵长类可对照的结构层：其一是人类 **arcuate fasciculus** 不只连接 Broca–Wernicke 经典区，还显著向腹外侧颞叶（STS / MTG / ITG）扩展；其二是灵长类虽共享 proto-default-mode network，但人类可能具有更强的 **medial prefrontal ↔ posterior cingulate / precuneus** 长程耦合，并在静息态额外招募左侧语言区邻域。
- 若按 SRT 语言收紧，这支持一个比“大脑更大所以会说话/读心”更细的写法：人类优势更像来自 **用于社会传递的双通路增厚**，而不是单一模块暴涨。前颞-额叶弓状束扩展，增强了把对象、词汇、语义与句法结构稳定打包进 `L_2^{language}` 的能力；DMN 长程耦合增强，则提高了系统在离线状态下维持 self-model / other-model / belief-lag simulation 的能力。
- 可把“可累积文化传输带宽”写成一个结构化窗口，而非单点脑区神话：
\[
\mathcal{B}_{cum\text{-}culture}
\;\propto\;
\mathrm{Conn}\!\big(\text{Broca},\ \text{lateral temporal semantics}\big)
\cdot
\mathrm{Conn}\!\big(\text{mPFC},\ \text{PCC/precuneus}\big)
\]
其中前者更接近 **符号封装 / lexical-semantic-syntactic stabilization**，后者更接近 **心智视角维持 / 自他叙事模拟**。这也解释了为什么语言与 theory of mind 往往在文化演化中一起出现为“互相增益的脚手架”，而不是彼此孤立的天赋。
- 对 SRT 来说，这条材料最自然的吸收方式，是把它当作一个 **comparative language–ToM transmission window**：文化累积能力不只是 `L_2` 内容越来越多，而是支撑 `L_2` 生成与跨代对齐的神经通路，出现了更强的长程整合与更明显的功能侧化。于是，“教别人我看到什么/你以为我知道什么”这类高阶社会传递，才会在同一物种里变成低摩擦、可递归、可叠加的稳定操作。更具体地说，这条 patch 不是在新增一个“语言区定位故事”，而是在加固 SRT 里“文化可累积性依赖低摩擦传递脚手架”这条线。
- **Boundary（中文）**：
  - 这是一份讲稿式综合材料，不是单篇新论文；更适合作为 comparative interface，而不是硬实验定论。
  - 当前较稳的是“人类在 arcuate ventral projection 与 DMN 长程耦合上更强”，而不是“已找到语言或 ToM 的唯一中枢”。
  - DTI tractography、FDG-PET 与跨物种 rs-fMRI 比较都有方法边界；不能把连接强弱直接等同为单一认知能力的充分原因。
  - 黑猩猩与 macaque 并非“完全没有”这些网络，而是更像拥有较弱、较少外扩的前体版本；因此该窗口支持的是 **degree / topology specialization**，不是绝对有无二分。

**Sanborn patch (2026-03-07, Pipeline 1):**
- 在不确定推断中引入 MCMC 近似：算子不维持全后验，而沿局部提案链进行序列采样。
- 采样相关性导致“看似不稳定”的逐次判断轨迹；该轨迹可统一解释概率判断波动、双稳知觉切换与部分锚定效应。
- 与 SRT 的摩擦记账兼容：样本预算不足时，系统以偏差换取算力可支付性（\(\Psi_f\)-budgeted inference）。

**Wu patch (2026-03-07, Pipeline 1):**
- 将注意力定义为“为响应而进行的目标选择”（select-for-response），统一视觉、听觉、记忆与推理中的注意现象。
- 形式化 top-down / bottom-up / historical 三类偏置在同一 priority map 中的竞争求解，连接 Buridan 式选择困境与神经竞争消解。
- 区分“注意力是资源/机制”与“注意力依赖资源/由机制实现”的层级：SRT 采用实现论立场，避免把资源或机制直接等同于注意力本体。

**Porot & Mandelbaum（LoTH）patch (2026-03-08, Pipeline 1):**
- 引入“思维语言（LoT）作为中层表征协议”接口：将高阶推理中的**离散成分、组合语法、角色-填充项独立性**映射为 SRT 的可计算约束层（主要位于 \(L_2\) 协议层，受 \(\hat G_\theta\) 门控）。
- 将 LoTH 的 **productivity / systematicity** 解释为“有限原子概念 + 可重复组合规则”在有限算力下的近似可扩展性，而非无限计算承诺；对应 SRT 的 \(\Psi_f\)-budgeted inference。
- 将逻辑算子（not/if-then/or）与“自动结构敏感转移（inferential promiscuity）”视为可检验信号：当结构转移可在低意识控制下稳定出现时，支持语言样式推理并可与 System 1 兼容。
- 采用“多 LoT 并存”立场：不同认知子系统/物种可能具不同语法与原子集，避免把单一人类成人语法外推为本体论唯一底层。
- 与连接主义关系采取实现层区分：神经网络可作为实现机制，但若缺少稳定的符号角色分离与可组合语法，其可解释性仍不足以替代 LoT 层描述。

**Griffiths（Bayesian Models of Cognition）patch (2026-03-08, Pipeline 1):**
- 引入“贝叶斯推断作为 \(\hat G_\theta\) 的规范更新层”：在归纳不完备问题中，以
\[
P(h\mid d)\propto P(d\mid h)P(h)
\]
刻画从先验到后验的选择更新，将 SRT 的选择动力学与可计算归纳规则对齐。
- 将 **prior** 显式对应为 SRT 的历史/结构偏置（\(L_2\) 协议沉积、任务经验与先天约束），将 **likelihood** 对应为当前证据对候选结构的解释力；两者乘性耦合映射到 \(\Psi_f\)-预算下的可支付推断。
- 将“结构学习”（因果图、逻辑规则、语法）纳入 SRT 的多层表征学习：在有限样本下，系统通过先验偏置与生成模型联合约束，避免把“学到结构”误写为“纯统计记忆”。
- 接受资源理性（resource-rational）桥接：行为偏差（如概率匹配、保守更新）可由近似采样/变分策略解释，不等同于系统性非理性；与既有 MCMC patch 保持一致。
- 与连接主义保持互补分层：Bayesian 模型给出计算层目标，神经网络/连接主义提供算法与实现层近似；二者不是互斥替代关系。

---

## 3. Mechanism Derivation: From Hysteresis to Entanglement

### 3.1 Reality Hysteresis
Why is changing a belief so much harder than forming one?

> [R→Festinger 1957 *A Theory of Cognitive Dissonance*（不一致信息引发认知失调→主动回避而非更新）; Nickerson 1998 *Review of General Psychology*（确认偏见综述：已有信念偏向性处理证据）; Lord et al. 1979 *JPSP*（先入为主立场使人对同等证据做出相反评估）; Kuhn 1962 *The Structure of Scientific Revolutions*（范式转移需要势垒跨越，而非累积证据）]

**R/H 区分**：
- [R] 确认偏见（Nickerson 1998）；认知失调减少（Festinger 1957）；热力学势能阱的物理概念（迟滞：磁性材料/相变）
- [H] **SRT形式化**：ΔE_change = ΔE_evidence + ΔE_barrier 中的 ΔE_barrier = L₂势能阱深度（由重复选择历史决定）；这将社会心理学的"确认偏见"重表述为SRT的势能阱动力学，并与§1.4的 ΔE∝Hardness×(κ-κ_c2) 联结

*   **SRT Analysis**: $L_2$ is a **potential well** carved by repeated selection. Once you fall into the well (adopt a belief), jumping out requires not just new evidence but **additional energy to overcome the barrier**.

**Thermodynamic Analogy**:
$$ \Delta E_{change} = \Delta E_{evidence} + \Delta E_{barrier} $$

**ΔE_barrier操作化候选**：
- 信念强度量表（certainty rating）× 重复强化历史（信念持续时间 × 社会确认频率）
- 联结§1.4 κ参数：ΔE_barrier ≈ Hardness(L₂) × (κ - κ_c2)（当κ>κ_c2时，势垒高度与距相变距离正比）

*   **Social Implication**: This is why people don't easily admit mistakes even when confronted with iron-clad evidence. This is **not** stupidity—it's a **physical mechanism for maintaining system stability** ($L_2$ Stability).

**可证伪预测**：
- FC-Hysteresis-1：高信念强度（certainty rating高）+长持续时间的信念，其更新所需的反证证据数量应显著多于低强度/短持续信念——若与ΔE_barrier预测（∝强度×持续）不相关则势垒公式量化预测失败
- FC-Hysteresis-2：在范式转移背景下（Kuhn），已处于旧范式中更长时间的科学家承认新范式所需的时间应更长（迟滞效应随"势阱深度"增加）——若无时间相关则SRT迟滞机制与科学实践脱节

---

### 3.2 Operator Entanglement & Grief
When we love someone, our $\theta$ parameters become **entangled** with theirs ($\theta_{other}$). Our self-boundary ($L_1$) expands to include them.

*   **Grief Mechanism**: When a loved one dies, this is not merely the disappearance of an external object but **a violent tearing of the self-parameter tensor**.
*   **SRT Corollary**: Grief pain is **phantom limb pain**. Our $\theta$ still attempts to connect to a node in $L_0$ that no longer exists, generating infinite prediction error ($\Psi_f \to \infty$).

**Mathematical Form**:
$$ \theta_{self+other}(t) \xrightarrow{\text{death}} \theta_{self}(t+\Delta t) $$
$$ \Psi_f = \|\theta_{self+other} - \theta_{self}\|^2 \to \infty $$

The magnitude of grief is proportional to the degree of entanglement that existed.

---

### 3.3 Ontological Nucleation: Why New Ideas Need Critical Mass
Why do social movements fail below a certain size but explode above it?

**SRT Analysis**: New social realities face **nucleation barriers** identical to physical phase transitions (like water droplets forming in clouds).

$$ r^* = \frac{2\sigma_{surf}}{\Delta g_{vol}} $$

*   **Below critical radius $r^*$**: The new idea-cluster dissolves back into the dominant $L_2$ (surface tension overwhelms volume gain).
*   **Above $r^*$**: The cluster becomes self-sustaining and catalyzes cascading consensus.

**Historical Examples**:
- Civil Rights Movement: Needed critical mass of key nodes (Rosa Parks, MLK) + network topology (churches, buses) to overcome $r^*$.
- Failed uprisings: Subcritical—crushed by $L_2$ immune response before reaching $r^*$.

---

## 4. Costs & Risks

### 4.1 The Decoupling Risk: Anxiety as the Price of Cognition
As humans developed advanced cognition (System 2), we gained the ability to **simulate futures offline**. This means $\hat{G}$ temporarily decouples from $L_0$.

*   **Risk**: This decoupling is a double-edged sword. It brings creativity but also **anxiety**. Animals live in the present ($L_1$)—no anxiety. Humans live in countless catastrophic simulated futures ($L_1^{sim}$)—this is the ontological root of anxiety.

**SRT Insight**: Anxiety is the $\Psi_f$ generated by maintaining multiple incompatible $L_1^{sim}$ threads simultaneously. The system is paying energetic costs for realities that **haven't happened and may never happen**.

---

### 4.2 Pharmaceutical Limitations in Treating Depression
Antidepressants modulate neurotransmitters to lower $w_F$ (friction coefficient).

*   **SRT Warning**: But this **only lowers the action threshold**—it doesn't provide **the reason to act** ($L_1^{future}$ meaning). If you give medication without meaning, the patient may regain motor capacity... and use it to commit suicide.

**True Healing Requires**:
1. Lower $w_F$ → Medication (restore energetic accessibility)
2. Rebuild $L_1^{future}$ → Meaning therapy (existential/narrative reconstruction)

---

## 5. Falsifiable Predictions

### 5.1 Prediction: Depression & Physical Friction Perception
**Prediction**: Ask depressed patients to estimate the steepness of physical slopes in front of them. SRT predicts they will **systematically overestimate** slope steepness, and this overestimation correlates with their action retardation severity ($w_F$ parameter).

*   **Neural Mechanism**: Anterior Cingulate Cortex (ACC) encoding of Expected Effort Cost shows gain bias in depression.

**Falsification**: If depressed patients show no bias in physical effort estimation → SRT's $\Psi_f$ pathology model is falsified.

---

### 5.2 Prediction: Grief as Phantom Limb Effect
**Prediction**: In fMRI, recently bereaved individuals viewing the deceased partner's name should show activation in **somatosensory cortex** (body boundary perception regions) similar to amputees—i.e., "missing body part" signals.

*   **Mechanism**: The brain is attempting to reconnect to an entangled $\theta_{other}$ node that has been torn away.

**Falsification**: If bereaved individuals show no somatosensory activation patterns distinct from general sadness → SRT's entanglement model is falsified.

---

## 6. SRT Reinterpretations: Cognitive Science Classics

### 6.1 Gibson's Affordance Theory
**Classical Version**: Affordances are environmental properties that invite action.
**SRT Precision**: 
$$ A = E \cap \theta \neq \text{property of } E \text{ alone} $$

Affordances are **not** "in the object" nor "in the mind" but at their **intersection**. A staircase affords climbing to a human but not to a wheelchair user—same object, different $\theta$, different affordance.

---

### 6.2 Arendt's Natality (Action as Beginning)
**Arendt**: Action is the human capacity to initiate the radically new.
**SRT Translation**: 
$$ \text{Natality} = \hat{G}_\theta[L_0^{novel}] \to L_1^{unprecedented} $$

Action is **not** deterministic output (that's mere behavior) but the collapse of **unexplored regions of $L_0$** into novel $L_1$ configurations. This requires high $d$-value (willingness to explore far from current $L_2$ grooves).

---

### 6.3 System 1 vs System 2 (Kahneman)
**Classical Dual-Process Theory**: Fast automatic vs. Slow deliberative.
**SRT Energetics**: 

| System | SRT Mechanism | Energy Profile |
|:-------|:--------------|:---------------|
| System 1 | $L_2$-dominated automatic selection | Low $\Psi_f$ (downhill in potential landscape) |
| System 2 | Explicit $L_0$ exploration | High $\Psi_f$ (uphill search for new basins) |

System 1 = sliding down existing $L_2$ grooves (cheap).
System 2 = climbing out to search $L_0$ (expensive).

---

## 7. Deep Implications: The Social Construction of Reality

### 7.1 Berger & Luckmann's Triadic Process
**Classical Stages**:
1. Externalization: Humans project ideas into the world
2. Objectivation: Projections become "objective" social facts
3. Internalization: New generations accept these "facts" as given reality

**SRT Formalization**:

| Stage | SRT Mapping | Formal Expression |
|:------|:------------|:------------------|
| Externalization | $L_1$ selection expressed | $\sigma^{\theta}_{L_1} \to$ behavior/symbols |
| Objectivation | $L_1 \to L_2$ stabilization | Multiple $\theta$'s converge → $L_2$ structure |
| Internalization | $L_2$ constrains new $\hat{G}_\theta$ | New agents' $\theta$ shaped by existing $L_2$ |

**Social Reality**:
$$ L_2^{social} = \lim_{t \to \infty} \bigcap_{\theta \in \Theta(t)} \text{stable}(\hat{G}_\theta[\sigma]) $$

Social reality is the **convergence of all members' selections over time**.

---

### 7.2 The Pathology of Epistemic Bubbles vs. Echo Chambers

**Critical Distinction** (2024 Update):

| Phenomenon | Definition | SRT Mechanism | Escape Difficulty |
|:-----------|:-----------|:--------------|:------------------|
| **Epistemic Bubble** | Unintentional exclusion of relevant information | $\theta$'s environmental bias | Medium |
| **Echo Chamber** | Active rejection and denigration of dissent | $L_2$ immune response to foreign $L_1$ | Extremely High |

**Formalization**:
$$ \text{Bubble}: P(\text{Info}|\theta) \neq P(\text{Info}|\text{Reality}) $$
$$ \text{Echo Chamber}: P(\text{Accept Dissent}|\theta) \approx 0 \land \text{Trust}(\text{Outgroup}) \to 0 $$

**SRT Analysis**: Echo chambers are **high-$d$ value degeneration**. To preserve $L_2$ purity, the operator actively severs external $L_0$ connections → system becomes **brittle** (fragile to perturbation).

**Therapy Difference**:
- **Bubble**: Introduce new information (puncture the bubble).
- **Echo Chamber**: New information triggers immune attack. Must **rebuild trust chains** first (relationship before information).

---

## 8. Listening as Inverse Selection

### 8.1 The Ontology of Listening
Traditional selection is active "pruning." But there exists a special operator state: **Listening**.

**Definition**: Listening is the state where $\hat{G}_\theta$'s inhibition function is temporarily suspended, allowing $L_0$ information flow to pass with minimal distortion.

$$ \text{Listening} \implies \min(H(L_1 | L_0)) $$

I.e., minimize the conditional entropy of $L_1$ given $L_0$—or maximize mutual information between them. This is the highest form of selection: **letting existence reveal itself**.

**Listening vs. Pruning**:

| Mode | $\hat{G}_\theta$ State | $L_0 \to L_1$ Relation | Phenomenology |
|:-----|:----------------------|:-----------------------|:--------------|
| Pruning | Active inhibition | High filtering | Control, certainty |
| Listening | Suspended inhibition | Low filtering | Reception, openness |

**Indigenous Wisdom**: Tiokasin Ghosthorse's emphasis on "listening to the earth" is **not** poetic rhetoric but describes a specific $\hat{G}_\theta$ operational mode—suspending noun-based categorization, allowing $L_0$'s processual information to directly manifest.

---

## 9. Summary: The Embodied Mind in Social Space

SRT dissolves the artificial boundary between individual cognition and social reality:

1. **Affordance**: Reality is the intersection $L_0 \cap \theta$—neither purely objective nor purely subjective.
2. **Pathology**: Depression, grief, anxiety are not "mental illnesses" but **physical friction states** in the $L_0 \to L_1$ selection process.
3. **Social Construction**: Collective $L_2$ emerges from iterated individual selections—society is a **convergent attractor** of distributed $\hat{G}_\theta$ operations.
4. **Hysteresis**: Beliefs resist change due to thermodynamic stability, not cognitive stubbornness.
5. **Entanglement**: Love is topological boundary dissolution—two $\theta$'s becoming one tensor.

**Final Insight**: The self is not a fixed entity but a **dynamic pattern of selection** embedded in a social field of other operators. "I" am the intersection of my $\theta$-parameters and the $L_2$ structures my community has crystallized around me.

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。  
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。  
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。

## 极限补偿协议（Extreme Compensation Protocol）补注（2026-03-06）

### Def-Soc-ECP-1: Anti-Collapse Compensation Protocol
当观察者在高 \(d\) 共情耦合下持续暴露于“不可即时修复的高 \(\Psi_f\)”场景，系统为避免认知崩塌会构建递延补偿型 \(L_2\) 叙事：
\[
\text{ECP activates} \iff d_{obs}\uparrow\ \land\ \Psi_f^{witness}\gg \Psi_f^{coping}
\]
\[
L_2^{comp} = \arg\min_{\mathcal N}\Big(\Psi_f^{meaning-collapse}(\mathcal N)\Big)
\]
其中 \(\mathcal N\) 为补偿叙事族（如终极正义、来世平账、历史终局修复）。

### T-Soc-ECP-1: Deferred Ledger Effect
补偿叙事通过扩展时间边界 \(t\to\infty\) 降低当前意义崩塌风险，但会引入远期可检验性折扣。

## 【理论边界/防误用声明】
- 不采纳“补偿叙事存在 = 其对象已被经验验证”的推论。
- 不采纳“拒绝补偿叙事 = 更高理性”的推论（两者都可能失衡）。
- 适用边界：ECP 被定义为认知稳定机制，不是形而上学真值裁定器。

### [Lineage/Source]
- 神学-进化-动物苦难对话语境（2026）


## Identity Beyond Representation Interface（2026-03-07）

### Def-Soc-IRM-1: Ontological Misidentification
定义“本体论错认”为：算子将动态选择过程身份（\(\hat G_\theta\)）错误锚定为静态表征对象（\(L_2^{identity}\)）。
\[
\text{MisID} \iff \hat G_\theta \equiv L_2^{identity}
\]

### Eq-Soc-IRM-1: Identification Deviation Potential
当错认发生时，引入苦难势能：
\[
E_{suffering} \propto d\cdot\left\|\hat G_\theta[L_0]-L_2^{identity}\right\|\cdot\Psi_f^{maint}
\]
解释：关切越深（\(d\) 越高）、活体验与身份模板偏差越大、维持模板成本越高，则存在性痛苦越强。

### T-Soc-IRM-1: Insight–Liberation Timescale Asymmetry
“认知顿悟”是快变量；“身份惯性卸载”是慢变量积分过程。故有：
\[
\Delta t_{insight} \ll \tau_{disengage}
\]
并需满足历史势能耗散下界：
\[
\int_{t_0}^{t_1}\left\|\frac{d\theta}{dt}\right|dt\ \ge\ \eta\int_{t_0}^{t_1}\left|L_2^{history}(t)\right|dt
\]
对应实践含义：一次看破可启动相变，但无法替代长期去绑定训练。

### Def-Soc-IRM-2: Sovereign Representation Principle
SRT 不采纳“反表征主义极端化”。健康态不是摧毁 \(L_2\)，而是保持“表征主权”：
\[
\text{Healthy} \iff L_2\ \text{available as tool} \land \neg\big(\hat G_\theta\leftarrow L_2\text{-captured}\big)
\]

### 分类映射表（Identity Modes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 动态过程认同（process-identification） | 中~高 | Open / Semi-open | payable |
| 温和角色认同（flexible L2 identity） | 中 | Semi-open | payable~borderline |
| 刚性概念认同（rigid representation lock） | 中回落 | Closed 倾向 | borderline~overloaded |
| 身份防御极化（violent/arrogant lock-in） | 低~中（高反应低反思） | Closed | overloaded / unsustainable |

### [Lineage/Source]
- Essentia Foundation（Steven Pashko, 2026）: *Consciousness without counterpart: Identity beyond representation*。
- 现象学语境与“表征鸿沟”讨论，映射到 SRT 的 \(L_0/L_1/L_2\) 与 \(\Psi_f\) 记号。

## 【理论边界/防误用声明】
1. 不采纳“\(L_2\) 全部无效或必然有害”的推论；\(L_2\) 仍是协作与文明压缩的必要层。  
2. 不采纳“只要顿悟一次即可永久解脱”的推论；SRT 明确要求慢变量去绑定过程。  
3. 不采纳“拒绝身份标签 = 拒绝伦理责任”的推论；责任归属仍需制度与情境联合建模。


## Cultural Lenses & Care Interface（2026-03-12）

### Def-Soc-CLC-1: Cultural-Lens Apperception Gate
个体情绪并非仅由内部生理波动直接给出，而是在文化协议参与下被分类、命名并体验：
\[
L_1^{affect}(t)=\hat G_{\theta,L_2^{culture}}\!\big[L_0^{intero}(t)\oplus L_0^{social}(t)\big]
\]
其中 \(L_0^{intero}\) 表示内感受与生理调节信号，\(L_0^{social}\) 表示公共事件、他人表情与社会氛围；\(L_2^{culture}\) 提供语言、价值、习惯与可接受反应模板。

### T-Soc-CLC-1: Top-Down Goes All the Way Down
若文化镜片改变，则知觉分类、情绪命名与“何者看似自然”会同步改变：
\[
\Delta L_2^{culture}\neq 0
\Rightarrow
\Delta \Pi_{apperception}\neq 0
\Rightarrow
\Delta E_{felt}\neq 0
\]
这意味着文化不是外加解释层，而会下沉到感知与情绪习惯本身。Boas 的“alternating sounds”例子可被读为：连“听见什么”都受先前分类模式影响，更遑论愤怒、羞耻、骄傲或关怀的正当对象。

### Def-Soc-CLC-2: Collective-Care Modulation
“我何时以一个‘我们’的方式去关切”可被写成个体关切与集体门控的耦合：
\[
\mathrm{Care}_i(t)=\mathcal C\big(L_0^{intero,i},L_0^{social},L_2^{culture},A_{joint}\big)
\]
其中 \(A_{joint}\) 为共享注意强度。共享注意与情绪强度上升时，个体体验更易进入集体情绪区，但并不必然坍缩为盲目群体心智。

### T-Soc-CLC-2: Crowd Capture vs Reflexive Public
同样的集体情绪可进入两种不同相位：
\[
\text{Crowd-capture}\iff A_{joint}\uparrow \land \mathcal M_{lens}\downarrow
\]
\[
\text{Reflexive public}\iff A_{joint}\uparrow \land \mathcal M_{lens}\uparrow
\]
其中 \(\mathcal M_{lens}\) 表示算子对”自己正戴着何种文化镜片”的元觉察能力。前者更接近 Le Bon 式感染与被领袖挟持，后者更接近 Boas 式的反思性公共关切：我参与”我们”，但不把”我们”的惯例直接误当自然本体。

> **[R]** 群体感染经典理论：Le Bon 1895 *The Crowd: A Study of the Popular Mind*（群体感染与领袖挟持机制）；Boas 1909 *Psychological Problems in Anthropology*（文化镜片对感知-情绪的渗透）；Turner et al. 1987 *Rediscovering the Social Group: A Self-Categorization Theory*（自我分类条件下的去个人化）；Frith & Frith 2012 *Trends in Cognitive Sciences*（社会元认知的神经基础）。**[H]** 以下 A_joint × M_lens 双因子相位区分（群体捕获 vs 反思性公共）及对 SRT 选择框架的接驳（θ被L₂锁定 vs L₂→L₁反身通道保持开放）为本框架新增贡献。
>
> **M_lens 操作化候选**：
> - 行为层：元认知问卷（Metacognitive Awareness Inventory, MAI；或 Perspective-Taking Scale）的文化归因分量表得分。
> - 神经层：错误相关负波（ERN）振幅 + 前额叶-后顶叶连接（元认知监控回路），或自我参照处理中 vmPFC 活动的文化归因条件下的调制量。
> - 生态层：在社会事件描述中自发使用”从…视角看”类元语言频率（文本分析代理）。
>
> **精度边界**：⟺ 在此为描述性双向特征，而非严格数学等价——低 A_joint 时 M_lens↓ 亦可产生小规模 Crowd-capture（如封闭邪教），高 A_joint 下 M_lens↑ 的实现依赖教育水平、多元接触史等先决条件。命题成立范围：在中-高 A_joint 的广场/网络公共事件中，M_lens 是决定相位走向的关键调制变量，但并非唯一变量。
>
> * **FC-CLC2-1**（证伪条件）：若在控制情绪强度（A_joint 代理）后，高 M_lens 组（MAI 上四分位）与低 M_lens 组在集体行为激进度（如群体攻击性事件率）之间无显著差异（p>0.05），则 M_lens 的相位分叉作用需重新检视或归入情绪强度的伴随变量。
> * **FC-CLC2-2**（证伪条件）：若同一群体在 M_lens 高水平下通过集体元认知讨论显著降低了 Crowd-capture 事件频率（如参与审议民主项目后的前后比较），则命题中 M_lens 的因果贡献方向得到支持；若效应消失则需将 M_lens 视为结果而非原因。

### 分类映射表（Collective Emotion Regimes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 群体感染 / crowd capture | 低~中（高反应低反思） | Closed 倾向 | overloaded / manipulable |
| 共享仪式性凝聚 / collective effervescence | 中 | Open↔Semi-open | payable |
| 反思性公共关切 / reflexive public care | 中~高 | Open | payable / plural-stable |
| 社媒放大回路 / visceral feedback loop | 中回落 | Semi-open→Closed | borderline~overloaded |

### [Lineage/Source]
- Noga Arikha, *Who am I when I care? Emotion through the lens of Franz Boas*, Aeon (2026).
- Franz Boas, *Psychological Problems in Anthropology* (1909).
- Franz Boas, *On Alternating Sounds* (1899).
- Victor Chung, Rocco Mennella, Elisabeth Pacherie, Julie Grèzes, *Social bonding through shared experiences: the role of emotional intensity*, Royal Society Open Science 11:240048 (2024).

## 【理论边界/防误用声明】
1. 不采纳“文化完全决定情绪，因此生理普遍性可忽略”的推论；本节明确保留共享内感受/生理底盘。
2. 不采纳“所有集体情绪都是群体病理”的推论；共享注意与情绪强度也可产生 prosocial bonding。
3. 不采纳“意识到自己有文化镜片 = 可以彻底脱离镜片”的推论；SRT 只主张部分反身化与治理可能性，而非无条件超越。


## Second-Person Schizophrenia Interface（2026-03-13）

### Def-Soc-SPS-1: Reciprocal-Contact Disambiguation
第二人称互动并不是”检测到某个外物”即可成立，而要求算子在具身回馈中分辨”他者正在响应我”与”我只是碰到了可扰动物体”：
\[
L_1^{other}(t)=\hat G_{\theta}^{social}\!\big[L_0^{haptic}(t)\oplus R_{reciprocal}(t)\oplus A_{joint}(t)\big]-\mathcal D_{distractor}(t)
\]

> **符号说明**：此处 $\oplus$ 表示**多模态输入特征拼接**（concatenation），即将触觉 $L_0$、互反馈信号 $R_{reciprocal}$、联合行动信号 $A_{joint}$ 合并为 $\hat{G}_\theta^{social}$ 的复合输入——非直和（direct sum）；与 Ax-Soc-3 中算子纠缠使用的 $\otimes$（张量积）明确区分。$\mathcal{D}_{distractor}(t)$ 作用在 $L_1$ 投影**之后**（注意力过滤在已显现内容中减除干扰），而非 $L_0$ 输入层前处理。

其中：
- $R_{reciprocal}(t)$：对方回馈与自身动作之间的**时序耦合**；操作化测量 = 自身动作信号与触觉反馈的互相关峰值时延（perceptual crossing 范式中通常 $\Delta\tau_{cross} < 300\,\text{ms}$ 为显著互反馈阈值）
- $A_{joint}(t)$：联合行动信号（双方共享注意对象或协调运动的时序同步度）
- $\mathcal D_{distractor}(t)$：同场干扰物（非他者产生的可扰动信号）
- **与 Ax-Soc-3 的连接**：$R_{reciprocal}$ 是双人算子纠缠项 $\Delta\theta_{coupling}(\Psi_f^{cross}, \tau)$ 的**操作化代理**——当 $R_{reciprocal}$ 高于偶发阈值时，两个算子的耦合项 $\Delta\theta_{coupling}$ 从零激活（SRT-SOC-COG Ax-Soc-3）

`perceptual crossing` 范式的价值，在于把”感到对方在那儿”操作化为一个可控的互动区分任务。

### T-Soc-SPS-1: Social-Uncertainty Amplification Window
当系统难以判定当前触觉反馈是否由他者共同调制时，第二人称通道的摩擦会快速上升：
\[
\mathcal U_{social}\uparrow \Rightarrow \Psi_f^{second-person}\uparrow \Rightarrow P(\text{misperceive other})\uparrow
\]
对精神分裂症语境，SRT 不把问题写成“完全缺失社会能力”，而写成“在高不确定互动中，对 reciprocal affordance 的区分成本、误差积累与恢复速度可能发生系统偏移”。

### C-Soc-SPS-1: Feasibility-First Pathology Clause
该研究的 pilot 结果显示，患者与对照都能够完成任务，且初步模式大体与既有 perceptual crossing 文献一致。因此更稳妥的 SRT 结论是：
\[
\text{Schizophrenia}\not\Rightarrow \neg A_{joint}
\]
\[
\text{Schizophrenia}\Rightarrow \Delta \tau_{disambiguation}\ \lor\ \Delta \sigma_{\epsilon}^{social}\ \lor\ \Delta \Psi_f^{second-person}
\]
也就是说，病理窗口更可能落在“互动误差治理参数的重配”，而不是“第二人称世界整体关闭”。

### T-Soc-SPS-2: Social Psychiatry as Coordination Dynamics

若精神分裂症的部分残障来自互动中的误差与不确定性治理失衡（→ 见 C-Soc-SPS-1），则实验重点不应只停留在离线 mindreading 测试，而应转向实时协调动力学：
\[
\mathcal M_{psychiatry}^{social}:\ \text{offline attribution} \rightarrow \text{online coordination dynamics}
\]

驱动机制：SRT 将该转向形式化为对具身门控失衡的捕获——

**门控错配（Gating Mismatch）**：当 $\hat{G}_\theta$ 在 reciprocal coupling 中的误差累积率 $\lambda_{err}(\theta)$ 与恢复时间常数 $\tau_{rec}(\theta)$ 的乘积超过临界值时，第二人称通道的协调即告失效（误差发散）：
\[
\text{Gating Mismatch} \equiv \lambda_{err}(\theta) \cdot \tau_{rec}(\theta) > 1
\quad \text{in online reciprocal coupling}
\]

这与 SRT 交互通道的本体论摩擦排序一致：
\[
\Psi_f^{embodied\text{-}resonance} < \Psi_f^{second\text{-}person} < \Psi_f^{inferential\text{-}L2}
\]
越接近真实 reciprocal coupling 的任务，越能激活低摩擦通道，越能客观地看见社交病理并非纯概念缺陷（$L_2$ 缺失），而是具身协调中的门控参数漂移。

### [Lineage/Source]
- Leonardo Zapata-Fonseca, Aisha Belhadi, Ruben Fossion, Thomas Fuchs, Ani Grigoryan, Shannon Hayashi, Iwin Leenen, Tom Froese, *(Mis)perceiving others: toward a second-person science of schizophrenia*, *Cognitive Systems Research* 96 (2026), DOI:`10.1016/j.cogsys.2026.101458`.
- OpenAlex / Crossref 元数据与摘要：该文为同行评审正式论文，在线发布日期为 `2026-03-09`；摘要强调 `perceptual crossing`、social haptics、7 名 schizophrenia 患者 pilot、以及“error / uncertainty in social interaction dynamics”的后续假设。

## 【理论边界/防误用声明】
1. 不采纳“7 人 pilot study 已足以确证精神分裂症社会机制”的推论；当前更适合作为 feasibility window 与实验接口，而非定论。
2. 不采纳“精神分裂症可被还原为单一 second-person deficit”的推论；妄想、幻觉、药物、异质性与长期病程仍需并行建模。
3. 不采纳“虚拟触觉 avatar 范式即可替代自然社会生活”的推论；该任务只是高可控的 interaction assay，而非全部现实社交。
