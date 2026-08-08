---
id: HOOK-NEURO-NEURAL23-EMBODIED-RHYTHMIC-ELIGIBILITY
patch_id: PATCH-NEURO-NEURAL23-EMBODIED-RHYTHMIC-ELIGIBILITY
type: integration_hook
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
domain: neuroscience_consciousness_interoception_brain_body_rhythms
status: active
integration_status: pending
landing_ledger:
  - target: "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md"
    state: pending
    blocked_by: "Neuroscience is a dormant/frozen layer; await the next compact-core synthesis pass. Preserve E_t(x) as bridge notation and keep phase-dependent eligibility distinct from canonical G_hat_theta and L0/L1 definitions."
  - target: "Neuroscience/SRT_Neuro_Predictions_Table.md"
    state: pending
    blocked_by: "Await the next prediction-table synthesis pass. Add only a preregisterable Phase x Stake differential prediction with arousal, decision-model, recovery, and null-outcome controls."
  - target: "Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md"
    state: pending
    target_status: planned
    blocked_by: "Await the planned neuroscience hardening synthesis; integrate after the transition-field/selection-architecture section and before downstream L1-to-L2 plasticity eligibility."
---

# NEURAL23 Integration Hook: Embodied Rhythmic Eligibility

## 1. Target documents

```text
Neuroscience/SRT_Neural_Mechanisms_CompactCore.md
Neuroscience/SRT_Neuro_Predictions_Table.md
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
```

## 2. Landing position

In the future neural-mechanisms synthesis, place after the composite `G_hat_theta` implementation sequence of competition, gain, gating, and stabilization, or immediately before that sequence if the rewrite distinguishes pre-gating eligibility from gating proper. In the hardening synthesis, place after N11's transition-field framing and before N10-style post-event plasticity eligibility. In the prediction table, add a dedicated brain-body rhythmic-coupling row rather than folding the claim into pain, anxiety, anesthesia, or dreaming.

## 3. Suggested native paragraph

> Accessible neural candidates do not face identical selection conditions at every moment. Cardiac, respiratory, gastric, and cross-system rhythms can modulate excitability, evidence accumulation, timing, and coordination before a percept, decision, or action becomes stably manifest. A useful implementation distinction is therefore between a candidate's selection weight and its momentary selection opportunity. The latter can vary continuously with embodied state without becoming a new canonical layer between `L_0` and `L_1`. This permits relatively discrete anchoring events to emerge from continuously changing constraints while avoiding the fiction of a single anatomical selector or universal neural collapse instant.

## 4. Suggested bridge box

```text
L0_accessible
-> momentary selection eligibility E_t(x)
-> competition / gain / gating / stabilization
-> L1
-> post-event plasticity eligibility
-> L2 write-back
```

Guardrail:

```text
eligibility to become current reality
!=
eligibility to enter history
```

## 5. Suggested mapping table

| Layer | Question | Candidate measure | SRT use | Guardrail |
|---|---|---|---|---|
| bodily phase | what temporal state is the organism in? | ECG phase, respiratory phase, gastric phase | input to momentary eligibility model | phase is not selection |
| coupling | how are bodily and neural rhythms related? | HEP, phase locking, cross-frequency coupling, MI | coordination / implementation proxy | coupling is not `d` or `Psi_f` |
| candidate eligibility | how favorable is this moment for candidate `x`? | phase-conditioned decision parameters / access probability | P3 bridge `E_t(x)` | bridge notation, not canonical variable |
| anchoring | what becomes stable/current? | behavior, report, persistent neural availability | `L1`-facing outcome | access is not subjecthood |
| recovery / future transition | what does the episode cost and constrain? | recovery half-life, rigidity, later adaptation | `Psi_f`-proxy / future-selectability test | cost proxy is not canonical `Psi_f` |

## 6. Suggested prediction row

```text
Phenomenon:
brain-body rhythmic coupling during decision, stress, and conscious access

Mainstream variables:
interoceptive precision, arousal, autonomic regulation, predictive processing,
drift-diffusion parameters, network physiology

SRT added variable:
momentary selection eligibility + stake-sensitive gating + future-transition consequences

Prediction:
with physical stimulus properties controlled, bodily phase effects on decision/access
should interact with manipulated consequence-bearing stake, and the interaction should
predict recovery or later transition behavior beyond arousal and standard decision controls.

Failure condition:
if ordinary arousal/interoception/decision variables fully explain the effect and the
stake-sensitive or future-selectability terms add no stable out-of-sample increment,
narrow or remove the SRT-specific bridge.
```

## 7. Do not include

- `E_t(x)` in `_SRT_SYMBOL_TABLE.md` or canonical files without a separate hardening decision;
- physiological synchrony as a cross-domain SRT primitive;
- language reviving `selective resynchronization` after its ML NO-GO;
- HEP amplitude or complexity as consciousness itself;
- brain-body coupling as canonical `d`;
- coupling magnitude, stress, or arousal as canonical `Psi_f`;
- the authors' optimal-coupling conjecture as a proven universal optimum;
- an organism as the derived bearer unit solely because body coupling exists;
- interpersonal synchrony as evidence of a collective subject;
- a fixed anatomical location for `G_hat_theta`.

## 8. Future synthesis target

Compress NEURAL23 into:

1. one paragraph on momentary embodied eligibility;
2. one two-gate diagram separating selection eligibility from plasticity eligibility;
3. one synchrony/coordination/selection guardrail;
4. one `Phase x Stake` prediction with explicit null conditions;
5. one bearer-unit sentence stating that organism-level coupling raises but does not settle the individuation question.

Future version target:

```text
Neuroscience/SRT_Neuroscience_Hardening_N1_N13_v0_2.md
```

Source patch:

```text
Neuroscience/patches/SRT_Neuro_NEURAL23_Embodied_Rhythmic_Eligibility_v0_1.md
```
