---
id: SRT-BOOK-VERSION-LOG
type: book_project_version_log
status: active
canonical: false
scope: 01_source_intuition_book
created: 2026-05-10
updated: 2026-05-14
---

# 《从存在到秩序》书稿版本管理日志

> 本文件只管理书稿施工版本，不替代理论 canonical，不替代正文。

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

- 第 7 章采用当前最高文学 / 哲学 polish 版本 `draft_v18_final_literary_philosophical_polish`。
- 第 8 章采用当前最高机制压缩版本 `draft_v5q_final_compression_pass`。
- 第 9 章采用未合并远端分支中的最高 tempering pass：`draft_v5v_cross_scale_tempered_pass`。
- `Versioned_Drafts/` 是书稿版本归档区，不替代稳定正文入口。

## 2026-05-11 第十章版本收束

本次将第 10 章最新版回写到稳定章节文件名。稳定文件路径暂不改名，以免破坏既有引用；章节内标题已随最新版调整为“不可逆性：撤回不是逆操作”。

| 章 | 稳定文件 | 本次采用来源 | 归档的独立版本 |
|---:|---|---|---|
| 10 | `Part_02_选择的本性/10_不可逆性_撤回不是回到原点.md` | `Versioned_Drafts/Part_02_选择的本性/10_不可逆性_撤回不是逆操作_v14_review_polish_pass.md` | v8, v9, v10, v11, v12, v13, v14 |

同步清理：

- 第 9 章 `v5s`–`v5v` 独立版本曾由远端合并重新出现在正文目录；本次确认其与 `Versioned_Drafts/Part_02_选择的本性/` 中的归档文件一致后，从正文目录移除。
- 第 10 章当前基准为 `draft_v14_review_polish_pass`；后续第 11–13 章应以第 7–10 章当前基准链为前提推进。

## 2026-05-11 第十一章版本收束

本次将第 11 章最新版回写到稳定章节文件名。独立版本草稿已在 `Versioned_Drafts/Part_02_选择的本性/` 中保留。

| 章 | 稳定文件 | 本次采用来源 | 归档的独立版本 |
|---:|---|---|---|
| 11 | `Part_02_选择的本性/11_本体论摩擦_为什么现实不会免费成形.md` | `Versioned_Drafts/Part_02_选择的本性/11_本体论摩擦_为什么现实不会免费成形_v12_philosophical_synthesis_pass.md` | v4, v5, v6, v7, v8, v9, v10, v11, v12 |

同步说明：

- 第 11 章当前基准为 `draft_v12_philosophical_synthesis_pass`。
- 远端同时带入了第 12 章 `v5_alignment_hardening_pass` 归档稿；本次不提前回写第 12 章稳定文件，留待第 12 章完成确认后收束。

## 2026-05-12 第十二、十三章版本收束

本次将第 12、13 章最新版回写到稳定章节文件名。独立版本草稿保留在 `Versioned_Drafts/Part_02_选择的本性/`，正文目录继续只保留稳定入口。

| 章 | 稳定文件 | 本次采用来源 | 归档的独立版本 |
|---:|---|---|---|
| 12 | `Part_02_选择的本性/12_可支付性_为什么路径越走越像路.md` | `Versioned_Drafts/Part_02_选择的本性/12_可支付性_为什么路径越走越像路_v16_final_prose_pass.md` | v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16 |
| 13 | `Part_02_选择的本性/13_三判据_可延续_可协调_可再选择.md` | `Versioned_Drafts/Part_02_选择的本性/13_三判据_可延续_可协调_可再选择_v8_final_prose_tension_pass.md` | v5, v6, v7, v8 |

同步说明：

- 第 12 章当前基准为 `draft_v16_final_prose_pass`。
- 第 13 章当前基准为 `draft_v8_final_prose_tension_pass`。
- 至此卷二第 7–13 章均已收束到稳定文件名；下一步进入卷二整体一致性 pass。

## 2026-05-12 BOOK 主稿路径同步与卷二冻结

本次对 `Part_01_从存在到成为/`、`Part_02_选择的本性/`、`Part_03_从选择到主体与价值/` 做主稿路径审计。审计结果：三个 `Part_*` 主目录当前只保留稳定章节文件名，没有 `*_vN*.md` 版本副本残留；无需移动文件。已有过程稿继续保留在 `Versioned_Drafts/`，其中卷二过程稿集中在 `Versioned_Drafts/Part_02_选择的本性/`。

同步动作：

- 所有当前主稿 frontmatter 增加 `maintext_status: stable_candidate`。
- 保留每章原 `status`，不把来源版本号抹成统一标签。
- 第 8、9、11 章稳定主稿已按最新冻结候选同步；第 7、10、12、13 章未改正文内容，仅补主稿标记。

卷二冻结矩阵：

| 章 | 稳定文件 | 当前主稿 status |
|---:|---|---|
| 7 | `Part_02_选择的本性/07_地形如何反过来选择人.md` | `draft_v18_final_literary_philosophical_polish` |
| 8 | `Part_02_选择的本性/08_选择算子_从可成为性到显现.md` | `draft_v5r_terrain_embodiment_focus_pass` |
| 9 | `Part_02_选择的本性/09_排除_选择的阴影.md` | `draft_v5w_shadow_return_alignment_pass` |
| 10 | `Part_02_选择的本性/10_不可逆性_撤回不是回到原点.md` | `draft_v14_review_polish_pass` |
| 11 | `Part_02_选择的本性/11_本体论摩擦_为什么现实不会免费成形.md` | `draft_v13_bridge_boundary_shadow_alignment_pass` |
| 12 | `Part_02_选择的本性/12_可支付性_为什么路径越走越像路.md` | `draft_v16_final_prose_pass` |
| 13 | `Part_02_选择的本性/13_三判据_可延续_可协调_可再选择.md` | `draft_v8_final_prose_tension_pass` |

机制链确认：

```text
07 地形进入选择之前
08 选择算子在地形中压出显现
09 显现制造阴影，阴影回流改变地形
10 前景与阴影共同造成不可逆
11 不可逆使现实不能免费成形
12 摩擦必须支付，支付沉积为路径
13 路径健康需要三判据，主体与价值被推出
```

## 2026-05-14 卷二整体一致性 weld pass

本次对卷二第 7–13 章稳定主稿执行整体一致性焊接修订。旧稳定主稿已归档至 `Versioned_Drafts/Part_02_选择的本性/`，主阅读入口仍为 `Part_02_选择的本性/` 下稳定文件名。

本次不做整卷重写，不新增正文目录版本副本。修订重点为：

- 增加卷二总导语；
- 补强 7→8、8→9、9→10、10→11、11→12、12→13、13→卷三桥句；
- 统一“地形、显现、阴影、不可逆、本体论摩擦、可支付性、路径、三判据”的术语分工；
- 压缩重复跨尺度材料；
- 明确第 13 章推出卷三主体与价值的问题；
- 新增 `13b_卷二小结_选择如何在地形中发生.md` 作为卷二命题组 / 短桥；
- 将卷二状态确认为 `stable_candidate / post_part02_consistency_weld`。

远端 rebase 后同步到稳定主稿的最新候选状态：

| 章 | 当前主稿 status |
|---:|---|
| 7 | `draft_v18_final_literary_philosophical_polish` |
| 8 | `draft_v5r_terrain_embodiment_focus_pass` |
| 9 | `draft_v6_philosophical_depth_pass` |
| 10 | `draft_v15_third_tier_final` |
| 11 | `draft_v13_literary_final_pass` |
| 12 | `draft_v17_final_literary_polish` |
| 13 | `draft_v9_necessity_hardening` |

归档动作：

- `07_地形如何反过来选择人_pre_consistency_weld_2026-05-14.md`
- `08_选择算子_从可成为性到显现_pre_consistency_weld_2026-05-14.md`
- `09_排除_选择的阴影_pre_consistency_weld_2026-05-14.md`
- `10_不可逆性_撤回不是回到原点_pre_consistency_weld_2026-05-14.md`
- `11_本体论摩擦_为什么现实不会免费成形_pre_consistency_weld_2026-05-14.md`
- `12_可支付性_为什么路径越走越像路_pre_consistency_weld_2026-05-14.md`
- `13_三判据_可延续_可协调_可再选择_pre_consistency_weld_2026-05-14.md`
- `07_地形如何反过来选择人_v17_completion_pass.md` 已从 `Part_02_选择的本性/` 移入 `Versioned_Drafts/Part_02_选择的本性/`，避免过程版本长期留在正文主目录。
- rebase 后进入主目录的第 7–13 章过程候选稿已同步进稳定主稿，并移入 `Versioned_Drafts/Part_02_选择的本性/`；其中第 7/8 章因已有同名归档且内容不同，追加 `_remote_main_2026-05-14` 后缀保留。

当前卷二机制链：

```text
L2 / 地形作为过去选择沉积后的摩擦分配
→ 选择不是从选项出现后才开始
→ 可成为性在地形中被压成显现
→ 显现必然制造排除与阴影
→ 前景与阴影共同写回，造成不可逆
→ 不可逆使现实不能免费改变
→ 本体论摩擦要求支付
→ 反复支付沉积为路径
→ 路径健康需要三判据
→ 主体与价值被推出
```
