---
id: SRT-PR1079-FACING-CHOICEMAP-FACE-REC-INDEPENDENT-CONTENT-REVIEW-20260927
type: audit
status: active
date: 2026-09-27
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - Operations/Handoffs/SRT_PR1079_INDEPENDENT_REVIEW_HANDOFF_2026-09-27.md
  - 01_Source_Intuition/SRT_AUTHOR_FACING_CHOICEMAP_REVERSE_INFERENCE_2026-09-27.md
  - Operations/Audits/SRT_FACING_CHOICEMAP_FR_ADV_REVERSE_METAETHICS_2026-09-27.md
tags: [IndependentReview, PR1079, Facing, ChoiceMap, ReverseMetaethics, Provenance, NeighborAbsorption]
---

# PR #1079 独立内容评审 — pre-09-25 普查 + ChoiceMap FACE-REC / FR-ADV

> **角色**：按 PR 内的 handoff（`Operations/Handoffs/SRT_PR1079_INDEPENDENT_REVIEW_HANDOFF_2026-09-27.md`）执行的合并前独立评审。只读：不修改 #1079 的任何文件、STATUS、HP-B owner 或 canonical owner，也不合并。
>
> **评审者独立性与利益披露**：独立 session，没有参与 #1079 的写作。但本 session 评审过 #1068–#1076，#1079 的普查 §6 采用的“盲步”，正是本 session 在 #1074 评审 F6、#1076 评审 F3 中提出的建议。因此本评审一部分是在检查自己建议的落实情况。
>
> **评审范围**：8 个文件全部通读。R1 用 git 提交次序核对；R4 中新增的三篇外部文献已联网核实。

## 0. 评审对象

```text
PR:    #1079 (OPEN, draft) “Facing: pre-09-25 census + ChoiceMap FACE-REC / FR-ADV”
head:  4aab01af   base: be392d34
time:  2026-09-27 10:48 → 13:30 (+0800), 24 commits, 8 files, +3243
CEN = …/SRT_PRE0925_FACING_COVERAGE_CENSUS_2026-09-27.md
AUT = 01_Source_Intuition/SRT_AUTHOR_FACING_CHOICEMAP_REVERSE_INFERENCE_2026-09-27.md
S2  = …/SRT_FACING_CHOICEMAP_FR_AUTH_STAGE2_2026-09-27.md
S3  = …/SRT_FACING_CHOICEMAP_REVERSE_METAETHICS_STAGE3_2026-09-27.md
HPX = …/SRT_FACING_DIRECTIONAL_GENERATION_HPB_UPSTREAM_CROSSWALK_2026-09-27.md
POL = …/SRT_FACING_CHOICEMAP_FRADV_DIRECTIONAL_POLARITY_2026-09-27.md
ADV = …/SRT_FACING_CHOICEMAP_FR_ADV_REVERSE_METAETHICS_2026-09-27.md
HND = Operations/Handoffs/SRT_PR1079_INDEPENDENT_REVIEW_HANDOFF_2026-09-27.md
```

为避免与来源类别 “A1”（被作者接受的机器整合）混淆，本评审把 handoff §2 的作者决定编号 A1–A10 改写为 **HD1–HD10**。

## VERDICT

```text
PASS-WITH-CORRECTIONS
```

没有 blocker。有三项 major，全部是措辞或来源类型的修正，不需要扩展本体。修正后可以作为非 canonical 包合并。

## BLOCKERS

无。逐项核对：

- **R1**：所有直接引文都能在逐字粗体块中找到；盲答提交（6816bfc0，10:58）早于机器候选提交（46f3b242，11:11）；没有机器综合冒充作者原话。
- **R2**：没有恢复原初道德内容。
- **R3**：没有改写 HP-B。
- **R7**：没有任何措辞暗示 ChoiceMap 已经在经验上识别出原初 Selection。

## MAJORS

### MJ-1（R1 来源类型）第一次盲答之后，Stage B 退回了“机器给菜单、作者选项”；HD7–HD10 的内容来自机器，经作者接受

逐项追溯 HD1–HD10 的来源：

| 决定 | 作者输入 | 内容来源 | 应有类型 |
| --- | --- | --- | --- |
| HD1 / HD2 | 盲答与澄清，作者原话（AUT §1、§4） | 作者 | A0-Q ✓ |
| HD3 | 「认同分析，关键问题认同后者」 | 机器提供的 A/B 分叉 | 作者选择机器选项（A1） |
| HD4 | 「我偏向于1，一种变好或变坏的感觉」 | 机器族 1（“a stable direction”，S2 l.301）；**“变好或变坏”是作者自己的注解** | 选择 + 作者措辞（注解部分为 A0-Q ✓） |
| HD5 | 「B」 | 机器 M8-A/B 分叉 | A1 |
| HD6 | 「十多年前的感觉里……反向推元道德也是srt想要去追寻的东西」 | 作者 | A0-Q ✓（本包最强的作者原生输入） |
| HD7 | 「认同你的分析，先选c」 | 机器选项 C（“耦合”）。机器早在 S2 l.423 就以 “A third allowed answer … one coupled process” 预先提出过 | A1 |
| HD8 | 「c」 | 机器选项 P-C（“分层”，S3 l.428） | A1 |
| HD9 | 「认同」 | 机器解释 | A1 |
| HD10 | 「认同，继续」 | 机器的尺度分离综合 | A1 |

每处引文都是准确的，没有冒充。但有三个实质问题：

1. **PR 正文把 HD7、HD8、HD10 的内容列为 “Current author-preformal convergence”。**按仓库的来源分类，这些是作者接受的机器整合（A1），不是作者原生的前形式内容。AUT 各节也用 “AUTHOR RECUT CANDIDATE” 标记它们，会被读成作者提出的重切。
2. **按本包自己的证据阶梯自我检验。**S2 M3 规定：“ordinary choice inside offered grammar = weak-to-moderate inverse evidence; author-generated recut / breakout = high-information”。按这条标准：
   - HD1、HD2、HD6 以及 HD4 的注解是高信息证据；
   - HD3、HD5、HD7–HD10 是在机器给定的语法里做选择，按本包自己的尺度属于弱到中等证据；而且没有一次拒绝、合并、拆分或跳出（breakout）。
3. **HD7 与 HD8 都是 A / B / C 三选一中的 C，也就是“两者兼有”的折中项。**这是一个已知的选择框架效应（折中效应），恰恰是 ChoiceMap 新数据单元要揭示的那种“提供的语法塑造了选择”。

v0.3 设立 Stage B，本意是在机器收敛之前捕获作者的生成性重切。本包只在第一问做了盲步，此后回到了菜单式裁决。

**修正（仅措辞与类型）：**

- PR 正文与 AUT 中，把 HD3、HD5、HD7–HD10 标为 “machine-proposed, author-selected within offered grammar (A1)”；
- “author-preformal convergence” 改为 “author-originated core (HD1, HD2, HD4 gloss, HD6) + author-accepted machine synthesis (HD3, HD5, HD7–HD10)”；
- 未来的 FR-AUTH 每个分叉先要求作者开放作答，再展示选项；并按 ChoiceMap 自己的新数据单元，记录作者是接受、拒绝、合并、拆分还是跳出。

### MJ-2（R4 邻居吸收）方向性“变好 / 变坏”与“耦合两个 facing”都有更精确的吸收者，ADV 没有列出

ADV §2 覆盖了 handoff 要求的五个家族，结论“phenomenon-level novelty NOT ESTABLISHED”是诚实的。但 HD4 的定义性特征，不是价值水平，而是**变化方向**：“一种变好或变坏的感觉”。这一点有比 Damasio、Solms 更精确的成熟理论，已联网核实：

- **Carver & Scheier (1990)**, “Origins and functions of positive and negative affect: A control-process view”, *Psychological Review* 97(1): 19–35。情感来自第二层反馈环路，它感知的是行动系统向目标推进的**速率**，而不是离目标的距离。
- **Joffily & Coricelli (2013)**, “Emotional valence and the free-energy principle”, *PLoS Computational Biology* 9(6): e1003094。效价被形式化定义为**自由能（在简化条件下即预测误差）随时间变化率的负值**。
- **Kiverstein, Miller & Rietveld (2019)**, “The feeling of grip: novelty, error dynamics, and the predictive brain”, *Synthese* 196(7): 2847–2869。“抓握感”来自误差动力学；同一误差动力学既被感受到，又驱动技能与模型的调整。这篇把 Skilled Intentionality 与预测加工结合在一起。

后果：

- **HD4（方向性的变好 / 变坏，先于对象）**在现象层被误差动力学 / 进展速率理论强吸收。
- **HD7（“感受到的方向”与“生成下一个切分”是同一事件的两个 facing）**有直接对应：在 Kiverstein 等人的框架中，同一误差动力学既构成感受（grip），又驱动表征或模型的修订。HD7 应记为 SOURCE_ABSORBED 候选，而不仅是 “NOT ESTABLISHED”。

**修正：** 在 ADV §2 增加 “2.6 error-dynamics / rate-of-progress valence”，并把这一家族加入 G3 的对手清单。

### MJ-3（R2 需要收窄）“变好 / 变坏”的**符号**来自哪里，必须写明

ADV §3 与 S3 §1 的调和（“L0 是来源线 ≠ L0 含有预先编码的道德内容”）成立，**没有 blocker**。但它之所以成立，是因为 L0 的贡献被削薄为非平坦（non-flatness），而这一点 09-14 已经写过。问题在于：

```text
非平坦 / 不对称
!=
带符号的极性（更好 vs 更坏）
```

从“不对称”走到“对谁、朝哪边算更好”，需要一个参照：已形成位置的维持、可行性或组织。所以：

- 符号只能在**已形成层**确定。否则就等于 L0 含有原效价（proto-valence），违反 09-14。
- 这座“缺失的中间桥”（S3 §2），恰好落在生成主义的适应性 / 意义建构理论（Di Paolo 2005；Weber & Varela 2002 **[本评审未联网核实]**），以及 MJ-2 的误差动力学理论的领地。

S3 §7 的 “the non-flatness can be internally enacted / registered as a pre-object directional polarity” 没有说明符号的参照。

**修正：** 在 S3 §7 与 ADV §3 写明：

> polarity sign = formed-position-relative（相对于已形成组织的维持 / 可行性 / 重构）；L0 只提供非平坦，不提供符号。

同时把 AUT §7 的 “L1 好坏的感觉来自 L0” 标注为“来源线 = 非平坦，不含符号”。

## MINORS

- **MN-1（R1）盲卡没有保存。** CEN §7 第 3–4 步写了“构建 FR-SRC 卡，只展示盲问 1–4”，但仓库里没有卡片原文。提交次序证明盲答在机器候选之前，却无法证明卡片本身没有暗示。另外，盲答使用了 L2 / L1 / L0-facing 词汇，说明卡片是用 Facing 框架提问的；这与 v0.3 §4 “Facing 矩阵最后出现”有张力。建议补存卡片原文。
- **MN-2（R3）HPX 的措辞超出冻结许可。** HPX §9 写 “UPSTREAM COMPLEMENT / POSSIBLE SOURCE-LINE CORRECTION”，§7 给出 “possible upstream-expanded reading of valence”。HP-B 冻结期间不允许新增钩子或核心条件。HPX 没有修改 owner，也保住了 “direction-source ≠ phenomenal-admission”，**因此不是 blocker**。但应改为 “upstream question held for a future HP-B reopen; not applied while frozen; adoption requires an author-named reopen trigger”。
- **MN-3（R6 先例）** “数据单元从选择改为切分变换”有方法学先例，应列为先例与基线：
  - 偏好建构（Lichtenstein & Slovic 2006）；
  - 顿悟研究中的表征改变（Ohlsson 1992；Knoblich et al. 1999）；
  - 选项生成（option generation）研究。

  G1（预测接受 / 拒绝 / 换层 / 合并拆分 / 回根）与表征改变理论直接对位，这类模型应当加入 G3 的对手清单。**以上文献本评审未联网核实。**
- **MN-4 标签冲突。**
  - handoff 的 A1–A10 与来源类别 A1 同名（本评审已改用 HD1–HD10）；
  - G1–G5（收益判据）与 G-A0…A3、GRG G-系列冲突；
  - M1–M8、D-facing / G-facing、D1–D3 也有重叠；
  - 建议加前缀。
- **MN-5 速度。** 24 次提交、约 2 小时 40 分钟，其间有 9 次作者回合。作者参与充分，这是 v0.3 的正面落实。只是每个分叉的回复都很短（「c」「认同」），这是 MJ-1 的成因之一。

## CLAIMS THAT SURVIVE

- **方法层的数据单元改变：** “提供的语法 / 切分 → 接受 / 拒绝 / 合并 / 拆分 / 回根 / 跳出 → 生成的替代切分”。这是真实而有意义的方法改变（R6 PASS），即使不具科学独特性。
- **ChoiceMap 作为逆向识别 / 层析方案：** 系统扰动 L2 语法、拟合彼此竞争的潜在生成模型、再次扰动以作区分（ADV §7 强版本）。
- **HD1 / HD2 / HD6**（作者原生）：L2 证据 → 潜在 L1 → 约束 L0 的研究方向，以及“反向推元道德”的长程目标。前者只作为方法方向，后者只作为研究纲领。
- **尺度分离的方向性（HD10）：** 先于当前对象，但不先于全部历史。这可以阻止“固定价值向量”与“每次从零生成”两个极端，作为 A1 保留。
- **CEN 普查：** 覆盖分类清楚，ChoiceMap 作为首个试点的程序性理由成立；“不重开 #1074 / HP-B”的边界清楚。
- **ADV 的总体否定性结论：**
  - REPARAMETERIZATION = NOT ESTABLISHED；
  - SCIENTIFIC DISTINCTIVENESS = NOT ESTABLISHED；
  - #1074 REOPEN = NO（R5、R7 PASS）。

## CLAIMS THAT MUST BE NARROWED

1. “Current author-preformal convergence”（PR 正文）→ 按 MJ-1 分成作者原生部分与作者接受的机器综合部分。
2. HD4 与 HD7 的现象层地位：NOT ESTABLISHED → SOURCE_ABSORBED 候选（误差动力学 / 进展速率，MJ-2）。
3. “L1 好坏来自 L0”→ 来源线仅为非平坦；符号相对于已形成位置（MJ-3）。
4. HPX “POSSIBLE SOURCE-LINE CORRECTION” → 冻结期间仅作为待问问题（MN-2）。
5. R5 更严一层：ADV §4 提出的判别器——在显式重切出现之前，预测必须修订的表征层级——必须专门对抗分层预测加工对手，因为后者同样可以由预测误差持续存在的层级，预测修订发生在哪一层。

## PROVENANCE FINDINGS

- 引文逐字、完整；盲答的提交次序已核实（6816bfc0 早于 46f3b242）；没有机器综合冒充作者原话。
- 类型问题：HD3、HD5、HD7–HD10 是“作者选择机器选项”（A1），不应以作者前形式收敛的名义出现（MJ-1）。
- HD6（十年前的直觉）是本包最有价值的作者原生输入，已正确保存为 A0-Q。
- 盲卡原文缺失（MN-1）。

## NEIGHBOR-ABSORPTION FINDINGS

- ADV 已列的五个家族：吸收判定公正。
- **新增**误差动力学 / 进展速率效价（Carver & Scheier 1990；Joffily & Coricelli 2013；Kiverstein, Miller & Rietveld 2019）：精确吸收 HD4 的“方向性”与 HD7 的“耦合”（MJ-2）。
- **新增**生成主义适应性：吸收“符号从何而来”的缺失中间桥（MJ-3）。
- **新增**偏好建构、表征改变与选项生成：作为 R6 方法改变的先例，以及 G1 / G3 的对手（MN-3）。
- 综合判断：现象层几乎全部被吸收；存活的是**方法层**（数据单元改变 + 逆向识别设计）与**长程研究纲领**（反向元伦理）。这与 ADV 的总体判定一致，而且更严格。

## MERGE RECOMMENDATION FOR THIS NONCANONICAL PACKAGE

```text
完成 MJ-1、MJ-2、MJ-3（均为措辞或类型修正）与 MN-2 之后：
  merge #1079 as noncanonical FACE-REC provenance + method package；
  不改 CURRENT NEXT；不重开 #1074；不改 HP-B owner；不做 canonical 推广。

后续（可选）：
  起草中立的 ChoiceMap 逆向识别方案时，把 G3 对手扩展为：
    误差动力学效价、分层预测加工、表征改变 / 顿悟模型、偏好建构；
  每个 FR-AUTH 分叉先开放作答、后展示选项。
```

本评审不建议任何 canonical 推广。
