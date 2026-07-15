---
id: SRT-TEMPLATE-STRUCTURE-EXTRACTION
type: template
tags: [Template, Structure, Extraction, Governance]
status: active_v1
layer: operations
epistemic_layer: workflow
claim_mode: prompt
canonical: false
date: 2026-07-15
usage: 三段式抽取，逐段留痕。红线以 Operations/README.md §Stop Rule + Governance/SRT_EDIT_PROTOCOL.md 为准。
---

# 结构接口抽取模板（三段式）

## 段 1 · Pre-audit（只读，不改文件）→ 存 `*_PreAudit_*.md`
- 目标文件/领域：
- frontmatter/章节/公式/阈值/claim level/导航链接 现状盘点：
- 候选抽取块 + 风险分级：
  | 块 | 风险（低=导航/表述；高=公式/阈值/subjecthood/collapse/常数/MWI/离散时间） | 是否进 adjudication |
  |---|---|---|
- 结论：哪些进段 2，哪些本段不动只标记。

## 段 2 · Adjudication（裁决，不改正文）→ 存 `*_Adjudication_*.md`
| 候选块 | A 抽 / B 缓 / C 不抽 | 最小可承重接口命题 | 主落点 | 备选落点 | 禁止落点 | claim level |
|---|---|---|---|---|---|---|
- companion↔canonical 关系确认（companion 永不升格）：

## 段 3 · Extraction record + Closure → 存 `*_Extraction_Record_*.md`（+ 领域收口时 `*_Closure_Report_*.md`）
- 只对段 2 判 A 的块执行最小定向抽取（配合 srt-safe-patch 纪律）。
- 抽了什么 / 留了什么：
- 导航/index/registry 链接更新：
- 自查脚本：
  - [ ] `scripts/governance_preflight.py`
  - [ ] `scripts/check_frontmatter.py`
  - [ ] `scripts/check_registry_consistency.py`
- broken link / 导航一致性：
- 是否需要 closure report：是/否

## 红线自查
- [ ] 有 pre-audit 才抽（无机会主义抽取）
- [ ] 未移动公式/阈值/高风险 claim（除非已有对应 adjudication）
- [ ] companion/annex/split/bridge 未升格 canonical
- [ ] 大文件最小编辑、未删未重排
- [ ] 未引入新理论
