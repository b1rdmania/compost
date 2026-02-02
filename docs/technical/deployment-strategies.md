# Deployment Strategies

How Compost deploys capital across HIP-3 markets.

---

::: warning Beta
This page describes our **current understanding** of deployment options. Mechanisms, terms, and availability change. Specific allocations will be confirmed at launch and updated regularly.
:::

---

## Overview

Compost doesn't just "stake with HIP-3 markets" — each market has a different mechanism for how outside capital can participate. This page breaks down our deployment options market-by-market.

---

## Deployment Approaches

| Approach | What It Means | Compost Use Case |
|----------|---------------|------------------|
| **Direct deployment** | We stake 500K HYPE and operate a market ourselves | Phase 2+ (requires scale) |
| **Stake provider** | We provide stake to a deployer who operates the market | Active discussions |
| **Pooled wrapper** | We deposit into a pool/LST that has market economics | Ready to deploy |
| **LP vault** | We deposit into a market-making vault | Ready to deploy |
| **Collateral yield** | We use reward-bearing collateral on HIP-3 venues | Ready to deploy |

---

## Market-by-Market Breakdown

### trade.xyz (Equities)

**Mechanism:** Direct HIP-3 deployer (builder fee share)

| Aspect | Detail |
|--------|--------|
| What they do | Deploy equity perps (XYZ100, NVDA, TSLA, etc.) |
| How yield works | Builder earns ~50% of trading fees |
| Our access path | No public staking program — would require direct arrangement |
| Capital required | TBD (relationship-dependent) |
| Fee mode | Currently Growth Mode (reduced fees) |
| Expected yield | Low now (Growth Mode), higher when Standard |
| Risks | Counterparty (terms), fee mode timing |
| Status | Researching; no public stake access |

**Compost approach:** Monitor for any public stake program. Explore direct relationship if scale justifies.

---

### Kinetiq Markets / Markets by Kinetiq

**Mechanism:** Pooled wrapper (stake into a program with economic rights)

| Aspect | Detail |
|--------|--------|
| What they do | Global indices and other markets via pooled stake model |
| How yield works | Pro-rata share of market revenues (pool-defined) |
| Our access path | Deposit HYPE into Kinetiq Launch / kmHYPE |
| Capital required | Variable (pool accepts deposits) |
| Fee mode | Market-dependent |
| Expected yield | Variable based on volumes + fee mode |
| Risks | Pool terms, smart contract, fee routing opacity |
| Status | Ready to deploy |

**Compost approach:** Allocate to Kinetiq pools for diversified market exposure. Monitor pool terms and on-chain fee routing.

---

### Felix (Equities)

**Mechanism:** Stake provider / structured stake arrangement

| Aspect | Detail |
|--------|--------|
| What they do | Equity perps (TSLA, more coming) |
| How yield works | Fees split across multiple parties (deployer, stake provider, etc.) |
| Our access path | Participate via stake provider programs (e.g., Hyperion DeFi arrangement) |
| Capital required | Program-dependent |
| Fee mode | Likely Growth Mode initially |
| Expected yield | Fee share after splits — lower than direct deployment |
| Risks | Counterparty (multiple parties), terms opacity, token dependency |
| Status | Researching; evaluating stake provider terms |

**Compost approach:** Evaluate stake provider arrangements. Only deploy if terms are transparent and competitive.

---

### Ventuals (Pre-IPO)

**Mechanism:** LP / market-making vault (VLP)

| Aspect | Detail |
|--------|--------|
| What they do | Pre-IPO perps (SpaceX, OpenAI, Anthropic, etc.) |
| How yield works | VLP vault earns MM PnL + fees |
| Our access path | Deposit into VLP vault |
| Capital required | Variable (vault accepts deposits) |
| Fee mode | Market-dependent |
| Expected yield | Strategy-dependent (MM PnL can be positive or negative) |
| Risks | Strategy risk (MM losses), smart contract, vault terms |
| Status | Ready to deploy |

**Compost approach:** Allocate to VLP with position sizing reflecting strategy risk. This is not pure fee yield — treat as higher-risk/higher-potential bucket.

---

### HyENA (USDe Perps)

**Mechanism:** Collateral-native yield (rewards on balances)

| Aspect | Detail |
|--------|--------|
| What they do | Perps with USDe as collateral (BTC, ETH, SOL, HYPE) |
| How yield works | USDe rewards distributed to collateral holders |
| Our access path | Hold USDe collateral on HyENA |
| Capital required | Variable |
| Fee mode | N/A (yield from collateral, not builder fees) |
| Expected yield | USDe reward rate (Ethena-dependent) |
| Risks | Collateral risk (USDe), smart contract, reward rate changes |
| Status | Ready to deploy |

**Compost approach:** Allocate USDe collateral for base yield. Note: this is collateral yield, not HIP-3 fee yield — different risk profile.

---

### Trove (Collectibles)

**Mechanism:** Direct deployment + token incentives

| Aspect | Detail |
|--------|--------|
| What they do | Collectibles perps (sneakers, cards, watches) |
| How yield works | HIP-3 fees + TROVE token incentives |
| Our access path | No public staking program — would require arrangement |
| Capital required | TBD |
| Fee mode | Likely Growth Mode |
| Expected yield | Fees + potential token upside (speculative) |
| Risks | Niche market volumes, token dependency |
| Status | Monitoring |

**Compost approach:** Monitor volumes. Token incentives are treated separately from core yield.

---

## Yield Expectations by Mechanism

| Mechanism | Growth Mode Yield | Standard Mode Yield | Risk Level |
|-----------|-------------------|---------------------|------------|
| Direct deployment | 1-3% | 8-15%+ | Medium |
| Stake provider | 0.5-2% | 5-10% | Medium |
| Pooled wrapper | 0.5-2% | 4-8% | Low-Medium |
| LP vault | -5% to +15% | -5% to +20% | Higher |
| Collateral yield | 5-15% (USDe) | 5-15% (USDe) | Medium |

**Note:** LP vault yields can be negative (MM losses). All yields are estimates and depend on volumes, fee modes, and market conditions.

---

## Our Allocation Philosophy

| Principle | Implementation |
|-----------|----------------|
| **Diversify mechanisms** | Don't rely on one yield source |
| **Prefer transparency** | Prioritize on-chain fee routing over opaque splits |
| **Size to risk** | Larger allocations to lower-risk mechanisms |
| **Stay liquid** | Avoid long lock-ups where possible |
| **Monitor actively** | Rebalance as fee modes and terms change |

---

## Target Allocation (Illustrative)

| Mechanism | Target % of HIP-3 Sleeve | Notes |
|-----------|--------------------------|-------|
| Pooled wrappers (Kinetiq, etc.) | 30-40% | Diversified, transparent |
| LP vaults (Ventuals VLP) | 15-25% | Higher risk, higher potential |
| Stake provider arrangements | 10-20% | If terms are favorable |
| Collateral yield (HyENA) | 10-20% | Stable, different risk profile |
| Direct deployment | 0% (Phase 2) | Future consideration |

---

## Fee Mode Impact

Most HIP-3 markets currently run in **Growth Mode** (90% fee reduction).

| Mode | Taker Fee | Builder Share | Impact |
|------|-----------|---------------|--------|
| Growth | ~0.45 bps | ~0.225 bps | Low yield now |
| Standard | ~4.5 bps | ~2.25 bps | 10x higher yield |

**Our approach:** Deploy now to capture positioning. Yield improves materially when markets transition to Standard Mode.

---

## What We're Watching

| Signal | Why It Matters |
|--------|----------------|
| Fee mode transitions | Standard Mode = 10x fee yield |
| New stake programs | More access paths for capital |
| Volume growth | More fees to share |
| New market launches | Diversification opportunities |
| Competitor allocations | Market intelligence |

---

## Updates

This page will be updated as:
- We complete due diligence on new markets
- Fee modes change
- Stake programs launch or evolve
- We deploy capital to new venues

---

::: info
**Next:** [Fees](fees.md)
:::
