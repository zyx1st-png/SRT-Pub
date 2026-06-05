---
id: SRT-COORDINATE-SYSTEM
type: governance
tags: [Governance, Layering, CoordinateSystem, Frontmatter]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-POSITIONING, SRT-LAYER-GUARD, SRT-DOC-ENGINEERING]
updated: 2026-06-05
---

# SRT Coordinate System

> **用途**：澄清 SRT 仓库中的两套层级不是竞争关系，而是两根正交坐标轴。
> 任何理论文档都应先确定自己的二维坐标，再写正文。

---

## 1. 核心原则

SRT 当前使用的是**二维坐标治理**，不是单一层级树：

- `layer` 表示**垂直轴**：文档处在 SRT 的哪一层理论深度
- `epistemic_layer` 表示**水平轴**：文档以何种认识论姿态发言
- `claim_mode` 表示**语句模式**：该文件主要在做定义、翻译、假说还是证据记录

因此，一个文件的正确理解方式不是“它属于哪一个层”，而是：

`Document = (layer, epistemic_layer, claim_mode)`

例如：

- `Core_Law/SRT_L0_Metaphysics.md` = `(L0, os, canonical)`
- `Philosophy/SRT_FEP_Comparison.md` = `(L1, bridge, translation)`
- `SRT_EXP_TEMPLATE.md` = `(L2, lab, canonical)`

---

## 2. 垂直轴：`layer`

`layer` 回答的问题是：**这份内容在 SRT 的理论深度上属于哪里？**

| `layer` | 含义 | 典型内容 |
|:--|:--|:--|
| `meta` | 治理/导航/运行层，不直接承担 SRT 理论深度 | registry、status、guide、audit |
| `L0` | 纯形而上根基，不依赖外部理论正确性 | 选择的本体论描述、四命题、元视角 |
| `L1` | 形式化与接口映射层 | 公理、方程、领域映射、比较、bridge |
| `L2` | 可操作化与验证层 | proxy、实验设计、证伪条件、protocol |

---

## 3. 水平轴：`epistemic_layer`

`epistemic_layer` 回答的问题是：**这份内容在以什么样的认识论姿态发言？**

| `epistemic_layer` | 含义 | 典型口气 |
|:--|:--|:--|
| `os` | 底层操作系统/概念语法/内部稳定锚点 | 定义、约束、工作原则、canonical |
| `bridge` | 与外部理论、学科或现实稳态的互译接口 | 对应、重写、窗口、部分特例、候选映射 |
| `lab` | 愿意下注的硬赌点与检验界面 | 假说、proxy、protocol、baseline、反证 |

---

## 4. 交叉矩阵

两根轴组合后，才构成文档的真正位置。

| 坐标 | 含义 | 典型例子 |
|:--|:--|:--|
| `(L0, os)` | SRT 最小形而上根基 | `Core_Law/SRT_L0_Metaphysics.md` |
| `(L0, bridge)` | 纯形而上命题与外部哲学传统的比较接口 | 哲学比较短文、过程哲学接口 |
| `(L0, lab)` | 极少使用；通常说明分类出错，因为纯 L0 一旦可证伪，多半已进入 L1/L2 | 默认避免 |
| `(L1, os)` | SRT 内部形式接口、reference、equation、canonical support | `Core_Law/SRT_Reference_Dynamics.md`、`Core/SRT_Core_22_Equations.md` |
| `(L1, bridge)` | 与 IIT / FEP / GWT / 社会理论 / AI 等的比较与重解读 | `Philosophy/SRT_FEP_Comparison.md`、`AI/_SRT_AI_Bridge.md` |
| `(L1, lab)` | 为实验下注服务的形式接口或 proxy 模型 | 稀有，但允许；需说明为何不是纯 L2 |
| `(L2, os)` | 实验治理、测量规范、验证基础设施 | registry、measurement standard |
| `(L2, bridge)` | 既有实验范式与 SRT 检验口的转换接口 | 外部范式映射到 SRT protocol |
| `(L2, lab)` | 真正下注的协议、假说、反证条件 | `SRT_EXP_TEMPLATE.md`、`Governance/SRT_LAB_HYPOTHESES.md` |

---

## 5. 作者规则

### 5.1 先问垂直，再问水平

每次写文前先回答两个问题：

1. 这段内容属于 `L0 / L1 / L2 / meta` 的哪一层？
2. 它是在以 `os / bridge / lab` 的哪种姿态发言？

只有这两个问题都答完，frontmatter 才算完整。

### 5.2 不要把两根轴熔成一个字段

以下写法一律视为过时：

- `layer: L1-bridge`
- `layer: L0-lab`
- 任何把垂直轴和水平轴熔成一个值的写法

正确写法是拆开：

```yaml
layer: L1
epistemic_layer: bridge
claim_mode: translation
```

### 5.3 `claim_mode` 不是第三套层级

`claim_mode` 只描述**主要断言模式**，不替代前两根轴：

- `canonical`：定义/规范锚点
- `translation`：互译/比较/接口重写
- `hypothesis`：待检验主张
- `evidence`：日志、状态、审计、结果记录

---

## 6. 推荐正文声明

高传播文件在标题后建议显式写坐标说明：

```markdown
> **坐标定位**：本文件位于 `(L1, bridge)`。
> 垂直上，它属于 SRT 的接口/形式层；水平上，它以 bridge 姿态与外部框架互译。
> 若外部理论修订，本文件需同步更新；这不自动回卷到 L0 根基。
```

这样读者不需要猜“这篇是不是在宣称终局真理”。

---

## 7. 与现有治理文件的关系

- `Governance/SRT_POSITIONING.md`：说明 SRT 为什么需要 `os / bridge / lab`
- `Governance/SRT_Layer_Guard.md`：说明如何防止 `L0 / L1 / L2` 漂移
- 本文件：把两者组合成**同一张坐标图**

从本文件起，贡献者默认按二维坐标描述文档，而不是只报单一层级。
