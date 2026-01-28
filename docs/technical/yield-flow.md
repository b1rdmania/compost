# Yield Flow

How yield moves from source to your cHYPE.

---

## Diagram

![Yield Flow](/yield-flow-diagram.svg)

---

## Step by Step

### Step 1: User Deposits HYPE

```
User sends HYPE to Vault
  └── Vault receives HYPE
  └── cHYPE minted at current exchange rate
  └── User receives cHYPE
```

**Example:** User deposits 1,000 HYPE when exchange rate is 1.05. They receive 952.38 cHYPE (1000 / 1.05).

---

### Step 2: Vault Allocates HYPE

```
Vault allocates capital:
  ├── 20-30% → Validator staking (liquidity buffer)
  └── 70-80% → HIP-3 markets (yield generation)
```

Allocation percentages may vary based on:
- Redemption demand
- Market opportunities
- Risk management

---

### Step 3: Yield Accrues

```
Yield flows in from:
  ├── Staking rewards: claimed daily
  ├── Builder fees: distributed per epoch (varies by market)
  └── Token incentives: held in treasury
```

Different yield sources have different timing:
- Validator rewards: continuous
- HIP-3 fees: epoch-based (market dependent)

---

### Step 4: Protocol Fee Deducted

```
Gross yield received
  └── Protocol fee deducted (15% of yield)
        ├── 90% → Compost operations
        └── 10% → Infrastructure partner
```

The 15% fee is taken on yield only — not on principal.

---

### Step 5: Net Yield Compounds

```
Net yield (85%) enters vault
  └── Vault HYPE balance increases
  └── cHYPE exchange rate increases
  └── All cHYPE holders benefit proportionally
```

No action required. cHYPE automatically appreciates.

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
