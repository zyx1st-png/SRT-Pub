# P1 一键启动清单（E1/E2）

更新时间：2026-03-01

## 1) 环境与文件
- [ ] 拉取最新仓库并确认 commit
- [ ] 确认存在以下文件：
  - `E1_A7_PREREG_DRAFT.md`
  - `E2_A11_PREREG_DRAFT.md`
  - `P1_DATA_DICTIONARY_v1.md`
  - `P1_PILOT_RUNBOOK.md`
  - `P1_QC_CHECKLIST.md`

## 2) 任务脚本与参数
- [ ] 任务脚本版本冻结（记录 hash）
- [ ] E1 条件：low/high 顺序平衡
- [ ] E2 条件：low/med/high 顺序平衡
- [ ] 异常 trial 规则已写入脚本（RT阈值、漏答阈值）

## 3) 设备与数据路径
- [ ] 数据目录已创建：`data/p1_pilot/`
- [ ] 命名规则：`{task}_{participant_id}_{session_id}.csv`
- [ ] 元数据 JSON 自动落盘
- [ ] 可选生理设备（EDA/HRV）联调通过

## 4) 被试与伦理
- [ ] 知情同意文本确认
- [ ] 纳入/排除标准确认
- [ ] 退出机制可执行

## 5) 试运行
- [ ] 内部试跑 2 人
- [ ] 通过 `P1_QC_CHECKLIST.md` 最小门槛
- [ ] 输出 `pilot_qc_summary.md`

## 6) 开始采集
- [ ] E1 先到 N=20 做中期检查
- [ ] E2 先到 N=24 看阈值趋势
- [ ] 每日收尾更新一次 QC 标签（PASS/WARN/FAIL）
