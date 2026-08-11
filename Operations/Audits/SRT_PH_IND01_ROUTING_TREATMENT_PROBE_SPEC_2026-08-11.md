---
id: SRT-PH-IND01-ROUTING-TREATMENT-PROBE-SPEC-20260811
type: audit
status: active
record_stage: probe_spec_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
claim_level: audit_only
canonical: false
date: 2026-08-11
source_of_truth: "origin/main @ 3a614ff4a40cb644450d41014d2b664574fbefd4"
baseline_ref: 122e47b0bbe3835318cd9d729b77f7a437fbc8c8
treatment_ref: 5c1cbc8d66c1f193b2fa1222719969c9dca6f23a
protocol: Operations/Audits/SRT_BOUNDED_RETRIEVAL_PROTOCOL_2026-08-08.md
baseline_specification: Operations/Audits/SRT_MATERIAL_CLUSTER_BASELINE_PROBE_SPEC_2026-08-11.md
baseline_results: Operations/Audits/SRT_MATERIAL_CLUSTER_BASELINE_PROBE_RESULTS_2026-08-11.md
runs_completed: 0
verdict: not_run
dependency:
  - SRT-MATERIAL-CLUSTER-BASELINE-PROBE-SPEC-20260811
  - SRT-MATERIAL-CLUSTER-BASELINE-PROBE-RESULTS-20260811
  - SRT-BOUNDED-RETRIEVAL-PROTOCOL-20260808
tags: [Governance, Audit, BoundedProbe, Treatment, Philosophy, PH-IND01]
---

# PH-IND01 routing treatment probe specification（2026-08-11）

> 这是 treatment 运行前冻结的 specification，不是结果。它只测试一次现有路由干预，不修改理论内容、Axis B 或 claim level。

## 0. Decision target

Baseline Philosophy suite 的唯一失败是：

~~~text
P-A / P-Q5 = fail
reason      = bounded budget 内未到达 PH-IND01
diagnostic  = unconstrained pass
case        = B retrieval/compression gap
~~~

本 treatment 只回答：

> 在其他理论内容完全不变时，给现有 Context Router 增加一条 PH-IND01 声明式入口，能否让同题同预算的 fresh sessions 稳定取得 object-tracking negative control？

本轮不测试 PH-IND01 的理论正确性，不把婴儿对象追踪升级为主体性证据，也不授权新的 Philosophy synthesis。

---

## 1. Frozen refs and treatment delta

### 1.1 Baseline

~~~text
122e47b0bbe3835318cd9d729b77f7a437fbc8c8
~~~

### 1.2 Treatment

~~~text
5c1cbc8d66c1f193b2fa1222719969c9dca6f23a
~~~

Treatment ref 从 baseline ref 直接分叉，只包含一个提交：

~~~text
nav: route object individuation negative control
~~~

唯一文件差异：

~~~text
_SRT_CONTEXT_ROUTER.md
~~~

唯一内容差异是在 Route 8 与 Route 9 之间加入 Route 8a：

- query triggers：object individuation / identification / tracking / index、infant object representation、`still this one`、minimal subject、bearer individuation、subjecthood negative control；
- Primary：`Philosophy/_SRT_Philosophy_Hardening_Index.md § PH-IND01`；
- Secondary：PH-IND01 patch、Subjecthood Threshold Interface、Core_Law Individuation；
- Boundary：object tracking continuity 不等于 consequence-bearing continuity；object index 不等于 minimal subject 或 consciousness。

Treatment ref 不含：

- baseline probe specification；
- baseline result；
- 本 treatment specification；
- rubric、标准答案或其他 run 输出。

运行前必须核验：

~~~text
git rev-parse HEAD
git status --short
test ! -e Operations/Audits/SRT_MATERIAL_CLUSTER_BASELINE_PROBE_SPEC_2026-08-11.md
test ! -e Operations/Audits/SRT_MATERIAL_CLUSTER_BASELINE_PROBE_RESULTS_2026-08-11.md
test ! -e Operations/Audits/SRT_PH_IND01_ROUTING_TREATMENT_PROBE_SPEC_2026-08-11.md
~~~

任一条件不满足，run 作废。

---

## 2. Matched conditions

为满足 protocol §1.3，对 baseline 已经实际使用的 frozen wrapper 做严格配对：

- 同一模型族与 reasoning 配置；
- 同一 Philosophy A/B/C 三个 form；
- 同一 18 个 observation；
- 同一 blind question 文本；
- 同一 rubric 与 positive markers；
- 同一每 run 6 body files / 2 navigation actions；
- 同一 `AGENTS.md §Session Start` 文件免费 wrapper；
- fresh independent session；
- 不传其他 run 路径、答案或评分。

这里沿用较宽 wrapper 只为 baseline/treatment 对称，不改变 protocol 对未来新 suite 的 4-file 默认规则。

Reserve 规则不变：Form D 只替换因预算、工具、ref 或泄题而作废的 run；有效但答错不能替换。第二个正式 run 作废则停止并修订 spec。

---

## 3. Frozen forms

问题文本、rubric、禁止捷径与 positive 标记逐字继承 baseline specification §6；不得在运行提示中发送 rubric。

| Form | Questions |
|---|---|
| P-A | P-Q1, P-Q2, P-Q4, P-Q5, P-Q8, P-Q10 |
| P-B | P-Q3, P-Q4, P-Q6, P-Q7, P-Q9, P-Q11 |
| P-C | P-Q1, P-Q5, P-Q6, P-Q9, P-Q10, P-Q12 |
| P-D reserve | P-Q2, P-Q3, P-Q7, P-Q8, P-Q11, P-Q12 |

Anti-gaming positives：`P-Q3 / P-Q5 / P-Q6 / P-Q10`。

---

## 4. Success and attribution gates

### 4.1 Treatment pass

必须同时满足：

- 3 个正式 run 均有效；
- 18/18 observation 为 pass；
- positive failures = 0；
- `P-A / P-Q5` 从 baseline fail 变为 pass；
- P-B、P-C 无回归。

因为 baseline 其余 17 项已通过，本 treatment 不采用一般的 17/18 下限；只有 18/18 才算 targeted treatment pass。

### 4.2 Intervention attribution

除 §4.1 外，还必须满足：

- `P-A` retrieval ledger 在预算内记录 Route 8a 或由 Route 8a 触发的 PH-IND01 hardening-index / patch 路径；
- Q5 的 repository basis 实际包含 PH-IND01 的 `tracking boundary != consequence-return boundary`；
- treatment ref 相对 baseline 没有其他内容或导航差异。

若 18/18 但 P-A 通过无关搜索取得 PH-IND01：

~~~text
behavioral availability = observed in treatment
intervention attribution = not established
~~~

若 P-A 仍失败：

~~~text
treatment effect = failed
next action       = reassess compression/trigger wording only
content writeback = not authorized
~~~

---

## 5. Operator wrapper

每个会话只接收以下 wrapper 加 baseline specification §6 中对应 form 的六个 blind questions：

~~~text
你正在对 SRT 仓库做一次预注册的 bounded routing treatment probe。

硬规则：
1. 当前 HEAD 必须是 5c1cbc8d66c1f193b2fa1222719969c9dca6f23a，且 worktree clean。
2. 先按 AGENTS.md Session Start 读取启动文件；为与 baseline 配对，这些免费。
3. 启动后最多读取 6 个正文文件，最多 2 次 search/grep/目录导航。
4. 禁止无目标递归遍历；失败搜索也计一次导航。
5. 对每题给出 verdict、关键区分、repository basis。
6. 仓库没有依据时明确写 NO REPO BASIS，不用一般常识补成 SRT 结论。
7. 最后报告完整预算与 retrieval ledger；不要给整个题组判 Case。
~~~

不得发送：

- Route 8a 的预期作用；
- P-Q5 是 baseline failure；
- rubric、required distinctions、positive markers；
- baseline 或其他 treatment run 的检索路径／答案。

---

## 6. Stop rule

运行完成前不得：

- 修改 Route 8a；
- 修改 PH-IND01、Philosophy hardening index、Subjecthood Threshold Interface 或 Core_Law Individuation；
- 修改 CompactCore、deep map、context bundle 或 active-theory registry；
- 新建 Philosophy synthesis；
- 把 spec merge 当作行为证据。

结果另建文件，记录原始答案、预算、路径、逐题评分、归因门与最终 disposition。

~~~text
treatment runs       = not_run
intervention effect  = untested
Axis B change        = none
Axis C change        = none
~~~
