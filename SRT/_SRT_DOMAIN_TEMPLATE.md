---
id: SRT-DOMAIN-TEMPLATE
type: framework
tags: [Template, Domain, Documentation]
status: axiomatic_hybrid_v1
dependency: [_SRT_DOC_ENGINEERING_GUIDE, _SRT_EXPLANATION_PROTOCOL, SRT-GLOSSARY]
---

# SRT Domain Document Template

> 用途：新建任何领域文档（Physics/Neuroscience/Philosophy/AI/Spirituality）时的标准骨架。  
> 目标：保证专业性、可解释性、可扩展性与 AI 可解析性一致。

---

## 1) Frontmatter（必填）

```yaml
---
id: SRT-<DOMAIN>-<KEY>
type: <theory|definition|axiom_set|equation|framework|experiment|architecture>
tags: [<Domain>, <Theme>, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-..., Core_Law/...]
---
```

规则：
- `id` 唯一、全大写、连字符风格。
- `dependency` 只写 canonical id 或 `Core_Law/...`。
- 不得省略 `tags/status/dependency`。

---

## 2) 标准正文骨架（强制）

```markdown
# <文档标题>

## Terminology Alignment（术语与规范对齐）
- d-value canonical: `AI/SRT_AI_01_Ontology.md` Ax-ONT-3
- 三域记号统一：`L_0 / L_1 / L_2`
- 算子记号统一：`\hat{G}_\theta`
- 摩擦记号统一：`\Psi_f`

# Part A: Formal Axioms (形式化公理)

## <模块A>
### <条目A1>
#### 1) 定义（Definition）
...

#### 2) 形式化（Formalization）
$$
...
$$
含义：...

#### 3) 机制解释（Mechanism）
...

#### 4) 可证伪条件（Falsification）
- 指标：...
- 对照：...
- 失败判据：...
- Evidence-Level: ...

## 【理论边界/防误用声明】
...

# Part B: Expanded Theoretical Discourse (扩展理论论述)
...
```

---

## 3) 术语治理字段（建议按条目补充）

每个高频术语建议追加：
- `Canonical Scope`
- `Confusable With`
- `Lineage/Source`

示例：
```markdown
- Canonical Scope: ...
- Confusable With: ...
- Lineage/Source: Internal: <path#heading> | DOI:...
```

---

## 4) 外部材料接入规则

1. 外部 state-space 记号（如 `Ω`, `S`）写入 SRT 时统一映射为 `L_0`（可脚注保留原记号）。
2. 新公式若是局部近似，必须标注“操作化近似，不替代 canonical 定义”。
3. 新术语必须带 `[Lineage/Source]`。
4. 若引入跨尺度结论，需检查 `Core_Law/SRT_Reference_Scaling.md` 是否需要补条目。

---

## 5) 发布前最小检查

```bash
./scripts/run_srt_checks.sh
```

必须通过：
- frontmatter 合规
- 本地链接可解析
- 符号表关键 token 不缺失

---

## 6) 文件命名建议

- 桥接文档：`_<SRT>_<Domain>_Bridge.md`
- 主题文档：`SRT_<Domain>_<NN>_<Topic>.md`
- 避免 Legacy 名称重复；若有迁移，保留 alias 或重定向注释。
