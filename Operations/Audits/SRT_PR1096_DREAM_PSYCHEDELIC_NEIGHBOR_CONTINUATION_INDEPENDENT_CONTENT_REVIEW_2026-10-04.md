---
id: SRT-PR1096-DREAM-PSYCHEDELIC-NEIGHBOR-CONTINUATION-INDEPENDENT-CONTENT-REVIEW-20261004
type: audit
status: active
date: 2026-10-04
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_DREAM_PSYCHEDELIC_SELECTION_CONSTRAINT_RECONSTITUTION_2026-10-04.md
  - Operations/Audits/SRT_DREAM_PSYCHEDELIC_MATURE_NEIGHBOR_CONTINUATION_AUDIT_2026-10-04.md
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
  - Operations/_SRT_MATERIAL_PIPELINE.md
tags: [IndependentReview, PR1096, Dream, Psychedelic, MatureNeighbor, SourceFidelity, ActiveInference, Christoff, Simondon]
---

# PR #1096 独立内容评审 — 梦境 / 迷幻剂直觉的成熟邻居延续审计

> **角色**：合并前独立内容评审。只读：不修改 #1096 的任何文件，也不改 STATUS、cognition owner、HP-B、NEURAL35 或 canonical owner，不合并。
>
> **评审者独立性**：独立 session，没有参与 #1096 的写作和前序对话。
>
> **范围**：#1096 的 9 个文件全部通读。对照了仓库内 owner：cognition programme CN-2 / E-ladder、Pass19、`03_Bridges/SRT_Processual_Bearer_Constraint_Bridge_2026-08-23.md` HEF-3/HEF-4、HP-B hook、NEURAL35，以及 `Operations/_SRT_MATERIAL_PIPELINE.md` 的 B 类规则。外部来源通过网络搜索核实；出版社页面（nature.com、wiley.com）、arXiv 和 Crossref 都被本环境的出口代理拦截，所以下文核实的程度按条注明。

## 0. 评审对象

```text
PR:    #1096 (OPEN, draft) “research: dream/psychedelic intuition mature-neighbor continuation audit”
head:  d8e8aa11   base: 4f0db8c5 (= 当前 main)
files: 6 new + 2 routing-only modified (+ 1 new Material Log part)
CI:    governance-preflight = success
```

本地复核：

- `scripts/check_material_log_consistency.py` → `PASS … latest=2026-10_Part01:4 total=254 A=167 B=37 C=50`。
- 两份新文件的 dependency 路径和各 SourceCard 中行内引用的 `.md` 路径全部存在。
- 9 月份分卷确为 10 行（5 A + 5 B），README 把“nine”更正为 10 是对的。
- 本地完整 preflight 有 2 项失败（context bundle），原因是浅克隆；`main` 上同样失败，与本 PR 无关。CI 的完整克隆是绿的。

## 1. 总体判断

```text
结构 / 治理边界      = PASS
owner 一致性          = PASS
来源忠实度            = 需修正（R2、R6，及 R1 中的 Friston 部分）
成熟邻居矩阵完整性    = 需修正（R1：缺少最近的同靶点邻居）
残余问题是否同靶点    = 尚未达到（R3）
作者来源标注          = 需澄清（R5）
建议                  = 修正 R1–R6 后再合并；R7–R8 可在同一次推送中顺带处理
```

PR 自己声明不做的事（不改 canonical / STATUS / CURRENT NEXT / HP-B，不新增术语，不建梦境 / 迷幻剂 programme，不作 novelty 声明）全部守住了。审计 §2 的五条内部 owner 约束都和现行 owner 文本一致：Pass19 的被动沉积退位、E4 ≠ history writeback、HP-B 的 `state update != Position reconstitution`、HEF-4 要求独立的 rule / boundary / composition 重写证据、NEURAL35 的 `reopening != reselectability`。下面的问题都出在**邻居覆盖和来源忠实度**上，不在治理边界上。

## 2. 发现（按严重性排列）

### R1（高）缺少最近的同靶点成熟邻居：Hobson–Friston 的“梦境 = 离线生成模型”

作者的原句是“梦境和迷幻剂都是一种**缺少选择的内部结构展示**”。对“梦境展示内部（生成）结构”这一说法，最直接的成熟邻居是主动推断 / 预测加工里的梦境理论：

- Hobson & Friston (2012), *Waking and dreaming consciousness: Neurobiological and functional considerations*, Progress in Neurobiology 98(1)：REM 梦境被看作生成模型在没有感觉输入约束时离线运行，功能是优化模型（降低复杂度）；
- Hobson, Hong & Friston (2014), *Virtual reality and consciousness inference in dreaming*, Frontiers in Psychology 5：梦境作为内部生成的“虚拟现实”；
- Friston et al. (2017), *Active inference, curiosity and insight*, Neural Computation 29(10)：三球范式的原始出处，把 Bayesian Model Reduction 和睡眠联系起来。

本 PR 自己的 B1 卡片来源（Friston et al., arXiv:2512.21129 版本）的摘要也写到：Bayesian Model Reduction “evinces mechanisms associated with sleep”，并带有“aha”时刻的全部特征。也就是说，B1 卡片的来源本身就对“梦境 / 睡眠中的结构”提出了一个主动推断式解释，但卡片和审计都没有记下这一点。

后果：

1. 审计 §3 矩阵里，“梦境作为对内部结构的展示”这一解释职能没有被分配给它的 source-native owner。矩阵用 Christoff（约束空间）和 REBUS（迷幻剂）来做减法，可两者都不是作者原句的同靶点竞争者。
2. 对审计 §4 的“strongest combined rival”而言，Hobson–Friston 是唯一一个**同时**在梦境、生成模型和结构学习三处都有现成形式化的邻居。少了它，组合竞争者被低估了。
3. 仓库其实已经有这条线索：`Philosophy/SRT_Philosophy_Foundations.md` 第 1027 行把 Hobson & Friston 2012 列为“睡眠/梦境与幻觉的PP解释”。所以这不是新材料，而是没有对接上。

建议：在审计 §3 加一行“offline generative-model display / optimisation during sleep”，owner 写 Hobson–Friston + 2017 年 curiosity/insight + 2026 年 artificial reasoning；在 Friston 卡片 §2 或 §5 记下“来源本身把 BMR 和睡眠联系起来”；照惯例只需 U-mode INHERIT，不必新建 SourceCard（也可以视需要补一张 B2）。

### R2（中高）Christoff 卡片对梦境位置的归属可能不忠实

Christoff et al. (2016) 的框架用两条轴：deliberate constraints 和 automatic constraints。按 Christoff 实验室后续的更新文献（Girn et al. 2020, *Updating the dynamic framework of thought: Creativity and psychedelics*）的概括，梦境处在 **deliberate 和 automatic 约束都低**的区域，是比走神更“自由流动”的状态，而不是“deliberate 低、automatic 强”。

而 #1096 在几个地方把后一种组合算到 Christoff 名下：

- 卡片 §1：“already pays a large part of the broad claim that dreaming can combine reduced deliberate control with strong automatic / affective structuring”；
- Material Log 行：“‘低 deliberate control + 强 automatic/affective structuring’ 已有成熟解释”；
- 审计 §8.1：“automatic affective / relational constraints can remain strong … Christoff-like constraint models must be given full explanatory access”。

卡片 §2.4 的措辞（“dreaming is treated as a case with weak deliberate constraint, while **other states** can remain strongly constrained by automatic processes”）本身是对的，但 §1 和 Material Log 把它推得太远了。

这影响的不只是措辞。如果 Christoff 原框架把梦境放在两轴都低的位置，它预测的是**弱结构、快转移**的内容。那么作者直觉里“结构展示”这一半，恰恰**不**被 Christoff 吸收，而是落到别处：Hobson–Friston（R1），以及威胁模拟 / 连续性假说一类梦境内容理论。目前的结论 “less deliberate control → structured automatic unfolding = SOURCE-OWNED” 把两件事并在了一起。

建议：对照 2016 原文 Fig. 1 及正文中关于梦境的段落重新核对。若确认原文是“两轴都低”，就把 §1 和 Material Log 改成“Christoff 只拥有 *deliberate 约束减弱* 这一职能；dream 中强情感 / 关系结构的存续须另找 owner（R1 等）”。注意：本评审没能打开原文 PDF，这一条依据的是 Christoff 实验室 2020 年更新论文的概括，所以需要 PR 作者对照原文确认。另外，Girn et al. (2020) 本身就把 dynamic framework 和 REBUS / 迷幻剂接在一起，可以作为可选的 B2 交叉引用。

### R3（中）OPEN 残余还不是同靶点残余；“组合竞争者”混了两种角色

这一条回答评审焦点 #4。

**(a) 角色混淆。** 审计 §4 / §12 要求残余在 held-out 预测、因果、递归增益上胜过一个“fair combined rival”，而这个组合竞争者包括 Simondon、enactive autonomy、SIF。可后三者不是能在 held-out 探针上跑出预测的模型。它们的合法作用是**所有权比较项**（阻止 SRT 在某个解释职能上声称新颖），不是**操作基线**。真正能在 E2–E4 中当基线跑的，只有结构学习 / 主动推断模型、灵活的潜状态模型、Christoff 式约束模型，以及 arousal / affect / attention 协变量模型。建议在 §4 显式拆成两个列表：ownership comparators 和 operational baselines。§12 的残余只应该针对后者。

**(b) “coordinated”本身不具区分力。** 主动推断的结构学习一旦切换模型结构，下游的分组、候选、转移预测本来就会**一起**变。所以“一次变化同时重组多个 held-out 探针”在结构学习竞争者那里是默认预测，不是它会失败的地方。审计 §13.2 的失败条件已经部分覆盖了这一点，但残余本身没有写出任何**方向性的分歧预测**：SRT 一侧具体预测出现哪种模式，而带 BMR 的结构学习模型预测不出来？

**(c) 与现有 owner 的关系。** 去掉 (a) 之后，§12 的残余在实质上就是 cognition programme CN-2 已有的 H3 reduction / increment / recursive 三项检验，只是竞争者集合升级了。这本身是正当的结论，但审计应该**这样说出来**（“残余 = 现有 CN-2 H3 检验，竞争者升级为含结构学习的 H2”），而不是把它写成一个新的“exact OPEN residual”。否则它看起来像是成熟机制的并集换了个名字（即焦点 #4 担心的情况）。

小的措辞点：CN-2 明确说 H1/H2/H3 “不是互斥的竞争者”，H2 是 reduction test 的约简基础。审计 §5 里的 “the current H2 comparator” 最好改成 “the H2 reduction base in CN-2's reduction test”，与 owner 保持一致。

### R4（中）Simondon 修正还不够强；“cross-formation continuity” 被当成了标题

这一条回答评审焦点 #2。

审计 §10 正确地撤回了 `operation -> structure -> later operation` 这一新颖性主张，但收窄后的残余是：

> whether a single typed dependency can connect pre-position formation with post-formation position-indexed rebuilding of selectability …

这仍然和 Simondon 的核心论点重叠。在 Simondon 那里，个体携带着**前个体实在的负荷**（charge of preindividual reality），正是这份负荷推动后续的心理个体化和集体（transindividual）个体化。“同一种依赖把形成前和形成后的再构接起来”，是 Simondon 本来就有的主张。收窄后剩下的区分词（position-indexed、consequence-bearing、objectification typing）全是 SRT 自己的词汇。按审计 §13.7 自己的失败条件（“only remaining advantage is shorter SRT vocabulary”），这里需要先对着 preindividual charge / transindividual 做一次显式比较，才能把它保留为 OPEN。

另外，PR 正文说不引入 “cross-formation continuity” 这一术语，可 trace §8 和审计 §10 都把它用作节标题。按 AGENTS.md 的新术语规则，建议在第一次出现时标注 “working label only; not a term-of-art; merge/failure condition = R4 Simondon comparison”，或者改成描述性标题。

### R5（中）作者来源标注：“accepted”和“converged”的主语不清楚

trace 的 authority guard 写得对（只有 seed 原句是 A0-Q，“认同，继续”只授权方向上的延续）。但正文用了几处容易被读成作者裁决的措辞：

- §4 标题 “Mature-neighbor subtraction **accepted** during the dialogue”；
- §7 “The dialogue **converged** on a sharper residual”。

在本仓库里，“convergence”专指作者的实质研究决定。建议：(i) 引用作者在对话中的实际回复原文（至少注明对哪一轮回复了“认同，继续”）；(ii) 把 §4 和 §7 的主语改成 “machine-proposed, carried under directional continuation”，以符合 `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONTINUE_DIRECTIONAL_ACCEPTANCE_2026-09-24.md`。

还有一个与 R1 相连的实质点。trace §2 把“缺少选择”分解成 deliberate/meta 约束、anchoring/reality calibration、candidate accessibility 三项，然后再排除 “primitive Selection absent”。它**没有列出**另一种读法：“缺少选择” = 缺少**外部 / 感觉一侧**对内部生成组织的选择压力，也就是离线生成。这一读法恰好是 Hobson–Friston 的靶点，而且可能比“deliberate control 减弱”更接近作者原句的意思。按 Constitution / Ontology Dialogue Hard Guard（从作者的问题出发，带着邻居意识呈现选项），这种读法应该作为一个选项交还给作者，而不是由机器代为排除或代为选择。trace §11 的 root return 把作者关于“展示了什么”的问题直接改写成“哪种组织能改变自身后续生成的条件”（也就是现有 E4 的负担）。这一步方向上合理，但它是一个**重定向**，应该标为待作者确认。

### R6（中低）Bonamino & Peters：把 agency 写成了 “deliberate agency”

经搜索核实：Bonamino & Peters (2026, JSR e70449, 2026-09-11) 存在，题名、作者、日期都和卡片一致。来源区分了 lucidity、agency 和 control，也区分了 agentic 和 non-agentic control。但来源说的 sense of agency **不一定意味着刻意控制**，而是一种更基础的、前反思的、对“发起并经历行动”的体验。

#1096 在 trace §6（“deliberate agency”）、卡片 §5（“deliberate agency”）和审计 §8.2 的测量清单中，把 agency 写成了 deliberate agency。这恰好把来源要分开的两件事（前反思的 agency 与 agentic / deliberate control）又并回去了。建议把测量维度改为：lucidity；sense of agency（前反思）；agentic vs non-agentic control；successful control；再加上 SRT 一侧的更强指标。

另外，卡片 §5 “Source-backed pressure” 下的第 4 项（“the stronger proposed change in the organizing conditions of later generation”）是 SRT 一侧的补充，应该移到 “SRT-side synthesis” 下面，以免在形式上混入来源一侧。

### R7（低）Friston 卡片的书目核实

这一条回答评审焦点 #1。

**内容方面：卡片公平。** 结构学习一面（区分状态、参数、结构三类不确定性；对模型结构的期望信息增益；BMR；三球范式；在 prior model space 内推理）和局限一面（“the agent knows the generative model under which the (unknown) rule is implemented; as opposed to having to learn the generative model from sampling some unsegmented sensory input, such as a pixel array”）都和 arXiv 版本一致，局限的引用经搜索核实为原文措辞。卡片第 7 节的 “the paper's limitations are not evidence that SRT fills the gap” 是对的。唯一缺漏是 R1 中的睡眠 / BMR 联系。

**书目方面：** 本评审只能确认 arXiv:2512.21129（2025-12-24，作者名单一致）。Nature Communications 17:10125 / DOI `10.1038/s41467-026-77209-5` / 2026-09-08 无法在本环境核实（出版社和 Crossref 被拦截，搜索没有命中）。卡片的 §2 anchors 用的是期刊版节标题，如 “Methods, ‘Active inference, learning and selection’”。建议在卡片 frontmatter 增加 `preprint: arXiv:2512.21129`，以便有人日后复核。这不构成阻断，但 B1 的定义要求“已有一手锚点”。

### R8（低）Pipeline-1 比例与小处

这一条回答评审焦点 #5。

- **分级是恰当的。** Friston 判 B1（可转 A 候选：日后作为 CN-2 的强 H2 基线落点）符合 `_SRT_MATERIAL_PIPELINE.md` B1 的定义；另外三张判 B2 guardrail 也合适。四张卡都有绑定工作线事件的复活触发条件，符合 2026-07-20 规则 1。
- **B2 卡片写得过深。** 按规则 3，B2 应写成**档案卡**（来源事实 + 一句边界 + 触发条件）。Christoff、REBUS、Bonamino 三张都带有完整的 “Owner-side novelty probe” 和 SRT-side synthesis。这不算违规，但与“深度匹配命运”的减负原则不一致，以后要多维护一份。可以接受，下一次推送时可以酌情精简。
- **REBUS 的 Material Log 落点。** “落点”列写了 `NEURAL35`，但本 PR 没有修改 NEURAL35，NEURAL35 本身也不引用 REBUS（已 grep 确认）。建议把落点改成 “NEURAL35 (cross-read only, not landed)”，或者从“落点”列移到备注。
- 根目录 `_SRT_MATERIAL_LOG.md` 的 `## Current note` 仍然停在 2026-09-16。这个文件过去也不是每条都记，所以不是必须改，记下供参考。

## 3. 对 PR 评审焦点的逐条回答

| # | 焦点 | 结论 |
|---|---|---|
| 1 | Friston 卡片是否公平陈述了结构学习的强项和“给定生成模型族”的局限 | **是**（局限已核实为原文措辞）；但遗漏了来源自身的睡眠 / BMR 联系（R1），书目只能核实到 arXiv 版本（R7） |
| 2 | Simondon 修正是否足以阻止重新认领 `Operation -> Structure -> later Operation` | 对这一句**足够**；对收窄后的残余**不够**，因为它仍与 preindividual charge / transindividual 重叠（R4） |
| 3 | 审计是否把 Position reconstitution 偷偷带进了中性认知学表述 | **没有**。§2.4 和 §12 守住了 HP-B 门；“recutting”与 cognition owner 用词一致。唯一的形式性混入是 Bonamino 卡片 §5 的第 4 项（R6） |
| 4 | 剩下的 OPEN 残余是不是真的同靶点，而不是成熟机制并集的换名 | **还不是**。去掉非操作性的比较项之后，它就是 CN-2 现有的 H3 检验；“coordinated”不具区分力；缺少方向性的分歧预测（R3） |
| 5 | B1/B2 分级是否恰当 | **恰当**；B2 卡片写得比规则 3 要求的深；NEURAL35 的落点标注需要修正（R8） |

## 4. 建议的修正顺序（最少改动）

1. 审计 §3 加入 Hobson–Friston 一行；Friston 卡片记下睡眠 / BMR 联系（R1）。
2. 对照原文核对 Christoff 的梦境位置，修正卡片 §1、Material Log 行、审计 §8.1（R2）。
3. 审计 §4 拆分 ownership comparators 和 operational baselines；§12 改写为“现有 CN-2 H3 检验 + 升级后的竞争者”，并要求先写出一条方向性的分歧预测（R3）。
4. 审计 §10 加上 Simondon preindividual charge / transindividual 的显式比较；“cross-formation continuity” 标为 working label（R4）。
5. 在 trace 中修正 accepted / converged 的主语，并把“外部 / 感觉选择缺失”这一读法列为交还作者的选项（R5）。
6. Bonamino 的 agency 维度和 §5 归位（R6）；Friston 卡片补 arXiv 号（R7）；REBUS 落点标注（R8）。

以上全部是对 #1096 自身文件的局部修正，不需要改任何 owner，也不需要作者先做理论裁决。唯一的例外是 R5 后半：“缺少选择”的第三种读法要不要采纳，归作者决定。

## 5. 核实来源

- Friston et al., *Active inference and artificial reasoning*, arXiv:2512.21129 — <https://arxiv.org/abs/2512.21129>
- Bonamino & Peters, *Lucid Dream Control: Mechanisms, Challenges and Future Directions*, JSR e70449 — <https://onlinelibrary.wiley.com/doi/10.1111/jsr.70449>
- Christoff et al. (2016), NRN — <https://www.nature.com/articles/nrn.2016.113>
- Girn et al. (2020), *Updating the dynamic framework of thought: Creativity and psychedelics* — <https://www.christofflab.ca/wp-content/uploads/2020/03/Updating-the-dynamic-framework-of-thought-Creativity-and-psychedelics.pdf>
- Friston et al. (2017), *Active inference, curiosity and insight* (UCL Discovery) — <https://discovery-pp.ucl.ac.uk/id/eprint/1570070>

## 6. 修正后复核（#1096 head `66adaec0`）

> **范围**：作者在 #1097 请求做一次修正后内容复核，重点有三：Hobson–Friston 的刻画是否足够窄；伪新残余是否彻底清除；作者来源标注是否干净。本节通读了 #1096 自 `d8e8aa11` 以来 6 个 commit 涉及的 6 个文件。仍是只读评审。

### 6.1 R1–R8 落实情况

| # | 状态 | 核对结果 |
|---|---|---|
| R1 | 已解决 | trace §4.2、审计 §3 新增一行、§8.2 和 §11 引入了 Hobson–Friston；Friston 卡片 §2.4 / §5 记下了 BMR 作为 introspection / sleep 的离线过程；§13.3 新增“梦境特有效应被离线生成模型 / 感觉脱耦解释吸收”这一失败条件 |
| R2 | 已解决 | Christoff 卡片 §1 / §2.5–2.6、Material Log 行、审计 §8.1 都改为“deliberate 约束最低；automatic 约束可在 low-to-medium 范围”，并显式收回了“强 automatic / affective”这一归属。“low-to-medium”的措辞本评审仍未能对照原文 Fig. 1 核实，但方向与 Christoff 实验室 2020 年的概括一致，可以接受 |
| R3 | 已解决 | 审计 §4 拆分了 ownership comparators 和 operational baselines；§1 / §7 / §12 撤回了 “exact OPEN residual”，归回 CN-2 的 reduction / increment / recursive 三项检验，并把 H2 的约简基础升级；§2.5 与 CN-2 的“分层而非互斥竞争者”一致；“coordinated”不具区分力也已明写 |
| R4 | 已解决 | 审计 §10 和 trace §8 撤回了收窄后的单一类型依赖残余；比较项写全了 preindividual charge 和 transindividual；“cross-formation continuity” 不再保留为工作标签，并进入 trace §10 的 non-decisions |
| R5 | 基本解决（见 P1） | trace 的 author_status、authority guard 和 §4 标题都改正了；“缺少选择”列出 A / B / C 三种读法，§2 和 §11 都声明不代作者选择 |
| R6 | 已解决 | Bonamino 卡片、trace §4.4 / §6、审计 §8.3 都改为“前反思的 sense of agency ≠ deliberate / agentic control”；SRT 一侧的测量项单独标为 “SRT-side addition, not a source claim” |
| R7 | 已解决 | frontmatter 增加了 `preprint: "arXiv:2512.21129"` |
| R8 | 已解决 | REBUS 行的“落点”列只剩 SourceCard 和审计，NEURAL35 移到融入状态列，标为 read-only cross-read；三张 B2 卡片已精简到接近档案卡的深度 |

### 6.2 对三个复核重点的回答

**(1) Hobson–Friston 的刻画是否足够窄：是。** trace §4.2 只认领 “reduced sensory constraint → offline internal generative-model operation / reduction” 这一职能；trace §10 明确不把 Hobson–Friston / Active Inference 视为梦境的完整解释；审计 §8.2 加了 “does not prove that dreams transparently expose a latent structure”；Friston 卡片的 hard guard 也写了 “sleep-associated offline model reduction != transparent display of a true hidden ontology”。范围合适。

剩下一处是标注问题：Hobson–Friston 在 #1096 中没有 SourceCard，也没有原文锚点（审计 §14 如实写了 “existing repository citation / neighbor routing only”），但审计 §1 的 “Source fidelity … PASS AT CURRENT BOUNDED DEPTH” 读起来像是覆盖了全部邻居。建议在 §1 补半句 “Hobson–Friston characterised at citation level only; not source-carded”（见 N1）。

**(2) 伪新残余是否彻底清除：是。** 审计 §1 / §7 / §12 / §14 和 trace §5 / §7 一致地写着 “new exact OPEN residual = NO”，并归回 CN-2；trace §7 的 “This PR does not manufacture a directional SRT prediction merely to preserve a residual” 正是正确的处理。审计 §5 保留的 “factorization / state-variable / boundary constitution question stays OPEN at the programme level” 是 programme 层面已有的 OPEN，不是新残余。§8.4 的 negative-control 逻辑明确标为 design idea only。没有发现被换个名字重新带回来的残余。

**(3) 作者来源标注是否干净：还差一处（P1）。**

### 6.3 新发现

**P1（中）把一个未保存为原文的现象学直觉归给了作者。** 有两处出现：

- `Materials/2026/SRC_2026_10_04_CogSci_Christoff_Spontaneous_Thought_Dynamic_Framework.md` 第 73 行：“Therefore **the user's phenomenological intuition** that old affective / authority structures can remain dominant in dreams …”；
- `Operations/Material_Log/2026-10_Part01.md` 的 Christoff 行，SRT 反哺：“**用户关于旧情绪/权威结构反复占优的现象学直觉** …”。

trace §1 保存的唯一作者原句是“我觉得梦境和迷幻剂都是一种缺少选择的内部结构展示”，里面没有“旧情绪 / 权威结构反复占优”的内容。修正前的版本（旧 Bonamino 卡片 §5）把同一个假设标为 “The current dialogue proposes … This is an SRT-side hypothesis”，修正后的 trace §6 也把它写成 “a phenomenological hypothesis requiring its own source and measurement”。所以这两处等于在修正中**新增**了作者归属。

修法二选一：(a) 如果作者确实在对话中说过，就把原话作为第二条 A0-Q 引文补进 trace §1，两处改成指向这条引文；(b) 如果没有说过，就改为 “a dialogue-generated phenomenological hypothesis (not an author quote)”。另外，仓库文件里用 “user / 用户” 指作者，与 trace 一贯使用的 “author” 不一致，建议统一。

**N1（低）** 见 6.2 (1)：在审计 §1 的 source-fidelity 判定里注明 Hobson–Friston 只到引用层级。附带一点：审计 §3 写的是 “Hobson & Friston 2012/2014 line”，但 2014 年那篇的作者是 Hobson, Hong & Friston，可以写全。

**N2（低）** Friston 卡片的局限一句从 “assumed to know the generative model …” 改成了 “has already learned the generative model of the task / puzzle”。本评审此前经搜索核实的原文是 “the agent knows the generative model under which the (unknown) rule is implemented”。“learned” 也许出自原文别处，但如果没有对应锚点，建议回到已核实的 “knows” 措辞，或者注明 “learned” 出自哪一节。

### 6.4 复核结论

```text
R1–R8                    = 已落实（R5 余 P1）
Hobson–Friston 刻画范围  = 足够窄
伪新残余                 = 已彻底清除
作者来源标注             = 还差 P1 一处（两个位置）
建议                     = 修正 P1 后，内容层面可以合并；N1–N2 可在同一次推送中顺带处理
```

### 6.5 作者对 R5 的裁决（#1096 head `851c01e4`）

作者在 #1097 上回复了 R5，#1096 随后在 `25aec5a` / `851c01e` 中把裁决落进了仓库：

```text
作者原话（2026-10-04）： “r5 c”
裁决： “缺少选择”的主要本意 = Reading C：reanchoring / reselective control 减弱
Reading A（deliberate / meta 约束减弱）、Reading B（外部 / 感觉选择压力减弱）
       = 次要的成熟邻居机制，可能同时出现，但不是作者原句的主要本意
```

**落地方式核对：合格。**

- 作者原话 “r5 c” 逐字保存在 trace §2；trace 和审计 frontmatter 的 `author_status` 都限定为 “R5 interpretive choice C author-adjudicated”，邻居减法仍标为机器评审，没有把这次裁决扩大成对整个包的确认。
- trace §10 把裁决列为本 trace 唯一确立的作者层决定；trace §5 和审计 §2 都写明这次澄清不产生新的判别器或残余，科学路由仍是 CN-2。这和 6.2 (2) 的结论一致。
- Hobson–Friston 在 trace §2 / Reading B 和审计 §8.2 中降为 “secondary mature-neighbor mechanism, not the primary intended meaning”。处理正确。
- 这次裁决也了结了原 R5 后半提出的问题：原 §11 把作者的问题改写成“哪种组织能改变自身后续生成的条件”，那是机器做的重定向；现在作者选了 C，等于作者本人认可了这一方向。

**裁决带来的后续问题。** 作者选定 C 之后，#1096 的邻居减法仍然主要围绕 A（Christoff）和 B（Hobson–Friston）组织。对 C 本身，目前只列了 NEURAL35 和 cognition programme 这两个**仓库内**的守卫。按 U-mode 的要求，作者选定的读法也需要先做同靶点的成熟邻居减法：

- **A1（中）C 的外部成熟邻居没有列出。** 在梦境一侧，“生成照常、但难以察觉 / 重构 / 跳出当前组织”这一职能已有现成的成熟解释：
  - 梦境的 single-mindedness，即对怪异内容不加批判地接受（Rechtschaffen 1978, *Sleep*）；
  - REM 期背外侧前额叶失活与反思 / 现实检验减弱（Maquet et al. 1996, *Nature*；Muzur, Pace-Schott & Hobson 2002, *Trends in Cognitive Sciences*）；
  - 把清醒梦看作元认知恢复的文献（如 Kahan & LaBerge 1994）。

  值得注意的是，清醒（意识到“这是梦”）本身就是一次典型的 reanchoring / 现实再校准，所以 Bonamino & Peters 那一行实际上也是 C 的直接比较项。在迷幻剂一侧，REBUS 管的是 opening，NEURAL35 管的是 `reopening != reselectability`，覆盖是够的。建议在审计 §3 加一行 “reduced reflective / reality-monitoring / reframing during dreaming”，owner 写上述文献，作用写 ownership comparator 加 dream-assay operational baseline。这些文献本评审没有在本 session 对照全文核实，只作为建议的比较项列出。

- **A2（中）需要写明 C 和 A 在操作上怎么区分，否则 C 会被 A 吸收。** “reopen / compare / reframe / reanchor” 都是典型的执行 / 元控制功能，单看措辞，C 很容易被读成 A 的子集。如果那样，Christoff 加上前额叶失活就整体支付了 C。两者其实可以区分，而且部分预测方向相反：
  - A（deliberate 约束减弱）在 Christoff 框架下预测**更自由、更快**的转移；
  - C 预测**更难退出**当前继承的组织：不察觉不一致、不重构、不回锚，表现为对当前框架的黏着。

  建议在 trace §2 Reading C 下补一句这个区分，并注明：如果在具体探针上分不开，就回落为 A 的子情形（SOURCE-OWNED AT THIS EXPLANATORY JOB）。这只是让作者选定的读法可检验，不需要新残余，也不改变 CN-2 路由。

- **A3（低）** 审计 §3 矩阵中 Hobson–Friston 那一行的最后一列仍写 “same-target dream neighbor”。trace §2 已改为 “same-target neighbor for dream-specific offline-generation mechanisms”，建议矩阵也同步，写成 “same-target for Reading B / offline-generation mechanism; not the author's primary meaning”。

**6.3 中的 P1、N1、N2 在 `851c01e4` 上仍未处理：**

- P1：Christoff 卡片第 73 行仍写 “the user's phenomenological intuition…”；Material Log 的 Christoff 行仍写 “用户关于旧情绪/权威结构反复占优的现象学直觉”。这次作者对 R5 的回复只有 “r5 c”，没有涉及这条直觉，所以 P1 的两种修法仍然适用。
- N1：审计 §1 仍是笼统的 “PASS AT CURRENT BOUNDED DEPTH”；§3 仍写 “Hobson & Friston 2012/2014”。
- N2：Friston 卡片第 71 和 89 行仍写 “already learned”。

### 6.6 更新后的结论

```text
R1–R8                      = 已落实；R5 已由作者裁决（主要本意 = C）
作者裁决的落地方式         = 合格（原话保存、范围限定、不重开残余）
伪新残余                   = 已清除，作者裁决后仍是如此
作者来源标注               = 还差 P1
作者选定读法 C 的邻居减法  = 尚未完成（A1、A2）
建议                       = 修正 P1、A1、A2 后，内容层面可以合并；A3、N1、N2 可在同一次推送中顺带处理
```
