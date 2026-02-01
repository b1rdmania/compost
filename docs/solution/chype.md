# cHYPE

cHYPE is your receipt token. It represents your share of the vault.

---

## Properties

| Property | Description |
|----------|-------------|
| Standard | ERC-20 |
| Mechanism | Appreciating (not rebasing) |
| Composability | Use in DeFi protocols |
| Liquidity | Tradeable on secondary markets |

---

## How It Works

### Appreciating Token

Unlike rebasing tokens (where your balance changes), cHYPE uses an exchange rate model:

- Your cHYPE balance stays constant
- The exchange rate (cHYPE → HYPE) increases as yield accrues
- When you redeem, you get more HYPE than you deposited

---

## Exchange Rate

> **cHYPE price** = Total HYPE in vault / Total cHYPE supply

**Example:**

| Time | Vault HYPE | cHYPE Supply | Exchange Rate |
|------|------------|--------------|---------------|
| Day 0 | 1,000,000 | 1,000,000 | 1.000 |
| Day 30 | 1,010,000 | 1,000,000 | 1.010 |
| Day 90 | 1,030,000 | 1,000,000 | 1.030 |

Your 100 cHYPE is worth 100 HYPE on Day 0, and 103 HYPE on Day 90.

---

## Composability

cHYPE is a standard ERC-20. Potential use cases include:

### Yield Tokenisation (e.g. Pendle)
Split cHYPE into:
- **PT (Principal Token)** — Fixed yield, redeemable at maturity
- **YT (Yield Token)** — Variable yield exposure

Trade future yield or lock in fixed rates.

### Lending (e.g. Morpho, Euler)
Use cHYPE as collateral on lending protocols. Borrow against your yield position without selling.

### Liquidity
Provide liquidity in cHYPE pairs on DEXs. Earn trading fees on top of vault yield.

::: warning
These are examples of potential integrations. Specific partnerships will be announced as they're confirmed.
:::

---

## Not a Governance Token

cHYPE is the product, not a governance token.

| What cHYPE Is | What cHYPE Isn't |
|---------------|------------------|
| Receipt for vault share | Governance rights |
| Yield-bearing asset | Another token to dump |
| Composable primitive | Speculation vehicle |

There is no separate Compost token.

---

::: info
**Next:** [Architecture](../technical/architecture.md)
:::
