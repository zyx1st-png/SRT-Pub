---
id: SRT-CHOICE-TRACE-WRITEBACK-PLAN-20260710
type: writeback_plan
tags: [ChoiceMap, ChoiceTrace, Writeback, Theory, Book, Bridge, OpenTensions, Planning]
status: plan_v1_phase1_executed_2026-07-10
layer: meta
epistemic_layer: os
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
created: 2026-07-10
provenance: 基于两份 2026-07-09 choice-trace（第一直觉「选择先于存在」+ 续写「去同步化再同步」）的收尾审计（各自 §6 / §7），整理理论层与书稿层的回写计划。
dependency: [01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md, 01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md, Operations/_SRT_CHOICEMAP_TRACE_WORKFLOW.md]
---

# Choice-Trace 回写计划：理论层与书稿层

> **Phase 1 执行记录（2026-07-10）**：Phase 1 全部无门项已执行。理论侧：T-A（`Core/SRT_OPEN_TENSIONS.md` 新增 §12 熵去选择化张力 + §7 两条 P0-04 直觉证词）、T-F（`04_External_Convergence/FIRST_EVIDENCE_CANDIDATES.md` 新增 Candidate 8 脆弱性候选方向，未编造未核实引用）、T-G（`Philosophy/SRT_Political_Philosophy.md` §6.2 新增显现权/分配权词汇对表注）均已落地。书稿侧：B-A #1/#2/#3/#4/#5-熵半边 以**候选性质章末注**形式落入 `Q06`(v22)/`Q19`(v18)/`Q22`(v29)/`Q28`(v19)，未改写任何既有正文；`Q28` 一并承接了原定位于 `Q18`/幕前·五的熵素材（理由：`Q28` 已有西蒙东亚稳态/热寂铺垫，`Q18` 未涉及熵、幕前·五页面过短不宜插入——详见 `BOOK_VERSION_LOG.md` 2026-07-10 条目）。附录术语表（#8）本轮未补词条：新增内容全部保持候选/章末注密度，未达术语表"正文核心概念"的收录门槛。**Phase 2/3 未执行**——门 G1/G2/G4/G5/G6 是作者裁决项（P8 选对定义、耗散结构排序、两种选择定义的层次关系、六条成文命题确认、三项术语裁决），按 §6 防误用红线不可由执行者代为拍板，仍待作者在下一轮对话中清点。
>
> **性质与边界（先读）**
> 1. 本文件是回写**计划**，非执行记录，非 canonical。列出的每一项在执行时仍须走各自的既有协议：canonical 冻结（`Governance/SRT_CANONICAL_FREEZE.md`）、编辑协议（`Governance/SRT_EDIT_PROTOCOL.md`）。
> 2. **书稿冻结豁免（2026-07-10 作者裁决）**：本计划的书稿轨道**不受 RC1-candidate 冻结约束**，按直接改章执行。首次动章时须在 `BOOK_VERSION_LOG.md` 与 `STATUS.md` 记录本次作者解冻授权及范围（限本计划 §3 所列章节与素材）；书稿其余治理纪律（术语指南、定梁页验收、章 frontmatter 同步）不豁免。
> 3. trace 是 provenance，不是 authority。所有回写命题按仓库惯例登记为 **book/trace-provenance 候选、待验证**，不作"已通过检验"。
> 4. 带 **[门 Gx]** 标记的项被作者裁决阻塞，裁决前不得动工。

---

## 0. 输入盘点

两份 trace 的审计已完成（trace1 §6、trace2 §7）。可回写资产分三档：

| 档 | 内容 | 去向 |
|---|---|---|
| **真实增量**（作者已确认，仓库无落点） | trace1: P6 边界作为存在成分、P10 选择地基四条件+四分层、P12 退化=脆弱性提升、P13 熵=去选择化画像；trace2: 机制链（去同步化/随机化→比较接住→选择性再同步）、1432 循环、P2-06 分配先于显现先于选择、P2-01 幸运开放 | 理论层 bridge / OPEN_TENSIONS / 证据卡 + 书稿轻补丁 |
| **直觉复认**（canonical 已覆盖） | trace1: P1–P5、P8 选错侧、P9；trace2: P2-02/03、P2-14 与 L0 随机性论证的兼容 | 不新增理论；仅在相关 bridge 中作为"直觉证词"引注 |
| **Pending**（未获作者成文确认） | trace1: P8 选对侧（CT-13）、P14 耗散结构排序（CT-23）；trace2: §5.3 六条成文命题（含 P2-16 比较来源、P2-11 分层改写措辞）、张力 T2 裁决 | 全部进 §1 裁决包，确认前不回写 |

一个**正向收敛**单独立项：trace1 P13（熵 = 去选择化后的统计画像，减法定义）与 trace2 P2-14（选择 = 对随机的生成性再同步，加法定义）构成同一边界的对偶表述——两者合并立一个 bridge，不各立。

---

## 1. 门：作者裁决包（Phase 0，阻塞项，建议一次清完）

| 门 | 内容 | 解锁 | 状态 |
|---|---|---|---|
| G1 | CT-13 二次确认：P8「选对 = 维持/扩展后续选择空间」是否按 assistant 提案原文确认或改写 | trace1 命题簇完整性 | 待裁决 |
| G2 | CT-23 二次确认：耗散结构 C+D 核心 / A 弱化 / B 边界的排序 | T-E 耗散结构 bridge + 书稿熵/耗散素材 | 待裁决 |
| G3 | 张力 T1 裁决：「痛苦最原始」限定主体层 | T-B 机制链 bridge 的痛苦接口 + 书稿 Q21 素材 | **已消解**（trace2 §0a.3 已应用 `layered` 改写；剩余的改写措辞确认并入 G5） |
| G4 | 张力 T2 裁决：P2-14 过程定义与 trace1 P7 操作定义的层次关系（建议互补分层） | T-B bridge 的框架 | 待裁决 |
| G5 | trace2 §5.3 六条成文命题逐条确认（含 P2-16 比较来源【现按 `assistant_proposal_pending` 记】、P2-11 分层改写措辞） | 比较—关切接口（d-value 方向）+ S 层对话恢复 | 待裁决 |
| G6 | 术语三项：①「选择地基」改名或分义（撞书稿 Q17 意识第一层）；②「同步化」与神经域 synchrony 显式分义（trace2 §5.1 已登记风险，进 bridge 时执行）；③「最小非中立」统一为「最低非中立性」既有词形 | T-B / T-D 全部动工前置 | 待裁决 |
| G7 | 补收 trace2 各轮选项全集 | trace2 负空间数据 | **已完成**（trace2 §0a.1/§5.5：CT2-02–20 已补回，CT2-01 为 `options_not_applicable`） |

> 建议在下一轮直觉挖掘对话（S 层：「关切到底指什么」）**开场**清 G1/G2/G4/G5/G6——这正是工作流 §2a.4 的恢复纪律。
>
> 另注：trace2 §5.1 已自带 canonical 碰撞三态表（L0 随机性论证、SRT_Suffering、Political_Philosophy、P0-04、神经域 synchrony、跨 trace 对偶均已挂锚）；T-A/T-B 动工时直接引用该表，不重做。

---

## 2. 理论层回写轨道

### T-A · OPEN_TENSIONS 登记（低风险，先行，不受门阻塞）

落点：`Core/SRT_OPEN_TENSIONS.md`（B 类编辑，append）。

1. 新登记一条张力：**熵的去选择化读法**——P13 的主张与 `Core/SRT_Core_25` 的方向差（Core_25 以热力学不可逆性为选择的签名；P13 把熵重定位为"抽掉选择后的剩余画像"），以及 trace1 CT-21 未完成的校准（ontological absence vs theoretical abstraction）。护栏：不得读成 SRT 反熵理论。
2. 在 §7 P0-04 条目下登记两条**直觉证词**：trace1 P2（选择先于主体）、trace2 P2-01（幸运开放）。证词≠解答，仅丰富该未解决点的直觉材料面。

### T-B · 合并 bridge：「熵—随机—再同步」（核心新建）[门 G4/G6]

落点：`03_Bridges/`（按 `BRIDGE_TEMPLATE.md`），登记入 `BRIDGE_INDEX.md`。claim level：P2/P3。

内容骨架：

- 对偶主轴：熵 = 去选择化画像（减法）↔ 选择 = 对随机的比较性再同步（加法）；
- 挂锚：`Core_Law/SRT_L0_Metaphysics.md` 随机性论证（"有约束的确定化即选择"——P2-14 是其操作化改写）；
- 分工划界：与 `Core/SRT_Core_25`（热力学签名桥）互不替代——Core_25 管测量投影，本桥管本体论定位；
- 机制链全链登记：旧同步 → 去同步化/随机化 → 比较接住 → 选择性再同步 → 命名与路径 → 新脚手架（SRT 首个选择发生过程模型）；
- 痛苦接口按 G3 裁决后的分层措辞写，并对齐 `Core_Law/SRT_Suffering.md` 类型学（张力 T3 的消解动作）；
- 术语防区：同步化 ≠ 神经振荡同步（G6②）。

### T-C · bridge：「边界作为存在成分」

落点：`03_Bridges/`。claim level：P2/P3。无硬门。

- 主命题：成功选择生成对象；失败选择生成边界；存在 = 对象 + 边界 + 可能性场三元动态共构（trace1 P6）；
- 挂锚：幽灵算子 Ĝ_θ（"缺席如何作用"获得结构位置：残留位于可能性场与边界之间）、书稿 Q06 三尊幽灵（作为显影不作为证明）；
- 远期出口：若桥经受住压力，才申请 L0 术语裁决（C 类编辑，本计划不含）。

### T-D · 跨域文件：「选择条件」（原"选择地基"，改名后）[门 G6①]

落点：理论层新文件（建议 `Core_Law/` 或 `Philosophy/`，视改名后的定位）。claim level：P2/P3。

- 四条件：可选项充足 + 脚手架 + 代价缓冲 + 对选择的尊重（trace1 P10）；
- 四分层：没有选择 → 伪选择 → 惩罚性选择 → 尊重选择——把 AI 域的"伪选择"（`AI/Ontology_Split/02_PseudoSelection_and_Barrier.md`）一般化为跨域分层，AI 文件回链本文件而非反向；
- 同时是 ChoiceMap 产品指标（选项充足度/脚手架/代价缓冲/可回退性/反牢笼）的理论侧定义源。

### T-E · bridge：「耗散结构 vs 选择结构」[门 G2]

落点：`03_Bridges/`。claim level：P3。

- 划界句（待 G2 确认排序后定稿）：耗散结构解释"秩序如何维持"，SRT 解释"秩序如何不退化为牢笼"；
- 与 T-B 分工：T-B 管熵/随机的本体论定位，本桥管与 Prigogine 传统的显式对表；
- 素材：书稿侧已有 Prigogine expression writeback，可引为表达层参照。

### T-F · External Convergence 证据卡：「脆弱性—选择空间收窄」

落点：`04_External_Convergence/`（按 `EVIDENCE_CARD_TEMPLATE.md`，登记 `EVIDENCE_INDEX.md`）。无硬门。

- 命题接口：退化 = 脆弱性提升；选择空间收窄 → 路径单一化 → 表面稳定实际脆弱（trace1 P12）；
- 候选外部文献族：robustness–fragility tradeoff、HOT（Highly Optimized Tolerance）、反脆弱——是两份 trace 全部命题中最容易接经验证据的一条；
- 按 `EVIDENCE_GRADING.md` 评级，不超格引用。

### T-G · 对表 note：「显现权/分配权 ↔ 政治哲学既有词汇」

落点：轻量——在 `Philosophy/SRT_Political_Philosophy.md` 相关节加回链注，或并入 T-B/T-C 的接口节。

- trace2 P2-07/08/09（显现权、分配权、三重垄断）与该文件已有"现实定义权、风险分配权、未来分支容量系统性不对称固定"是近亲概念，先对表统一词汇，防止平行词汇系生长；
- 「选择贫困」「1432 循环」随对表一并登记为社会本体论素材池条目。

---

## 3. 书稿层回写轨道

**执行方式（2026-07-10 作者裁决）**：不受 RC1-candidate 冻结约束，**直接改章**。仍守书稿治理其余纪律：

- 开工前按 `BOOK_CURRENT_STATUS.md §4` 读取顺序（本文件 → 定位简报 → 目标章及前后章 → 建筑图 → 术语指南）；
- 每章改动同步章 frontmatter 版本号与 `BOOK_VERSION_LOG.md`；全部完成后更新 `BOOK_CURRENT_STATUS.md §2` 进度表；
- 验收基准仍是定梁页（signed_v2.6）：主梁不替换、不新增大章、不过载（不得写成"再选择能力是一切判断的唯一标准"式全称句）；
- 首次动章时在 `BOOK_VERSION_LOG.md` 记录本次作者解冻授权与范围。

### B-A · 直接改章清单（按依赖排序）

| # | 目标章 | 改动 | 来源 | 门 | 预估幅度 |
|---|---|---|---|---|---|
| 1 | Q06 排除与阴影 | 章末收口段：「失败选择生成边界」——背面不只是继续受力，它构成存在的边界成分（成功选择生成对象 / 失败选择生成边界 / 未完成选择保留为可能性场） | trace1 P6 | 无 | 小（1 段 + 章末注） |
| 2 | Q19 脚手架与牢笼 | 显影段：四分层「没有选择 → 伪选择 → 惩罚性选择 → 尊重选择」，与既有"好脚手架留能力/坏脚手架留依赖"对接 | trace1 P10 | 无（分层本身不依赖 G6①；若引入"选择条件"新词则等 G6①） | 小-中（1 节内插段） |
| 3 | Q20 遮蔽 + Q22 方向 | 操作顺序主张：1432 循环（去遮蔽→解笼→重建尺度→重分配→新一轮去遮蔽）——Q20 承接"去遮蔽为什么是第一步"，Q22 §3 权力节承接"垄断如何按此顺序拆" | trace2 P2-10 | 无 | 中（两章各 1 段 + 交叉引用） |
| 4 | Q28 回到生成（+ 幕前·五轻触） | 负向链对位段：「没有选择=没有生成=存在退化→脆弱性提升→熵」作为正向主梁"把选择交还给主体的地面"的暗面收口；Q00 序章只在必要时加一句钩子，不动结构 | trace1 P11/P12/P13 | 无 | 中（Q28 1 段；幕前·五 1-2 句） |
| 5 | Q18 秩序与自由（或幕间桥） | 熵的位置：正面回答"这本书和热力学第二定律什么关系"——熵=去选择化画像（章末注形态优先，防止正文物理化）；耗散半边（秩序维持 vs 不牢笼化）等 G2 后并入 | trace1 P13/P14 | 熵半边无门；耗散半边 G2 | 中（章末注 + G2 后扩 1 段） |
| 6 | Q21 苦难 | 痛苦作为被遮蔽现实最早、最强迫性的显现形式；「主体层最原始动力」分层措辞；用词按 `SRT_Suffering.md` pain/suffering 类型学分义 | trace2 P2-11/P2-13 | G5 | 小-中 |
| 7 | Q15 关切维度 | 「比较来自关切」接口段：关切作为比较空间生成器（为 S 层对话的回流预留位置，不提前写死） | trace2 P2-16 | G5 | 小 |
| 8 | 附录_术语表 | 随 1–7 落地的新表述补词条（边界、四分层、1432 循环、去选择化——以实际进正文者为准） | — | 随各项 | 小 |

**顺序依据**：1–4 无门且相互独立，可一轮完成；5 拆两半（熵半边随 1–4，耗散半边等 G2）；6–7 等 G5（建议下一轮对话开场清掉后立即执行）。

### B-B · 素材池（不进本书）

- 显现权/分配权/选择贫困/三重垄断 → 社会本体论素材池（母书接口的后续延伸卷方向）；
- ChoiceMap 产品指标（含 1432 循环产品化）→ 第二卷（应用/工具卷）前哨，维持种子文件既有定位；
- S 层未完成问题（「关切到底指什么」，候选 S1–S6 已冻结在 trace2 §1）→ 下一轮直觉挖掘对话，产出可能回流 `_SRT_D_VALUE_CANONICAL.md` 接口，但那是 trace3 的事。

### B-B · 素材池（不进本书）

- 显现权/分配权/选择贫困/三重垄断 → 社会本体论素材池（母书接口的后续延伸卷方向）；
- ChoiceMap 产品指标（含 1432 循环产品化）→ 第二卷（应用/工具卷）前哨，维持种子文件既有定位；
- S 层未完成问题（「关切到底指什么」，候选 S1–S6 已冻结在 trace2 §1）→ 下一轮直觉挖掘对话，产出可能回流 `_SRT_D_VALUE_CANONICAL.md` 接口，但那是 trace3 的事。

---

## 4. 执行顺序

| 阶段 | 内容 | 前置 |
|---|---|---|
| **Phase 0** | 作者裁决包 G1/G2/G4/G5/G6（建议下一轮对话开场一次清完；G3/G7 已消解/完成） | — |
| **Phase 1**（可立即，与 Phase 0 并行） | 理论侧：T-A OPEN_TENSIONS 登记、T-F 脆弱性证据卡、T-G 政治哲学对表；书稿侧：B-A #1–4 直接改章（Q06 边界收口、Q19 四分层、Q20/Q22 1432 循环、Q28+幕前·五负向链）+ #5 熵半边章末注 + #8 术语表随动 | 无门 |
| **Phase 2** | T-B 熵—随机—再同步合并 bridge；T-C 边界 bridge；T-D 选择条件文件 | G4/G6 |
| **Phase 3** | T-E 耗散结构 bridge；书稿 B-A #5 耗散半边、#6 Q21、#7 Q15 | G2/G5 |
| **Phase 4**（远期，不在本计划内启动） | P6 三元共构申请 L0 术语裁决（C 类）；S 层对话（关切）→ d-value 接口回流 | T-C 桥硬化 + trace3 |

---

## 5. 验收与留痕规则

- 每完成一项：`STATUS.md` 最近关键推进留痕一条；bridge 入 `BRIDGE_INDEX.md`；证据卡入 `EVIDENCE_INDEX.md`。
- 书稿直接改章：每章同步 frontmatter 版本号 + `BOOK_VERSION_LOG.md` 条目；B-A 全部完成后更新 `BOOK_CURRENT_STATUS.md §2` 进度表；导出校验（`scripts/check_book_outline_split.py`）须保持绿。
- 所有新文件 frontmatter 标 `canonical: false` + trace-provenance；命题一律"待验证"，不写"已证明/已验证"。
- 本计划文件在各阶段完成时更新 status 字段（plan_v1 → 执行进度标注），不重写历史。

## 6. 防误用

- 本计划不是理论内容的一部分；执行任何一项前重读对应协议文件；
- 门未清就动工的项，视为违反委托收敛协议的同类错误——作者裁决不可被计划文件的存在所替代；
- 两份 trace 的 pending 命题（P8 选对侧、P14、P2-16、§5.1 四条）在确认前**禁止**出现在任何 bridge、证据卡或书稿 notes 的正文主张里。
