# TOOLS.md - SRT Local Notes

This file keeps SRT-specific tool conventions local to the project so sibling OpenClaw/ClawX projects do not overwrite them.

## ClawX Tool Notes

### uv (Python)

- Run project scripts from `SRT/` with `uv run python <script>`.
- If a helper script lives one level up, run it from `SRT/` as `uv run python ../scripts/<script>.py`.
- Prefer `uv pip install <package>` if this project needs a package-level install step.

### Browser

- Use the browser automation flow when page interaction is required: start -> snapshot -> act.
- For simple link-opening tasks, prefer the platform's external-open behavior instead of full browser automation.

### SRT Paths

- Canonical ops docs live in `Operations/`.
- Canonical governance docs live in `Governance/`.
- Generated artifacts normally stay in `data/`, `papers/`, or `memory/`.
- Historical `SRT_openclaw/` references are legacy only and should not be used as live paths.
