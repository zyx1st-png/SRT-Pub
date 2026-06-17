---
id: IRP-THEORY-PACKET-TEMPLATE-V0
type: theory_packet_template
status: ready_to_use_v0
canonical: false
scope: public_project_planning
project: Independent Researcher Platform
source_prd: ../INDEPENDENT_RESEARCHER_PLATFORM_PRD_2026-06-17.md
created: 2026-06-17
updated: 2026-06-17
language: en
note: "Field set and provenance model are specified in PRD §5.2–§5.4. This is the fillable instantiation. English is the product-facing language; bilingual labels mirror the PRD."
---

# Theory Packet — Template v0

> 这是 PRD §5.2 的 20 字段 + §5.3 来源模型 + §5.4 成熟度门的**可填充模板**。它同时是：访谈输出规格、Gate 0 的承接容器、landing 示例骨架。
>
> **填表三件套**（每个字段下方一行）：`prov`（来源状态）· `label`（展示标签）· 内容。任何 `ai_inferred` 且未 `author_confirmed` 的字段**不得进入社区评审**（PRD FR-CFM-02）。

## 图例

- **prov ∈** `original` | `ai_inferred` | `author_confirmed` | `reviewer_challenged`
- **label ∈** `AI assisted` | `human revised` | `author confirmed` | `reviewer challenged`
- **Req@** = 该字段成为必填的最低成熟度（T1–T7，见 §5.4 门 g1–g7）
- **★** = 单点赌注相关；**★★** = 产品命门字段

---

## Packet header

```yaml
packet_id:        TP-____
theory_title:     ____
author:           ____ (or de-identified id)
maturity:         T_   # T0 Impulse → T7 Public-ready
visibility:       private | unlisted | public
risk_flags:       [none]   # domain ∈ medical|psych|child_ed|finance|legal|political|neuro|self_state
allowed_output_forms:  [unrestricted]   # 高风险时收窄，见字段 15
created / updated: ____ / ____
```

---

## Fields

### 1. Theory title / 理论名称 — Req@ T1
> prov: `____` · label: `____`

`____`

### 2. One-sentence thesis / 一句话主张 — Req@ T1
> prov: `____` · label: `____`

`____`

### 3. Problem origin / 问题来源 — Req@ T1
> prov: `____` · label: `____`
<!-- 这个理论从哪种不满 / 痛点 / 跨学科冲动里长出来？ -->

`____`

### 4. Object proposal / 想让什么被看见 ★ — Req@ T1
> prov: `____` · label: `____`
<!-- 作者真正想让什么被看见、而现在没被看见？ -->

`____`

### 5. Choice tension / 选择张力 ★★ — Req@ T1
> prov: `____` · label: `____`
<!-- 产品命门字段。结构化，不是自由文本。 -->

```yaml
protected_value:           ____   # 真正想守护的选择/价值
competing_pressures:       [____] # 与之冲突的价值/压力/痛苦/优化/权威/处境
current_misread_object:    ____   # 当前语言把它误切成了什么对象
alternative_objectifications: [____] # 同一张力下其他对象化方式（评审补充）
```

### 6. Core concepts / 核心概念 — Req@ T1
> prov: `____` · label: `____`

- `____`

### 7. Glossary / 术语翻译表 — Req@ T1
> prov: `____` · label: `____`

| Author term | Plain-language meaning | Nearest existing term |
|---|---|---|
| `____` | `____` | `____` |

### 8. Core claims / 核心命题 — Req@ T2
> prov: `____` · label: `____`

| # | Claim | type (descriptive/causal/normative/definitional) | strength (strong/weak/unspecified) |
|---|---|---|---|
| C1 | `____` | `____` | `____` |

### 9. Claim map / 命题地图 — Req@ T2
> prov: `____` · label: `____`
<!-- 命题之间的依赖/支撑/冲突关系。文本或 mermaid。 -->

`____`

### 10. Evidence types / 证据类型 — Req@ T3
> prov: `____` · label: `____`

| Claim | Evidence type (empirical / formal / phenomenological / conceptual / none-yet) |
|---|---|
| C1 | `____` |

### 11. World knowledge alignment / 与已有知识关系 — Req@ T2
> prov: `____` · label: `____`

| Adjacent work / field | Relation: complement / oppose / rename / re-draw boundary / misread | Note |
|---|---|---|
| `____` | `____` | `____` |

### 12. Steelman / 最强版本 — Req@ T3
> prov: `____` · label: `____`

`____`

### 13. Red-team critique / 最强反对 — Req@ T3
> prov: `____` · label: `____`

- `____`

### 14. Failure conditions / 失败条件 ★ — Req@ T3
> prov: `____` · label: `____`
<!-- 在什么情况下这个理论被判为错/不适用？这是 T3 门槛，也是严出抓手。 -->

- `____`

### 15. Risk flags / 风险标注 — Req@ T1
> prov: `____` · label: `____`

```yaml
domain: none   # medical|psych|child_ed|finance|legal|political|neuro|self_state
level:  none|low|med|high
allowed_output_forms:   [hypothesis, reflection_framework, research_proposal, observation_protocol, non_clinical_educational]
forbidden_output_forms: [diagnosis, treatment, intervention, financial_legal_advice, protocol_for_others]
author_care_note: "翻译内容，不评判作者本人（PRD DP7）。"
```

### 16. Author confirmation / 作者确认 ★ — Req@ T2
> prov: `____` · label: `____`
<!-- 命门：作者是否觉得被看穿，而非 AI 拆得准不准（PRD FR-CFM-01）。 -->

- Tension layer "did we see you?": `HIT / PARTIAL / MISS`
- Per-field confirmed: `____`
- Overall author sign-off: `[ ] confirmed`

### 17. Review ledger / 评审账本 — Req@ T4
> prov: `____` · label: `____`

| Date | Reviewer | Layer (tension/object) | Key point | Adopted? |
|---|---|---|---|---|
| `____` | `____` | `____` | `____` | `____` |

### 18. Revision history / 修订历史 — Req@ T5
> prov: `____` · label: `____`

| Version | Change summary | Triggered by | Maturity at time |
|---|---|---|---|
| v0.1 | `____` | `____` | `____` |

### 19. Public brief / 大众解释版 — Req@ T6
> prov: `____` · label: `____`

`____`

### 20. Academic brief / 学院对接版 — Req@ T6
> prov: `____` · label: `____`

`____`

---

## Maturity gate checklist (PRD §5.4)

- [ ] **g1 T0→T1**: 字段 1–7、15 已生成
- [ ] **g2 T1→T2**: 字段 5/4 命中（作者确认"被看穿"），核心字段 author_confirmed
- [ ] **g3 T2→T3**: 字段 8 + 14 清晰，字段 15 风险已解析到合规输出形态
- [ ] **g4 T3→T4**: 收到 ≥2 份结构化评审（张力层 ≥1 + 对象层 ≥1）
- [ ] **g5 T4→T5**: 评审触发一次实质性版本变更（字段 18 有 diff）
- [ ] **g6 T5→T6**: 字段 20 生成且通过冷读者测试（PRD §7.6 验收）
- [ ] **g7 T6→T7**: 字段 19 生成，高风险限形已强制
