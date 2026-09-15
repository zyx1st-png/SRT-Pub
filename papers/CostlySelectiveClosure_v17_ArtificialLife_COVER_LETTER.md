# Cover Letter — Artificial Life

Dear Editors of *Artificial Life*,

Please consider the manuscript **“Costly Selective Closure: An Operational Heuristic for Life-Likeness in Artificial Systems”** for publication as an Article in *Artificial Life*.

The manuscript fits the journal’s scope by combining a conceptual contribution about life-like organization with a controlled artificial-life experiment. It proposes costly selective closure (CSC) as a profile protocol organized around four maintenance-and-consequence questions—selective breadth, maintenance burden, historical retention, and irreversible vulnerability—indexed to an explicitly declared organizational unit, boundary, timescale, and recovery regime. The framework is intentionally non-scalar and does not claim to define life or replace established work on autopoiesis, autonomy, precariousness, dimensional accounts of life, or active inference.

The empirical contribution isolates one narrow CSC-relevant variable in a two-agent reinforcement-learning survival environment. The primary comparison holds the programmed reward function, observation specification, energy dynamics, policy architecture, training schedule, and paired seeds fixed while changing the depletion transition from termination of the current episode-token to cheap restoration. After withdrawal of an explicit cooperation incentive, mutual cooperation averages 0.55 under terminal failure versus 0.04 under cheap restoration across 30 paired seeds. The result survives a zero-penalty ablation, a graded lives manipulation, a payoff sweep, and a frozen-policy common-state probe. The paper treats the standard reinforcement-learning explanation—termination changes the return structure—as the mechanism rather than as an alternative to be denied.

We believe this combination is well suited to *Artificial Life*: the manuscript uses a synthetic system to make a question about life-like organization experimentally manipulable, while keeping the distinction between the controlled causal result and the broader life-likeness interpretation explicit. The reproduction package contains the version-controlled experiment code, fixed result files, statistical procedures, seeds, figure-generation scripts, and a locked environment for exact reproduction of the common-state probe. Supplementary material will be supplied with the submission in a form that does not expose reviewer identity through access permissions or logs.

In accordance with MIT Press policy, I also disclose the use of AI assistance. OpenAI ChatGPT (OpenAI; accessed September 2026, including GPT-5.6 Sol during the current revision) was used as an editorial and research-assistance tool during manuscript development, including literature discovery, structural critique, language revision, and consistency checking. It is not an author. I reviewed the resulting material and take full responsibility for the cited sources, experimental descriptions, analyses, claims, and submitted text. The reported numerical results derive from the committed experimental runs, not from generative-model output.

The manuscript is substantially unique and is not currently published or under review elsewhere.

Thank you for considering this work.

Sincerely,

Yuxin Zhang  
Independent Researcher  
zyx1st@gmail.com
