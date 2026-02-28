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
```
- Frontmatter lint
- Link check
- Symbol governance
- 质量指标自动快照（输出 `SRT/_SRT_QUALITY_METRICS.md`）

### 半自动/人工抽样
- 解释链完整率：抽样检查本周新增/重构文档

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
- Explainability Completeness：**协议已发布（待按周抽样量化）**
- Boundary Header Coverage：**48.4%**（31/64，自动粗筛口径；持续提升中）

---

## 【理论边界/防误用声明】

1. Scorecard 是工程质量仪表，不是理论真值判定器。  
2. 指标高分不代表理论命题必然正确，仅代表文档结构更可审计。  
3. 对“证据等级”与“统计显著性”的判定，仍须回到具体实验与数据分析流程。
