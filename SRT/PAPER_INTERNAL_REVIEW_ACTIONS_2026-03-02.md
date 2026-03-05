---
id: SRT-PAPER-INTERNAL-REVIEW-ACTIONS-2026-03-02
type: paper
tags: [Paper, InternalReview, Actions]
status: draft_v1
dependency: [_SRT_PAPER_CANDIDATES, Core_Law/SRT_Reference_Dynamics, Core/SRT_Core_14_Dynamics_Scaling]
---

# 内审修订单 v1（选题 #1）

## 题目
From Partial Closure to Stable Closure: Minimal Embodiment Threshold in SRT

## 必修项（立刻）
1. **补一手文献链**
   - 目标：找到 New Scientist 报道对应的原始论文/预印本 DOI。
   - 验收：正文引用至少 1 条 primary source。

2. **锁定 \(N_{crit}\) 操作化定义**
   - 方案：给出单一主口径（信息承载量 proxy），其余作为备选 proxy。
   - 验收：方法节出现“主口径 + 备选口径 + 失效条件”。

3. **反例边界表**
   - 最低包含：晶体增长、模板复制但无自治闭环、外部脚本驱动复制系统。
   - 验收：每个反例都有“不满足哪条闭包条件”的明确判据。

## 次修项（本周内）
4. **增加可证伪预测 2-3 条**
   - 如：环境补偿下降时，\(\mathcal{C}_{partial}\) 系统复制链中断概率陡升。

5. **图1结构化**
   - Phase diagram: partial closure → stable closure with \(I(\theta)\), \(\Psi_f\), env-window axes.

## 风险控制
- 禁止把“结构自治阈值”写成“意识起源阈值”。
- 必须保留：结构复制 \(\neq\) \(d>0\) 关切涌现。


## 新增硬条件（2026-03-05）

6. **N_{crit} 可回写性硬判据（必加）**
   - 规则：跨越 \(N_{crit}\) 不仅要求系统可维持复制与局部闭包，还必须满足“环境规律可被微观组件稳定回写到 \(\theta\)”：
   \[
   \exists\,\mathcal{R}_{env\to\theta}>0,\quad \theta_{t+1}=\theta_t+\Delta\theta(\mathcal{E}_{env},\Psi_f)
   \]
   - 验收：正文方法节出现“可回写性指标（rewrite index）+ 阈值 + 失效域”。

7. **时间之箭双判据对齐（必加）**
   - 规则：论文中关于“生物时间之箭”的表述，必须同时呈现：
     1) 错综层级记录增量 \(\Delta L_2^{nested}\)；
     2) 摩擦不可逆账本 \(\int\Psi_f dt\)。
   - 验收：讨论节给出联合表达式，并说明缺任一项时的解释失败场景。

