---
id: SRT-BOOK-CH14-V6-MAINTEXT-CANDIDATE-MERGE-NOTE-2026-05-14
type: book_project_update_queue_note
status: pending_maintext_sync
scope: 01_source_intuition_book
chapter: 14
created: 2026-05-14
source_candidate:
  - 01_Source_Intuition/BOOK/Versioned_Drafts/Part_03_从选择到主体与价值/14_在乎是什么_v6_third_tier_maintext_candidate.md
current_stable_file:
  - 01_Source_Intuition/BOOK/Part_03_从选择到主体与价值/14_在乎是什么.md
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
---

# 第 14 章 v6 主稿候选合并说明

本次已新增第 14 章第三类主稿候选：

`01_Source_Intuition/BOOK/Versioned_Drafts/Part_03_从选择到主体与价值/14_在乎是什么_v6_third_tier_maintext_candidate.md`

## 1. 处理结论

建议将该 v6 候选作为第 14 章新的稳定主稿来源，并在本地或下一次可靠 blob SHA 可用时回写到：

`01_Source_Intuition/BOOK/Part_03_从选择到主体与价值/14_在乎是什么.md`

原因：当前稳定主稿仍为 `draft_v4 / stable_candidate`，而卷二第 7–13 章整体一致性 weld pass 与 13b 卷二小结已经完成；第 14 章应从卷二最新链条进入，而不是继续停留在 v4 的横向说明结构。

## 2. v6 相对 v4 / v5 的主要变化

- 以 13b 的卷二结尾为入口：谁在承接后果？谁能让阴影回流？谁还能重新打开未来？
- 将章节主梁压成：后果回流 → 存在回流 → 主体性显形。
- 保留并压缩两组操作性对照：
  - 看起来在乎，但后果不回流；
  - 不想承认，但已经被改写。
- 明确“改写选择结构”的三种直觉层标志：
  - 注意分配被重组；
  - 未来选项的可见性改变；
  - 身体、情绪和承重状态成为新的地形。
- 增加强反对者段落：这只是更复杂的心理学吗？
- 保留 d-value 语义入口，但不进入公式、刻度或规范定义。
- 章末用四条命题推出第 15 章“价值不是偏好”。

## 3. 建议同步更新项

当 v6 被正式回写到稳定文件名后，同步更新以下文件：

1. `01_Source_Intuition/BOOK/BOOK_CURRENT_STATUS.md`
   - 第 14 章状态改为：`stable_candidate / draft_v6_third_tier_maintext_candidate`。
   - 下一步改为：与第 15、16 章做卷三 14–16 一致性 pass。

2. `01_Source_Intuition/BOOK/Outline_Parts/03_卷三_从选择到主体与价值.md`
   - 第 14 章状态改为：当前主稿候选来自 v6。
   - 本章任务改为：从卷二三判据之后的承受位置进入主体性入口。

3. `01_Source_Intuition/BOOK/BOOK_VERSION_LOG.md`
   - 追加 `2026-05-14 第十四章第三类主稿候选` 条目。
   - 记录 v6 候选来源：v4 稳定稿、两个 v5 候选、13b 卷二小结、第三类改写指南。

4. 稳定文件 frontmatter 建议：

```yaml
status: draft_v6_third_tier_maintext_candidate
maintext_status: stable_candidate
consolidation_pass: ch14_third_tier_maintext_sync_2026_05_14
based_on:
  - 01_Source_Intuition/BOOK/Part_03_从选择到主体与价值/14_在乎是什么.md
  - 01_Source_Intuition/BOOK/Versioned_Drafts/Part_03_从选择到主体与价值/14_在乎是什么_v5_third_tier_argument.md
  - 01_Source_Intuition/BOOK/Versioned_Drafts/Part_03_从选择到主体与价值/14_在乎是什么_v5_third_tier_subject_entry.md
  - 01_Source_Intuition/BOOK/Part_02_选择的本性/13b_卷二小结_选择如何在地形中发生.md
```

## 4. 建议后续工作

- 先将 v6 回写为第 14 章稳定主稿。
- 再推进第 15 章第三类 pass，重点收紧与第 14 章的边界：第 14 章负责“在乎 / 后果回流 / 主体性入口”，第 15 章负责“价值 / 假关切 / 不可替代承担”。
- 第 16 章随后接 d-value，只做书稿层语义刻度，不提前引入规范公式。
