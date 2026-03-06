---
id: SRT-QUALITY-SCORECARD
type: framework
tags: [Quality, Audit, Governance]
status: rolling_v1
dependency: [_SRT_DOC_ENGINEERING_GUIDE, _SRT_FRONTMATTER_AUDIT, SRT-GLOSSARY]
---

# SRT Quality Scorecard

> 用途：每周更新一次，用于追踪 SRT 文档工程质量与理论治理健康度。  
> 周期：Weekly（建议每周末）。

---

## 1) 指标定义

1. **元数据覆盖率（Frontmatter Coverage）**
   - 定义：含完整 frontmatter 的 `.md` 文件占比。
   - 目标：`>= 95%`

2. **断链率（Broken Link Rate）**
   - 定义：内部链接中失效链接占比。
   - 目标：`= 0`

3. **符号治理合规（Symbol Governance Pass）**
   - 定义：关键 canonical 符号检查通过与否。
   - 目标：`PASS`

4. **术语治理覆盖（Terminology Governance Coverage）**
   - 定义：高频术语是否具备 `Canonical Scope / Confusable With / Lineage`。
   - 目标：核心术语集 `100%`

5. **解释链完整率（Explainability Completeness）**
   - 定义：新建/改造核心文档中，五段结构（定义/形式化/机制/证伪/边界）覆盖率。
   - 目标：`>= 90%`

6. **边界声明覆盖率（Boundary Header Coverage）**
   - 定义：关键理论扩展文档包含 `## 【理论边界/防误用声明】` 的比例。
   - 目标：`>= 90%`

---

## 2) 采集方式

### 自动采集
```bash
./scripts/run_srt_checks.sh
python3 scripts/srt_quality_metrics.py
python3 scripts/srt_explainability_audit.py
```
- Frontmatter lint
- Link check
- Symbol governance
- 质量指标自动快照（输出 `SRT/_SRT_QUALITY_METRICS.md`）
- 解释链审计快照（输出 `SRT/_SRT_EXPLAINABILITY_AUDIT.md`）

---

## 3) 周报模板

```markdown
## Week <YYYY-WW>
- Frontmatter Coverage: <x%> (Target >=95%)
- Broken Link Rate: <x%> (Target =0)
- Symbol Governance: <PASS/FAIL>
- Terminology Governance Coverage: <x%>
- Explainability Completeness: <x%>
- Boundary Header Coverage: <x%>

### Key Findings
- ...

### Regressions
- ...

### Actions Next Week
- ...
```

---

## 4) 当前基线（2026-02-28）

- Frontmatter Coverage：**100%**（91/91，来源：`_SRT_QUALITY_METRICS.md`）
- Broken Link Rate：**0**（`run_srt_checks.sh` 当前通过）
- Symbol Governance：**PASS**
- Terminology Governance Coverage：**100%**（核心术语集 4/4）
- Explainability Completeness：**100.0%**（71篇候选，5段结构平均覆盖；见 `_SRT_EXPLAINABILITY_AUDIT.md`）
- Boundary Header Coverage：**100.0%**（64/64，自动粗筛口径）

---

## Week 2026-W10
- Frontmatter Coverage: **84.4%** (Target >=95%)
- Broken Link Rate: **N/A**（本轮被 frontmatter lint 噪声提前中断）
- Symbol Governance: **N/A**（同上）
- Terminology Governance Coverage: **100.0%**
- Explainability Completeness: **42.8%**
- Boundary Header Coverage: **90.1%**

### Key Findings
- 本周完成大量外部理论回写，边界声明覆盖仍维持在 90% 以上。
- 主映射矩阵仍保留 3 条高优先级 Gap（Eq-Select-Thermo / Eq-LDP-01 / Eq-LDP-02）。

### Regressions
- 质量脚本扫描范围包含 `.venv/`、`papers/` 与若干非治理文档，拉低 frontmatter 覆盖率并阻断全量检查。
- Explainability 审计基数扩大后，5-block 完整度显著下降（3/79）。

### Actions Next Week
- 将 `run_srt_checks.sh` 与审计脚本改为仅扫描 SRT 主治理范围（排除 `.venv/`、第三方许可证、临时论文包）。
- 对低分高价值文档执行分层补块（先补 definition/formalization/falsification）。
- 先推进 G1 最小验证，把主矩阵 1 条 Gap 转为可检验 Partial+。
