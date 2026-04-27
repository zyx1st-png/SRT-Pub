---
id: SRT-PHIL-ANNEX-11-CONCEPTS
type: interface
tags:
  - Philosophy
  - Interface
  - Annex
status: active_v1
layer: bridge
epistemic_layer: bridge
claim_mode: translation
canonical: false
parent: Philosophy/SRT_Philosophy_Foundations.md
date: 2026-03-08
---

> **Annex file** — extracted from [`SRT_Philosophy_Foundations.md`](../SRT_Philosophy_Foundations.md). Canonical content.

## Concepts Interface（2026-03-08）

这条 interface 真正推进的，不是再定义一次“概念是什么”，而是把概念处理从单一路径神话里解放出来：概念不是一个固定定义包，也不是纯原型、纯样例、纯理论中的某一条独占路线，而更像一组会随任务和带宽重新配重的可重组资源。它也顺手修正了把 `concept` 和 `conception` 混写成同一个东西的旧习惯。

### Def-Phil-CON-1: Concept as Recombinable Deliberative Representation
在 SRT 中，概念定义为可在有意识推理中带宽受限地重组的表征类型：
\[
\text{Concept}(X) \iff R_X \in \mathcal{R}_{delib}\ \land\ \text{Recombinable}(R_X)
\]
其核心不是”固定定义包”，而是可在任务中与其他概念形成结构化组合。

> **SRT 谓词展开**（两个谓词的形式定义）：
>
> **$R_X \in \mathcal{R}_{delib}$（有意识推理可及域）**：$\mathcal{R}_{delib}$ 是个体算子 $\hat{G}_\theta$ 在高 d 值状态下（$d > d_{threshold}$，Semi-open 至 Open 能流区间）可以显式访问和操作的 L₁ 表征子集，对应注意力对内容的自上而下控制窗口。反义：$R_X \notin \mathcal{R}_{delib}$ 指非符号化的感知-运动图式（d 值低，自动化处理，不可被主动拼接）。
>
> **$\text{Recombinable}(R_X)$（可重组性）**：$R_X$ 可以在不丧失指称完整性的前提下与其他 $\{R_{Y_i}\}$ 形成新的结构化组合 $\mathcal{C}(R_X, R_{Y_1}, \ldots, Goal_t)$（参见 Def-Phil-CON-3）。SRT 约束：重组是**带宽受限的**——可形成的组合数量上界由当前 d 值决定（$|\mathcal{C}| \leq \exp(d_{cog})$），而非无限”自由”重组。
>
> **Cross-ref**: $\mathcal{R}_{delib}$ 对应 `Core/SRT_Core_13a §2.1` 中 d 值与认知可及范围的论述；Recombinable → Def-Phil-CON-3（ad-hoc 概念组装窗口）。

### Def-Phil-CON-2: Concept vs Conception Split
采用 Shea 的区分：
- **concept**：指称载体（representation type）；
- **conception**：与该载体可访问的信息簇（prototype/exemplar/theory/characterization）。
\[
\text{Use}(R_X,t)=\Gamma_t\big(\mathcal{K}_{proto},\mathcal{K}_{ex},\mathcal{K}_{theory},\mathcal{K}_{char}\big)
\]
即一次使用中被调度的是情境门控后的 conception 子集，而非完整知识库。

### T-Phil-CON-1: Hybrid Conceptions Theorem
分类与推理的稳健性通常依赖混合结构，而非单一路径（纯定义/纯原型/纯样例）：
\[
\text{Performance}_{cat+infer} \approx f(w_p\mathcal{K}_{proto}+w_e\mathcal{K}_{ex}+w_t\mathcal{K}_{theory}+w_c\mathcal{K}_{char})
\]
权重 \(w_i\) 随任务、压力、文化语境和工作记忆负载动态改变。

### T-Phil-CON-2: Externalist Reference / Internal Selection Coupling

概念指称由外部历史轨迹稳定（externalism），具体分类由内部算子在该约束下展开：

$$R_X \xleftarrow{\text{stabilized by}} L_2^{social}(\text{causal-historical chain})$$

$$\text{Categorization}_t(X) = \hat{G}_\theta[L_0 \mid R_X] \quad (\theta\text{-specific unfolding})$$

**机制说明**：

- **指称的 SRT 翻译**：克里普克「因果历史命名链」= 多个 $\hat{G}_\theta$ 在不可逆时间轴上对同一对象反复进行 $L_0 \to L_1$ 选择后，在 $L_2$ 刻下的迟滞结构（Hysteresis）。语义不悬在空中，而是沉积于跨算子的历史选择轨迹之中。
- **分类的 SRT 翻译**：$\hat{G}_\theta[L_0 \mid R_X]$ 表示个体算子在 $R_X$（$L_2$ 社会指称约束）的条件下，从潜在域坍缩出属于自身 θ 的 $L_1$ 概念切片——同一指称，不同 θ 展开出不同的概念结构（专家 vs. 非专家）。

**两个推论**：

1. **「同指称但不同理解」**：$R_X$ 由 $L_2^{social}$ 统一锚定，$\hat{G}_\theta[L_0 \mid R_X]$ 因 θ 不同而产生不同的 $L_1$ 展开。沟通功能有效，是因为外部指称同构，而非 $L_1$ 现象学同构（参见 T-ONT-8d：沟通 = 共同符号带来注意力预期满足，不要求内部 $L_1$ 完全一致）。这解答了维特根斯坦「甲虫盒子」问题：我们无需钻进别人的 $L_1$，$L_2$ 的外部抓手已保证沟通的语义基础。

2. **「可错分类但语义不崩」**：单次分类错误（如把铜认作黄金）是单个算子偏离 $L_2$ 势阱底部的高自由能涨落。只要涨落能量无法克服集体自由能景观的拓扑壁垒 $|\text{Hess}(\mathcal{F}_{coll})|$，系统就会被社会纠错机制（他人纠正、感知反馈）立即拉回谷底，$L_2$ 语义结构不受影响。现实的「语义刚性」= 势阱曲率，而非每次应用的正确率（参见 SRT_Core_12b::社会迟滞与共识摩擦）。

### Def-Phil-CON-3: Ad-hoc Concept Construction Window

[R→Barsalou 1983（ad-hoc概念的原始研究：目标导向的临时概念）; Shea 2026（《Concepts》：hybridism与generality constraint）] [H→SRT将ad-hoc构造形式化为目标驱动的L₀→L₁投影重组]

概念可在情境中临时组装（ad-hoc）以满足当前目标：
\[
R_{adhoc}=\mathcal{C}(R_{i_1},R_{i_2},...,Goal_t,Context_t)
\]
如”garage-sale items”一类任务特定概念，体现 SRT 的目标驱动结构压缩能力。
- **SRT解读**：ad-hoc概念 = $\hat{G}_θ$ 在当前 Goal_t 约束下将多个L₂概念节点临时合并为新的L₁锚点；”临时性”体现在θ的短暂激活模式，而非θ结构的永久改变

更稳的读法因此不是“概念有一个唯一正确本体”，而是：概念的稳定性主要落在共享指称与可重组约束上，至于每次调用到底偏原型、偏规则还是偏理论，则要看当前任务、压力和可用带宽如何重新配重。

### 分类映射表（Concept Processing Regimes → SRT）

[R→Smith & Medin 1981（经典规则理论）; Rosch 1978（原型理论）; Murphy & Medin 1985（理论驱动分类）; Barsalou 1983（ad-hoc概念）] [H→以SRT三变量（d值/能流/Ψ_f）重映射四种概念加工模式]

| 外部分类（认知科学） | d-value 区间（proxy，示意） | 能流特征 | \(\Psi_f\) 状态 | 代表文献 |
|---|---|---|---|---|
| 规则/定义主导分类 [R] | 中~高（需要主动推理） | Semi-open（显式运算） | 中负载 | Smith & Medin 1981 |
| 原型/样例快速分类 [R] | 中（并行相似度计算） | Open↔Semi-open（并行启发） | 低~中负载 | Rosch 1978 |
| 理论驱动概念推理 [R] | 中高（结构推演需要关切带宽） | Open（结构推演） | 中~高负载可支付 | Murphy & Medin 1985 |
| 情境即席概念构造 [R→Barsalou 1983] [H→SRT形式化] | 中~高（目标驱动激活） | Open（目标约束重组） | 边缘高负载但高收益 | Barsalou 1983; Shea 2026 |

**证伪候选**：若原型分类（快速启发）和规则分类（显式推理）在d值代理（注意力带宽）上无可区分差异，则SRT以d值轴区分四种模式的框架需重新操作化。

### [Lineage/Source]
- [R→Nicholas Shea (2026), *Concepts*]：generality constraint（概念须跨实例泛化）、hybridism（多机制并存而非单一理论）、externalism（概念内容部分由外部世界决定）、ad-hoc concepts（目标驱动的即席构造）、concept/conception区分
- **SRT附加**[H]：将Shea的hybridism解读为θ参数化的多模式加工（不同θ→不同概念加工主导模式）；concept/conception区分对应L₂共享指称vs L₁个体展开（参见lines 1634-1637）

## 【理论边界/防误用声明】
本段边界声明已 annex 化；详见 `Foundations_Annex/00_General_Boundary_Block.md`。
