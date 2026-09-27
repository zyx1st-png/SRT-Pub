---
id: SRT-PR1076-FACING-V0-3-HUMAN-IN-LOOP-INDEPENDENT-CONTENT-REVIEW-20260927
type: audit
status: active
date: 2026-09-27
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FACING_HUMAN_IN_LOOP_GENERATIVE_CONFRONTATION_2026-09-27.md
  - Operations/Proposals/SRT_FACING_HUMAN_IN_LOOP_GENERATIVE_CONFRONTATION_METHOD_V0_3_2026-09-27.md
  - Operations/Audits/SRT_FACING_COMPLETION_SCOPE_AUDIT_2026-09-27.md
tags: [IndependentReview, PR1076, Facing, HumanInLoop, GenerativeConfrontation, MethodReview]
---

# PR #1076 独立内容评审 — Facing v0.3：跨域重构前的作者生成性对质

> **角色**：对**已合并**的 PR #1076 做合并后独立内容评审。只读：不修改 #1076 的任何文件、STATUS、路由面或 canonical owner。
>
> **评审者独立性与利益披露**：独立 session，没有参与 #1076 的写作。但有两点需要说明：
> - 本 session 评审过此前的全部 Facing PR（#1068、#1071、#1074）；
> - 本 session 曾在对话中向作者指出，AI 起草的表达会把内容拉向已有文献的平均值。#1076 回应的正是这一类风险。
>
> 因此评审者对 #1076 的方向可能有认同偏向。
>
> **评审范围**：三份文件全部通读；STATUS、路由面与认知程序 owner 做了关键词核对。

## 0. 评审对象

```text
PR:    #1076 (MERGED 2026-09-27 02:06Z) “Facing v0.3: require author generative confrontation before cross-domain reconstruction”
head:  e0a57ce0   base: 3cb6857f (= #1074 merge)   merge: cea5359e
time:  commits 10:04:50 → 10:04:54 (+0800); PR opened 02:05:33Z, merged 02:06:26Z (≈1 min)
AJ = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FACING_HUMAN_IN_LOOP_GENERATIVE_CONFRONTATION_2026-09-27.md (182)
MT = Operations/Proposals/SRT_FACING_HUMAN_IN_LOOP_GENERATIVE_CONFRONTATION_METHOD_V0_3_2026-09-27.md (367)
SC = Operations/Audits/SRT_FACING_COMPLETION_SCOPE_AUDIT_2026-09-27.md (86)
```

## 1. Verdict

```text
CANONICAL IMPACT                                   = NONE
PROBLEM DIAGNOSIS (machine-only Facing converges to
  inherited domain cuts)                           = CORRECT
SCOPE CORRECTION (8/8, 7/7 ≠ full reconstruction)  = CORRECT; consistent with #1072 F1
DIVISION OF LABOR (A machine / B author / C machine) = SOUND
STAGE C TESTS (C1–C8) + negative results valid     = STRONG
SUCCESS OPTION D (“traditional cut was adequate”)  = EXCELLENT anti-bias clause
MODE S / MODE R distinction                        = CLEAR

guards are one-sided (machine failure modes only)  = F1
Stage C independence                               = F2
confrontation card anchors the author              = F3
#1074 reverse-neighbor work not typed under S / R  = F4
wiring: v0.3 / SC unreachable from STATUS, routers,
  v0.2 method, cognition owner; STATUS has two
  different CURRENT NEXT values (pre-existing)     = F5 (mechanical, high practical impact)
label collisions                                   = F6

REVERT NEEDED = NO     BLOCKER = NO
RECOMMENDATION = add author-side guards + Stage C independence + anti-anchoring card;
                 wire v0.3 / SC into routing; fix the stale STATUS CURRENT NEXT line
```

## 2. 优点

- **诊断正确。** MT §1–2 指出了真实的失败模式：机器先接受成熟领域的对象清单，再把它们分进各个 facing，推出残差，最后宣布“领域已重构”。这只是给传统研究加了一层分类，没有追问切分本身是怎样生成的。核心问题因此从“X 属于哪一层”，改成了“X 要成为一个看似现成的解释对象，此前必须生成、稳定、保留、隐藏些什么”。这一改写抓住了要害。
- **范围更正是诚实的。** SC 明确写出：#1071 的 8/8 与 7/7 只在其声明的范围内完成；早期 / 历史 SRT 概念的整体重构、作者主导的跨域重构，都是 NOT COMPLETE。这与 #1072 F1（“09-25 之前的概念退役数 = 0”）一致，也直接回答了作者的问题：「我之前定的对于前期SRT理论概念的三层facing分析是否完成」。
- **分工合理。**
  - 机器负责源生文献、基线与反例；
  - 作者负责挑战既有对象化，并提出重切；
  - 机器再回到文献做对抗检验。

  作者的贡献被正确界定为“生成性重切”，而不是检索领域事实。
- **Stage C 很强。**
  - C1–C8 覆盖先例、吸收、矛盾、重参数化、依赖次序、对象化改变与收益；
  - C8 明确允许 SOURCE_ABSORBED / NO_GAIN / REORGANIZATION_ONLY；
  - §11 的成功选项 D：“传统对象化已经足够，不需要 SRT 重切”，是很少见、也很可贵的反自我偏向条款。
- **反收敛护栏里有关键的一条**（MT §9）：“replace author confrontation with a machine-generated simulated author answer”。它禁止机器替作者回答。
- **边界清楚**（AJ §8、MT §10）：
  - 中立实验、复现与判别测试可以照常进行，不受作者对质关口的限制；
  - 只有“这个结果证明了新的领域对象化或 SRT 重切”这类主张，才必须经过 B + C 两个阶段。

## 3. 发现

### F1（中高）护栏只防机器的失败，不防作者的失败

MT §9 的反收敛护栏全部针对机器：把领域词汇当自然本体、把源对象换成 SRT 同义词、用文献数量压倒作者尚未解决的重切，等等。**没有一条针对作者一侧可能的失败**，而 Stage B 恰恰给了作者重切一个受保护的位置：

- MT §3 Stage B：“Do not penalize the author response for lacking source terminology”——合理；
- MT §9：“use literature quantity as a reason to override an unresolved author recut”被列为禁止项——合理，但它没有对称的一面；
- **Stage B 第 7 问**：“What would count as the domain having followed the wrong explanatory direction **even if its local models predict well**?”——这等于邀请提出一种“预测良好但方向错误”的主张。如果不配套可检验的后果，这类主张原则上无法证伪。

需要补上的作者侧失败模式：

```text
- 重切的动机来自 SRT 先验，而不是领域材料；
- 重切没有指明任何能表明它错了的观察；
- “方向错误”的主张没有任何判别性后果；
- 重切因为出自作者而被保留为 OPEN，从而永远不被否定。
```

**建议：** 在 MT §9 加一组“作者侧护栏”，并对 Stage B 第 7 问加一条硬性配套：凡是主张“预测良好但方向错误”，必须在 Stage C 的 C7 中给出至少一个判别性后果；给不出，就只能记为“解释性重述”。

### F2（中）Stage C 的独立性

Stage A 和 Stage C 由同一个“机器”执行。在实际操作中，通常还是准备 Stage B 对质卡的同一个会话。按仓库自己的 edit protocol，canonical 语义编辑要求独立复审者，而且“复审者不能与同一 semantic edit pass 混为一体”。

Mode R 的产物会直接导向实验设计和 SRT / GRG 的领域重构主张，分量不低于一次语义编辑。

**建议：** 至少对这两类 Mode R 结论——导向实验的，或导向 canonical 后果的——要求 Stage C 由一个独立的会话或上下文执行，并能重新读取来源，而不是复述 Stage A 的结论。

### F3（中）对质卡会锚定作者

MT §8 的对质卡包含 “POSSIBLE OBJECT-TOO-EARLY POINT: <one or two candidates, explicitly machine-proposed>”。作者要防的正是机器收敛；而在作者给出直觉之前就先摆出机器的候选，会把作者的回答锚定在机器的切法上。这是一种常见的启动（priming）效应。

**建议：** 对质卡分两步：

1. 先只给出 DOMAIN、SOURCE-NATIVE CUT 与四个问题，由作者作答并存档；
2. 再展示机器的候选，请作者比较。

这也就是 #1074 评审 F6 提出的“盲步”在作者一侧的对应做法。

### F4（中低）#1074 的反向邻居工作没有按 Mode S / Mode R 归类

MT §5 把 #1071 Pass B 追溯归类为 Mode S（源生减法 / 校准）。但此后 #1074 的 R0 反向邻居推导与“原初三角测量”做的已经不止减法：它们尝试把邻居重建为特例。#1074 最终以作者接受的 **anti-tautology STOP** 收尾（STATUS l.186：“scientific distinctiveness … NOT ESTABLISHED”）。

按 v0.3 的逻辑，如果机器独自分析会收敛到传统切分，那么 #1074 的否定结论有一部分可能正是 Mode S 的产物。这不等于它错了，但它的地位应当写清楚。

**建议：** 在 SC 中补一行，说明：

- #1074 R0 与三角测量属于 Mode S；
- anti-tautology STOP 是否以“未来的 Mode R 对质”作为其重开条件之一。STATUS l.223 现有的重开条件（新的原初区分、非循环的下游推导等）可以把 Mode R 的产出列为合格输入。

### F5（机械，实际影响高）v0.3 与范围审计没有接入路由；STATUS 有两个不同的 CURRENT NEXT

**接入缺失。** 在 STATUS、`_SRT_CONTEXT_ROUTER.md`、`_SRT_AGENT_RETRIEVAL_PROFILE.md`、`Glossary/SRT_Live_Term_Router.md`、AGENTS.md 中，都检索不到 v0.3 或 SC。另外：

- router l.95 的 Facing 行仍指向 “Facing method v0.2”；
- v0.2 方法文件本身没有加“后续跨域工作以 v0.3 为准”的指引；
- 当前 CURRENT NEXT 的 owner（认知程序 `SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md`）中也检索不到 Stage B 关口。

SC 的全部目的，是防止后来的代理误读“8/8 COMPLETE”。但代理按路由面读文件，实际上到达不了 SC。v0.3 最重要的一条硬边界——中立结果转为 SRT 重切主张之前，必须经过 B + C——也没有写进正在执行的认知程序 owner。

**STATUS 中两个不同的 CURRENT NEXT（这是 #1074 遗留的问题，不是 #1076 引入的）：**

- l.186 与 l.228：CURRENT NEXT = pre-object generative orientation of cognition（中立认知程序）；
- l.1019–1021（“Immediate routing”）：CURRENT NEXT = primitive Selection anti-tautology，owner 仍是 anti-tautology 问题文件。

#1076 写的是 “No change to the single repository CURRENT NEXT”，这以 STATUS 内部一致为前提，而现在它并不一致。

**建议：** 一次纯路由的后续修补：

1. STATUS l.1019–1021 改为认知程序；
2. STATUS 加一行 #1076 ledger，并指向 v0.3 与 SC；
3. router l.95 与 retrieval profile 指向 v0.3；
4. v0.2 方法文件加一句前向指引；
5. 认知程序 owner 加一行 “SRT recut claims require Facing v0.3 Stage B + C”。

### F6（低）标签

- **Stage A / B / C** 与 #1074 的 “A”（Selection-totality 选项）、“Axis A”、G-A0…A3 重叠。
- **A1–A8、C1–C8** 中，C1 与 Expectation 类型化中的 C1（model-mediated anticipation）同名。
- **Mode S / Mode R** 与仓库既有的 research_mode U / N 是两对不同的“mode”，而且 MT 没有说明两者的关系。建议补一句：Mode R 一旦含有比较性主张，就同时触发 N-mode。

按作者已接受的命名空间原则，建议加前缀，例如 FA1–FA8、FC1–FC8。

## 4. 对作者的建议

```text
1. 方法方向可以直接保留；它回应的是真实风险，而且 Stage C 与成功选项 D 保证了它不会变成“作者直觉通行证”。
2. 优先做 F5（纯路由修补）：不接入路由，v0.3 与范围审计对后续代理不起作用。
3. 下一次真正使用 Mode R 之前，补上：
   - 作者侧护栏，以及 Stage B 第 7 问必须配套判别性后果（F1）；
   - 对质卡两步制（F3）；
   - 导向实验或 canonical 的 Mode R 结论由独立会话做 Stage C（F2）。
4. 在 SC 中给 #1074 的工作归类，并说明 anti-tautology STOP 与未来 Mode R 的关系（F4）。
```

以上均为作者可选的修正；本评审不代为执行。
