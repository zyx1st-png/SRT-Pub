---
id: SRT-SIGNAL-PIPELINE
type: framework
tags: [Signals, Intake, Curation]
status: active_v2
dependency: [SRT-EXECUTION-PLAN, SRT-QUALITY-SCORECARD, SRT-DAILY-REVIEW-PIPELINE]
---

# SRT 情报采集与融合流水线（Pipeline 3）

> **变更（2026-03-02）**：节奏从"每 3 天"升级为**每日**，并通过 HEARTBEAT 自动触发。

---

## 触发方式

**自动触发（HEARTBEAT）**：
- 检查 `memory/heartbeat-state.json` 中 `pipeline3_last`
- 若距上次采集 ≥ 22 小时 → 自动执行本次采集
- 防重复：若当日 0:00-23:59 内已执行 → 跳过

**手动触发**：
- 用户发送 `信号采集` → 立即执行（忽略时间间隔检查）

---

## 来源范围

### Scholar（每日）
- arXiv 关键词：`consciousness`, `free energy principle`, `selection operator`, `ontological friction`, `d-value attention`, `structural resonance`
- Semantic Scholar：跟踪已引用 SRT 相关论文的新引文

### Reddit（每日）
- `r/neuroscience`、`r/philosophy`、`r/consciousness`、`r/cogsci`
- 筛选条件：Hot 帖 + 关键词命中（意识、自由能、决策理论、心身问题）

### Twitter/X（每日）
- 关键词：`#consciousness`、`#freeenergy`、`#IIT`、`#predictivecoding`
- 目标账号：Karl Friston、Anil Seth、Giulio Tononi 等意识研究者

---

## 审核门（6 项，与 Pipeline 1 共用）

每条信号必须通过以下 6 项审核：
1. **相关性**：与 SRT 核心命题（L₀/L₁/L₂、Ĝ_θ、d、Ψ_f）实质相关
2. **增量性**：非已有内容的重复
3. **证据等级**：peer-reviewed / preprint / editorial / secondary（标注）
4. **可对齐性**：能映射到 SRT 框架（d 区间、能流态、Ψ_f 状态）
5. **风险**：是否存在误导/过度外推/伪背书风险
6. **落点清晰**：能明确写入哪个文件的哪个节位

**审核结论**：
- **A**：直接融入（修改 SRT 目标文档 → git commit）
- **B**：延后观察（记录到 `_SRT_SIGNAL_LOG.md`，3 个月后重评）
- **C**：不融入（记录原因）

---

## 输出格式

每条信号记录写入 `_SRT_SIGNAL_LOG.md`：

```
| 时间 | 来源 | 主题（50字内） | 证据等级 | 审核结论 | 落点 | 是否已融入 |
```

若审核结论为 A，同时追加 `_SRT_MATERIAL_LOG.md` 台账记录。

---

## 状态更新

采集完成后更新 `memory/heartbeat-state.json`：
```json
{ "pipeline3_last": <当前 Unix 时间戳> }
```

---

## 约束（不变）
- 不走 `diff.md`（直接审核通过后修改正文）
- 采集和审核分开：先批量采集，再批量审核，再按 A 类逐一融入
- 不自动发布任何内容到外部平台
