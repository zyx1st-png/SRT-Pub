---
id: SRT-WORKLINE-AUTHOR-PRIORITIES-20260805
title: "SRT 工作线作者排期裁决（2026-08-05）"
type: author_decision_record
status: active
record_stage: priorities_fixed_2026-08-05
canonical: false
layer: meta
epistemic_layer: os
claim_mode: governance
date: 2026-08-05
supersedes_scheduling_only:
  - STATUS.md@2026-08-04
  - Operations/_SRT_CHOICE_TRACE_WRITEBACK_PLAN_2026-07-10.md@plan_v5_t-e_bridge_built_2026-08-04
related_issue:
  - https://github.com/zyx1st-png/SRT-Pub/issues/740
---

# SRT 工作线作者排期裁决（2026-08-05）

## 0. 文件角色

本文件记录作者对当前理论、书稿和论文工作线的**排期与施工顺序裁决**。

它只覆盖：

- 现在先做什么；
- 哪些工作暂缓；
- 哪些状态需要在仓库中纠正；
- 哪些旧 Issue / PR 应关闭、停驻或合并。

它不修改：

- canonical 定义、符号、方程或 claim level；
- 已冻结的 forcing–CH 策略或协议；
- SEA 五门协议与编码手册；
- 书稿正文；
- 已投稿论文的科学内容。

“暂缓”不等于失败、撤回理论主张或永久取消。工作线重新启动时仍需读取当时最新 `main`。

## 1. Forcing–CH 控制档案

### 裁决

**暂缓进入控制档案 Part II 和控制案例后续程序。**

原因：论文所需的硬性数学史书籍、原始材料和同期记录仍在收集整理，当前档案深度不足以诚实签署 `CONTROL_ARCHIVE_ADEQUACY_CERTIFICATE_v0_1` Part II。

### 保持不变

- `strategy_note_v0_7` 继续 frozen；
- `METHOD_INDIVIDUATION_PROTOCOL_v0_1` 与 `CONTROL_CASE_SELECTION_PROTOCOL_v0_1` 不修改；
- `EVD-D05-0001` 保持 **qualified**；
- `EVD-D04-0002` 保持 **unresolved**；
- Part II 未签署前，控制案例枚举、评分、排名、选择和 individuation 仍被阻塞。

### 当前允许

- 继续收集和整理书籍、论文、评论、综述与书评；
- 记录来源、覆盖范围与尚未取得的材料；
- 不把材料收集偷换为候选筛选。

## 2. SEA 独立编码可靠性试验

### 裁决

**稍后处理。**

- SEA 协议、制度案例和编码手册保留；
- `SRT_SEA_CASE_CODING_MANUAL_v0_1` 继续保持 pilot-ready；
- 不立即招募编码者、制作正式测试包或启动一致性统计；
- PR #738 已按 deferred 关闭，不解释为方法被否定。

重新启动前需复核：材料融合完成度、私有证据包可用性、脱敏要求和独立编码者条件。

## 3. Frontiers 已接受稿的转投

稿件：*A Translational Cross-Modal Control-Cost Framework for Executive Breakdown*，原稿号 `1837760`。

### 当前事实

- 稿件已经接受并进入接受后流程；
- 由于 APC 费用过高，作者准备终止原出版路径并转投其他期刊；
- 当前不得写作 `published`、`in press` 或已取得 DOI，除非另有公开记录被核验。

### 硬顺序

1. 核验 accepted / production / proof / DOI / online publication 的真实状态；
2. 取得原期刊明确的撤回或终止出版确认；
3. 确认无版权和重复投稿冲突；
4. 再选择并提交新期刊。

该流程由 Issue #740 管理。费用原因不应被写成学术拒稿或对审稿质量的评价。

## 4. 状态面收口

### 裁决

立即更新 `STATUS.md`，纠正以下过期口径：

- T-B / T-D / T-E 不再是“待建立”的桥；首轮 bridge、五域联合压力测试和后续 SEA 操作化已经完成；
- Frontiers 不再处于 major revision；当前为“已接受但因 APC 过高准备终止原出版路径并转投”；
- Costly Selective Closure / Adaptive Behavior 不再是“重投准备”；已经投稿，但尚未进入外部评审；
- forcing–CH 控制档案因硬性历史材料尚未齐备而暂缓；
- SEA reliability pilot 暂缓；
- 书稿与 history-dependent reachability 的统一优化均等待未融合材料收口。

## 5. 《从存在到秩序》统一优化

### 裁决

**等待所有此前未融合材料完成融合后，再进行统一优化。**

当前不启动：

- Q15、Q21、Q18/耗散接口的统一正文回写；
- #657 的跨尺度“退让—阴影—选择代理层”正文施工；
- #474 的可视化骨架落地；
- 全书统一术语、结构与专业读者 pass。

材料可以继续通过 Pipeline 1 进入 SourceCard、Patch、Hook、Material Log 和索引，但不得因单篇材料到来立即触发全书局部重写。

旧 Part / 52 章路线 Issue #152、#153、#155 已按 superseded 关闭。未来统一优化必须从 `BOOK_CURRENT_STATUS.md`、`BOOK_ACTIVE_MANIFEST.json` 和 `Drafts_26Q/` 当前主稿重新立项。

## 6. History-dependent reachability

### 裁决

与书稿相同：**等待此前未融合材料全部收口后，再进行统一优化或新一轮投稿包装调整。**

当前不因 SEA、意识材料、耗散材料或其他新卡片逐项改写稿件。已有实验、统计、图表和 assembly 记录保持不动；未来统一 pass 再决定哪些材料真正进入 related work、limitations、discussion 或方法边界。

本裁决不声称该稿件已经投稿，也不改变其已有科学结论。

## 7. Costly Selective Closure / Adaptive Behavior

### 当前事实

- 稿件已经投稿；
- 当前尚未进入外部评审；
- 不再写作“重投准备”；
- 当前动作是等待编辑处理，并保持稿件、匿名补充包和实验结果稳定。

除非编辑或审稿流程提出明确要求，不继续增加实验或无目标扩张 framing。

## 8. 本轮 PR / Issue 处置

### 已合并

- #730 forcing 多表征与方法族同一性审计；
- #739（替代自动关闭的 #733）countable-standard-model premise typing；
- #735 salience / lateral-inhibition source-intuition genealogy；
- #734 AIGOAL01 LLM goal-selection 材料；
- #728 consciousness and cognition material cards；
- #710 重新编号为 NEURAL22 的 astrocyte hierarchy bridge。

### 已关闭或延期

- #738 SEA reliability pilot：deferred 关闭；
- #152、#153、#155：旧书稿路线，superseded / not planned；
- #657、#474：保留但延期至材料融合完成；
- #740：Frontiers 撤回／终止与转投流程的当前执行卡。

## 9. 当前优先顺序

1. 继续完成此前未融合材料的 Pipeline 1 收口，并保持台账、索引与 registry 一致；
2. 完成 Frontiers 原出版路径的合规终止和转投准备（#740）；
3. 维护已投稿的 Adaptive Behavior 稿件，等待编辑处理；
4. 继续收集 forcing–CH 所需硬性历史书籍和同期记录，但不提前筛选控制案例；
5. 材料收口后，再分别启动书稿和 history-dependent reachability 的统一优化；
6. SEA reliability pilot 在上述工作减压后重新评估。

## 10. 防误用

- 排期优先级不改变 claim level；
- “已接受但因费用转投”不等于已出版，也不等于学术拒稿；
- “已投稿、未外审”不等于 under review；
- 材料融合不自动授权正文、canonical 或论文改写；
- forcing 书籍收集不等于候选控制案例枚举；
- SEA pilot 暂缓不等于 SEA 方法得到验证或被否定；
- 任何重启都必须从当时最新 `main` 和当前状态入口重新读取。
