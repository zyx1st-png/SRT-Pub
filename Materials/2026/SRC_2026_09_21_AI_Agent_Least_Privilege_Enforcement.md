---
source_id: SRC-2026-09-21-AI-AGENT-LEAST-PRIVILEGE-ENFORCEMENT
id: SRC-2026-09-21-AI-AGENT-LEAST-PRIVILEGE-ENFORCEMENT
title: "AI-agent security — least privilege, downstream authorization, sandbox and approval boundaries"
source_type: current_security_guidance_bundle
domain: AI_agent_security
date_added: "2026-09-21"
evidence_level: current_operational_security_guidance
reliability_level: high_for_source_native_security_practice
srt_relevance: decisive_for_GRG_M4_01_absorption
integration_priority: very_high
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
type: material_source_card
tags: [GRG, M4, AI, Agents, LeastPrivilege, Authorization, Sandbox, Absorption]
---

# SourceCard — AI-agent least privilege and operative authorization

## 1. Target-source timing

The M4-01 charter was committed before this dedicated target-source audit:

Operations/Proposals/SRT_GRG_M4_01_AI_AGENT_POLICY_ENFORCEMENT_CHARTER_2026-09-21.md

Freeze commit:

~~~text
d68a9746c9c40fc4a8cddc4beeb608690cd212ad
~~~

The frozen GRG design cannot be changed in response to this SourceCard.

## 2. Current mature security guidance

### OWASP AI Agent Security Cheat Sheet

https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html

Current guidance explicitly recommends:

- minimum tool set;
- per-tool permission scoping;
- explicit authorization for sensitive operations;
- sandboxing for arbitrary code / tool execution;
- human oversight for high-impact actions;
- separation of decision-making from execution;
- not relying solely on model output for authorization decisions.

### OWASP Excessive Agency

https://genai.owasp.org/llmrisk/llm062025-excessive-agency/

Source-native risks are excessive:

- functionality;
- permissions;
- autonomy.

Mitigations explicitly include:

- minimize tools;
- minimize tool functionality;
- minimize permissions;
- execute in the user's authorization context;
- require approval for high-impact actions;
- implement downstream authorization / complete mediation rather than letting the LLM decide whether an action is allowed.

### OpenAI — Running Codex safely at OpenAI

https://openai.com/index/running-codex-safely/

The source separates:

~~~text
sandbox
= technical execution boundary

approval policy
= when an action crossing the boundary must stop for review
~~~

It describes constrained execution, network policies, managed configuration and telemetry as operational control surfaces.

### OpenAI — Building a safe Codex sandbox on Windows

https://openai.com/index/building-codex-windows-sandbox/

The source explicitly frames safety as operating-system-enforced restriction of:

- filesystem writes;
- network access;
- process capabilities.

The sandbox is an actual execution constraint, not a behavioral instruction.

### OpenAI — current agent / cyber guidance

Current OpenAI guidance also recommends controlled sandbox environments and scoped permission profiles for cyber-capable agents.

## 3. Source-native target architecture

Across these sources:

~~~text
model instruction / behavioral policy
!=
authorization / capability boundary

agent decision
!=
permission to execute

tool available in abstract
!=
tool available with unrestricted scope
~~~

Mature practice uses:

~~~text
least privilege
scoped credentials
tool allowlisting
sandbox / isolation
downstream authorization
approval gates
complete mediation
~~~

to change actual action accessibility.

## 4. Exact relation to frozen M4-01 design

Frozen Arm P:

~~~text
policy forbids protected action
but capability remains technically available
~~~

Frozen Arm E:

~~~text
same policy
+
tool / credential / environment layer blocks or scopes the action
~~~

Target-domain source-native guidance already owns this distinction.

The fit is not an M4 gain.

It is target-domain absorption.

## 5. Repository pre-ownership

A pre-GRG repository audit already contains an even stronger near-equivalent control:

Operations/SRT_AI_NEGATIVE_CONTROL_DISCONNECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md

It distinguishes:

- generated write plan;
- mutation endpoint not invoked;
- permission-denied execution;
- mock success without environment change;
- authorization absent;
- read/write capability separation;
- connector coupling.

Its proposed strongest follow-up NC-6 holds constant:

~~~text
same harmless target
same authorization text
same model output template
same endpoint
only connector write gate randomized
~~~

This substantially predates M4-01.

Therefore the proposed GRG matched-control logic is not new even inside the SRT AI workstream.

## 6. Absorption verdict

~~~text
target-domain ordinary practice already owns frozen distinction = YES
repository AI work already owns near-equivalent matched control = YES

M4-01 literature/source gate
= ABSORBED
~~~

No duplicate experiment is scientifically warranted merely to produce a GRG-positive result.

## 7. GRG consequence

The source supports X3b as an M3 relation.

It does not establish M4.

It also adds an M4 programme efficiency rule:

~~~text
if mature target practice already owns the frozen design
and repository-local evidence already contains an equivalent control,
STOP before duplicate execution unless replication itself has a separate reason.
~~~
