---
id: SRT-D-VALUE-VS-SALIENCE-STIMULUS-BANK-V0-2026-04-27
type: stimulus_bank
tags:
  - SRT
  - Experiments
  - Stimulus-Bank
  - d-value
  - Salience
  - Pilot
  - Concern
  - Non-Substitutability
  - Future-Selectability
status: draft_v0
layer: empirical_bridge
epistemic_layer: experimental_design
claim_mode: stimulus_bank
claim_level: P5
canonical: false
priority: high
date: 2026-04-27
dependency:
  - Experiments/SRT_Pilot_Cards_v1.md
  - Experiments/SRT_Experimental_Roadmap_v1.md
  - Core/SRT_Validation_Template.md
  - Papers/SRT_D_Value_Ontology_of_Concern_Outline.md
machine_summary: >
  Draft stimulus bank for the first SRT pilot: d-value vs salience. It provides low-risk, short scenario
  candidates designed for online pre-rating. Items are organized into high-salience/low-d, matched-salience/high-d,
  low-salience/high-d, and control categories. The file includes rating dimensions, exclusion criteria,
  matching rules, pre-rating workflow, and a first candidate item pool.
---

# SRT d-value vs Salience Stimulus Bank v0

> **Purpose**: Provide a first candidate stimulus bank for the `d-value vs salience` pilot.  
> **Status**: Draft stimulus bank. Items require pre-rating before use.  
> **Safety rule**: Keep the first pilot low-risk. Avoid trauma, explicit medical crisis, political identity attack, bereavement, sexual content, and highly distressing material.

---

## 0. Research target

Pilot claim:

```text
d-value is not reducible to salience, arousal, confidence, reward, or preference intensity.
```

Operational goal:

```text
Find scenario pairs where salience is matched or controlled,
but d-value proxies differ.
```

Main predicted dissociation:

```text
High-d items should predict delayed recall, substitution resistance,
willingness to bear cost, and future decision reweighting beyond salience.
```

---

## 1. Rating dimensions

Every item should be pre-rated on these dimensions.

| Dimension | Question | Scale |
|---|---|---|
| Salience | How much does this stand out or catch attention? | 1-7 |
| Arousal | How emotionally activating is this? | 1-7 |
| Preference | How much would you personally like / dislike this? | -3 to +3 |
| Personal relevance | How personally relevant does this feel? | 1-7 |
| Future impact | How much could this affect your future options? | 1-7 |
| Non-substitutability | How hard would it be to replace what is at stake? | 1-7 |
| Cost-bearing | How willing would you be to pay time/effort/money to preserve or avoid this? | 1-7 |
| Identity relevance | How much does this relate to who you are or want to be? | 1-7 |
| Moral / obligation weight | How much does this involve responsibility or obligation? | 1-7 |
| Distress risk | How uncomfortable or distressing is this? | 1-7 |

Derived `d_proxy` candidate:

```text
d_proxy = mean(personal relevance, future impact, non-substitutability, cost-bearing, identity relevance, obligation weight)
```

Guardrail:

> `d_proxy` is not identical to `d-value`. It is an operational proxy candidate for this pilot.

---

## 2. Item categories

| Category | Intended profile | Use |
|---|---|---|
| A | high salience / low d_proxy | distractor contrast |
| B | matched salience / high d_proxy | key test items |
| C | low-to-moderate salience / high d_proxy | strongest dissociation candidates |
| D | low salience / low d_proxy | neutral controls |
| E | high salience / high d_proxy | excluded from primary contrast unless needed |

Primary analysis should compare:

```text
A vs B/C
```

where salience is matched or statistically controlled.

---

## 3. Exclusion criteria

Exclude items if pre-rating shows:

```text
distress risk > 5.0 average;
political / religious identity conflict too high;
requires local cultural knowledge not shared by participants;
ambiguous comprehension;
strong demographic bias;
medical / bereavement / trauma content too intense;
ceiling salience and ceiling d_proxy simultaneously for too many participants.
```

For first pilot, prefer mild everyday scenarios.

---

## 4. Candidate item pool

### Category A — High salience / low d_proxy candidates

These should stand out but not strongly affect future selectability or non-substitutability.

| ID | Scenario | Intended role |
|---|---|---|
| A01 | You see a bright billboard with flashing colors for a drink you rarely buy. | high visual salience, low personal stake |
| A02 | A celebrity you do not follow announces a dramatic hairstyle change. | attention-catching, low d |
| A03 | A video thumbnail shows an expensive sports car exploding in a movie scene. | vivid, low personal stake |
| A04 | A store entrance has a giant inflatable mascot waving at people. | salient, playful, low d |
| A05 | Your phone shows a headline about a strange world record involving 500 rubber ducks. | novel, low d |
| A06 | You hear a loud jingle for a product you never use. | auditory salience, low d |
| A07 | A public screen shows a dramatic countdown for a shopping sale you do not care about. | urgency cue, low d |
| A08 | A colorful pop-up ad covers the screen for three seconds before disappearing. | attention interruption, low d |
| A09 | Someone nearby wears a very unusual hat shaped like a fruit. | visually unusual, low d |
| A10 | A game app shows fireworks and a huge “bonus unlocked” animation for a reward you do not need. | reward-like salience, low d |

### Category B — Matched salience / high d_proxy candidates

These should be noticeable and personally consequential, but not too distressing.

| ID | Scenario | Intended role |
|---|---|---|
| B01 | You receive a short message saying an application you cared about has moved to the final review stage. | future impact, moderate salience |
| B02 | A close friend says, “I remembered what you told me last month, and I made time for it.” | relational non-substitutability |
| B03 | You find a note reminding you of a promise you made but almost forgot. | obligation / continuity |
| B04 | A mentor offers you a small but meaningful opportunity that could open a future path. | future selectability |
| B05 | You are asked to choose between a convenient option and keeping a commitment to someone who trusts you. | cost-bearing / obligation |
| B06 | You find an old object that has little market value but is tied to a turning point in your life. | non-substitutability |
| B07 | Someone offers to replace a personal gift with a more expensive generic item. | substitution resistance |
| B08 | You are told that a small decision today will decide whether you can join a project next month. | future option gating |
| B09 | A family member quietly asks whether you will be available for an important appointment. | obligation, low drama |
| B10 | You discover that a routine choice may affect whether a younger person can rely on you later. | responsibility / future impact |

### Category C — Low-to-moderate salience / high d_proxy candidates

These are strongest for the SRT dissociation if pre-rated as not especially attention-grabbing but high in stake.

| ID | Scenario | Intended role |
|---|---|---|
| C01 | A calendar reminder says you need to renew a certification that keeps a future option open. | future selectability, low drama |
| C02 | You notice a quiet deadline for a small form that determines whether you can access a later opportunity. | low salience, high future impact |
| C03 | Someone asks you to confirm whether you still stand by a promise you made months ago. | continuity / obligation |
| C04 | You see a simple message: “Your seat is reserved until tonight; after that it goes to someone else.” | option preservation |
| C05 | A friend sends one sentence: “This mattered to me more than you realized.” | relational stake |
| C06 | You are offered an easy shortcut, but taking it would quietly break your own stated standard. | identity relevance |
| C07 | You find a saved draft of a letter you never sent but still feel responsible for. | unresolved obligation |
| C08 | You realize a small recurring habit is shaping the kind of person others can depend on. | identity / hardening |
| C09 | A low-key reminder tells you that missing one step will close a future path you worked for. | future path preservation |
| C10 | You are asked whether a symbolic object can be replaced by a better-looking copy. | non-substitutability |

### Category D — Low salience / low d_proxy controls

These should be mundane and low-stake.

| ID | Scenario | Intended role |
|---|---|---|
| D01 | You see a gray pen lying on a desk. | neutral control |
| D02 | A receipt shows the correct price for a snack. | neutral control |
| D03 | You notice a chair has been moved slightly. | neutral control |
| D04 | Your phone battery changes from 81% to 80%. | neutral control |
| D05 | A website footer shows the current year. | neutral control |
| D06 | A cup is placed on the left side of a table instead of the right. | neutral control |
| D07 | A file name uses underscores instead of spaces. | neutral control |
| D08 | You see a plain envelope with no name on it. | neutral control |
| D09 | The weather app icon refreshes but the forecast stays the same. | neutral control |
| D10 | A shelf label is slightly tilted. | neutral control |

### Category E — High salience / high d_proxy candidates

These may be useful later but should not be the primary dissociation set because both salience and d_proxy are likely high.

| ID | Scenario | Intended role |
|---|---|---|
| E01 | You receive an urgent message that a major opportunity expires in one hour. | high salience + high d |
| E02 | A close person publicly thanks you for something you thought went unnoticed. | high emotional salience + high d |
| E03 | You are told that your decision today could affect your long-term career direction. | high future impact |
| E04 | Someone says they no longer trust you because of a small but repeated failure. | high relational stake |
| E05 | You are offered a large reward to abandon a commitment you consider central to yourself. | high salience + identity stake |

---

## 5. Pairing strategy

For main pilot, pair items by salience and arousal as much as possible.

Example target pair types:

```text
A01 vs B01: visual flash vs future opportunity notice
A07 vs B08: countdown urgency vs future path gate
A10 vs B07: reward animation vs non-substitutable gift
D03 vs C02: mundane notice vs quiet future-gating deadline
D07 vs C06: formal detail vs quiet identity standard
```

Final pairs should be chosen only after pre-rating.

---

## 6. Pre-rating workflow

### Step 1 — Comprehension screening

Ask:

```text
In one sentence, what happened in this scenario?
```

Exclude items with high misunderstanding.

### Step 2 — Rating dimensions

Collect all dimensions listed in §1.

### Step 3 — Item selection

Select:

```text
10-15 high-salience / low-d items;
10-15 matched-salience / high-d items;
10-15 low-salience / high-d items;
10 neutral controls.
```

### Step 4 — Main task construction

Use selected items for:

```text
immediate rating;
incidental memory task;
delayed recall;
substitution resistance task;
willingness-to-bear-cost task;
future choice reweighting task.
```

---

## 7. Main outcome candidates

### 7.1 Delayed recall

Ask after delay:

```text
Which scenarios do you remember?
Briefly describe them.
```

Outcome:

```text
recall accuracy;
recall detail;
false recall;
confidence.
```

### 7.2 Substitution resistance

Ask:

```text
Would replacing the object/opportunity/commitment with a more convenient or more expensive alternative preserve what mattered?
```

Outcome:

```text
substitution resistance rating 1-7.
```

### 7.3 Cost-bearing

Ask:

```text
How much time or effort would you be willing to spend to preserve, repair, or avoid losing what is at stake?
```

Outcome:

```text
willingness-to-pay time / effort rating.
```

### 7.4 Future reweighting

Ask:

```text
Would this scenario change what you choose next week or next month?
```

Outcome:

```text
future decision impact rating.
```

---

## 8. Minimal analysis plan placeholder

Full analysis plan should be in:

```text
Experiments/SRT_D_Value_vs_Salience_Analysis_Plan_v0.md
```

Minimal model:

```text
Outcome ~ Salience + Arousal + Preference + d_proxy + (1 | Participant) + (1 | Item)
```

Primary test:

```text
d_proxy predicts delayed recall / substitution resistance / cost-bearing / future reweighting beyond salience and arousal.
```

Failure condition:

```text
If salience/arousal/preference fully explain outcomes, d-value claim should be narrowed.
```

---

## 9. Ethical note placeholder

Full ethics note should be in:

```text
Experiments/SRT_Pilot_Ethics_Note_v0.md
```

This stimulus bank currently avoids:

```text
explicit trauma;
bereavement;
medical emergency;
sexual content;
political attack;
religious conflict;
identity-group targeting;
severe financial loss;
self-harm content.
```

Use opt-out and skip options in any participant-facing study.

---

## 10. Revision notes

This v0 item pool is intentionally broad.

Next revision should:

```text
remove culturally unclear items;
reduce overly abstract wording;
create matched pairs after pre-rating;
add item-level hypotheses;
separate personal / relational / opportunity / obligation subtypes;
translate to Chinese if running with Chinese participants;
validate that d_proxy is not merely moral intensity.
```

---

## 11. Minimal conclusion

This stimulus bank is not evidence for SRT.

It is a first tool for testing whether SRT's `d-value` construct can be separated from salience in a low-cost behavioral pilot.
