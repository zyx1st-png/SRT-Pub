---
id: SRT-CONFIRMED-PROPOSITION-SEMANTIC-COVERAGE-AUDIT-20260808
type: audit
status: active
record_stage: audit_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-08-08
source_of_truth: "origin/main @ aa56d7f2"
machine_readable: Operations/Audits/data/srt_confirmed_proposition_semantic_coverage_2026-08-08.json
probes: Operations/Audits/SRT_SEMANTIC_COVERAGE_PROBES_2026-08-08.md
dependency:
  - SRT-OPS-AUDIT-ACTIVE-THEORY-ASSIMILATION-2026-08-06
  - SRT-BOUNDED-RETRIEVAL-PROTOCOL-20260808
tags: [Governance, Audit, SemanticCoverage, ConfirmedPropositions]
---

# 已确认命题的语义覆盖审计（2026-08-08）

> **审计单位改了。** 此前是 SourceCard / patch / hook / owner path / router / bundle——**文件工程状态**。本轮改为**已确认的理论命题与区分**。
>
> 换单位的理由是连续五次假阴性：静态清单五次判"未吸收"，五次被行为探针推翻。文件状态不能可靠推断思想是否进入理论。

---

## 0. 一句话

> 审计了 **18 条已确认命题**（不是 18 个文件）。**11 条已显式吸收，2 条隐式，4 条部分，1 条冲突。真正 confirmed-but-unassimilated 的：1 条，而且它不是理论命题，是一个导航文件陈旧。**
>
> 换句话说：**在本轮抽样范围内，没有找到一条"作者已确认、AI 从当前 theory owners 学不到"的理论命题。**

这是阴性结果，而且是本轮最有价值的结果。

---

## 1. 覆盖范围（不得外推）

| 已覆盖 | 未覆盖 |
|---|---|
| `Operations/SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md` 的全部 **13 条**作者已确认命题（G1/G2/G4/G5/G6）——这是仓库中**唯一已完全关闭的 author gate** | 其余约 127 条 A 类 Material Log 行 |
| **5 条** Pipeline 1 A 类材料命题（REP01、NEURAL23、NEURAL18、P07，加 1 条行为发现） | 11 份 author gate **未关闭**的 choice trace / ghost card——按本轮规则，它们是 provenance 不是已确认理论，明确排除 |
| AI / Consciousness / Neural / Physics 四个高价值区 | 10 份 `Conversations/`（其索引自述证据等级低于 choice trace） |
| | 书稿术语同步桥的候选词；Spirituality 全域 |

**18 条是样本。其类别分布不得当作全仓统计。**

---

## 2. 只抽取"已确认"的，不抽取过程材料

按本轮规则，**不**计入：assistant proposal、pending confirmation、未被选中的分支、brainstorming、trace 原话本身。

作者裁决文件恰好提供了干净的边界：G1/G2/G4/G5/G6 五个门都写明"作者确认"，且文件 §7 明确列出"本轮裁决解锁什么 / 不授权什么"。13 条命题全部取自该文件的确认语，未从 trace 正文自行提炼。

---

## 3. 结果

| coverage_class | 条数 | |
|---|---:|---|
| `explicitly_assimilated` | **11** | 活跃 owner 有语义明确、边界相同的对应内容 |
| `implicitly_assimilated` | **2** | 无同一句，但现有理论结构可明确推出且不丢关键限制 |
| `partially_assimilated` | **4** | 主命题进了，护栏／边界／降级条件没全进 |
| `archived_only` | **0** | — |
| `conflict_with_active_theory` | **1** | 见 §5 |
| `redundant` | 0 | |
| `author_gate` | 0 | |

### 3.1 三条 A 类材料命题从 `archived_only` 被推翻

初稿按"有没有 hook / 落点文件在不在"把 REP01、NEURAL23、NEURAL18 判为 `archived_only`。**bounded 探针全部推翻：**

- **REP01**：`px` 运行 1 次导航到达，7/7 全对，覆盖 theory-package 五元组与 package-targeted falsification。三张 hook 指向的 `Physics/SRT_Physics_Bridge_v0_2.md` 从未创建——**完全没有妨碍**。
- **NEURAL23**：`nd` 运行 **0 次导航**，`STATUS.md` 启动层本身就带着 `selection weight / selection opportunity / friction` 三分。
- **NEURAL18**：同一次运行 0 导航到达，五分表（decodability / causal access / behavioral use / conscious anchoring / L2 write-back）完整可用。

**这是第 3、4、5 次假阴性。**

### 3.2 四条 `partially_assimilated`

| 命题 | 缺的是什么 |
|---|---|
| **G5-2** 痛苦是具身位上的结构性损失压力 | 只落在 T-B 桥。canonical 苦难 owner `Core_Law/SRT_Suffering.md` 中「结构性损失」「具身位」命中 **0**，且**不反向链接** T-B（T-B 链接它 2 次，单向）。作者裁决自己写明"进入正式理论文件时仍须与 pain/distress/suffering 既有类型学逐项对表"——**该对表从未执行**。语义张力具体在：owner 的 `Def-PAIN` 限定为 `θ_somatic` 躯体威胁信号，而 G5-2 的「痛苦」明含「可选路径收缩／未来选择空间被压缩」，后者在 owner 词汇里属 suffering 而非 pain。**两处「痛苦」外延不同。** |
| **G5-5** 痛苦的最低强制性地位 | 同上，只在 T-B。 |
| **G5-4** 关切的关系性加权 | d-value canonical 覆盖了「关切 ≠ 有意识欲望」，但没有把关切放到**候选形成门**上——那里 `d` 是选择事件整合的关切范围，不是候选准入的加权器。 |
| **G6-2** 「选择性再组织」统一用词 | `Core/SRT_OPEN_TENSIONS.md §12`（2026-07-10 登记，早于裁决）仍以 resynchronization 呈现该读法。**这不违规**——它是按 G6-2 允许的第一种场景引用 source trace。但 §12 没告诉读者该词已于 2026-08-04 被裁定不再作跨层级定义用语。**陈旧，非冲突。** |

**四条都不是"AI 学不到"。** 它们是"AI 从 owner 学到的版本，比作者确认的版本少一层限制或少一个入口"。这是有意义的差别，但不是本轮要找的那种缺口。

---

## 4. 删除测试

对每条命题问：**删掉原始 SourceCard / patch / trace，只读 theory owner 的 AI 是否仍有该命题的实质判别能力？**

结果最有说服力的是 Choice Generation。`cg1` 与 `cg3` 两次 bounded 运行，**都没有打开 T-D 条件矩阵，也都没有打开 PR #744 新建的 CompactCore**，却都答对全部题目——它们改用 canonical 骨架（P1-T05 / P1-T06 / P0-02 / P0-03 / 赌注门 `R·A·C`）加各自的第二条路径拼出等价判别。

**该节点的判别能力在 canonical 层就够了。** 快速层不是它可用的原因。这与 2026-08-07 的零差分结论一致，并且这次是在**有界预算**下复现的。

---

## 5. 唯一一条 confirmed-but-unassimilated

它不是理论命题。

| | |
|---|---|
| **`NAV-NEURO-REGISTRY`** | `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` 已陈旧 |
| 来源 | `nd` 运行**主动报告**，非静态审计发现 |
| 内容 | 该 registry 是 `active_v2`（2026-05），§1/§4 的图止于 N9，未提 N10–N12 或任何 NEURAL15–23 patch，也不指向 `_SRT_Neuroscience_Hardening_Index.md` 作为当前 material-patch 权威 |
| 为什么重要 | 一个只按该 registry 声明的「最短主线」阅读顺序走的 agent，会**错过决定 Q1–Q7 的每一个文件**。这次探针成功是因为检索画像的领域起点图把它带到了 hardening index，不是因为 registry 起作用 |
| 影响的判断 | 可解码性 ≠ 锚定、编码门 ≠ 稳定化门、ATP ≠ 已支付负担、中心性 ≠ 因果、节律 = selection opportunity |
| 修法 | 一行指针。**不是理论写回。** |

方向值得注意：这是与那五个假阴性**相反**的一类发现——静态审计看不见，行为探针看得见。

---

## 6. 静态审计假阴性的来源

五次假阴性，三个来源：

1. **从「没有 hook」推「内容没进 owner」**（AIREASON01/AIEVID01、NEURAL18、REP01）。内容可经 hook 之外的路径落地——直接写进 owner、写进 STATUS、或就留在域内 patch 里而被域起点图捞到。
2. **从「落点文件不存在」推「不可达」**（Physics 三张 hook 指向从未创建的 `_v0_2`）。落点缺失挡的是"这笔回写有没有归位"，不是"这个判别能不能被取到"。
3. **可达性统计没计入实际检索行为**：frontmatter `dependency:` 链、`STATUS.md` 权威锚点、检索画像的领域起点图、以及 `<域>/patches/` 本身都在有界预算内可达。原先 80.6% 的"不可达"只度量"是否被活跃表面文件按文件名提及"。

三次探针还找出**三个静态审计从未登记过的 owner**：`Neuroscience/SRT_FEP_MetaAwareness_AffectiveSelf_Bridge.md`、`Philosophy/SRT_Phenomenal_Structure_Interface.md`、`Core_Law/SRT_Individuation.md`。清单本身是不完备的。

---

## 7. 结论：本轮不施工

除 PR #744 自身的方法收口外，**不修改** canonical、Core owner、domain owner、CompactCore、router、bundle。

理由是审计结果，不是保守：抽样的 18 条里没有一条构成 genuine content gap。唯一可动的是那一行 registry 指针，而它属于导航修复，不属于理论写回——本轮按纪律**不做**，登记待办。

---

## 8. 下一步该做什么（不是施工队列）

1. **扩大语义审计样本**，而不是开始写回。当前 18 条只覆盖唯一一个已关闭的 author gate 加 5 条材料。真正的缺口若存在，更可能在未抽样的 127 条 A 类材料里。
2. **修 `NEUROSCIENCE_COMPACT_REGISTRY.md` 的指针**（单独一个小 PR）。
3. **执行作者裁决自己欠下的那笔**：G5-2 与 `pain / distress / suffering` 既有类型学的逐项对表。这是作者已经写明要做而从未做的，是本轮找到的最接近"真实理论工作"的一项——但它是**对表**，不是新增命题。
4. **给 `Core/SRT_OPEN_TENSIONS.md §12` 加一行**说明 G6-2 的用词裁决。
5. 停止用"有多少材料没闭环"作为进度指标。

---

## 9. 局限

1. **18 条是样本**，覆盖唯一一个已关闭的 author gate 加 5 条材料。类别分布不得外推。
2. 语义匹配由我判定。grep 只用于定位候选，最终裁决靠阅读——但"读懂了没有"本身无法自证。
3. 删除测试由 bounded 探针近似，探针题目由我设计，**系统性盲点按定义测不到**。
4. `partially_assimilated` 的四条里，"少一层限制算不算缺口"是判断而非测量。我判为不算，因为探针显示 AI 不会因此判错；但若有人认为 canonical owner 必须自带全部作者确认语，结论会不同。
5. 本审计不评价任何命题的**真值**，只评价其**可达性与完整性**。
