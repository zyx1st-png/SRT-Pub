# diff.md

## [2026-02-28 12:29 GMT+8] 材料：Why Everything in the Universe Turns More Complex（https://www.quantamagazine.org/why-everything-in-the-universe-turns-more-complex-20250402/）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：把外部“复杂化路径”转成 SRT 分类映射表（分类→d 区间/能流态/\(\Psi_f\) 状态）。
- `SRT/Core_Law/SRT_Reference_Scaling.md`：补全新实证尺度（矿物演化、天体核合成）的 \(\hat{G}_\theta\), \(L_0\), \(L_1\), \(L_2\) 定义。
- `SRT/SRT_Glossary.md`：新增功能信息术语，附 `[Lineage/Source]`，并统一全状态空间符号到 \(L_0\)。
- `SRT/Core/SRT_Experimental_Applications.md`：增加可证伪实验（条件复杂度漂移 + 突跃检验）。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: External Complexity Classes → SRT
+
+| 外部分类 | SRT 对应 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 元素核合成复杂化（恒星/超新星） | 宇宙物理选择层 | 低~中 | Open-flow（高能） | payable（阶段性高负载） |
+| 矿物谱系复杂化（地球化学历史） | 地球化学中尺度层 | 中 | Semi-open / Open | payable 或局部 overloaded |
+| 生物功能复杂化（适应与突跃） | 生物-认知层 | 中~高 | Open-flow（代谢耦合） | payable；失衡时 unsustainable |
+
+**Constraint**: 上表 d 为 canonical d 的语境化区间，canonical 定义保持：
+$$d \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|$$
+
+## 【理论边界/防误用声明】
+- 不采纳“复杂度无条件单调上升”的推论。
+- 不采纳“功能信息可替代热力学熵”的推论。
+- 边界：SRT 仅支持“能流开放 + 选择记忆 + 摩擦可支付”条件下的复杂度漂移。
```

```diff
--- a/SRT/Core_Law/SRT_Reference_Scaling.md
+++ b/SRT/Core_Law/SRT_Reference_Scaling.md
@@
+## Def-Scale-M1: Mineral Evolutionary Scale（矿物演化尺度）
+- **\(\hat{G}_{\theta,miner}\)**：在温压-化学势约束下筛选矿物相稳定路径的选择算子。
+- **\(L_0^{miner}\)**：矿物构型、晶格拓扑、缺陷与相变路径的潜在域。
+- **\(L_1^{miner}\)**：当前环境可维持的实际矿物相集合。
+- **\(L_2^{miner}\)**：地质历史沉积出的稳定矿物谱系与路径依赖约束。
+
+## Def-Scale-C1: Cosmic Nucleosynthesis Scale（天体核合成尺度）
+- **\(\hat{G}_{\theta,cosmo}\)**：在引力与核反应网络下对可持续核素组合进行选择的算子。
+- **\(L_0^{cosmo}\)**：核素与反应通道的潜在状态域（外部文献 \(\Omega/S\) 语义统一映射为 \(L_0\)）。
+- **\(L_1^{cosmo}\)**：当前宇宙时段可观测的元素丰度切片。
+- **\(L_2^{cosmo}\)**：恒星代际循环沉积出的丰度结构与演化约束。
+
+## 【理论边界/防误用声明】
+- 不采纳“尺度扩展即可自动获得意识语义”的推论。
+- 边界：跨尺度同构是动力学结构同构，不是现象体验同构。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Functional Information - 功能信息（\(I_f\)） 🟡
+**定义**：
+$$
+I_f \equiv -\log\left(\frac{|\{\sigma: f(\sigma)\ge\theta_f\}|}{|L_0|}\right)
+$$
+其中外部文献常见的全状态空间符号（\(\Omega\), \(S\)）在 SRT 文档中统一映射为 \(L_0\)。
+
+**[Lineage/Source]**：
+- Proposer: Jack W. Szostak
+- Source: Nature (2003), “Functional information”
+- Later extension context: Hazen–Wong complexity framework (as discussed in Quanta feature and cited PNAS program)
+
+## 【理论边界/防误用声明】
+- 不采纳“高信息量=高真实度=高意识”的等号链推论。
+- 边界：信息量、功能性、意识判据在 SRT 中需通过 d 与 \(\Psi_f\) 联合约束。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-Comp-1 条件复杂度漂移检验（跨域）
+**内容**：在开放能流且存在选择记忆的系统中，功能复杂度期望值上升。
+**最小实验**：生物/矿物/天体数据各自建模，并统一到分段趋势检验框架。
+**证伪条件**：满足条件样本不呈正向漂移，且与随机对照无显著差异。
+
+### H-Jump-1 复杂度突跃检验
+**内容**：复杂度增长呈“平台-突跃-平台”分段而非线性连续上升。
+**证伪条件**：突跃模型在三域数据中均无统计优势。
+
+## 【理论边界/防误用声明】
+- 不采纳“由历史趋势直接外推文明终局”的预测性过度推断。
+- 边界：SRT 的实验命题是条件检验，不是无条件历史决定论。
```

### Notes (brief)
- 已按最新 skill 执行：
  - 具体分类已提取并映射到 d 区间/能流态/\(\Psi_f\)
  - 新尺度缺口已给 `SRT_Reference_Scaling.md` 补丁
  - 新术语含 `[Lineage/Source]`
  - `## 【理论边界/防误用声明】` 已作为实际目标文件 Header 写入补丁
