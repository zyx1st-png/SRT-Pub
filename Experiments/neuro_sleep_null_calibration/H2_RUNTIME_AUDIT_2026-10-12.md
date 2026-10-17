---
id: SRT-NEURO-H2-HISTORICAL-RUNTIME-AUDIT-20261012
type: audit
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: evidence
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Experiments/neuro_sleep_null_calibration/NC0A_READINESS_AND_RESOURCE_LEDGER_2026-10-12.md
  - Experiments/neuro_sleep_null_calibration/PSA_RUNTIME_EVIDENCE_HANDOFF.md
tags: [Neuroscience, Runtime, Evidence, Resource, Audit]
---

# H2 Historical PS-A Runtime Evidence and Resource Feasibility Audit

**裁决：H2 NO-GO / RESOURCE NO-GO。** 已恢复大量此前未入账的原始证据，但尚不能接受一个完整、口径一致且可比较的 `T_PS-A`。这不是“没有查到日志”：6,006 个作业全部核对，历史环境、实际 worker 配置、七次工具结束计时、一次漏记的失败启动及休眠记录均已找回。下述部分时间与条件估算不得填入预注册分母。

## 1. 审核对象、权限和独立性

- 原始审核 HEAD：`9f68b77b0ae35ed9369090eb78d702523a1f8cbf`；base：`4af1135e0908c51edbce4f61f39572d2e9a2f463`，分支 `experiments/neuro-objectification-phase1-20260918`；PR 分支 `codex/neuro-sleep-null-calibration-prereg-20261009`，Draft 保持不变。
- 核查日期：2026-10-12，日志本地时区 `+08:00`；时间表均用此时区。发布时的最终 HEAD 与 CI 另记于 PR 评论。
- 已读取 AGENTS 指定入口、运行/治理入口、H2 handoff、证据审计器、资源账本、预算校验器及预注册 §6.1，并回核 [R5 原评论](https://github.com/zyx1st-png/SRT-Pub/pull/1114#issuecomment-6115880496)。这是同一 R5 审查者的证据补查，不伪称第二名独立审查者已批准预算。
- 原始 `.local/phase2_population_size_scaling/` 存在于主工作树。进一步检查了对应历史 Codex 执行记录、系统电源 ASL 与 Python 系统诊断。未改原始日志、MAT、作业或历史 runner；未运行正式 NC-0a、真实 G0/T1、120 图重建或新的生物学分析。无合并、Draft 变更、NC-0 冻结或 canonical 修改。

## 2. 原始证据和完整性

`P/` 表示原始 `.local/phase2_population_size_scaling/`。`S1` 是本机 `~/.codex/sessions/2026/09/18/rollout-2026-09-18T18-44-40-01a0aed0-33b3-7353-b0a0-a0b5849c316c_01a0b41e-5083-7270-bde7-6208c16a5c51.jsonl`，只读取任务相关记录，不上传会话内容。`ASL/` 表示 `/var/log/powermanagement/`。完整 SHA-256 见文末。

独立扫描结果：

- `execution.log` **1,036,063 行**，其中 981,007 条 checkpoint、49,049 条窗口完成、6,006 条唯一作业完成、1 条全完成记录；没有无法分类的行。
- 6,006 个 job JSON 全部 `complete`，唯一 ID 与日志完成 ID 集合相等；49,049 个窗口 ID 也逐个相等；保存 Q 值计数 **9,809,800**。这是元数据/计数核查，不是重跑 Q。
- 完成清单 CSV 按 job ID 排序，列 `job_id,state`；SHA-256 `648fab574d2f57fbb507f33fe41772a027b47028138e48e175420725da5b583a`。
- 6,006 文件逐一哈希，按文件名排序，每行 `SHA256␠␠filename\n`；该私有哈希清单 SHA-256 `c777ece16da04aa36faca63fbd77184dd4e0c4d52d54f1e467455efb1fcbef9c`。
- `runner.stdout.log` 为空，不能据此恢复运行；`environment.txt` 是最后一次覆盖写。`state.json` 的 `workers=4` 是初始化遗留，不能覆盖历史启动命令与实际子进程证据。

## 3. 启动、结束、进度与并发

下表“首末进展”只是日志包络，不自动等于有效运行时间。序号对应 `commands.log` 行号；中间额外列出不在该文件中的启动尝试。

| 次序 | 启动 / 首末进展（2026，+08） | workers | 本次唯一完成 jobs / windows | execution.log 行 | 工具结束计时秒 / 状态 |
|---|---|---:|---:|---|---|
| 1 | 09-24 18:16:10；18:16:16.734—18:16:19.908 | 4 | 1 / 4 | 1–85 | 10.415713458 / exit 0 |
| 2 | 09-24 18:17:40；18:17:51.717—18:19:46.812 | 4 | 1 / 4 | 86–170 | 127.084100375 / exit 0；含 py_compile 包装 |
| 3 | 09-24 18:20:38；18:20:50.703—18:22:14.344 | 8 | 1 / 4 | 171–255 | 96.012022416 / exit 0 |
| 额外失败尝试 | 09-24 18:22:35.955，nohup 回显 PID 14458；18:23:01 检查无存活进程、无新进度 | 设定 8 | 无可归属新增作业 | 无 | 启动 shell 结束不等于后台 Python 完成；不计有效时间 |
| 4 | 09-24 18:23:58；18:24:05.303—09-25 12:36:58.861 | 8 | 1,994 / 12,960 | 256–274427 | **缺最终结束计时**；09-25 16:26:43 已无进程 |
| 5 | 09-25 16:28:04；16:28:17.706—10-07 20:37:13.332 | 8 | 2,995 / 26,947 | 274428–843311 | 151,457.683190125 / exit -1 |
| 6 | 10-08 10:55:26；11:03:00.829—17:16:29.236 | 8 | 806 / 7,259 | 843312–996558 | 22,916.396337333 / exit -1 |
| 7 | 10-08 22:41:20；22:41:28.920—10-09 14:02:16.097 | 8 | 178 / 1,609 | 996559–1030530 | 28,117.260324833 / exit 1 |
| 8 | 10-09 14:32:10；14:32:24.059—16:38:14.857 | 8 | 30 / 262 | 1030531–1036063 | 7,565.058228542 / exit 0 |

七个 `CommandExecution.duration` 的 S1 行号依次为 **10099、10146、10187、10460、10591、10707、10761**。额外 nohup 见 S1 10196–10197；主运行 #4 的 OS PID 为 14502，#5 为 25977，#6 为 7241，#7 为 9399，#8 为 62530。工具 `process_id`/session 编号不是 OS PID。

S1 10390、10415、10438、10677、10699、10750 的进程快照显示主进程及八个计算子进程；caffeinate 是保活进程，不能另算一次实验。现有证据支持这些主运行按先后续跑，没有发现两个 PS-A 主运行同时贡献完成作业；这不是完整进程审计。子进程每图重建，不能把主进程包络与八个子进程包络相加后称为墙钟。

#4 最后进展与确认消失之间的退出时刻未知；#5/#6/#7 的非零退出记录没有可信的终止原因，不把它们改写成“人工暂停”。#6 包装命令在约 10:54:33 开始，进入 runner 的 `commands.log` 到 10:55:26、首 checkpoint 到 11:03:00；这些准备/等待成本不能悄悄删除。

## 4. 重复执行、休眠与未知区间

**续跑成本已找到。** checkpoint 比无重复情况下的 `49,049 × 20 = 980,980` 多 27 条，即至少 **270 次已保存/已报告的重复 trial**。四次回退为 `180→10、20→10、20→10、50→10`，相邻日志行为 `(274427,274428)、(843311,843312)、(996558,996559)、(1030530,1030531)`。原 runner 在进入窗口遍历前重置 `active_window`（原脚本行 437–460），使未完成窗口的已记录 trial 被重做。未完成或尚未输出的并行 trial 可能更多。不要按唯一输出计数把这些成本减掉；本轮不修历史脚本。

**休眠证据显著缩小了空白，但不产生精确全程时钟。** 用 `/usr/bin/syslog -f ... -F raw` 读取 09-28、09-29、09-30、10-07、10-08、10-09 六个原 ASL；按 epoch Time + TimeNanoSec 排序，匹配真正的 `Entering Sleep state` 至下一个 Wake/DarkWake。保留未配对事件，不能强行补全。

- 09-30 **11:56:35.185179 → 10-07 20:37:00.493798**：低电量休眠，事件包络 **636,025.309 秒（176.674 小时）**。execution.log 对应长无进展间隔在行 843309–843310。该大段休眠内部排除；转换边缘与首末 checkpoint 的约 10 秒差仍分开。
- 10-09 **01:28:40.903045 → 09:01:42.774846**：低电量休眠，包络 **27,181.872 秒（7.551 小时）**，日志无进展间隔为行 1013563–1013564。仍有约 7 秒退出休眠前后记日志的边界差，不能把电源事件时间当精确 CPU 停止时刻。
- 可匹配的 **251 对**真实 Sleep/Wake 事件包络合计 **867,097.733 秒（240.860 小时）**，大量是 09-28 至 09-30 的短暂维护唤醒。此和数用于解释长空档，**不是可直接从日历跨度扣除的精确修正量**：存在未配对事件、转换延迟和跨源时钟误差。
- **反例：10-08 16:15:41 的 domain=Sleep 实际 Message 为 `Entering DarkWake state`**，其后 PS-A 一直计算到 17:16:29。若只看 Sleep 标签就扣至 22:17 的 FullWake，会错误删除至少约一小时计算。已明确排除此错误规则。
- 09-27 05:38:47 以后出现周期性停顿；最早保留的原电源日文件从 **09-28** 起。不能把 09-27 的每个约 15 分钟间隔自动归为休眠，亦不能计为连续活跃。09-25 中断、10-07 退出至次日续跑、10-08 傍晚、10-09 两次运行之间的剩余空档均不作为已证实计算。
- 日志存在 **6 次时间回退，共 1.218 秒**。时间核算必须合并重叠区间，不把每个正时间差简单相加；原记录保留不改。

## 5. 时间核算：实证、条件估算、不可得

### 5.1 部分进展支持的活跃墙钟区段

以密集 checkpoint、完成事件、历史调用和进程快照作为持续推进的证据，选择下面九个**部分区段**（包含通常的串行准备/I/O，不是 CPU 满载证明）：

`execution.log` 行对 `(1,85)、(86,170)、(171,255)、(256,274427)、(274428,836653)、(843312,996558)、(996559,1013550)、(1013564,1030530)、(1030531,1036063)`。

其中 #5 只取到 09-27 05:38:47.454；#7 分为截至 01:28:33.902 和自 09:01:46.034 起的两段，避免跨过休眠。没有依照 null 结果或统计阈值选择区段。

使用修复后的 **`psa_runtime_evidence.py`** 对真实日志哈希、精确行锚、时区和完成清单执行核查，结果为：

- 区间并集：**257,619.466 秒 = 71.560963 小时**；这些已选择主进程区段的时长和相同，没有重复累计并发墙钟。
- 名义 worker 时间：**2,060,482.652 worker-seconds = 572.356292 worker-hours**，前两段乘 4，其余乘 8。
- 状态仅为 `ARITHMETIC_CHECK_ONLY_INDEPENDENT_REVIEW_REQUIRED`。**71.56 小时是部分进展支持的 elapsed time，不是完整 `T_PS-A`、不是严格 CPU-active 下界。** 6,006 作业覆盖 CSV 不能证明这九段覆盖其全部计算。

### 5.2 历史工具 duration 与完整时间候选

七次可恢复工具结束计时之和为 **210,289.909917 秒 = 58.413864 小时**；缺 #4，因此不能称为全部进程运行时间之和。按历史配置相乘得到 **467.158133 名义 worker-hours**，仍不是 CPU-hours。

若**条件性假设**工具 duration 可当去休眠的进程 elapsed，并用 #4 的 `commands.log` 启动至最后 checkpoint 的 **65,580.861 秒**补其缺失计时，可拼得 **275,870.770917 秒 = 76.630770 小时**，名义 **612.893380 worker-hours**。这个混合估算有用，但**不予验收**：

1. #4 的最终退出/挂起时刻缺失；用末 checkpoint 代替退出是未验证假设。
2. S1 `started_at_ms/completed_at_ms` 与 `duration` 不同口径：#5 分别为 **1,051,773.507 秒 vs 151,457.683 秒**；#7 为 **55,256.554 秒 vs 28,117.260 秒**。后者差 **27,139.294 秒**，与电源休眠包络相差 **42.578 秒**。工具会话标记 CLI 0.153.4，但尚无该次实际计时实现及完整单调时钟校准证据；只能说与去休眠计时大体相符。
3. 首 checkpoint 之前的建图/读盘、pool 启停、阻塞等待、资源争用、部分窗口重做和未回收的在途 trial 没有全程分账。全部子进程的实际 CPU 时间/进程 elapsed 和未保存，瞬时 `ps %CPU` 无法积分恢复。

另作**纯敏感性算术**：在同一次调用内，把相邻日志间隔不超过 10/30/60/120/300/600 秒的区间取并集，分别为 **74.587873 / 75.770858 / 75.904653 / 75.948123 / 76.273272 / 77.172967 小时**。不同阈值改变结果，说明“遇到大 gap 就删”不能建立有效分母；这些不是置信区间、正式阈值或获准运行时间。

**结论：实际全部主/子进程 CPU-hours 不可得；完整可比较 `T_PS-A` 不可得。不得用 71.56、76.63、334.09 小时进展包络和数、两周日历跨度或末次约两小时替代分母。**

## 6. 硬件、依赖和效率可比性

这部分证据比 R5 时显著改善：

- S1 行 10073（09-24 18:15:17）记录 NumPy **2.5.3**、h5py **3.16.0**、NetworkX **3.6.1**、python-louvain/community **0.16**、SciPy **1.18.1**；行 10080 记录 Python **3.14.0**。与最终环境/现有解释器一致，但不是每阶段不可变依赖锁。
- S1 行 10154 记录逻辑/物理 CPU 均为 8；10160 是原 runner 从硬编码 4 workers 改为环境变量的历史修改，10167 起明确设置 8。不能反向假定前两次小试也是 8。
- 系统 `Python_2026-10-08-142259_*.diag` 的 PID **7241**与 S1 10547/10581 的 PS-A runner 相符，记录 **MacBookPro18,3、8 CPU、16 GB、macOS 15.7.4、arm64、Python 3.14.0**。当前机器为 Apple M1 Pro/8 CPU/16 GiB；支持同类、本地同机 lineage 的解释，但没有每次启动机器指纹与完整负载记录。
- 该诊断的通用 Duration 从 **10:01:48** 开始，早于 #6 启动，不能当作其运行时长；同文件 PID 7241 的采样段为 **11:10:13.550–14:22:37.331**。`disk writes / file-backed memory dirtied` 约 **8.59 GB** 提醒 I/O 成本，不能等同于最终磁盘占用或精确物理写入量。另一个 PID 1379 的 Python 报告未证明属于 PS-A，排除其计时。
- 历史 `ps` 的八个 worker 瞬时 CPU 使用率并非每个 100%：例如 S1 10415 约 45–49%/worker。是资源竞争/调度状态的采样证据，不能按八倍墙钟声称已测得 CPU-hours。未来最多八 worker 是并行度上限，不保证八倍加速。

未发现完整进程 accounting 文件；现存系统日志/诊断也没有覆盖所有阶段的进程树 CPU 积分。后续 G0 即使使用同机同版本，重连后的拓扑、Louvain 迭代成本、串行建图/连通检查和 I/O 均不同，PS-A 总用时只能作为预算参照，不能直接按 trial 数外推。

## 7. G0/T1 与正式 NC-0a 的资源判断

| 工作 | 固定工作量 | 当前判断 |
|---|---|---|
| 正式 NC-0a | 44,937,216 长链交换提议 + 16,000 BFS oracle 提议；128 链 | 独立绝对预算、外部监控/中止机制尚未获审；不启动 |
| G0 | 约 49,000 null 图、9,800,000 Louvain、1,797,712,000 交换提议 | `T_PS-A` 未验收，现有比较门槛无法判定通过 |
| T1 | 另 2,450,000 Louvain + 信号/相关矩阵重建 | 必须单列成本并在任何 G0 结果前决定是否授权 |

预注册 §6.1 的实质不变：G0 要求 `T_pred_G0 ≤ (5/3) T_PS-A`，T1 另要求 `T_pred_T1 ≤ T_PS-A`。若只是把未验收的 76.63 小时放进去，会制造约 127.72 / 76.63 小时的伪精确可用预算；**本审计不作这种批准**。这些资源倍率是止损规则，不是吞吐保证。

R5 微型 benchmark 仍是探索性：每个 N 仅一个 factor 图、2,000 次初始交换、5 次 Louvain、单进程；不含当前 runner 的完整逐接受审计、全部图族/链尾部、BFS oracle、并行竞争、checkpoint 与 I/O。不能以那三点证明 NC-0a 或 G0 可行，不能用其结果重调门槛。R4 自选种子的 4/16 试跑仍仅为已披露探索，不计正式验证。

存储也须区分最终产物与累计写入：G0 全部无向边按两端 uint32 原始存储约 **3.60 GB**，Q 数组 float64 约 **78.4 MB**，均未含容器/索引/日志；每次提议即使只落 16 字节，17.98 亿条也约 **28.76 GB**。这会侵蚀目前约 **31 GiB** 的空闲盘，更可能违反 `<70% baseline free disk`。相关矩阵需要流式处理，不能保留所有源图的稠密矩阵。当前 16 GiB RAM 的 80% 门槛约 12.8 GiB，必须测聚合峰值与共享页，不能把单进程 RSS 当整机峰值。

### 正式 NC-0a 的建议预算和中止机制（仅前瞻性建议）

当前可执行预算为**未批准，NO-GO**。若要把资源止损具体化，可另送独立评审一个明确的**损失上限候选**：整套含 oracle/准备/落盘 **48 小时墙钟、256 CPU-hours、最多 8 workers、进程树聚合内存 10 GiB、临时及失败产物合计 4 GiB、至少保留 20 GiB 空闲盘**；每个 case 12 小时、单 case oracle 30 分钟，且不得超过剩余总预算。数字只是限制愿意承担的资源损失，**不是本次实测吞吐预测，也没有证明足够完成**。基线空间不足或独立评审不接受时就不执行；不能为通过而扩大数字。

需要独立于计算进程的 watchdog：同时记录 UTC、包含休眠的总 elapsed、单调计时定义、父子进程 user/system CPU、聚合 RAM、临时空间及剩余预算；AC 供电、禁止系统休眠，检测到实际休眠或时钟异常即按预定规则中止/记录偏离。超墙钟/CPU/内存/磁盘/单 case 上限任一项，终止整个进程组，记录 interrupted/failed 与已消耗资源；不能只报告完成的有利用例。重跑必须另审并沿原 seed 从第零步开始，累计失败成本。

`nc0a_contract_runner.py` 目前只在每 1,000 提议（oracle 每 100）做软 wall 检查，单次图生成、BFS、指标调用可能跨过检查点；`nc0a_budget_preflight.py` 只验 schema。两者均已声明不能替代总体 launcher/批准。这不是新增“偷偷授权”漏洞，但缺少经审外部强制预算仍是执行阻断项。上述候选和任何替代 `T_PS-A` 的绝对预算方案，都必须先形成有日期的前瞻修订并独立审核，**本轮不改预注册规则**。

## 8. 实际修复与验证

1. 修复 `psa_runtime_evidence.py` 对 Python logging 的逗号毫秒格式支持。旧 regex 把 `18:16:16,734` 截为整秒，真实 19 ms 间隔会坍成零；增加 19 ms 与 ISO 小数/时区等价回归测试。没有降低哈希、锚点、worker 或独立复审要求。
2. 新增 `psa_history_inventory.py`：只读 commands/log/job 元数据，生成私有排序 CSV、逐文件 SHA、完成覆盖、重做/时间回退与 gap 敏感性；明确输出 `INVENTORY_ONLY_T_PSA_NOT_ESTABLISHED`，不自动把 gap 分类为空闲，不推断完整 active time，不读取 MAT。已有输出目录拒绝覆盖。
3. 新增两个小型 inventory 测试，并纳入已有 bounded-test CI；全部 **42 项单元测试通过**。真实 6,006-job 扫描及上述 `psa_runtime_evidence.py` 私有 manifest 均实际执行。
4. 本地 `governance_preflight.py --skip-write-report --strict-split-metadata` 通过（failures=0）；最终提交的 CI 状态在评论发布时记录。
5. **未运行**：正式 16×8×32E、完整 16,000 oracle 验证、真实 G0/T1、任何新的 RIKEN null、全量基准或 NC-0 身份面板。本轮单元测试不是正式验证。

复算私有 inventory：

```sh
uv run python Experiments/neuro_sleep_null_calibration/psa_history_inventory.py \
  /PRIVATE/original/phase2_population_size_scaling /PRIVATE/new-output --utc-offset +08:00
uv run python Experiments/neuro_sleep_null_calibration/psa_runtime_evidence.py \
  /PRIVATE/partial-active-manifest.json --output /PRIVATE/new-arithmetic-report.json
```

manifest 必须按第 5.1 节真实行锚构造，注明 **PARTIAL**，前两段 4 workers、其余 8；机器标识的历史不确定性保留。不可因为 CSV 有 6,006 个完成 ID 就将部分区间升格为全时段证据。

## 9. 剩余阻断与最小下一步

- **H2：仍未关闭。** 缺 #4 可审计的结束/挂起时刻，09-24 至 09-27 完整 sleep/awake/进程覆盖，工具 duration 的历史计时口径验证及关键差异解释，足以支持全程可比性的负载/环境记录。缺的是这些具体证据，不是再抄一个总小时数。没有全部进程 CPU 账本时，CPU-hours 必须保持 unknown。
- 优先保全已经找回的原始文件和私有派生清单；如能恢复旧系统备份/该版计时实现，独立复审后才决定历史基准能否接受。否则停止把现有历史分母作为可完成的前提，另行提出**前瞻绝对资源预算替代方案**；这是待审设计变更，不自动解除现门槛。
- 正式 NC-0a 前还须完成 H1 的完整验证器独立复审、逐 case/总体预算批准与强制监控、固定身份/种子/顺序/恢复政策。H3 的 120 图参考重建及其他 NC-0 门槛不在本轮解除。
- G0 与 T1 独立预算；必须在看到任何生物学 null 结果前记录 T1-GO 或 T1-NOT-AUTHORIZED-RESOURCE，不得看 G0 再决定是否做 T1。

**最终选择：H2 NO-GO。** 已恢复可信的部分区段和一个有用但未验收的约 76.63 小时条件估算；没有恢复可直接用于现有门槛的完整资源基准。即使将来 H2 PASS，也不自动批准正式 NC-0a。

## 10. SHA-256 证据账本

以下仅发布标识和哈希，不上传原始记录。系统电源导出及私有清单仍保留本地；原 ASL 为主要锚点。

| 证据文件 | SHA-256 |
|---|---|
| `P/checksums.txt` | `a94931e00a1519acb05345a0cedd4e01414fd07787b750f0b0e36d9ee0df6f18` |
| `P/commands.log` | `a852da536b4673998025c5c08373909bf82f63d112e8b46ee1855039b0da163a` |
| `P/data_inventory.txt` | `11f6eafb660d6d7d4696f3fe5c67d534b529659aead85259b321384e42ee39dd` |
| `P/environment.txt` | `3035a7394b7e12c4168e04019e11acbf0e62a71c812218d7f992fb321b2a6fa1` |
| `P/execution.log` | `4db0ecc7ca3ca7a32af9d59e745cc935a6db6819f9be8f84f64f6f5288759c55` |
| `P/louvain_seed_ledger.jsonl.gz` | `226e52fb4c2d510a5cf033305489b9e2ae197716c0eec6215c2368ebc3fd1ae6` |
| `P/plot_population_size_scaling.py` | `0307541631338ecd28544fe15d1a3dda7c91de54e8318fae435207ead323bec5` |
| `P/population_size_scaling.py` | `0e7af206456348b9eb91d5771d7cd4d18fe312ea4508b71a5772d7a47370b625` |
| `P/runner.stdout.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `P/state.json` | `c4cefcbb909534efaf92b252e4720a947f287e442704dc16d015b39d9262d03a` |
| `P/summarize_population_size_scaling.py` | `ae54e980a721948a63ae9ed57b5317d3ae8701105627b77ba48968a921700751` |
| `S1`（上述历史会话文件） | `d7d15ddf2204bcdf2b8cddb5c36f01cf7169882ac78de2089ffa34ff626ae3af` |
| `ASL/2026.09.28.asl` | `8265eaf2eb5a44492cd4627825074b9173733ca4929cae0251f3c2d094a24968` |
| `ASL/2026.09.29.asl` | `dd8e4953d20dff4a344c2936f18dc4240cf6ad45dbd3f2ca65a46b8d0d6fc71c` |
| `ASL/2026.09.30.asl` | `6354d8b81e7f44e5169c577b3a338838ac78d9ac7da25c29dc0ef7e3e41b5451` |
| `ASL/2026.10.07.asl` | `dd1bc1c8c35566fd5dccaa7304ae9eaee6fe43b003e238920daa27c629e7688e` |
| `ASL/2026.10.08.asl` | `474ef377455dd90b620085fb3ad573ecce44745eb492bb7e32dd5034af1b37af` |
| `ASL/2026.10.09.asl` | `9e926f03b90413c73f7e8bcfc62da669ab5e2ebbeb57f2fb80d4ef8bea957111` |
| `Python_2026-10-08-100150_HOST.diag` | `0c61986fb3eb2e8124f165f180fb12eb615b9762145b3ec84aa8a49646d8f92f` |
| `Python_2026-10-08-142259_HOST.diag` | `e7799c129e98befde04ac4e547ba3674c32329df007cf47a6f9fe0a5feab5f56` |
| `psa_history_inventory.py`（本轮代码/派生文件） | `7441a3d655d87d340e8f8f4713f5922c957b8323fdf3a1e0325787aecdfb4c98` |
| `psa_runtime_evidence.py`（本轮代码/派生文件） | `0bfe4dbe024d40de610d5e7c595bcead14e12b6c30650a413e0b66bafc98918a` |
| `power-history-raw.txt`（本轮代码/派生文件） | `edac3b7bf5e81c1d108d96cea48126836f7f145eeb9d4d67f6f47ed6ec68acea` |
| `partial-active-manifest.json`（本轮代码/派生文件） | `b2d5f1a7d3178721c20f6e57174c463ef78b5946054342e2d3d9837ed6511cc7` |
| `partial-active-audit.json`（本轮代码/派生文件） | `b1d200e98e1b57d6c974c4c290262646bc625cb0cb7486bf85d7f81e67705197` |
