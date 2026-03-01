# P1 数据字典 v1（E1/E2）

更新时间：2026-03-01
范围：E1(A7)、E2(A11)

## 通用字段
- `participant_id`：字符串，匿名ID
- `session_id`：字符串，会话编号
- `task`：枚举（E1/E2）
- `condition`：E1=low/high；E2=low/med/high
- `trial_id`：整数
- `timestamp`：ISO时间

## 行为字段
- `rt_ms`：反应时（毫秒）
- `correct`：0/1
- `error_burst_flag`：0/1（连续错误段标记）
- `recovery_latency_ms`：恢复到稳定表现所需时间

## 协变量字段
- `sleep_hours`：前一晚睡眠时长
- `caffeine_mg`：实验前咖啡因摄入估计
- `baseline_anxiety`：基线焦虑评分
- `subjective_load_0_10`：主观负担评分

## 可选生理字段
- `eda_peak`：皮电峰值
- `hrv_rmssd`：HRV-RMSSD

## 清洗规则（预设）
1. `rt_ms < 150` 或 `rt_ms > mean+3SD` 标记异常并剔除。
2. 连续漏答超过预设阈值的区段剔除。
3. 缺失值不插补，按 trial/区段剔除并记录比例。

## 派生指标
- `tradeoff_index`（E1）：标准化 RT 与 Accuracy 的组合指数
- `instability_index`（E2）：错误爆发率 + 恢复时间加权指数

## 缺失与异常记录
- `missing_reason`：设备故障/中断/拒答/其他
- `qc_flag`：pass/warn/fail

## 导出格式
- 主表：CSV（UTF-8）
- 元数据：JSON（字段说明与单位）
