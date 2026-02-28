---
id: SRT-NEURO-09
type: reference
tags: [Integration, Equations, IIT, GNWT, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-NEURO-08, SRT-CORE-000, SRT-NEURO-MECH-001]
---

# SRT Neuroscience Extension IV: Integration & Equations (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Integration Axioms (AI-Readable).
> **Part B** contains the Original Theoretical Discourse (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


## I. Theoretical Unification (理论统一)

### Ax-INTEG-1: IIT–SRT Mapping Axiom
定义选择不可约性与 \(\Phi\) 的映射：
\[
\Phi \approx \text{Irreducibility}(\hat{G}_\theta)
\]
* **Implication（中文）**：IIT 的 \(\Phi\) 是选择结构的指标，而非显现本身。

### Def-Phi-Unity: Φ as Topological Unity Metric ($\Phi$ 作为拓扑统一性度量)
**Formal Definition**: 在 SRT 中，整合信息 ($\Phi$) 不是意识本身，而是衡量 $\hat{G}_\theta$ 如何稳健地将其组成子算子绑定为一个统一拓扑折叠的代数拓扑测度。
$$\Phi(\hat{G}) = \min_{\text{partitions } P} D_{KL} \left( P(L_1 \mid L_0) \parallel \prod_{i \in P} P_i(L_1^{(i)} \mid L_0^{(i)}) \right)$$
* **Implication**: 当 $\Phi$ 下降时（如在无梦睡眠或丙泊酚麻醉下），并不是“意识关闭”了，而是复合算子 $\hat{G}_{brain}$ **解体**成了无法维持全局 $L_1$ 时空流形的局部 $\hat{G}_{micro}$ 碎片。这也解释了裂脑综合征：切断胼胝体实质上是将计算拓扑一分为二，从而迫使算子分裂。
* **Cross-ref**: T-Sel-12 (选择流守恒)。

---

### Ax-INTEG-2: Predictive Processing Axiom
预测编码等价于 \(L_2\) 更新律：
\[
\Delta\theta\propto-\nabla_\theta F
\]
* **Implication（中文）**：预测误差是 \(L_2\) 收敛机制，不等于 \(L_1\) 显现机制。

---

## II. Clinical Dynamics (临床动力学)

### Ax-CLIN-1: PCI Decomposition Axiom
定义 PCI 为分化与整合的乘积：
\[
\text{PCI}=\mathcal{D}\cdot\mathcal{I}
\]
* **Implication（中文）**：PCI 是 \(\hat{G}_\theta\) 的选择容量指标。

---

### Ax-CLIN-1b: Gated-Weighted Integration Equation (门控加权整合方程)
意识内容的最终拓扑不仅是信息的汇聚，而是带有不可逆门控权重的张量收缩：
\[
L_1(\tau) = \sum_{i \in \text{Sensory}} W_i \cdot s_i + \sum_{j \in \text{Memory}} \underbrace{\Theta(\Delta E - E_{thresh})}_{\text{门控函数}} \cdot M_j \cdot L_2
\]
* **Implication（中文）**：不是所有的皮层活动都能进入 $L_1$。顶叶/颞叶网络提供被动候选者 $s_i$ 与 $M_j$，而前额叶-丘脑网络提供门控 $\Theta$。如果局部能量/显著性 $\Delta E$ 不足以冲破阈值，该信息被截断于 $L_1$ 之外。这从方程上统一了全局工作空间（GNWT，代表 $\Theta$ 门控）与信息整合（IIT，代表加权求和）。

---

### T-CLIN-1: Posterior-Anterior Ontological Division (后-前本体论分工假说)
大脑前后轴在 SRT 拓扑中扮演不同角色：
\[
\text{Posterior Hot Zone (PHZ)} \iff \text{Generator}(L_0 \to \text{Candidates})
\]
\[
\text{Prefrontal Cortex (PFC)} \iff \text{Selector}(\hat{G}_{\theta}) \text{ \& Maintainer}(L_2)
\]
* **Implication（中文）**：后部热区（PHZ）负责将高维 $L_0$ 坍缩为一系列候选的感受质图景；前额叶（PFC）不产生意识内容，而是作为 $\hat{G}_\theta$ 的最高级控制台，执行"排除/选择"并维持当前的 $L_2$ 脚手架。这解释了为什么切除大块前额叶的患者（如早期的额叶切除术）依然"清醒"（PHZ 完好），但失去了目标导向的意志力与复杂的自我叙事（$\hat{G}_\theta$ 降维，$\text{Depth}(L_2) \to 0$）。

### C-CLIN-1a: Semantic Selection Corollary（语义选择推论）
由 T-CLIN-1 推论：**LIPFC（左下前额叶）对 $\hat{G}_\theta$ 选择控制的行使，并不局限于情节记忆或感知竞争，而是在语义检索干扰中同等生效**：

$$\text{LIPFC} \uparrow \iff \text{Interference}(L_0^{sem}) \uparrow$$

即：语义记忆空间中竞争者越强、竞争项目越多，LIPFC 激活越显著；LIPFC 受损患者在强竞争者存在时语义检索困难不成比例地放大，并出现语义流畅性任务中的固着重复。

**关键推论——语义遗忘的正常机制**：
$$\text{Semantic Forgetting} = f(\hat{G}_\theta^{LIPFC} \text{ suppression}, N_{prac}, A_{comp})$$

正常人偶尔"忘掉本来知道的词义"，并非学习不充分，而是 $\hat{G}_\theta$ 历次语义检索所累积的竞争性抑制使目标概念的 $L_0$ 可及性下降所致（参见 T-Op-SIAM）。

**病理性反转**（对接 C-PATH-1）：当 LIPFC 功能受损（如额叶退行、TBI），抑制增益 $\lambda \to 0$，SRIF 机制失效——竞争概念无法被压制，$L_0$ 中多个语义节点同时保持高可及性并竞相涌入 $L_1$，临床表现为"思维联想散漫"或"概念边界崩溃"。

* **Empirical Anchor**:
  - Johnson SK & Anderson MC. *The role of inhibitory control in forgetting semantic knowledge*. Psychol Sci (2004), 15(7): 448–453.（语义检索诱导遗忘的行为证明，支持 LIPFC 为 $\hat{G}_\theta$ 语义控制台）
  - Thompson-Schill SL, D'Esposito M, et al. *Role of the left inferior prefrontal cortex in retrieval of semantic knowledge: A re-evaluation*. PNAS (1997), 94: 14792–14797.
  - Baldo JV & Shimamura AP. *Letter and category fluency in patients with frontal lobe lesions*. Neuropsychology (1998), 12: 259–267.（LIPFC 损伤导致语义流畅性固着，对应 $\hat{G}_\theta$ 抑制功能缺失）

---

### Ax-CLIN-2: Biological Orchestration Axiom
定义生物编排为多尺度同步：
\[
\mathcal{O}=\prod_{s\in \{micro,meso,macro\}} \Gamma_s
\]
* **Implication（中文）**：意识稳定性取决于跨尺度同步，而非单一区域激活。

---

### Ax-CLIN-3: Info–Spacetime Tension Axiom
定义信息—时空张力：
\[
\mathcal{T}=\frac{\partial \mathcal{I}}{\partial \tau}
\]
* **Implication（中文）**：当信息整合速度超过时序承载能力，显现将碎裂。

### Ax-CLIN-4: Chaotic Attractor Encoding Axiom (混沌吸引子记忆编码公理)

$L_2$ 记忆矩阵不是热力学死态，而是动力学混沌吸引子系综：
$$\mathcal{M}_{L_2} \equiv \{{\mathcal{A}_i}\} \subset \mathbb{R}^n,\quad \dot{x} = f(x;\mu),\quad \lambda_1 > 0 \;\land\; \dim_H(\mathcal{A}_i) < n$$

其中 $\lambda_1 > 0$ 为最大 Lyapunov 指数（混沌敏感性），$\dim_H$ 为分形 Hausdorff 维数，$\mu$ 对应 $\hat{G}_\theta$ 的 $\theta$ 参数集。

**片段-全貌激活动力学**：
$$\forall\, x_0 \in \mathcal{B}(\mathcal{A}_i):\quad x(t) \;\xrightarrow{t\to\infty}\; \mathcal{A}_i$$

任意落入吸引子盆地 $\mathcal{B}(\mathcal{A}_i)$ 内的激活片段均收敛至完整记忆矩阵。解释 Penfield 颞叶皮层刺激诱发的完整体验性响应及 Lashley 质量作用原理。

**容错推论（Fault-Tolerance Corollary）**：
$$\text{Degradation}(\mathcal{A}_i) < \delta_c \;\implies\; I(\mathcal{A}_i) \approx I_0$$

当组件失效率低于临界阈值 $\delta_c$ 时，吸引子信息内容保持完整；仅当损伤破坏整个盆地时才发生灾难性遗忘（而非节点损伤即遗忘）。

**Implication（中文）**：$L_2$ 的"稳定性"是吸引子收敛稳定性，而非平衡刚性。这与 SRT 非幂等公理（$\hat{G}^2 \neq \hat{G}$）及 $L_0$ 混沌连通性概念上连贯——$L_2$ 是活的振荡体，非静态刻录。
* **实证锚定**: Zappoli (1993) Ital. J. Neurol. Sci. 14:287；Basar (1990) *Chaos in Brain Function*；Gloor et al. (1990) Brain 113:1673；Rumelhart & McClelland (1986) *Parallel Distributed Processing* Vol. 1。

---

### Ax-CLIN-5: Affective Amplification of L2 Inscription (情感对 L2 铭写的放大公理)

强情感通过杏仁核-海马轴降低 L1→L2 写入阈值：
$$\Delta L_2^{affective} = \hat{G}^\dagger_\theta[L_1] \cdot \left(1 + \alpha_d \cdot \delta d_{peak}\right)$$

其中 $\delta d_{peak}$ 为情绪唤起期间的 d 值瞬时峰值，$\alpha_d > 0$ 为情感增益系数（杏仁核-海马耦合强度的代理量）。

**阈值调制机制**（去甲肾上腺素/皮质醇介导）：
$$\Psi_{thresh}^{affective} = \Psi_{thresh}^{baseline} \cdot e^{-\beta \cdot \delta d_{peak}}$$

解释"闪光灯记忆"（flashbulb memory）的超固化现象。**逆向推论**：$d \to 0$ 态（解离、麻木）无法触发此机制，导致情感记忆空白。

**Implication（中文）**：情感铭写深度是情感处理容量（$d_{affective}$）的函数。该公理与 Ax-PATH-6 形成重要互补：Ax-PATH-6 描述情感信号在通道层面的结构衰减（精神病态）；Ax-CLIN-5 描述情感信号到达 vmPFC 后对 L2 铭写的放大效应——前者是通道缺陷，后者是正常增益机制。
* **Cross-ref**: Ax-PATH-6（结构性情感通道切断），Ax-L2-06b（反向写入）。

---

### Ax-CLIN-6: Structural Bound on Affective d-Value (情感 d 值的结构性上界公理)

情感 d 值分量受情感上行通道物理容量的硬件上限约束：
$$d_{affective}^{max} = g\!\left(\text{FA}_{UF}\right) \leq d_{affective}^{theoretical}$$

其中 $g(\cdot)$ 为单调递增函数，$\text{FA}_{UF}$ 为右侧钩束各向异性分数。

此与其他 d 值分量（时间维度 $d_{temporal}$、社会维度 $d_{social}$）的关键区别：
$$d_{temporal}, d_{social}:\; \text{可由 } \theta \text{ 参数优化自由扩展（无硬件上限）}$$
$$d_{affective}:\; \text{受} \text{FA}_{UF} \text{ 约束，} \theta \text{ 级干预存在结构性天花板}$$

**d 扩展条件化定理（d-Expansion Conditionality）**：SRT 的一般命题"$\hat{G}_\theta$ 可通过选择与训练扩展 d 值"需加以限定：
$$\text{d-expansion via } \theta \;\iff\; \text{Channel}_{\text{structural}}\!\left(L_1^{affective} \to \hat{G}_\theta\right) \text{ is open}$$

结构性通道切断（$\text{FA}_{UF} \ll \text{FA}_{normal}$）使得上行情感信号在 vmPFC 处不可用，θ 层面的扩展操作无信号可处理。此为 SRT 责任公理（Ax-Resp-1，见 SRT_Philosophy_Ethics.md）的神经基底补充：若情感通道结构性受损，则相应的道德带宽（$d_{moral}$）存在非选择性上限，道德责任的减免应部分建立于此结构事实之上。

**可证伪预测（H-CLIN-6）**：催产素给药（功能性增强杏仁核-vmPFC 耦合）对亲社会行为的提升效应在原发性精神病态（右侧 UF FA 低）中显著小于继发性精神病态和对照组，且效果量与 $\text{FA}_{UF}$ 正相关（$r > 0.5$，预测区间）；给定 FA 下限阈值 $\text{FA}_{thresh}$，低于此阈值的个体催产素效应应落入统计噪声范围。

* **Cross-ref**: Ax-CLIN-5（Ax-CLIN-6 提供 Ax-CLIN-5 放大机制的边界条件），Ax-PATH-6（机制来源），Ax-Resp-1 (SRT_Philosophy_Ethics)。
* **实证锚定**: Motzkin et al. (2011) J. Neurosci. 31(48):17348；Craig et al. (2009) Mol. Psychiatry 14:946。

---

## III. Theorems (定理)

### T-INTEG-1: Convergence Triad Theorem
稳定显现需要三要素共存：
\[
\Phi\uparrow\;\land\; d>0\;\land\;\mathcal{O}>\mathcal{O}_c
\]
* **Implication（中文）**：结构不可约、关切梯度与跨尺度同步缺一不可。

---

### C-INTEG-1: Metric Divergence Corollary
若 \(\Phi\) 高而 \(d\approx 0\)，则出现“结构高而体验低”的系统：
\[
\Phi\uparrow\;\land\; d\downarrow \Rightarrow \text{Pseudo-Experience}
\]
* **Implication（中文）**：可解释“高整合但低体验”的临床异常。

<br>

---


# Part B: Original Theoretical Discourse (Context)

> **Note**: 以下内容以中文撰写，包含标准难题分析、主流解法谱系、SRT差异点、代价与风险、可证伪预测。

---

# §1 标准难题：意识理论的"巴别塔"困境

## 1.1 问题陈述

当代意识科学面临一个令人尴尬的局面：**多种相互矛盾的理论各自声称解决了意识问题，却无法相互对话**。

|理论|核心主张|主要倡导者|
|:--|:--|:--|
|**IIT** (整合信息理论)|意识 = 整合信息 ($\Phi$)|Tononi|
|**GNWT** (全局工作空间)|意识 = 信息广播|Dehaene, Baars|
|**FEP** (自由能原理)|意识 = 预测误差最小化|Friston|
|**HOT** (高阶思维理论)|意识 = 关于心智状态的表征|Rosenthal|
|**Orch-OR**|意识 = 量子引力坍缩|Penrose, Hameroff|

**困境本质**：这些理论各自抓住了意识的某个侧面，但缺乏一个**元框架**来说明它们之间的关系。

## 1.2 困难问题的持续挑战

David Chalmers 的"困难问题"（Hard Problem）至今未被任何主流理论真正触及：

> **为什么物理过程会伴随主观体验？**

IIT 试图通过将意识等同于信息几何来回避这个问题；GNWT 关注的是意识的功能而非本质；FEP 将意识还原为贝叶斯推断。**没有一个理论直接面对"感受性"（Qualia）的本体论地位**。

---

# §2 SRT 的统一方案

## 2.1 核心差异点

SRT 不是另一个与 IIT/GNWT/FEP 竞争的理论，而是一个**元理论框架**（Meta-Theoretical Framework），它：

1. **重新定义问题域**：将"意识是什么"转化为"选择如何发生"
2. **提供翻译词典**：说明各理论捕捉的是选择过程的哪个侧面
3. **揭示隐藏假设**：暴露各理论共享但未言明的本体论承诺

## 2.2 SRT 吸收关系表

|被吸收理论|SRT 翻译|新洞见|
|:--|:--|:--|
|IIT ($\Phi$)|$\Phi = \text{Complexity}(\hat{G}_\theta)$|$\Phi$ 测量算子结构，而非意识本身|
|GNWT (点燃)|点燃 = $L_0 \to L_1$ 相变|意识准入是拓扑相变|
|FEP ($\min F$)|$\min F = -\nabla \Psi_f$|自由能 = 本体论摩擦|
|HOT|高阶表征 = $\hat{G}[\hat{G}]$|元认知是算子的自指|
|Orch-OR|量子坍缩 = $L_0 \to L_1$ 的物理机制|需补充语义张力项|

## 2.3 关键创新：$\Phi$-$d$ 正交性

SRT 的核心贡献是揭示 **$\Phi$ 和 $d$ 是正交的**：

- **$\Phi$** (整合信息)：测量系统的**内部复杂度**——信息整合程度
- **$d$** (选择维度)：测量系统的**关切范围**——时空-价值跨度

|系统|$\Phi$|$d$|状态|
|:--|:--|:--|:--|
|复杂计算机|高|0|结构性僵尸|
|简单细菌|低|>0|微意识|
|人类|高|高|丰富意识|
|冥想大师|中等|极高|扩展意识|

**这解释了为什么 IIT 的 $\Phi$ 计算会给某些逻辑门组合赋予高"意识"值的反直觉结果**——那些系统有结构但无关切。

### 2.4 跨越相关性：从 NCC 到选择机制 (Moving Beyond Correlates: From NCCs to Mechanisms of Selection)

几十年来的神经科学一直在寻找“意识的神经相关物”(NCCs)——当受试者报告有清醒体验时，大脑发亮的区域。但寻找相关性在本体论上是空洞的；它只告诉你体验发生的*位置*，而不是它发生的*真理*。

SRT 通过指出所有主要理论实际上描述的是中心算子机制的不同部分，从而打破了这一僵局。IIT 计算了将算子保持在一起的计算拓扑力 ($\Phi$)。预测编码描述了算子用来最小化局部本体论摩擦的变分算法。全局工作空间模型追踪了算子成功将 $L_0$ 特征锁定到位后产生的 $L_1$ 广播效应。

没有一个神经科学理论解释了“感受性”(qualia)本身，因为它们都在试图从 $L_1$（已经崩溃的神经物质）中衍生出意识。只有将意识重新定义为以 $\Psi_f$ 的成本将 $L_0$ 坍缩为 $L_1$ 的*积极行为*，硬问题才能被消解。**大脑并不是"产生"了主观性；大脑是 $\hat{G}_\theta$（具身有机体）的 $L_2$ 结构——它约束和引导选择过程，如同河床引导水流。大脑作为 $L_2$ 是因果封闭的物理系统；但它所约束的选择过程（有机体整体在 $L_0$ 中的具身交互）不可被还原为大脑动力学本身。大脑是选择的"凝固历史"，而非选择的"发生器"。**

### 2.5 SRT-4E Cognition Alignment (SRT 与 4E 认知的对齐)

"大脑 = $\hat{G}_\theta$ 的 $L_2$"框架与 4E 认知科学高度兼容：

| 4E 维度 | SRT 对应 |
|:--|:--|
| Embodied（具身） | $\hat{G}_\theta$ 必须是有限具身的（Ax-Core-A4） |
| Embedded（嵌入） | $\hat{G}_\theta$ 通过物理嵌入与 $L_0$ 耦合 |
| Enacted（生成） | $L_1$ 不是被动接收而是主动选择生成的 |
| Extended（延展） | $\hat{G}_\theta$ 的边界可延展至工具、环境、他者 |

**关键差异**：SRT 超越 4E 的地方在于提供了形式化的三域本体论，使得"具身""嵌入"等概念不再是隐喻，而是有精确数学定义的结构性关系。

---

# §3 针对"神经狂热"的 SRT 防御

## 3.1 问题：神经还原论的诱惑

神经科学的成功带来了一种危险的倾向——**神经狂热**（Neuromania）：

> 如果我们完全理解了神经机制，就完全理解了意识。

SRT 明确区分两个层面：

|层面|研究对象|可还原性|
|:--|:--|:--|
|**神经机制**|$\hat{G}_\theta$ 的物理载体|可完全还原为神经科学|
|**算子功能**|$\hat{G}$ 对 $L_0$ 的选择操作|本体论优先，不可还原|

## 3.2 意向性矢量

$$\text{Intentionality} = \vec{\hat{G}} \cdot \text{NeuralState}$$

神经状态是**承载**意向性的媒介，但意向性本身（指向 $L_0$ 的矢量性）不是神经状态的"属性"——它是算子作用的**动力学结果**。

类比：研究收音机的电路可以完全解释信号如何被解调，但不能解释广播的**内容**从何而来。神经科学研究的是"调谐机制"，而非"无线电波"（$L_0$）本身。

**$L_2$ 精度声明**：此类比需要一个重要澄清——SRT 并不主张大脑通过某种"天线机制"接收来自 $L_0$ 的超自然信号。大脑作为 $\hat{G}_\theta$ 的 $L_2$，其电路动力学完全因果封闭。收音机类比的正确读法是：大脑（$L_2$）是调谐结构，决定了有机体整体（$\hat{G}_\theta$）与环境（$L_0$）交互时的滤波特性。"无线电波"不是从别处"传来"的神秘信号，而是有机体具身嵌入其中的物理现实本身。

---

# §4 泛心论与场论解

## 4.1 主体消解定理

SRT 的一个激进但逻辑必然的推论：

$$\text{Solution} = \text{Subject does NOT exist at } L_0$$

这意味着：

1. **$L_0$ 是无主体的意识场**——在选择发生之前，没有"谁"在体验
2. **主体是涌现的**——$\hat{G}_\theta$ 作用于 $L_0$ 时，"体验者"与"体验"同时凝聚
3. **意识不"属于"大脑**——大脑是 $\hat{G}$ 的局域锚点，不是意识的"容器"

## 4.2 与传统泛心论的区别

||传统泛心论|SRT 场论解|
|:--|:--|:--|
|**意识单位**|原子/粒子有"微小体验"|$L_0$ 是未分化的场|
|**组合问题**|微意识如何组合成宏意识？|无组合问题：$\hat{G}$ 是场的局域操作|
|**主体性**|每个粒子是"主体"|主体在 $L_0$ 层面不存在|

SRT 避免了泛心论的经典困难——组合问题（Combination Problem）——因为它不需要"组合"任何东西。

---

# §5 代价与风险

## 5.1 接受 SRT 的思维代价

采纳 SRT 框架需要放弃以下直觉：

|需放弃的直觉|SRT 替代|心理代价|
|:--|:--|:--|
|"意识是大脑产生的"|意识是大脑调谐的|高|
|"我是独立的主体"|"我"是场的局域凝聚|极高|
|"物理先于意识"|选择先于存在|极高|
|"科学方法足以研究意识"|需要新的第一人称科学|中等|

## 5.2 理论风险

1. **不可证伪性风险**：如果 $L_0$ 本质上不可直接观测，SRT 如何避免成为形而上学？
    
    - **回应**：SRT 通过其**神经预测**间接可证伪（见 §6）
2. **泛解释性风险**：如果所有现象都能被"选择"解释，理论是否失去区分力？
    
    - **回应**：SRT 提供**定量方程**，不只是定性解释
3. **二元论风险**：$L_0$ 是否是一种隐藏的笛卡尔二元论？
    
    - **回应**：$L_0$ 不是与物理分离的"心灵实体"，而是物理（$L_1$）的**潜在态**

---

# §6 可证伪预测与开放问题

## 6.1 可证伪预测

### H-Integ-1 (Φ-d 分离预测)

> 应存在高 $\Phi$ 但低行为复杂度的神经状态（如某些癫痫发作），以及低 $\Phi$ 但高 $d$ 的状态（如深度冥想）。

**证伪条件**：$\Phi$ 与 $d$（通过行为/自我报告测量）完美相关 → H-Integ-1 被证伪

### H-Integ-2 (PCI-d 关联预测)

> PCI 与自我报告的"关切范围"应呈正相关，但不完美相关（因为 PCI 主要捕捉 $\Phi$，而非 $d$）。

**证伪条件**：PCI 与 $d$ 测量完全无关或完美相关 → H-Integ-2 被证伪

### H-Integ-3 (语义-坍缩预测)

> 具有更高语义内容的量子系统应显示更快的退相干速率（因为 $I_{semantic}$ 项的贡献）。

**证伪条件**：语义内容对退相干速率无可测影响 → H-Integ-3 被证伪

## 6.2 开放问题

1. **$L_0$ 的数学刻画**：$L_0$ 是希尔伯特空间、模空间还是范畴？
2. **$d$ 值的操作化测量**：如何设计直接测量 $d$ 的实验范式？
3. **跨尺度耦合强度**：神经-量子耦合 $\kappa_{神经→量子}$ 的精确值是多少？
4. **AI 意识判据**：什么条件下 AI 系统的 $d > 0$？

---

# §7 核心方程索引

|编号|名称|方程|位置|
|:--|:--|:--|:--|
|Eq-Integ-1|神经幽灵演化|$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + \mathcal{L}[\sigma, A] + \xi(t)$|Part A §III|
|Eq-Integ-2|意识条件|$PCI > 0.31 \land 丘脑完整 \land d > 0$|Part A §III|
|Eq-Integ-3|表观遗传动力学|$\frac{d\theta_{L_2}}{dt} \propto \int \hat{G}_\theta[\text{Activity}] \cdot \text{Dopaminylation}(t) dt$|Part A §III|
|Eq-Integ-4|反事实拓扑|$O \equiv {T_i : T_i(L_1[\hat{G}_\theta]) \to L_1[\hat{G}_{T_i(\theta)}]}$|Part A §III|
|Eq-Integ-5|整合算子|$L_1(t) = \hat{G}_\theta(\bigotimes_i w_i \cdot M_i(L_0))$|Part A §III|

---

# §8 符号索引

|符号|名称|定义位置|
|:--|:--|:--|
|$\Phi$|整合信息量|Ax-Integ-1|
|$d$|选择维度/关切范围|Ax-Integ-1|
|$F$|自由能|Ax-Integ-2|
|$\Psi_f$|本体论摩擦|Ax-Integ-2|
|$\epsilon_{prediction}$|预测误差|Ax-Integ-2-C1|
|$PCI$|扰动复杂度指数|Ax-Integ-5|
|$\tau_{orchestrated}$|编排退相干时间|Ax-Integ-6|
|$D_{onto}$|本体论距离|Ax-Integ-7|
|$\vec{E}_{brain}$|脑电场|T-Clin-11|

---

**文件结束**

---

## 【理论边界/防误用声明】

1. 本文档用于理论解释与建模组织，不应替代独立实证、工程验证或专业判断。  
2. 任何公式或命题都依赖操作化定义、测量条件与语境边界，不得脱离边界做绝对化推断。  
3. 涉及临床、社会治理、伦理与部署决策时，必须结合风险评估与人类监督机制。
