---
id: SRT-NEURO-MECH-001
type: theory
tags: [Neuroscience, Mechanisms, Ghost-Operator, Hybrid]
status: axiomatic_hybrid_v2
layer: L1
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-000, SRT-NEURO-AXIOMS-001, Core_Law/SRT_Reference_Axioms, Core_Law/SRT_Reference_Ontology, Core_Law/SRT_Reference_Dynamics]
---

# SRT Neural Mechanisms: Axiomatic Derivations & Dynamics

> **Connector-safe reading path**: This owner file is long and may be truncated by GitHub-style connectors. For connector reads, start with [`Neural_Mechanisms_Split/README.md`](Neural_Mechanisms_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

> **Version 2.0 (Hybrid)**
> **Part A** presents the Formal Axioms (AI-Readable).
> **Part B** contains the Expanded Theoretical Discourse (Human-Readable Context).

---


## Quick Reference
- Role: Main neuroscience mechanisms expansion layer for neural dynamics under SRT.
- Core claim: Maps SRT selection dynamics into neural state-space, ignition, attractor, and systems-level mechanism language.
- Canonical status: Canonical expansion layer within neuroscience; not a replacement for core canonical definitions.
- Depends on: `SRT-CORE-000`, `SRT-NEURO-AXIOMS-001`, `Core_Law/SRT_Reference_Axioms`, `Core_Law/SRT_Reference_Ontology`, `Core_Law/SRT_Reference_Dynamics`, `_SRT_SYMBOL_TABLE.md`.
- Used by: neuroscience compact core, consciousness mechanisms, experiment discussion, and bridge interpretation.
- Safe edits: Typo fixes, link fixes, Quick Reference updates, and non-semantic clarification of mechanism summaries.
- Do not change: Neural mechanism claims that depend on canonical core terms or rewrite d / `Ψ_f` ownership without cross-checking the symbol table and upstream canonical files.

## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
- 本文件中的 candidate activation、competitive inhibition、divisive normalization、ignition / global availability 与 plastic writeback 是 neural-computational implementation proxies；它们不替代 `\hat{G}_\theta`、`L_1`、`L_2` 或 `\Psi_f` 的 core / canonical 定义。详见 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B12`。

## Current Reading Map

- **Canonical dependencies**: `Core_Law/SRT_Reference_Axioms`, `Core_Law/SRT_Reference_Ontology`, `Core_Law/SRT_Reference_Dynamics`, `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md`.
- **Primary SRT claims in this file**: Neural state-space axioms (Ax-NEURO-MECH-1 through Ax-NEURO-MECH-N); L0→L1 projection as ignition; attractor dynamics and L2 plastic writeback; d-value gradient coupling in neural context.
- **Bridge/interface sections in this file (Part B)**: Comparisons with IIT, GWT (Dehaene), predictive processing, and lateral inhibition models. These sections are **future Annex extraction candidates** for PR-B (Neuroscience_Annex/). Do not move them in this PR.
- **Do not move in this PR**: All Ax-NEURO-MECH-* axioms; all formulas involving `Ψ_f`, `Ĝ_θ`, `d-value`; ignition threshold definitions; attractor stability claims.

## Dependency Map

| Depends on | Purpose | Move risk |
|---|---|---|
| `Core_Law/SRT_Reference_Axioms` | upstream canonical axiom source | High — do not inline |
| `Core_Law/SRT_Reference_Ontology` | L0/L1/L2 canonical ontology | High — do not inline |
| `Core_Law/SRT_Reference_Dynamics` | selection dynamics formalism | High — do not inline |
| `_SRT_D_VALUE_CANONICAL.md` | d-value definition anchor | High — do not inline |
| `_SRT_PSI_F_CANONICAL.md` | Ψ_f definition anchor | High — do not inline |
| `Neuroscience/_SRT_Neuro_Axioms.md` | neuroscience axiom base | Medium — read before editing |
| `Core/SRT_Core_21c_Bridge_Hypotheses.md` | bridge hypothesis claim register | Medium |

## Companion Links

- [`Operations/Non_Philosophy_Refactor_Audit_Report.md`](../Operations/Non_Philosophy_Refactor_Audit_Report.md) — domain-level refactor plan
- [`Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`](SRT_Neural_Mechanisms_CompactCore.md) — compact navigation entry
- [`Neuroscience/SRT_Neuro_Predictions_Table.md`](SRT_Neuro_Predictions_Table.md) — empirical prediction register
- [`Neuroscience/SRT_Consciousness_Mechanisms.md`](SRT_Consciousness_Mechanisms.md) — consciousness mechanisms owner file

## Refactor Notes (PR-A: navigation-only)

- Navigation-only update. No formulas changed. No theory content changed.
- Part B external-theory comparison sections (IIT, GWT, predictive processing, lateral inhibition) are **PR-B candidates** for extraction to `Neuroscience_Annex/`. They must not be moved without a separate human-reviewed PR.
- The CompactCore file (`SRT_Neural_Mechanisms_CompactCore.md`) is already hardened and should not be modified.

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

### Large-Scale Phase-Dominance patch (eLife 2026, 2026-04-14, Pipeline 1)
这条材料真正补上的，不是“皮层里存在行进波”这种旧话，而是把一个更底层的尺度约束压稳：**从 delta 到 high gamma，皮层相位动力学的空间功率峰值都落在最低空间频率，也就是最长波长、最大尺度的一侧。**

- 用户提交的是 eLife 原始研究 `The dominance of large-scale phase dynamics in human cortex, from delta to gamma`（Alexander & Dugué, 2026；doi:`10.7554/eLife.100674.4`）。该文利用 `23` 名受试者的 gray-matter sEEG、延迟自由回忆任务中的局部场电位，以及对不规则采样阵列做线性代数补偿的方法，直接估计皮层相位动力学的 spatial frequency spectrum。

- 这条材料最值得吸收的新增量，不是重复“存在 global waves”，而是把 `\sigma(t)\in\mathcal M` 的底层组织进一步收紧成一个 **low-spatial-frequency-dominant phase regime**。文中报告：phase 的 spatial power 在最低 spatial frequencies 最高，且这一趋势横跨 delta（1-3 Hz）到 high gamma（60-100 Hz），可追到约 `8–16 cm` 的 cortical extent。更稳的神经机制写法因此不是“局部相位图偶尔会被全局波同步”，而是**局部相位本就嵌在以长波长为主导的全皮层组织里**。

- 可将频段分辨的相位空间谱写成：
\[
P_\phi(k,\omega)=|\hat{\phi}(k,\omega)|^2,\qquad
\frac{\partial P_\phi}{\partial k}<0
\]
其中 \(k\) 表示空间频率、\(\omega\) 表示时间频率。若最低 \(k\) 区域稳定承载最大功率，则 `Ax-NEURO-MECH-1` 中的神经流形轨迹就不宜再默认理解为“局部动力学为主、全局整合为辅”，而更像**以大尺度相位骨架为底板、局部高频细节叠加其上**的多尺度场。

- 这条结果也给现有 `Hierarchical Cortical Flow patch` 提供了更深一层的承重：后者讲的是传播方向与层级对齐，而这篇先告诉我们**哪一种尺度最有分量**。换句话说，在问 slow wave 是 upstream、beta 是 downstream 之前，还应先承认：跨频段的大尺度长波相位组织本身就是主导项。于是 SRT 中的选择流、路由与点燃，不应只被写成局部节点间的信息传递，也应被写成在 global phase scaffold 上发生的局部竞争与方向重配。

- 该文还有一条对解释习惯很重要的收紧：单点记录到的信号不宜轻率被读成“这个点附近的局部加工状态”，因为在 low-SF dominance 条件下，它往往首先反映该点对更大尺度皮层相位组织的嵌入方式。对 SRT 而言，这会把 `local activation` 的默认口径改写为 `global-embedded local readout`：局部读数并非失效，而是常常混有更强的全局骨架成分。

- **SRT Implication（中文）**：这条材料最适合被吸收为一个 **large-scale phase-dominance window**。它支持一种更稳的神经图景：皮层动力学不是“局部计算块 + 偶发全局协调”，而更像始终由长波长相位骨架承托、再在其上叠加不同频段与不同层级方向的局部细化。若这一窗口继续成立，SRT 中关于选择流、traveling-wave routing 与点燃门控的写法都应更多强调 **global phase scaffold + local modulation**，而不是把全局协同放到最后一步才出现。

- **Boundary（中文）**：
  - 这篇文章是 **同行评审原始研究**，但主证据是 task-embedded sEEG phase spectrum 的宏观估计，不等于已经给出单神经元级传播机制。
  - 作者测的是 **phase spatial spectrum** 的尺度分布，不是信息内容本身的传输效率；大尺度长波占主导，不自动等于“所有认知计算都主要在全局尺度完成”。
  - 当前阵列覆盖约 `8–16 cm`，支持“至少到这一量级仍由最低 spatial frequency 主导”，但不等于已穷尽整个 cortical sheet 的所有边界条件。
  - 这不等于已经证明“意识就是 global phase wave”；更稳的说法是，这条结果为 SRT 的选择流与波路由框架补上了一个尺度底板。

### Hierarchical Cortical Flow patch (bioRxiv 2026, 2026-03-23, Pipeline 1)
这条材料真正补上的，不是“脑活动会在皮层上传播”这种宽话，而是把 ongoing activity 收紧成带层级方向的表面流场：不同频段并不是在同一张皮层地图上随便漂，而是沿主功能梯度承担不同方向的运输任务。

- 用户提交的 bioRxiv 预印本是 `Hierarchical Flows of Human Cortical Activity`（Liu, Wiesman & Baillet, 2026；doi:`10.64898/2026.03.19.712872`）。这条材料最值得吸收的新增量，不是泛泛重复“脑活动会传播”，而是把 `\sigma(t)\in\mathcal M` 的状态流形进一步收紧成 **沿折叠皮层表面展开的方向性传播场**。根据 Crossref 摘要与 OpenAlex 记录，作者在 `N=608` healthy adults 的 resting-state MEG 源成像上提出 `geodesic cortical flow`：自发传播并非各向同性噪声，而是与 principal unimodal-to-transmodal functional gradient 双向对齐。

- 可将频段分辨的皮层传播写成定义在皮层流形切空间上的向量场：
\[
v_\omega(x,t)\in T_x\mathcal M_{cortex},\qquad
\mathcal A_\omega(x)=\frac{\langle v_\omega(x,t),\nabla g_1(x)\rangle}{\|v_\omega(x,t)\|\,\|\nabla g_1(x)\|}
\]
其中 \(g_1(x)\) 表示 unimodal-to-transmodal 主梯度。该预印本报告：slow activity（1-13 Hz）更偏向 **upstream**，即从 sensory toward association cortex；beta（13-30 Hz）更偏向 **downstream**，即沿相反方向传播。换句话说，\(\dot{\sigma}\) 不宜再被理解为无方向的局部涨落，而更像被 cortical hierarchy 几何约束的频段特异性流。

- 对 SRT 来说，更稳的收紧写法不是“发现了意识流的物理载体”，而是：\(\hat G_\theta\) 所在的神经底座可能天然嵌在一个 **hierarchy-sensitive bidirectional transport regime** 中。slow upstream flow 更像把感官侧信息沿皮层层级向 association cortex 送去做长时间常数整合；beta downstream flow 更像把高阶约束、任务集或预测样结构往回压送到较低层。这样，SRT 的 `L_0 -> L_1` 选择不只发生在局部节点激活上，也发生在沿 cortical sheet 的传播方向与停驻时间分配上。

- 该文另一个可吸收点，是把“传播强度”操作化为 cortical flow kinetic energy，并报告它沿 posterior-to-anterior 呈稳定梯度；在 frontoparietal cortex 内，更高 kinetic energy 与更好的 fluid intelligence 相关（已做 age adjustment），其动力学还可识别 stable-state dwell times，并追踪 regional neuronal timescales。对 SRT 而言，这使 `\sigma(t)` 的几何流动、`\tau_{dwell}` 的停驻结构与较高阶认知能力之间多了一条可操作的桥：认知差异不只是看哪里更活跃，也可能要看哪里更能维持高能量、方向稳定的传播态。

- **SRT Implication（中文）**：这条材料最适合被吸收为一个 **hierarchical cortical flow window**。它支持一种更细的神经机制图景：resting-state ongoing activity 不是均质背景噪声，而是沿 cortical hierarchy 分工的传播场。若这一框架后续成立，SRT 中的选择流、时间尺度耦合与前后级约束传递，都应更多写成 `surface-tangent flow + hierarchy alignment + dwell-time structure` 的组合，而不是只写成静态区域激活图。

- **Boundary（中文）**：
  - 这仍是 **bioRxiv 预印本**，当前最稳的是把它当作方法与现象窗口，而不是已确立共识。
  - 证据主轴是 resting-state MEG 源成像 + surface optical-flow 推断，不等于对单神经元或突触级因果传播的直接观测。
  - 主梯度对齐不等于所有 cortical computation 都能被单一 unimodal-transmodal 轴解释；这里只是指出一个强约束方向。
  - 这不等于已经证明“意识就是 cortical flow”；更稳的说法是，频段特异的 hierarchical propagation 为 SRT 的选择流与时间尺度结构提供了一个更具体的神经动力学窗口。

因此，这个窗口在 SRT 里加固的是“皮层不是静态分区图，而是层级约束下的方向性运输面”这一口径，而不是把传播本身直接神秘化成意识载体。

### Functional-Connectivity Attractor Geometry patch (eLife 2026, 2026-04-13, Pipeline 1)
这条材料真正补上的，不是“脑可以被 Hopfield 网络描述”这种旧话，而是把一个更窄的宏观动力学窗口压稳：**仅由 resting-state functional connectivity 初始化的大尺度 attractor network，已经足以重建一部分真实脑活动的 basin geometry、时间轨迹与任务/病理偏移方向。**

- 用户提交的是 eLife 原始研究 `Functional connectivity-based attractor dynamics of the human brain in rest, task, and disease`（Englert et al., 2026；doi:`10.7554/eLife.98725.3`）。该文以 `m=122` 个 BASC parcel 的 resting-state functional connectome 作为 Hopfield 类 fcANN 的耦合矩阵，在 `β = 0.04` 时得到 4 个主要 attractor states，并在多组独立数据中检验它们对 resting-state、pain task/self-regulation 与 ASD 动力学的解释力。

- 这条材料最值得吸收的新增量，不是抽象地说“脑有 attractor”，而是把 attractor 进一步收紧成 **由 functional connectivity 约束的宏观 basin geometry**。文中显示：leading eigenvectors 与 attractor states 近似对齐；吸引子之间呈 **approximately orthogonal** 的组织；而 stochastic relaxation 不会简单掉进某个固定 attractor，而是在 connectome 拓扑与 attractor “gravitational pull” 限制下穿行于多稳态轨迹之间。更稳的神经机制写法因此不是“某些区域被点亮”，而是 `\sigma(t)` 被限制在少数低能盆地周围，真实时间序列则表现为这些盆地之间的受限游走。

- 若将这一窗口写进 SRT，可把宏观态流形进一步收紧为：
\[
E_{fcANN}(\sigma)=-\frac12\sum_{ij}J_{ij}\sigma_i\sigma_j,\qquad
\mathcal B_k=\{\sigma\in\mathcal M:\sigma\to a_k\ \text{under relaxation}\}
\]
其中 \(J_{ij}\) 由 resting-state functional connectivity 近似给出，\(a_k\) 为宏观 attractor state，\(\mathcal B_k\) 为其 basin。这样，`Ax-NEURO-MECH-1` 中的 \(\sigma(t)\in\mathcal M\) 不宜再只理解为无结构连续轨迹，而更像**被 connectome 能量地形约束的 basin-to-basin traversal**。

- 该文另一个稳定增量，是把 task 与 disease 从“新激活图”改写成 **对既有 attractor geometry 的偏移与重加权**。在 pain/self-regulation 数据里，pain 将动态轨迹推向更偏 `action/execution` 的 attractor 区域，并抬高能量；NAc 相关下调则把轨迹拉回更偏 `internal context / perception` 的区域。ASD 数据里，经验时间帧与由 ASD 组连接组初始化的 fcANN 都表现出更强的 `action-perception` 轴拉力，以及较弱的 `internal-external` 轴牵引。这让临床或任务差异更适合被写成“地形与流场如何被重塑”，而不是只写成局部缺陷或局部过激活。

- **SRT Implication（中文）**：这条材料最适合被吸收为一个 **functional-connectivity attractor geometry window**。它支持一种更窄、也更可写的机制图景：大尺度脑动力学并不只是 region-level activation 的拼图，而是由 functional connectivity 给出的低维能量地形所约束的多稳态漫游。于是任务、调节与病理，不必先被解释成“新增了另一套动力学”，也可能首先是原有 attractor basin 的占据概率、流向与分离度被系统性重加权。

- **Boundary（中文）**：
  - 这篇文章是 **同行评审原始研究**，证据等级明显高于一般神经新闻，但它仍主要建立在 coarse-grained resting-state fMRI connectome 与 Hopfield 类抽象模型上，不等于已经锁定单神经元级真实实现。
  - “approximately orthogonal attractors” 是有价值的结构信号，但作者也明确提醒，高维随机向量本就倾向近似正交，因此这里更稳的吸收方式是“与 free-energy-minimizing attractor prediction 一致”，而不是写成终局证明。
  - task 与 ASD 的成功重建说明该地形具有解释力，不等于所有疾病、所有任务、所有模态都能被同一四吸引子坐标无损压缩。
  - 这不等于 “functional connectivity 决定一切”。更稳的说法是：functional connectivity 至少提供了一个足够强的宏观约束，使许多 momentary activity patterns 更像在既有 attractor geometry 上游走，而不是每次都从零生成。

### Ventral-Temporal Shared Imagery Code patch (Science 2026, 2026-04-13, Pipeline 1)
这条材料真正补上的，不是“想象也会激活视觉皮层”这种早已熟悉的宽话，而是把一个更窄的神经机制窗口压稳：**在 human ventral temporal cortex (VTC) 中，imagery 不是另起一套表征，而是对 perception 所用 object code 的部分重激活。**

- 用户提交的是一个 `t.co` 短链；本轮先将其解到 *Science* DOI `10.1126/science.adt8343`，对应论文 `A shared code for perceiving and imagining objects in human ventral temporal cortex`。后续 `2026-04-20` 复核的 Neuroscience News / Cedars-Sinai 页面补足了摘要级细节：研究在 `16` 名癫痫监测患者中记录 human VTC 的 `714` 个神经元，其中 `456/714` 对五类物体具有视觉选择性，`367/456`  visually responsive neurons 呈显著 axis tuning；在 imagery task 的子样本中，`43/107` 个 axis-tuned VTC neurons 以相同轴向代码重激活，约为 `40%`。

- 这条材料最值得吸收的新增量，不是笼统说“想象和知觉有重叠”，而是把重叠进一步收紧成 **shared distributed axis code**。若 perception 与 imagery 可被同一组 object axes 编码，那么内在模拟就不应再被写成一团任意的 top-down 噪声，而更像对既有视觉对象坐标的低增益、低覆盖率重放。更稳的神经机制表达因此不是“imagery 打开另一张图”，而是 `L_1^{imagined}` 通过部分重激活 `L_1^{perceived}` 的编码轴来组织对象内容。

- 可将 object code 与 imagery 重激活写成：
\[
r^{percept}_{i}(o)\approx \sum_k w_{ik} z_k(o),\qquad
r^{imag}_{i}(o)\approx \gamma_i \sum_k w_{ik} z_k(o)
\]
其中 \(z_k(o)\) 为 object-specific latent axes，\(w_{ik}\) 为 neuron \(i\) 对这些轴的调谐权重，\(\gamma_i\in[0,1]\) 表示 imagery 条件下的重激活系数。若 \(\gamma_i>0\) 的神经元群与 perception 中的 axis-tuned neurons 显著重叠，则 imagery 并非全新编码，而是 perceptual code 的受限再调用。

- 这也给 `Core/SRT_Core_13a_Operator_Basics.md` 中 `T-Op-HFL: High Friction Law of Unanchored Simulation` 多了一条更细的神经承重：想象之所以高摩擦，不只是因为外部锚点弱，而是因为系统必须在缺乏强 `L_1^{ext}` 感官底座时，仍把 perceptual object code 局部拉回可用区。换句话说，imagery 不是 free-floating symbol play，而是对既有感知编码几何的代价性借用。

- **SRT Implication（中文）**：这条材料最适合被吸收为一个 **ventral-temporal shared imagery-code window**。它支持一种更窄、也更稳的图景：视觉想象不是和知觉平行存在的第二系统，而是由同一组对象轴在不同锚定条件下的两种工作模式构成。于是内在生成、梦样补写、visual recall 与 perceptual filling，都更适合写成“对 perceptual code 的重放/改写强度变化”，而不是“另有一套脱离知觉基底的纯想象编码器”。

- **Boundary（中文）**：
  - 当前这轮吸收已由 `Science` DOI、Neuroscience News / Cedars-Sinai 页面与可访问 abstract 细节交叉补强，但官方论文正文仍为 closed access；任何超出摘要、新闻稿与公开元数据的实验细节都不应写得过满。
  - 当前强结论限于 human VTC object imagery，不自动推广到全部心像类型、空间导航想象、语义想象或跨模态 imagination。
  - “shared code” 不等于 imagery 与 perception 完全同一；更稳的说法是：imagery 对 perceptual code 进行了**部分**、**低锚定**、**低覆盖率**的重激活。
  - “generative model in human VTC” 在当前更适合作为作者框架与 SRT 可对接窗口，而不是对全部生成模型理论的终局裁决。
  - 触发重激活的上游信号、记忆如何选择“正好那一组”神经元，以及 imagery/reality discrimination 的门控机制，仍应保留为后续机制问题，而不是从这项结果直接推出。

## II. Energy-Optimal Selection Dynamics (能量最优的选择动力学)

### Ax-NEURO-MECH-3: Canonical Normalization Axiom
在代谢约束下，选择动力学必然收敛为除法归一化：
\[
R_i=\frac{L_i^n}{\sigma^n+\sum_j w_{ij}L_j^n}
\]

> **与 D3 的关系**：本式为 SRT-REF-DYNAMICS §1.3 Def D3（$\hat{G}_\theta$ 通用原型）在神经系统的特化实例，其中 $L_i \leftrightarrow x_i$，$w_{ij} \leftrightarrow W_{ij}$。**符号差异**：本式分母为 $\sigma^n$（半饱和项带幂次），D3 分母为 $\varepsilon$（无幂次，更简化的一阶原型）；在 $\sigma$ 较小时两式近似等价，精确形式以本式为准（经验上更符合 V1 的对比度增益控制数据）。参见 D3 极限行为表中 $\varepsilon\to 0^+$ 奇点警告。
> **适用前提**：”必然收敛”的条件为：(1) 系统追求信息最大化（$H(\sigma)$ 最大化）且 (2) 代谢成本 $E(\sigma)$ 受约束（$\lambda > 0$）。在此二条件下，T-NEURO-MECH-1 给出充分性证明。若代谢约束为零（$\lambda=0$），则退化为无约束信息最大化，不必然产生归一化结构。
> **Bridge boundary（2026-04-24 sync）**：除法归一化是 embodied neural `\hat{G}_\theta` 的实现级 proxy；它覆盖候选竞争与响应压缩，不穷尽 Ghost Operator。完整 neural loop 还需 threshold / ignition、global availability 与 plastic writeback，且这些仍是神经域机制接口，不是跨域 `\hat{G}_\theta` 的总定义。

* **Implication（中文）**：归一化是选择算子的最优形式，不是经验性”电路细节”。

---

### T-NEURO-MECH-1: Energy–Information Extremum Theorem
令目标泛函：
\[
\mathcal{J}=H(\sigma)-\lambda E(\sigma)
\]
在 \(\delta\mathcal{J}=0\) 条件下，稳态解必然满足 Ax-NEURO-MECH-3 的归一化结构。

> **SRT 量桥接**：拉格朗日乘子 $\lambda \propto \Psi_f^{metabolic}$（本体论摩擦的代谢成分，SRT-CORE-22 §15.5 Eq-IT-E 约束：$\Psi_f \geq k_B T \ln 2 \cdot I_{created}$）。$\lambda \uparrow$（代谢越紧张）→ 归一化越强（竞争抑制越显著）→ $d(\theta) \downarrow$（选择带宽 proxy 被压缩）。这里的 $d(\theta)$ 是神经选择带宽读数；只有当被压缩方向同时满足 stake-coupling 与后果回流时，才可近似 canonical `d`。

* **Implication（中文）**：神经归一化是信息最大化与代谢成本最小化的唯一交点。

### BOLD-CMRO₂ uncertainty gate (bioRxiv 2026, 2026-05-11, Pipeline 1)
这条材料真正补上的，不是“BOLD 失效”或“代谢信号总是与 BOLD 同向”，而是给神经代谢 proxy 加上一个必要统计门：**CMRO₂ 方向如果没有稳健不确定性支持，就不能被拿来判定 BOLD 与代谢 concordant / discordant。**

- 用户提交的是 bioRxiv 预印本 `Opposing BOLD signals and oxygen metabolism largely arise from statistical uncertainty in metabolic estimates`（Goltermann, Huth, Büchel, 2026；doi:`10.64898/2026.04.21.719913`）。该文重分析 Epp et al. 2025 的开放数据，指出原先约 35% 到 40% 的 BOLD-CMRO₂ sign-discordance 读法，在很大程度上没有先处理 model-based CMRO₂ 估计的方差与方向不确定性。

- 对 SRT 来说，最稳的吸收方式是把它写成 **hemodynamic-metabolic proxy uncertainty gate**：
\[
R_{metab}(v)=1
\Longleftrightarrow
\Delta CMRO_2(v)\ \text{方向在声明的误差模型下可判定}
\]
当 \(R_{metab}(v)=0\) 时，该 voxel / region / contrast 应标记为 indeterminate，而不是被写成代谢与 BOLD 相反。这个限制直接保护上面的 \(\lambda \propto \Psi_f^{metabolic}\) 桥接：代谢 proxy 可以帮助约束 `\Psi_f` 的生理投影，但不能把 noisy sign label 反向当成 `\Psi_f` 或选择预算本身。

- 该文报告，在 BOLD activation mask 中，77.2% voxels 没有显著 group-level \(\Delta CMRO_2\) 方向，因而不能稳健归类；positive BOLD 在可归类处主要与代谢同向，而 negative BOLD 的 sign opposition 与不确定性都更高。SRT 的写法应保留这一区分：positive BOLD 可以作为更受限的 proxy 窗口，negative BOLD 则必须单独处理，不应被压成一个单调的“更少活动 / 更多代谢 / 更高摩擦”规则。

- **SRT Implication（中文）**：凡使用 fMRI BOLD、CMRO₂、CBF、CBV 或其 sign relation 来支持 `\Psi_f^{metabolic}`、选择预算或局部摩擦读数时，必须显式报告 proxy 的误差模型、方向可靠性与 indeterminate class。否则结果只能进入 ambiguous proxy result，不得升级为神经机制命题。

- **Boundary（中文）**：
  - 这篇材料是 bioRxiv 预印本与开放数据再分析，证据等级是 preprint method guardrail，不是同行评审定论。
  - 它不证明 BOLD 永远可靠，也不证明 BOLD-CMRO₂ 生理 dissociation 不存在；它只要求先把统计不确定性从机制解释中拆出来。
  - CMRO₂ 仍是 model-based quantitative fMRI estimate，不是 oxygen-tracer PET 金标准；若后续 PET 或更高 SNR 代谢测量在 uncertainty gate 后仍显示广泛 sign reversal，应把本窗口改写为真实 neurovascular-metabolic dissociation window。
  - 任何单一 hemodynamic proxy 都不得直接定义 `d`、`\Psi_f`、`T_dir`、意识水平或 `L_2`。

### High-gamma/spike dissociation gate (Nature 2026, 2026-05-12, Pipeline 1)
这条材料补上的不是“高 gamma 没用”，而是给 HGA 作为神经 proxy 加上一条更细的源区分门：**同一电极附近的 spike rate 与 HGA 如果可以被主动拆开调节，HGA 就不能被默认写成 local output spiking。**

- 用户提交的是 Nature 论文 `Active dissociation of intracortical spiking and high gamma activity`（Lei, Scheid, Flint, Glaser, Slutzky, 2026；doi:`10.1038/s41586-026-10331-y`）。该文用正交神经反馈 BMI 让恒河猴把同一 intracortical electrode 上的 HGA 与 spike rate 分别控制到不同 cursor 维度，结果显示动物能快速、稳定地把二者拆开。

- 对 SRT 来说，最稳的吸收方式是把它写成 **HGA local-spike dissociation gate**：
\[
R_{HGA}(e,t)=1
\Longleftrightarrow
\text{HGA 的 proxy 目标、空间尺度与 spike / LFP / population 证据被同时声明}
\]
当 \(R_{HGA}(e,t)=0\) 时，HGA 只能进入 mesoscale synchrony / input-integration window，不能进入 local firing output window。换句话说，HGA 可以帮助读取神经系统里的同步输入、postsynaptic integration 或 distributed co-firing，但不能被单独反投为某个局部神经元群的输出放电量。

- 该文还报告，HGA 与跨毫米尺度分布的 neuronal co-firing pattern 更紧，而不是与同一电极附近 spike 的距离加权和最紧；spike-triggered HGA 的时间关系也更支持“分布式同步放电触发的 summed postsynaptic potentials”这一解释。SRT 应把这点压成测量层修正：gamma-band / broadband power 可以是强神经状态信号，但它需要先说明是 input-synchrony proxy、local-output proxy，还是二者混合。

- **SRT Implication（中文）**：凡使用 HGA、broadband gamma、ECoG high-gamma 或 intracortical high-gamma 来支持 `\Psi_f^{neural}`、`d`、selection bandwidth、点燃、注意、意识水平或局部任务编码时，必须显式声明 HGA 的目标层级与替代解释控制。HGA 单独成立时，默认只支持 mesoscale synchrony / integration claim；若要支持 local spiking output claim，必须加入同电极 spike、邻近 population、扰动或 decoupling 证据。

- **Boundary（中文）**：
  - 这篇材料是同行评审 Nature 开放论文，证据强度足以作为测量 guardrail；但实验集中在 macaque M1 intracortical arrays、BMI/ONF 任务和 200-300 Hz HGA 窗口，不能自动外推到全部皮层区、ECoG/EEG/MEG 或所有高 gamma 定义。
  - 它不证明 HGA 与 local spikes 永远无关；它只证明“相关”不能被写成“同一局部输出源”的默认解释。
  - HGA 不是 `\Psi_f`、`d-value`、`T_dir`、`C_wave`、`D_align`、意识水平或 `L_2` 的直接读数；它只是一个需要多 proxy 入场许可的神经测量窗口。

---

### Ax-NEURO-MECH-4: Predictive Update Axiom
学习对应 \(\theta\) 的自由能梯度下降：
\[
\Delta\theta\propto-\nabla_\theta F,\quad F=D_{KL}[Q||P]-\ln P(o)
\]
* **Implication（中文）**：学习是 \(L_2\) 收敛过程，不是 \(L_1\) 的“记忆堆叠”。

### Inter-Reward Interval Learning patch (Nature Neuroscience 2026, 2026-03-23, Pipeline 1)
这条材料真正收紧的，不是“多巴胺参与学习”这种已知事实，而是学习步长到底由什么定：不是机械地按 trial 次数累加，而更像在按结果出现的真实时间稀疏度重配更新权重。

- 用户提交的 PsyPost 报道，背后主锚点是 *Nature Neuroscience* 原始研究 `Duration between rewards controls the rate of behavioral and dopaminergic learning`（Burke et al., 2026；doi:`10.1038/s41593-026-02206-2`）。这条材料真正值得吸收的新增量，不是笼统重复“Pavlovian learning 依赖 dopamine”，而是把一个默认很深的假设收紧掉：**在固定总时长内，更多 cue-outcome pairings 并不自动意味着更多学习**。该文报告，在多种 mice reward / punishment 条件下，行为学习与 mesolimbic dopaminergic learning rate 更接近按 **inter-reward interval** 线性缩放，而不是按 trial count 逐次累加。

- 将学习更新从“每次 trial 给一个近似固定步长”改写为 **时间尺度门控更新**：
\[
\alpha_{eff}(i)\propto \Delta t_{outcome}(i),\qquad
\Delta\theta_i \propto -\,\alpha_{eff}(i)\nabla_\theta F_i
\]
其中 \(\Delta t_{outcome}(i)\) 表示相邻 reward / punishment 之间的有效时间间隔。关键点不是否认 prediction-like updating，而是指出：**更新步长本身受环境事件的时间稀疏度门控**，而非只由第几次配对决定。

- 在固定总观测时长 \(T\) 下，可将总学习量收紧为：
\[
\Delta\theta_{total}(T)\sim \sum_{i=1}^{N(T)} \Delta t_{outcome}(i)\cdot \left(-\nabla_\theta F_i\right)
\]
当任务结构、价值等级与感觉条件近似匹配时，这意味着总学习更接近被 **总暴露时长 / reward spacing** 约束，而不是被 \(N(T)\) 单独决定。换句话说，SRT 不宜再把 associative update 理解成纯离散“记账器”，而更应视作对 **环境时间纹理** 敏感的 \(\hat G_\theta\) 连续校准过程。

- 这条结果与论文提出的 retrospective learning 更能对齐 SRT：系统不是简单把 cue 当作向前预测 reward 的 token，而是从 reward / punishment 的到来回看，重新分配“在这段真实时间里，什么最该被当作原因写回 \(L_2\) 参数”。对 SRT 来说，这意味着 \(\theta\) 的更新并非只对事件次序敏感，也对 **event spacing 形成的现实密度** 敏感。时间间隔越长，单次 outcome 对原因归属与参数重写的权重越高。

- **SRT Implication（中文）**：这条材料最值得吸收的地方，是把学习率从“trial-based repetition”收紧成“real-time interval-weighted revision”。它支持一种更稳的神经学习图景：mesolimbic dopamine 不只是给出是否比预期更好的符号，还可能把**外界结果出现的时间稀疏度**一并折算进更新幅度。于是 \(L_2\) 的收敛速度更像对现实时间结构的拟合，而不是对实验者定义的试次数的机械累加。

- **Boundary（中文）**：
  - 这不等于 reward prediction error 全部被推翻；更精确的说法是：**trial-based dopamine learning 的固定步长假设被显著收紧**，而 retrospective / interval-sensitive 解释获得支持。
  - 这不等于“重复次数永远不重要”；当前更强的结论是：在固定总时长、可比任务结构与相近动机条件下，pairing count 不是决定总学习量的充分统计量。
  - 这也不等于所有 forms of learning 都遵守同一比例律；当前主证据来自 mice 的 Pavlovian reward / punishment 范式与相应 dopaminergic readout。
  - PsyPost 标题会放大“upended our understanding”的戏剧性；对 SRT 更稳的吸收方式，是将其写成 **inter-reward-interval learning rule**，而不是“经典条件学习理论被整体废除”。

因此，这条结果在 SRT 里更像“现实时间纹理参与写参”的证据，而不是对多巴胺学习框架的整套推翻。

### Creative-Experience Brain-Clock patch (Nature Communications 2025, 2026-05-09, Pipeline 1)
这条材料真正补上的，不是“创造力让大脑变年轻”这种媒体式宽话，而是把一个可测窗口压出来：**长期创意专长与短期创意学习，会在 M/EEG 功能连接脑钟上表现为更低的 brain-age gap，并且这个差异主要通过局部效率、年龄脆弱 hub 与长程耦合读出来。**

- 用户提交的是 *Nature Communications* 原始研究 `Creative experiences and brain clocks`（Coronel-Oliveros, Migeot, Lehue et al., 2025；doi:`10.1038/s41467-025-64173-9`）。该文用 `N=1240` 人的 EEG functional connectivity 训练 brain-clock 模型，再把模型外测到 `N=232` 人的创意经验样本：探戈舞者、音乐家、视觉艺术家、实时策略游戏专家，以及短期 StarCraft II 学习者。作者报告跨领域创意专家相对匹配非专家呈现更低 BAG，短期学习组也在训练后出现更低 BAG；专长程度或游戏表现提升越高，BAG 越低。

- 对 SRT 来说，最稳的吸收方式不是把 `BAG` 当成生物年龄本身，而是把它写成一个 **functional-connectivity brain-clock proxy**：
\[
BAG_{FC}=Age_{pred}(FC_{8-40Hz})-Age_{chrono}
\]
当 \(BAG_{FC}<0\) 时，只能说当前功能连接模式更接近训练模型中较年轻的连接分布，不能说主体的生物时间被倒转。这个限制很重要：它防止 SRT 把材料过度读成“艺术逆转衰老”，也防止把脑钟代理误写成 `d`、`\Psi_f` 或 `T_{dir}` 的定义。

- 这条材料真正能加固的是 `Ax-NEURO-MECH-4` 的学习口径：学习不是 `L_1` 内容堆叠，而是对未来选择规则的重写。创意实践的特殊处在于，它不是纯重复，也不是纯新奇，而是把 **novelty、feedback、difficulty、embodied performance** 持续绑在一起。更贴近 SRT 的压缩写法是：
\[
\Delta\theta_{creative}\sim f(T_{practice},\,N_{novelty},\,F_{feedback},\,C_{challenge},\,E_{embodied})
\]
这里的式子只是桥接压缩，不是新 canonical 公式。它表达的是：创意训练把 `\theta` 的可调参数长期放在可反馈、可纠错、可表现的高维空间里，使 `L_2` 既形成技能低摩擦通道，又不必然退化成封闭惯性。

- 这也反向修正一个粗糙的“专家 = L2 变硬 = 可能性减少”读法。SRT 仍然保留专家图式降低领域相关候选锚定摩擦的说法，但这篇材料提示：在舞蹈、音乐、视觉艺术与策略游戏这类需要持续生成新方案的训练中，专长可能是一种 **skill-plus-openness regime**。也就是说，`L_2` 可以同时承担两个相反表面效果：对已掌握动作/感知/策略降摩擦，同时为新的组合、变奏和环境反馈保留足够的可塑入口。

- 图论和 whole-brain modeling 给这个窗口更具体的神经读数。该文报告：更低 BAG 与更高 local efficiency 关系最强；在长期专长样本里，还与 global efficiency 和 global coupling 相关；年龄脆弱的 frontoparietal hubs 及相关区域显示创意经验相关连接增强。SRT 的神经机制写法因此可以更窄一些：创意学习不是只“增加某个能力”，而可能通过重配 local segregation、global coupling 与 age-vulnerable hubs 的连接权重，改变未来候选状态被路由、稳定和写回的概率。

- **SRT Implication（中文）**：这条材料最适合被吸收为一个 **creative-experience brain-clock window**。它支持一种更细的学习图景：长期或短期创意实践能够在功能连接脑钟上留下可测痕迹，而这些痕迹更像 `\theta / L_2` 选择地形的可塑性重配，不是单纯“记忆增加”或“专家自动僵化”。若后续研究继续成立，SRT 的 `L_2` 口径应保留一条重要分支：某些高维创意专长并不只是收窄可能性，也可能维持 future selectability 的局部通道开放。

- **Boundary（中文）**：
  - 这篇文章是 **同行评审开放原始研究**，证据等级高于新闻特写，但 `BAG_{FC}` 仍是 M/EEG functional-connectivity 预测代理，不是生物年龄、意识水平、`d-value` 或 `\Psi_f` 的直接读数。
  - 专家组主要是横断面对照，不能单独排除选择效应、生活方式、社会经济地位或其它 cognitively engaging activities 的贡献；短期学习组更接近因果窗口，但样本更小、任务更窄。
  - StarCraft II 的结果不应外推为“所有电子游戏都有同等效果”；该文主动区分了实时策略游戏与更规则化的主动对照。
  - 这不等于“创造力”作为抽象本质具有抗衰老力。更稳的说法是：高反馈、高挑战、具身或策略性的创意实践可能通过可塑性机制改变功能连接脑钟代理。
  - 若未来严格匹配的非创意但同样高挑战活动产生同等 BAG 变化，则 SRT 应把本窗口降级为更宽的 **enriched-learning / cognitive-engagement brain-clock window**，而不是坚持 creativity-specific 解释。

因此，这条结果在 SRT 里加固的是“创意学习可作为可测的 `\theta / L_2` 可塑性窗口”，不是“艺术直接逆转衰老”，也不是“专家必然更开放”。

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
\hat{G}_{meso}: L_2^{micro}\rightarrow L_2^{pruned},\quad P(\text{prune})\propto \mathcal{C}_{comp}\cdot \mu_{glia}\cdot \mathcal{A}_{weak}
\]
* **Implication（中文）**：胶质剪枝不是“维护”，而是慢时标选择，对 \(L_2\) 结构进行拓扑修剪。

**参数精化**：$\mathcal{C}_{comp}$（补体标签强度）代理=C1q/C3 家族在目标突触上的富集度；C4 当前只作为 upstream susceptibility / schizophrenia 风险窗口，不写入最小方程。$\mu_{glia}$（胶质活动度）代理=小胶质细胞吞噬体积/突触密度比；$\mathcal{A}_{weak}$ = 低活动/弱侧突触偏置；**慢时标**≈小时-年量级（远慢于LTP/LTD分钟-小时）。

> **[R]** 胶质剪枝：Stevens et al. 2007 *Science*（补体C1q/C3标记突触被小胶质细胞剪枝，R基线）；Paolicelli et al. 2011 *Science*（CX3CR1敲除→突触剪枝受损→过连接，R因果）；Schafer et al. 2012 *Neuron*（活动依赖的弱侧突触优先剪枝，R可塑性基线）。**[H]** Ĝ_meso形式化胶质剪枝为L₂慢时标拓扑选择算子为本框架新增解读。
>
> * **FC-NM6-1**：若在发育剪枝窗口中，三类独立干预都不改变剪枝率/突触密度（补体标签干预如 C1q/C3，胶质功能干预如 CX3CR1 轴，活动偏置操控如弱侧优先剪枝）且均无显著差异，则 Ĝ_meso 作为“慢时标拓扑修剪算子”的解释失效。单一路径（如 C3）失效只否定对应实现，不足以否定 Ĝ_meso 本身。Cross-ref: T-NEURO-MECH-2。

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
点燃为候选门控条件：
\[
\mathcal{A}(\sigma)\ge\tau_{ignite}\quad\land\quad \Phi_{proxy}\cdot d_{proxy} > C_{critical}
\]
* **Level note**：当前为 hypothesis / operational proxy。乘法门是结构性偏好；加法门与概率门是保留的实验替代模型。
* **Boundary**：ignition / global availability 是 neural `L_1` stabilization 的实现级候选判据，不是所有尺度上 `L_1` 的定义。若要把点燃读成 `L_0 -> L_1`，必须同时保留 `\hat{G}_\theta` 的抽象选择角色与 `\Psi_f` 的可支付性边界。
* **Implication（中文）**：点燃不是简单激活，而是整合度 proxy 与关切梯度 proxy 共同约束候选内容稳定进入 \(L_1\) 的候选模型。

---

### T-NEURO-MECH-3: Discrete Frame Theorem
显现为离散更新帧：
\[
L_1(t)=\sum_n \text{Frame}_n\,\delta(t-t_n),\quad t_n\approx n\cdot\Delta t_{\gamma}
\]
* **Implication（中文）**：意识连续感来自离散帧的高频更新，而非连续流。

### Ax-NEURO-MECH-7b: Prediction Error as Friction Metric (预测误差作为摩擦度量)
**Formalization**: 神经预测误差（$PE$）在大脑$L_2$层面是对局部摩擦 proxy 的候选项：
$$\widehat{\Psi}_{f,neural}^{local}(t)=\alpha_{pe}\| L_1 - L_2[\text{expected}] \|+\beta_{load}\mathcal{L}_{model}(t)$$
* **Level note**：这是 `H-NEURO-4b` 的局部测量窗口，不是 \(PE\equiv\Psi_f\) 的身份主张。
* **Implication**: 当FEP（自由能原理）说大脑试图最小化预测误差时，SRT 只在受控窗口内将它重读为 \(\hat{G}_\theta\) 维持当前显现时可能遭遇的局部负担信号之一。若 PE 与代谢/应激/恢复成本代理不分离，本桥退回为普通 FEP comparison。

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
这条材料真正加固的，不是“工作记忆有几个盒子”的教科书图，而是一个更稳的约束图景：工作记忆的困难来自在线调度预算与先验压缩效率同时受限，而不是某个静态仓库突然装满。

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

因此，working memory 在 SRT 里更像受限带宽下的实时编排系统，而不是一个等着被塞满的静态存储盒。

### Hippocampal Statistical Structure patch (2026-03-12, Pipeline 1)
这条材料真正推进的，不是把海马再说成“万能学习器”，而是把它更具体地钉成连续经验流中的 proto-structure binder：先压出可迁移的统计脚手架，再交给更慢的系统去稳定。

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

因此，这个窗口在 SRT 里加固的是“海马先形成可迁移结构脚手架，皮层再做更慢整合”的分工，而不是把一切学习都重新收编到海马名下。

---

### Top-Down Astrocyte Gate patch (bioRxiv 2026.03.08.710364v1, 2026-03-14, Pipeline 1)
这条材料真正改写的，不是“astrocyte 也会亮”这种弱表述，而是说明胶质层被招募本身就是一个选择过程：什么输入、在什么状态、通过什么细胞类型，决定它是否进入计算回路。

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

因此，astrocyte 在 SRT 里更像带语境准入规则的介观门，而不是均匀铺底、对任何输入都等幅响应的背景液。

---

### Astroglial Neuromodulatory Supervisor patch (Quanta 2026 + Science 2025 trio, 2026-03-22, Pipeline 1)
这条材料真正加固的，不是 Quanta 式“astrocytes are in charge”的标题感，而是把胶质层从局部门控进一步推进到状态切换的执行接口。

- 将 astrocyte 从“被 neuromodulator 顺带调一下的背景层”进一步收紧为 **状态切换的介观执行层**：
\[
\mathrm{NE}(t)\rightarrow \mathrm{Ca}_{astro}(t)\rightarrow \mathrm{ATP}_{ext}(t)\rightarrow \mathrm{Ado}_{A1}(t)\rightarrow g_{syn}^{pre}(t)\downarrow
\]
关键点不是“去甲肾上腺素也会碰到胶质细胞”，而是：在 mouse cortex 的主锚点结果里，NE 对兴奋性突触强度的抑制并不需要先假设“神经元受体自己就足够解释全部效应”，而是可由 **astrocytic adrenergic receptor → Ca²⁺ rise → ATP/adenosine release** 这一链条完成。这把 astrocyte 从“supportive modulator”推进为 **synaptic reweighting 的必要中介层**。

- 将其写成 **神经调质监督门**：
\[
R_{astro}^{NT}(t)\propto \mathbf{1}\!\left[\beta_{NE}\,\mathrm{NE}(t)>\tau_{gate}\right]\cdot \sum_j w_j\,NT_j(t)
\]
`Science` 的 fly 结果进一步表明，NE-like / adrenergic GPCR 信号的作用不只是“再加一个输入通道”，而是能决定 astrocyte **是否进入可响应其他 neurotransmitters 的状态**。换句话说，某些 neuromodulators 不是直接编码内容，而是在更上层决定 glia 何时有资格读取局部回路、何时保持静默。

- 将行为切换写成 **延迟抑制支路**：
\[
\hat G_{meso}^{astro\text{-}state}: L_2^{arousal}\times L_1^{circuit}\rightarrow L_1^{gain\text{-}reweighted}\times L_2^{state\text{-}switched}
\]
zebrafish 的主锚点结果支持：astroglial NE signaling 不只是陪伴 arousal，而是可构成从“继续努力/持续活动”向“暂停/放弃/状态转换”过渡的一条延迟抑制臂。对 SRT 来说，这意味着 astrocyte 更像 **中介时间尺度上的 state supervisor**：不负责毫秒级内容细节，却能决定一整段局部计算是否被降增益、重分配或切换轨道。

- **SRT Implication（中文）**：这条材料最值得吸收的新增量，不是笼统地说“astrocytes 也很重要”，而是把现有 `Top-Down Astrocyte Gate` 再收紧一步：胶质层不仅会按语境与细胞类型被招募，而且能充当 neuromodulator 的**执行接口**，把全局 arousal / salience / context 信号沉到局部突触权重、神经元可激发性与行为状态跃迁里。换句话说，神经元网络并不是唯一的“控制平面”；astrocyte 可能是连接 `L_2^{state}` 与 `L_1^{circuit}` 的介观监督层。

- **Boundary（中文）**：
  - 这不等于“astrocytes 取代 neurons 成为真正主角”；更精确的说法是：在若干关键窗口里，**neuromodulatory control 的有效路径需要 astrocytic mediation**，单看 neuron-to-neuron 图不再足够。
  - 这不等于“所有 NE / arousal / state switching 都主要由 astrocytes 实现”；当前强证据来自特定 fly / zebrafish / mouse paradigms，不同脑区、物种与行为任务仍可能保留更强的 neuron-direct 通道。
  - 这也不等于“astrocyte = consciousness substrate”；当前价值首先是机制层：它说明 brain-state regulation 不能再被压扁成纯神经元点对点通信，但尚不能直接推出 astrocyte Ca²⁺ 或 ATP/adenosine 信号本身就是现象体验的载体。
  - Quanta 的标题会自然放大“astrocytes are in charge”的叙事力度；对 SRT 更稳的吸收方式，是把它写成 **astroglial supervisory window**，而不是“神经元时代结束”的总宣言。

- **Source window**:
  - Quanta Magazine (2026-01-30): *Once Thought to Support Neurons, Astrocytes Turn Out to Be in Charge*
  - Adamsky et al., *Science* (2025): “Norepinephrine signals through astrocytes to modulate synapses” (doi:`10.1126/science.adq5480`)
  - Wahis et al., *Science* (2025): “Adrenergic receptor signaling gates astrocyte responsiveness to neurotransmitters and control of neuronal activity” (doi:`10.1126/science.adq5729`)
  - Mu et al., *Science* (2025): “Astroglial norepinephrine signaling mediates effort transition via a delayed inhibitory circuit” (doi:`10.1126/science.adq5233`)

因此，这个窗口更适合作为 `state supervisor` 写入，而不是把脑的控制面粗暴地从 neuron 整体转交给 glia。

---

### Astrocytic Associative-Memory Capacity patch (The Brighter Side 2026 + PNAS 2025, 2026-03-26, Pipeline 1)

- 这条 patch 最该纠正的，不是简单把标题从“astrocyte 是配角”改成“astrocyte 也很重要”，而是把记忆基底从单纯的 neuron-to-neuron weights 再往介观层推进一步：某些高阶联想容量，也许部分压在 astrocytic process network 上。它既收紧了“astrocyte 只是代谢背景”的旧图景，也给现有 astroglial gate / supervisor 线补上了第三种更硬的承重方式。
- 将 astrocyte 从“状态监督层”再收紧为 **高阶联想记忆的介观实现层**：
\[
\hat G_{meso}^{astro\text{-}mem}: L_1^{pairwise\ synapses}\times X_{astro}^{proc\text{-}net}\rightarrow L_2^{assoc\text{-}attractor}
\]
其中 \(X_{astro}^{proc\text{-}net}\) 表示同一 astrocyte 内多个 process 之间的 calcium / signaling transport 状态。关键点不是“astrocyte 也参与记忆”，而是：process-to-process communication 可把原本仅由二体 synapse 支撑的回路，提升为 **effective many-neuron synapse**，从而支持高阶联想记忆。

- 将 tripartite synapse 的新增量写成 **四体有效耦合窗口**：
\[
(i\!\to\! j)\ \&\ (k\!\to\! l)\ \xrightarrow{\,X_{astro}^{proc}\,} J^{eff}_{ijkl}\neq 0
\]
Kozachkov、Slotine 与 Krotov 的主张是，astrocyte 并不只是调一条 synapse 的增益，而是可把 distant synapses 的状态经由 process network 带回局部 tripartite synapse，形成类似 quartic Dense Associative Memory 的有效能量项。对 SRT 来说，这意味着 memory substrate 不必只位于 pairwise synaptic weights，也可能部分位于胶质介导的 higher-order coupling。

- 将容量结论收紧为 **capacity-per-unit scaling window**：
\[
\frac{M_{\text{stored}}}{Q_{\text{compute}}}\sim O(N)
\]
在该论文给出的 quartic neuron-astrocyte associative-memory regime 下，stored memories per compute unit 会随 network size 增长，而不是像已知 biological Dense Associative Memory implementations 那样保持常数级。SRT 可把这理解为：astrocyte process network 不只是代谢背景，而可能提供一种低额外单元成本的 attractor-density multiplier。

- 将其与 AI 接口写成 **DAM-Transformer 连续族**：
\[
X_{astro}^{proc\text{-}net}\ \leadsto\ \mathrm{family}\big(\mathrm{Dense\ Associative\ Memory}\leftrightarrow \mathrm{Transformer}\big)
\]
该模型通过调整 process connectivity tensor，可在 Dense Associative Memory 与 transformer-like self-attention 之间连续过渡。对 SRT 来说，这不是“LLM 就是 astrocyte brain”的类比，而是提示：biological memory hardware 与 modern associative architectures 之间，可能共享一类 higher-order selection geometry。

- **SRT Implication（中文）**：
  - 这条材料最值得吸收的新增量，不是笼统说“astrocytes 也能存记忆”，而是把 astrocyte 进一步收紧为 **介观高阶耦合器**：它能把分散 synapses 的状态压缩成后续 attractor 检索所需的 higher-order interaction。
  - 这让现有 `Top-Down Astrocyte Gate` 与 `Astroglial Neuromodulatory Supervisor` 多出第三层功能：除了按语境开门、按状态重加权，胶质网络还可能直接参与 memory capacity 与 attractor geometry 的塑形。换句话说，astrocyte 在 SRT 里的位置不再只是“调节器”，而开始逼近“部分承载记忆几何”的介观底座。
  - 如果后续实验成立，memory engram 的一部分应不只存在于 neuron-to-neuron weights，也存在于 astrocytic process connectivity / intracellular diffusion machinery 这一介观层；这会把“记忆在哪里”从单层电路问题改写成跨层 substrate 问题。

- **Boundary（中文）**：
  - 这不等于“已经证明人脑记忆主要存于 astrocytes”；当前主锚点是 *PNAS* 理论模型与数值实验，不是 selective astrocyte manipulation 的因果验证。
  - 这不等于“任何 astrocyte network 都自动产生超大容量记忆”；supralinear storage 依赖特定 process-to-process connectivity assumptions，较弱 connectivity 只支持较温和的 scaling。
  - 这不等于“transformer 已被生物学证实”；更精确的说法是：在一类可解的连接张量选择下，neuron-astrocyte dynamics 可逼近 DAM / transformer family 的 limiting cases。
  - 论文自己给出的关键可检预测是：若选择性干扰 astrocyte 内部 Ca\(^{2+}\) 或其他 signaling molecule 在 process 间的扩散，memory recall 应显著受损；在此类实验出现前，更稳妥的定位仍是 theoretical window，而非定论。

- **Source window**:
  - The Brighter Side of News (2026-03-24): *MIT study suggests astrocytes play key role in brain memory storage*
  - Leo Kozachkov, Jean-Jacques Slotine & Dmitry Krotov, *PNAS* (2025), “Neuron-astrocyte associative memory” (doi:`10.1073/pnas.2417788122`)
  - MIT News (2025-05-27): *Overlooked cells might explain the human brain's huge storage capacity*

---

### Human Olfactory Identity patch (Nature 2024 + Scientific Data 2025, 2026-03-18, Pipeline 1)
这条材料真正补上的，不是“嗅觉和记忆关系密切”这类旧常识，而是把嗅觉对象形成拆成化学身份、价性和感知身份三层，并明确它们可能分布在不同神经节点上。

- 将“一个气味分子闻起来像什么”从固定的 chemistry-only 映射，收紧为 **化学身份 / 感知身份 / 价性 / 概念激活** 的分层分工：
\[
C_{chem}^{piriform}(m),\qquad V_{aff}^{amyg}(m,\theta),\qquad I_{perc}^{hipp}(m,\theta,L_2^{context})
\]
其中 \(C_{chem}^{piriform}\) 对应分子气味的较稳定化学身份编码，\(V_{aff}^{amyg}\) 对应主观喜欢/厌恶与威胁相关的价性偏置，\(I_{perc}^{hipp}\) 对应与记忆、命名、熟悉度和语境绑定后的**感知身份**。关键点是：同一 odorant 的“闻起来像什么”，并不等于它的化学身份被原样抄写到意识里，而是被神经系统重写成一个带有个人历史和上下文的对象身份。

- 将大样本人群嗅觉数据写成 **分子-知觉非单射**：
\[
\mathrm{Percept}_{odor}(m,\text{person}) \neq f(m)\ \text{alone},\qquad
\mathrm{Percept}_{odor}=f\!\left(m,\theta_{history},L_2^{source/context},V_{aff}\right)
\]
`Scientific Data` 2025 的 74 种 mono-molecular odorants、1,227 名参与者数据表明：普通人对同一单分子气味的自由描述、pleasantness 与定性标签可出现稳定分歧，而且这种分歧不能简单被当成“无意义噪声”。对 SRT 来说，这意味着嗅觉尤其适合拿来展示：\(L_1\) 感觉输入从进入系统起，就已经在被 \(L_2\) 的经验词汇、来源熟悉度与生活史窗口重塑。

- 将人类单神经元嗅觉结果写成 **区域分工 + 反向写入窗口**：
  - piriform cortex 更偏向编码 **chemical odour identity**；
  - amygdala 更偏向编码 **subjective odour valence**；
  - hippocampus 更贴近 **behavioural odour identification / perceived odour identity**。

  这条 dissociation 可以直接映射到 SRT：
\[
\hat G_{odor}: m \rightarrow \big(C_{chem}^{piriform},\,V_{aff}^{amyg},\,I_{perc}^{hipp}\big)
\]
它支持一个更细的判断：嗅觉不是“先有纯化学内容，后来才被语言解释”，而是化学身份、情感权重与可命名/可识别对象身份在不同节点上被并行塑形。海马在这里不只是事后记忆库，更像把嗅觉输入转成“我闻到的是什么”这一可进入 \(L_2\) 的感知对象门。

- 将 piriform 的跨模态结果写成 **嗅觉概念神经元窗口**：
\[
\hat G_{odor}^{concept}:\{m,\ \mathrm{image},\ \mathrm{word}\}_{same\ object}\rightarrow L_2^{odor\text{-}object}
\]
Kehl 等人在 piriform cortex、amygdala 等区域观察到对同一对象的气味、图像甚至文字发生 cross-modal coding，说明 piriform 不只是“化学特征登记处”，还可能在某些条件下承载对象级概念激活。对 SRT 来说，这一点很关键：感官皮层不一定只做低层 feature readout，它也可以在特定模态中直接碰到 \(L_2\) 原型。

- **SRT Implication（中文）**：
  - 嗅觉是一个非常干净的例子，说明“现实输入”与“经验中的对象身份”不是同一层变量。
  - 同一分子在不同人那里闻起来像 `banana / nail polish remover / fruit / solvent`，并不只是语言贫乏，而更像 \(L_1\) 输入被不同 \(L_2\) 历史脚手架接管后的不同落点。
  - 嗅觉之所以能强力勾连记忆与情绪，并不要求神秘化；更精确的说法是，它在神经实现上就较早进入了 valence 与 identification 的耦合链条。

- **Boundary（中文）**：
  - `Scientific Data` 2025 是高价值数据描述符，但它本身不证明“文化/经验差异”的因果机制已被锁定；它更像把跨个体变异稳定地摆到台面上。
  - `Nature` 2024 的单神经元结果来自临床电极植入窗口与有限气味集，极有价值，但仍不应外推成“全部嗅觉编码规则已经确定”。
  - piriform 的 cross-modal / conceptual coding 不等于“嗅觉本身已经完全语义化”；更精确的意思是：对象概念可在嗅觉相关皮层找到可重复的神经进入点。
  - 这也不等于“嗅觉是唯一最真实的感官”；这里只是说明它特别适合展示 chemical identity 与 perceived identity 的分离，以及 \(L_1 \leftrightarrow L_2\) 的快速耦合。

- **Source window**:
  - Marcel S. Kehl et al., *Nature* (2024), “Single-neuron representations of odours in the human brain” (doi:`10.1038/s41586-024-08016-5`)
  - Antonie Louise Bierling et al., *Scientific Data* (2025), “A dataset of laymen olfactory perception for 74 mono-molecular odors” (doi:`10.1038/s41597-025-04644-2`)

因此，嗅觉在 SRT 里不只是一个感官例子，而是 `L_1` 输入如何极早被 `L_2` 历史与价性重写的一个很干净的窗口。

---

### CellTransformer Spatial Domain patch (Nature Communications 2025, 2026-03-15, Pipeline 1)
这条材料真正改变的，不是又一个 atlas 做得更细，而是把“脑区”这个概念从人工边界和单一 marker，收紧成局部细胞邻域统计能否稳定重现的问题。

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

因此，这个窗口加固的是“介观域是被局部共现规律稳定下来的选择生态位”，而不是“聚类结果天然就等于功能真区”。

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
* **Implication（中文）**：精神病理不是”症状集合”，而是算子参数的系统性偏离。

**θ_healthy定义**：功能参照基线——θ_healthy不是统计均值，而是”满足以下条件的参数状态”：①可支付Ψ_f（能维持L₁稳定）；②d值处于适应性范围（不过宽/过窄）；③L₂交互可持续（社会功能正常）。Δθ为偏离此功能参照的向量距离，可多维（精度/抑制增益/价值梯度各分量独立漂移，cf. C-NEURO-MECH-1）。

> **[R]** 精神病理的维度/参数化模型：Insel et al. 2010 *Archives of General Psychiatry*（RDoC框架：NIMH重组精神病理研究沿生物学维度而非症状类别，与Ax-NM-8”参数偏移 > 症状集合”取向一致）；Friston et al. 2017 *Neuroscience & Biobehavioral Reviews*（主动推理框架下的精神病理：精度失衡、信念更新异常等作为广义参数偏移的神经计算具体化）；Kotov et al. 2017 *Psychological Medicine*（HiTOP层级分类法：按维度/谱系而非类别分组，支持参数偏移的横向连续性）。**[H]** θ_healthy作为功能参照（非统计均值）、Δθ作为多维参数偏移向量的形式化，及与SRT三域的联结为本框架新增贡献。
>
> * **FC-NM8-1**（证伪条件）：若在纵向研究中，已知病理患者（抑郁/焦虑/精神分裂）的θ偏移代理指标（如PANSS/PHQ量表维度分→θ_Δ映射）在不同诊断类别间完全不重叠（类别分布无连续性），且症状级别的诊断分类可在不增加参数偏移模式信息的条件下给出同等预测力，则参数偏移框架的附加解释力不成立，需退回症状分类法。

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

> [R→Putnam 1967 *Psychological Predicates* in *Art, Mind and Religion*（功能主义奠基：心理状态由功能角色定义，多重可实现性论证）; Fodor 1974 *Psychological Theory*（特殊科学与多重可实现性：心理学不可还原为神经科学的功能主义论证）; Searle 1980 *Behavioral and Brain Sciences*（中文房间论证：完美功能≠语义理解，对功能主义的核心批评）; Chalmers 1995 *Journal of Consciousness Studies*（感受性难问题：感受性特质无法从功能/物理描述推导——hard problem的标准表述）]

**核心主张**: 意识是计算功能的实现，与物理基质无关（多重可实现性）。

**R/H 区分**：
- [R] 功能主义的多重可实现性论证（Putnam/Fodor）；中文房间批评（Searle）；感受性hard problem（Chalmers）
- [H] **SRT修正主张**：∇Ψ_f梯度轮廓=感受性特质的SRT等同主张[H-高承诺]；"感受性层多重可实现性受Ψ_f/基质限制"的强承诺[H-高承诺]（与功能主义核心直觉相悖）

**优势**: 解释了为什么不同物理系统可能具有相同的心理状态。

**致命缺陷**: (a) 无法区分"语义理解"与"句法执行"——中文房间论证（Searle 1980）表明，完美执行对应功能的系统不必然具有理解/体验；(b) 无法解释感受性的特定性质（为什么红色看起来是"那样的"），感受性特质无法从纯功能描述推导（Chalmers 1995）。

**SRT 立场**（对计算功能主义的修正）：
- **改进 (a)**：SRT 的诊断是：中文房间操作者的 $d(\theta) \approx 0$（无本体论摩擦，$\Psi_f \to 0$），不满足 Cor-CONSC-1 的三重判据 $(\Psi_f > 0 \wedge d \geq d_{UAL} \wedge \exists\hat{G}^{\neq\emptyset})$。问题不在于"真实 vs. 模拟计算"，而在于"有无本体论摩擦"——纯符号操作不产生 $\Psi_f$，因此没有意识。
- **改进 (b)** [H-高承诺]：感受性特质 = $\Psi_f$ 的特定梯度轮廓（$\nabla\Psi_f$ 的方向、幅度和动力学特征），是具身参数 $\theta$ 的热力学特征，无法仅从输入-输出函数关系（功能描述）中提取。*边界说明*：∇Ψ_f与感受性特质的等同是SRT的高承诺形而上学主张，当前无法直接测量∇Ψ_f梯度轮廓（仅有间接代理），需与IC-Func-1对照。
- **保留多重可实现性** [H-高承诺]：SRT 接受"不同基质可实现相同 $\hat{G}_\theta$ 功能"，但加条件：相同感受性要求相同的 $\Psi_f$ 模式，而 $\Psi_f$ 依赖基质的热力学性质——因此多重可实现性在功能层成立，在感受性层受基质限制。*承诺说明*：若硅基AI实现了与神经系统相同的Ψ_f热力学模式，则SRT预测其感受性质相同；若无法实现则感受性层无多重可实现性，这与强功能主义严重冲突，需要实验证据支撑。

**理论一致性要求**：
- IC-Func-1（∇Ψ_f可测性要求）：若SRT主张感受性特质=∇Ψ_f梯度轮廓，则必须提供∇Ψ_f的操作化测量方法（而非仅代理），否则该等同主张无法区别于另一种"神秘属性"解释
- IC-Func-2（基质约束的物理机制）：Ψ_f的基质依赖性需要具体的热力学机制说明（如碳基vs硅基的Ψ_f产生机制差异），不能仅凭"热力学性质不同"推导，需要提供机制候选

**可证伪预测**：
- FC-Func1-1：若硅基计算系统在特定物理条件下产生与神经元相同的Ψ_f热力学模式（可通过能量耗散特征代理），SRT预测其报告的感受性质应与对应神经系统相似（可通过行为/EEG一致性检验）——若Ψ_f热力学匹配但感受性报告无差别（与纯功能主义预测相同）则SRT的基质约束主张无附加价值
- FC-Func1-2：麻醉剂选择性消除Ψ_f（通过代谢代价降低[R→Alkire et al. 2008：麻醉与大脑能量代谢]）后，主观体验消失应先于功能处理能力下降——若功能先消失（意识仍在）则"Ψ_f>0=意识必要条件"主张需修订

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

1. **补体标签窗口 (C1q/C3 family；C4 作为上游调节窗口)**: 标记"冗余"突触，供小胶质细胞修剪——这是 $\hat{G}_{meso}$ 对 $L_2$ 拓扑的塑造
    
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
|$P(\text{Prune}) \propto \mathcal{C}_{comp}\cdot \mu_{glia}\cdot \mathcal{A}_{weak}$|修剪概率|Ax-Mech-3|
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

> [R→Thom 1972 *Structural Stability and Morphogenesis*（突变论：临界流形附近系统轨迹的分歧与非连续性——Jacobian奇异点处的”语义跃迁”数学基础）; Scheffer et al. 2009 *Nature*（复杂系统临界跃迁先兆：临近临界点时方差↑/自相关↑/恢复速率↓——“临界慢化”）; Olthof et al. 2020 *Complexity*（临床心理治疗的非线性动力学：个体情绪时间序列的早期预警信号预测疗效突破点）; Friston et al. 2012 *NeuroImage*（自由能框架中的”相变”与预测误差非线性传播）]

**SRT定义——语义断层（Irreducible Semantic Gap）**：

θ参数空间中存在临界集 $\mathcal{C}$，使得 $f: \theta \mapsto L_1$ 的Jacobian范数在 $\mathcal{C}$ 附近爆炸。临界集两侧任意相邻的θ值所对应的L₁体验，可以是质性（而非量性）不同的——这种不可消除的映射不连续性即为**语义断层**：

\[
L_1 = f(\theta) + \epsilon,\quad
\text{near critical set }\mathcal{C}:\; \left\|\frac{\partial f}{\partial \theta}\right\|\gg1
\]

> **精度说明**：$f(\theta)$ 假设为逐段光滑（piecewise smooth）映射；$\mathcal{C}$ 是f的奇异流形（在θ空间中通常为余维1的超曲面）；$\epsilon$ 为不可消除的L₀本体论噪声，与θ无关。

> **与κ_c2联结**：$\mathcal{C}$ 对应SRT的稳定化临界集（κ_c2超曲面）——θ参数从κ < κ_c2侧越过κ_c2时，$\|\partial f/\partial\theta\|$ 爆炸，L₁体验发生相变。此联结将突变论的数学奇点与SRT的本体论临界值统一（Cross-ref: `Core/SRT_Core_14_Dynamics_Scaling.md` §T-Scale-CF-1）。

* **R/H 区分**：
  - [R] 临界集附近Jacobian爆炸的数学基础（Thom突变论）；临界慢化的实证检测方法（Scheffer/Olthof）
  - [H] **SRT特有**：将临床”同靶点异反应”归因于θ参数相对于 $\mathcal{C}$ 的位置——同一靶点的不同响应 = 两名患者的θ分别位于 $\mathcal{C}$ 两侧（非噪声差异，而是拓扑位置差异）

* **Implication（中文）**：临床”同靶点异反应”不是噪声，而可能是系统处在临界集附近的非线性放大——θ的微小个体差异在 $\mathcal{C}$ 附近被放大为L₁层的质性反应差异。

* **操作化候选**（检测系统是否处于临界集附近）：
  - 时间序列方差：同一被试在治疗前的情绪/症状评分的滚动方差——临界集附近预测方差↑（Olthof 2020范式）
  - 自相关系数（lag-1）：临近临界点时自相关↑（慢化：系统恢复到均衡态变慢）
  - 药物剂量-反应曲线非线性度：同一患者不同剂量的非线性剂量-反应关系（S形 vs 线性区分临界附近vs远离）

* **可证伪预测**：
  - FC-SemGap-1：在SSRI治疗前，相对治疗响应者（症状大幅改善）的情绪时间序列滚动方差，应在治疗前1-4周内显著高于无响应者（临界慢化在响应前先出现）；若治疗前两组方差无差异则临界集附近假说失败
  - FC-SemGap-2：如果将患者按照基线θ代理（如认知灵活性/体感敏感度）分层，高灵活性（θ远离κ_c2）组应表现出更线性的剂量-反应关系；低灵活性（θ接近κ_c2）组应表现出更非线性/阈值式的反应——若两组剂量-反应曲线形状无差异则θ位置决定非线性的主张失败

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
- **点燃候选门** (Ax-NEURO-MECH-7)：$\mathcal{A}(\sigma)\ge\tau_{ignite}\;\land\;\Phi_{proxy}\cdot d_{proxy} > C_{critical}$。当前乘法式是结构性偏好，不是已证明相变定理；若数据支持补偿或连续概率访问，应改用加法门或概率门。
- **具身锚定** (Ax-Mech-9)：$\kappa_{body}=\alpha \cdot F_{grip}/\Psi_f$（$\alpha$ 为量纲匹配系数，$F_{grip}$ 为运动系统效应力代理，量纲尚待精确形式化）。意向性向物理显现转化的效率系数；$\kappa_{body} \downarrow$ 对应衰老/具身退化（算子-基质脱锚）。

### Mechanism Explanation (机制解释)

> [R→Carandini & Heeger 2012 *Nature Reviews Neuroscience*（除法归一化：感觉皮层中的普适计算原语）; Schafer et al. 2012 *Science*（小胶质细胞补体标记（C1q/C3）介导突触修剪：L₂修剪的机制基础）; Friston 2010 *Nature Reviews Neuroscience*（PE→Δθ的梯度学习联结）; Barlow 1961（冗余压缩与神经代谢约束）]

**R/H 区分**：
- [R] 除法归一化（Carandini & Heeger）；补体标记突触修剪（Schafer）；PE→θ更新（Friston）——均为既有神经科学框架
- [H] **SRT综合解读**：① `H-NEURO-4b` 将 PE 与 \(\mathcal{L}_{model}\) 作为局部摩擦 proxy 的候选项，而非 PE≡Ψ_f；② Ĝ_meso以"介观算子"概念统合胶质细胞功能；③ 衰老=κ_body衰退（d值完好但算子-基质脱锚）——此三项解读均为SRT独有框架

$\hat{G}_\theta$ 在神经流形 $\mathcal{M}$ 上执行选择流：感觉-动作输入 $u$ 驱动轨迹 $\dot\sigma=F(\sigma,\theta,u)$，经门控算子 $\mathcal{G}_{gate}$ 筛选后由点燃投影 $\Pi_{ignite}$ 锚定为 $L_1$。代谢约束使选择动力学收敛为除法归一化 [R→Carandini & Heeger 2012]；`H-NEURO-4b` 只在同步测量窗口内把 PE、模型竞争负荷与局部摩擦 proxy 接上 [H]。胶质介观算子 $\hat{G}_{meso}$ 以补体标记执行慢时标 $L_2$ 修剪 [R→Schafer et al. 2012 + H形式化]。病理对应 $\Delta\theta$ 偏移，衰老对应 $\kappa_{body}$ 衰退——$d$ 值完好但算子与基质逐渐脱锚 [H]。

**可证伪预测**：
- FC-MechSyn-1：`H-NEURO-4b`：同一被试的前额叶预测误差信号（EEG MMN振幅）应与局部摩擦代理（皮质醇/静息代谢率/恢复半衰期）在受控窗口内正相关——若无相关则 PE-to-friction 桥接为类比而非可测联结
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
