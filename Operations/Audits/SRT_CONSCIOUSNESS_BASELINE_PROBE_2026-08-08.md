---
id: SRT-CONSCIOUSNESS-BASELINE-PROBE-20260808
type: audit
status: active
record_stage: probe_v1_preliminary
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
node_id: NODE-CONSCIOUSNESS
date: 2026-08-08
protocol: Operations/Audits/SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md
probed_ref: a07d2a72
runs: 1
suite_items: 7
verdict: directional Case A — needs two more runs before it is final
---

# NODE-CONSCIOUSNESS 基线探针（2026-08-08，n=1，方向性）

> **这是一次运行，不是结论。** 协议要求 3 次独立 bounded run 才能判 `robustly_observed`。本文件只记录第一次，方向指向 Case A，但**不足以据此关闭该节点**。

---

## 1. 设计

- 协议与预算同 `SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md`；代码库 `origin/main` @ `a07d2a72`，未作修改。
- 7 道题，全部取自清单记录的该节点 blocker——即 2026-08-05 五张意识源卡的**反向修正**：
  1. affective salience ≠ `d`
  2. dual self-states 不应实体化为两个固定模块
  3. 同一连接数据被竞争理论等同拟合 ⇒ 指标判别力
  4. meta-awareness ≠ `T_dir`
  5. 控制感恢复 ≠ 控制权归还
  6. 无任务范式 ⇒ 是否避开预裁剪
  7. 第一人称—神经的可证伪数学桥该如何对待
- 题干不出现任何 SRT 术语名或正确答案。

## 2. 结果

**预算**：启动后 6 / 6 个正文文件，**1 / 2** 次导航（一次 `ls Philosophy/ Neuroscience/`）。未超预算。

（会话自述有一处口径说明：它把 `_SRT_CONTEXT_ROUTER.md` 记为条件性启动文件而非正文文件，因为 `AGENTS.md §Session Start` 第 6 项列了它且触发条件成立。按更严格读法则为 7 个正文文件，**略超预算 1 个**。此处如实记录，不做有利解释——这一点使本次运行的预算合规性带一个保留。）

**判分**：7 / 7 pass，全部调用了正确区分，**没有一题需要 `NO REPO BASIS`**。

要点：

- Q1 正确拒绝把显著性网络活动当 `d`，并同时守住"重叠不是还原"的反向护栏；
- Q2 用 `stable ISP` + `σ_self` 二阶凝结拒绝模块化，而不是简单否认区分；
- Q3 把"两理论等同拟合"读成**这一层指标不判别**，而不是"神经指标无用"，并联系到方法族个体化；
- Q4 把 meta-awareness 定位为 `T_dir^v0 = R_self · A_reorient` 里 `R_self` 的候选代理，**只是半个因子**；
- Q5 用 辅助式／替代式 `L_2` 判准区分"恢复了介入入口"与"只恢复了感受"；
- Q6 指出无任务 ≠ 无脚本，可能采样到**更多** `L_2` 执行；
- Q7 欢迎可证伪的桥接，但按 P3 收，并守住"映射准确 ≠ 同一性"。

## 3. 它是怎么到达的

会话没有读那五张源卡，也没有读任何 `Materials/` 文件。它经 router Route 2 / 3 / 8 到达 `_SRT_D_VALUE_CANONICAL.md`、`_SRT_T_DIR_CANONICAL.md`、`Neuroscience/SRT_Clin_00_IIT_PCI.md`，再经一次目录列举发现了两个我在静态审计中**从未登记过**的文件：

- `Neuroscience/SRT_FEP_MetaAwareness_AffectiveSelf_Bridge.md`
- `Philosophy/SRT_Phenomenal_Structure_Interface.md`

这两个文件直接承载了 Q1／Q2／Q4／Q7 需要的区分。

**这重复了 AI-REASONING 的发现**：清单登记的 blocker（"五张源卡的反向修正在任何快速层中 0 命中"）字面上仍然为真，但它**没有产生行为缺口**——同样的区分在仓库里由别的文件独立承载。静态清单再一次高估了缺口。

## 4. 当前判定

```text
NODE-CONSCIOUSNESS
  structural_assimilation = partially_active   （不变；blocker 字面仍成立）
  behavioral_availability = observed           （bounded，n=1）
  behavior_observation_mode = bounded
  下一步 = 再跑 2 次独立 bounded run；通过则判 Case A 并升 robustly_observed
```

**不施工。** 一次运行不足以立项，也不足以关闭。

## 5. 局限

1. **n=1**，无重复，无方差。
2. 预算合规带一个保留（见 §2 的路由文件计法）。
3. 7 题由我从 blocker 反推设计，可能系统性偏向仓库已覆盖的形状。
4. 本探针不评价那五张源卡本身的价值，只测量相关区分能否在有界预算内被检索并正确使用。
