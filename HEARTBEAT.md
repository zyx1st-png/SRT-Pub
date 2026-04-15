# HEARTBEAT.md

SRT heartbeat behavior is project-local.

## Checklist

1. Read `STATUS.md`.
2. Read `Operations/_SRT_OPERATIONS_SCHEDULE.md`.
3. Use `memory/heartbeat-state.json` to avoid duplicate work.
4. If Pipeline 3 has not run for about 22 hours, run `信号采集`.
5. If Pipeline 6 has not run for about 22 hours, run `内审`.
6. Around 08:00 Asia/Shanghai, consider `选题`.

## Quiet Hours

- 23:00-08:00 Asia/Shanghai: stay quiet unless something is urgent.

## Fallback

- If nothing needs attention, reply `HEARTBEAT_OK`.
