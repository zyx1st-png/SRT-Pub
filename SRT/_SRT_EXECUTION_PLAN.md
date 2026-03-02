---
id: SRT-EXECUTION-PLAN
type: framework
tags: [Operations, Workflow, Governance]
status: active_v2
dependency: [SRT-INDEX, SRT-QUALITY-SCORECARD, SRT-OPERATIONS-SCHEDULE]
---

# SRT 执行总计划（Active）

## 关键变更记录
- **2026-02-28**：Pipeline 1/3 不再走 `diff.md`，改为"先审核→直接修改正文"
- **2026-03-02**：新增 Pipeline 6（每日内审），Pipeline 3 升级为每日，Pipeline 5 升级为双路线，添加材料台账 `_SRT_MATERIAL_LOG.md`

---

## 六条流水线

| 编号 | 名称 | 节奏 | 触发 | 文档 |
|-----|------|------|------|------|
| Pipeline 1 | 材料融合（直接入正文） | 随时，用户提交后立即执行 | 用户指令 | 本文件 |
| Pipeline 2 | 论文孵化 | 每周候选 + 每两周投稿评估 | HEARTBEAT / `论文候选` | `_SRT_PAPER_PIPELINE.md` |
| Pipeline 3 | 网络信号采集 | **每日** | HEARTBEAT / `信号采集` | `_SRT_SIGNAL_PIPELINE.md` |
| Pipeline 4 | 文档治理 + 理论方向评审 | 每周 | HEARTBEAT 提醒 / `周评` | `_SRT_GOVERNANCE_PIPELINE.md` |
| Pipeline 5 | 双路线媒体选题 | 每日（大众+精英各 1 条） | Cron 08:00 / `选题` | `_SRT_MEDIA_PIPELINE.md` |
| Pipeline 6 | **每日自动内部审查（新）** | 每日 | HEARTBEAT / `内审` | `_SRT_DAILY_REVIEW_PIPELINE.md` |

配套运行节奏：`_SRT_OPERATIONS_SCHEDULE.md`

---

## Pipeline 1：材料融合（详细规范）

### 接受的输入格式

1. **文本粘贴**：用户直接在对话中粘贴内容
   - 触发词：`材料 <粘贴文本>`
2. **文件附件**：用户上传 PDF / MD / TXT
   - 触发词：上传后发送 `材料 <文件描述>`
3. **URL**：用户提供链接，agent 使用 web_fetch 抓取
   - 触发词：`材料 <URL>`
   - 失败处理：web_fetch 失败 → 降级为 DOI 元数据 + 可访问来源

### 审核门（6 项，必须通过）

每条材料先做 6 项审核，输出 A/B/C 结论：

1. **相关性**（与 SRT 核心命题实质相关）
2. **增量性**（非重复）
3. **证据级别**（peer-reviewed / preprint / commentary，标注）
4. **可对齐性**（d, Ψ_f, Ĝ_θ, L₀/L₁/L₂）
5. **风险**（误导/过度外推/伪背书）
6. **落点清晰**（写入文件和节位明确）

审核结论：
- **A**：直接融入
- **B**：延后观察（3 个月后重评）
- **C**：不融入（记录原因）

### 台账记录（每次审查必须执行）

将审查结果追加到 `_SRT_MATERIAL_LOG.md`：

```
| YYYY-MM-DD | 来源标题/URL | 证据等级 | 审核结论(A/B/C) | 落点（文件+节位） | 融入状态 | 备注 |
```

---

## 通过后执行（A 类）

1. 直接修改 SRT 目标文档（非 diff.md）
2. 补引用与证据等级标注
3. 保留边界声明
4. 运行：
   - `./scripts/run_srt_checks.sh`
   - `python3 scripts/srt_quality_metrics.py`
5. git commit（格式：`docs(material): integrate <来源关键词> into <域名>`）
6. 写入 `_SRT_MATERIAL_LOG.md` 台账

---

## 通用约束

- `diff.md` 仅在需要"补丁提案模式"时使用（风险材料缓冲/审稿前评审）
- Core_Law 目录仅做谨慎结构优化，避免语义漂移
- 重大语义变更需单独 commit + release 标注
- 每条材料处理完毕必须有台账记录（`_SRT_MATERIAL_LOG.md`）
