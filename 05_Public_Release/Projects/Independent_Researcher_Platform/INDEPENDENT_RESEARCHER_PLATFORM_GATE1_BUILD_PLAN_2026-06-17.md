---
id: INDEPENDENT-RESEARCHER-PLATFORM-GATE1-BUILD-PLAN-2026-06-17
type: build_plan
status: draft_v0_1_preparatory
canonical: false
scope: public_project_planning
project: Independent Researcher Platform
source_prd: INDEPENDENT_RESEARCHER_PLATFORM_PRD_2026-06-17.md
gated_on: INDEPENDENT_RESEARCHER_PLATFORM_GATE0_VALIDATION_KIT_2026-06-17.md
created: 2026-06-17
updated: 2026-06-17
language: zh-CN
---

# IRP Gate 1 构建计划 v0.1（预备）

> **前置条件（硬）**：本计划的价值依赖 [Gate 0](INDEPENDENT_RESEARCHER_PLATFORM_GATE0_VALIDATION_KIT_2026-06-17.md) **PASS**。Gate 0 不过则迭代访谈协议、不进本计划（PRD §11）。本文件是"一旦 PASS 即可启动"的预备件，不是开工令。
>
> 目标：用最薄的工程，把 [PRD](INDEPENDENT_RESEARCHER_PLATFORM_PRD_2026-06-17.md) 的 **P0 集**做成可供 10–20 人 alpha 的平台（BP §17 的 31–90 天）。

## 1. 构建哲学

- **最大风险不是开发费，而是质量控制不足导致品牌被定义为低质量民科场**（BP §15.2）。所以 alpha 先验证质量，不堆功能。
- LLM 辅助开发、轻量平台先行。
- 单点赌注已在 Gate 0 验过；alpha 只需把"手工跑通的协议"产品化，并加上严出与治理护栏。
- 凡 P1/P2 一律延后（PRD §3.2）。

## 2. 推荐技术栈（builder 可改，给默认以免起步即纠结）

| 层 | 推荐默认 | 理由 |
|---|---|---|
| 应用 | Next.js（React）全栈 | 单仓、SSR、API routes，小团队最快 |
| 数据库 | Postgres（含 JSONB） | packet 20 字段用 JSONB，claims/reviews/versions 正规化便于查询 |
| ORM | Prisma | schema 即文档 |
| 认证 | Auth.js / Clerk | opt-in 邮箱注册，符合 FR-ACC-01 |
| LLM | Provider SDK + 自建路由层 | 张力层用前沿模型，其余降级（§5） |
| 文件存储 | S3 兼容对象存储 | 上传长文/原文 |
| 支付 | **延后到 Gate 2** | alpha 不收费 |
| 埋点 | 轻量事件表 + 一个分析面板 | PRD §10.5 |

> 决策点：若团队更熟悉其他栈（如 SvelteKit / Rails），以"小团队能最快交付质量"为准，不强绑上表。

## 3. 数据模型落地（PRD §5.5 → schema 草图）

```text
users(id, email, training_optin bool default false, created_at)          # FR-GOV-09 默认 false
projects(id, owner_id→users, title, visibility[private|unlisted|public]  # 默认 private FR-PRJ-02
         , source_text, created_at)
interview_sessions(id, project_id→projects, phase[tension|object], status, created_at)
turns(id, session_id→interview_sessions, role[system|user], content, intent, created_at)
theory_packets(id, project_id→projects, maturity[T0..T7],
               fields jsonb,        # 20 字段，每字段 {value, prov_status, prov_label, edited_by_human}
               created_at, updated_at)
claims(id, packet_id→theory_packets, text, type, strength, evidence_type, prov_status, prov_label)
risk_flags(id, packet_id, domain, level, allowed_forms[], forbidden_forms[])
reviews(id, packet_id, reviewer_id→users, layer[tension|object], answers jsonb, adopted bool, created_at)
versions(id, packet_id, snapshot jsonb, change_summary, triggered_by, maturity_at, created_at)
events(id, user_id, packet_id, name, props jsonb, created_at)            # PRD §10.5
llm_costs(id, packet_id, operation, model, tokens, amount, created_at)   # PRD §9.4
```

**关键不变量**（用约束/中间件强制，不靠自觉）：
- 任何 `fields[*].prov_status == ai_inferred && !author_confirmed` 的 packet **不可进入 reviews**（FR-CFM-02）。
- `risk_flags.domain ∈ 高风险集` 时，packet 输出端点只能产出 `allowed_forms`（FR-GOV-02/03）；未限形不可升 T3（g3）。
- 成熟度升级只能由 g1–g7 门触发（PRD §5.4），不可手动跳级、不可由点赞触发（DP10）。

## 4. P0 范围与构建顺序

> P0 = Gate 1 alpha 阻断项（PRD §7 各表 P0 + §8 治理 P0）。下列里程碑按依赖排序。

### M1 — 地基（约 2 周）
- FR-ACC-01 注册/登录；FR-PRJ-01/02 项目 CRUD + 默认 private。
- 数据模型 + provenance 管道（每字段带 prov_status/prov_label）。
- FR-GOV-01 风险分类器（先规则 + LLM 兜底）写入 risk_flags。
- 退出：能创建私密项目、上传原文、看到空 packet 骨架。

### M2 — 皇冠（约 3–4 周）★ 核心
- FR-INT-01..05/07 访谈引擎：**张力层在前**、多轮、可续答、反磨平护栏、不评判作者本人。
- FR-INT-04 + §5 模型路由：张力层前沿模型，不降级。
- FR-GEN-01/02 packet 生成 + 字段级 provenance。
- FR-CFM-01/02/03 **命门确认**（"我们有没有看穿你？"）→ 触发 g2。
- FR-GOV-07 AI 透明标签在展示层可见。
- 退出：真实输入 → 张力层产物 → 作者确认命中 → packet 到 T2。

### M3 — 严出 + 发布（约 2–3 周）
- FR-GOV-02/03/04 风险限形门（接 g3）；FR-GOV-05/06 作者照护边界。
- FR-REV-05 AI-assisted red-team；FR-GEN-04 失败条件协同补全（到 T3）。
- FR-PUB-01/02 发布 private/public + 透明标签；FR-GOV-08/10 归属/删除/导出；FR-GOV-09 训练 opt-in 默认关。
- 退出：packet 能安全走到 T3 并发布；高风险样例（如 joy 样本）被正确限形。

### M4 — alpha 硬化（约 2 周）
- PRD §10.5 埋点；§9.4 单 packet 成本记录 + 超限告警。
- 接入 10–20 alpha 用户（founding circle + opt-in 招募）。
- 跑 BP §14.1 三指标。

## 5. LLM 集成与模型路由（PRD §9.4）

- **张力层（命门）**：前沿模型，不为成本降级（DP3）。访谈 `turn.intent` 留痕以便事后审计挖掘质量。
- **对象层生成 / red-team / 风险分类**：可用较低成本模型。
- 每 packet 写 `llm_costs`；设单 packet 成本上限告警，超限不静默吞。

## 6. 埋点（PRD §10.5 最小集）

`interview_tension_completed` · `author_confirm_hit|miss` · `packet_published` · `review_submitted{layer}` · `review_adopted` · `version_created{substantive}` · `maturity_changed{from,to}` · `risk_flag_set{domain}` · `brief_exported{type}` · `llm_cost_recorded`。

## 7. 里程碑总览

| 里程碑 | 内容 | 约 | 退出判据 |
|---|---|---|---|
| M1 | 地基：账户/项目/数据模型/风险分类 | 2w | 私密项目 + 空 packet 骨架 |
| M2 | 皇冠：访谈引擎 + 生成 + 命门确认 | 3–4w | 真实输入 → T2，命门命中 |
| M3 | 严出 + 发布 + 治理 | 2–3w | 安全走到 T3 并发布，高风险正确限形 |
| M4 | 埋点 + 成本 + 10–20 alpha | 2w | 跑出 BP §14.1 三指标 |

合计 ≈ 9–11 周，落在 BP §17 的 31–90 天窗口内。

## 8. Alpha 完成定义 / 退出到 Gate 2

**Alpha DoD**：10–20 真实用户跑通"创建→访谈→packet→确认→发布→一轮评审"，并产出 BP §14.1 三指标读数：
1. 作者确认准确率（延续 Gate 0 北极星）；
2. 陌生读者 10 分钟理解率；
3. 评审导致实质修订率（g5 触发）。

**进 Gate 2 的判据**：三指标站得住 + 已定首批付费形态（Q4 默认：**Deep Theory Packet 服务包 $199 先行**）。Gate 2 加 P1：张力层/对象层评审表、成熟度状态机全量、版本历史、世界知识对齐、导出、订阅。

## 9. 明确推迟（PRD §3.2 / BP §8.3）

完整推荐流、私信、专家市场、复杂群组、大规模积分经济、自动认证徽章、应用市场、机构私有空间、出版系统、Phase 2 Object Commons。

## 10. 构建期风险

| 风险 | 应对 |
|---|---|
| 把访谈做成"固定问卷"而丢掉张力质量 | M2 以 Gate 0 验过的协议为准；动态追问 FR-INT-06 即便 P1 也尽早做轻量版 |
| 严出门被产品压力磨软（变回音壁） | g3 限形 + g6 冷读者测试用代码不变量强制（§3），非靠人自觉（DP5） |
| LLM 成本失控 | §5 路由 + 单 packet 成本告警 |
| provenance 漏标导致 AI 字段冒充作者确认 | 入库约束：未确认 ai_inferred 不可进评审（§3 不变量） |

## 11. 角色分工（BP §12 → 落到里程碑）

- **Founder / Protocol Architect**：守 M2 访谈协议与命门定义、守严出边界。
- **LLM Workflow Builder**：M2/M3 访谈、生成、red-team、模型路由、确认评估。
- **Full-stack Builder**：M1–M4 平台、数据模型、发布页、埋点。
- **Review Editor**：M3/M4 评审表、成熟度门、冷读者测试、质量边界。
- **Community Moderator**：M4 alpha 招募、用户访谈、争议处理。
