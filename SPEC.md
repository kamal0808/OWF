# Open Work Framework v0.1

Draft, 2026-10-06. Items marked *(default)* are proposed and may still change; everything else is settled for v0.1.

> "Genius is one percent inspiration, ninety-nine percent perspiration." (Thomas Edison)

## The thesis

In a company, capital earns ownership: money buys shares, and money makes more money. OWF makes work the capital. You invest skill and time instead of cash, and that work earns you a share of what gets built. Ideas matter, but they're the 1%. Doing the work is the 99%.

This isn't communism (nobody plans or equalises outcomes) and it isn't capitalism (money doesn't steer). Labor hires capital, not the other way round: money is welcome, gets a fair return, and never gets control.

OWF is a framework, not a product. It defines what work, credit and ownership mean and the rules that keep them fair. It says nothing about any tool, platform or organisation. Anyone can build an implementation on it and pick their own parameters.

The rules exist so people feel it's fair enough to keep showing up. When a rule can be precise or simple and legible, pick legible.

## 1. Three units that never mix

| Unit | Measures | Scope |
|---|---|---|
| **Credit** | work done | the same everywhere |
| **Ownership %** | your share of one venture | per venture |
| **Money** | what the venture is worth | set by the market |

Credit is a unit of work, not of money. The same work at the same stage earns the same credit on any venture. What that credit is worth in money depends only on how the venture does, through your ownership %.

## 2. Definitions

**Venture.** Anything people build together toward a shared outcome: a product, a service, a campaign, a co-op. Ownership only ever means something relative to one venture.

**Need.** An outcome the venture wants ("ten paying users", "a working signup"). Needs are prompts, not gates: a contribution doesn't have to answer a posted need.

**Idea.** A claim about what should be done, with no evidence. "People should do X." Talk, advice, discussion, gyaan. Good and bad gyaan look the same until someone acts on it.

**Work.** Anything that comes with evidence someone else can check without trusting you. The same thought becomes work once it's backed: "I talked to 12 shopkeepers and 9 said X, here are the notes" is work. Connecting people, advising and coordinating count as work when there's evidence they happened and helped.

**Contribution (the unit of work).** A claim that you added something to a venture, plus its evidence. A contribution is atomic if it's useful on its own and can be judged on its own. If splitting it doesn't produce two things that each stand alone, it's one contribution. *(default)*

**Evidence.** Something another person can check without taking your word for it. Fabricated evidence (invented interviews, fake users) makes a contribution worthless. Which tools helped, AI included, never matters; whether it's real always does.

**Attribution (the unit of attribution).** Two things about a contribution, kept separate from its value:
- **Who**: the people behind it and their split, adding up to 1. One person proposes the whole split from the evidence and every person named confirms or counters it. Nobody states their own share separately, because self-estimates of joint work always add up to more than 100%. *(default)*
- **Builds on**: the idea or earlier contribution it builds on. The person who did the work names it, not the idea-giver, and anyone can challenge it. *(default)*

Attribution answers "who". Value answers "how much". A dispute about one should never turn into a dispute about the other.

**Value.** How much a contribution adds, judged when it's handed in and topped up later when real impact shows. Time spent is never value. Quality and impact are.

**Credit.** Value expressed in the credit unit. Once given, credit never goes down. Impact can add to it later; only proven fraud removes it.

**Ownership.** Your share of one venture, worked out from the pools in section 3.

**Dilution.** New credit shrinks everyone's % but never anyone's credit. Dilution is fair when the venture grows at least as much as your slice shrinks. People accept being diluted by someone who made the thing bigger. Junk doesn't need punishing: it keeps its credit but falls behind as good work earns impact.

## 3. The pools

Every venture's ownership is split into pools:

| Pool | Share | Who earns it | How it's split |
|---|---|---|---|
| **Idea** | 1%, forever | people whose ideas got executed | by the credit of the work built on each idea |
| **Work** | the rest | people who did the work | your credit ÷ all credit in the venture |
| **Capital** | set at each raise | people who put in money | by money put in |
| **Network** (optional) | a small fixed slice | a network that hosts many ventures | its own rules |

- The idea pool stays exactly 1%, whatever happens. Capital and any network slice come out of the work side, never out of the 1%.
- Only executed ideas earn. An idea's slice of the 1% = credit of work built on it ÷ all work credit in the venture. Ideas nobody built on earn nothing.
- Ideas don't earn credit themselves. If they did, 1 idea-credit and 1 work-credit would buy very different ownership, and "1 credit = 1 credit" would break. *(default)*
- Someone who has an idea and also builds it earns from both pools. The idea share is capped by the 1%, so this can't be farmed.
- Capital is money only. Anything an investor does beyond money (introductions, advice, sales) is work and earns credit like anyone else's.
- Capital buys a share of the capital pool at a price agreed at each raise. That price is the venture's valuation. Capital doesn't earn credit. *(default)*
- A network slice lets ventures share risk with each other, the way Mondragon's co-operatives back each other. If a network takes one, it's fixed before the venture's first contributor joins and never raised afterwards. *(default)*

Example with a 1% network slice, after one raise of 20%: idea 1%, network 1%, capital 20%, work 78%.

## 4. Defining 1 credit *(default)*

Credit has to mean the same thing on every venture and in every year, so it's anchored to a **reference set**: 10–15 real contributions with fixed credit amounts. For example, "a working landing page, shipped" = 50 and "10 real user interviews with notes" = 30.

- Every judgement compares new work against the reference set. Nobody scores in the abstract.
- The set is versioned. A new version applies only to work handed in after it's published, never retroactively.
- The set learns from outcomes. When impact keeps landing on a kind of work the set undervalues, the next version raises it. Nobody can price value perfectly up front, so the set follows what actually worked.
- Every award shows the version it was judged under and one sentence on why.

## 5. Early risk

Work done early carries more risk: the venture is worth nothing and will probably die. Skill invested early is like seed money, so it earns a stage multiplier.

- The multiplier is fixed at the moment of the contribution and never changes afterwards.
- A venture moves stage only on evidence (first live user, first revenue), dated by when the evidence happened, not when someone posted it.
- Keep it small. Markets price early risk far higher, but a big multiplier lets early people own everything forever and makes newcomers not bother. The multiplier is a fairness nod, not a full risk price. Foundational work gets its real upside through impact on the work that builds on it.

## 6. Capital and dilution *(default)*

- **Between raises, capital's % is fixed.** New work dilutes only the work pool. Investors paid for a fixed share, and the work after a raise is what their money funds. Every raise says it in one sentence: "the work pool stays at X%, shared by everyone who contributes until the next raise."
- **Each new raise dilutes the work pool and earlier capital proportionally.** The 1% is never touched. Earlier investors may buy in again at the new price to keep their share.
- **Capital gets a return, not control.** Capital has no votes, and the capital pool has a ceiling below half, so builders always own most of what they build.

## 7. Control *(default)*

- Raises, selling the venture, shutting it down and changing its licence are decided by **active credit**: credit held by people who contributed recently. Credit is owned forever, but only active builders steer. Without this, people who left slowly outvote the people building.
- No single person carries more than a set share of any vote, however much credit they hold.
- Anyone active can propose a rule change. It's adopted by the same vote, applies only to future work, and is never retroactive.

## 8. Impact *(default)*

- Each venture picks 1–3 outcome measures for its stage, locked before each measurement window.
- Impact is paid per unit of outcome moved, with a cap, not as a fixed pot. A fixed pot turns builders into rivals who gain when others fail.
- Impact adds credit to the contributions that moved the outcome, and through "builds on" to the work they stood on. It never takes credit away.

## 9. Cash and access *(default)*

Working for ownership alone only works for people who can afford to. Small cash payments for work are allowed, and whatever was paid in cash is subtracted from that contribution's credit.

## 10. Disputes and legibility

- Disputes look for middle ground first: talk, then a mediator proposes middle options, and only as a last resort neutral people pick one of those options. Never all-or-nothing, except for fake work.
- Responses are graduated between a value dispute and fraud: a note, then credit held pending review, then removal for proven fake work. *(default)*
- Awards are provisional until the challenge window closes, then final. *(default)*
- Show ownership as credit first, since it only grows. Show % next to what changed it and how far the venture has moved. Default to a personal view, and keep the full ledger public one step away. Put the most explanation into the bad moments: low awards, challenges, dilution and raises. *(default)*

## 11. Lifecycle

- **Joining** is open. Anyone can contribute to any venture.
- **Leaving.** People who stop contributing keep all their credit. Only proven fraud loses it.
- **Work from before the rules.** It's handed in with evidence and judged by the same rules as everyone's, before the first outside contributor joins. Nobody, founders included, gets credit by decree.
- **Bake.** A venture may define a moment when credit converts into fixed equity (incorporation, a funding round). OWF allows it but doesn't require it.

## 12. Invariants

These hold in every OWF implementation:

1. Splitting, padding or reposting the same work never earns more.
2. Credit is never taken away, except for proven fraud.
3. Rules are published, versioned, and never applied retroactively.
4. Anyone can understand in one sentence why they got what they got.
5. The idea pool is 1%, forever.
6. Time is not value.
7. Capital never steers.

## 13. Parameters

Implementations set these. Suggested starting values:

| Parameter | Suggested |
|---|---|
| Stage multiplier (idea / building / live / revenue) | 2× / 1.5× / 1.2× / 1× |
| Capital pool ceiling | 49% |
| "Active" for voting | contributed in the last 6 months |
| Vote cap per person | 25% |
| Network slice | 0–1% |

## 14. Left to each implementation

How a tool's activity becomes evidence, who or what does the judging (and how it's protected from manipulation), challenge windows and costs, identity checks, the reference set itself, and the parameters above.

## Open questions

- Credit can't be sold, so people who left pile up in every venture forever. Eventually a bake or a buy-back route is needed.
