# Yield Flow

How yield moves from source to your cHYPE.

---

## Diagram

![Yield Flow](/yield-flow-diagram.svg)

---

## How Capital Moves

### Deposit
1. You deposit HYPE
2. Vault mints cHYPE at current rate
3. You receive cHYPE

### Allocation
Vault splits HYPE two ways:

- **Validators (20-30%)** — Staked with Hyperliquid validators, ~2.5% APY, 7-day unstake
- **HIP-3 Markets (50-70%)** — Staked with deployers (Felix, Kinetiq, etc.), 20-40% of trading fees

### Yield
1. Fees and rewards flow to vault
2. 15% taken as protocol fee (on yield, not principal)
3. Net yield (85%) compounds
4. cHYPE exchange rate rises

### Withdrawal
1. Burn cHYPE
2. HYPE queued (7-14 days) or sell cHYPE on DEX

---

## Exchange Rate Example

| Time | Vault HYPE | cHYPE Supply | Exchange Rate |
|------|------------|--------------|---------------|
| Day 0 | 1,000,000 | 1,000,000 | 1.000 |
| Day 30 | 1,010,000 | 1,000,000 | 1.010 |
| Day 60 | 1,020,100 | 1,000,000 | 1.020 |
| Day 90 | 1,030,301 | 1,000,000 | 1.030 |

Your cHYPE balance stays constant. Its value in HYPE increases.

---

::: info
**Next:** [Allocation](allocation.md)
:::
