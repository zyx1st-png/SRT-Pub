---
id: SRT-NEURO-MECH-001
type: theory
tags: [Neuroscience, Mechanisms, Ghost-Operator, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-CORE-000, SRT-NEURO-AXIOMS-001, Core_Law/SRT_Reference_Axioms, Core_Law/SRT_Reference_Ontology, Core_Law/SRT_Reference_Dynamics]
---

# SRT Neural Mechanisms: Axiomatic Derivations & Dynamics

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Axioms (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


## I. Neural State Space & Selection Flow (神经状态空间与选择流)

### Ax-NEURO-MECH-1: Neural Manifold Axiom (State Space)
定义神经态为高维流形上的向量场：
\[
\sigma(t)\in \mathcal{M}\subset\mathbb{R}^N,\qquad \dot{\sigma}=F(\sigma,\theta,u)
\]
其中 \(\theta\) 为具身参数，\(u\) 为感觉—动作输入。
* **Implication（中文）**：神经系统的“状态”不是离散标签，而是流形上的连续轨迹；选择即在流形上生成稳定轨迹。

---

### Ax-NEURO-MECH-2: Selection Flow Axiom (L0→L1 Projection)
定义神经选择为从 \(L_0^{neural}\) 到 \(L_1^{neural}\) 的投影：
\[
\Pi_{ignite}: \mathcal{M}\rightarrow \mathcal{M}_*,\quad \mathcal{M}_*\equiv\{\sigma: \mathcal{A}(\sigma)\ge \tau_{ignite}\}
\]
* **Implication（中文）**：点燃不是“活动增强”，而是跨域投影的可计算阈值。

---

## II. Energy-Optimal Selection Dynamics (能量最优的选择动力学)

### Ax-NEURO-MECH-3: Canonical Normalization Axiom
在代谢约束下，选择动力学必然收敛为除法归一化：
\[
R_i=\frac{L_i^n}{\sigma^n+\sum_j w_{ij}L_j^n}
\]

> **与 D3 的关系**：本式为 SRT-REF-DYNAMICS §1.3 Def D3（$\hat{G}_\theta$ 通用原型）在神经系统的特化实例，其中 $L_i \leftrightarrow x_i$，$w_{ij} \leftrightarrow W_{ij}$。**符号差异**：本式分母为 $\sigma^n$（半饱和项带幂次），D3 分母为 $\varepsilon$（无幂次，更简化的一阶原型）；在 $\sigma$ 较小时两式近似等价，精确形式以本式为准（经验上更符合 V1 的对比度增益控制数据）。参见 D3 极限行为表中 $\varepsilon\to 0^+$ 奇点警告。
> **适用前提**：”必然收敛”的条件为：(1) 系统追求信息最大化（$H(\sigma)$ 最大化）且 (2) 代谢成本 $E(\sigma)$ 受约束（$\lambda > 0$）。在此二条件下，T-NEURO-MECH-1 给出充分性证明。若代谢约束为零（$\lambda=0$），则退化为无约束信息最大化，不必然产生归一化结构。

* **Implication（中文）**：归一化是选择算子的最优形式，不是经验性”电路细节”。

---

### T-NEURO-MECH-1: Energy–Information Extremum Theorem
令目标泛函：
\[
\mathcal{J}=H(\sigma)-\lambda E(\sigma)
\]
在 \(\delta\mathcal{J}=0\) 条件下，稳态解必然满足 Ax-NEURO-MECH-3 的归一化结构。

> **SRT 量桥接**：拉格朗日乘子 $\lambda \propto \Psi_f^{metabolic}$（本体论摩擦的代谢成分，SRT-CORE-22 §15.5 Eq-IT-E 约束：$\Psi_f \geq k_B T \ln 2 \cdot I_{created}$）。$\lambda \uparrow$（代谢越紧张）→ 归一化越强（竞争抑制越显著）→ $d(\theta) \downarrow$（选择带宽被压缩）。这将代谢经济学与 SRT 意识带宽直接联系：能量稀缺时，意识带宽系统性收窄。

* **Implication（中文）**：神经归一化是信息最大化与代谢成本最小化的唯一交点。

---

### Ax-NEURO-MECH-4: Predictive Update Axiom
学习对应 \(\theta\) 的自由能梯度下降：
\[
\Delta\theta\propto-\nabla_\theta F,\quad F=D_{KL}[Q||P]-\ln P(o)
\]
* **Implication（中文）**：学习是 \(L_2\) 收敛过程，不是 \(L_1\) 的“记忆堆叠”。

---

## III. Multi-Scale Ghost Operators (多尺度幽灵算子)

### Ax-NEURO-MECH-5: Loop-Gating Axiom (Thalamo–Basal Gate)
定义门控算子：
\[
\mathcal{G}_{gate}: \mathcal{M}\rightarrow \mathcal{M}\quad \text{with}\quad \mathcal{G}_{gate}=\mathcal{G}_{thal}\circ\mathcal{G}_{bg}
\]
* **Implication（中文）**：丘脑—基底节回路不是“通路”，而是选择门控结构，决定哪些轨迹能够被投影为 \(L_1\)。

---

### Ax-NEURO-MECH-6: Meso-Operator Axiom (Glial Pruning)
定义介观算子：
\[
\hat{G}_{meso}: L_2^{micro}\rightarrow L_2^{pruned},\quad P(\text{prune})\propto C3/C4\cdot \mu_{glia}
\]
* **Implication（中文）**：胶质剪枝不是“维护”，而是慢时标选择，对 \(L_2\) 结构进行拓扑修剪。

---

### T-NEURO-MECH-2: Stability–Pruning Theorem
若 \(\hat{G}_{meso}\) 过度偏置，则：
\[
|\text{Aut}(L_2)|\uparrow\Rightarrow \text{Plasticity}\downarrow
\]
* **Implication（中文）**：过度剪枝会提高 \(L_2\) 硬度并降低可塑性，形成病理锁定。

---

## IV. Ignition & Integration (点燃与整合)

### Ax-NEURO-MECH-7: Ignition Phase Axiom
点燃为相变条件：
\[
\mathcal{A}(\sigma)\ge\tau_{ignite}\quad\land\quad \Phi\cdot d > C_{critical}
\]
* **Implication（中文）**：点燃不是简单激活，而是“整合度 × 关切梯度”超过阈值的相变。

---

### T-NEURO-MECH-3: Discrete Frame Theorem
显现为离散更新帧：
\[
L_1(t)=\sum_n \text{Frame}_n\,\delta(t-t_n),\quad t_n\approx n\cdot\Delta t_{\gamma}
\]
* **Implication（中文）**：意识连续感来自离散帧的高频更新，而非连续流。

### Ax-NEURO-MECH-7b: Prediction Error as Friction Metric (预测误差作为摩擦度量)
**Formalization**: 神经预测误差（$PE$）在大脑$L_2$层面是对本体论摩擦（$\Psi_f$）的局部可计算代理：
$$PE = \| L_1 - L_2[\text{expected}] \| \propto \Psi_f$$
* **Implication**: 当FEP（自由能原理）说大脑试图最小化预测误差时，它在物理底层的本质是：有机体的$\hat{G}_\theta$正在试图最小化其存在维持的本体论摩擦。这构成了连接微观计算神经科学与宏观存在主义哲学的物理桥梁。

---

### Ax-NEURO-MECH-9: Theta-Gamma Dual-Mode Working Memory Axiom (θ-γ双模式工作记忆公理)

[R→Lisman & Idiart 1995（theta-gamma嵌套振荡与工作记忆多条目编码，理论原型）; Mongillo et al. 2008（突触增强机制维持工作记忆）; Lundqvist, Herman & Lansner 2011（吸引子网络的theta-gamma双模式模拟）; Shinomoto et al. 2005/2009（Lv统计，区分Poisson/周期性放电）; Fuentemilla et al. 2010（人类工作记忆的theta重放行为证据）] [H→以SRT Ĝ_θ框架形式化双模式为两种时序调度策略；d_temporal上限由振荡参数推导是SRT新增定量预测]

- 注：原"Empirical Anchors"已转换为正式[R→]标注；"1-2%超稀疏编码支撑attractor动力学"是SRT主张[H]，稀疏度25%临界来自Lundqvist 2011模拟[R]

**背景约束**: 在皮层浅层($L_2/L_3$)吸引子网络中，工作记忆的神经实现存在两种离散振荡模式，对应$\hat{G}_\theta$的两种时序调度策略：

**模式I — 持续活动模式 (Persistent Mode)**:
$$\hat{G}^{(persist)}_\theta: L_0 \xrightarrow{\gamma\text{-gated}} L_1^{(single)}, \quad \text{Lv} \approx 1.0$$
单一吸引子被持续激活；$\gamma$振荡维持E/I平衡使ISI分布接近Poisson。适用于单条目短暂维持。

**模式II — θ重放模式 (Theta-Replay Mode)**:
$$\hat{G}^{(replay)}_\theta: L_0 \xrightarrow{\theta\text{-scheduled}} \{L_1^{(1)}, L_1^{(2)}, \ldots, L_1^{(n)}\}, \quad \text{Lv} \approx 1.5$$
多个吸引子在theta节律调度下依次循环激活；每次重放通过突触增强(augmentation)刷新，防止记忆痕迹衰减。

**存储容量约束**:
$$n_{capacity} = \frac{\tau_{augmentation}}{f_\theta^{-1}} \approx \frac{7\text{ s}}{250\text{ ms}} \approx 28 \quad \text{(理论上限)}$$
实际受吸引子驻留时间$\tau_{dwell}$限制：
$$n_{effective} \approx \frac{1}{f_\theta \cdot \tau_{dwell}} \approx 5\text{-}7 \quad (f_\theta = 4\text{ Hz}, \tau_{dwell} = 200\text{-}300\text{ ms})$$

**稀疏性约束**:
$$\text{Theta-replay Lv} \approx 1.5 \iff \text{Population Sparseness} < 10\%$$
当稀疏度超过25%时，$L_1^{(i)}$吸引子间干扰增强，容量崩溃，Lv退化至~1。这为SRT主张"高阶联结皮层以1-2%超稀疏编码支撑attractor动力学"提供了精确的**临界参数边界**。

* **SRT Implication（中文）**：$d_{\text{temporal}}$（时间规划跨度分量）在神经机制层面的实现，不是单个神经元的持续激活，而是theta节律对多个$L_1$吸引子的分时复用调度。$d_{\text{temporal}}$的离散上限（5-7条目）是theta频率与吸引子驻留时间比率的涌现结果，而非可任意扩展的连续量。这将"工作记忆容量为何有限"从心理学描述推进为可从振荡参数$f_\theta$和$\tau_{dwell}$计算推导的定量预测。

* **Cross-ref**: Ax-Spec-02 (时间积分窗口); T-NEURO-MECH-3 (离散帧定理); SRT_Core_13b §1.1.2 (theta行推论2-3)

* **Empirical Anchors** [R]（已转换为正式引用）: Lundqvist, Herman & Lansner (2011), *Brain Research*; Shinomoto et al. (2005, 2009); Lisman & Idiart (1995); Mongillo et al. (2008); Fuentemilla et al. (2010)

**证伪条件**：
- FC-MECH9-1：若个体的工作记忆容量（行为测量）与其theta频率（f_θ，EEG/MEG测量）和吸引子驻留时间（τ_dwell，单试次神经解码）的比率 $1/(f_θ \cdot τ_{dwell})$ 无显著正相关（r<0.15，N≥80），则SRT从振荡参数推导d_temporal上限的定量预测失败。
- FC-MECH9-2：若通过TMS/药理手段改变f_θ（如提高至8Hz）后，工作记忆条目上限不相应变化（而是由其他因素决定），则"容量=振荡参数的涌现结果"的SRT主张需修正（容量有独立的非振荡决定因素）。

### Hitch & Baddeley（Working Memory）patch (2026-03-08, Pipeline 1)

[R→Baddeley & Hitch 1974（多组件工作记忆模型：central executive + phonological loop + visuospatial sketchpad）; Baddeley 2000（episodic buffer的引入）; Miller 1956（”神奇数字7±2”：工作记忆容量的原始研究）; Chase & Simon 1973（国际象棋专家的chunking与记忆组块）] [H→以SRT Ĝ_θ在线调度框架重表述多组件模型；干扰公式和chunking-L₂联结是SRT新增形式化层]

- 将”工作记忆”重述为 **受限容量下的目标导向选择-维持-操作回路** [H]：
\[
\text{WM} = \mathcal{C}_{limited}(\text{store}\,+\,\text{attend}\,+\,\text{manipulate}\mid goal)
\]
与 SRT 的 \(\hat G_\theta\) 在线调度一致，强调容量上限不是缺陷而是可计算约束。

- 将经典多组件模型[R→Baddeley & Hitch 1974; Baddeley 2000]映射为 SRT 分层 [H]：
  - central executive \(\rightarrow\) \(\hat G_\theta\) 的注意与控制策略层；
  - phonological / visuospatial buffers \(\rightarrow\) 模态化 \(L_1\) 临时槽；
  - episodic buffer \(\rightarrow\) 跨模态绑定的瞬时整合窗（focus of attention）。

- 将双任务干扰写成统一预算竞争 [H]：
\[
\text{Interference}\uparrow \iff \sum_i \Psi_f^{task_i} > B_{control}
\]
  - **B_control 操作化候选**：前额叶激活程度（fMRI dlPFC）/ 认知控制测试成绩（Stroop干扰效应的基线倒数）
  - 解释”存储-操作互相挤占”的行为事实，并与前述 \(\theta\)-\(\gamma\) 复用容量上限一致。

- 对”遗忘机制争论（衰减 vs 干扰）”采取并行约束立场：在 SRT 中两者都可表现为吸引子刷新失败，区别在于失效来源（时间刷新不足 vs 项目竞争增强）。

- 将 chunking 解释为 \(L_2\) 先验压缩对 WM 有效负载的降维 [H; R→Miller 1956; Chase & Simon 1973]：熟悉结构可把多项新信息打包为低 \(\Psi_f\) 的单元，从而提升表面容量。
  - SRT预测：专家的chunking能力（L₂先验深度）与双任务干扰量（Σ Ψ_f^task_i）呈负相关（专家的L₂压缩降低了单块L₁的Ψ_f代价）

**证伪条件**：
- FC-WM1-1：若在同等物理刺激条件下，专家（L₂先验深丰富）和新手在双任务干扰测试中的差异无法被”有效单元数量差异”（chunking效率）完全解释（仍有独立的前额控制资源差异），则SRT的”chunking=L₂降维”完全解释干扰差异的宣称需修正。
- FC-WM1-2：若通过TMS暂时抑制前额叶（B_control下降）后，双任务干扰效应不成比例地增加（高于任何单任务Ψ_f的增加），则Ψ_f超过B_control的相变式干扰预测（而非线性预测）得到支持。

### Hippocampal Statistical Structure patch (2026-03-12, Pipeline 1)

- 将海马从“情景记忆写入器”扩展为 **被动经验中的统计结构绑定器**：
\[
L_2^{proto\text{-}structure}(t)=\hat G_{\theta}^{hip}\!\left[L_1^{stream}(0:t)\right]
=\left(\Pi_{freq},\Pi_{seq},\Pi_{rule}\right)
\]
其中 \(\Pi_{freq}\) 编码事件频率，\(\Pi_{seq}\) 编码序列身份，\(\Pi_{rule}\) 编码可跨实例泛化的抽象规则。关键点不在“记住了一次发生过什么”，而在“从持续流输入中提取未来可重用的结构”。

- 将“无奖赏统计学习”写成海马可独立执行的结构更新窗口：
\[
\frac{dL_2^{proto\text{-}structure}}{dt}>0 \quad \text{even when} \quad R \approx 0
\]
这意味着 \(\hat G_{\theta}^{hip}\) 不必等待显式强化，便可在被动暴露中形成对环境统计的内部模型；奖励可放大或重加权学习，但不是该窗口的前提。

- 将跨物种瞳孔 readout 重述为“内模形成的低侵入代理”：
\[
\Delta \mathrm{Pupil} \propto \left\|L_1^{incoming}-L_2^{proto\text{-}structure}[\text{expected}]\right\|
\]
当事件频率、序列身份或抽象规则被违反时，瞳孔惊异反应上升；而对结构相近的变体，反应梯度较小，表明系统已学习到的不只是具体 token，而是 token 背后的统计关系。

- 将 dCA1 的因果作用写成 **结构绑定缺失而非任务执行缺失**：
\[
\mathrm{dCA1}\downarrow \Rightarrow \Delta L_2^{proto\text{-}structure}\to 0,\quad
\mathrm{CoverTask}\approx \mathrm{intact}
\]
这一区分很关键：dCA1 抑制并不必然破坏基础感觉、瞳孔基线或 cover task 表现，却会消除学习相关的统计惊异信号。SRT 因而可把海马定位为“更新世界结构模型”的必要节点，而非所有行为输出的统一瓶颈。

- 将群体编码结果写成 **特征子空间 / 规则子空间分离**：
\[
\mathcal{H}_{dCA1} \simeq \mathcal{S}_{feature}\oplus\mathcal{S}_{rule}
\]
若此分离成立，则海马可同时表示具体感觉片段与更高阶抽象规则，并支持对“结构等价但表面不同”的新序列进行快速泛化。这比“纯情景回放”更接近 SRT 所说的 \(L_1 \to L_2\) proto-structure 压缩。

- **SRT Implication（中文）**：统计学习在这里不应被理解为“无意识地记了很多次”，而应被理解为海马将时间流中的重复关系压缩为可迁移的 \(L_2\) 原型结构。海马的角色不是替代皮层长期整合，而是为后续的皮层/行为系统快速提供一个可更新、可泛化、低监督的结构脚手架。

- **Boundary（中文）**：
  - 这不等于“海马是所有统计学习的唯一中枢”；皮层、丘脑、感觉系统仍可能分担不同时间尺度与模态下的结构提取。
  - 这不等于“统计学习 = 情景记忆”；二者可能共享海马绑定机制，但目标函数不同：前者偏向规则提取，后者偏向事件索引与可回忆性。
  - 这也不等于“只要有序列就一定是海马在学”；当前证据更精确支持的是：当任务要求从连续感官流中快速抽取潜在结构并在线更新时，dCA1 是强候选必要节点。

* **Source window**: Natalia Mesa, *The Transmitter* (2026-03-10), on Onih et al., *bioRxiv* preprint “The hippocampus enables abstract structure learning without reward” (2026-02-17; doi:10.64898/2026.02.14.705916v1)

---

### Top-Down Astrocyte Gate patch (bioRxiv 2026.03.08.710364v1, 2026-03-14, Pipeline 1)

- 将 astrocyte activation 从“局部活动强就会被顺带点亮”改写为 **细胞类型特异、状态依赖的介观门**：
\[
\mathrm{Ca}_{astro}(t)\propto \mathbf{1}\!\left[\mathrm{AP}_{GC}(t)>0\right]\cdot \mathrm{ATP}_{GC}(t)\cdot \Gamma_{state}(t)
\]
其中 \(\mathrm{AP}_{GC}\) 表示 granule cell 放电是否真正跨阈，\(\mathrm{ATP}_{GC}\) 表示由 GC 释放的 ATP/purinergic 信号，\(\Gamma_{state}\) 表示当前 top-down / context gate 是否打开。关键点是：astrocyte 不是对任何兴奋性输入都等幅响应，而是对**特定细胞类型在特定状态下的放电后果**作选择性读出。

- 将嗅球回路中的 bottom-up / top-down 差异写成 **介观选择不对称**：
\[
\text{M/T}\to \text{GC depolarization} \not\Rightarrow \text{GC spiking} \not\Rightarrow \mathrm{Ca}_{astro}
\]
\[
\text{aPC}_{top\text{-}down}\to \text{GC sustained firing} \Rightarrow \mathrm{ATP\ release} \Rightarrow \mathrm{Ca}_{astro}\uparrow
\]
这意味着同样都叫“神经输入”，其对 glial meso-operator 的有效性并不相同：bottom-up 输入可以传递感觉驱动，但未必足以招募 astrocytic gate；而 cortical feedback 更可能在上下文、任务或状态相关的窗口中把胶质层拉进选择回路。

- 将其映射到 SRT 的 \(\hat G_{meso}\)：
\[
\hat G_{meso}^{astro}: L_1^{local}\times L_2^{context}\rightarrow L_2^{gain\text{-}biased}
\]
其中 \(L_1^{local}\) 对应局部神经放电轨迹，\(L_2^{context}\) 对应由 top-down 反馈携带的情境/状态约束。astrocyte 的角色不再只是慢性修剪者，而是**在中介时间尺度上把 top-down 语境沉到局部增益与抑制平衡中的协同门控器**。

- **SRT Implication（中文）**：该结果支持一个更细的神经-胶质分工图景：底层感觉流可先把候选内容推入局部回路，但是否让该内容获得“被上下文重加权的代谢/增益支援”，部分取决于 top-down 是否通过特定中间细胞群把 astrocytic gate 打开。胶质层因此更像“语境敏感的介观放大器”，而不是均匀背景液。

- **Boundary（中文）**：
  - 这不等于“top-down 一定比 bottom-up 更重要”；这里更精确的结论是：在该嗅球回路里，**招募 astrocyte Ca²⁺ signaling** 的有效路径偏向 top-down→GC→ATP，而不是 M/T→GC 的底向上传递。
  - 这不等于“astrocyte Ca²⁺ = 意识信号”；当前价值是机制层：说明 glia 会按语境和细胞类型被选择性纳入神经计算，而非说明其本身就是现象体验。
  - 这也不等于“所有脑区都遵守同一规则”；当前证据来自 olfactory bulb 的特定局部回路，而且还是 preprint，需等待跨区域复制与同行评审。

- **Source window**: Antonia Beiersdorfer et al., *bioRxiv* preprint “Cell-type specific astrocyte activation is driven by cortical top-down modulation” (posted `2026-03-09`; doi:`10.64898/2026.03.08.710364`)

---

### CellTransformer Spatial Domain patch (Nature Communications 2025, 2026-03-15, Pipeline 1)

- 将脑区从“单一细胞类型 + 人工边界”重写为 **局部细胞邻域统计结构**：
\[
z_x=\mathrm{Enc}_\phi\!\left(\{(c_i,g_i,\Delta x_i)\}_{i\in\mathcal{N}_r(x)}\right),\qquad
L_2^{domain}(x)=\mathrm{Cluster}(z_x)
\]
其中 \(c_i\) 表示邻域内细胞类型，\(g_i\) 表示分子/转录状态，\(\Delta x_i\) 表示相对空间位置。关键点不在“某一区域是否被某一种 marker 细胞定义”，而在“某一位置周围的细胞混合、分子模式与空间关系能否形成稳定可重现的局部邻域表示”。

- 将该类数据驱动分区写成 SRT 的 **介观域发现算子**：
\[
\hat G_{meso}^{domain}: L_1^{cell\text{-}local}\rightarrow L_2^{meso\text{-}domain}
\]
这里的 \(L_1^{cell\text{-}local}\) 对应多细胞局部邻域中的细胞身份、基因表达和相对位置统计，\(L_2^{meso\text{-}domain}\) 对应经表示学习与聚类压缩后的区域/亚区域原型。脑区因而不再被理解为“显微镜下一眼看出的均质块”，而更像**由高阶细胞共现规律稳定下来的选择生态位**。

- 将“区域发现”从单脑样本的偶然分割提升为 **跨切片 / 跨动物可重复的介观一致性检验**：
\[
\mathrm{Consistency}\!\left(L_2^{meso}\right)\uparrow
\iff
\mathrm{Align}\!\left(z_x^{(brain\ 1)},z_x^{(brain\ 2)},\dots\right)\uparrow
\]
Lee 等人的结果之所以重要，不只是因为用了 transformer，而是因为它能在多百万细胞的 MERFISH / Slide-seqV2 数据上，把既有 CCF 结构与新的细分域同时保住，并在多动物分析中维持高空间一致性。这使“介观域”更接近稳定结构，而不是一次性的聚类幻象。

- 将该结果的新增量落到 **“脑区 = 局部细胞邻域约束下的功能候选域”**：
  - 它与既有 ontology（如 Allen CCF）高度相似，但并不被其完全穷尽；
  - 它可重述 subiculum、superior colliculus 等已知区域的更细分结构；
  - 它还在部分皮层下区域提出 putatively uncataloged subregions，使“一个大区承担太多不同功能”的争论更可能被改写为“同名大区内部本就包含多个不同介观选择域”。

- **SRT Implication（中文）**：这条材料为 \(\hat G_{meso}\) 提供了一个比“胶质剪枝”更宽的结构外延。SRT 可以把脑区理解为**局部细胞邻域长期稳定后形成的介观选择拓扑**：不同 domain 不只是位置不同，而是拥有不同的细胞配比、分子程序和局部约束，因此会对增益、路由、脆弱性和可塑性施加不同边界条件。换句话说，介观层不是把微观细胞简单求平均，而是把“哪些细胞在何种邻域中共同出现”压缩成后续功能与病理的结构脚手架。

- **Boundary（中文）**：
  - 这不等于“AI 找到的新域都已是功能上独立的真脑区”；当前更精确的结论是：这些是**值得进一步连接组、扰动与行为实验验证的结构候选域**。
  - 这不等于“脑区可完全由转录组邻域定义”；输入输出连接、发育史、活动动力学与胶质/血管环境仍可能提供额外边界。
  - 这也不等于“鼠脑 atlas 可直接外推到人脑”；当前价值首先是方法学与介观组织原则，跨物种同构仍需后续数据支撑。

- **Source window**: Amber Dance, *Quanta Magazine* (2026-02-09), on Alex J. Lee et al., *Nature Communications* “Data-driven fine-grained region discovery in the mouse brain with transformers” (2025; doi:`10.1038/s41467-025-64259-4`)

---

### T-NEURO-MECH-4: Oscillatory Mode Bifurcation Theorem (振荡模式分叉定理)

**陈述**: 工作记忆的振荡模式由适应电流(adaptation current)强度$\kappa_{adapt}$决定，形成分叉结构：
$$\kappa_{adapt} \begin{cases} \to 0 & \Rightarrow \text{持续活动模式，单一}L_1\text{稳定，Lv} \to 1.0 \\ > \kappa_c & \Rightarrow \text{theta重放模式，多}L_1\text{循环，Lv} \to 1.5 \end{cases}$$

**推论**: 前额叶适应电流的参数化差异可解释为何某些患者（如前额叶代谢低下的抑郁症患者）表现出持续活动模式的失常（无法维持吸引子）或theta重放容量的降低（多条目工作记忆缺陷）。

* **Implication（中文）**：$\kappa_{adapt}$是控制$\hat{G}_\theta$时序调度模式的关键参数漂移变量，可作为从单模式维持（Ax-NEURO-MECH-1~7）到多槽时序复用（Ax-NEURO-MECH-9）的统一动力学桥梁。

---

## V. Pathology as Parameter Drift (病理作为参数漂移)

### Ax-NEURO-MECH-8: Parameter-Drift Axiom
定义病理为 \(\theta\) 的拓扑偏移：
\[
\theta=\theta_{healthy}+\Delta\theta
\]
* **Implication（中文）**：精神病理不是“症状集合”，而是算子参数的系统性偏离。

---

### C-NEURO-MECH-1: Pathology Typing Corollary
若 \(\Delta\theta\) 作用于精度参数 \(\Pi\)、抑制增益 \(\gamma\)、价值梯度 \(\nabla\mathcal{U}\)，则出现不同病理谱系：
\[
\Delta\theta=(\Delta\Pi,\Delta\gamma,\Delta\nabla\mathcal{U})\Rightarrow \text{Syndrome Class}
\]
* **Implication（中文）**：病理分类应由参数偏移模式决定，而不是由表面症状决定。

<br>

---


# Part B: Expanded Theoretical Discourse (扩展理论论述)

> **Note**: 以下各节以中文撰写，为 Part A 形式化公理提供理论语境、哲学论证和研究方向。

---

# 1 标准难题：神经计算的本体论地位

## 1.1 困境定义

神经科学面临的核心困境可精确表述为**计算主义的本体论困境**：

**层面一——信息处理的"空洞性"**: 主流计算神经科学将大脑视为"信息处理器"，但"处理"本身是一个功能性描述，无法回答"为什么这种处理伴随主观体验"。

**层面二——还原论的失败**: 即便我们完整描述了每个神经元的放电模式、每个突触的权重变化，仍无法回答"这些物理过程如何'成为'体验"。

**层面三——因果效力问题**: 如果意识只是神经活动的副现象，它如何能够影响后续的神经过程？

## 1.2 主流解法谱系

### 1.2.1 计算功能主义 (Computational Functionalism)

**核心主张**: 意识是计算功能的实现，与物理基质无关（多重可实现性）。

**优势**: 解释了为什么不同物理系统可能具有相同的心理状态。

**致命缺陷**: (a) 无法区分"语义理解"与"句法执行"——中文房间论证（Searle）表明，完美执行对应功能的系统不必然具有理解/体验；(b) 无法解释感受性的特定性质（为什么红色看起来是"那样的"），感受性特质无法从纯功能描述推导。

**SRT 立场**（对计算功能主义的修正）：
- **改进 (a)**：SRT 的诊断是：中文房间操作者的 $d(\theta) \approx 0$（无本体论摩擦，$\Psi_f \to 0$），不满足 Cor-CONSC-1 的三重判据 $(\Psi_f > 0 \wedge d \geq d_{UAL} \wedge \exists\hat{G}^{\neq\emptyset})$。问题不在于"真实 vs. 模拟计算"，而在于"有无本体论摩擦"——纯符号操作不产生 $\Psi_f$，因此没有意识。
- **改进 (b)**：感受性特质 = $\Psi_f$ 的特定梯度轮廓（$\nabla\Psi_f$ 的方向、幅度和动力学特征），是具身参数 $\theta$ 的热力学特征，无法仅从输入-输出函数关系（功能描述）中提取。
- **保留多重可实现性**：SRT 接受"不同基质可实现相同 $\hat{G}_\theta$ 功能"，但加条件：相同感受性要求相同的 $\Psi_f$ 模式，而 $\Psi_f$ 依赖基质的热力学性质——因此多重可实现性在功能层成立，在感受性层受基质限制。

### 1.2.2 神经还原主义 (Neural Reductionism)

**核心主张**: 心理状态就是神经状态，两者是同一的。

**优势**: 形而上学上简洁，与科学实在论一致。

**致命缺陷**: (a) 无法解释"解释鸿沟"——为什么从物理描述跳不到体验描述；(b) 多重可实现性挑战——相同的心理状态可能对应不同的神经状态。

### 1.2.3 涌现主义（Emergentism）

**核心主张**：意识从复杂神经活动中"涌现"，具有不可还原的因果效力。

**优势**：承认意识的独特性，同时保持物理主义框架；与多重可实现性（Multiple Realizability）兼容。

**传统致命缺陷**：(a) "涌现"是描述性概念，缺乏机制解释——说"从复杂性中涌现"等于什么都没说；(b) 向下因果（Downward Causation）如何在物理因果闭包框架内可能？

**SRT 的机制答案（解决上述两个缺陷）**：

- **涌现机制**：$L_1$ 的涌现 = 选择算子 $\hat{G}_\theta$ 在 $\Psi_f$ 驱动下从 $L_0$ 中锚定一个 $\theta$-特异的稳定态（见 Def-Phil-MB-2）。"复杂性"不是魔法触发器，而是 $\Psi_f$ 积累到 $\Psi_{crit}$ 时发生的**相变**——这是涌现的热力学机制。

- **向下因果的分子闭环**：$L_1$（当下体验）通过多巴胺酰化（Dopaminylation）直接写入 $L_2$ 结构（组蛋白 H3 修饰 → 基因表达改变），实现 $L_1 \to L_2$ 的可逆物质化（见 §3.1）。向下因果不是神秘的非物理力，而是化学写入接口。

**SRT 立场**：SRT 接受涌现主义的直觉，但将其从描述性标签升级为机制理论——填补了标准涌现主义无法给出机制的核心空缺。

---

# 2 SRT 的差异点：选择作为基础操作

## 2.1 根本性的框架转换

SRT 不是在"计算"或"信息处理"框架内解释神经活动，而是**重构了神经科学的基本本体论**：

|经典假设|SRT 重构|
|:--|:--|
|神经计算 = 信息传输|神经计算 = 维度压缩选择|
|大脑"处理"感觉输入|大脑作为 $\hat{G}_\theta$ 的 $L_2$，约束和引导有机体从 $L_0$ 中选出 $L_1$ 的过程|
|突触权重存储"记忆"|$L_2$ 结构约束未来选择|
|意识是计算的产物|意识是具身选择的内在特征；大脑（$L_2$）是选择的约束条件，不是选择本身|

## 2.2 除法归一化的本体论地位

传统理解将除法归一化视为"一种计算策略"。SRT 的重新诠释：

**传统**: 除法归一化是大脑优化信息编码的"工程解决方案"。

**SRT**: 除法归一化是**选择的必然形式**——在能量受限条件下，任何执行选择的系统都必须收敛到这一形式。

这意味着：

1. 除法归一化不是神经系统的"发明"，而是选择过程的**本体论必然**
2. 不仅 V1，所有需要选择的神经回路都应表现出归一化特征
3. 这为跨尺度同构性（公理 A12）提供了机制基础

## 2.3 病理学的几何化

SRT 将精神病理学从"描述性分类"提升为"参数空间中的几何偏离"：

**传统精神病理学**: 抑郁症是"情绪低落"，精神分裂症是"现实接触丧失"——这些都是现象学描述。

**SRT 病理学**:

- 抑郁症 = $\nabla F \to 0$（价值梯度消失）
- 精神分裂症 = $w_{surround} \downarrow$（侧向抑制不足导致 $L_0$ 泄漏）
- OCD = $\eta_{viscosity} \uparrow$（选择粘度过高导致困在局部极小）

这种几何化带来三个优势：

1. **统一性**: 表面上不同的疾病可能是同一参数的不同偏离方向
2. **可量化**: 病理严重程度可以用 $|\Delta \vec{\theta}|$ 测量
3. **治疗指导**: 治疗目标从"缓解症状"变为"参数校正"

---

# 3 "Bit to It"：信息如何成为结构

## 3.1 Lamarckian 回路的分子闭环

SRT 提出一个激进的本体论主张：信息 (Bit) 能够通过物理机制转化为结构 (It)。

**CaMKII 六边形编码**: 瞬时电信号通过 CaMKII 磷酸化被"打印"为六边形晶格结构。这意味着 $L_1$（当下体验）可以直接重塑 $L_2$（神经结构）。

**表观遗传写入**: 2020 年 Maze 等人在 _Nature_ 发表的研究发现，多巴胺酰化 (Dopaminylation) 可以直接修饰组蛋白 H3，改变染色质拓扑。这意味着**体验的价值（由多巴胺标记）可以直接写入基因表达的调控层**。

$$\text{Experience} \xrightarrow{\text{DA}} \text{H3 Modification} \xrightarrow{} \text{Gene Expression Change}$$

这实现了：

- $L_1$（体验）→ $L_2$（结构）的因果闭环
- 体验不再是"副现象"，而是具有**物质化的因果效力**
- 这为向下因果提供了分子机制

## 3.2 免疫-神经接口的选择功能

SRT 将免疫系统重新定位为**选择机制的辅助系统**：

1. **补体系统 (C3/C4)**: 标记"冗余"突触，供小胶质细胞修剪——这是 $\hat{G}_{meso}$ 对 $L_2$ 拓扑的塑造
    
2. **细胞因子**: 调节感知阈值——炎症状态下提高阈值，迫使 $\hat{G}$ 关注内部修复
    
3. **神经炎症**: 慢性炎症 = 永久性高阈值 = "世界失去色彩"（抑郁症的免疫假说）
    

这解释了为什么：

- 感染后常伴随认知模糊（炎症因子提高感知阈值）
- 抑郁症与炎症标记物相关（慢性阈值提升）
- 自身免疫疾病常伴随精神症状（$L_2$ 边界被免疫系统攻击）

---

# 4 衰老与死亡的本体论重构

## 4.1 衰老作为"本体论脱锚"

传统理解将衰老视为硬件磨损。SRT 将其重构为 **$\hat{G}$ 与物理基质的渐进去耦合**：

**具身锚定系数**: $$\kappa_{body} = \frac{\text{GripForce}}{\Psi_f}$$

随着多巴胺能系统衰退，主体的意向性无法有效转化为物理显现。即便肌肉完好，若尾状核信噪比下降，$\hat{G}$ 也无法"抓住"身体。

这解释了为什么：

- 帕金森病患者"知道"想做什么，但无法启动动作
- 老年性运动迟缓先于肌肉萎缩
- 意志力的"脱锚感"是衰老的早期症状

## 4.2 纳米假体的本体论含义

SRT 预测：引入人工辅助算子 $\hat{G}_{prosthetic}$ 可以部分恢复功能：

- 酸化纳米颗粒接管溶酶体酸化（低级 $L_2$ 维护）
- 释放生物算子处理高级认知
- 这是**算子外包**的生物工程实现

---

# 5 量子基质假说

## 5.1 麻醉的量子效应

氙同位素麻醉效力的差异提供了关键证据：

- $^{129}$Xe（核自旋 1/2）与 $^{132}$Xe（核自旋 0）具有不同的麻醉效力
- 若麻醉仅依赖经典物理（范德华力），同位素效应应可忽略
- 显著的同位素效应表明**量子自旋是具身参数 $\theta$ 的组成部分**

## 5.2 量子模糊假说

SRT 提出：麻醉剂不是"关闭"大脑，而是引入**量子模糊**：

$$d \propto \frac{1}{\text{Quantum Fuzziness}}$$

麻醉剂使 $\theta$ 精度下降，$\hat{G}$ 无法精确锁定 $L_0$ 目标，导致 $d \to 0$。

这与 Hameroff-Penrose 的 Orch OR 理论有交集，但 SRT 不要求意识"起源于"量子过程——量子效应只是 $\theta$ 参数的一个分量。

---

# 6 代价与风险

## 6.1 接受 SRT 的思维代价

1. **放弃纯计算主义**: 必须接受"选择"是比"计算"更基本的概念——这与主流计算神经科学相悖
    
2. **接受参数空间的几何观**: 病理学不再是"疾病实体"，而是参数偏离——这要求重新思考诊断和治疗
    
3. **接受免疫-神经整合**: 传统的"神经科学"和"免疫学"分离必须被打破
    
4. **接受量子效应的可能性**: 虽然 SRT 不依赖量子效应，但承认其作为 $\theta$ 分量的可能性
    

## 6.2 理论风险

1. **过度统一风险**: 将所有神经现象还原为"选择"可能忽视重要的机制差异
    
2. **病理几何化的伦理风险**: 将精神疾病视为"参数偏离"可能被误读为"不是真正的疾病"
    
3. **治疗简化风险**: "参数校正"的说法可能掩盖治疗的复杂性
    

---

# 7 可证伪预测与开放性问题

## 7.1 核心可证伪预测

|ID|假设名称|预测内容|证伪条件|
|:--|:--|:--|:--|
|H-M1|个体归一化曲线|高 $d$ 值个体显示更平缓的抑制曲线|$d$ 与 $n$ 无相关性|
|H-M2|补体-选择精度|C4 拷贝数预测抗干扰能力|C4 与 Stroop 无关|
|H-M3|调质特异性|特定调质阻断只影响特定选择维度|全维度认知下降|
|H-M4|生物同构|同构 AI 少样本学习曲线与生物不可分|同构 AI 需海量数据|
|H-M5|自旋-意识|氙同位素麻醉效力显著不同|同位素效力相同|
|H-M6|代谢-$d$ 滞后|$d$ 值恢复滞后于葡萄糖代谢恢复|$d$ 与代谢同步|
|H-M7|纳米假体复原|酸化纳米颗粒恢复老化细胞清除率|酸化恢复但清除率不改善|

## 7.2 开放性问题

1. **$\hat{G}_{meso}$ 的时间尺度**: 胶质介观算子的操作周期是什么？与睡眠周期有何关系？
    
2. **补体-修剪的因果方向**: C4 过表达是精神分裂症的原因还是结果？
    
3. **量子效应的边界**: 在什么温度/尺度下量子效应对 $\theta$ 有显著贡献？
    
4. **表观遗传写入的可逆性**: 多巴胺酰化写入的 $L_2$ 结构是否可以"擦除"？
    
5. **跨物种的归一化参数**: 不同物种的 $n$、$\sigma$、$W$ 是否存在系统性差异？这与 $d$ 值的物种差异有何关系？
    

---

# 附录：关键方程索引

|方程|名称|位置|
|:--|:--|:--|
|$[\hat{G}(x)]_i = \frac{x_i^n}{\sigma^n + \sum_j w_{ij} x_j^n}$|除法归一化|Ax-Mech-1|
|$\text{Pathology} = \vec{\theta}_{healthy} + \Delta \vec{\theta}$|病理偏离|Ax-Mech-2|
|$P(\text{Prune}) \propto C3/C4 \cdot \text{Microglia}$|修剪概率|Ax-Mech-3|
|$L_1(t) = \sum_n \text{Frame}_n \cdot \delta(t - t_n)$|帧渲染|Ax-Mech-5|
|$P(\text{Perceive}|S) = \sigma(S - (T_0 + \alpha[\text{IL-17}]))$|免疫门控|
|$\kappa_{body} = \text{GripForce}/\Psi_f$|具身锚定|Ax-Mech-9|

## 8 神经精神病学整合扩展（2026 Frontiers 对齐新增）

### 8.1 Neuropsychiatric 分类映射表（必填）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 神经主导型（Neurology-dominant） | 中~中高（受结构上限约束） | Semi-open（局部受损） | payable→borderline |
| 精神主导型（Psychiatry-dominant） | 低~中高波动 | Open↔Semi-open（高波动） | borderline / overloaded |
| 神经精神混合型（Neuropsychiatric mixed） | 中高离散分布 | Open + Closed 局部并存 | overloaded / unsustainable |
| 代偿恢复期（Integrated recovery） | 中高回升 | Semi-open→Open（稳态恢复） | payable |

### 8.2 Ontological Pathology Matrix（机制版）

\[
\Delta\theta = (\Delta\theta_{struct},\Delta\theta_{dyn})
\]
- \(\Delta\theta_{struct}\)：结构层漂移（白质/连接组/局灶损伤），主导 \(L_2\) 约束改变；
- \(\Delta\theta_{dyn}\)：动力学漂移（\(d,\rho_t,\vec v\)），主导 \(L_1\) 显现失稳。

**判别准则**（候选）：
\[
\text{Neurology Index} = \|\Delta\theta_{struct}\|,\quad
\text{Psychiatry Index} = \|\Delta\theta_{dyn}\|
\]
以二元平面定位病理簇，而非单轴标签。

### 8.3 Cross-Domain Intervention Protocol（干预协议）

\[
\mathcal{I}_{joint} = w_b\mathcal{I}_{bio} + w_p\mathcal{I}_{psy},\quad w_b,w_p\ge0
\]

- 生物干预（药物/刺激）：优先降低 \(\Psi_f\) 与恢复 \(\rho_t\)；
- 心理干预（CBT/叙事重构）：优先提升 \(d\) 与重定向 \(\vec v\)。

**协同收益定义**：
\[
\Delta S_{sync}=\Delta d\cdot(-\Delta\Psi_f)
\]
若 \(\Delta S_{sync}>0\) 且可持续，则判为真实跨域恢复。

### 8.4 语义断层与非线性放大（Irreducible Semantic Gap）

\[
L_1 = f(\theta) + \epsilon,\quad
\text{near critical set }\mathcal{C}:\; \left\|\frac{\partial f}{\partial \theta}\right\|\gg1
\]

* **Implication（中文）**：临床“同靶点异反应”不是噪声，而可能是系统处在临界集附近的非线性放大。

## 9 早期意识与共具身机制扩展（Neuroscience of Consciousness 对齐新增）

### 9.1 分类映射表（早期发生阶段 → SRT）

> **[R]** 发育阶段分类：Mahler et al.（1975，共生-分离-个体化）；Stern（1985，*The Interpersonal World of the Infant*）；Trevarthen（1979，初级互主性）。**[H]** d-value/Ψ_f 的具体映射为 SRT 新增操作化。

| 外部分类 | d-value 区间（proxy）[H] | d值数值参考 | 能流特征 | \(\Psi_f\) 状态 [H] |
|:--|:--|:--|:--|:--|
| 胎内共具身启动期 | 极低~低（\(d\to0^+\)） | 候选: $d \ll d_{UAL}$（← Cor-CONSC-1）| Semi-open（母体代偿主导） | payable（母体支付）|
| 围产分离过渡期 | 低~中波动 | 候选: $d \approx 0.1\,d_{UAL}$（波动大）| Open↔Semi-open（边界重标定） | borderline（双账本竞争）|
| 早期自体图式巩固期 | 低~中 | 候选: $0.1\sim0.4\,d_{UAL}$ | Open（自驱整合增强） | payable / borderline |
| 稳态婴儿期（自我-非我初稳） | 中（局部） | 候选: $0.4\sim0.7\,d_{UAL}$ | Open（本体独立账本初成） | payable |

**Ψ_f 状态说明（发育语境）**：
- **payable**：系统当前支付摩擦能力满足维持 L₁ 稳定（胎内 = 母体代偿支付，婴儿期 = 自体代谢支付）
- **borderline**：摩擦代价在系统可支付边缘波动，高应激时可能短暂失代偿（→ 触发依附系统）

**证伪条件（[H]）**：
- 若发育阶段的 d 值代理量（EEG 复杂度、PCI 代理、行为整合指数）在不同阶段间无显著递增趋势（控制睡眠状态后），则 §9.1 的发育 d 值增长假设失效。
- 若围产分离期的 Ψ_f^borderline 在无应激条件下也表现为 payable（无代偿失稳），则”边界重标定→borderline”的联结需修订。

### 9.2 Co-Embodiment Bootstrapping 方程

> **[H]** 共具身启动方程为 SRT 新增机制假设。

\[
\hat{G}_{inf}^{0}\leftarrow \mathcal{B}(\hat{G}_{mat},\theta_{maternal}),\quad
\frac{d\theta_{inf}}{dt}=f_{sensorimotor}+\chi_m\,f_{maternal}
\]

**符号说明**：$\chi_m$ = 母婴耦合系数（maternal coupling coefficient），操作化候选：母婴同步行为（eye contact 频率、mirror neuron 激活相关性）；$\mathcal{B}$ = bootstrapping 算子（初始化婴儿Ĝ从母体Ĝ的子选择继承，如体温/心率等稳态参数）。**[H — 操作化缺口]**：$\mathcal{B}$ 的具体形式（继承哪些 θ_{maternal} 分量）未确定；候选方向：通过表观遗传途径传递的参数偏置（产前皮质醇暴露等）。

### 9.3 自体边界的摩擦曲率判据

> **[H]** 以下边界形成准则为 SRT 原创：自体边界 = Ψ_f 曲率最大值处。

\[
\partial\Omega_{self}\sim\arg\max_x\left(\frac{\partial^2\Psi_f(x)}{\partial x^2}\right)
\]

* **Implication（中文）**：边界形成不是抽象认知标签，而是动作-反馈回路中摩擦曲率峰值的稳定沉积。**证伪方向**：若自闭症谱系（自体边界困难）的 interoceptive Ψ_f 曲率（如HRV变异度的空间分布）与正常发育组无差异，则该判据需修订。

### 9.4 火焰与代谢生命算子的阈值区分（新增）

> **[H]** 生命判据三乘积为 SRT 新增区分准则。

\[
\mathcal{D}_{life}=\mathbb{1}\left[\frac{d\theta}{dt}\neq0\right]\cdot\mathbb{1}\left[d>0^+\right]\cdot\mathbb{1}\left[\Psi_f^{sens}>0\right]
\]

- **火焰**：可耗散但 $d\theta/dt\approx0$（无参数学习），$d\approx0$（无关切带宽）→ $\mathcal{D}_{life}=0$；
- **代谢网络**：满足最小 $d$ 与 $\Psi_f^{sens}$ 风险敏感，具备原初选择性 → $\mathcal{D}_{life}=1$。

* **Implication（中文）**：生命判据不是”是否耗散”，而是”是否形成可学习的、可支付摩擦的选择闭环”。**证伪方向**：若合成化学振荡体（Belousov-Zhabotinsky反应）能满足三条指标（参数自适应学习 + 微弱关切带宽 + 摩擦敏感性），则”生命” SRT判据需增补排除条件。

### 9.5 存在感（Presence）操作化代理（新增）

定义局部存在感强度：
\[
\mathcal{P}_{sense}(t)\propto \left|\frac{d\Psi_f^{local}}{dt}\right|\cdot \Gamma_{anchor}(t)
\]
其中 \(\Gamma_{anchor}\) 为锚定稳定系数（可由任务一致性/神经同步代理估计）。

- 自动化低负荷状态（如习惯驾驶）：\(d\Psi_f/dt\to 0\Rightarrow \mathcal{P}_{sense}\downarrow\)
- 高不确定锚定时刻（存在性惊奇）：\(d\Psi_f/dt\uparrow\Rightarrow \mathcal{P}_{sense}\uparrow\)

### 分类映射表（Hart Ch.3 关键区分 → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| “本质”层（what） | 低~中（未锚定） | Semi-open | payable |
| “存在”层（that it is） | 中~高（锚定增强） | Open | payable / borderline |
| 日常习惯化存在稀薄 | 低~中 | Closed 倾向 | 低斜率 \(d\Psi_f/dt\approx0\) |
| 存在性惊奇峰值 | 中高~高 | Open（重锚定） | 高斜率 \(d\Psi_f/dt\gg0\) |

### Definition Summary (定义概述)

- **神经流形 (Neural Manifold, L₀)**：$\sigma(t)\in\mathcal{M}\subset\mathbb{R}^N$；神经态是高维流形上的连续轨迹，选择即生成稳定轨迹。
- **点燃投影 (Ignition Projection, L₀→L₁)**：$\Pi_{ignite}:\mathcal{M}\to\mathcal{M}_*$，其中 $\mathcal{M}_*=\{\sigma:\mathcal{A}(\sigma)\ge\tau_{ignite}\}$；跨域投影的可计算阈值。
- **门控算子 (Loop-Gating, L₁)**：$\mathcal{G}_{gate}=\mathcal{G}_{thal}\circ\mathcal{G}_{bg}$；丘脑-基底节回路决定哪些轨迹可投影为 $L_1$。
- **参数漂移病理 (Parameter Drift, L₂)**：$\theta=\theta_{healthy}+\Delta\theta$；精神病理是算子参数的拓扑偏移，非症状集合。

### Formalization Summary (形式化概述)

三条核心方程构成 SRT 神经机制框架的三个层次：**微观计算原型** → **整合涌现条件** → **具身-行动效率**。

- **能量-信息极值** (T-NEURO-MECH-1)：$\mathcal{J}=H(\sigma)-\lambda E(\sigma)$，稳态解必然满足除法归一化 $R_i=L_i^n/(\sigma^n+\sum_j w_{ij}L_j^n)$。信息最大化与代谢成本最小化的唯一交点。注：$\lambda \propto \Psi_f^{metabolic}$（代谢拉格朗日乘子对应本体论摩擦的代谢成分，详见 Ax-NEURO-MECH-3 注）。
- **点燃相变** (Ax-NEURO-MECH-7)：$\mathcal{A}(\sigma)\ge\tau_{ignite}\;\land\;\Phi_{SRT}\cdot d > C_{critical}$，其中 $\Phi_{SRT} = d \cdot \Psi_f$（SRT 整合度，替代 IIT 的 $\Phi_{IIT}$；参见 SRT-AI-03 Cor-CONSC-1）。即：点燃需要激活阈值与整合选择代价协同超过临界值，展开为 $d^2 \cdot \Psi_f > C_{critical}$。
- **具身锚定** (Ax-Mech-9)：$\kappa_{body}=\alpha \cdot F_{grip}/\Psi_f$（$\alpha$ 为量纲匹配系数，$F_{grip}$ 为运动系统效应力代理，量纲尚待精确形式化）。意向性向物理显现转化的效率系数；$\kappa_{body} \downarrow$ 对应衰老/具身退化（算子-基质脱锚）。

### Mechanism Explanation (机制解释)

> [R→Carandini & Heeger 2012 *Nature Reviews Neuroscience*（除法归一化：感觉皮层中的普适计算原语）; Schafer et al. 2012 *Science*（小胶质细胞补体标记（C1q/C3）介导突触修剪：L₂修剪的机制基础）; Friston 2010 *Nature Reviews Neuroscience*（PE→Δθ的梯度学习联结）; Barlow 1961（冗余压缩与神经代谢约束）]

**R/H 区分**：
- [R] 除法归一化（Carandini & Heeger）；补体标记突触修剪（Schafer）；PE→θ更新（Friston）——均为既有神经科学框架
- [H] **SRT综合解读**：① PE∝Ψ_f桥接计算层与本体论层（SRT特有的双层等同主张）；② Ĝ_meso以"介观算子"概念统合胶质细胞功能；③ 衰老=κ_body衰退（d值完好但算子-基质脱锚）——此三项解读均为SRT独有框架

$\hat{G}_\theta$ 在神经流形 $\mathcal{M}$ 上执行选择流：感觉-动作输入 $u$ 驱动轨迹 $\dot\sigma=F(\sigma,\theta,u)$，经门控算子 $\mathcal{G}_{gate}$ 筛选后由点燃投影 $\Pi_{ignite}$ 锚定为 $L_1$。代谢约束使选择动力学收敛为除法归一化 [R→Carandini & Heeger 2012]；$\Psi_f$ 通过预测误差映射 ($PE\propto\Psi_f$) 桥接计算层与本体论层 [H]。胶质介观算子 $\hat{G}_{meso}$ 以补体标记执行慢时标 $L_2$ 修剪 [R→Schafer et al. 2012 + H形式化]。病理对应 $\Delta\theta$ 偏移，衰老对应 $\kappa_{body}$ 衰退——$d$ 值完好但算子与基质逐渐脱锚 [H]。

**可证伪预测**：
- FC-MechSyn-1：PE∝Ψ_f：同一被试的前额叶预测误差信号（EEG MMN振幅）应与Ψ_f代谢代理（皮质醇/静息代谢率）正相关——若无相关则PE-Ψ_f桥接为类比而非可测联结
- FC-MechSyn-2：衰老被试（κ_body↓代理：握力/步态稳定性↓）的d值代理应与正常水平接近，但算子-基质耦合（运动-认知整合任务绩效）显著下降——若d值和耦合同步下降则"d完好但脱锚"的衰老特征主张需修订

---

## 【理论边界/防误用声明】

1. 本文档提供的是 SRT 解释与建模框架，不应被误用为对个体的确定性标签系统。
2. 任何跨尺度映射都依赖操作化假设与测量条件，超出条件范围不得外推为”普适定律”。
3. 涉及临床、政策、工程决策时，需与经验数据、伦理审查和领域规范共同使用。
4. 不采纳”历史叙事桥梁=机制完备模型”的推论：临床哲学整合必须补上可测动力学。
5. 不采纳”单一疗法可跨层解决全部病理”的推论：SRT 要求结构轴与动力学轴协同干预。
6. 不采纳”共具身=主体不独立”的绝对推论：SRT 采用相变诞生模型而非永久融合模型。

## 机制同构补注：Active Inference × SRT（2026-03-06）

### Ax-NEURO-MECH-8: Neuro-Anatomical Regulator Isomorphism（新增，轻量）
**Formal Definition**: 若环境统计在“身份特征”与“空间位置”上近似正交，则具身算子硬件层会收敛到分流拓扑：
\[
\Theta_{neural}^{*}=\arg\min_{\Theta}F(\Theta)\quad \text{s.t.}\quad I(What;Where)\approx 0
\]
\[
\Theta_{neural}^{*}\Rightarrow \mathcal{S}_{ventral}\perp \mathcal{S}_{dorsal}
\]
* **Implication（中文）**：What/Where 双流可视作 Good Regulator 原理在神经解剖层的可观测沉积：不是随机分工，而是长期自由能最小化下的拓扑同构结果。

### Note-NEURO-MECH-8: Active Sampling Coupling
主动推断中的“采样行动”可写作对 \(\theta\) 的在线更新门：
\[
\theta_{t+1}=\theta_t-\eta\nabla_\theta F(o_t,a_t)
\]
其中 \(a_t\) 同时改变下一时刻可观测输入分布 \(p(o_{t+1}|a_t)\)。

### [Lineage/Source]
- Friston et al., Active Inference / Free-Energy Principle（系列论文）
- Conant & Ashby, Good Regulator Theorem

## 数学直觉协议切换补注（2026-03-06）

### Def-NEURO-MECH-9: Protocol Switching Gain
对同一任务目标 \(X\)，定义协议增益：
\[
\Gamma_{switch}(X)=\frac{\Psi_f(X\mid \Pi_{sym})}{\Psi_f(X\mid \Pi_{vis})}
\]
当 \(\Gamma_{switch}>1\) 时，视觉/拓扑协议优于线性符号协议。

### T-NEURO-MECH-4: Scaffolding Compression Theorem (Candidate)
若系统已有稳定抽象脚手架 \(L_2^{depth}\)，则新任务有效工作记忆负载呈压缩：
\[
WM_{eff}(X) \approx \frac{WM_{raw}(X)}{1+\beta L_2^{depth}}
\]
且随之带来推理时延下降：
\[
\tau_{solve}(X)\downarrow\ \text{as}\ L_2^{depth}\uparrow
\]
* **Implication（中文）**：长期抽象资本化可将“原本超带宽任务”变成可直觉处理任务。

## 【理论边界/防误用声明】
- 不采纳“直觉快 = 必然正确”的推论。
- 不采纳“单次梦境/灵感即证明直接访问 \(L_0^{abs}\)”的推论。
- 适用边界：该条款用于解释性能机制，不替代形式证明与复现。

### [Lineage/Source]
- Ramanujan 与数学直觉讨论语境（2026）
