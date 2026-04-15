---
id: SRT-QUALITY-SCORECARD
type: framework
tags: [Quality, Audit, Governance]
status: rolling_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
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
# from workspace root
./scripts/run_srt_checks.sh

# from SRT/
uv run python ../scripts/srt_quality_metrics.py
uv run python ../scripts/srt_explainability_audit.py
```
- Frontmatter lint
- Link check
- Symbol governance
- 质量指标自动快照（当前输出根目录 `_SRT_QUALITY_METRICS.md`）
- 解释链审计快照（当前输出根目录 `_SRT_EXPLAINABILITY_AUDIT.md`）

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

- Frontmatter Coverage：**100%**（91/91，来源：`Governance/_SRT_QUALITY_METRICS.md`）
- Broken Link Rate：**0**（`run_srt_checks.sh` 当前通过）
- Symbol Governance：**PASS**
- Terminology Governance Coverage：**100%**（核心术语集 4/4）
- Explainability Completeness：**100.0%**（71篇候选，5段结构平均覆盖；见 `Governance/_SRT_EXPLAINABILITY_AUDIT.md`）
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

## Week 2026-W11
- Frontmatter Coverage: **99.2%** (Target >=95%)
- Broken Link Rate: **0** (Target =0)
- Symbol Governance: **PASS**
- Terminology Governance Coverage: **100.0%**
- Explainability Completeness: **57.0%**（raw auto；治理可比口径仍约 **83.5%**）
- Boundary Header Coverage: **68.2%**（raw auto；治理可比口径仍约 **98.5%**）

### Key Findings
- 已补齐 `Operations/_SRT_DAILY_REVIEW_LOG.md` 与 `memory/2026-03-12.md` 的 frontmatter，frontmatter lint 恢复通过。
- 已修复 `Governance/_SRT_CHANGELOG_2026.md` 的相对链接漂移；workspace 根目录 `./scripts/run_srt_checks.sh` 已全量通过。
- 当前自动 explainability / boundary 审计会把 split / compact / governance / operations 文档一并计入，raw 指标明显失真，但治理可比快照仍维持在高位。

### Regressions
- Pipeline 4 文档说明在结构改造后出现脚本路径与产物位置漂移。
- 自动 explainability / boundary 审计的候选范围扩大过头，导致理论质量信号被非理论文档稀释。

### Actions Next Week
- 统一 Pipeline 4 的执行根目录口径，并让 `run_srt_checks.sh` 摆脱对执行目录的隐含依赖。
- 收紧 explainability / boundary 审计候选范围，排除 split / compact / governance / operations 等非主理论层文档。
- 推进 G1 最小数据包与 `d-value canonical` 引用批处理，优先把 `Eq-Select-Thermo` 往可检验 Partial+ 推动。
