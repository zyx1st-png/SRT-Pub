# Cover Letter — Artificial Life

Dear Editors of *Artificial Life*,

Please consider the manuscript **“Failure Is Not One-Dimensional: Terminality, Persistent Damage, and Recovery Architecture in Artificial Agents”** for publication as an Article in *Artificial Life*.

The manuscript fits the journal’s scope by using a synthetic software system to test a question about life-like organization: whether different ways of making failure consequential can be treated as interchangeable points on a common vulnerability or recoverability axis. The paper combines a controlled multiagent reinforcement-learning testbed with a methodological proposal for declaring the organizational unit, boundary, timescale, and recovery regime before comparing mortality, damage, repair, reset, or persistence across artificial systems.

The empirical programme is deliberately evidence-led. Experiment 1 compares matched survival-coupled REINFORCE agents whose energy depletion either terminates the current episode-token or restores the depleted agent. After withdrawal of a cooperation bonus, post-withdrawal mutual cooperation averages approximately 0.55 under terminal failure versus 0.04 under restoration across 30 matched seeds. The historical inference uses a two-sided two-sample label-permutation test; because the seeds are matched, the revised manuscript also reports a post-hoc paired sign-flip sensitivity analysis on the fixed committed outcomes. The two analyses give the same resampling-floor conclusion. The terminal-versus-restore separation also survives a zero-penalty ablation, a graded lives manipulation, a payoff sweep, and a frozen-policy common-state probe.

Two later follow-ups were designed after the Experiment 1 result was known and were separately preregistered in timestamped repository commits before their confirmatory implementation/execution. Experiment 2 holds episode length fixed while varying the persistence of non-terminal metabolic impairment; its preregistered positive gradient is not supported. Experiment 3 imposes fully reversible recovery latency through temporary forced-Rest periods; its preregistered positive hypothesis also fails, with the observed association instead strongly negative. These outcomes are retained in the main manuscript rather than treated as supplementary failures or reinterpreted post hoc as confirmatory support.

The resulting conceptual claim is intentionally narrower than the manuscript’s earlier formulation. The paper does not claim that mortality itself is novel, that precariousness was previously neglected, or that failure has a universal scalar effect on cooperation or life-likeness. Instead, the E1/E2/E3 sequence supports a structured **consequence architecture** view: terminality, persistent impairment, action restriction, recovery latency, opportunity loss, and continuity at token or controller-lineage level should be stated explicitly because superficially similar “more consequential” manipulations can generate qualitatively different learning outcomes. The paper also retains selective breadth, maintenance burden, and historical retention only as descriptive comparison questions; it does not claim that this study validates them as universal dimensions.

I believe this combination is well suited to *Artificial Life*. It uses a reproducible artificial system not merely to illustrate a preferred concept, but to expose a failed generalization and revise the conceptual framework accordingly. This directly connects synthetic experimentation with careful interpretation of life-like organization while keeping the reinforcement-learning mechanism, organizational level, and limits of generalization explicit.

The reproduction package contains the version-controlled experiment code, fixed result files, the timestamped follow-up preregistrations, statistical procedures, seed-level evidence, figure-generation scripts, and an audit that reproduces the Experiment 1 historical test alongside the paired-sensitivity analysis without retraining. Supplementary material will be supplied in a reviewer-safe form that does not depend on identity-revealing access permissions or logs.

In accordance with MIT Press policy, I also disclose the use of AI assistance. OpenAI ChatGPT (OpenAI; accessed September 2026, including GPT-5.6 Sol during the current revision) was used as an editorial and research-assistance tool during manuscript development, including literature discovery, structural critique, language revision, consistency checking, and audit support. It is not an author. I reviewed the resulting material and take full responsibility for the cited sources, experimental descriptions, analyses, claims, and submitted text. The reported numerical results derive from the committed experimental runs, not from generative-model output.

The manuscript is substantially unique and is not currently published or under review elsewhere.

Thank you for considering this work.

Sincerely,

Yuxin Zhang  
Independent Researcher  
zyx1st@gmail.com
