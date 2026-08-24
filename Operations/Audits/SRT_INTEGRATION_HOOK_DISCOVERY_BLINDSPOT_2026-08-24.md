---
id: SRT-INTEGRATION-HOOK-DISCOVERY-BLINDSPOT-2026-08-24
type: audit_note
status: active
layer: operations
epistemic_layer: os
claim_mode: governance
canonical: false
---

# IntegrationHook discovery blind spot — 2026-08-24

## Finding

`scripts/check_hooks.py` currently discovers integration hooks only through the filename glob:

```text
*_Integration_Hook.md
```

A Markdown file under a `hooks/` directory can therefore declare:

```yaml
type: integration_hook
```

while escaping ledger validation if its filename carries a suffix after `Integration_Hook`, for example:

```text
Example_Integration_Hook_2026-08-24.md
```

This is a discovery-contract mismatch: the governance contract is semantic (`type: integration_hook`) while the checker discovery rule is filename-only.

## Important scope correction

Do **not** solve this by validating every filename containing `Hook`. Recent dated files such as research/theory hooks are legitimate non-IntegrationHook types and do not owe an IntegrationHook landing ledger merely because `Hook` appears in the filename.

The safe target is:

```text
all legacy filename-matched IntegrationHooks
+
all files under */hooks/ whose frontmatter type == integration_hook
```

## Proposed repair

1. Keep legacy filename discovery for backward compatibility.
2. Scan Markdown files directly under `hooks/` directories and additionally include any file whose frontmatter declares `type: integration_hook`.
3. Add fixture coverage showing:
   - a dated-suffix `type: integration_hook` is discovered;
   - a dated `type: research_hook` is not pulled into IntegrationHook ledger validation.

This repair is governance-only and should remain separate from material PR #852.
