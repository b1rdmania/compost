# Product Marketing Context

*Last updated: 2026-04-17 — V1 auto-draft from codebase + strategy notes. Needs human pass.*

> ⚠️ Compost is **parked / exploratory**, not a live product. This doc reflects what the **site (compost.fi)** is positioned as **today**, not the original Sept 2025 vault product. The vault thesis lives in `litepaper.html` as a concept archive.

---

## Product Overview

**One-liner:**
A live, independent view of Hyperliquid's builder markets — HIP-3 board, HIP-4 notes, vault-mechanic demos, and the original cHYPE litepaper as concept archive.

**What it does:**
Aggregates and surfaces on-chain activity from HIP-3 deployers (volume, fees, OI) on a refreshed live board. Tracks HIP-4 outcome books on testnet. Hosts a working vault-mechanic demo on HyperEVM testnet (deposit/withdraw/synthetic-APR proof of accounting). Preserves the September 2025 cHYPE litepaper as historical concept context.

**Product category:**
Hyperliquid ecosystem intelligence / builder-market data hub. (Not a vault. Not a yield product. Not an exchange.)

**Product type:**
Free, public, static marketing site + live data dashboards + open-source contracts (testnet-only). No authentication, no on-site transactions in production.

**Business model:**
None active. Originally intended as a fee-routing vault product (cHYPE) — that route is parked. Today the site exists as a research surface and a way to find HL-aligned collaborators.

---

## Target Audience

**Target segments (3, in order of fit):**

1. **HL-native traders, deployers, and whales**
   Already trading on Hyperliquid; tracking HIP-3 deployments because it affects their flow / strategies / capital allocation.

2. **DeFi researchers, analysts, journalists, fund GPs**
   Building a thesis on Hyperliquid as a venue for builder-deployed perps + outcome markets. Want an independent, non-deployer-affiliated lens.

3. **Aligned builders / potential collaborators**
   Working on HL-native tooling (data, UX, vault primitives). May want to partner, fork, or compare notes.

**Primary use case:**
"I want to know what's actually happening across HIP-3 builder markets right now — and I don't want to read four Dune dashboards and a Discord to figure it out."

**Jobs to be done:**
- *Bookmark a single page* that gives a refreshed snapshot of HIP-3 ecosystem volume / fees / OI
- *Understand HIP-4* (early, mostly testnet) without trawling docs
- *See a worked example* of vault accounting + receipt-token mechanics, on testnet
- *Read an opinionated take* (the litepaper) on the vault thesis around builder markets

**Use cases / scenarios:**
- A Hyperliquid power user opens the HIP-3 board mid-session to see deployer fee share trends
- A fund GP sends a colleague the litepaper as a primer for a thesis discussion
- A builder evaluating vault primitives looks at the HyperEVM testnet contracts
- A journalist looking for HIP-3 stats lands here from search and uses the live board as a citation

---

## Personas

| Persona | Cares about | Challenge | Value we promise |
|---|---|---|---|
| HL-native trader / whale | Real-time signal on builder-market flow | Data is fragmented across Dune dashboards + per-deployer telemetry | One bookmarkable, refreshed view of HIP-3 + HIP-4 |
| Researcher / fund GP | Independent take on Hyperliquid's HIP-3 thesis | Most HL writing is from deployers themselves (conflicted) | Independent dashboards + opinionated litepaper |
| Aligned HL builder | Finding others working on HL-native primitives | Solo / scattered ecosystem; signal-to-noise is low | Public craft work + an honest "we're parked, here's what we're thinking" hook |
| Anti-persona: generic crypto retail | "Where's the APY?" | Wants a yield product to deposit into | Site explicitly says no live vault — this is not for them |

---

## Problems & Pain Points

**Core problem (for the site's audiences):**
HIP-3 / HIP-4 are interesting and material — billions in volume — but the data + the conceptual model live in disconnected places (Dune, deployer Twitter, HL docs, Discord). There's no opinionated, independent ecosystem-level view.

**Why alternatives fall short:**
- **Raw Dune dashboards** → great data, no narrative, no curation, no HIP-4
- **Deployer-published stats** (trade.xyz, Kinetiq, etc.) → conflicted, only their slice
- **Hyperliquid official docs** → spec-level, not market-level
- **Generic crypto news** → doesn't go deep on HIP-3 mechanics

**What it costs them:**
Time stitching together fragmented data; risk of forming a thesis on partial info; missing HIP-4 entirely (most general crypto coverage hasn't caught up).

**Emotional tension:**
Being late on a thesis you suspected was real. Sounding underprepared in a conversation about Hyperliquid. Trusting a stat that turned out to come from a deployer's marketing page.

---

## Competitive Landscape

**Direct (HL-ecosystem dashboards):**
- *Dune dashboards* (e.g. yandhii/hip3) — raw, no narrative layer, no HIP-4 curation
- *ASXN, Hypurrscan, other HL trackers* — broad HL focus, not HIP-3/HIP-4-specific lens

**Secondary (general DeFi data tools):**
- *DeFiLlama, Token Terminal* — venue-level, not builder-market level

**Indirect (vault / yield products on HL):**
- *Kinetiq, Felix, Looped HYPE etc.* — actual HL-native products competing for capital and mindshare. Compost was originally one of these on paper; today it's not competing in that lane.

**How each falls short for our audience:**
None of them combines: (a) HIP-3 live data, (b) HIP-4 explainer + board, (c) opinionated independent vault-thesis writing, (d) honesty about being a researcher rather than an active product.

---

## Differentiation

**Key differentiators:**
- **Independence** — not a deployer; not selling a vault. Stats are reported, not sold.
- **HIP-3 + HIP-4 in one place** — most existing trackers don't cover HIP-4 yet
- **Concept archive (cHYPE litepaper)** — opinionated thesis-level writing, dated and honest
- **Working testnet contracts** — proof of mechanism, not just slides

**How we do it differently:**
Built as a public, static, refreshing site — not a paid newsletter, not a deployer dashboard, not an LP product. Honest about what it is: a research surface from someone who tried to build the vault and now writes about why it's hard.

**Why that's better:**
Visitors don't have to filter for conflicts of interest. A deployer telling you their venue is doing well is one thing; an independent dashboard showing the whole HIP-3 share is another.

**Why people choose us:**
Curiosity + low cost. Free, fast, refreshed, honest. No signup friction. Bookmarkable.

---

## Objections

| Objection | Response |
|---|---|
| "Is this a vault? Can I deposit?" | No — site is explicitly research + demos. Live testnet only. The litepaper describes what *would* have been the product. |
| "Why should I trust your data?" | Sourced from public dashboards (Dune) and on-chain reads. Refresh times labelled. Method linked. |
| "Aren't you just another HL fan site?" | Built by someone who tried to ship a vault and learned where the thesis is hard. The litepaper is dated and honest about what didn't land. |
| "HIP-3 / HIP-4 — why should I care?" | Builder-deployed perps + outcome markets are arguably the most under-covered structural shift in HL. Numbers are on the live board. |
| "Is the project alive?" | The vault product is parked. The data + writing surface is maintained. Reach out if you're HL-aligned. |

**Anti-persona:** Generic crypto retail looking for "the next high-APY yield play." This site doesn't have one and won't pretend.

---

## Switching Dynamics

**Push (away from current):**
Tired of stitching together Dune dashboards. Tired of deployer-published stats with a marketing slant. Don't have time to track HIP-4 across testnet announcements.

**Pull (toward us):**
One bookmarkable independent page. Live HIP-3 numbers on top. HIP-4 board, vault demo, and a litepaper if they want to go deep.

**Habit (what keeps them on alternatives):**
"I already have my Dune dashboards bookmarked." Counter: ours aggregates them with narrative + HIP-4 layered in.

**Anxiety (what worries them about us):**
Project is parked → will the data be maintained? (Need to address this with: live refresh timestamps, last-updated labels, GitHub links to scrapers.)

---

## Customer Language

**How HL-native users describe the space:**
- "HIP-3", "HIP-4", "builder markets", "deployers", "growth mode", "builder fee share"
- "HL", "Hyperliquid", "HYPE", "HLP", "HyperBFT", "HyperEVM"
- "perps", "OI", "TVL", "venue", "deployer share"

**How they describe the problem:**
- "I just want one page that tells me what HIP-3 is doing this week"
- "Half of HL coverage is deployer marketing"

**How they (might) describe us:**
- "Independent HIP-3 / HIP-4 board"
- "That site with the cHYPE litepaper"

**Words to use:**
- HIP-3, HIP-4, builder markets, builder fees, deployer share, HyperEVM, on-chain
- "Live", "independent", "refreshed", "ecosystem aggregates"
- "Concept archive" (for the litepaper)

**Words to avoid:**
- "Yield", "APY", "earn", "guaranteed" (regulatory + retail-bait)
- "Infrastructure-grade", "institutional-grade" (vague brag)
- "Exploratory project", "parked", "experiment in craft" (true internally; reads like an apology to first-time visitors)
- "Our story" / "Why it didn't land" as section titles (confessional voice)

**Glossary:**

| Term | Meaning |
|---|---|
| HIP-3 | Hyperliquid Improvement Proposal 3 — builder-deployed perpetual markets |
| HIP-4 | HIP 4 — outcome / event markets primitive (early, mostly testnet) |
| Deployer | Team that launches a HIP-3 perp market and earns a fee share |
| Builder fee share | Protocol-defined share of trading fees routed to the deployer |
| cHYPE | Receipt token in Compost's original vault concept (litepaper) |
| HLP | Hyperliquid Liquidity Provider vault |
| HyperEVM | EVM-compatible execution layer on Hyperliquid |

---

## Brand Voice

**Tone:** Quiet, technical, honest. "Whispers, not shouts" (per `DESIGN.md`).

**Style:** Direct, plainspoken. No hype words. Prefers concrete numbers and dated stats over generalities. Acknowledges what it is and isn't.

**Personality (3–5 adjectives):** Independent · curious · honest · craft-driven · understated.

**What to never sound like:** A yield aggregator landing page. A whitepaper-launch hype thread. A "we're back" pivot post.

---

## Proof Points

**Metrics (ecosystem, not Compost performance):**
- $87.32B HIP-3 cumulative volume
- $13.63M HIP-3 cumulative fees
- $2.07B HIP-3 open interest
- *(as of 2026-04-14, source: Dune yandhii/hip3)*

**On-chain proof of craft:**
- HyperEVM testnet vault contract: `0x89bBacDACA0D20CB48FA617b57CF6779979AEC4E`
- Mock asset (vHYPE): `0xAdBc75586E2F5338F460410B87F7AFde0374Fc31`

**Deployers tracked / referenced:**
- trade.xyz (~$75.5B vol)
- Kinetiq (~$1.4B vol)
- Felix (TSLA, equities)
- Ventuals (SpaceX, OpenAI, Anthropic — pre-IPO)

**Value themes:**

| Theme | Proof |
|---|---|
| Live data | Refresh timestamps on every stat; HIP-3 board refreshes every 60s |
| Independent | Not a deployer; not selling a vault; affiliated with no specific HL venue |
| Honest | Litepaper labelled as Sept 2025 archive; site says "no live vault" plainly |
| Built, not just written | HyperEVM testnet contracts deployed and verifiable |

---

## Goals

**Business goal:** Maintain a small, useful HL-research surface that signals craft and finds HL-aligned collaborators. Optionally: feed into a future, sharper product around HIP-3 / HIP-4 data or tooling.

**Primary conversion action:**
1. **Open the HIP-3 live board** (most likely useful action for any visitor)
2. **Bookmark / return** (no instrumented metric yet)
3. **Email `grow@compost.fi`** if HL-aligned (collaboration funnel)
4. *Optional secondary:* low-volume email updates list (only if it adds value, not as a generic "waitlist")

**Current metrics:** Not instrumented. (Should add basic analytics if we're going to optimize.)

---

## Resolved direction (2026-04-17)

Decisions made after V1 draft review:

1. **Primary audience: aligned HL builders / collaborators.**
   The site's main job is to *signal craft + thesis* and surface HL-native folks who want to work together. Traders and researchers are real secondary audiences (they're the ones who'll *find* and *share* the boards), but the conversion action is collaboration, not a recurring product use.

2. **Kill the email signup form.**
   Replace with a single direct CTA: `grow@compost.fi`. No "waitlist", no "updates" newsletter framing — that creates expectation of a launch we're not making.

3. **HIP-3 + HIP-4 boards are co-headline products.**
   Both get equal weight above the fold. HIP-4 is genuinely under-covered and acts as a differentiator vs. existing HL trackers.

4. **Litepaper → "Concept".**
   Rename the nav item from "Litepaper" to "Concept" so it reads as opinion / thesis, not a whitepaper-launch artefact. The page itself stays at `/litepaper.html` (URL stable) but the framing is "concept document, Sept 2025".

5. **Implications for the homepage rewrite:**
   - Headline frame: data + craft as proof, collaboration as ask
   - Above the fold: twin board CTAs, no apology
   - Mid-page: builders shipping HIP-3 (existing market cards work)
   - Bottom: short concept paragraph + single collaborate CTA
   - No email form section
