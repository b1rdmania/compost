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

## 2. HIP-3 Builder Fees

The majority of the vault is allocated to HIP-3 markets.

### Fee Share by Method

| Method | Fee Share | Notes |
|--------|-----------|-------|
| Direct deployment | 50% | Protocol-enforced, requires 500K HYPE stake |
| Partner allocation | 20-40% | Negotiated with deployers (Felix, Ventuals, etc.) |
| Pooled staking | Variable | Via Kinetiq Launch or similar, pro-rata share |

### Allocation Strategy

Compost targets the highest risk-adjusted yield across methods:

- **Direct deployment** — Higher yield, higher capital requirement
- **Partner allocations** — Lower yield, better diversification

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

---

## Yield Comparison

| Source | Yield | Consistency | Risk |
|--------|-------|-------------|------|
| Validator staking | ~2.5% | High | Low |
| HIP-3 fees | Variable (10-50%+) | Medium | Medium |
| Token incentives | Variable | Low | Low |

---

::: info
**Next:** [Yield Flow](yield-flow.md)
:::
