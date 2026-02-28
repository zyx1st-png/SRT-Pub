---
id: SRT-SIGNAL-PIPELINE
type: framework
tags: [Signals, Intake, Curation]
status: active_v1
dependency: [_SRT_EXECUTION_PLAN, _SRT_QUALITY_SCORECARD]
---

# SRT 情报采集与融合流水线（Pipeline 3）

## 来源范围
- Reddit
- Twitter/X
- Scholar（Google Scholar / arXiv / Semantic Scholar）

## 规则（按用户指令）
- 计划 3 不走 `diff.md`
- 先审核必要性（A/B/C）
- A 类才直接修改正文文档

## 审核门
1. 相关性
2. 增量性
3. 证据等级
4. 可对齐性
5. 风险
6. 落点清晰

## 日志
- 新建：`SRT/_SRT_SIGNAL_LOG.md`
- 字段：时间、来源、主题、审核结论、落点、是否已融入
