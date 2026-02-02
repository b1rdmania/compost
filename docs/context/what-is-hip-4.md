# What is HIP-4?

::: warning
**Testnet only.** HIP-4 is currently being tested on testnet. Mainnet deployment will follow once technical development is complete.
:::

HIP-4 introduces **outcome trading** — fully collateralized contracts that settle within a fixed price range.

---

## How It Works

Outcomes are a new primitive for Hyperliquid, distinct from perpetual futures (HIP-3).

Key characteristics:
- **Fully collateralized** — no margin calls, no liquidation risk
- **Fixed range** — contracts settle at a price within a specified range
- **Dated markets** — unlike perpetuals, these have expiry dates
- **Non-linear payoffs** — enables options-like instruments

---

## Use Cases

| Application | Description |
|-------------|-------------|
| Prediction markets | Binary or multi-outcome event contracts |
| Bounded options | Options-style derivatives with capped risk |
| Insurance products | Collateralized coverage contracts |
| Novel applications | Builders will likely create new use cases |

---

## Current Status

- **Testnet**: Live for testing
- **Mainnet**: Pending technical completion
- **Initial markets**: Curated canonical markets with objective settlement sources
- **Future**: Potentially permissionless deployment (pending user feedback)

Canonical markets will be denominated in **USDH** (Hyperliquid's native stablecoin).

---

## How It Differs from HIP-3

| Feature | HIP-3 (Perps) | HIP-4 (Outcomes) |
|---------|---------------|------------------|
| Contract type | Perpetual futures | Dated, fixed-range |
| Leverage | Yes | No (1x isolated) |
| Liquidation risk | Yes | No |
| Payoff structure | Linear | Non-linear |
| Primary use | Trading exposure | Prediction markets, options |

---

## Compost and HIP-4

As HIP-4 matures and deployment economics are confirmed, Compost may allocate to HIP-4 markets alongside HIP-3 — providing depositors exposure to both perpetual and outcome-based yield sources.

---

## Official Resources

- [Hyperliquid announcement](https://x.com/HyperliquidX/status/2018327360723202167)

---

::: info
**Next:** [The Opportunity](the-opportunity.md)
:::
