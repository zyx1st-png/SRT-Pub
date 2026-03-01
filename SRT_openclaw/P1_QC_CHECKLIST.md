# P1 数据质量检查清单（QC）

更新时间：2026-03-01
范围：E1/E2

## A. 结构完整性
- [ ] 必备字段齐全（见 `P1_DATA_DICTIONARY_v1.md`）
- [ ] participant_id / session_id 非空
- [ ] 条件标签合法（E1: low/high; E2: low/med/high）

## B. 行为数据质量
- [ ] RT 异常值比例 < 10%
- [ ] 连续漏答异常区段已标记
- [ ] 任务完成率 > 90%

## C. 主观/协变量完整性
- [ ] baseline_anxiety 完整率 > 95%
- [ ] subjective_load_0_10 完整率 > 95%
- [ ] sleep_hours/caffeine_mg 缺失率可接受（<20%）

## D. 可选生理质量（如采集）
- [ ] EDA/HRV 信号可用率 > 80%
- [ ] 设备异常日志已附加

## E. 结果可用性门槛
- [ ] E1 可计算 tradeoff_index
- [ ] E2 可计算 instability_index
- [ ] 每位被试至少保留 70% 有效 trial

## F. 结论标签
- PASS：全部核心门槛通过
- WARN：非核心门槛有缺口，但可分析
- FAIL：核心门槛不通过，需重采或剔除
