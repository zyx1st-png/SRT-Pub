---
id: SRT-DOWNSTREAM-GUARDRAILS
type: framework
status: active
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-EDIT-PROTOCOL, SRT-CANONICAL-FREEZE, SRT-D-VALUE-CANONICAL, SRT-SYMBOL-TABLE]
provenance:
  - 01_Source_Intuition/Conversations/2026-07-25_具身位_d_q_o_收尾审计.md
  - Operations/_SRT_REVIEW_QUEUE.md#RQ-2026-08-A02
  - Operations/SRT_AUTHOR_DECISION_PACKET_EUCLID_DQO_PHYSICS_A10A11_2026-08-05.md
updated: 2026-09-13
tags: [Governance, Guardrail, Embargo, DownstreamSurfaces]
---

# SRT Downstream Guardrails

> **Role**: owner of standing restrictions on what may reach **downstream surfaces** — 书稿, 公共内容, bridge, 论文. These are governance decisions about propagation, not theory definitions: nothing here creates, changes or relaxes a canonical definition, and nothing here settles an OPEN question.
>
> **Why this file exists**: these restrictions were living in `STATUS.md`, a high-churn dashboard that says of itself that it is routing/programme state and not a definition authority. `Governance/SRT_EDIT_PROTOCOL.md` assigns 治理规则 to `Governance/`, so they belong here. `STATUS.md` keeps a pointer, not the source.

## Reading rule

A guardrail here says a restriction is **in force**. It does not say the underlying question is settled — in general the opposite: an interim guardrail exists precisely because the substantive decision is still open, and its job is to stop an unadjudicated candidate from propagating downstream while the author decides.

```text
downstream restriction = ACTIVE
!=
substantive / formal question = ADJUDICATED
```

Each guardrail below records:

- **Guardrail status**: in force, and whether the underlying decision is open or settled.
- **Recorded**: where the restriction was first written down, and where the open decision is tracked.
- **Restriction**: the operative sentence, verbatim.
- **Scope**: which surfaces it binds.
- **Lift condition**: what would end it. Absent that, it stands.

A guardrail is lifted by an explicit author decision recorded here — never by omission, by a rewrite elsewhere, or by a downstream file simply going ahead. Recording a guardrail here never upgrades the status of the question it guards.

## Machine consumers

`scripts/build_srt_context_bundles.py` reads the restriction sentences from this file by anchor marker and renders them into every context bundle. `scripts/check_status_recording_rule.py` fails if an anchor is removed.

Keep each restriction between its `SRT-GUARDRAIL:<ID>-BEGIN` / `-END` markers, on its own line. Editing the prose inside the markers changes what every bundle tells its reader, so treat it as a governance edit, not wording cleanup. The earlier form of this anchor was a free-text search for a Chinese phrase, and status rewrites deleted it twice (`ed20ccf`, `156c4db`), each needing its own restore commit — that is the failure mode the markers exist to stop.

---

## G-DQO — `d` / `q` / `o` three-axis embargo

**Guardrail status**: **ACTIVE / INTERIM — the underlying decision is AWAITING AUTHOR.** The embargo is in force; whether `q` is a post-stake-gate constitutive-depth profile or an independent axis, and whether `o` is operationalized or given a symbol, is **not adjudicated**.

**Recorded**: 2026-07-25, by the closure audit `01_Source_Intuition/Conversations/2026-07-25_具身位_d_q_o_收尾审计.md`, which states of itself 「本文件不裁决理论……所有认定均为候选，是否成立、是否落地都归作者裁决」. The open decision is tracked as **`RQ-2026-08-A02`** in `Operations/_SRT_REVIEW_QUEUE.md` (status: Awaiting author), with the embargo listed there as its 当前护栏; it is carried in the author decision packet `Operations/SRT_AUTHOR_DECISION_PACKET_EUCLID_DQO_PHYSICS_A10A11_2026-08-05.md`.

The 2026-07-23..07-25 materials proposing an embodied-position rewrite and the `d`/`q`/`o` three axes were logged as **routed as candidates, none landed**. Known collisions: `d` read as participation rate conflicts with the norm definition in `Def-d-canonical`; two of the five components of `q` fall inside the `C_i` definition text of `Def-w_i`.

**Restriction**:

<!-- SRT-GUARDRAIL:DQO-BEGIN — extracted verbatim by scripts/build_srt_context_bundles.py guard_dqo(); do not delete, reword or split the marker pair. -->
已加下游护栏：符号重命名与 `q` / `o` 的形式选择做出前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文。
<!-- SRT-GUARDRAIL:DQO-END -->

**Scope**: 书稿, 公共内容, bridge, 论文. It does not restrict internal audits, proposals, or material-pipeline records, which may discuss the candidate axes as candidates.

**Lift condition**: `RQ-2026-08-A02` is adjudicated by the author — the symbol rename decided **and** the formal choice for `q` / `o` made. Until both, the embargo stands. Nothing in this file may be read as having made that decision.

**Not implied**: the embargo is not a verdict that the three axes are wrong, and it does not authorize rewriting the `d` definition. `_SRT_D_VALUE_CANONICAL.md` remains the `d` owner; `_SRT_SYMBOL_TABLE.md` remains the symbol owner.
