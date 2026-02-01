# Allocation

How Compost allocates capital across markets.

---

## How Capital Is Allocated

Compost allocates capital across a few buckets. At any point in time these **sum to 100%** (the liquidity bucket is the residual).

### 1. Validator Staking (20-30% of vault)

| Aspect | Detail |
|--------|--------|
| Purpose | Liquidity buffer for redemptions |
| Yield | ~2.5% APY base |
| Queue | 7-day unstake |

Provides consistent base yield while maintaining liquidity.

---

### 2. HIP-3 Strategies (target 50-80% of vault)

HIP-3 exposure can be accessed through different mechanisms depending on the market/operator.

| Aspect | Detail |
|--------|--------|
| Primary source of yield | Trading fees (builder fee share), sometimes strategy PnL |
| Terms | Mechanism-specific (protocol-enforced vs negotiated vs pooled) |
| Objective | Diversified exposure to HIP-3 fee generation |

#### Mechanism types

| Mechanism | What it means | Typical yield driver |
|----------|----------------|----------------------|
| **Builder fee exposure** | Directly earn a share of HIP-3 trading fees | Fee share (often protocol-enforced) |
| **Stake provider arrangements** | Stake is provided/structured by a third party; fees are split across parties | Fee share after the split |
| **Pooled wrappers** | Pool co-owns/has rights to a market; vault earns pro-rata | Pool-defined revenue share |
| **LP / MM vaults** | Capital deployed to market-making strategies around HIP-3 markets | MM PnL + fees (strategy risk) |
| **Collateral-native yield** | Yield comes from collateral rewards rather than fee splits | Collateral rewards |

::: warning
All market/operator examples in the docs are **illustrative**. "Current allocations" and confirmed mechanisms will be published at launch and updated regularly.
:::

---

### 3. Liquidity + In-Transit (residual, typically 0-30%)

Unallocated HYPE used for redemptions, rebalancing, and allocation changes.

| Aspect | Detail |
|--------|--------|
| Purpose | Smooth withdrawals + operational flexibility |
| Yield | May earn 0% while idle |
| Notes | Can temporarily rise during heavy inflows/outflows |

---

### 4. Direct Deployment (0% initially)

Compost deploys its own HIP-3 market.

| Aspect | Detail |
|--------|--------|
| Fee share | 50% (protocol-enforced) |
| Requirement | 500K HYPE minimum + operator responsibility |
| Status | Under evaluation for Phase 2+ |

Future consideration once scale and operations justify the capital commitment.

---

## Allocation Summary

| Channel | % of Vault | Primary yield driver | Status |
|---------|------------|-----------|--------|
| Validator staking | 20-30% | ~2.5% APY | Active |
| HIP-3 strategies | 50-80% | Fees / strategy PnL | Active |
| Liquidity + in-transit | Residual | 0% (when idle) | Active |
| Direct deployment | 0% | Builder fees | Phase 2+ |

---

## Selection Criteria

Before allocating to any HIP-3 strategy, we assess:

### Operator

- Team background and track record
- Previous projects and on-chain history
- Communication and transparency
- Responsiveness to issues

### Market

- Volume history and trajectory
- Fee generation (actual, not projected)
- Oracle quality and update frequency
- Leverage limits and risk parameters
- Fee mode status (e.g. Growth Mode vs standard)
- Operational dependencies (market makers, vault strategy, collateral model)

### Fit

- Correlation with existing allocations
- Category diversification
- Liquidity profile

---

## Governance

Allocation decisions are made by the Compost team with oversight from an independent advisory committee.

| Aspect | Detail |
|--------|--------|
| Decision maker | Compost team |
| Oversight | Independent advisory committee |
| Transparency | All allocations and terms published |

---

## Current Allocations

::: warning
Allocations will be published on launch and updated regularly.
:::

| Market | Category | Allocation % | Method |
|--------|----------|--------------|--------|
| TBC | TBC | TBC | TBC |

---

## Limits

| Constraint | Limit |
|------------|-------|
| Single market | Max 25% of vault |
| Single operator | Max 40% of vault |
| Unproven markets | Structured exposure only (no large direct concentration) |

---

::: info
**Next:** [Fees](fees.md)
:::
