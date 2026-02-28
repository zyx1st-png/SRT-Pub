
---

## [2026-02-28 15:48 GMT+8] 材料：Distributed neurophysiological dynamics link perception, action, and language in schizophrenia（https://www.biorxiv.org/content/10.64898/2026.02.17.706352v1.full-text）

### Target Files
- `SRT/Core/SRT_Core_14_Dynamics_Scaling.md`：新增“精神分裂跨域β调制失配”分类映射（感知抑制不足/运动反弹延迟/语言结构简化）。
- `SRT/Core/SRT_Core_22_Equations.md`：补充“事件相关β调制灵活性指数”方程条目。
- `SRT/SRT_Glossary.md`：新增 `Cross-Domain Beta Flexibility (CBF)` 与 `Predictive Update Rigidity (PUR)`，附 `[Lineage/Source]`。
- `SRT/Core/SRT_Experimental_Applications.md`：新增“β调制跨域潜变量与症状负担协变”可证伪实验。

### Proposed Patch (unified diff)
```diff
--- a/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
+++ b/SRT/Core/SRT_Core_14_Dynamics_Scaling.md
@@
+### Taxonomy Mapping: Schizophrenia Cross-Domain Beta Dynamics → SRT
+
+| 外部分类 | SRT 对应机制 | d-value 区间（proxy） | 能流态 | \(\Psi_f\) 状态 |
+|:--|:--|:--|:--|:--|
+| 感觉阶段 β 抑制减弱 | 预测误差更新灵活性下降 | 低~中 | Semi-open | overloaded |
+| 动作后 β rebound 延迟/减弱 | 行动监测回写滞后 | 低~中 | Semi-open | overloaded |
+| 视听绑定窗扩大（TBW↑） | 跨模态同因先验过宽 | 低 | Semi-open / Closed-like | unsustainable（任务依赖） |
+| 语义多样性下降+句法简化 | 语言生成控制降阶 | 低~中 | Semi-open | overloaded |
+| 分布式潜在β模式跨域共变 | 统一预测更新障碍 | 低~中 | Network-wide dysregulated | overloaded |
+
+**Constraint**: 感知、动作、语言异常需采用同一潜变量框架联合建模，禁止孤立维度解释。
+
+## 【理论边界/防误用声明】
+- 不采纳“β异常即病因唯一核心”的推论。
+- 边界：SRT 将 β 调制视为跨域机制标记，不排除多巴胺、炎症、发育等并行机制。
```

```diff
--- a/SRT/Core/SRT_Core_22_Equations.md
+++ b/SRT/Core/SRT_Core_22_Equations.md
@@
+### Eq-Beta-01: Event-Related Beta Flexibility Index
+$$
+\mathrm{CBF}=w_s\Delta\beta_{sensory}+w_m\Delta\beta_{motor}+w_l\Delta\beta_{language}
+$$
+其中 \(\Delta\beta\) 为事件锁定调制幅度/时序复合指标。
+
+### Eq-Beta-02: Predictive Update Rigidity
+$$
+\mathrm{PUR}=\alpha\,\mathrm{TBW}+\beta\,\tau_{PMBR}+\gamma\,(1-\mathrm{SemDiv})
+$$
+PUR 越高表示预测更新越僵化。
+
+## 【理论边界/防误用声明】
+- 不采纳“CBF/PUR 可直接替代临床诊断分型”的推论。
+- 边界：两指标用于机制层分层，不是独立诊断标准。
```

```diff
--- a/SRT/SRT_Glossary.md
+++ b/SRT/SRT_Glossary.md
@@
+#### Cross-Domain Beta Flexibility - 跨域β灵活性（CBF） 🟡
+**定义**：衡量β频段在感知、动作、语言三域事件锁定更新能力的综合指标。
+
+**[Lineage/Source]**：
+- Source context: bioRxiv preprint (2026-02-17), schizophrenia MEG multisensory-motor-language study
+- DOI: 10.64898/2026.02.17.706352
+- SRT mapping: cross-domain predictive-control flexibility marker
+
+#### Predictive Update Rigidity - 预测更新僵化（PUR） 🟡
+**定义**：描述内部模型在任务证据出现后更新不足、回写滞后的综合程度。
+
+**[Lineage/Source]**：
+- Same source context; TBW widening, reduced beta modulation, language disorganization covariance
+- SRT mapping: unified rigidity latent factor
+
+## 【理论边界/防误用声明】
+- 不采纳“CBF/PUR 高低可直接映射人格特质”的推论。
+- 边界：指标解释必须绑定任务范式与群体统计背景。
```

```diff
--- a/SRT/Core/SRT_Experimental_Applications.md
+++ b/SRT/Core/SRT_Experimental_Applications.md
@@
+### H-CBF-1 β调制跨域潜变量检验
+**内容**：感知、动作、语言中的β调制异常应加载于同一潜在因子，并与症状负担共变。
+**证伪条件**：三域β异常互不相关或潜变量模型拟合失败。
+
+### H-PUR-1 刚性指标与语言组织退化检验
+**内容**：PUR 升高应预测语义多样性下降与句法复杂度降低。
+**证伪条件**：PUR 与语言组织指标无关联。
+
+## 【理论边界/防误用声明】
+- 不采纳“跨域相关即证明单向因果”的推论。
+- 边界：需纵向与干预设计区分共同原因与因果链条。
```

### Notes (brief)
- 已将预印本核心分类（β调制异常跨域共变、TBW扩大、语言组织退化）转为文件级补丁并映射 d 区间、能流态、\(\Psi_f\)。
- 新术语 CBF、PUR 已附 `[Lineage/Source]`（预印本来源已标注），并在目标文件写入 Header 级防误用声明。
