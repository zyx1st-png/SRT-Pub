---
id: SRT-BOOK-CURRENT-STATUS
type: book_project_current_status
status: active_current
canonical: false
scope: 01_source_intuition_book
role: single_construction_entry
updated: 2026-07-12
layer: meta
epistemic_layer: os
claim_mode: navigation
last_pass: book_retrieval_governance_hardening_2026-07-12
---

# 《从存在到秩序》当前唯一施工入口

> 当前规则：每次写作、修订、AI 协作、founder pass，先读本文件，再读 `BOOK_ACTIVE_MANIFEST.json`。
>
> 本文件不替代理论 canonical，不替代正文。它只负责说明当前书稿实际主线、当前可用元文件、下一步施工优先级和历史结构的归档边界。
>
> **当前施工状态（2026-07-12）**：`2026-06-19` 的 RC1-candidate 正文冻结已由 `BOOK_CURRENT_STATUS_UNFREEZE_ADDENDUM_2026-07-02.md` 解除。当前进入**生成哲学战略总装轮**；解除对象仅为书稿正文与书稿元文件，canonical 理论冻结不受影响。
>
> **当前定位**：一部从 SRT 出发、但不被 SRT 封闭的生成哲学书。旧的“SRT 奠基书 / SRT 说明书”口径仅作历史背景，不再作为当前施工目标。

---

## 0. 当前真实主线

当前正文主线是：

```text
01_Source_Intuition/BOOK/Drafts_26Q/致读者.md
01_Source_Intuition/BOOK/Drafts_26Q/Q00_序章.md
01_Source_Intuition/BOOK/Drafts_26Q/Q01_给定性.md
...
01_Source_Intuition/BOOK/Drafts_26Q/Q04b_选材.md
...
01_Source_Intuition/BOOK/Drafts_26Q/Q15b_能动性.md
...
01_Source_Intuition/BOOK/Drafts_26Q/Q28_回到生成.md
```

说明：

- `Drafts_26Q/` 是历史目录名；当前实际内容采用过渡方案：保留 `Q00–Q28` 文件命名与既有交叉引用，并把 `Q04b_选材.md`、`Q15b_能动性.md` 作为五幕重构新增的两个主题章嵌入阅读顺序。
- 当前阶段不做全书连续重编号；正式出版排版前，再决定是否将 `Q00–Q28 + 两个主题章` 统一为 30 章连续章号。
- 幕前 / 幕间桥属正文阅读顺序：第一幕开门由序章 Q00 承担，幕前·一取消；幕前·二/三/四/五保留；幕终·一/二/三/四与第五幕内部两座幕间桥保留。构建脚本与 `scripts/check_book_outline_split.py` 已登记；当前导出顺序包含 `Q04b`、`Q15b`、幕前与幕间桥。
- 旧 `Part_*` 主稿、旧 `Outline_Parts/`、旧 52 章结构已经下沉到 `01_Source_Intuition/BOOK/Archive_52Chapter/`，只作历史材料和差异审计，不再作为当前施工入口或初稿母版。
- 当前根目录只应保留能继续指导 `Q00–Q28 + 两个主题章` 主线的元文件；被新版取代的元文件放入 `01_Source_Intuition/BOOK/Archive_Meta/`。
- 机器可读的当前章节路由、概念到章节映射与归档降权规则见 `BOOK_ACTIVE_MANIFEST.json`。

当前全书一句话：

> 稳定不是起点，而是选择留下来的历史；秩序不是终点，而是后果回得来的地面。
>
> （主梁全句与施工纪律见 `BOOK_MASTER_BEAM_PAGE_2026-06-12.md`，signed_v2.6。）

---

## 0.1 当前定位

当前书稿定位为：

> **一部从 SRT 出发、但不被 SRT 封闭的生成哲学书。**

SRT 在本书中是发动机，而不是要求读者先接受的一整套说明书。书的任务，是带读者追问对象、主体、稳定世界、选择、价值、意识和秩序这些“已经在那里”的东西如何生成、如何稳定、如何退入背景，以及如何重新开放。

因此，本书不是论文、社交媒体长文、学术综述或纯思想随笔，也不应被写成 canonical 文档的通俗转录。正文可以更白话、更有经验抓手；传统术语承担边界、对照和压力测试功能；形式锚点只负责准确性守门，不负责正文语气。

详细定位以 `BOOK_CURRENT_STATUS_POSITIONING_ADDENDUM_2026-07-02.md` 与新版 `BOOK_POSITIONING_BRIEF_2026-06-07.md` 为准。

---

## 0.2 当前结构口径：五幕生成运动（2026-07-08）

全书结构已从旧“四幕题材分组”升级为“五幕生成运动”：拆地板 → 选材 / 成地板 → 长出世界 → 从摩擦到秩序 → 从秩序回到生成。骨架见 `BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md`，它替代 06-03 建筑图的**结构视图**（六根主梁/各章内容卡仍为有效引用）。

当前实际形态不是重新编号后的 30 章版，而是：`Q00–Q28` 主线章 + `Q04b_选材.md`、`Q15b_能动性.md` 两个主题章 + 幕前 / 幕间桥。两个主题章是五幕重构新增承重点，暂不粗暴替换为正式连续章号。

已经关闭的规划残影：

- **Q10/Q11 保持独立**：Q10 处理秩序的结构，Q11 处理秩序对选择者的预裁剪效应。
- **Q26/Q27 保持独立**：Q26 处理理论作为命题如何失败，Q27 处理理论如何在使用中变成牢笼。
- **本体论摩擦不另立独立章**：已落入 Q18 §3 与后续第四幕脉络。
- **权力不另立独立章**：已落入 Q22 §3。
- **幕前·一取消**：序章 Q00 承担第一幕开门功能；幕前·二/三/四/五保留。

全书一句话：§0 定梁主梁句“秩序不是终点，而是后果回得来的地面”仍是验收基准；五幕骨架 §0 的运动版“把选择交还给主体的地面”是它在第五幕多主体层的延伸，不替换。

当前优先级是生成哲学战略总装、当前主线一致性、导出顺序、元文件同步与评审准备，不是无目标地平均润色全部章节。

---

## 0.3 AI / Agent 施工硬规则

任何涉及本书现状、章节内容、续写、修订或回写的任务：

1. 先读本文件；
2. 再读 `BOOK_ACTIVE_MANIFEST.json`；
3. 根据 manifest 打开 `Drafts_26Q/` 中的当前 primary 文件；
4. 当前 primary 已读取后，才可打开 `Archive_52Chapter/` 或 `Archive_Meta/` 做历史比较。

禁止：

- 以 GitHub 搜索排名、关键词密度、旧稿版本后缀或旧章节编号判断当前性；
- 只读归档稿、不读当前章，就回答“书里现在怎么写”；
- 直接以旧稿作为当前初稿或补丁母版；
- 使用归档材料时不标注“历史稿 / 旧路线”。

---

## 1. 当前可用元文件

| 层级 | 当前文件 | 用途 |
|---|---|---|
| 唯一施工入口 | `BOOK_CURRENT_STATUS.md` | 本文件；确认当前正文主线、状态和读取顺序 |
| 机器路由 | `BOOK_ACTIVE_MANIFEST.json` | 当前主稿根目录、概念路由、归档降权和 Agent 硬规则 |
| 当前定位 | `BOOK_CURRENT_STATUS_POSITIONING_ADDENDUM_2026-07-02.md`, `BOOK_POSITIONING_BRIEF_2026-06-07.md` | 生成哲学书定位；SRT 是发动机而非说明书 |
| 当前结构骨架 | `BOOK_ARCHITECTURE_MAP_5ACT_2026-06-24.md` | 五幕生成运动重构骨架；当前实际形态为 `Q00–Q28 + Q04b + Q15b + 幕前/幕间桥` |
| 章节内容建筑图 | `BOOK_ARCHITECTURE_MAP_2026-06-03.md` | 六根主梁与各章不可删概念、记忆点；仅作内容引用，结构视图已被五幕骨架取代 |
| 当前术语规则 | `BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md` | `Q00–Q28 + 两个主题章` 总修阶段术语降噪、核心记忆点与经验材料纪律 |
| d-value 补丁 | `BOOK_TERMINOLOGY_DVALUE_GOVERNANCE_2026-06-03.md` | Q14/Q15 深度/宽度分工；已并入 06-03 术语指南 |
| 问题链 | `BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` | Q01-Q28 的问题推进与旧稿回收关系；不得覆盖当前五幕结构 |
| 章节卡 | `BOOK_CHAPTER_CARDS_2026-05-22.md` | 每章写作卡片；已覆盖 Q28 |
| 核心命题 | `BOOK_CORE_PROPOSITIONS_2026-05-30.md` | 全书命题压缩版；2026-06-05 已同步 Q21-Q28 |
| 版本日志 | `BOOK_VERSION_LOG.md` | 重要书稿/元文件变更记录 |
| 定梁页 | `BOOK_MASTER_BEAM_PAGE_2026-06-12.md` | 全书主梁“留下与回来”施工图首页（signed_v2.6） |
| 校验读报告 | `BOOK_VERIFICATION_READ_REPORT_2026-06-12.md` | 第一轮全书校验读：合章议题关闭、违例登记、动土许可 |
| 外部评审处置 | `BOOK_EXTERNAL_REVIEW_DISPOSITION_知微_2026-07-04.md` | 当前外部评审过堂与施工裁决 |
| 专业/公共入口 | `PROFESSIONAL_READING_BRIEF*.md`, `PUBLIC_MINIMAL_READING_PACK.md` | 外部读者压缩入口 |

历史文件：

| 位置 | 含义 |
|---|---|
| `Archive_52Chapter/` | 旧 52 章 / Part / Outline_Parts 体系；只作历史、来源和材料库，不得作为当前初稿母版 |
| `Archive_Meta/` | 已被当前 Q00-Q28 与五幕主线取代的元文件；只作历史对照 |
