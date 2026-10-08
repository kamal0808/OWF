# Open Work Framework: rules for every agent

This file is for any AI agent working in this repo: Claude Code, Codex, Gemini CLI, Cursor, Copilot or anything else. `CLAUDE.md` and `GEMINI.md` only point here, so keep project rules in this file and nowhere else.

## What this repo is

OWF (Open Work Framework) is an open protocol for working together on ideas and sharing ownership by contribution: splitting work into units, attributing contributions and rewarding them. It is part of **TOPC** (The One Percent Company), a co-operative built in tech where contribution is equity. Anyone can work on a TOPC project, and verified work earns **Neki**, TOPC's reward for contributions (for now an internal, off-chain coin that can't be transferred or sold). Every task splits 1% to whoever had the idea and 99% to whoever did the work. Tasks are picked and handed in through Ideato (ideato.social). Ideato is the first product built on OWF.

- [`SPEC.md`](SPEC.md) is the specification; `README.md` is the plain-language overview; `origins/` is background; `sim/` holds simulations.
- **The spec is principles only.** Tools, flows, scoring formulas, AI-judge details and anything product-specific belong to the implementation (Ideato and its docs), not here.
- This repo is public. Write for anyone reading it cold.

## Working rules

- One branch per piece of work, off `main`, merged through a pull request. Never push to `main` directly.
- Keep a change to its task. Unrelated fixes get their own branch.
- Invented work counts for nothing: no made-up users, quotes, numbers or sources. Research needs a source for every claim, and if you can't find something, say so.
- Never commit secrets. Real env files stay untracked; only non-secret templates like `.env.example` are committed.

## Your own machine

Setup that only exists on one person's machine (ports, local servers, file locks, worktree layout) does not belong here. Claude Code loads a gitignored `CLAUDE.local.md` next to this file; other agents have their own global config (for example `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`).
