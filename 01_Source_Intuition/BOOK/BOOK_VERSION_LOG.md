---
id: SRT-BOOK-VERSION-LOG
type: book_project_version_log
status: active
canonical: false
scope: 01_source_intuition_book
created: 2026-05-10
updated: 2026-05-10
---

# 《从存在到秩序》书稿版本管理日志

> 本文件只管理书稿施工版本，不替代理论 canonical，不替代正文。

## 版本规则

1. `01_Source_Intuition/BOOK/Part_*` 正文目录只保留稳定章节文件名，例如 `02_L0不是虚无.md`。
2. 后续修订直接写回稳定章节文件；不要再新增 `*_vN*.md` 正文副本。
3. 版本历史由 Git commit / branch 承接；重要版本变化在本文件追加记录。
4. 需要并行试写时，优先使用 Git branch；若只是材料回收，放入 `90_Backstage/Restructure_2026/BOOK_PROJECT/`。
5. frontmatter 中的 `status` 可以继续标注 `draft_vN`、`draft_vN_polished` 等施工状态，但文件名保持稳定。

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
