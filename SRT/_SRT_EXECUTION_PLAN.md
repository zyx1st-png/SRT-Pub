---
id: SRT-EXECUTION-PLAN
type: framework
tags: [Operations, Workflow, Governance]
status: active_v1
dependency: [_SRT_INDEX, _SRT_QUALITY_SCORECARD]
---

# SRT 执行总计划（Active）

## 关键变更（2026-02-28）
- **计划 1（材料融合）与计划 3（定时情报采集）不再走 `diff.md`。**
- 新流程：**先审核必要性 → 通过后直接修改 SRT 正文文档**。

---

## 五条流水线

1. 材料融合线（直接入正文）
2. 论文孵化线（可投稿）
   - 见：`_SRT_PAPER_PIPELINE.md`
3. 定时情报采集线（先审后入正文）
   - 见：`_SRT_SIGNAL_PIPELINE.md`
4. 文档治理线（质量与减冗）
   - 见：`_SRT_GOVERNANCE_PIPELINE.md`
5. 自媒体策划线（仅提供选题/方向/原因/内部关联整理，不直接成文）
   - 见：`_SRT_MEDIA_PIPELINE.md`

配套运行节奏：`_SRT_OPERATIONS_SCHEDULE.md`

---

## 计划 1/3 的审核门（必须通过）

每条材料先做 6 项审核：
1. 相关性（与 SRT 核心命题实质相关）
2. 增量性（非重复）
3. 证据级别（peer-reviewed / preprint / commentary）
4. 可对齐性（d, Ψ_f, Ĝθ, L_0/L_1/L_2）
5. 风险（误导/过度外推/伪背书）
6. 落点清晰（写入文件和节位明确）

审核结论：
- A 直接融入
- B 延后观察
- C 不融入

---

## 通过后执行

- 直接改 SRT 目标文档（非 diff.md）
- 补引用与证据等级
- 保留边界声明
- 运行：
  - `./scripts/run_srt_checks.sh`
  - `python3 scripts/srt_quality_metrics.py`
- 每轮 git commit
