---
id: SRT-BOOK-CURRENT-STATUS
type: book_project_current_status
status: active_current
canonical: false
scope: 01_source_intuition_book
role: single_construction_entry
updated: 2026-06-12
layer: meta
epistemic_layer: os
claim_mode: navigation
last_pass: polish_round1_batch1_act1_act2_2026-06-12
---

# 《从存在到秩序》当前唯一施工入口

> 当前规则：每次写作、修订、AI 协作、founder pass，先读本文件。
>
> 本文件不替代理论 canonical，不替代正文。它只负责说明当前书稿实际主线、当前可用元文件、下一步施工优先级和历史结构的归档边界。

---

## 0. 当前真实主线

当前正文主线是：

```text
01_Source_Intuition/BOOK/Drafts_26Q/致读者.md
01_Source_Intuition/BOOK/Drafts_26Q/Q00_序章.md
01_Source_Intuition/BOOK/Drafts_26Q/Q01_给定性.md
...
01_Source_Intuition/BOOK/Drafts_26Q/Q28_回到生成.md
```

说明：

- `Drafts_26Q/` 是历史目录名；当前实际内容已经闭合到 `Q00-Q28`，即“序章 + 二十八章”。
- 三座幕间桥属正文阅读顺序：`幕间桥_二三幕.md`（Q10/Q11 之间）、`幕间桥_三四幕.md`（Q17/Q18 之间）、`幕间桥_Q24_Q25.md`（Q24/Q25 之间）。构建脚本与 `scripts/check_book_outline_split.py` 已登记（2026-06-12）。
- 旧 `Part_*` 主稿、旧 `Outline_Parts/`、旧 52 章结构已经下沉到 `01_Source_Intuition/BOOK/Archive_52Chapter/`，不再作为当前施工入口。
- 当前根目录只应保留能继续指导 Q00-Q28 主线的元文件；被新版取代的元文件放入 `01_Source_Intuition/BOOK/Archive_Meta/`。

当前全书一句话：

> 稳定不是起点，而是选择留下来的历史；秩序不是终点，而是后果回得来的地面。
>
> （主梁全句与施工纪律见 `BOOK_MASTER_BEAM_PAGE_2026-06-12.md`，signed_v2.6。）

---

## 0.1 当前定位

当前书稿定位为：**非学院化的 SRT 奠基书**。

这本书不是论文、社交媒体长文、学术综述或纯思想随笔。它存在的理由是：SRT 要移动的不是某个局部观点，而是读者理解现实时默认站立的第一块地板。一般读者不容易接受 SRT，不只是因为术语陌生，而是因为 SRT 追问的是对象、主体、稳定世界、选择、价值、意识和秩序这些“已经在那里”的东西如何生成、如何稳定、如何退入背景。

因此，本书必须系统性讲解 SRT，但不能主要依赖传统学院术语来推进。传统术语可以承担边界、对照和压力测试功能，却不能成为正文主语言；否则读者会被重新带回旧地板。本书的读者入口可以更白话、更有经验抓手，但作者端骨架必须保持体系性：Q00-Q28 需要成为后续意识、AI、价值、自由、共同体和理论方法延伸的母书接口。

详细定位以 `BOOK_POSITIONING_BRIEF_2026-06-07.md` 为准。

---

## 1. 当前可用元文件

| 层级 | 当前文件 | 用途 |
|---|---|---|
| 唯一施工入口 | `BOOK_CURRENT_STATUS.md` | 本文件；确认当前正文主线、状态和读取顺序 |
| 当前定位 | `BOOK_POSITIONING_BRIEF_2026-06-07.md` | 非学院化 SRT 奠基书定位；说明本书为何不是论文/社媒/学术综述/纯叙事 |
| 当前建筑图 | `BOOK_ARCHITECTURE_MAP_2026-06-03.md` | Q00-Q28 闭合后的六根主梁、缺口链、总修顺序 |
| 当前术语规则 | `BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md` | Q00-Q28 总修阶段术语降噪、核心记忆点与经验材料纪律 |
| d-value 补丁 | `BOOK_TERMINOLOGY_DVALUE_GOVERNANCE_2026-06-03.md` | Q14/Q15 深度/宽度分工；已并入 06-03 术语指南 |
| 问题链 | `BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` | Q01-Q28 的问题推进与旧稿回收关系 |
| 章节卡 | `BOOK_CHAPTER_CARDS_2026-05-22.md` | 每章写作卡片；已覆盖 Q28 |
| 核心命题 | `BOOK_CORE_PROPOSITIONS_2026-05-30.md` | 全书命题压缩版；2026-06-05 已同步 Q21-Q28 |
| 版本日志 | `BOOK_VERSION_LOG.md` | 重要书稿/元文件变更记录 |
| 定梁页 | `BOOK_MASTER_BEAM_PAGE_2026-06-12.md` | 全书主梁“留下与回来”施工图首页（signed_v2.6）；总装阶段一切修改的验收依据 |
| 校验读报告 | `BOOK_VERIFICATION_READ_REPORT_2026-06-12.md` | 第一轮全书校验读：合章议题关闭、违例登记、动土许可 |
| 专业/公共入口 | `PROFESSIONAL_READING_BRIEF*.md`, `PUBLIC_MINIMAL_READING_PACK.md` | 外部读者压缩入口 |

历史文件：

| 位置 | 含义 |
|---|---|
| `Archive_52Chapter/` | 旧 52 章/Part/Outline_Parts 体系；只作历史和材料库 |
| `Archive_Meta/` | 已被当前 Q00-Q28 主线取代的元文件 |

---

## 2. 当前正文进度

| 编号 | 文件 | 当前状态 |
|---|---|---|
| 致读者 | `Drafts_26Q/致读者.md` | `draft_v4`（v4 口径对齐：地板句后半改“后果回得来的地面”；二三幕改留下/回来运动口径） |
| Q00 | `Drafts_26Q/Q00_序章.md` | `draft_v23`（v21–v22 漏记轮次补正；v23 润色一轮：注5 簇句变形） |
| Q01 | `Drafts_26Q/Q01_给定性.md` | `draft_v15`（v15 Traces of the Other 正文表达：把真假争论改写为世界如何以特定格式抵达） |
| Q02 | `Drafts_26Q/Q02_对象化.md` | `draft_v18`（v18 润色一轮：§4 二次搭桥去重、反对者出场句变形、“本章不能停”去重、簇句变形） |
| Q03 | `Drafts_26Q/Q03_前对象场.md` | `draft_v17`（v17 润色一轮：操作接口句式变形） |
| Q04 | `Drafts_26Q/Q04_最低非中立性.md` | `draft_v15b`（v13-v15b：西蒙东亚稳态注、主动推断引文升级、独立路径佐证、新地板计数） |
| Q05 | `Drafts_26Q/Q05_选择不是挑选.md` | `draft_v22`（v22 润色一轮：反对者出场句变形、§1/§7 簇句变形、操作接口句式变形） |
| Q06 | `Drafts_26Q/Q06_排除与阴影.md` | `draft_v13`（v13 Traces of the Other 正文表达：被排除者以痕迹改变当前路径，而非完整返回） |
| Q07 | `Drafts_26Q/Q07_锚定.md` | `draft_v15`（v14 章末注重编号同步；v15 去环专项：§4“结构闭环”改“锚定阶梯”章内语汇） |
| Q08 | `Drafts_26Q/Q08_不可逆性.md` | `draft_v15`（v13–v14 漏记轮次补正；v15 润色一轮：§3 三连“上一章说”去重、链条回顾引导句变形） |
| Q09 | `Drafts_26Q/Q09_现实厚度.md` | `draft_v19`（v18 漏记轮次补正；v19 润色一轮：反对者出场句变形） |
| Q10 | `Drafts_26Q/Q10_秩序背景化.md` | `draft_v16`（v16 润色一轮：连续“到这里”去重、§3 簇句变形、注七簇句变形） |
| Q11 | `Drafts_26Q/Q11_被选择.md` | `draft_v16`（v16 Traces of the Other 正文表达：可见性是接口结果，不是世界边界） |
| Q12 | `Drafts_26Q/Q12_攸关.md` | `draft_v17`（v17 主梁试焊：§4“承重的两个方向”定理段，Q09/Q05 交叉引用） |
| Q13 | `Drafts_26Q/Q13_在乎.md` | `draft_v17`（v17 Embodied Development 正文表达：在乎会改写走路、回避、等待和日常安排） |
| Q14 | `Drafts_26Q/Q14_价值不是偏好.md` | `draft_v12`（v12b 回头轮：接口标签 + Q28 测试回指核验） |
| Q15 | `Drafts_26Q/Q15_关切维度.md` | `draft_v15`（v14 §7 去环；v15 薄 ε 红线修复 V-R1：删“和最低非中立性”） |
| Q16 | `Drafts_26Q/Q16_主体沉积.md` | `draft_v21`（v21 ε 归因校正 Y-R1：选择先于主体记账到第四＋五章） |
| Q17 | `Drafts_26Q/Q17_意识.md` | `draft_v24`（v22 迪肯目的动力学注 C／v23 达马西奥注 H；v24 断言密度专项：§4–§5 旗标命题降为候选安置／最小接口／可失败位置＋章末注重复铺陈压缩，47,001→44,151 bytes connector-safe 转绿，三层结构与 Q25 边界接口保留） |
| Q18 | `Drafts_26Q/Q18_秩序与自由.md` | `draft_v11`（v11 Embodied Development 正文表达：限制也可以成为可承受的学习脚手架） |
| Q19 | `Drafts_26Q/Q19_脚手架与牢笼.md` | `draft_v12`（v12 Embodied Development 正文表达：好脚手架留下能力，坏脚手架留下依赖） |
| Q20 | `Drafts_26Q/Q20_遮蔽.md` | `draft_v14`（v14 Traces of the Other 正文表达：遮蔽不是藏起事实，而是把事实改译成当前秩序可吸收格式） |
| Q21 | `Drafts_26Q/Q21_苦难.md` | `draft_v11`（v11 Simondon 正文表达：个体痛苦的结构错配与共同地形） |
| Q22 | `Drafts_26Q/Q22_方向.md` | `draft_v18`（v18 Prigogine/Stengers 正文表达：好方向不是死平衡，而是保留可再选择张力） |
| Q23 | `Drafts_26Q/Q23_共同体.md` | `draft_v18`（v17 §4 秩序级关切宽度安装；v18 去环化七处，记忆点改“后果还回不回得来”） |
| Q24 | `Drafts_26Q/Q24_AI.md` | `draft_v22`（v20-v21 融合轮；v22 ε/真实摩擦归因校正 Y-R2，两处章末注） |
| Q25 | `Drafts_26Q/Q25_选择广于意识.md` | `draft_v11`（v11b 评审轮：§7 冰川/绒泡菌区分） |
| Q26 | `Drafts_26Q/Q26_可证伪性.md` | `draft_v12`（v11 迪肯 autogen 注八；v12 章末注九：主梁三条失败条件记账并映射正文五条件） |
| Q27 | `Drafts_26Q/Q27_理论自反.md` | `draft_v11`（v11 Traces of the Other 正文表达：异常材料须保留竞争解释、失败结果与非 SRT 复核） |
| Q28 | `Drafts_26Q/Q28_回到生成.md` | `draft_v13`（v11 合梁三焊：暗线补回程、薄 ε 违例修复、§9 双地板句收口；v12 注四一致性；v13 §5 回流落点消歧） |
| 幕间桥 | `Drafts_26Q/幕间桥_二三幕.md` ／ `幕间桥_三四幕.md` ／ `幕间桥_Q24_Q25.md` | `draft_v1`×3（梁级路标：留下运动收束／回来运动收束＋第四幕三种断法读法／诊断收束＋刀转向自己） |

---

## 3. 当前写作顺序

当前全书已经从旧 52 章路线收束到 Q00-Q28 闭合版。近期施工优先级按 `BOOK_ARCHITECTURE_MAP_2026-06-03.md`、`BOOK_POSITIONING_BRIEF_2026-06-07.md` 与 `BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md` 执行：

1. ~~元文件同步~~（2026-06-06 完成：建筑图、核心命题与状态表同步）
2. ~~Q06-Q10 机制段专项审计~~（2026-06-06 完成：Q06-Q09 问题秩序改变段落 + Q00 §四压缩）
3. ~~Q11-Q15 问题秩序改变段落审计~~（2026-06-07 完成：Q11/Q12/Q13/Q15 四章补齐）
4. ~~模板疲劳微修~~（2026-06-07 完成：Q11 对手入口直接化、Q12 跨领域折叠、Q13 旧地板开法变化）
5. ~~普通读者入口~~（2026-06-07 完成：新增 `致读者.md`，四幕地图 + 阅读建议）
6. ~~Q16-Q20 问题秩序改变段落检查~~（2026-06-07 完成：Q16/Q19/Q20 三章补齐；致读者→Q00 衔接验证通过）
7. ~~全书定位补丁~~（2026-06-07 完成：新增 `BOOK_POSITIONING_BRIEF_2026-06-07.md` 并挂入当前入口）
8. ~~第四幕（Q21-Q28）质量审计~~（2026-06-07 完成：经验入口、对手力度、跨领域折叠、理论自限四维通过；无需结构性修改）
9. 全书语言润色第一轮：跨章节过渡衔接 + 重复句式消除 + 模板疲劳微调。**第一批已完成（2026-06-12，致读者＋Q00–Q10＋幕间桥二三幕）**：全书量化扫描（“不是…而是”603 处、“旧地板”73 处、“本章要做/本章不”63 处、反对者出场句四章同型）；第一批施工 7 章 20 处词句级——Q02 §4 二次搭桥去重、Q08 §3 三连“上一章说”去重、Q02/Q05/Q09 反对者出场句变形（Q01 留原型作锚，Q06/Q07 已自带变体）、“但本章不能停在这里”逐字重复去重（留 Q01）、六处段内“不是…而是”机械簇变形、Q03/Q05 操作接口句式变形、Q10 连续“到这里”去重、Q08 链条回顾引导句变形。**刻意保留**：Q03 §9 L0 收束排比、Q09 “现实重量是被踩出来的”平行句、Q10 “强到成了背景”、双地板句、各章定义黑体句与最后一拍。致读者／Q01／Q04／Q06／Q07／幕间桥扫描后判定干净或已有变体，零改动。**待办第二批**：Q11–Q17＋幕间桥三四幕（重点 Q16 38 处“不是…而是”、Q11 33 处）；**第三批**：Q18–Q28＋附录（重点 Q28 36 处、Q20/Q22 28–30 处、第四幕“到这里”收束句型）。
10. 全书语言润色第二轮：逐章行级打磨。
11. ~~Q07 去环专项~~（2026-06-12 完成：§4“结构闭环”改“走完留痕、承重、再入场的阶梯”，取 §2 既有“锚定阶梯”语汇；全量扫描确认其余“回路/循环”均有正当职务——神经/技术义、对手语态隔离墙、Q14 偏好图景贬抑装置、Q16 反馈对照论证——两处低优先候选 Q12 §4“构成一个循环”与 Q20 §4“社会回路”留作者裁决，未动）。
12. ~~**Q17/Q25 断言密度专项（硬触发已到，作者裁定 2026-06-12）**~~（2026-06-12 完成，中等手术）：`Q17_意识.md` 原 47,001 字节超过 connector-safe 上限 45,000——main 既有 CI 红灯（`scripts/check_book_outline_split.py`）。本专项一次处理三件事：① 尺寸超限——压到 **44,151 bytes**（留约 849 bytes 余量），`check_book_outline_split.py` 转绿；② 断言密度——§4–§5 四句旗标命题（“感受性＝回流张力内部面”“感受质＝从承重位置内部被经历的样子”“反身意识＝内部历史闭合承重层”“先有主体反身意识才凝结”）由黑体直陈降为**候选安置／最小接口／可失败位置**，命题实体与原创密度保留，三层意识结构不拆；③ 感受质安置——明确“候选模型，不是困难问题终结判决”。尺寸余量主要取自八条章末注重复铺陈与重述段压缩（A/C/D/E/F/G/H）。**Q25 随轮复核后不改**：§4 分化命题已有四层护栏（回读范畴非预存原料／非基质一元论／分化产物仍真实／生成一元论定位非心物终解），表达强度充分，改动反而违反“不得大改 Q25”。未重开任何总装阶段已关闭裁决。

---

## 4. 每次开工的读取顺序

1. 读本文件，确认当前正文主线和历史归档边界。
2. 读 `BOOK_POSITIONING_BRIEF_2026-06-07.md`，确认“非学院化 SRT 奠基书”的定位红线。
3. 读目标章节、前一章、后一章。
4. 读 `BOOK_ARCHITECTURE_MAP_2026-06-03.md`，确认该章在六根主梁和缺口链中的位置。
5. 读 `BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md`；若涉及 Q14/Q15 或 d-value，再核 `BOOK_TERMINOLOGY_DVALUE_GOVERNANCE_2026-06-03.md`。
6. 需要深结构时读 `BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` 和 `BOOK_CHAPTER_CARDS_2026-05-22.md`。
7. 需要命题压缩或专业入口时读 `BOOK_CORE_PROPOSITIONS_2026-05-30.md` 和 `PROFESSIONAL_READING_BRIEF*.md`。
8. 只在追溯旧 52 章材料、旧 Part 主稿、旧 Outline_Parts 时进入 `Archive_52Chapter/`。

---

## 5. 当前护栏

1. 不把书稿句子升级为 canonical 定义；书稿是 `canonical: false` 的源头哲学主文本。
2. 不再把 `Archive_52Chapter/Outline_Parts/` 当作当前章节状态入口。
3. 不再使用 `BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-02.md` 指导当前正文；当前术语规则以 06-03 v4.1 为准。
4. Q14 讲价值深度，不使用 d-value；Q15 讲关切宽度，d-value 只在这里后置命名。
5. Q25 负责“选择广于意识但不是泛心论”的边界；不要把早期选择结构误写成意识泛化。
6. Q26/Q27/Q28 是理论自限与回到生成，不是把 SRT 包装成封闭体系。
7. AI、科学、跨领域与实证材料可以承担局部经验支持、结构锚点和最小证明压力，但不能承担整套 SRT 的证明任务，也不能展开成学科综述。
8. 本书当前定位是“非学院化 SRT 奠基书”：读者入口可以白话化、经验化，但不能牺牲 Q00-Q28 作为后续意识、AI、价值、自由、共同体与理论方法延伸母书的体系功能。
9. 传统哲学和学科术语可以作为边界、对照和压力测试进入，但不能成为正文主语言；否则会把 SRT 重新拉回旧地板。

---

## 6. 更新规则

- 章节正文更新：同步目标章节 frontmatter、必要时同步 `BOOK_VERSION_LOG.md`。
- 全书结构更新：同步本文件、`BOOK_ARCHITECTURE_MAP_2026-06-03.md` 或新建筑图、`BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md`、`BOOK_CHAPTER_CARDS_2026-05-22.md`。
- 定位更新：同步 `BOOK_POSITIONING_BRIEF_2026-06-07.md`；若改变“非学院化 SRT 奠基书”定位，必须同步本文件、`致读者.md` 和公共入口材料。
- 术语规则更新：同步 `BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md`；若改变 d-value 用法，必须同步 d-value 治理补丁并核 `_SRT_D_VALUE_CANONICAL.md`。
- 历史材料归档：不删除有 provenance 价值的旧文件；从根目录移入 `Archive_Meta/` 或 `Archive_52Chapter/` 并在当前入口说明。
- 不把 `Archive_*` 文件、backstage notes、operations logs 写成新的定义权威。

---

## 7. 出版导出规则

源文件保留完整 YAML front matter，用于仓库状态、版本管理与 AI 协作。

出版稿 / 读者版导出时应自动剥离 YAML front matter，只保留正文 Markdown。注意：`---` 也在正文中用作章节分隔线，请勿使用 `sed '/^---$/,/^---$/d'`（会误删正文分隔线）。

推荐导出方式（只剥离文件开头第一段 YAML front matter）：

```bash
awk 'NR==1 && $0=="---" {skip=1; next}
     skip && $0=="---" {skip=0; next}
     !skip {print}' 原文件.md > 导出文件.md
```

或使用 pandoc：

```bash
pandoc 原文件.md -o 导出文件.pdf
```

正文中的 `optimization_axis`、`based_on`、`references` 等字段不进入读者稿；这些信息留存于源文件 YAML 和 `BOOK_VERSION_LOG.md`。
