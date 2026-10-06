# OWF simulation

A small agent-based model that attacks the hand-in-to-credit rules (SPEC section 7). Python 3, no dependencies.

```
python3 sim/owf_sim.py
```

Each scenario prints every group's share of credit next to its share of the real value it delivered. A ratio of 1.0 is fair; above 1 means that group gains at everyone else's expense.

Agents: founders, honest builders who join over time, one very prolific builder, plus whichever attacker a scenario adds (splitters, padders, fake-work accounts, honest small contributors). The judge is noisy, flattens big work, and can be biased toward polish or against newcomers.

Re-run it whenever a default in the spec changes, and add a scenario for any new attack.

Results behind the v0.1 rules (40 runs each):

| Attack | Before the rule | After |
|---|---|---|
| Splitting across weeks | 1.23 | 1.06 (running total per need) |
| Splitting, flatter judge | 1.60 | 1.13 |
| Padding | 1.48 | 1.18 (length normalised) |
| Insiders lowball newcomers 20% | founders 1.18 | 1.04 (outside judges) |
| 20 fake-work accounts | honest builders 0.73–0.83 | depends on how much fake work is caught |
| "Below smallest reference earns 0" | honest small work 1.39 | 0.07, rejected |
