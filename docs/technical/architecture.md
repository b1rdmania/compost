# Architecture

Overview of the Compost system architecture.

---

## Diagram

![Architecture Overview](/architecture-diagram.svg)

---

## Components

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin: 24px 0;">
  <div style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; background: #111; border: 1px solid #1a1a1a; border-radius: 4px;">
    <img src="/icons/vault.svg" alt="" style="width: 32px; height: 32px; flex-shrink: 0;" />
    <div>
      <div style="font-weight: 500; color: #e5e5e5;">Vault Contract</div>
      <div style="font-size: 0.875rem; color: #666;">Holds HYPE, manages allocations, handles deposits/withdrawals</div>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; background: #111; border: 1px solid #1a1a1a; border-radius: 4px;">
    <img src="/icons/token.svg" alt="" style="width: 32px; height: 32px; flex-shrink: 0;" />
    <div>
      <div style="font-weight: 500; color: #e5e5e5;">cHYPE Token</div>
      <div style="font-size: 0.875rem; color: #666;">Receipt token, tracks pro-rata share of vault</div>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; background: #111; border: 1px solid #1a1a1a; border-radius: 4px;">
    <img src="/icons/fee.svg" alt="" style="width: 32px; height: 32px; flex-shrink: 0;" />
    <div>
      <div style="font-weight: 500; color: #e5e5e5;">Fee Router</div>
      <div style="font-size: 0.875rem; color: #666;">Splits yield between vault and protocol</div>
    </div>
  </div>
  <div style="display: flex; align-items: flex-start; gap: 12px; padding: 16px; background: #111; border: 1px solid #1a1a1a; border-radius: 4px;">
    <img src="/icons/clock.svg" alt="" style="width: 32px; height: 32px; flex-shrink: 0;" />
    <div>
      <div style="font-weight: 500; color: #e5e5e5;">Withdrawal Queue</div>
      <div style="font-size: 0.875rem; color: #666;">Manages unstaking requests</div>
    </div>
  </div>
</div>

---

## Vault Contract

The core contract that:
- Receives HYPE deposits
- Mints cHYPE at current exchange rate
- Manages allocation to HIP-3 markets and validators
- Processes withdrawals
- Compounds yield

### Key Functions

```solidity
deposit(uint256 amount) → uint256 cHYPEMinted
withdraw(uint256 cHYPEAmount) → uint256 queueId
claimWithdrawal(uint256 queueId) → uint256 HYPEReceived
```

---

## cHYPE Token

Standard ERC-20 with exchange rate tracking.

### Exchange Rate

```
exchangeRate = totalHYPE / totalcHYPE
```

The rate only increases (barring slashing events), making cHYPE an appreciating asset.

---

## Fee Router

Handles yield distribution:

```
Yield received
  └── 15% → Protocol fee
        ├── 90% → Compost operations
        └── 10% → Infrastructure partner
  └── 85% → Compounds into vault
```

---

## Infrastructure

| Item | Status |
|------|--------|
| Infrastructure partner | TBC |
| Multisig | TBC (signers and threshold) |
| Audit | TBC |

---

::: info
**Next:** [Yield Sources](yield-sources.md)
:::
