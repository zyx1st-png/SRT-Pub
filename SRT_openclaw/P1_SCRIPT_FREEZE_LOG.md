# P1 脚本冻结记录（T0）

更新时间：2026-03-01

- 冻结范围：E1(A7), E2(A11) 执行相关脚本与配置
- 冻结原则：
  1) 进入采集后不得修改任务逻辑
  2) 如必须修改，需新增版本号并在日志说明原因

## 冻结版本
- Repo commit: `b77616c`
- E1 task script: `<TO_FILL_PATH_AND_HASH>`
- E2 task script: `<TO_FILL_PATH_AND_HASH>`
- 参数文件: `<TO_FILL_PATH_AND_HASH>`

## 变更门禁
- 若采集中途变更：必须触发 `THEORY_CHANGE_GATE.md` 和 `DIALOGUE_TRIGGER_POLICY.md` 相关流程。
