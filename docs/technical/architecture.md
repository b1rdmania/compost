# Architecture

Overview of the Compost system architecture.

---

## Diagram

![Architecture Overview](/architecture-diagram.svg)

---

## Components

| Component | Function |
|-----------|----------|
| **Vault Contract** | Holds HYPE, manages allocations, handles deposits/withdrawals |
| **cHYPE Token** | Receipt token, tracks pro-rata share of vault |
| **Fee Router** | Splits yield between vault and protocol |
| **Withdrawal Queue** | Manages unstaking requests |

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
