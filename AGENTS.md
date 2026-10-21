# Open Work Framework: rules for every agent

This file is for any AI agent working in this repo: Claude Code, Codex, Gemini CLI, Cursor, Copilot or anything else. `CLAUDE.md` and `GEMINI.md` only point here, so keep project rules in this file and nowhere else.

## What this repo is

OWF (Open Work Framework) is how work happens in the open, in any setting: public needs, open pick-up, contributions with evidence, attribution, visible acceptance and an append-only record. It holds no rewards: each setting plugs in its own. TOPC (The One Percent Company) started it, and TOPC's own economics (1% to ideas, 99% to work, Neki) live in TOPC's docs, never here. Tasks: `topc-social/owf-tasks`.

- [`SPEC.md`](SPEC.md) is the specification; `README.md` is the plain-language overview; `origins/` is background; `sim/` holds simulations.
- **The spec is principles only, and reward-free.** Rewards, pricing, scoring formulas, tools, flows and anything product-specific belong to whoever uses OWF, not here. Test: would this hold for any setting, any reward, any tool?
- This repo is public. Write for anyone reading it cold.

## Working rules

- One branch per piece of work, off `main`, merged through a pull request. Never push to `main` directly.
- Keep a change to its task. Unrelated fixes get their own branch.
- Invented work counts for nothing: no made-up users, quotes, numbers or sources. Research needs a source for every claim, and if you can't find something, say so.
- Never commit secrets. Real env files stay untracked; only non-secret templates like `.env.example` are committed.

## Your own machine

Setup that only exists on one person's machine (ports, local servers, file locks, worktree layout) does not belong here. Claude Code loads a gitignored `CLAUDE.local.md` next to this file; other agents have their own global config (for example `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`).
