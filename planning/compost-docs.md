# Compost Finance Documentation

---

## Part 1: Context

---

### What is Hyperliquid?

Hyperliquid is the fastest-growing perpetuals exchange in crypto.

- $1B+ daily volume
- Sub-200ms latency
- Fully on-chain order book
- $9.6B total open interest (more than all competitors combined)

It's not a fork. It's purpose-built infrastructure: a custom L1 (HyperBFT consensus) with a native order book (HyperCore) and an EVM-compatible smart contract layer (HyperEVM).

In October 2025, Hyperliquid launched HIP-3.

---

### What is HIP-3?

HIP-3 (Hyperliquid Improvement Proposal 3) enables permissionless deployment of perpetual futures markets.

Anyone who stakes 500K HYPE can deploy their own market on Hyperliquid's infrastructure. They choose the asset, oracle, leverage limits, and parameters. Hyperliquid handles matching, settlement, and risk.

**What can be listed:**
- Equities (Tesla, Nvidia, indices)
- Commodities (gold, silver)
- FX pairs
- Pre-IPO companies (SpaceX, OpenAI, Anthropic)
- Crypto assets
- Custom indices and baskets

**The economics:**

Deployers receive 50% of all trading fees their market generates. This is protocol-enforced — not discretionary, not a promise. Code.

The other 50% goes to Hyperliquid (protocol fees, HYPE buybacks).

---

### The Barrier

To deploy a HIP-3 market, you must stake 500K HYPE.

At $30/HYPE, that's **~$15 million**.

This isn't a bug. It's a security mechanism:
- Ensures deployers have skin in the game
- Stake can be slashed for malicious behaviour (bad oracles, manipulation)
- Creates accountability without centralised gatekeepers

But it locks out most participants from the best yield opportunity in crypto right now.

---

### The Opportunity

HIP-3 markets are live and generating real fees.

| Metric | Value |
|--------|-------|
| Cumulative volume | $32B+ |
| Open interest | $917M+ |
| Fees generated | $5M+ |
| Live markets | 7+ |

**Live markets include:**

| Market | Category | Notes |
|--------|----------|-------|
| trade.xyz | Equities | XYZ100 (Nasdaq proxy), NVDA, TSLA — $12.7B+ volume |
| Kinetiq Markets | Global indices | $363M 30d volume |
| Felix | Equities | TSLA first, more coming |
| HyENA | USDe perps | Ethena-backed, BTC/ETH/SOL/HYPE |
| Ventuals | Pre-IPO | SpaceX, OpenAI, Anthropic |
| Vaultus | Structured | Live |

**Note on fees:** Most markets currently operate in "Growth Mode" — a 90% fee reduction to bootstrap volume. As markets mature and Growth Mode ends, fee rates will normalise to standard levels (~4.5 bps taker), significantly increasing yield.

---

### The Problem Compost Solves

If you have $20M, you can deploy a market and earn 50% of fees.

If you don't, your options are fragmented:
- Stake via Kinetiq Launch (their pools, their terms)
- Buy individual deployer tokens (single-market exposure)
- Watch from the sidelines

There's no simple way to get diversified exposure to HIP-3 yield.

**Compost fixes this.**

---

## Part 2: Solution

---

### What is Compost?

Compost is the capital formation layer for Hyperliquid builder markets.

We aggregate capital into a single vault, allocate across vetted HIP-3 markets, and pass through yield to depositors.

**How it works:**

1. You deposit HYPE
2. You receive cHYPE (your receipt token)
3. Vault allocates capital across HIP-3 markets and validator staking
4. Yield accrues to the vault
5. cHYPE appreciates as yield compounds
6. Withdraw anytime (14-day queue or sell on secondary market)

**One token. Diversified exposure. No $20M minimum.**

---

### Who It's For

| User | Use Case |
|------|----------|
| HYPE holders | Earn yield without picking markets |
| DeFi users | Composable yield token (Pendle, lending, LP) |
| Institutions | Compliant access to HIP-3 yield |
| Protocols | White-label yield infrastructure |

---

### cHYPE

cHYPE is your receipt token. It represents your share of the vault.

**Properties:**
- ERC-20 standard
- Appreciating (not rebasing) — exchange rate increases as yield accrues
- Composable — use in DeFi (Pendle, lending, LP)
- Tradeable — secondary market liquidity

**Exchange rate:**

```
cHYPE price = Total HYPE in vault / Total cHYPE supply
```

As yield accrues, the numerator grows. cHYPE appreciates.

---

## Part 3: Technical

---

### Architecture

[DIAGRAM: Architecture overview showing Vault, cHYPE token, Fee Router, and connections to HIP-3 markets and validator staking]

**Components:**

| Component | Function |
|-----------|----------|
| Vault Contract | Holds HYPE, manages allocations, handles deposits/withdrawals |
| cHYPE Token | Receipt token, tracks pro-rata share of vault |
| Fee Router | Splits yield between vault and protocol |
| Withdrawal Queue | Manages unstaking requests |

**Infrastructure Partner:** [TBC — Infra Singularity]

**Multisig:** [TBC — signers and threshold]

**Audit Status:** [TBC]

---

### Yield Sources

Compost generates yield from three sources:

#### 1. Validator Staking

A portion of the vault is staked with Hyperliquid validators.

- Base yield: ~2.5% APY
- 7-day unstake queue
- Used as liquidity buffer for redemptions

#### 2. HIP-3 Builder Fees

The majority of the vault is allocated to HIP-3 markets.

Yield varies by allocation method:

| Method | Fee Share | Notes |
|--------|-----------|-------|
| Direct deployment | 50% | Protocol-enforced, requires 500K HYPE stake |
| Partner allocation | 20-40% | Negotiated with deployers (Felix, Ventuals, etc.) |
| Pooled staking | Variable | Via Kinetiq Launch or similar, pro-rata share |

Compost targets the highest risk-adjusted yield across methods, balancing direct deployment (higher yield, higher capital) with partner allocations (diversification, lower capital).

#### 3. Token Incentives

Some deployers distribute token incentives to stakers (FELIX, KNTQ, etc.).

Compost holds these in treasury and sells periodically to fund operations. This does not affect cHYPE yield — it's a separate revenue stream.

---

### Yield Flow

[DIAGRAM: Yield flow from deposit through allocation, yield accrual, fee deduction, and cHYPE appreciation]

**Step by step:**

```
1. User deposits HYPE
   └── Vault receives HYPE
   └── cHYPE minted at current exchange rate
   └── User receives cHYPE

2. Vault allocates HYPE
   ├── 20-30% → Validator staking (liquidity buffer)
   └── 70-80% → HIP-3 markets (yield generation)

3. Yield accrues
   ├── Staking rewards: claimed daily
   ├── Builder fees: distributed per epoch (varies by market)
   └── Token incentives: held in treasury

4. Yield enters vault
   └── Protocol fee deducted (15% of yield)
       ├── 90% → Compost operations
       └── 10% → Infrastructure partner

5. Net yield compounds
   └── Vault HYPE balance increases
   └── cHYPE exchange rate increases
   └── All cHYPE holders benefit proportionally
```

---

### Allocation

#### Methods

| Method | How It Works | Yield | Risk |
|--------|--------------|-------|------|
| Direct deployment | Compost stakes 500K HYPE, deploys market | 50% of fees | Full slashing exposure |
| Partner allocation | Stake with existing deployer (Felix, etc.) | Negotiated (20-40%) | Operator risk |
| Pooled staking | Contribute to Kinetiq Launch pool | Pro-rata share | Pool + operator risk |
| Indirect exposure | Hold deployer LST (kmHYPE, etc.) | Token appreciation | Token risk |

Compost uses a blend of methods to optimise for:
- Yield (maximise returns)
- Diversification (no single-market concentration)
- Risk (minimise slashing and operator exposure)

#### Selection Criteria

Before allocating to any market, we assess:

**Operator**
- Team background and track record
- Previous projects and on-chain history
- Communication and transparency
- Responsiveness to issues

**Market**
- Volume history and trajectory
- Fee generation (actual, not projected)
- Oracle quality and update frequency
- Leverage limits and risk parameters
- Slashing history

**Fit**
- Correlation with existing allocations
- Category diversification
- Liquidity profile

#### Current Allocations

[TBC — will be published on launch and updated regularly]

| Market | Category | Allocation % | Method |
|--------|----------|--------------|--------|
| TBC | TBC | TBC | TBC |

#### Advisory Committee

Allocation decisions are reviewed by an independent advisory committee.

- 3-5 members with DeFi and risk management experience
- All allocations published with rationale
- Quarterly portfolio reviews

Committee members: [TBC — disclosed on launch]

---

### Fees

#### Protocol Fee

**15% of all yield** (staking + builder fees)

Deducted from yield before compounding into vault.

#### Fee Split

| Recipient | Share | Use |
|-----------|-------|-----|
| Compost operations | 90% | Team, growth, marketing, legal, audit |
| Infrastructure partner | 10% | Vault build and maintenance |

#### Institutional

Institutional clients may negotiate different terms. Contact grow@compost.fi.

---

### Redemptions

Two exit paths:

#### 1. Protocol Redemption

- Burn cHYPE
- HYPE queued for withdrawal
- 14-day unstake period (Hyperliquid protocol constraint)
- HYPE released after queue clears

**No fee on principal.** Protocol fee is already taken on yield.

#### 2. Secondary Market

- Sell cHYPE on DEX
- Instant liquidity
- Price may differ from NAV (premium or discount depending on demand)
- No protocol interaction required

#### Liquidity Buffer

20-30% of vault is kept in validator staking (not HIP-3 allocated).

Purpose:
- Cover normal redemptions without unwinding HIP-3 positions
- Maintain base yield during rebalancing
- Shorter unstake queue (7 days vs 14)

#### Large Redemptions

Redemptions >5% of vault may be processed in tranches to avoid market impact and forced position unwinding.

#### Edge Cases

| Scenario | Handling |
|----------|----------|
| Bank run | Redemptions processed FIFO, HIP-3 positions unwound as needed |
| Market dislocation | Secondary market price may diverge from NAV |
| Slashing event | Loss absorbed pro-rata by all cHYPE holders |

---

### Risk

#### Smart Contract Risk

Vault contracts may contain bugs or vulnerabilities.

**Mitigation:**
- Audit by [TBC]
- Bug bounty program [TBC]
- Multisig controls
- Gradual TVL ramp-up

#### Slashing Risk

HIP-3 deployers can be slashed for malicious behaviour (bad oracles, manipulation).

If Compost stakes directly and is slashed, the loss is absorbed by the vault (all cHYPE holders).

**Mitigation:**
- Careful market selection
- Diversification (no single market >25% of vault)
- Monitoring and rapid response
- Prefer partner allocations for unproven markets

#### Operator Risk

Deployers (Felix, Ventuals, etc.) may mismanage markets, have technical issues, or act against staker interests.

**Mitigation:**
- Due diligence on operators
- Diversification across operators
- Monitoring of market health
- Relationships with operator teams

#### Liquidity Risk

In a bank run scenario, the vault may not have enough liquid HYPE to cover all redemptions immediately.

**Mitigation:**
- 20-30% liquidity buffer
- Secondary market provides alternative exit
- Large redemptions processed in tranches
- Clear communication during stress events

#### Regulatory Risk

HIP-3 markets (especially equities, pre-IPO) may face regulatory scrutiny.

**Mitigation:**
- Legal review of structure
- Institutional onboarding with KYC/AML
- Geographic restrictions where required
- Monitoring of regulatory developments

---

## Part 4: Ecosystem

---

### Integrations

cHYPE is a standard ERC-20 token. It's composable across DeFi.

#### Where cHYPE Can Be Used

| Integration | Use Case |
|-------------|----------|
| Pendle | Split into PT (principal) + YT (yield) — trade future yield |
| Lending (Morpho, Euler, Felix) | Use as collateral, borrow against yield position |
| DEX (Beets, etc.) | Provide liquidity in cHYPE pairs |
| Yield aggregators | Auto-compound strategies |
| Structured products | Use as underlying for other protocols |

#### API Access

For protocols and platforms integrating Compost:

**Endpoints:**

| Endpoint | Function |
|----------|----------|
| `POST /deposit` | Deposit HYPE, receive cHYPE |
| `POST /withdraw` | Burn cHYPE, queue HYPE withdrawal |
| `GET /balance` | cHYPE balance, HYPE value, yield accrued |
| `GET /nav` | Current cHYPE/HYPE exchange rate |
| `GET /yield` | Current APY, breakdown by source |
| `GET /allocations` | Current market allocations |

**Webhooks:**
- `deposit_confirmed`
- `withdrawal_ready`
- `yield_accrued` (daily)

Full API documentation: [TBC]

#### Partnership Models

| Model | How It Works | Best For |
|-------|--------------|----------|
| Standard integration | Use API, no fee arrangement | Small integrations |
| Revenue share | Reduced protocol fee (10%), partner gets kickback | Large AUM partners |
| Referral | 10-20% of protocol fee on referred TVL | Affiliates, influencers |
| White-label | Full API, their brand, their clients | Platforms, neobanks |

Contact grow@compost.fi to discuss integration.

---

### Institutional Access

For funds, family offices, and platforms requiring compliance, reporting, and dedicated support.

#### Onboarding

- KYC/AML verification through regulated partner
- Investor qualification (accredited/qualified purchaser)
- Legal entity contracting
- Subscription agreement and risk disclosures

#### Reporting

- NAV reporting (daily, weekly, or monthly)
- Allocation breakdown
- Yield attribution (staking vs builder fees)
- Fee transparency
- Full audit trail
- Tax documentation

#### Custody

Integration available with:
- Fireblocks
- Anchorage
- Copper
- Other qualified custodians on request

#### Advanced Structures

**Segregated Vaults**

For larger allocations or compliance requirements:
- Separate vault instance
- Not commingled with retail
- Jurisdiction-specific if needed
- Own receipt token (cHYPE-[X])
- Same allocation strategy, same yield

**White-Label**

Offer Compost yield to your clients:
- Your brand, your UI
- Your client relationships
- API access to vault infrastructure
- Custom fee arrangements

**Feeder Funds**

Regulated vehicle (Cayman, BVI, etc.) that invests into Compost:
- Cleaner structure for LPs with fund mandates
- Admin and audit handled by fund service providers

---

### Early Stakers

Compost rewards early believers.

**No points. No token. Just better terms.**

#### Launch Bonus

- First 30 days: 0% protocol fee
- All yield goes to stakers
- Day 31+: Standard 15% fee

#### Access

- Whitelist before public launch
- Capped deposit phases
- Top stakers may be invited to Advisory Committee

#### Referrals

- Bring $500K+ TVL
- Earn 10% of protocol fees on that TVL for 12 months
- Paid monthly in HYPE

---

## Part 5: Appendix

---

### Contracts & Addresses

| Contract | Address | Notes |
|----------|---------|-------|
| Vault | [TBC] | Main vault contract |
| cHYPE Token | [TBC] | Receipt token |
| Fee Router | [TBC] | Fee distribution |
| Multisig | [TBC] | [X]-of-[Y] signers |

---

### Audit Status

| Auditor | Status | Report |
|---------|--------|--------|
| [TBC] | [TBC] | [Link TBC] |

---

### Team

Compost is built by [TBC — how much to disclose?]

Contact: grow@compost.fi

---

### FAQ

**What is cHYPE?**

Your receipt token. It represents your share of the vault and appreciates as yield accrues.

**Is there a Compost token?**

No. cHYPE is the product. There is no governance token.

**What's the minimum deposit?**

No minimum for retail. Institutional onboarding available for larger allocations.

**How do I withdraw?**

Burn cHYPE for HYPE (14-day queue) or sell cHYPE on secondary markets for instant exit.

**What are the fees?**

15% of yield. No deposit or withdrawal fees.

**Is it audited?**

Audit in progress. Report will be published before mainnet launch.

**Who manages allocations?**

Compost team with oversight from an independent advisory committee. All allocations are published.

**What if a market I'm allocated to gets slashed?**

Diversification limits exposure. No single market >25% of vault. Losses are absorbed pro-rata by all cHYPE holders.

**What about token incentives from deployers?**

Held in treasury and sold periodically to fund operations. Does not affect cHYPE yield directly.

**Can institutions use Compost?**

Yes. KYC/AML onboarding, NAV reporting, custody integration, and dedicated support available. Contact grow@compost.fi.

**Can I use cHYPE in DeFi?**

Yes. cHYPE is composable — use it on Pendle, as collateral, in LP positions, etc.

---

### Links

| Resource | URL |
|----------|-----|
| Website | https://compost.fi |
| Twitter | https://twitter.com/compostfi |
| Docs | https://docs.compost.fi |
| Email | grow@compost.fi |
| Dune (HIP-3 stats) | https://dune.com/yandhii/hip3 |

---

*Last updated: [DATE]*

*Version: 1.0*
