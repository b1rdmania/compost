# HIP-3 Yield Mechanisms — Research Notes (Feb 2026)

This page summarizes **how HIP-3 markets appear to raise/lock capital and route yield**, based on public documentation and third-party writeups available at the time of writing.

:::: warning
This is **research**, not a guarantee. Mechanisms, fee modes (e.g. Growth Mode), and terms can change. Treat all “examples” as illustrative and verify from primary sources.
::::

---

## The core primitive (what HIP-3 enforces)

Across HIP-3 markets, the protocol-level idea is:

- A market exists because a large stake requirement is met (commonly discussed as **500K HYPE** for deployment).
- Fees can be configured in modes (notably “Growth Mode” vs “Standard”).
- Builder economics are primarily expressed as a **share of trading fees** (often described as **50% to the builder** in standard configurations).

This is the “cleanest” yield source: **fee revenue** tied to market volume, not emissions.

---

## Mechanism taxonomy (how “HIP-3 yield” reaches participants)

Different markets wrap the base primitive in different ways. These are the buckets we found most useful:

| Mechanism | What it means in practice | What the yield actually is |
|----------|----------------------------|----------------------------|
| **Direct deployer fee share** | Builder deploys and earns protocol-defined fee share | Trading fees (mode-dependent) |
| **Stake provider / stake-as-a-service** | A third party supplies/structures the required stake and takes a cut | Trading fees split across parties |
| **Pooled wrapper / co-ownership** | Users stake into a pool/LST-style wrapper that has defined economic rights | Pro-rata share of market revenues (pool-defined) |
| **LP / market-making vault** | Users deposit into a vault that market-makes a HIP-3 venue | MM PnL + fees (strategy risk), sometimes external yield |
| **Collateral-native yield** | Yield comes from reward-bearing collateral balances | Collateral rewards, often daily/weekly |
| **Token incentives / points** | Airdrops/emissions/points layered on top | Separate, non-guaranteed, often non-cash |

---

## Fee modes matter (Growth Mode vs Standard)

If a market runs in a reduced-fee “Growth Mode” regime, fee-driven yield is typically **materially lower** than under standard fees (often described as ~90% lower in aggregate).

**Illustrative math (not a forecast):**

```
$25B volume × 4.5 bps ≈ $11.25M total fees
Builder share (50%) ≈ $5.6M to builders

$25B volume × 0.45 bps ≈ $1.125M total fees
Builder share (50%) ≈ $0.56M to builders
```

---

## Market-by-market notes (non-exhaustive)

### trade.xyz (equities perps)

- **Mechanism**: Direct HIP-3 deployer fee share (builder earns share of trading fees).
- **Public references**:
  - `https://docs.trade.xyz/about-trade-xyz/hyperliquid-xyz-and-hip-3`
  - `https://docs.trade.xyz/trading/fees`
- **Notes**:
  - Public docs describe **fee split** and note that Growth Mode can reduce fees significantly.
- **Unknowns (for “staking yield”)**:
  - Whether there is any *separate* staking program distributing the builder’s fee share beyond the builder entity itself.

### Kinetiq Markets / “Markets by Kinetiq”

- **Mechanism**: Pooled/wrapper-style exposure (stake into a program that “co-owns” economic rights).
- **Public references**:
  - `https://kinetiq.xyz/launch/markets-by-kinetiq`
  - `https://kinetiq.xyz/kntq`
- **Notes**:
  - Public material describes a pooled stake model and a stated revenue-share concept.
- **Unknowns**:
  - Exact fee routing details (timing, on-chain vs off-chain), oracle costs, and the net yield after costs.

### Felix (equities; TSLA mentioned publicly)

- **Mechanism (as described publicly)**: Stake-provider / structured stake arrangement (third party provides stake; fees split across multiple parties).
- **Public references**:
  - `https://ir.hyperiondefi.com/node/11211/pdf` (partnership communication)
  - `https://medium.com/@felix-protocol/qualify-for-the-felix-protocol-airdrop-october-2025-259e95d49bd7`
- **Notes**:
  - Public comms describe fee distributions across multiple parties and a points/token program layered on top.
- **Unknowns**:
  - Exact percentages of fee splits and how (or if) any stakeholder program passes through fee yield.

### Ventuals (pre-IPO perps)

- **Mechanism**: LP / market-making vault exposure (VLP-style vault).
- **Public references**:
  - `https://docs.ventuals.com/providing-liquidity/vlp`
  - `https://docs.hyperbeat.org/hyperbeat-earn/ventuals-hip-3-vlp-vault` (third-party vault writeup)
- **Notes**:
  - Yield described as market-making/trading profits + potential integrated strategy yield.
- **Unknowns**:
  - Exact allocation of deployer fee share vs vault participants; net yield after strategy costs/risks.

### HyENA (USDe perps)

- **Mechanism**: Collateral-native yield (rewards on balances/collateral).
- **Public references**:
  - `https://docs.hyena.trade/usde-rewards`
  - `https://www.rootdata.com/news/457090` (third-party coverage)
- **Notes**:
  - Yield is described in terms of **USDe rewards** on balances, not primarily “builder fee share to stakers.”
- **Unknowns**:
  - Whether/where the builder’s fee share flows to any “staking” layer.

### Trove (collectibles perps; additional notable market)

- **Mechanism (reported)**: HIP-3 deployment + token incentives/utility token.
- **Public references**:
  - `https://learn.trovemarkets.com/hip-3/trove-on-hip-3`
  - `https://whales.market/blog/what-is-trove/` (third-party writeup)
- **Notes**:
  - Useful example of a project combining market deployment with token incentive design.
- **Unknowns**:
  - Exact fee pass-through mechanics and emissions schedule.

---

## Implications for Compost (what this research changed)

- “HIP-3 yield” needs to be modeled as **multiple mechanism types**, not just “partner allocations.”
- For near-term projections, **fee mode (Growth vs Standard)** is a first-order driver.
- Token incentives should be treated as **separate** from core fee yield unless there’s a clear, durable policy for capture/distribution.

---

## Source list (quick links)

- trade.xyz: HIP-3 overview — `https://docs.trade.xyz/about-trade-xyz/hyperliquid-xyz-and-hip-3`
- trade.xyz: fees — `https://docs.trade.xyz/trading/fees`
- Kinetiq: Markets by Kinetiq — `https://kinetiq.xyz/launch/markets-by-kinetiq`
- Kinetiq: KNTQ — `https://kinetiq.xyz/kntq`
- Ventuals: VLP — `https://docs.ventuals.com/providing-liquidity/vlp`
- HyENA: USDe rewards — `https://docs.hyena.trade/usde-rewards`
- Felix: airdrop/points — `https://medium.com/@felix-protocol/qualify-for-the-felix-protocol-airdrop-october-2025-259e95d49bd7`
- Hyperion DeFi: Felix partnership comms — `https://ir.hyperiondefi.com/node/11211/pdf`
- Trove: HIP-3 explainer — `https://learn.trovemarkets.com/hip-3/trove-on-hip-3`
- Trove: third-party writeup — `https://whales.market/blog/what-is-trove/`

