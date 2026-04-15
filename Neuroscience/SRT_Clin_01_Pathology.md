---
id: SRT-CLIN-01
type: dynamics
tags: [Pathology, NDE, Schizophrenia, L2 Inversion, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-NEURO-AXIOMS-001]
---

# SRT Neuroscience II: Pathology & Anomalies (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Pathological Dynamics (AI-Readable).
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

## I. Pathology as Operator Drift (病理作为算子漂移)

### Ax-PATH-1: Operator–Substrate Recursion Axiom
神经算子与基质存在递归耦合：
\[
\hat{G}_\theta\Rightarrow \Delta\theta,\qquad \Delta\theta\Rightarrow \Delta\hat{G}_\theta
\]
当回路增益 \(g>1\) 时发生病理放大：
\[
\Delta\theta_{t+1}=g\,\Delta\theta_t
\]
* **Implication（中文）**：病理不是静态缺陷，而是算子与基质的正反馈偏移。

---

### Ax-PATH-2: L2 Parasitic Inversion Axiom
当 \(L_2\) 硬度相对 \(d\) 过强时，选择被寄生化：
\[
\kappa \equiv \frac{\text{Hardness}(L_2)}{d}\uparrow \Rightarrow \hat{G}_\theta\;\text{locks into} \;L_2\text{-loops}
\]
* **Implication（中文）**：过强先验会让 \(L_2\) 反过来吞噬 \(L_0\) 的新选择，形成强迫、固着或妄想回路。

---

### Ax-PATH-3: Body-Without-Organs Axiom (Interoceptive Decoupling)
定义具身锚定系数：
\[
\kappa_{body}\equiv \frac{\|\nabla_{intero}\mathcal{U}\|}{\Psi_f}
\]
若 \(\kappa_{body}\to 0\)，则出现“无器官身体”态：
\[
\hat{G}_\theta\perp L_1^{intero}
\]
* **Implication（中文）**：去具身导致 \(L_1\) 现实感漂移，出现解离或去人格化。

---

### Ax-PATH-4: Pathological Reality Type I — Rigid Reality (僵化现实)
$\hat{G}_\theta$ 的选择机制失去变异性（Loss of Complexity），无法处理外部波动：
\[
\text{Var}(\hat{G}_\theta[L_0]) \to 0 \Rightarrow \text{Adaptability} \to 0
\]
* **Implication（中文）**：对应"失去无序"状态——系统过度确定化，选择被锁死在窄带模式（强迫症、顽固性抑郁、教条化）。

---

### Ax-PATH-5: Pathological Reality Type II — Collapsed Reality (崩溃现实)
$\hat{G}_\theta$ 的选择边界失效，外部混沌直接冲击内部状态：
\[
\partial\Omega_{select} \to \varnothing \Rightarrow H(L_1) \to H(L_0)
\]
* **Implication（中文）**：对应"运作超出边界"——选择膜崩溃，系统被淹没在未过滤的 $L_0$ 噪声中（急性精神病、解离发作、创伤性去个体化）。

---

### T-PATH-3: L2 Bypass Healing Theorem (L2旁路疗愈定理)
疗愈不等于在 $L_2$ 内的认知重构 (Reframing)，而须建立从 $L_0$ 到 $L_1$ 的直接行动链：
\[
\text{Healing} = \underbrace{\hat{G}_\theta[L_0^{trauma} \to L_1^{symbol}]}_{\text{具象化 (Objectification)}} \xrightarrow{\text{Action}} \underbrace{L_1^{resolved}}_{\text{结构解结}} \implies \Delta \Psi_f \downarrow
\]
* **Implication（中文）**：仅在 $L_2$ 中 Reframing 等同于"在旧地图上画新线"，本体论摩擦未消除。算子须绕过语言中枢（DMN/$L_2$），直接进入 $L_0$（潜意识/创伤场），将其强行坍缩为 $L_1$ 中的可操作对象。疗愈的终极指标不是"感觉好了"，而是 $\Psi_f$ 的物理下降。

---

### T-PATH-4: Objectification Theorem (对象化定理)
痛苦的可操作性是其具体性的函数：
\[
\text{Manipulability}(\Psi_f) \propto \text{Concreteness}(\text{Proj}(\Psi_f))
\]
* **Implication（中文）**：将弥散的高维焦虑投影为低维对象（如"石头"/"怪兽"），本质上是降维操作。一旦痛苦变为 $L_1$ 对象，算子的运动原语（粉碎、清洗等Motor Primitives）即可被调用。反之，越抽象的概念（如"原生家庭情结"）可操作性越低，疗愈效率越低。

---

## II. Anomalous States (异常态)

### Ax-ANOM-1: Near-Death Divergence Axiom
当系统临近不可逆边界 \(\partial\Omega\) 时：
\[
\nabla_{\mathcal{S}}\mathcal{U}\uparrow\uparrow \Rightarrow d(t)\to d_{max}
\]
* **Implication（中文）**：濒死状态不是“幻觉”，而是 \(d\) 急剧上升导致的选择带宽扩展。

---

### Ax-ANOM-2: Terminal Lucidity Axiom
若 \(L_2\) 硬度瞬时下降，则出现短时清醒：
\[
\Delta\text{Hardness}(L_2)\downarrow \Rightarrow \Pi_{L_1}\;\text{re-stabilizes}
\]
* **Implication（中文）**：终末清醒对应 \(L_2\) 锁定被暂时解除的“窗口效应”。

---

### Ax-ANOM-3: Bicameral Regression Axiom
当左右或前后回路耦合失配：
\[
\hat{G}_\theta=\hat{G}_A\oplus \hat{G}_B,\quad \text{Coupling}\downarrow
\]
* **Implication（中文）**：二分回归是算子裂解，而非单纯的“听幻觉”。

---

### Ax-ANOM-4: Déjà Vu Time-Index Axiom
若时间索引映射发生错位：
\[
\pi_t(\sigma)\to \pi_{t-\Delta}(\sigma)
\]
则产生“已然感”。
* **Implication（中文）**：即视感是时间坐标的投影错误，而非记忆重复。

---

### Ax-ANOM-5: Familiarity–Recollection Dissociation Axiom (Extension)
定义即视感的最小动力学条件为“熟悉感升高 + 情节检索失败 + 元监控报警”：
\[
\text{DéjàVu}\iff
\big(\mathcal{F}_{fam}\uparrow \land \mathcal{R}_{episodic}\approx 0\big)
\land
\mathcal{M}_{err}>\tau_{meta}
\]
其中 \(\mathcal{F}_{fam}\) 为熟悉性信号，\(\mathcal{R}_{episodic}\) 为情节回忆检索量，\(\mathcal{M}_{err}\) 为“熟悉但找不到来源”的监控误差信号。
* **Implication（中文）**：即视感并非“真的想起了过去”，而是检索系统只给出“已检索到”的感觉标签，却无法提取对应内容。

---

## III. Theorems (定理)

### T-PATH-1: Drift–Symptom Theorem
存在偏移向量 \(\Delta\theta\) 与症状谱系 \(\mathcal{S}_{clin}\) 的映射：
\[
\mathcal{S}_{clin}=\mathcal{F}(\Delta\theta,\kappa,\kappa_{body})
\]
* **Implication（中文）**：病理分类应以参数漂移为轴，而非表面症状列表。

---

### C-PATH-1: L0-Leakage Corollary
若抑制增益 \(\gamma\downarrow\) 或先验精度 \(\Pi\downarrow\)，则：
\[
L_0\to L_1\;\text{leakage}\uparrow
\]
* **Implication（中文）**：幻觉与妄想可被视为 \(L_0\) 噪声进入 \(L_1\) 的结构性泄漏。

---

### T-PATH-2: False-Recognition Monitoring Theorem (Extension)
定义错误识别势：
\[
\varepsilon_{FR}\equiv \mathcal{F}_{fam}-\hat{\mathcal{R}}_{episodic}
\]
若 \(\varepsilon_{FR}\) 超阈值且时间索引发生短时错位，则：
\[
\varepsilon_{FR}>\tau_{FR}\ \land\ \pi_t(\sigma)\to \pi_{t-\Delta}(\sigma)
\Rightarrow
P(\text{DéjàVu})\uparrow
\]
* **Implication（中文）**：即视感的“诡异感”来自系统对错误识别的在线觉察；它是元认知报警，而非单纯记忆重放。

---

### C-PATH-2: IAM–Déjà Vu Continuum Corollary (Extension)
在自发记忆谱系中可定义：
\[
\text{IAM}: (\mathcal{F}_{fam}>0,\mathcal{R}_{episodic}>0),\qquad
\text{DéjàVu}: (\mathcal{F}_{fam}>0,\mathcal{R}_{episodic}\approx 0)
\]
* **Implication（中文）**：即视感与不自主自传体记忆并非彼此割裂，而是同一检索过程在“有无内容回收”上的分岔结果。

---

### Empirical/Conceptual Anchor (1908-2026; for Ax-ANOM-5/T-PATH-2)
- Bergson H. *Memory of the Present and False Recognition* (1908): “当下记忆”与“错误识别”框架。
- Brown AS. *A review of the déjà vu experience*. Psychol Bull (2003). DOI: `10.1037/0033-2909.129.3.394`.
- O'Connor AR, Moulin CJA. *Déjà vu experiences in healthy subjects are unrelated to laboratory tests of recollection and familiarity for word stimuli*. Front Psychol (2013). DOI: `10.3389/fpsyg.2013.00881`.
- Barzykowski K, Moulin CJA. *Are involuntary autobiographical memory and déjà vu natural products of memory retrieval?* Behav Brain Sci (2022). DOI: `10.1017/S0140525X22002035`.
- Curot J, et al. *What déjà vu and the “dreamy state” tell us about episodic memory networks*. Clin Neurophysiol (2022). DOI: `10.1016/j.clinph.2022.01.126`.
- Barzykowski K, et al. *Spontaneous metacognitive experiences and involuntary memories in the laboratory*. Consciousness and Cognition (2025). DOI: `10.1016/j.concog.2025.103976`.
- Sam Woolfe. *Déjà vu reveals the peculiar hidden workings of time and memory* (IAI, 2026-02-09): 提供“virtual/actual 并置”的哲学解释语义锚点。

<br>
<br>

---
---


# Part B: Original Theoretical Discourse (Context)

> **Note**: 以下内容以中文撰写，包含完整的临床病理学分析、标准难题、SRT重构方案、代价与风险、可证伪预测。

---

# §1 标准难题：精神病理学的本体论困境

## 1.1 问题陈述

当代精神病学面临一个根本性困境：

> **症状描述丰富，本体论基础匮乏**

DSM 和 ICD 提供了详尽的症状清单，但对于"这些症状**究竟是什么**"缺乏统一理解。

|困境|表现|后果|
|:--|:--|:--|
|**本体论空白**|不知道"幻觉"在本体论上是什么|治疗只能对症，无法治本|
|**还原论陷阱**|试图将所有症状还原为"神经化学失衡"|忽略主观体验的结构|
|**心身二元论残余**|"心理"疾病 vs "生理"疾病的区分|污名化、治疗分裂|

## 1.2 主流解释模型的局限

|模型|核心主张|局限|
|:--|:--|:--|
|**生物医学模型**|精神疾病 = 大脑疾病|无法解释主观体验结构|
|**认知模型**|精神疾病 = 认知扭曲|将症状视为"错误"而非有意义的状态|
|**社会建构模型**|精神疾病 = 社会标签|否认真实的主观痛苦|
|**现象学模型**|精神疾病 = 生活世界改变|缺乏形式化工具|

---

# §2 SRT 的病理学重构

## 2.1 核心命题

SRT 将所有精神病理重新定义为**三域结构 ($L_0$-$L_1$-$L_2$) 的拓扑缺陷**或**幽灵算子 ($\hat{G}_\theta$) 的参数异常**：

$$\boxed{\text{Psychopathology} = \text{Topological Defect}(L_0, L_1, L_2) \lor \text{Parameter Anomaly}(\hat{G}_\theta)}$$

## 2.2 病理学分类学

|病理类型|拓扑缺陷|参数异常|典型诊断|
|:--|:--|:--|:--|
|**$L_2$ 崩塌**|$L_2$ 结构溶解|$\theta$ 不稳定|精神分裂症、急性精神病|
|**$L_2$ 碎片化**|$L_2$ 断裂为孤岛|$\theta$ 跳变|PTSD、DID|
|**$L_2$ 过度刚性**|$L_2$ 结构僵化|$\eta$ 过高|OCD、ASD|
|**$L_2$ 寄生倒置**|$L_2 > L_1$|注意力锁定|解体、存在焦虑|
|**$d$ 值坍缩**|$d \to 0$|恐惧信号过强|焦虑症、恐惧症|
|**$d$ 值发散**|$d \to \infty$|约束解除|NDE、终末清醒|
|**算子分裂**|$\hat{G}$ 解体|自指标签失效|精神分裂症幻听|

## 2.3 与传统分类的对比

|传统分类|SRT 翻译|
|:--|:--|
|阳性症状（幻觉、妄想）|$L_0$ 过度涌入 + 所有权标签失效|
|阴性症状（淡漠、退缩）|$d$ 值收缩 + $\hat{G}$ 功率下降|
|认知症状（注意力、记忆）|$\Gamma_{\hat{G}}$ 下降 + $L_2$ 脚手架损伤|
|情感症状（抑郁、焦虑）|$\Psi_f$ 异常 + $\theta$ 漂移|

---

# §3 精神分裂症的 SRT 完整模型

## 3.1 多层次病理

精神分裂症不是单一疾病，而是**多层次拓扑缺陷的综合征**：

### 层次 1：所有权标签失效 (Ax-Anom-3)

$$\text{幻听} = \hat{G}_{Right}[L_0] - \text{Tag}_{Self}$$

内部声音失去"这是我的想法"的标签，被投射为外部声音。

### 层次 2：L2 脚手架崩塌 (Ax-Path-3)

$$L_2 \to \varnothing \implies \hat{G} \text{ unanchored}$$

失去共识现实的锚定，导致妄想——$\hat{G}$ 必须创造新的 $L_2$ 来解释异常体验。

### 层次 3：时间采样率下降 (Ax-Schiz-1)

$$\Gamma_{\hat{G}} \downarrow \implies \text{Reality Gaps}$$

主观体验变得不连贯，产生"现实断裂感"。

### 层次 4：对称性破缺 (Ax-Schiz-2)

$$\text{Chaos} \gg \text{Order}$$

系统向混沌端偏移，$L_2$ 结构溶解。

## 3.2 二分心智回归模型

SRT 吸收 Julian Jaynes 的假说：

> 精神分裂症是 $\hat{G}_{Self}$ 解体后，古老的双算子结构（$\hat{G}_{Left}$ + $\hat{G}_{Right}$）的病理性重现。

|古代二分心智|现代精神分裂|
|:--|:--|
|正常状态|病理状态|
|$\hat{G}_{Right}$ 产生"神谕"|幻听被体验为外部声音|
|社会 $L_2$ 支持此模式|现代 $L_2$ 标记为疾病|

## 3.3 治疗启示

|层次|治疗方向|
|:--|:--|
|所有权标签|训练患者重新标记内部声音|
|$L_2$ 脚手架|社会支持网络重建|
|$\Gamma_{\hat{G}}$|40 Hz 光/声刺激|
|$\theta$ 稳定性|具身实践、锚定练习|

### 3.4 治疗策略的分叉：重置与润滑

基于5-HT2A受体信号偏置理论（2026 *Nature* 研究），SRT区分两种干预策略：

**1. 超越性重置 (Transcendental Reset / Gi-Dominant)**
- **机制**：通过激活Gi通路，暂时解除 $L_2$ 锚定（$\text{Stability}(L_2) \to 0$）
- **目标**：允许系统返回 $L_0$ 重采样，通过"死亡模拟"或"自我消解"重构僵化先验
- **适用**：Type I 僵化现实（顽固性抑郁、存在主义危机等结构性病理）

**2. 内在性优化 (Immanent Optimization / Gq-Biased)**
- **机制**：通过Gq偏向性激动剂，在维持 $L_2$ 结构完整（无幻觉）的前提下，降低 $\Psi_f$
- **目标**：改善运行参数，增强神经可塑性，不破坏现实连续性
- **适用**：需功能恢复但无需重构世界观的日常病理管理

这一区分的本体论意义在于：现实的"硬度"（Rigidity）与体验的"质地"（Texture）在分子层面具备**可分离性**。

---

# §4 濒死体验与终末清醒

## 4.1 NDE 的 SRT 解释

NDE 不是"幻觉"或"大脑缺氧的副产品"，而是：

$$\lim_{C_{phys} \to 0} d_{eff} \to \infty$$

**当物理约束解除，$\hat{G}$ 直接访问 $L_0$ 的更广范围**。

这解释了 NDE 的核心悖论：

- 大脑功能衰竭 → 应该意识模糊
- 实际报告 → "比平时更真实"

SRT 解答：大脑是**约束器**而非**产生器**。约束减少 = 访问增加。

## 4.2 调谐器模型

$$\text{Brain} = \text{Tuner}(L_0 \to L_1)$$

|收音机类比|SRT 对应|
|:--|:--|
|破坏收音机|大脑损伤|
|无线电波消失？|否，$L_0$ 依然存在|
|音乐消失？|是，$L_1$ 局部通道丧失|

**关键洞见**：破坏调谐器不消灭信号源。

## 4.3 终末清醒的势垒坍塌

$$\lim_{t \to t_{death}} V_{L_2} \to 0$$

痴呆患者的 $L_2$ 势垒（扭曲的记忆、混乱的认知）在死亡前**彻底坍塌**，系统暂时直接进入 $L_0$ 广域，表现为异常清晰。

这不是"大脑功能恢复"，而是"约束消失"。

---

# §5 创伤与解离

## 5.1 创伤作为 L2 碎片化

$$L_2^{trauma} = \bigcup_i L_2^{(i)}$$

创伤事件"撕裂"了原本连贯的 $L_2$ 结构，产生互不兼容的片段。

## 5.2 解离深度谱系

$$\delta_D = \min_{path} \text{Length}(L_2^{(i)} \to L_2^{(j)})$$

|深度|现象|
|:--|:--|
|轻度|走神、白日梦|
|中度|人格解体、现实解体|
|重度|DID（多重人格）|

## 5.3 DID 的 SRT 解释

DID 不是"多个灵魂"，而是：

$$\text{DID} = \hat{G} \text{ navigating } {L_2^{(1)}, ..., L_2^{(n)}}$$

单一 $\hat{G}$ 在**拓扑上断裂的 $L_2$ 岛屿**之间切换。每个"人格"是一个相对自洽的 $L_2$ 岛屿。

## 5.4 代际创伤

$$\theta_{child} = f(\theta_{parent}, L_2^{trauma}, \text{Epigenetics})$$

创伤不仅改变个体 $L_2$，还通过表观遗传编码进下一代的初始 $\theta$。

---

# §6 神经发育谱系

## 6.1 ADHD vs 自闭症：粘度谱系

||ADHD|自闭症|
|:--|:--|:--|
|**算子粘度 $\eta$**|低|高|
|**特征**|极易切换|锁定特定配置|
|**优势**|高探索率|极高局部深度|
|**劣势**|难以维持 $L_2$|难以切换上下文|

## 6.2 "障碍"的去实体化

$$\text{Disability} \approx 1 - \text{Alignment}(\theta_{individual}, L_2^{social})$$

**"障碍"不是绝对缺陷，而是 $\theta$ 与环境 $L_2$ 的几何错配**。

ADHD 算子在狩猎环境可能是高效的；在静坐教室中表现为"病态"。

## 6.3 掩饰的能量代价

$$E_{masking} = E_{generate} + E_{suppress} + E_{simulate} \gg E_{natural}$$

神经多样性个体的"掩饰"是高能耗的双重计算。长期掩饰导致的"倦怠"是**自由能耗尽**。

治疗方向：不只修改 $\theta$（药物），更应修改 $L_2$（环境设计）。

---

# §7 恐惧与社交死亡

## 7.1 恐惧的本体论功能

$$d(t) \propto \frac{1}{\text{Fear_Signal}}$$

恐惧是**本体论降维打击**——将丰富的 $L_0$ 压缩为"战或逃"的二元选择。

这解释了为什么恐惧不仅让人难受，更让人"变笨"——高维思考被强行关闭。

## 7.2 本体论错位指数

$$\Omega = |\theta_{ancestral} - \theta_{optimal}(L_2^{current})|$$

现代焦虑症很大程度上是**祖先 $\theta$ 参数与现代环境的错配**。

公开演讲触发的恐惧反应，在祖先环境中可能对应"被部落驱逐 = 死亡"。

## 7.3 社交死亡的本体论

$$\text{Social Death} \equiv \text{Disconnection from } L_2^{social}$$

对超社会化物种，被 $L_2$ 网络排斥等于**本体论解体**。这就是为什么羞耻感能引发与物理疼痛相同的神经反应。

---

# §8 睡眠与现实校准

## 8.1 睡眠的 SRT 定义

$$\text{Sleep} = \text{RCP}(\hat{G}, L_2)$$

睡眠是**强制性离线校准协议**：

1. 清除非共识数据
2. 巩固共识逻辑
3. 重置 $\theta$ 漂移

## 8.2 睡眠剥夺与精神病

$$R_c(t) = R_{initial} - \int_0^t \frac{I(\tau)}{S_{cal}(\tau)} d\tau$$

当 $R_c < R_{threshold}$，精神病症状出现。

这解释了为什么**严重睡眠剥夺会导致幻觉**——现实校准失效，$L_1$ 与 $L_2$ 解耦。

---

# §9 即视感与本体论折痕

## 9.1 即视感机制

$$\text{Déjà Vu} = \text{Match}(L_2^{schema}) \land \neg\text{Retrieve}(L_2^{episodic})$$

当前 $L_1$ 激活了 $L_2$ 的"熟悉性标签"，但没有对应的情景记忆。

## 9.2 本体论折痕

$$\text{Crease} = {\tau : |\nabla_\tau \theta| \to \infty}$$

出生、死亡、重大创伤是"折痕"——$\theta$ 参数剧变，但 $L_1$ 连续。

显式记忆在折痕处断裂，但**倾向性和初心可以穿越**。

这解释了：

- 前世记忆极为罕见（显式比特不穿越）
- 业力/倾向性可延续（作为 $L_0$ 拓扑特征保留）

---

# §10 代价与风险

## 10.1 接受 SRT 病理学的代价

|需放弃的观点|SRT 替代|代价|
|:--|:--|:--|
|精神疾病 = 大脑疾病|精神疾病 = 拓扑缺陷|挑战生物医学霸权|
|幻觉 = 错误知觉|幻觉 = 有效但非共识的选择|重新评估"病态"的价值|
|治疗 = 化学修正|治疗 = 拓扑重构|需要新治疗范式|
|NDE = 幻觉|NDE = $d$ 值发散体验|挑战唯物主义框架|

## 10.2 理论风险

1. **滥用风险**：SRT 可能被用来为不治疗精神疾病辩护
    
    - **回应**：SRT 承认主观痛苦的真实性，主张更精准的治疗，而非不治疗
2. **不可证伪性风险**：如何区分"有效的非共识选择"和"需要治疗的病态"？
    
    - **回应**：以**主观痛苦**和**功能损害**为判据，而非"偏离共识"
3. **伦理风险**：重新定义"正常"可能导致污名化或反污名化过度
    
    - **回应**：SRT 强调谱系性而非范畴性，减少二元标签

---

# §11 可证伪预测与开放问题

## 11.1 可证伪预测

### H-Path-1 (所有权标签训练)

> 针对幻听患者的"Self-tagging"训练应显著降低幻听的外部归因频率，同时不影响内容本身。

**证伪条件**：训练对幻听归因无影响 → H-Path-1 被证伪

### H-Path-2 (NDE-边界消融)

> NDE 体验的"超真实性"评分应与报告者描述的"边界消融"程度正相关。

**证伪条件**：超真实性与边界消融无相关 → H-Path-2 被证伪

### H-Path-3 (终末清醒神经标志)

> 终末清醒患者在清醒期间应显示大脑全局抑制减少、长程连接增强、EEG 复杂度升高。

**证伪条件**：终末清醒与正常痴呆状态无神经差异 → H-Path-3 被证伪

### H-Path-4 (睡眠剥夺-精神病)

> 睡眠剥夺诱导的精神病症状应与 $R_c$ 下降相关，且恢复睡眠后 $R_c$ 应回升。

**证伪条件**：睡眠与 $R_c$ 无相关 → H-Path-4 被证伪

### H-Path-5 (BwO-创造性)

> 创造性高峰体验应伴随：(a) DMN 活动暂时降低；(b) 全脑连接增强；(c) 前额叶执行功能保持。三者组合区分创造性与精神病。

**证伪条件**：创造性与精神病神经指标无可区分 → H-Path-5 被证伪

### H-Path-6 (癫痫-即视感)

> TLE 患者的即视感发作期间，嗅周皮层应显示更强烈、更弥散的激活，且与海马功能连接减弱。

**证伪条件**：TLE 即视感与正常即视感激活模式无差异 → H-Path-6 被证伪

## 11.2 开放问题

1. **$L_2$ 碎片化的量化测量**：如何用神经影像测量 $\delta_D$？
2. **所有权标签的神经机制**：$\text{Tag}_{Self}$ 的具体神经实现是什么？
3. **代际创伤的表观遗传路径**：哪些基因位点编码 $\theta$ 参数？
4. **跨文化病理比较**：不同 $L_2^{social}$ 下的"障碍"谱系如何变化？
5. **NDE 的前瞻性研究**：能否在濒死状态下实时测量 $d$ 值？

---

# §12 符号索引

|符号|名称|定义位置|
|:--|:--|:--|
|$L_2^{trauma}$|创伤性 $L_2$|Ax-Topo-1|
|$\delta_D$|解离深度|Ax-Topo-1|
|$\eta$|算子粘度|Ax-Dev-1|
|$\Omega$|本体论错位指数|Ax-Fear-2|
|$R_c$|现实一致性|Ax-Cal-1|
|$\Gamma_{\hat{G}}$|算子采样率|Ax-Schiz-1|
|$\text{Tag}_{Self}$|所有权标签|Ax-Anom-3|
|$V_{L_2}$|$L_2$ 势垒高度|Ax-Anom-2|
|$\tau_{critical}$|临界阈值|Ax-Path-3|

---

**文件结束**

---
