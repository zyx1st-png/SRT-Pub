---
id: SRT-EXPLANATION-PROTOCOL
type: framework
tags: [Documentation, Explainability, WritingProtocol]
status: axiomatic_hybrid_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [_SRT_DOC_ENGINEERING_GUIDE, SRT-GLOSSARY, SRT-REF-AXIOMS]
---

# SRT 解释协议（Definition → Mechanism → Falsification）

## 目的

该协议用于统一 SRT 文档的解释链条，确保每个核心概念都能被：
- 人类读者快速理解；
- 跨学科读者可靠验证；
- AI 系统稳定检索与推理。

---

## 标准五段结构（强制）

每个核心条目（概念/定理/模型/方程）必须按如下顺序组织：

1. **定义（Definition）**
   - 给出最小可判定定义。
   - 明确该条目的层级语境：`L_0 / L_1 / L_2`。

2. **形式化（Formalization）**
   - 至少一个公式或符号关系。
   - 公式后必须紧跟“含义句”。

3. **机制解释（Mechanism）**
   - 说明该结构如何在系统中起作用（过程/路径/因果门控）。
   - 明确与 `\hat{G}_\theta`, `\Psi_f`, d 的关系。

4. **可证伪条件（Falsification）**
   - 提供可观测指标、对照条件或失败判据。
   - 标记证据等级（preprint / peer-reviewed / speculative）。

5. **边界声明（Boundary）**
   - 使用正式标题：`## 【理论边界/防误用声明】`
   - 说明该条目不适用的范围、不可推导结论、常见误用。
   - 若涉及“方法论闭包/自然主义/神经还原”争议，必须单列：
     - `方法论有效性` 与 `本体论完备性` 的区分；
     - `神经关联` 与 `体验同一` 的非等价声明；
     - 主观沉思证据的公共可检验边界。

---

## 规范模板（可直接复用）

```markdown
### <条目标题>

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

## d 值与符号专门约束

1. d 值 canonical 定义锚定：`_SRT_D_VALUE_CANONICAL.md`。
2. 任何近似式（如线性组合）必须标注“操作化近似，不替代 canonical”。
3. 外部 state-space 记号（`\Omega`, `S` 等）写入 SRT 时统一映射为 `L_0`（可在脚注保留来源符号）。
4. `\Psi_f` 仅用于本体论摩擦语境，避免与其他符号语义混用。

---

## 来源与谱系（Lineage）

- 新术语、新变量、新判据首次引入必须附：`[Lineage/Source]`。
- 推荐格式：
  - `[Lineage/Source] DOI:...`
  - `[Lineage/Source] Author (Year), Section ...`
  - `[Lineage/Source] Internal: <path#heading>`

---

## 最小发布检查（与工程规范协同）

发布前至少满足：
1. 五段结构完整。
2. 方程后有含义句。
3. 存在可证伪条件。
4. 边界声明为正式 Header。
5. 新术语带 lineage。

可与 `Governance/_SRT_DOC_ENGINEERING_GUIDE.md` 的 QA 项联动执行。
