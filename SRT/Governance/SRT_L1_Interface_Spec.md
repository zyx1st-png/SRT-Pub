---
id: SRT-L1-INTERFACE-SPEC
type: governance
tags: [Governance, L1, Template, InterfaceSpec]
layer: meta
status: canonical_v1
epistemic_layer: os
claim_mode: canonical
---

# SRT L1 接口规范

> **用途**：新建任何 L1 领域文件（Bridge / Axioms / 领域理论）前，以本规范为模板。
> 遵守本规范，新文件就自动处于正确的层级位置，不会成为 L0 污染源。

> **坐标提醒**：L1 是垂直轴，不等于水平轴里的 `bridge`。
> 大多数 L1 文件的标准坐标是 `(L1, bridge)` 或 `(L1, os)`；不要再写 `L1-bridge` 这样的融合值。

---

## 一、L1 文件的 Frontmatter 标准

```yaml
---
id: SRT-[DOMAIN]-[IDENTIFIER]        # 全大写缩写，例如 SRT-NEURO-CONSC-001
type: [theory|bridge|experiment|mechanism|analysis]
tags: [[Domain], Bridge, Hybrid]
layer: L1                             # 必填，固定值
status: axiomatic_hybrid_v1
epistemic_layer: bridge               # bridge / os / lab 之一
claim_mode: translation               # translation / canonical / lab
dependency: [SRT-L0-METAPHYSICS, ...]  # 必须包含 SRT-L0-METAPHYSICS
---
```

**必须满足的字段**：
- `layer: L1` — 明确标注，不可省略
- `dependency` 第一项必须是 `SRT-L0-METAPHYSICS`
- `epistemic_layer` 选 `bridge`（领域映射）或 `os`（操作系统层理论）
- `layer` 与 `epistemic_layer` 是正交字段，不得合并

---

## 二、L1 文件的头部 Blockquote 标准

每个 L1 文件正文开头必须有一个定位 blockquote，包含三行：

```markdown
> **坐标定位**：本文件位于 `(L1, bridge)`。
> **层级说明**：本文件属于 **L1（接口层）**，是 L0 [具体命题名] 在 [领域名] 的映射。
> L0 形而上意义见 [`Core_Law/SRT_L0_Metaphysics.md`](../Core_Law/SRT_L0_Metaphysics.md)。
> 本文件的论证成立依赖 [列举本文件依赖的外部框架]，若该框架修订，本文件需同步更新。
```

示例（神经科学文件）：
```markdown
> **层级说明**：本文件属于 **L1（接口层）**，是 L0"选择总是有位置的"命题在神经科学中的映射。
> L0 形而上意义见 [`Core_Law/SRT_L0_Metaphysics.md`](../Core_Law/SRT_L0_Metaphysics.md)。
> 本文件的论证依赖自由能原理（FEP）与预测编码框架；若 FEP 被证伪，本文件的 L1 映射需更新，但 L0 命题不受影响。
```

---

## 三、[R] / [H] 标注规范

L1 文件中引用外部文献时，使用以下标注区分来源与 SRT 独有贡献：

| 标注 | 含义 | 何时使用 |
|:---|:---|:---|
| `[R]` | 既有框架 / 文献 / 科学结论 | 引用 Whitehead、IIT、FEP、神经科学发现等 |
| `[H]` | SRT 独有主张 / 新映射 | SRT 对 [R] 内容的重新诠释、新增结构、形式化 |
| `[H-高承诺]` | 高风险 SRT 主张 | [H] 中尚无证伪路径的强形而上主张 |

**铁律**：任何 `[R]` 标注的内容都不能作为 L0 命题的"证明"。它们只是 L0 命题在该领域的"共鸣"或"实例"。

---

## 四、L1 ↔ L0 映射表（每个 L1 文件必须有）

每个 L1 文件应在靠前位置包含一张映射表，显式说明本文件与 L0 的对应关系：

```markdown
## L0 → L1 映射说明

| L0 命题 | 本文件的 L1 映射 |
|:---|:---|
| 选择先于存在（命题一）| [本领域中对应的概念，如：神经选择先于感知表征] |
| 三域结构（命题二）| [本领域的三域实例，如：量子叠加/本征态/退相干] |
| 选择有位置（命题三）| [本领域的算子实例，如：具身预测编码系统] |
| 选择有代价（命题四）| [本领域的代价量，如：代谢成本 / 自由能 / Ψ_f] |
```

---

## 五、可证伪性声明（L2 内容的挂载点）

L1 文件可以包含可证伪性声明，但需明确标注为 L2 内容挂载点：

```markdown
> **[L2 挂载]**：以下预测属于 L2 验证层内容，可证伪。
> 若被证伪，影响本文件的 L1 映射，不影响 L0 命题。
```

如果可证伪内容较多，应独立成 L2 文件（`SRT_EXP_*.md`），而不是堆积在 L1 文件内。

---

## 六、一个完整的最小 L1 文件示例

```markdown
---
id: SRT-NEURO-EXAMPLE-001
type: theory
tags: [Neuroscience, Bridge, Hybrid]
layer: L1
status: axiomatic_hybrid_v1
epistemic_layer: bridge
claim_mode: translation
dependency: [SRT-L0-METAPHYSICS, SRT-NEURO-AXIOMS-001]
---

# SRT 神经科学接口：意识选择机制（示例）

> **坐标定位**：本文件位于 `(L1, bridge)`。
> **层级说明**：本文件属于 **L1（接口层）**，是 L0"选择总是有位置的"命题在神经科学中的映射。
> L0 形而上意义见 [`Core_Law/SRT_L0_Metaphysics.md`](../Core_Law/SRT_L0_Metaphysics.md)。
> 本文件依赖预测编码框架（Clark 2016, Friston 2010）；若该框架被修订，本映射需同步更新。

---

## L0 → L1 映射说明

| L0 命题 | 神经科学映射 |
|:---|:---|
| 选择先于存在 | 预测先于感知输入的整合 |
| 三域结构 | 先验信念（L₀）/ 当下感知（L₁）/ 习得模型（L₂）|
| 选择有位置 | 预测编码系统绑定于具身神经结构 |
| 选择有代价 | 预测误差最小化 ≈ Ψ_f 的神经实现 |

---

## §1 核心机制

[正文内容...]

> **[L2 挂载]**：以下预测属于可证伪内容：
> - 高 L₂ 固化的被试（强迫症状）在预测误差校正任务中应表现出更高代谢成本
```

---

## 七、检查清单（提交前验证）

- [ ] frontmatter 包含 `layer: L1`
- [ ] `dependency` 第一项是 `SRT-L0-METAPHYSICS`
- [ ] 没有把 `layer` 和 `epistemic_layer` 融成 `L1-bridge` 之类的单值
- [ ] 正文开头有定位 blockquote（三行标准格式）
- [ ] 包含 L0 → L1 映射表
- [ ] 所有引用文献标注了 `[R]` 或 `[H]`
- [ ] L2 内容（可证伪预测）有明确的 `[L2 挂载]` 标注
- [ ] 没有任何一句话在为 L0 命题"提供证明"
