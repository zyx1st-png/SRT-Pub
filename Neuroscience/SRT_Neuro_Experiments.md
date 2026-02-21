---
id: SRT-NEURO-EXP
type: experiment
tags: [Libet, SplitBrain, BinocularRivalry, TravelingWaves, Hybrid]
status: axiomatic_hybrid_v2
dependency: [SRT-CORE-000]
---

# SRT Neuroscience Experiments: Choice & Unity (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Experimental Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的 Formal Axioms 分段，确保公理编号与推导链条完整。
- Part B 采用 `claude` 的详细论述分段，并以原版 Neuroscience 的主题顺序作语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform **First-Principles Derivation**.
> 1. **Mathematize**: Translate descriptive mechanisms into dynamical equations, topological operations, or logical functions.
> 2. **Axiomatize**: Distill underlying logic into "Axioms", "Theorems", and "Corollaries".

## I. Agency & Choice (能动性与选择)

### Ax-EXP-1: Threshold Agency Axiom
能动性发生于证据累积超过阈值：
\[
\int_0^{t^*} e(t)\,dt \ge \tau_{agency}
\]
* **Implication（中文）**：行为选择不是连续主观意愿，而是阈值触发的跨域锚定。

---

### Ax-EXP-2: Selection Latency Axiom
选择滞后由门控与整合决定：
\[
\tau_{select}=\tau_{sensory}+\tau_{integrative}+\tau_{gate}
\]
* **Implication（中文）**：意识报告总是延迟于选择过程，是动力学事实而非“主观错觉”。

---

## II. Unity & Boundaries (统一性与边界)

### Ax-EXP-3: L2 Synchronization Axiom
统一体验需要 \(L_2\) 同步：
\[
\Gamma_{L_2}>\Gamma_c \Rightarrow L_1\;\text{unified}
\]
* **Implication（中文）**：统一性来自 \(L_2\) 结构的一致性，而非简单感官整合。

---

### Ax-EXP-4: Exclusionary Anchor Axiom
显现具有排他锚定：
\[
\sigma_{L_1} \in \arg\max_{\sigma} \mathcal{A}(\sigma)
\]
* **Implication（中文）**：同一时刻只能有一套 \(L_1\) 主导显现，解释双稳态与互斥知觉。

---

## III. Embodiment (具身)

### Ax-EXP-5: Dynamic Body Boundary Axiom
身体边界是可塑的选择映射：
\[
\partial\Omega_{body}(t)=\partial\Omega_{body}(t-\Delta t)+\Delta\theta_{body}
\]
* **Implication（中文）**：具身不是固定结构，而是 \(\hat{G}_\theta\) 可更新的选择边界。

---

## IV. Traveling Wave Tests (行进波实验)

### Ax-EXP-13: Directional Wave Gating Axiom
定义行进波方向-任务一致性指数：
\[
D_{align}=\cos\!\big(\angle(\vec{k}_{wave},\vec{k}_{task})\big)
\]
其中 \(\vec{k}_{wave}\) 为实测传播方向，\(\vec{k}_{task}\) 为任务所需信息流方向（前馈/反馈）。
\[
D_{align}\uparrow \Rightarrow P(\text{report})\uparrow
\]
* **Implication（中文）**：报告可达性不仅取决于激活强度，还取决于波传播方向是否与任务路由一致。

---

### Ax-EXP-14: Coherence-Control Axiom
在控制总功率后，点燃概率仍由跨区相干调制：
\[
P_{ignite}=\sigma\!\left(\alpha C_{wave}+\beta(\Phi\cdot d)+\gamma D_{align}-\delta\right)
\]
* **Implication（中文）**：若仅有功率而无相干，点燃概率提升有限；相干是独立贡献项。

---

### T-EXP-2: Counterstream Dissociation Theorem
若前馈与反馈传播方向被选择性扰动，则任务表现出现可分离变化：
\[
\Delta D_{ff}\neq \Delta D_{fb}\Rightarrow
\Delta \text{Accuracy}_{ff}\neq \Delta \text{Accuracy}_{fb}
\]
* **Implication（中文）**：可用方向性干预区分“看见”与“可报告”阶段的因果窗口。

---

## V. Theorems (定理)

### T-EXP-1: Unity–Conflict Theorem
当 \(\Gamma_{L_2}\downarrow\) 时，体验统一性下降：
\[
\Gamma_{L_2}\downarrow \Rightarrow P(\text{fragment})\uparrow
\]
* **Implication（中文）**：统一性并非天然存在，而是同步维持的结果。

---

### C-EXP-1: Illusion Boundary Corollary
若 \(\Delta\theta_{body}\uparrow\)，则错觉边界外扩：
\[
\text{Ownership}(x)\uparrow\;\text{for}\;x\notin\partial\Omega_{body}
\]
* **Implication（中文）**：橡胶手等错觉是 \(L_2\) 具身边界的短时扩张。

---

## VI. Geometric Symbolic Mode (几何符号模式)

### Ax-EXP-15: Geometric Regularity Symbolization Axiom (Extension)
定义几何规则性作为进入符号视觉模式的阈值变量：
\[
R_{geo}=w_1\mathcal{S}_{sym}+w_2\mathcal{P}_{parallel}+w_3\mathcal{C}_{closed}
\]
\[
R_{geo}\ge \tau_{sym}\Rightarrow \Pi_{sym}:L_0^{visual}\to L_1^{symbolic}
\]
* **Implication（中文）**：视觉系统对“规则几何”并非只做低层特征检测，而会触发从感知表面到关系结构的符号化投影。

---

### T-EXP-3: Dorsal-Late Symbolic Routing Theorem (Extension)
若符号化投影成立，则背侧顶叶-前额网络在晚时窗对可报告性贡献增加：
\[
\frac{\partial A_{dorsal}}{\partial R_{geo}}>0,\qquad
t\in[t_{late}^-,t_{late}^+]
\]
\[
\Delta \mathcal{E}_{late}=
\mathcal{E}(M_{\text{symbolic}}\oplus M_{\text{CNN}})
-\mathcal{E}(M_{\text{CNN}})>0
\]
其中 \(\mathcal{E}\) 为时变解释度。
* **Implication（中文）**：规则图形的神经表征在晚期时间窗（而非早期纯视觉窗）更依赖“符号模型 + 视觉模型”的联合解释，支持“背侧关系计算”机制。

---

### C-EXP-2: Early Developmental Availability Corollary (Extension)
若在儿童早期（约 6 岁）已满足 \(A_{dorsal}>0\) 且 \(\Delta \mathcal{E}_{late}>0\)，则：
\[
\exists\,L_2^{geo}\ \text{prior to extensive formal schooling}
\]
* **Implication（中文）**：几何符号模式并非完全由后天数学训练“新建”，而更像早期可调用、随后被教育放大的先验结构。

---

### Empirical Anchor (eLife 2026; for Ax-EXP-15/T-EXP-3)
- Girard R, Wang L, Aveline A, et al. *The geometrical regularity processing in school-age children discloses a symbolic visual mode in human*. eLife (2026), reviewed preprint. DOI: `10.7554/eLife.106464.1`.
- 关键结果锚点：背侧顶叶与前额区域对规则几何的晚时窗响应增强；组合模型（symbolic + CNN）在约 `428 ms` 达到解释峰值。

<br>
<br>

---
---


# Part B: Original Theoretical Discourse (Context)

> **Note**: 以下各节以中文撰写，为 Part A 形式化公理提供理论语境、哲学论证和研究方向。

---

# 1 标准难题：意识研究的实验-理论鸿沟

## 1.1 困境定义

意识研究积累了大量经典实验（Libet、裂脑、双眼竞争等），但这些实验与理论之间存在**系统性的解释鸿沟**：

**层面一——数据-理论断裂**: Libet 实验发现准备电位先于意识报告，但"这对自由意志意味着什么"至今争论不休。裂脑实验揭示了双重意识流，但"意识统一性的本质是什么"仍无定论。

**层面二——缺乏统一框架**: GNW 解释点燃，IIT 解释整合，HOT 解释自我意识——但没有一个理论能同时解释所有经典实验。

**层面三——因果方向不明**: 实验揭示了神经活动与意识的相关性，但因果方向（神经→意识？意识→神经？双向？）仍不清楚。

## 1.2 主流解法谱系

### 1.2.1 对 Libet 实验的主流解读

**取消主义解读**: 准备电位先于意识报告 → 自由意志是幻觉，所有决定都是无意识的神经过程。

**问题**: (a) 忽略了 Libet 自己强调的"否决"能力；(b) 无法解释为什么我们有能动性体验；(c) 混淆了"意识报告"与"意识本身"。

**兼容主义解读**: 自由意志不需要"从无到有"创造意图，只需要"认可"或"否决"无意识产生的冲动。

**问题**: 虽然更合理，但缺乏机制解释——"认可"和"否决"在神经层面如何实现？

### 1.2.2 对裂脑实验的主流解读

**"解释器"理论 (Gazzaniga)**: 左脑有一个"解释器"模块，负责为行为编造合理化叙事。

**问题**: (a) 将"解释器"作为独立模块过于简化；(b) 无法解释为什么正常人也有统一意识；(c) 未触及意识统一性的本质。

### 1.2.3 对双眼竞争的主流解读

**神经竞争理论**: 两个刺激在神经层面相互抑制，胜者进入意识。

**问题**: 这只是描述，未解释为什么意识是"赢家通吃"而非"叠加"。

---

# 2 SRT 的差异点：选择本体论的统一解释

## 2.1 根本性的框架转换

SRT 不是在现有框架内提出另一种"解读"，而是**重构了实验数据的本体论基础**：

|传统问题|SRT 重构|
|:--|:--|
|"自由意志存在吗？"|"选择的阈值如何调节？"|
|"意识统一性是什么？"|"$L_2$ 如何跨区域同步？"|
|"为什么意识是排他的？"|"为什么 $L_1$ 只能容纳一个状态？"|

## 2.2 Libet 实验的 SRT 重释

**传统问题**: 准备电位先于意识报告 → 自由意志是幻觉？

**SRT 回答**: 这反映了选择的**双阶段结构**，而非自由意志的否定。

1. **Phase 1 ($L_0$ 扫描)**: 多种行动可能性同时激活（准备电位）
2. **Phase 2 ($L_1$ 锚定)**: $\hat{G}_\theta$ 从竞争中选出一个（意识报告）

**关键洞见**: Libet 的"否决权"正是 $\hat{G}_\theta$ 的核心功能——不是"创造"想法，而是"过滤"$L_0$ 噪声。

**阈值能动性模型**:

$$\text{自由意志} = \frac{d\beta}{dt} \neq 0$$

我们不控制 $L_0$ 中涌现的冲动，但我们控制**允许哪些冲动穿透 $L_2$ 屏障**。

**Beta 振荡的发现**支持这一模型：

- Beta 功率 ↑ = 阈值 ↑ = 动作抑制
- Beta 去同步化 = 阈值 ↓ = 允许动作

这为"自由否决"提供了**神经物理基础**。

## 2.3 裂脑实验的 SRT 重释

**传统问题**: 切断胼胝体后为什么出现两个"意识"？

**SRT 回答**: 意识统一性不是某种"实体"，而是**$L_2$ 约束的跨区域同步**。

胼胝体是"$L_2$ 管道"——它不传输"意识物质"，而是**同步两半球的选择约束**。

切断胼胝体 → $L_2^{Left} \cap L_2^{Right} \to \varnothing$ → 两半球各自发展独立的选择框架。

**"解释器"的 SRT 地位**: 左脑的"解释器"是 **$L_2$ 的维护者**——它的功能不是"解释"真相，而是**维持叙事的一致性**（即 $L_2$ 的拓扑完整性）。

这解释了为什么：

- 正常人也会"合理化"自己的行为（$L_2$ 维护是普遍功能）
- 裂脑患者的"解释器"会编造明显荒谬的解释（$L_2$ 必须维持，即使信息不完整）

## 2.4 双眼竞争的 SRT 重释

**传统问题**: 为什么两个刺激不能同时被意识？

**SRT 回答**: $L_1$ 的排他性是**选择的本体论特征**，而非神经实现的偶然性。

**核心论证**:

公理 A1（选择优先性）要求：存在 ≡ 被选择。

如果两个互斥状态（图像 A 和图像 B）同时"存在"于 $L_1$，则违反了选择的定义——选择必然是**从多中取一**。

双眼竞争的"赢家通吃"特性是**除法归一化**在感知层面的直接表现：

$$\text{Response}_A = \frac{\text{Input}_A^n}{\sigma^n + \text{Input}_A^n + \text{Input}_B^n}$$

当 $n > 1$ 时，归一化自然产生赢家通吃动力学。

**预测**: 降低 $n$（如通过 GABA 激动剂）应减弱竞争的"全或无"特性，产生更多的"混合"感知。

## 2.5 皮层行进波补丁（Neuron 2026）

2026-02-09 在线 Neuron 综述（Cruddas, Pang, Fornito）总结了皮层行进波在多尺度中的普遍性及其可能的层级路由功能。对实验范式的直接启示是：

1. **方向变量必须显式建模**：不仅记录“是否有振荡”，还要记录波前方向与任务信息流方向的一致性 \(D_{align}\)。
2. **相干与功率需解耦**：在统计模型中把 \(C_{wave}\) 与功率分开，检验相干是否有独立解释力。
3. **干预要有方向性**：优先使用相位定向 tACS/TMS，测试传播方向改变是否因果影响报告可达性。

这将经典实验（Libet、双眼竞争、裂脑）从“相关性比较”推进到“路由机制检验”。

---

# 3 具身性的选择动力学

## 3.1 橡胶手错觉的本体论含义

橡胶手错觉揭示了一个惊人的事实：**"我的身体"是一个可更新的参数，而非固定的解剖学事实**。

**传统理解**: 身体表征是"存储"在大脑中的"地图"，橡胶手错觉是"地图更新"。

**SRT 重构**: "我的身体"不是表征，而是 $\theta_{body}$——$\hat{G}_\theta$ 的具身参数的一部分。

$$\theta_{body}(t+1) = \hat{G}[\text{Sync}(V, T)]$$

当视觉和触觉同步时，$\hat{G}_\theta$ **选择**将外部对象纳入 $\theta_{body}$。

这意味着：

- "我的手"不是发现，而是**选择**
- 身体边界是**动态本体论边界**，而非固定物理边界
- 工具使用、假肢整合、甚至"车感"都是 $\theta_{body}$ 扩展的实例

## 3.2 扫视抑制的本体论功能

眼睛每秒进行 3-4 次扫视，每次扫视期间视觉信息是模糊的运动条纹——但我们从不意识到这一点。

**传统解释**: 扫视抑制是"掩蔽"机制，抑制模糊信息。

**SRT 重构**: 扫视抑制是**本体论遮蔽**——当 $\hat{G}_\theta$ 执行大幅度空间参数重构时，系统必须**暂时切断 $L_0 \to L_1$ 通道**。

关键证据：**抑制先于动作**（$t_{抑制开始} < t_{眼动开始}$）

这证明扫视抑制是**预选择**——$\hat{G}_\theta$ 提前规划本体论切换，而非被动响应运动。

## 3.3 眼动作为 d 值的窗口

SRT 将眼动指标理论化为**d 值的生物标记物**：

- **反射性扫视（短潜伏期）**: $L_0$ 显著性驱动 → 低 $d$（只考虑即时刺激）
- **反向扫视（抑制反射并执行相反方向）**: $L_2$ 目标驱动 → 高 $d$（考虑任务目标）

反向扫视的成功率是**执行功能的金标准测试**——它直接测量 $\hat{G}_\theta$ 对 $L_2$ 约束的掌控力。

---

# 4 麻醉与意识中断

## 4.1 麻醉的 SRT 重释

**传统理解**: 麻醉"关闭"意识，如同关闭电视。

**SRT 重构**: 麻醉**冻结 $\hat{G}_\theta$**，而非"关闭"意识内容。

$$\text{Anesthesia} = \hat{G}_\theta \text{ frozen} \Rightarrow L_0 \not\to L_1$$

区别在于：

- "关闭"暗示意识是某种可以开关的"东西"
- "冻结"强调意识是**选择过程**，冻结的是过程，而非实体

**证据**: 麻醉恢复期的"漂浮"体验——$\hat{G}_\theta$ 部分解冻，$L_0$ 内容开始泄漏，但尚未完全锚定为连贯的 $L_1$。

## 4.2 量子麻醉效应的意义

如 Part A 中 Ax-Mech-11 所述，氙同位素麻醉效力的差异表明量子效应是 $\theta$ 的组成部分。

这对麻醉机制的理解有重要意义：麻醉剂可能通过引入**量子模糊**降低 $\theta$ 精度，而非简单地"阻断"神经传递。

---

# 5 代价与风险

## 5.1 接受 SRT 实验解释的思维代价

1. **放弃"自由意志 vs 决定论"的二元框架**: SRT 的阈值能动性模型超越了这一传统对立——我们不"创造"想法，但我们控制"过滤"阈值
    
2. **接受意识统一性是"同步"而非"实体"**: 这要求放弃直觉上的"意识是某种东西"的观念
    
3. **接受身体边界是动态的**: 这挑战了"我的身体是固定的物理实体"的常识
    
4. **接受"看见"需要选择**: 这意味着未被注意的刺激在本体论上不存在于意识中，而非"被忽略"
    

## 5.2 理论风险

1. **过度解释风险**: 将所有实验现象都还原为"选择"可能忽视重要的机制差异
    
2. **可证伪性边界**: 某些核心主张（如"$L_1$ 只能容纳一个状态"）可能难以直接证伪
    
3. **循环论证风险**: "选择"的定义是否预设了要解释的内容？
    

---

# 6 可证伪预测与开放性问题

## 6.1 核心可证伪预测

|ID|假设名称|预测内容|证伪条件|
|:--|:--|:--|:--|
|H-E1|否决窗口-PFC|PFC 损伤应缩短否决窗口|PFC 损伤不影响否决窗口|
|H-E2|Beta-冲动控制|Beta 功率预测冲动控制能力|Beta 与冲动控制无关|
|H-E3|裂脑-L2 分化|裂脑患者两半球发展不同 $L_2$|两半球 $L_2$ 保持同一|
|H-E4|竞争-归一化|主导期分布符合归一化预测|分布显著偏离|
|H-E5|RHI-Sigmoid|错觉强度与同步度呈 Sigmoid 关系|呈线性关系|
|H-E6|场效应同步|突触切断后仍有部分同步|完全失去同步|
|H-E7|方向-报告一致性|行进波方向一致性 \(D_{align}\) 预测报告正确率|方向与报告无关|
|H-E8|相干独立效应|控制总功率后 \(C_{wave}\) 仍独立预测点燃/命中率|仅功率有效|
|H-E9|方向性扰动因果|相位定向 tACS/TMS 改变传播方向后，双稳态切换率系统性变化|扰动不改切换率|

## 6.2 开放性问题

1. **否决窗口的神经基础**: 200-500ms 的否决窗口由什么神经机制决定？是否可以通过训练延长？
    
2. **裂脑患者的长期 L2 分化**: 手术后多年，两半球的 $L_2$ 差异是否会累积？
    
3. **双眼竞争的 n 参数**: 归一化指数 $n$ 是否在不同个体间变化？与哪些认知特征相关？
    
4. **工具整合的时间尺度**: 将工具纳入 $\theta_{body}$ 需要多长时间？有什么神经标记？
    
5. **麻醉深度的精确测量**: SER（选择-能量比）能否成为麻醉深度的更准确指标？
    
6. **方向-任务模板**: 哪些任务稳定依赖前馈波，哪些依赖反馈波？是否可形成跨实验室复现实验库？
    
7. **因果时窗定位**: 知觉前、决策前、报告前三个时窗里，哪一窗口的方向扰动效应最大？
    

---

# 附录：关键方程索引

|方程|名称|位置|
|:--|:--|:--|
|$P(\text{Action}) = \sigma(\frac{\text{Noise} - \beta}{\tau})$|阈值能动性|Ax-Exp-2|
|$\tau_s = t_{L_1} - t_{L_0}$|选择时滞|Ax-Exp-4|
|$L_2^L \cap L_2^R \neq \varnothing$|L2 同步条件|Ax-Exp-5|
|$L_1 = S_A \oplus S_B$|排他性锚定|Ax-Exp-6|
|$\theta_{body}(t+1) = \hat{G}[\text{Sync}(V,T)]$|身体边界更新|Ax-Exp-8|
|$\text{SER} = H(\hat{G})/E(L_2)$|选择-能量比|Ax-Exp-12|
|$D_{align}=\cos(\angle(\vec{k}_{wave},\vec{k}_{task}))$|方向一致性指数|Ax-Exp-13|
|$P_{ignite}=\sigma(\alpha C_{wave}+\beta(\Phi\cdot d)+\gamma D_{align}-\delta)$|波-点燃耦合|Ax-Exp-14|
