---
id: SRT-RELEASE-NOTE-TEMPLATE
type: framework
tags: [Release, Template, Governance]
status: rolling_v1
dependency: [_SRT_QUALITY_SCORECARD, _SRT_INDEX]
---

# SRT Release Note Template

> 频率：每两周一次（或关键重构后立即发布）。

## Release Meta
- Version: `SRT-YYYY-MM-<seq>`
- Date: `YYYY-MM-DD`
- Scope: `Docs / Theory / Experiment / Tooling`
- Maintainer: `<name>`

---

## 1) Highlights
- ...
- ...

## 2) Architecture & Documentation Changes
- 新增文件：
  - `...`
- 重构文件：
  - `...`
- 清理/迁移：
  - `...`

## 3) Theory Changes
- 新增/修订公理：...
- 新增/修订方程：...
- 术语治理更新：...

## 4) Experiment & Falsification Updates
- Eq ↔ Hypothesis 映射变化：...
- 新增实验路径：...
- Gap 状态变化：...

## 5) Pipeline & Tooling Updates
- `diff.md` 流水线更新：...
- 脚本与自动化检查：...
- 运行命令：`./scripts/run_srt_checks.sh`

## 6) Quality Snapshot
- Frontmatter Coverage: ...
- Broken Link Rate: ...
- Symbol Governance: ...
- Terminology Governance Coverage: ...
- Boundary Header Coverage: ...

## 7) Breaking / Migration Notes
- ...

## 8) Next Cycle Plan
- P0/P1/P2/P3 的下一步：...

---

## 【理论边界/防误用声明】
1. Release Note 记录的是文档与工程状态，不代表理论主张自动成立。  
2. 任何新命题仍需通过证据等级与证伪流程检验。  
3. 对外引用时应明确版本号与证据级别，避免跨版本误读。
