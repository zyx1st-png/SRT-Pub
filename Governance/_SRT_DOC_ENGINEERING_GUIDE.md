---
id: SRT-DOC-ENGINEERING
type: framework
tags: [Documentation, Engineering, Standards]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [_SRT_MANIFEST, _SRT_SYMBOL_TABLE]
updated: 2026-06-05
---

# SRT Documentation Engineering Guide

## Scope
This guide defines how SRT docs are organized for:
- theoretical consistency (cross-domain invariants),
- tooling compatibility (linting, graphing, indexing),
- AI interaction reliability (stable parsing and retrieval).

## Canonical Metadata Contract
Every theory file should keep YAML frontmatter at the first line:

```yaml
---
id: SRT-<DOMAIN>-<KEY>
type: <theory|definition|axiom_set|equation|framework|experiment|architecture>
tags: [TagA, TagB, Hybrid]
layer: <meta|L0|L1|L2>
epistemic_layer: <os|bridge|lab>
claim_mode: <canonical|governance|navigation|translation|hypothesis|evidence|historical_record|manifesto>
status: axiomatic_hybrid_vN
dependency: [SRT-..., Core_Law/...]
---
```

Rules:
1. `id` is globally unique, uppercase, hyphen-separated.
2. `dependency` stores canonical IDs (or `Core_Law/...` paths), not ambiguous aliases.
3. Frontmatter must appear before any heading text.
4. `status` is versioned and monotonic (`v1`, `v2`, ...).
5. `claim_mode` describes the file's dominant speech act; it is not the same thing as definition authority.

## Frontmatter Minimal Schema Ratchet (2026-07-20)

治理减负轮起，frontmatter 规范改为**棘轮制**，不做全仓回改（1289 个文件的 churn 不值得）：

1. **只对新建或本次实质修改的文件**要求最小 4 字段：`id`、`status`、`claim_mode`、`updated`。其余字段（`type`、`tags`、`layer`、`epistemic_layer`、`dependency`）推荐但不强制；理论承重文件仍应补全上面 Canonical Metadata Contract 的完整字段。
2. **`status` 收敛为小枚举**：`draft` / `active` / `frozen` / `archived`（历史文件保留旧的 `active_vN` 等值，不强制回改；新写只用这四个）。版本细节写在正文，不再进 `status`。
3. **废除逐文件 `canonical:` 字段**。是否 canonical 只看 `CANONICAL_REGISTRY.md`——逐文件写 `canonical: false` 是冗余噪音（全仓 702 处都在说"我不是权威"），新文件不再写该字段；碰到旧文件时可顺手删除，但不为此专门开轮。
4. 存量文件的旧字段值不算违规；preflight 警告基线继续记录已知债，不作为质量分。

## Touch-Based Repair Rule (2026-07-20)

休眠层与存档层文件（域层、coverage 快照、archive 记录、停驻种子）按**触碰即修**治理：

- 只在被活跃任务实际读取、且发现错误、断链或过时符号用法时修复；
- 修复走普通 A 类编辑 PR，**不开专项治理轮，不产生新台账**；
- 不预防性地扫描或同步休眠层 frontmatter；"让它保持最新"不是修复理由，"活跃任务被它绊到"才是。

这与书稿的 hard guard 同构：不预防性维护档案，只在使用时校验。

## Current Claim-Mode Notes

- `canonical`: definition-bearing or canonical-facing theory anchor.
- `governance`: edit policy, claim discipline, quality protocol, or workflow rule.
- `navigation`: index, router, reading path, registry, or bootstrap aid.
- `translation`: bridge/interface mapping to another domain or theory.
- `hypothesis`: lab, proxy, prediction, or testable candidate.
- `evidence`: source card, material record, empirical summary, or support note.
- `historical_record`: archive, dated log, old audit, release note, or provenance record.
- `manifesto`: public/worldview statement; not a theory definition source unless separately anchored.
5. `layer` is the vertical axis; `epistemic_layer` is the horizontal axis.
6. Never fuse the two axes into one value such as `L1-bridge`.
7. `claim_mode` describes assertion posture, not theory depth.

## Two-Axis Layer Contract

SRT docs use a two-axis coordinate model:

- `layer` = vertical theory depth (`meta`, `L0`, `L1`, `L2`)
- `epistemic_layer` = horizontal posture (`os`, `bridge`, `lab`)

Recommended reading of the pair:

- `(L0, os)` = metaphysical root
- `(L1, os)` = internal formal/reference interface
- `(L1, bridge)` = external comparison or domain translation
- `(L2, lab)` = falsifiable protocol / hard bet

For full semantics, see `Governance/SRT_COORDINATE_SYSTEM.md`.

## Hybrid Model Layout Contract
All domain theory files should keep this fixed skeleton:
1. Title + version note.
2. `## Terminology Alignment`.
3. `# Part A: Formal Axioms (形式化公理)`.
4. Axioms/Theorems with LaTeX + Chinese implications.
5. `# Part B: Expanded Theoretical Discourse (扩展理论论述)`.

Stability rules:
1. Do not duplicate `Part A`/`Part B` blocks in one file.
2. Keep theorem IDs stable after publication.
3. Preserve legacy terms by alias notes when renaming symbols.

## Symbol Governance
Single source of truth: `_SRT_SYMBOL_TABLE.md`.

Rules:
1. One symbol, one canonical meaning in core context.
2. Contextual symbols must carry scope suffixes if overloaded.
3. Use `\Psi_f` for ontological friction; reserve `\Phi` for IIT context.
4. Update symbol table before introducing new notation in domain files.

## Directory Contract
Domain roots:
- `Core_Law/`: supreme axiomatic references
- `Core/`: core bridge + kernel + formal equations
- `Physics/`, `Neuroscience/`, `Philosophy/`, `Spirituality/`, `AI/`: domain expansions

Cross-domain registries:
- `_SRT_INDEX.md`
- `_SRT_ATOMIC_MAP.md`
- `_SRT_SYMBOL_TABLE.md`
- `_SRT_MANIFEST.yaml`

Rules:
1. Domain-local bridge files use leading underscore (example: `_SRT_AI_Bridge.md`).
2. Public entry docs should be listed in `_SRT_MANIFEST.yaml`.
3. Broken links must be fixed in both `_SRT_INDEX.md` and `_SRT_ATOMIC_MAP.md`.

## AI Interaction Contract
To maximize retrieval and reasoning quality:
1. Keep one stable heading per concept block.
2. Avoid conflicting IDs/symbols across files.
3. Keep equations near the theorem that uses them.
4. Put dependency-critical terms in frontmatter and section headers.
5. Mark legacy aliases explicitly instead of silent replacement.
6. High-propagation docs should state their coordinate explicitly, such as `(L1, bridge)`.

## Minimal QA Checklist
Before publishing changes:
1. Frontmatter parse check: every modified file has valid YAML block.
2. Link check: all Markdown links resolve.
3. ID check: no duplicate `id:` across repository.
4. Symbol check: no duplicate core symbol semantics.
5. Equation sign check: no contradictory dynamics in same module.

## Automation Commands
Use these commands before publishing:

```bash
# 0) Update manifest-maintained entrypoint blocks manually
# Sync `_SRT_MANIFEST.yaml`, `SRT_Quick_Start.md`, `_SRT_INDEX.md`

# 1) Run repository checks from workspace root
./scripts/run_srt_checks.sh

# 2) Generate quality snapshot from SRT/
uv run python ../scripts/srt_quality_metrics.py

# 3) Generate explainability audit from SRT/
uv run python ../scripts/srt_explainability_audit.py
```

> 注：仓库当前未包含 `srt_doc_validate.py`、`srt_sync_entrypoints.py` 或 `sync_srt_entrypoints.sh`。依赖字段规范化与入口块同步目前仍是人工流程。

## Human Writing & Style Protocol (人类写作与文风规范)

### 1. 总体原则
1. **先定义，后发挥**：先给可检验定义，再给哲学解释。
2. **一条公式，一句中文解释**：避免只堆公式或只讲概念。
3. **Canonical 优先**：涉及 d 值、核心公理时，先回链规范定义。
4. **同一术语同一写法**：中英、符号、大小写保持一致。

### 2. 标题与层级
- 一级标题：文档主题（唯一）
- 二级标题：模块分区（定义/推导/实验/边界）
- 三级标题：具体条目（如某公理、某案例）

推荐结构：
1) 核心命题  
2) 形式化表达  
3) 直观解释  
4) 可证伪预测  
5) 边界与反例

### 3. 双语术语规范
- **首次出现格式**：`中文术语（English Term, Symbol）`
  - 示例：潜在域（Latent Domain, $L_0$）
- **再次出现格式**：可只用中文+符号，或英文+符号，但整篇要一致。

### 4. 公式书写规范
1. 行间公式后必须跟一句“含义句”。
2. 若为局部近似，必须标注“近似/投影/操作化”。
3. 不得把局部公式写成全局定义。

### 5. d 值专门规则（强制）
- 任何文档引入 d，必须至少一次引用 canonical：`AI/SRT_AI_01_Ontology.md` Ax-ONT-3
- 若使用 $d\approx \alpha A + \beta\log V + \gamma\tau$，必须注明：“认知域操作化近似，不替代 canonical 定义”。
- 跨尺度 $d_{quantum}/d_{bio}/d_{cosmic}$ 必须标注为投影语境。

### 6. 证据与引用规范
- 每个关键主张至少给 1 个来源（内部文件路径或外部论文/书籍）。
- 若为推测，标注：`[Speculative]`
- 若为待验证，标注：`[Testable Hypothesis]`

### 7. 语气与可读性
- 避免绝对化词汇（“必然正确”“最终真理”）。
- 优先使用“在以下条件下成立”。
- 每 300-500 字加入一个结构锚点（小标题/列表/表格）。

### 8. 表格与符号一致性
- L0/L1/L2 统一写为 `L_0/L_1/L_2`
- `\Psi_f`、`\hat{G}_\theta`、`ii` 不混写成其他近似拼法。
- 同一表格中单位统一（秒、Hz、概率等）。
