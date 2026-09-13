# TOOLS.md - SRT Local Notes

Run repository helpers from the repository root (the directory containing AGENTS.md and scripts/):

```bash
uv run python scripts/<helper>.py
```

Use the execution environment's supported tools. Browser automation is needed for page interaction; direct retrieval suffices for reading a page.

Active operations and governance documents live in `Operations/` and `Governance/`. Follow each workflow's output location; generated artifacts commonly use `data/`, `papers/` or `memory/`. `SRT_openclaw/` is historical, and a nested `SRT/` directory is not the runtime root.
