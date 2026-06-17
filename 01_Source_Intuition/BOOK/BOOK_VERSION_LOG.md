---
id: SRT-BOOK-VERSION-LOG
type: book_project_version_log
status: active
canonical: false
scope: 01_source_intuition_book
created: 2026-05-10
updated: 2026-06-17
layer: meta
epistemic_layer: os
claim_mode: navigation
---

# 《从存在到秩序》书稿版本管理日志

> 本文件只管理书稿施工版本，不替代理论 canonical，不替代正文。

## 2026-06-17 LLM、公共对象与生活场书稿备注

新增 `BOOK_NOTE_OBJECT_BEHIND_OBJECT_LLM_PUBLIC_REASON_2026-06-17.md`，作为 active note 保存“对象背后的生活场、LLM 与公共理性的重新开放”轴线。该备注不改正文、不新增 canonical 定义；其功能是为后续 Q02/Q05/Q14-Q15/Q20-Q24/Q26-Q27 提供展开接口：科学对象化是必要截面，但不能垄断什么经验、压力、痛苦和价值有资格成为公共理性中的合法对象；LLM 不作为新权威，而作为帮助主体显影选项结构、把尚未命名的压力带入可批评公共空间的工具。具体触发事件和私人通信信息不进入正文。

## 2026-06-15 Q04-Q09 远端 main 底稿冲突吸纳微修

以 GitHub 远端 `main` 最新版为底稿，只吸纳先前 Q04-Q09 冲突分支中经裁决保留的句子级优点，拒绝整章版本回退。

本轮正文微修四章：Q04 `draft_v20→draft_v21`，硬币段补“最低非中立性不是对象、也不预设具体形态”的边界，并修正异常引号；Q05 `draft_v26→draft_v28`，行动理论段补“选项和行动者稳定之前”的追问位置，保留远端既有 v27 引擎护栏轴线；Q08 `draft_v21→draft_v24`，修复护栏改成正面表达并统一中文引号，保留远端 v22/v23 护栏轴线；Q09 `draft_v23→draft_v25`，在远端 v24 guardrail 底稿上吸纳峡谷转场、注意力响度/选择厚度区分，以及厚≠真/正当的终段护栏。

Q06/Q07 未修改；Q17 v26 与远端后续 Q18-Q28 写回状态保留。Canonical 未修改。

## 版本规则

1. 稳定章节文件仍是最终入口，例如 `02_L0不是虚无.md`。
2. `Part_*` 正文目录应只保留当前可读主稿；过程版本、候选稿、alignment pass 和 hardening pass 应进入 `Versioned_Drafts/` 或工具中转目录。
3. 为兼容 ChatGPT / 网页 GitHub 工具，若不得不在 `Part_*` 正文目录短期生成独立新版本文件，应在本地同步时尽快合并、清理，并移入 `Versioned_Drafts/`。
4. 独立版本文件应在 frontmatter 标注 `status`、`based_on`、`optimization_axis`；若知道基准 commit / blob SHA，也应写入。
5. 稳定正文与独立版本文件只允许短期并存。后续由本地 git 环境比较、合并、清理，把最终版本回写到稳定章节文件。
6. 版本历史最终由 Git commit / branch 承接；重要版本变化在本文件追加记录。
7. `90_Backstage/Restructure_2026/BOOK_PROJECT/update_queue/` 保留为可选通道，用于 section patch、合并说明或不适合放入正文目录的工具中转材料。
8. 稳定主稿 frontmatter 保留精确来源 `status`，并增加 `maintext_status: stable_candidate`，用于区分当前主阅读入口与过程稿。

## Web / GitHub 工具写入规则

当 ChatGPT / 网页工具有新版要提交时：

1. 如果能可靠取得目标稳定文件的完整内容和 blob SHA，可以直接更新稳定章节文件。
2. 如果读取大文件被截断、无法可靠取得 blob SHA，优先创建 `Versioned_Drafts/` 或 `update_queue/` 中转稿；若工具限制导致必须在同一 `Part_*` 正文目录创建独立版本文件，只能作为短期中转。
3. 独立版本文件命名建议：
   `08_选择算子_从可成为性到显现_v5_polished.md`
4. 不要求网页工具强行使用 `update_queue`。`update_queue` 只作为可选的 patch / notes 通道。
5. 后续清理时，把最新版并入稳定文件名，删除或归档多余版本副本，并在 Git commit 中保留历史。卷级 pass 后的主目录不得长期保留过程版本。

## 2026-05-10 版本收束

本次把 `Part_*` 正文目录中的多版本章节收束为稳定文件名。旧 `*_vN*.md` 文件已从工作树移除，内容仍可通过 Git 历史追溯。

| 章 | 稳定文件 | 本次采用来源 | 从工作树移除的旧版本 |
|---:|---|---|---|
| 2 | `Part_01_从存在到成为/02_L0不是虚无.md` | `02_L0不是虚无_v13_polished.md` | v9, v10, v11, v12, v13 |
| 3 | `Part_01_从存在到成为/03_ε_pg_L0的最小非中立性.md` | `03_ε_pg_L0的最小非中立性_v12_polished.md` | v8, v9, v10, v11, v12 |
| 4 | `Part_01_从存在到成为/04_选择不是挑选.md` | `04_选择不是挑选_v10_polished.md` | v6, v7, v8, v9, v10_candidate, v10_polished, v11_candidate |
| 5 | `Part_01_从存在到成为/05_锚定让一留下.md` | `05_锚定让一留下_v15_polished.md` | v6, v7, v8, v9, v10_integrated_candidate, v11_recursive_candidate, v12, v13_no_L1_frontstage_candidate, v14_third_tier_candidate, v15_polished, v15_refined_candidate |
| 6 | `Part_01_从存在到成为/06_秩序如何成为背景.md` | `06_秩序如何成为背景_v9_polished.md` | v5, v6, v7, v8, v9 |
| 7 | `Part_02_选择的本性/07_地形如何反过来选择人.md` | `07_地形如何反过来选择人_v16_final_compression_pass.md` | v8, v9, v10, v11, v12, v13, v14, v15, v16 |
| 14 | `Part_03_从选择到主体与价值/14_在乎是什么.md` | `14_在乎是什么_v4.md` | v1, v2, v3, v4 |
| 15 | `Part_03_从选择到主体与价值/15_价值不是偏好.md` | `15_价值不是偏好_v4.md` | v1, v2, v3, v4 |
| 16 | `Part_03_从选择到主体与价值/16_d-value_在乎的最小形式化尝试.md` | `16_d-value_在乎的最小形式化尝试_v5.md` | v1, v2, v3, v4, v5 |

选择原则：

- 卷一第 2–6 章采用已在施工入口中标为当前基准 / active draft 的 polished 稿。
- 卷二第 7 章采用当前最高压缩版本 `draft_v16_final_compression_pass`，但仍需人工/卷二一致性确认。
- 卷三第 14–16 章采用当前最高已有版本，并合并为稳定文件名；后续仍暂缓，待卷二重构后再做第三类 pass。

## 2026-05-11 卷二版本归档

本次同步远端后，将卷二第 7–9 章的最新版回写到稳定章节文件名，并把独立版本草稿移入 `Versioned_Drafts/Part_02_选择的本性/`。正文目录只保留稳定入口；旧稿仍作为仓库内版本材料保留，后续也可通过 Git 历史追溯。

| 章 | 稳定文件 | 本次采用来源 | 归档的独立版本 |
|---:|---|---|---|
| 7 | `Part_02_选择的本性/07_地形如何反过来选择人.md` | `07_地形如何反过来选择人_v18_final_literary_philosophical_polish.md` | v17, v18 |
| 8 | `Part_02_选择的本性/08_选择算子_从可成为性到显现.md` | `08_选择算子_从可成为性到显现_v5q_final_compression_pass.md` | v5, v5c–v5q |
| 9 | `Part_02_选择的本性/09_排除_选择的阴影.md` | `origin/codex/ch09-v5s-third-tier-tightening` 的 `09_排除_选择的阴影_v5v_cross_scale_tempered_pass.md` | v5s, v5t, v5u, v5v |

选择原则：
