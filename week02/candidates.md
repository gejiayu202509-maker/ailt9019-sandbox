# Week 2 project candidate shortlist

These are discussion-ready directions, not final team commitments. Each is
small enough to evaluate this semester and has an explicit safety boundary.

## 1. Quant: Backtest Integrity Checker

**Primary users and single task:** Student quantitative researchers upload a
strategy summary and trade log; the tool identifies common reasons a backtest
may be misleading and produces an evidence-linked review checklist.

**Current pain and motivation:** A strategy can look profitable while hiding
look-ahead bias, leakage, insufficient trades, unrealistic costs, or one-period
dependence. Beginners often inspect headline return instead of test validity.

**Dataset:** Self-curated synthetic backtest reports with deliberately seeded
errors, plus permissively licensed daily market data from a documented public
source. No brokerage or private account data is required.

**Pipeline:** Parse report -> calculate integrity checks -> attach evidence ->
classify PASS/WARN/FAIL -> generate a compact review report.

**Does not:** Recommend securities, predict returns, place trades, connect to a
brokerage account, or claim that a passing backtest will remain profitable.

**Evaluation:** A labelled suite of clean and flawed fixtures. Measure seeded
issue recall, false-warning rate, evidence correctness, and safe handling of
missing or malformed data. A minimum viable target is detecting at least 8 of
10 seeded issues without inventing unavailable facts.

**Difficulty:** Medium. Strong fit with Jiayu's existing quantitative workflow;
main challenge is defining rigorous checks rather than building the interface.

## 2. Web3: Transaction Intent Explainer

**Primary users and single task:** People learning Web3 paste a decoded,
unsigned EVM transaction; the tool explains the intended token movements and
permissions in plain language before the user makes an independent decision.

**Current pain and motivation:** Wallet prompts expose contract addresses and
method calls that beginners cannot easily map to practical consequences,
especially unlimited approvals and operator permissions.

**Dataset:** Public EVM ABI specifications and self-curated, labelled transaction
fixtures. Only public chain data and unsigned examples are used.

**Pipeline:** Validate input -> decode method and parameters -> map known token
actions -> highlight high-impact permissions -> cite the decoded fields ->
return UNKNOWN when evidence is insufficient.

**Does not:** Request or store keys or seed phrases, sign or broadcast
transactions, label a contract as safe, provide investment advice, or guarantee
that an explanation captures all contract behaviour.

**Evaluation:** Labelled fixtures for transfer, approval, revoke, unknown ABI,
malformed input, and suspicious permission scope. Measure field-level decoding
accuracy, citation match, refusal on undecodable input, and zero secret-key
collection.

**Difficulty:** Medium to challenging. Distinctive topic with an excellent
safety story, but ABI coverage must stay deliberately narrow.

## 3. Robotics/AI: Simulated Robot Task Safety Gate

**Primary users and single task:** Robotics students submit a proposed task plan
and a small simulated workspace description; the tool checks the plan against
explicit safety constraints before any execution.

**Current pain and motivation:** Natural-language or agent-generated plans can
contain unsupported actions, forbidden zones, unknown objects, or payloads over
a robot's declared limit. These faults should be caught before a physical run.

**Dataset:** Self-curated JSON scenarios containing simulated objects, zones,
payload limits, plans, and expected verdicts. No live sensor or personal data is
used.

**Pipeline:** Load scenario -> validate schema -> inspect every action against
the environment and policy -> return PASS/FAIL with step-level evidence.

**Does not:** Control physical hardware, infer safety beyond the supplied rules,
replace a qualified operator, or claim that a passing simulated plan is safe in
the real world.

**Evaluation:** Labelled safe and unsafe plans covering forbidden zones,
unsupported actions, unknown objects, overload, malformed input, and a valid
baseline. The minimum viable target is the correct verdict and cited step for
every supplied fixture.

**Difficulty:** Medium. Best current prototype choice: it demonstrates agent
evaluation and safe failure while remaining deterministic and testable.

## Recommendation for team discussion

Start the discussion with the Robotics/AI candidate because its scope,
evaluation, and explicit refusal boundary are strongest. Keep Quant as the best
domain-fit alternative and Web3 as the most distinctive alternative. Choose
only after the team confirms interest, data permission, and a workload split.
