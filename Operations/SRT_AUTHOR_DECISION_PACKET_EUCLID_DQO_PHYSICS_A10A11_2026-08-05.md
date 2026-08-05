---
id: SRT-AUTHOR-DECISION-PACKET-EUCLID-DQO-PHYSICS-A10A11-20260805
type: framework
status: active
claim_mode: governance
updated: 2026-08-05
record_stage: awaiting_author_decision
layer: meta
epistemic_layer: os
related_files:
  - 01_Source_Intuition/Conversations/2026-07-25_具身位_d_q_o_收尾审计.md
  - Governance/Archive_2026-06-05/SRT_CORE_TEXT_ADJUDICATION_2026-04.md
  - Operations/Audits/Hook_Closure_Audit_2026-07-25.md
  - Core/SRT_Core_01_Axioms.md
  - Physics/_SRT_Physics_Hardening_Index.md
  - Operations/_SRT_REVIEW_QUEUE.md
---

# 作者裁决包：中文主论证、`q/o`、A10/A11 与 Physics P03/P04/P05

## 0. 文件角色

本文件只整理仍需作者决定的真实仓库事项，不替 canonical 层作废止、升格或符号决定。

- 未裁决前，不修改 canonical registry、符号表、Core/Core_Law、Physics owner、书稿或论文正文；
- 可以逐项裁决；
- 推荐项只是保守治理建议，不是既成结论。

---

## D1. 中文主论证入口

### 当前事实

- `Core_Law/SRT_Core_Text_CN.md` 是 `legacy_v1` 的历史主文／读者入口，并明确不再承担唯一主入口；
- `Core_Law/SRT_Core_Text_CN_Euclid.md` 是可升格候选，CLAUDE 快速路由已指向它，但 registry 仍只把它标作 candidate；
- 2026-04 预审记录位于 `Governance/Archive_2026-06-05/SRT_CORE_TEXT_ADJUDICATION_2026-04.md`。

### CT-A — 维持现状（推荐默认）

- CN.md 维持 legacy 读者入口；
- Euclid 维持快速路由候选，不升格为正式 registry / canonical 入口；
- `SRT_Selection_Argument.md` 维持哲学辩护／展开论证角色。

### CT-B — 正式升格 Euclid

- Euclid 成为正式中文主论证入口，但不替代 L0 anchor；
- 同步 registry、manifest、快速路由和三文件角色说明；
- CN.md 继续保留为 legacy reader entry。

### CT-C — 撤回 Euclid 的快速入口

- Euclid 回到实验／候选位置；
- 中文快速路由改回其他入口；
- 需要说明为什么推翻 2026-04 以来的入口演进。

---

## D2. `q` 的形式地位

候选含义：已通过 stake gate 的关切方向之不可替代性、历史写入、身份连续性影响、未来选择能力影响与历史调用深度。

### Q-A — 门后剖面，不设新轴（推荐默认）

- 暂称 `constitutive depth`；
- 作为已通过 `R·A·C` 门的解释性剖面；
- 只有出现与 `d_stakes` 可分离的经验后果后，再评估独立变量。

### Q-B — 独立候选轴

先进入 open tension / P2–P3 candidate；必须补定义域、与 `d` 的关系、matched-different-q 案例、可分离预测和删除测试。未满足前不进 canonical。

### Q-C — 继续停驻

只保留原始对话与审计记录，不继续发展术语或操作化。

---

## D3. `o` 是否形式化

### O-A — 分解读数，不设裸 `o`（推荐默认）

分别保留跨位置不变性、现实抵抗、公共可校正性、共享沉积稳定性与持续可失败性，不合成为最终分数。

### O-B — fallibilist 向量

建立明确标注为 P3/P4 的向量对象，只在声明域与扰动协议内解释。

### O-C — 综合标量

当前不推荐；选择前必须解决权重、域依赖、共同遮蔽和“高分但仍错误”的反例。

---

## D4. `Ax-Core-A10/A11` 的实验钩缺口

### 当前事实

`Core/SRT_Core_01_Axioms.md` 仍是 `claim_mode: canonical`、version 6.0 的活 owner；`Ax-Core-A10` 与 `Ax-Core-A11` 仍在使用，`Governance/SRT_POSITIONING.md` 也继续将意识论／统一论路由到该文件。Core 21 主锚点化不等于 Core_01 已废止。

### AX-A — 保留为待审缺口（推荐默认）

- 不改 Core_01 的地位；
- 将“Part B 是否缺标准化实验钩”保留为待重新核验项；
- 只有重新检查当前正文与实验映射后，才判断需新增、迁移或关闭。

### AX-B — 建立双层同步方案

- Core_01 继续承载现有 A10/A11；
- 新实验接口落到当前 P2–P4 / hypothesis 架构；
- 增加明确 cross-reference 和 owner-sync 规则，而不是宣布旧 owner 被取代。

### AX-C — 证实已被现有实验接口覆盖后关闭

只有逐项列出 A10/A11 对应的当前实验钩与证据路径，才能关闭该缺口。

---

## D5. Physics P03/P04/P05 的统一落点

真实待裁决组：

- `Physics/patches/SRT_Phys_P03_Cosmological_Principle_Effective_Symmetry_v0_1.md`
- `Physics/patches/SRT_Phys_P04_Spontaneous_Collapse_Classicality_v0_1.md`
- `Physics/patches/SRT_Phys_P05_Quantum_Proper_Time_Optical_Clocks_v0_1.md`

`Operations/Audits/Hook_Closure_Audit_2026-07-25.md §3.3` 已确认：三张 hook 的 planned target 都是尚未创建的 `Physics/SRT_Physics_Bridge_v0_2.md`。真实裁决是一个统一二选一，不是三项分别评分。

### PHY-A — 新建 `Physics/SRT_Physics_Bridge_v0_2.md`

- 将 P03/P04/P05 与现有 Physics hardening patch 做一次去材料化综合；
- 保留 `_SRT_Phys_Bridge.md` 为旧主文／历史 bridge；
- 必须说明 v0.2 与 P06–P08、REP01、E01–E05 的分工和不重复边界。

### PHY-B — 并入现有 `Physics/_SRT_Phys_Bridge.md`

- 修改三张 hook 的 landing target；
- 在现有主文增加三个有边界的段落；
- 避免再创建第二份长期维护的 Physics bridge owner。

两种选择都不构成对 P03/P04/P05 的 canonical 升格，也不声称相关物理材料证明 SRT。

---

## 6. 最小裁决格式

```text
Chinese core = CT-A / CT-B / CT-C
q = Q-A / Q-B / Q-C
o = O-A / O-B / O-C
A10/A11 hooks = AX-A / AX-B / AX-C
Physics P03-P05 landing = PHY-A / PHY-B
```

## 7. 执行边界

- CT-B 才触发入口与 registry 修改；
- Q-B、O-B 只允许先进入 open tension / bridge；
- AX-B 必须保留 Core_01 的当前 canonical 事实，除非另有正式废止裁决；
- PHY-A/PHY-B 只处理 hook landing，不授权 Physics canonical 升级；
- 任一选择都不自动授权书稿或投稿论文回写。
