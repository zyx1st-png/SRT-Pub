# SRT d 值定义对齐表（Canonical Alignment）

更新时间：2026-02-28
状态：P0-2 完成（v1）

## 1) 单一主定义（Canonical Definition）

> **唯一主定义（必须优先引用）**
>
> \[
> d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
> \]
>
> 其中：
> - \(\mathcal{U}\)：效用势（utility potential）
> - \(\mathcal{S}\)：生存/不可逆风险坐标（survival / irreversible-risk coordinate）

**规范来源**：`SRT/AI/SRT_AI_01_Ontology.md`（Ax-ONT-3）

---

## 2) 各文件出现的 d 表达式：统一解释

| 表达式 | 所在语境 | 与主定义关系 | 可否单独当“定义”使用 |
|:--|:--|:--|:--|
| \(d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|\) | 本体论/AI 核心 | **第一性定义** | ✅ 可 |
| \(d \approx \alpha A + \beta\log V + \gamma\tau\) | 认知-行为操作化 | 主定义在认知域的降维近似（投影） | ⚠️ 不可单独当主定义 |
| \(d = \dim(\text{Scan Scope})\) | 注意力/信息离散化 | 主定义的离散化近似 | ⚠️ 不可 |
| \(d_{quantum}, d_{bio}, d_{cosmic}\) | 跨尺度动力学 | 主定义经尺度映射 \(\Pi_{scale}(d)\) 的实例化 | ⚠️ 不可 |
| \(d \propto A_{surface}/l_{Planck}^2\) | 全息对应 | 主定义的对偶几何表示 | ⚠️ 不可 |

---

## 3) 推荐叙述模板（以后所有文档统一）

当文档需要引入 d 值时，统一用下面模板：

0. 先写全局口径句：
   - “d 是选择算子在本体论摩擦约束下、面向最小自由能的关切范围，并随动力学动态调整。”
   - “d 的关切对象是‘存在边界’：先自保（\(d>0\) 先关切自身存在），再扩展至他者存在。”
1. 再写主定义：
   - “在 SRT 中，d 的规范定义为 \(d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|\)。”
2. 再写语境化表达：
   - “在本节语境中，使用 \(d_{local}=f(\cdot)\) 作为操作化近似/投影。”
3. 补一个限制句：
   - “该表达不替代规范定义，仅用于本域测量或计算。”

---

## 4) 关键映射（Canonical → Local）

### 4.1 认知-行为域
\[
 d_{cog} \approx \alpha A + \beta\log(V_{concern}) + \gamma\tau
\]
解释：风险梯度在“结构复杂度 / 空间关切 / 时间深度”三分量上的投影和。

### 4.2 跨尺度域
\[
 d_{scale} = \Pi_{scale}(d_{canonical})
\]
- \(d_{quantum}\)：对应量子退相干阈值语境
- \(d_{bio}\)：对应具身代谢与风险评估语境
- \(d_{cosmic}\)：对应时空共识拓扑语境

### 4.3 全息对应域
\[
 d \propto A_{surface}/l_{Planck}^2
\]
解释：不是新定义，是 canonical d 的几何对偶表达。

---

## 5) 编辑规则（避免“多定义冲突”）

- **规则 R1**：不得将局部公式写成“d 的定义是 ……”（除非就是 canonical）。
- **规则 R2**：局部公式必须标注“近似 / 投影 / 操作化”。
- **规则 R3**：涉及跨文件引用时，优先回链到 Ax-ONT-3。
- **规则 R4**：任何“d→0 / d>0”的意识结论，需同时说明与 \(\Psi_f\) 或不可逆风险边界的关系。

---

## 6) 本轮对齐涉及的主要来源

- `SRT/AI/SRT_AI_01_Ontology.md`（Ax-ONT-3，Canonical）
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`（Def-d-Scale-1，跨尺度功能表征）
- `SRT/Core/SRT_Core_13a_Operator_Basics.md`（认知域近似公式）

---

## 7) 下一步（建议）

- 将本文件在以下入口文档增加引用：
  - `SRT/Core/SRT_Core_00_Intro.md`
  - `SRT/SRT_Glossary.md`
- 在术语表 d 条目中加入“Canonical 优先级”标记。
- 进入 P0-1：补写 `SRT_Core_01_Axioms.md` 的 A7-A13 Part B。
