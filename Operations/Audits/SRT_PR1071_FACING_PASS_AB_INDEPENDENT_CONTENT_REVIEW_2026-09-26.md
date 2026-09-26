---
id: SRT-PR1071-FACING-PASS-AB-INDEPENDENT-CONTENT-REVIEW-20260926
type: audit
status: active
date: 2026-09-26
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - Operations/Proposals/SRT_FACING_RECONSTRUCTION_SIMPLIFICATION_METHOD_V0_1_2026-09-26.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PR1069_FACING_METHOD_CORRECTIVE_2026-09-26.md
  - Operations/Audits/SRT_PR1068_FACING_RECONSTRUCTION_METHOD_INDEPENDENT_CONTENT_REVIEW_2026-09-26.md
tags: [IndependentReview, PR1071, Facing, PassA, PassB, OUTD, Simplification, AuthorDecisionPacket]
---

# PR #1071 独立内容评审 — Facing 重构 Pass A / B 与作者决策包

> **角色**：对**未合并**的 draft PR #1071 做合并前独立内容评审。PR 自身写明“作者 D1–D6 裁决前不合并”，因此本评审的主要作用是在作者裁决**之前**校正决策包的表述。只读：不修改 #1071 的任何文件、STATUS、路由面或 canonical owner。
>
> **评审者独立性与利益披露**：独立 session，没有参与 #1071 的写作。但 #1071 执行的方法 v0.2 基本就是本 session 在 #1069 提出的修正（经作者在 #1070 采纳并部分改写），所以本评审有一部分是在检查自己建议的落实情况，特此披露。
>
> **评审范围**：#1071 的 10 份审计**全部通读**，STATUS diff 全部核对，#1070 的作者裁决与方法 v0.2 的相关节核对。对 canonical 与既有 owner 的引用做了抽查（§2 列出）；Pass B 的 4 条外部文献中，有 2 条通过网络检索核实。

## 0. 评审对象

```text
PR:    #1071 (OPEN, draft) “Facing reconstruction Pass A/B — subtractive simplification and author decision packet”
head:  65ca951b   base: 208bdca8 (= #1070 merge = current main)
time:  commits 21:42:53 → 22:04:32 (+0800), 11 commits, 11 files, +3261 / −21
CI:    governance-preflight on 65ca951b = success

OUT = …PASS_AB_INTEGRATED_OUT_A_D (456)      FRH0 = …PASS_A_FRH0_L0_CONTINUITY_REDUCTION (212)
FRH1 = …PASS_A_FRH1_ONE_POSITION_ORIENTATION (239)
CONT = …PASS_A_CONTINUITY_STABLEISP_RESELECTABILITY (276)
EXP  = …PASS_A_EXPECTATION_ANTICIPATION (262)
GATE = …PASS_A_GATE_BRIDGE_PROPERTY_OBJECTIFICATION (343)
FLD  = …PASS_A_FIELD_ATTRACTOR_REACHABILITY (312)
REC  = …PASS_A_RECONSTRUCTIBILITY_GENERATIVE_DEBT (376)
NEG  = …PASS_A_PRIMITIVE_SELECTION_O0_NEGATIVE_CONTROL (297)
PB   = …PASS_B_BOUNDED_NEIGHBOR_COMPARISON (453)
ST   = STATUS.md (CURRENT NEXT → author adjudication D1–D6)
```

控制 owner / source：

- 方法 v0.2：§7 前向检验、§10–11 上限、§13 FRH-0…7、§18 停止规则与 HP-B 护栏、§19 成功判据；
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PR1069_FACING_METHOD_CORRECTIVE_2026-09-26.md`（下称 C70），D-1…D-4 与 §5–§8；
- `Glossary/SRT_Live_Term_Router.md`：l.95–97（Facing 别名、Position-relative L0-facing、L0-facing continuity）、l.113、l.125–127；
- Spine：§2（O0 / S0）、§6.2、§6.3、§7；
- `Core_Law/SRT_One_Formation.md` l.172；
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_O0_PRIMITIVE_GENERATIVITY_2026-09-14.md` l.63–69；
- `Operations/Audits/SRT_HPB_MINIMAL_PHENOMENAL_TOPOLOGY_CONVERGENCE_AUDIT_2026-09-26.md` l.103。

## 1. Verdict

```text
CANONICAL IMPACT (file edits)                         = NONE
HP-B READ-ONLY                                        = RESPECTED
METHOD v0.2 COMPLIANCE (FRH-0 first, caps 8/7,
  namespaced labels, structure-learning baseline)     = PASS
#1069 FINDINGS F1–F10                                 = ADDRESSED (by #1070 + this pass; see §2)
CITATION SPOT-CHECK                                   = ACCURATE (§2)
TYPING QUALITY (FRH1, EXP, GATE, FLD, REC)            = GOOD
PASS B (7 families)                                   = HONEST; no novelty overclaim

“SUBTRACTIVE SIMPLIFICATION” CLAIM                     = OVERSTATED (F1)
FRH-0 “FULLY ABSORBED”                                 = one residual unassigned (F2)
DECISION PACKET D3 / D4                                = hides a vocabulary shift / a scope condition (F3, F4)
DECISION PACKET completeness                           = missing cognition-programme / toy-sim decision (F5)
NEGATIVE CONTROL                                       = self-checklist, not a control; K/A mixing (F6)
LABELS / ROUTING                                       = minor collisions; STATUS guard block dropped (F7, F8)

BLOCKER                                               = NO
RECOMMENDATION = before author adjudication, amend OUT-D per F1–F5 (wording + two added questions);
                 after adjudication, merge; routing cleanup per F7–F8
```

## 2. 优点与核对结果

- **按 v0.2 执行，没有越界。**
  - FRH-0 先跑；Pass A 8/8、Pass B 7/7，没有超出上限。
  - Bearer / Ψ_f / 意识三项只读。REC §5 按 C70 §7 把失配读作 Ψ_f 的情境读数，而不是摩擦的定义。
  - 标签已加命名空间：FACE-L0/1/2、FRH-0…7、OUT-A…D。
  - 没有写 canonical，没有执行模拟，PR 以 draft 形式等待作者裁决。
- **#1069 的发现均已处理：**

  | #1069 发现 | 处理 |
  | --- | --- |
  | F1 | FRH-0 还原 |
  | F2 | 别名化；不再用 bare L0 |
  | F3 | v0.2 §7–8 |
  | F4 | OUT B4 消除循环 |
  | F5 | FRH1 §5–6 |
  | F6 | REC §5 |
  | F7 | PB |
  | F8 | C70 §8 |
  | F9 | 上限 8/7 |
  | F10 | router l.95–97、REC §4 |

  作者对 D-3 的改写（“具体内容预测只能经由声明的下游模型，并归属于该模型”）比 #1069 原来的“只允许二阶预测”更好，本评审采纳这一改写。
- **FRH1 对 B/C 的处理正确。** Position 上的前向不对称被归为 B（结构性生成期待）的一个实例，而不是 C（预期实现），同时遵守 Spine §6.3 “Selection affecting later selectability != formed-position anticipation automatically”。这正好修掉了 v0.1 把 Expectation 压进 Position 的问题。
- **FLD §10 是这次最有用的结果。** 它把作者的「整体吸引子场如何形成」拆成四个可回答的问题：原初（O0）、已形成系统的协调、局部切分的稳定、回写递归。一个过载的“场形成机制”因此不再需要。
- **REC §4 把 reconstructibility 分成三义**（生成性 / 方法论 / 仓库工程）。这与 router l.113 的限定一致。
- **PB 诚实。** 7 个家族逐一写明“SRT 不得声称为自己独有的内容”，§9 把 SRT 剩余的负担收窄为“类型化与依赖次序”，并声明 “not declared novel merely because they remain”。
- **B6 找对了真正的原初残差：** genuine Selection 与描述性状态转换之间的反同义反复判据。
- **引用抽查全部准确：**
  - FRH1 K3 = One Formation l.172；
  - FRH1 §7 的 HP-B 引文 = HP-B convergence audit l.103；
  - EXP 的 P_G / E_G = router l.125–127 与 GRG v0.3；
  - CONT 的 B13 / P1-T06 = Core_12b l.174 的交叉引用；
  - NEG §1 的 “primitive orientation = irreducible non-flat role-structure” = O0 裁决 l.69。
- **外部文献：**
  - 已联网核实：Geniusas, *EJP* 33 (2025) 1021–1037, doi 10.1111/ejop.12931；Blomberg, *Public Journal of Semiotics* 9(1) (2019) 78–94。
  - 未联网核实（Crossref 被网络策略阻断），但是本领域标准文献，书目信息与评审者所知一致：West, Fisher, Gardner & Kiers, *PNAS* 112 (2015)；Montévil & Mossio, *J Theor Biol* 372 (2015)；Mossio & Bich, *Synthese* 194 (2017)。

## 3. 发现

### F1（中）“减法式简化”的说法言过其实：退役的只有三天内的新名词

OUT-B B1 退役 / 降级了三项：

- `L0-facing continuity`（#1068，09-26）；
- `formed Orientation`（#1068，09-26）；
- `L0-facing / attractor field` 作为本体名词（#1058 / #1066，09-25 至 09-26）。

三项都是**本周**新造的。09-25 之前的概念**没有一个被退役**：OUT-B B2 保留了 18 项，其中多数是 09-25 之前已有的 owner 概念。与此同时，有几处 SPLIT 增加了类型区分：

- Gate 拆为 formation / standing / operation / property-object 四个角色；
- Expectation 拆为 B / C / P_G / E_G；
- reconstructibility 拆为三义。

本 pass 自己还新增了两个标签：

- `methodological reconstructibility`（REC §4）；
- `Gate standing`（GATE §4）。其中 “standing” 在 Spine §7 是 Stable ISP 的用词。

按术语计，净变化约为 −3 + 2。

所以准确的描述是：**这次 pass 成功遏制并撤回了本周的概念膨胀，并对旧概念做了类型整理；旧 owner 在减法检验下全部保留。** 后一点本身是有价值的稳健性结果：它说明 One、Selection-position、O0 等旧 owner 确实承重。但这不是“对以前的概念做了简化”。作者在 #1068 下达的指令（「对于之前的概念……进行一轮分析重构和简化」）目前只完成了“分析重构”这一半。

**建议：**

- OUT §0 与 “Final machine disposition” 的 “SUCCESSFUL AS SUBTRACTIVE METHOD” 改为“containment + typing pass; older owners survived subtraction”；
- 把 “older concepts retired = 0” 写进 OUT-D，由作者决定这是否足够。

### F2（中）FRH-0 的“全部吸收”漏掉了一个分级负担；`Position-relative L0-facing` 没有处置

FRH0 §5 把候选的每一行都标为 “FULLY ABSORBED”。对**二值**部分，这是对的：

- O0 支付“不被穷尽”；
- One / 重构支付连续；
- Selection-position 支付局部性。

但 #1068 的材料里还有一个**分级**负担，没有被分配到任何地方：

- TR §27：“A system may be highly stable in L1/L2 while **increasingly closed** in L0-facing terms”；
- O0 本身只说 “not **fully** preclosed”，允许部分预闭合。

“一个已形成过程的自身历史在多大程度上收窄了它下一次 Selection”，是一个程度量。O0 是二值的，不支付它。

这个负担有两个可能的去处：

1. **已形成层**：低 generative reselectability，加上低 latent reconstructive reach（CONT §6、REC §2）。这样的话，“closed in L0-facing terms” 本身就是一个 facing 错误，应改写为 L2 刚性。
2. **B6 原初残差**：如果收窄到极限，下一次转换就是“执行”而不是 genuine Selection，这正是 B6 的反同义反复问题。

两者都合理，但 FRH0 应该**写出来**。C70 D-1 的原话是 “If not fully absorbed: state the residual explicitly”。

同时，router l.96 把 `Position-relative L0-facing` 登记为 “WORKING_LABEL_ONLY / do not harden without residual”。本 pass 在 CONT §6、GATE §8、REC §5 中继续使用它，但 OUT-B 没有给它任何处置。它承载的正是上述分级负担。

**建议：** OUT-B 给它一个处置：要么随 FRH-0 一起退役，由 reselectability / latent reach 接管；要么写明它就是 F2 残差的载体。

### F3（中）D3 隐含了一个词汇迁移，应当向作者明示

作者的 A0-Q 是「是原初选择让 **position 持续地**维持某种状态的转化」。但在 canonical 中，Selection-position_t 是 **time-local** 的（Spine §6.2、router l.90）。持续的、跨时间的，是 **One**。

OUT D3 的重构（“same-process continuation = … recurrent reconstitution”）已经把连续性放在了 One 一侧，但没有告诉作者：

> 接受 D3，就意味着作者句子中“Position 持续地维持转化”里的 “Position” 在 canonical 词汇中应读作 **One**。Position 在每个 t 被重新形成，而不是持续存在。

这正是作者在 D3 中要判断的问题（“does Position itself still carry an additional burden”），所以应当明说。**建议**在 D3 中加一句：若作者坚持 “Position 本身持续”，那就是在主张 Selection-position 有跨时间身份，与 Spine §6.2 冲突，需要走 canonical 流程。

### F4（中）D4 的“为了”超出了组织功能论的适用条件

PB §5 正确地用组织功能论（Montévil & Mossio 2015；Mossio & Bich 2017）为非外在目的论的“为了”提供了成熟依据，同时写明 “closure of constraints != One automatically”。

但 D4 的建议是把“为了”用于 **Position formation 一般**：“Position formation may be described as functioning to keep transformation non-arbitrary if …”。在 Mossio 一派的理论里，“功能”以**约束闭合**（约束之间相互依赖、共同维持）为条件，而不是只要有递归重构就成立。不满足闭合的 One（例如只有路径依赖加重构、没有约束间互相维持的过程）没有这种意义上的功能。

**建议：** D4 改为 “formed-level ‘为了’ is licensed **where closure-like mutual dependence of constraints is paid**；for Ones without it, ‘为了’ is explanatory metaphor only”。作者的「一个Position的形成，就是为了……」因此只在满足闭合的情形下是字面的。

### F5（中）决策包缺一问：认知程序与玩具模拟在 SRT 中还剩什么目标

本 pass 的两个结果合在一起，对 #1066 包有直接后果：

- FLD §6、§10：“pre-object generative orientation” 只是研究伞；它的已形成系统问题交给认知科学与系统科学；SRT 特有的部分只剩 O0 与类型化。
- GATE §11：玩具模拟的任何正结果“would support only that bounded formed architecture. It would not validate primitive Selection, O0 or L0 ontology”。

也就是说，按本 pass 的结论，**玩具模拟无论结果如何，都不能对 SRT 特有的负担提供证据**。OUT D9 只写“保持 downstream”，没有问它在 SRT 队列中还有什么目的。

**建议**加 D11：

- (a) 认知程序改为中立认知科学程序，SRT 解释可选（这正是该程序开头自己写的边界），玩具模拟移出 SRT 队列 [推荐]；
- (b) 保留在 SRT 队列中，但须写明它检验的是哪一个 SRT 特有负担。

### F6（低中）“negative control” 其实是同一产出者的自查清单，并且混合了 K 与 A

NEG 由执行 Pass A 的同一产出者在同一轮中写成，内容是逐项确认“没有回灌到原初层”。这是有用的**回灌检查清单**，但不是实验意义上的对照：没有一个预期会失败的对照项。

NEG §0–1 在 “Keep exactly” 下把 O0（K，Spine §2）与 “primitive orientation = irreducible non-flat role-structure” 并列。后者出自 09-14 作者裁决 l.69，是 A 级来源，不是 K。方法 v0.2 §5 要求每条陈述标注来源。

**建议：** 改名为 “back-import checklist”，并为 §1 的两行分别标 K / A。

### F7（低）标签

- **OUT-D 的 D1–D10 与 C70 的 D-1…D-4 含义不同**，例如 C70 D-3 = 前向检验，OUT D3 = 动态 Position。STATUS 引用的是 “D1-D6”。按作者在 C70 §8 接受的原则，应加命名空间，例如 FD1…FD10。
- **`Gate standing` 与 Stable ISP 的 “standing” 冲突**（Spine §7）。建议改为 “formed Gate (retained)” 或 “Gate availability”。
- **`methodological reconstructibility`** 是新标签。router l.113 只登记了 generative reconstructibility，l.156 把仓库恢复义排除在外。如果保留，需要登记一行。

### F8（低，机械）STATUS 删去了研究框架护栏

#1071 的 STATUS diff 把 Immediate routing 下的 “Research framing” 块整块替换成了 “Post-pass guard”。被删掉的内容包括：

- “forward test = structural constraints first; concrete content only through declared downstream models”；
- “structure-learning / expandable-hypothesis-space models are required baselines”；
- “Facing = method alias”。

这些护栏仍保留在方法 v0.2 和 C70 中。但 OUT D10 的两个后续方向（反同义反复、分支同一性）都可能导向检验，所以 STATUS 应保留这三行。

### F9（信息）速度

10 份审计、约 3000 行，在 #1070 合并后 22 分钟内生成（21:42–22:04），平均每个目标约 2 分钟，内部没有独立复审。

抽查结果显示引用准确、类型化质量好（§2），所以不构成问题。只记录两点：

- PR 保持 draft、等待作者裁决的做法是正确的；
- 作者裁决时，D1、D3、D4、D11 这四项值得逐项确认，不宜一次性以「认同，继续」覆盖（参见 CONTINUE_DIRECTIONAL_ACCEPTANCE §3 例外 2、4：OUT-D 各项已处在显式的 ACCEPT / MODIFY / REJECT 待确认关口）。

## 4. 对作者裁决的建议顺序

```text
1. 先读 F1：决定 “older concepts retired = 0” 是否可以接受为本轮结论。
2. D1（退役三个本周名词）：可直接接受；同时处置 Position-relative L0-facing（F2）。
3. D3：确认你句子中的 “Position 持续” 读作 One（F3）；否则须走 canonical 流程。
4. D4：“为了” 以约束闭合为条件（F4）。
5. D11（新增）：认知程序与玩具模拟是否移出 SRT 队列（F5）。
6. D2 / D5 / D6：机器建议合理，按 OUT 接受即可。
7. D10：本 pass 的三个结果（F2 残差、NEG、B6）都指向反同义反复问题，
   因此 A（primitive anti-tautology）是自然的下一问；是否开启由作者决定。
```

## 5. 合并前小修清单（作者可选）

```text
OUT §0 / final       “SUCCESSFUL AS SUBTRACTIVE METHOD” -> containment + typing; older concepts retired = 0 (F1)
FRH0 §5–7            加残差行：graded preclosure -> reselectability / latent reach 或 B6 (F2)
OUT-B                为 Position-relative L0-facing 给出处置 (F2)
OUT D3               写明 Position(time-local) vs One(diachronic) 的迁移 (F3)
OUT D4               加 closure 条件 (F4)
OUT D11              新增：认知程序 / 玩具模拟的 SRT 目标 (F5)
NEG                  改名 back-import checklist；§1 标 K / A (F6)
OUT-D labels         D1–D10 -> FD1–FD10；Gate standing 改名；methodological reconstructibility 登记或改写 (F7)
ST                   Immediate routing 保留三行研究框架护栏 (F8)
```

以上均为作者可选的修正；本评审不代为执行。
