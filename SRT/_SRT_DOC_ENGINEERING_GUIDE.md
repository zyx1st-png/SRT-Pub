---
id: SRT-DOC-ENGINEERING
type: framework
tags: [Documentation, Engineering, Standards]
status: axiomatic_hybrid_v1
dependency: [_SRT_MANIFEST, _SRT_SYMBOL_TABLE]
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
status: axiomatic_hybrid_vN
dependency: [SRT-..., Core_Law/...]
---
```

Rules:
1. `id` is globally unique, uppercase, hyphen-separated.
2. `dependency` stores canonical IDs (or `Core_Law/...` paths), not ambiguous aliases.
3. Frontmatter must appear before any heading text.
4. `status` is versioned and monotonic (`v1`, `v2`, ...).

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
# 0) Sync manifest entrypoints into quick-start and index
python3 scripts/srt_sync_entrypoints.py

# 1) Normalize dependency aliases to canonical IDs
python3 scripts/srt_doc_validate.py fix-deps

# 2) Run repository checks (IDs, dependencies, key links)
python3 scripts/srt_doc_validate.py check

# 3) Convenience wrapper
./scripts/run_srt_checks.sh

# 4) Entrypoint sync wrapper
./scripts/sync_srt_entrypoints.sh
```

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
