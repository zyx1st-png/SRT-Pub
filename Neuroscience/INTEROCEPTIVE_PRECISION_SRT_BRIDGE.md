---
id: SRT-INTEROCEPTIVE-PRECISION-BRIDGE-2026-08-08
type: bridge_audit
tags: [Neuroscience, ActiveInference, Interoception, Precision, Homeostasis, d-value, Psi_f, Experiment]
status: active
layer: L1-L2-bridge
epistemic_layer: bridge-lab
claim_mode: interface
claim_level: P3-P4
canonical: false
date: 2026-08-08
dependency:
  - SRT-FEP-METAAWARENESS-AFFECTIVESELF-BRIDGE-2026-05-04
  - SRT-PHIL-COMPARE-FEP
  - SRT-FISHER-FEP-LANDSCAPE-INTERFACE
  - SRT-D-VALUE-CANONICAL
  - SRT-PSIF-CANONICAL
  - SRT-OPEN-TENSIONS
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
source:
  title: "Interoceptive Attention as Dynamic Homeostatic Prioritization in a Foraging Agent"
  authors: "St John Grimbly et al."
  date: 2026-08-04
  arxiv: "2608.04232"
  peer_reviewed: false
---

# Interoceptive Precision × SRT：技术审计与差异实验

> **结论先行**：这篇 active-inference 预印本为“有限资源下必须选择性分配感知精度”提供了一个很好的 P3 实现桥，但它**不证明** `precision = d`、`precision budget = Ψ_f`，也暂时**没有给出 SRT 相对 richer active inference 的独有预测**。最有价值的下一步，是冻结比较模型后做一个 `precision × stake` 因子实验，并允许结果否定 SRT 的额外解释价值。

## 0. 来源与最小事实

Grimbly 等人在四通道觅食环境 AffectWorld 中，让 active-inference agent 在固定 interoceptive precision budget 下，把更多 precision 动态分配给当前最需要的身体通道。论文报告：在 11 个布局、每个布局 32 个随机种子中，动态 need-aligned precision allocation 的学习期生存率为 `0.414`，uniform precision 为 `0.199`；若将 precision 指向最不需要的通道，表现低于均匀分配。把同一 shaped likelihood 从 planner 中拿掉，会损失约一半收益。

来源：Grimbly et al., arXiv:2608.04232, 2026-08-04。**预印本，尚未同行评审。**

这项结果支持的最窄命题是：

```text
在固定总精度预算下，精度分配的方向本身会改变信念更新、规划与生存表现。
```

它不自动支持：

```text
precision = SRT selection
precision = d
precision budget = Ψ_f
survival advantage = consciousness
active inference = SRT
```

---

## 1. 问题一：precision allocation 与 SRT“选择”是否同构？

### 裁决：**部分同构的实现桥，不是完整同构。**

在论文模型中，总预算受限：

\[
\sum_i \pi_i = B_\pi
\]

因此提高某一身体通道的 precision 必然降低其他通道的相对权重。它具备 SRT 很关心的三个结构：

1. **排他性 / 机会成本**：不能同时把所有通道都提到最高精度；
2. **方向性**：系统必须决定哪个需要优先；
3. **下游后果**：该分配同时进入 belief update 与 planning，并改变后续生存轨迹。

但 precision 仍主要是**信号可靠性 / gain / likelihood weighting**。仓库现有 FEP bridge 已明确：precision deployment 可以作为 attention-like selection mechanism，却不能因此成为完整的 SRT 选择事件。

SRT 额外要求检查：

- 候选可达集是否真的被收窄或重排；
- 后果是否回到同一 bearer；
- 是否发生历史写回而改变未来可选择能力；
- 是否存在不可逆或至少非平凡的重新开放成本。

因此最安全的映射是：

```text
precision allocation
→ P3 attention / selection-eligibility implementation
→ 可能参与 SRT selection event
≠ SRT selection 本身
```

---

## 2. 问题二：fixed precision budget 能否作为 selection cost 的实验代理？

### 裁决：**可以作为资源约束与机会成本操纵，不可直接作为 `Ψ_f`。**

`B_π` 的优点是非常适合实验：总预算固定后，选择一个方向会可测地牺牲其他方向。因此它可以作为：

- attentional / inferential capacity constraint；
- local opportunity-cost manipulation；
- `P_sel` 可用选择预算的候选实验接口之一。

但 `B_π` 本身不是实际支付的 `Ψ_f`。canonical `Ψ_f` 关心的是：系统把可能性压成一个可维持现实路径时，真正承担了多少 payability burden，以及支付后是否仍保有闭包、身份连续性和后续选择能力。

所以实验中应分开记录：

```text
总 precision budget          = 资源约束
precision reallocation       = 分配动作
belief / planning distortion = 机制后果
恢复时间、损伤、未来容量下降 = Ψ_f-related paid-burden proxy 候选
```

若只看到“预算有限”，最多证明存在 trade-off；不能据此写 `Ψ_f`。

---

## 3. 问题三：`d` / `Ψ_f` 能否预测 precision 重新分配的临界点？

### 裁决：**目前不能给出已校准临界公式；只能提出 P4 候选。**

仓库当前开放张力仍包括：

- `D_eff → d_stakes` 的必要充分 gate 尚未完全封口；
- `Ψ_f` 各 projection 的完整必要充分条件仍未完成；
- precision、salience、homeostatic error 都不得直接替代 canonical `d`。

因此这里不能伪造一个“由 SRT 已推导”的 threshold。可保留两个可失败候选：

### P4-IP1 — Stake-gated precision shift

在**感知噪声、当前 homeostatic error 和总 precision budget 匹配**时，如果某通道的失配会真实回流到同一 bearer，并造成更高的不可逆风险 / 未来选择能力损失，那么该通道的 precision reallocation 应表现出：

- 更早 onset；
- 更陡的 allocation slope；
- 更强的历史依赖或 after-effect。

这里的 `d` 只能作为 stake-coupled concern 的解释坐标；不能用 need magnitude 或 precision 本身代替。

### P4-IP2 — Payability turnover

逐步提高 precision sharpening / switching 的实际代价时，性能收益不应无限单调增加。候选现象是：当恢复成本、资源透支或未来选择能力损失进入不可支付区间后，系统出现策略重构、迟滞或崩塌，而不只是连续的小幅性能下降。

这可作为 `Ψ_f` payability 的实验窗口，但在数据前不得声称存在确定的 SRT 临界常数。

---

## 4. 问题四：怎样设计 active inference 与 SRT 可能给出不同结果的阴性实验？

## 4.1 核心设计：`precision × stake` 因子分离

至少做一个 2×2：

| | 低/均匀 precision control | 动态 need-aligned precision |
|---|---:|---:|
| **低 stake / 可重置后果** | C1 | C2 |
| **高 stake / bearer-returning 后果** | C3 | C4 |

尽量匹配：

- 当前 homeostatic error magnitude；
- sensory noise；
- 总 precision budget；
- 即时 reward / preferred-outcome strength；
- 当前任务难度。

**stake 操纵不要用“更大奖励”代替。** 推荐把差异放在后果结构：

- **低-stake 条件**：失败带来同等即时数值损失，但可以完全 reset，不改变该 agent 后续 sensorimotor / policy capacity；
- **高-stake 条件**：失败的后果回到同一 agent，并持续缩窄其之后可用的 observation / action / recovery capacity。

主要观察量：

1. precision reallocation onset / slope；
2. policy switching latency；
3. post-threat hysteresis；
4. recovery cost；
5. future reachable-policy loss；
6. survival / task performance（只作为结果之一，不作为唯一指标）。

## 4.2 必须冻结 competitor，而不是赛后扩大 FEP

这项实验只有在比较前先锁定模型类才有意义。至少比较：

- `M_AIF-base`：论文式 precision allocation + 当前 generative model；
- `M_AIF-history`：允许足够的 temporal depth / transition learning / richer preferred priors；
- `M_SRT-bridge`：在相同基础机制上额外显式编码 bearer-specific consequence return、future-selectability loss 与 paid-burden proxy。

必须预先声明相同的 refit budget、horizon 和评价向量，避免出现：

```text
SRT 赢了 → 说明 SRT 必要
AIF 输了 → 赛后把 stake/history 全部塞回 AIF 再宣布等价
```

也要避免反向作弊：若 richer AIF 在相同复杂度 / refit budget 下已经完整解释数据，不能因为 SRT 语言更贴切就宣布额外机制成立。

## 4.3 阴性结果 / 删除审计

按 `GOV-SUB01`，目标不是“证明 SRT”，而是测试删除 SRT 特有角色后是否产生稳定损失。

### 对 SRT 不利、必须接受的结果

若在冻结比较条件下：

```text
M_AIF-history
```

仅靠 precision、preferred states、transition model、temporal depth 和 ordinary learning 就能同时解释：

- stake 条件差异；
- hysteresis；
- recovery；
- future policy-space contraction；

且加入 bearer-specific `d` / `Ψ_f` bridge 变量没有带来新的预测、干预或反事实区分，则本接口应判为：

```text
R2 implementation substitutable
或
R3 target-relative dispensable
```

至少对这个实验目标而言，SRT 没有取得独立增量。

### 对 SRT 有利但仍不足以升级 canonical 的结果

只有当冻结后的 richer-AIF 在允许的 refit budget 内仍系统性遗漏：

- bearer relocation；
- 相同即时价值下的不可逆 consequence-return 差异；
- delayed future-selectability loss；
- matched endpoint 下不同 history 造成的持续 reallocation / hysteresis；

而显式加入这些结构后产生稳定的预测或干预增益，才可把该角色记为：

```text
N1 current target-relative indispensable candidate
```

这仍只是 P4 实验支持，不是 `d` / `Ψ_f` 的 canonical 证明。

---

## 5. 本次桥接的最小保留结论

1. **值得吸收**：固定预算下的动态 precision routing 是“选择不是单纯增加资源，而是决定资源给谁”的干净实现案例。
2. **不得吸收**：precision、need、survival、free energy 都不能直接改名为 `d` 或 `Ψ_f`。
3. **真正的 SRT 压力点**：如果 active inference 通过 richer priors、temporal depth 与 history learning 已经能无损吸收 stake / payability 现象，SRT 必须承认该局部桥没有独有机制贡献。
4. **最值得做的实验**：不是比较“dynamic precision vs uniform precision”，论文已经做了；而是做 **matched precision / different stake** 与 **matched endpoint / different consequence history** 的分离，并在数据前冻结 comparator 和 refit budget。

## 6. 当前状态

```text
Bridge verdict: useful, non-canonical P3 interface
Experimental status: P4 candidate
Unique SRT prediction: not yet established
Best next test: precision × stake factorial + subtractive audit
Canonical edits required: none
```
