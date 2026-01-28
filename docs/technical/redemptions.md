# Redemptions

How to exit your Compost position.

---

## Two Exit Paths

### 1. Protocol Redemption

Standard withdrawal through the vault.

```
1. Burn cHYPE
2. HYPE queued for withdrawal
3. 14-day unstake period (Hyperliquid protocol constraint)
4. HYPE released after queue clears
```

**No fee on principal.** Protocol fee is already taken on yield.

### 2. Secondary Market

Instant exit via DEX.

```
1. Sell cHYPE on DEX
2. Receive HYPE (or other token) immediately
3. No protocol interaction required
```

**Price may differ from NAV** — premium or discount depending on demand.

---

## Comparison

| Aspect | Protocol Redemption | Secondary Market |
|--------|---------------------|------------------|
| Speed | 14 days | Instant |
| Price | NAV (exact) | Market (variable) |
| Slippage | None | Depends on liquidity |
| Fees | None | DEX fees + slippage |

---

## Liquidity Buffer

20-30% of vault is kept in validator staking (not HIP-3 allocated).

### Purpose

| Function | Benefit |
|----------|---------|
| Cover normal redemptions | No need to unwind HIP-3 positions |
| Maintain base yield | Earning during rebalancing |
| Shorter queue | 7 days vs 14 for validator unstaking |

---

## Large Redemptions

Redemptions >5% of vault may be processed in tranches.

### Why

- Avoid market impact
- Prevent forced position unwinding
- Maintain orderly operations

### Process

1. Initial tranche processed (up to 5%)
2. Remaining amount queued
3. Processed as liquidity becomes available
4. Full communication throughout

---

## Edge Cases

| Scenario | Handling |
|----------|----------|
| **Bank run** | Redemptions processed FIFO, HIP-3 positions unwound as needed |
| **Market dislocation** | Secondary market price may diverge from NAV |
| **Slashing event** | Loss absorbed pro-rata by all cHYPE holders |

---

## Queue Status

Check your withdrawal status:
- On-chain: Query vault contract
- Dashboard: [TBC]
- API: `GET /withdrawal/{queueId}`

---

{% hint style="info" %}
**Next:** [Risk](risk.md)
{% endhint %}
