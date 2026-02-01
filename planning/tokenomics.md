# Tokenomics

$COMPOST token distribution, vesting, and TGE mechanics.

---

## Total Supply

**1,000,000,000 $COMPOST** (fixed, no inflation beyond scheduled emissions)

---

## Distribution

| Category | % | Tokens | Vesting |
|----------|---|--------|---------|
| Founder + Team | 10% | 100,000,000 | 36-month linear (no cliff) |
| Genesis Airdrop | 30% | 300,000,000 | Liquid at TGE* |
| Emissions (ve/gauges) | 45% | 450,000,000 | 4-year release via gauges |
| Treasury / POL / Integrations | 13.5% | 135,000,000 | Governed, no discretionary sales |
| Legion Raise + Lock Bonus | 1.5% | 15,000,000 | See raise mechanics |

*Airdrop liquidity subject to oversubscription rule (see below).

---

## What's Liquid at TGE

| Category | Liquid | Locked |
|----------|--------|--------|
| **Airdrop (30%)** | 100% (default) | — |
| **Founder + Team (10%)** | 0% | 36mo linear vest |
| **Legion Liquid Tier** | 100% | — |
| **Legion Lock Tier** | 0% | 12 months (base + bonus) |
| **Emissions (45%)** | 0% | Released via gauges |
| **Treasury (13.5%)** | 0% | Governed sales only |

### Initial float calculation

**Default scenario (no oversubscription):**
- Airdrop: 30%
- Legion liquid tier (estimated): ~0.5%
- **Total float: ~30.5%**

**Oversubscribed scenario (90% to lockers):**
- Airdrop: 30%
- Legion liquid tier: ~0.15% (only 10% of raise is liquid)
- **Total float: ~30.15%**

High float at TGE = less sell pressure concentration.

---

## Airdrop Mechanics

### Eligibility

Points accrued from:
- Holding cHYPE (1x multiplier)
- LP in whitelisted pools (2x multiplier)
- Duration weighted (longer = more points)

### Distribution

- Pro-rata based on points at snapshot
- Minimum threshold to qualify (prevents dust claims)
- Fully liquid at TGE (default)

### Oversubscription Rule

If the Legion raise is heavily oversubscribed:
- 90% of raise allocation goes to lock-tier participants
- 10% to liquid-tier participants

This does not affect airdrop liquidity — airdrop remains liquid.

---

## Legion Raise

**Target:** $1,000,000  
**Mechanism:** Legion-style public raise

### Tiers

| Tier | Lock Period | Allocation |
|------|-------------|------------|
| Liquid | None | Base allocation |
| Locked | 12 months | Base + 50% bonus |

### Example

Participant contributes $10,000:
- **Liquid tier:** Receives X tokens, immediately tradeable
- **Lock tier:** Receives 1.5X tokens, locked for 12 months

### Oversubscription handling

If total demand exceeds $1M:
1. Lock-tier gets priority (90% of slots)
2. Liquid-tier gets remainder (10% of slots)

Excess contributions refunded.

---

## Founder Secondary

- **Amount:** 0.5% of total supply (5,000,000 tokens)
- **Mechanism:** OTC sale at TGE
- **Buyer(s):** Disclosed, with lock agreement
- **Purpose:** Founder liquidity + investor alignment

This is separate from the 10% founder+team allocation (which vests over 36 months).

---

## Vesting Schedules

### Founder + Team (10%)

```
Month 0:     0% unlocked
Month 1-36:  Linear unlock (~2.78% per month)
Month 36:    100% unlocked
```

No cliff — tokens start vesting immediately at TGE.

### Emissions (45%)

```
Year 1: ~20% of emissions released
Year 2: ~25% of emissions released
Year 3: ~30% of emissions released
Year 4: ~25% of emissions released
```

Actual release depends on gauge votes and protocol activity.

### Treasury (13.5%)

- No automatic unlock
- Sales require governance approval
- Capped, transparent, and disclosed

---

## Initial Gauges

At TGE, the following pools are eligible for emissions:

| Pool | Chain | Purpose |
|------|-------|---------|
| cHYPE / HYPE | HyperEVM | Core liquidity |
| cHYPE Pendle Market | HyperEVM | Yield tokenization |

Additional gauges added via veCOMPOST governance.

---

## Token Utility

### veCOMPOST

Lock $COMPOST → receive veCOMPOST (vote-escrowed)

| Lock Duration | veCOMPOST Multiplier |
|---------------|---------------------|
| 1 week | 0.02x |
| 1 month | 0.08x |
| 6 months | 0.5x |
| 1 year | 1x |
| 4 years | 4x |

veCOMPOST decays linearly as lock approaches expiry.

### Governance

veCOMPOST holders vote on:
- Gauge weights (where emissions go)
- New gauge approvals
- Protocol parameters
- Treasury proposals

### Bribes

External protocols can offer bribes to veCOMPOST voters:
- "Vote for our pool to receive emissions"
- "We'll pay you X tokens per vote"

Creates secondary income for veCOMPOST holders.

---

## Treasury Policy

| Rule | Detail |
|------|--------|
| No discretionary dumps | Treasury cannot sell without governance |
| Capped sales | Max 1% of treasury per quarter |
| Disclosure | All sales announced 7 days in advance |
| Use of funds | Audits, integrations, liquidity, grants |

---

## Emissions Schedule

Weekly emissions decrease over 4 years:

| Period | Weekly Emissions | Cumulative |
|--------|-----------------|------------|
| Year 1 | ~1.73M/week | 90M (20%) |
| Year 2 | ~2.16M/week | 202.5M (45%) |
| Year 3 | ~2.6M/week | 337.5M (75%) |
| Year 4 | ~2.16M/week | 450M (100%) |

Note: Actual weekly amounts depend on gauge utilization. Unused emissions roll over.

---

## Anti-Dump Mechanisms

| Mechanism | Effect |
|-----------|--------|
| High float at TGE | No concentrated unlock events |
| Team linear vest (36mo) | No large team dumps |
| Lock tier bonus | Incentivizes long-term holding |
| veCOMPOST utility | Rewards for holding, not selling |
| Treasury governance | No surprise treasury dumps |

---

## Comparison to HYPE

$COMPOST tokenomics are inspired by Hyperliquid's approach:

| Aspect | HYPE | $COMPOST |
|--------|------|----------|
| Team allocation | Low % | 10% |
| Community distribution | High % | 75%+ (airdrop + emissions) |
| Float at TGE | High | ~30%+ |
| Emissions | Staking rewards | Gauge-directed |
| Governance | Core team | veCOMPOST |

---

> Tokenomics are subject to adjustment before TGE based on market conditions and community feedback. All changes will be communicated transparently.
