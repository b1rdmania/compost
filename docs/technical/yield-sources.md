# Yield Sources

Compost generates yield from three sources.

---

## 1. Validator Staking

A portion of the vault is staked with Hyperliquid validators.

| Metric | Value |
|--------|-------|
| Base yield | ~2.5% APY |
| Unstake queue | 7 days |
| Purpose | Liquidity buffer for redemptions |

This provides consistent base yield while maintaining liquidity for withdrawals.

---

## 2. HIP-3 Yield (Builder Fees)

The majority of the vault is allocated to HIP-3 markets.

### Mechanisms

HIP-3 yield is not one thing — different markets expose you to fees through different mechanisms.

#### Direct deployment

Compost stakes the 500K HYPE requirement and operates the market directly.

| Aspect | Detail |
|--------|--------|
| Vault earns | Protocol-enforced builder fee share (typically 50%) |
| Trade-off | Highest fee exposure, highest operational burden |
| Status | Phase 2+ consideration |

#### Stake provider arrangements

Capital allocated to a stake provider or structured stake arrangement.

| Aspect | Detail |
|--------|--------|
| Vault earns | Share of builder fees after provider split |
| Trade-off | Terms are market- and counterparty-specific |

#### Pooled staking wrappers

HYPE allocated into a pool that co-owns or has economic rights to a market.

| Aspect | Detail |
|--------|--------|
| Vault earns | Pro-rata share of market revenues |
| Trade-off | Yield depends on pool terms + market volumes |

#### LP / market-making vaults

Non-HYPE capital (often stablecoins) allocated to a market-making strategy.

| Aspect | Detail |
|--------|--------|
| Vault earns | MM PnL + fees |
| Trade-off | Strategy risk; not the same as builder fee share |

#### Collateral-native yield

Yield from collateral rewards rather than stake economics.

| Aspect | Detail |
|--------|--------|
| Vault earns | Collateral rewards (e.g. stablecoin incentives) |
| Trade-off | May be independent of HIP-3 fee flows |

::: warning Potential Markets
Markets and partners listed are examples under consideration. Specific allocations confirmed prior to launch.
:::

### Growth Mode

Most HIP-3 markets run at 90% reduced fees to bootstrap volume.

| Mode | Taker Fee | Effect |
|------|-----------|--------|
| Growth | ~0.45 bps | Lower yield now |
| Standard | ~4.5 bps | Higher yield later |

#### Why this matters for yield

If a market is in Growth Mode, fee-driven yield is roughly **~10x lower** than it will be at standard fees (all else equal).

**Illustrative math (not a forecast):**

```
$32B volume × 4.5 bps ≈ $14.4M total fees
Builder share (50%) ≈ $7.2M to builders

$32B volume × 0.45 bps ≈ $1.44M total fees
Builder share (50%) ≈ $0.72M to builders
```

$32B volume has generated ~$5M fees to date (across markets and fee modes). When markets exit Growth Mode, fee-driven yield can increase materially.

[Live stats →](https://dune.com/yandhii/hip3)

### Allocation Strategy

Compost targets the highest risk-adjusted yield across methods:

- **Fee exposure (HIP-3 fees)** — Prefer transparent, protocol-enforced fee flows where possible
- **Diversification** — Avoid single-operator and single-mechanism concentration
- **Liquidity-aware** — Balance fee yield with redemption liquidity

The mix optimises for yield while managing concentration risk.

---

## 3. Token Incentives

Some deployers distribute token incentives to stakers:
- FELIX
- KNTQ
- Others TBC

### Handling

These tokens are:
1. Held in treasury
2. Sold periodically
3. Used to fund operations

::: info
Token incentives do **not** affect cHYPE yield directly — they're a separate revenue stream for the protocol.
:::

### Why separate from cHYPE yield?

- Incentives may be **non-cash**, time-limited, or contingent on specific actions
- Incentives introduce **token risk** we don't want embedded in the core yield token

---

## Yield Comparison

| Source | Yield | Consistency | Risk |
|--------|-------|-------------|------|
| Validator staking | ~2.5% | High | Low |
| HIP-3 yield (fees + strategies) | Variable | Medium | Medium |
| Token incentives | Variable | Low | Low |

---

::: info
**Next:** [Yield Flow](yield-flow.md)
:::
