---
id: SRT-GOV-LOAD-REDUCTION-2026-07-20
type: framework
status: active
claim_mode: governance
updated: 2026-07-20
dependency: [SRT-GOVERNANCE-README, SRT-DOC-ENGINEERING, SRT-PARKED-INDEX]
---

# Governance Load Reduction Round — 2026-07-20

## 触发与诊断

用户反馈：仓库治理过度，严格筛选后的内容"沉底"。诊断确认核心病灶不是筛选太严，而是**只有下沉通道、没有回流通道**，且治理规模仍按巅峰期十条 pipeline 设计，而当前活跃工作面只有书稿、论文与社媒文章三条线。量化证据（减负前）：

- 近 60 天提交：`01_Source_Intuition`（书稿）742 次，papers 34，Operations 31；AI / Neuroscience / Physics / Spirituality 四域 **0 次**。
- 根目录 80 个 md（口径见下「计数口径」）；`claim_mode: navigation` 文件 231 个（约 18%）；`canonical: false` 逐文件字段 702 处（`canonical: true` 0 处——权威只在 REGISTRY，逐文件字段是纯噪音）。
- 状态镜像三份且互相不一致：`STATUS_FAST.md` 自 05-23 未更新，却是 bootstrap 必读。
- Operations 顶层条目 92 项（含子目录；其中 md 文件 84），50+ 是已关账的一次性审计记录（冻结成 markdown 的 CI 日志）。

## 确立的四条比例原则

见 `Governance/README.md §Proportionality Principles`：①治理强度跟活跃度走；②过滤器必须自带回流路径；③状态只有一个面；④导航一进一出。

## 本轮执行动作

1. **Operations 归档**：51 个已关账记录 → `Operations/Archive_Records/`（含 README）；链接全改；`scripts/audit_large_files.py` 报告路径同步。Operations 顶层 md 84 → 34（含子目录的顶层条目 92 → 44）。
2. **根目录瘦身**：22 个停驻文件移出根目录——16 个研究种子/候选 note → `90_Backstage/Incubation/`；3 个停摆计划 → `90_Backstage/Plans_Archive/`；2 个一次性审计 → `Operations/Archive_Records/`；`FRONTSTAGE_RESTRUCTURE_PLAN.md` → `Governance/`（裁决记录）；删 `_tmp.txt`。根目录 md 80 → 54。
3. **停机坪索引**：新建 `_SRT_PARKED_INDEX.md`——全仓停驻内容唯一浮标索引，每条带具名复活触发条件（绑工作线事件）；覆盖种子、材料 B 卡、未合 PR（P1-T07 #676、common-state-probe 分支）、停摆计划。
4. **冻结 7 个 coverage index**：`status: archived` + `snapshot_as_of: 2026-07-20` + 冻结横幅，停止维护义务（评审修正：不扩展 status 小枚举，快照语义走非 status 字段）。
5. **休眠层冻结戳**：AI / Neuroscience / Neuroscience_Annex / Physics / Spirituality 入口加"带冻结戳的图书馆"声明（as-of 2026-05、canonical 漂移免同步、touch-based repair only）。
6. **状态面收口**：`STATUS.md` 45KB → ~15KB，历史条目迁入 `Operations/Status_History/2026-04_to_2026-07_Dashboard_Part.md`，新增 §Fast Status 吸收 bootstrap 职责；删 `STATUS_FAST.md`、`STATUS_Split/`。
7. **Boot 读单 4 → 3**：`_SRT_SYMBOL_QUICK_GUARD.md` 并入 `SRT_AI_START.md §3`；`AGENTS.md §Session Start` 改写。
8. **Router 侧车合并**：3 个 `_SRT_CONTEXT_ROUTER_*_EXTENSION/ADDENDUM.md` 折进主 router §21/§22/§23，删除；加禁止新增侧车的维护规则。
9. **人类入口收编**：`SRT_Public_Reading_Guide.md` 的分轨阅读并入 `SRT_Navigation_Map.md`（单一人类 hub），删除；`SRT_Quick_Start.md` 与 `SRT_1H_Onboarding.md` 作为不同深度的真实阅读体验保留，由 hub 路由。
10. **治理规则更新**：frontmatter 最小 4 字段棘轮 + status 小枚举 + 废除逐文件 `canonical:` 字段 + touch-based repair（`_SRT_DOC_ENGINEERING_GUIDE.md`）；B 类裁决语义改"停驻 + 具名触发条件"（`Operations/_SRT_MATERIAL_PIPELINE.md`）；四原则入 `Governance/README.md`；可观测指标入 `_SRT_QUALITY_METRICS.md`。

## 明确不做（沿用 2026-07-07 前台裁决，理由一致）

- 不做目录大迁移、不重编号（高断链风险、零理论收益）。
- 不动 claim ladder、canonical freeze、edit protocol、书稿 hard guard（真正承重且都很小）。
- 领域层文件不删不并（跨域身体，保留检索价值，只解除维护义务）。
- 不做全仓 frontmatter 回改（1289 文件 churn 不值得；棘轮只对新建/新改生效）。

## 计数口径（唯一权威）

核心减负计数只用一个指标：**深度 1 的 `*.md` 文件数**，命令固定为：

```bash
find . -maxdepth 1 -type f -name '*.md' | wc -l
find Operations -maxdepth 1 -type f -name '*.md' | wc -l
```

「含子目录的顶层条目数」（`ls -1 <dir> | wc -l`）是另一个指标，引用时必须写明「含子目录」，不得与 md 文件数混用。

## 可观测指标

见 `_SRT_QUALITY_METRICS.md §Governance Load Indicators`：boot 必读 4→3、根目录 md 80→54、Operations 顶层 md 84→34、状态镜像 3→1、「超 30 天未更新的状态文件」 ≥1→0。

## 评审修正（2026-07-20，合并前）

作者评审提出 4 项承重修正，均已落地：

1. `CLAUDE.md §必读顺序` 收缩为对 `AGENTS.md §Session Start` 的唯一跳转，不再维护竞争性 6 文件列表；TASTE.md 等改标为任务触发后的条件加载。
2. B 卡复活触发条件采用方案 B：**Material Log 为唯一权威源**，`_SRT_PARKED_INDEX.md §2` 只留入口指针，删除逐卡同步义务（避免第二份台账）。
3. `archived_snapshot` 违反本轮新立的 status 小枚举，改为 `archived` + `snapshot_as_of` 字段；`scripts/check_frontmatter.py` 增加枚举棘轮验证（存量旧值锁入警告基线，新违规使 preflight 失败）。
4. 计数口径统一为本节命令，PR 描述 / 本记录 / `_SRT_QUALITY_METRICS.md` / `STATUS.md` 四处数字对齐（含子目录的条目数与 md 文件数分别命名）。

## 链接完整性

迁移 / 删除的文件名在全仓相对链接中已用脚本重算并逐条改写。仓库既有断链基线（changelog split shard 内部链接等 83 处）为迁移前遗留，本轮未新增断链（迁移前后计数 84 → 83）。
