# Launch Spec

Everything a staker needs to know in 2 minutes.

---

## Vault Structure

Deposit HYPE → receive **cHYPE** (appreciating receipt token).

| Bucket | Target % | Yield Driver |
|--------|----------|--------------|
| Validator staking | 20-30% | ~2.5% APY (HYPE staking rate) |
| HIP-3 strategies | 50-80% | Builder fees + strategy PnL |
| Liquidity buffer | Residual | 0% (used for redemptions) |

cHYPE is ERC-20, composable in DeFi (Pendle, lending, LP).

---

## Fees

| Fee | Amount | Notes |
|-----|--------|-------|
| Deposit | None | |
| Withdrawal | None | |
| Management | 0.5% on HIP-3 sleeve | ~0.25% of total AUM if sleeve = 50% |
| Performance | 15% of excess return | Only above HYPE staking APR hurdle |

### Performance fee hurdle

We only charge performance fees on returns **above the default HYPE staking rate** (~2.37% at 400M staked).

**Example:**
- Vault generates 8% yield
- HYPE staking rate: 2.5%
- Excess return: 5.5%
- Performance fee: 15% × 5.5% = 0.825%
- Net yield to holders: ~7.175%

If yield ≤ staking rate → no performance fee.

---

## Points

Points accrue based on cHYPE holdings and LP activity.

| Activity | Multiplier |
|----------|------------|
| Hold cHYPE | 1x |
| LP in whitelisted pools | 2x |

Points are non-transferable and determine eligibility for:
- Future token airdrops
- Protocol incentives
- Any HIP-3 token rewards we receive

---

## $COMPOST Tokenomics

| Allocation | % of Supply | Vesting |
|------------|-------------|---------|
| Founder + team | 10% | 36-month linear (no cliff) |
| Genesis airdrop | 30% | Liquid (see oversubscription rule) |
| Emissions (ve/gauges) | 45% | Released over 4 years via gauges |
| Treasury / POL / integrations | 13.5% | Governed, no discretionary dumps |
| Legion raise + lock bonus | 1.5% | See raise mechanics |

### Token utility

- **veCOMPOST** — vote-lock for governance + gauge voting
- **Gauges** — direct emissions to cHYPE pools (Pendle, DEXs)
- **Bribes** — protocols bribe veCOMPOST voters for emissions

---

## TGE Raise

$1M raised via Legion-style mechanism.

| Tier | Lock | Bonus |
|------|------|-------|
| Liquid | None | Base allocation only |
| Locked | 12 months | +50% bonus tokens (locked with base) |

### Oversubscription rule

If raise is oversubscribed:
- 90% of allocation goes to lock-tier participants
- 10% to liquid-tier

This rewards long-term commitment.

---

## Founder Secondary

- **0.5% of total supply** sold OTC at TGE
- Fully disclosed, locked buyer(s)
- No surprise unlocks

---

## What's Liquid at TGE

| Category | Liquid | Locked |
|----------|--------|--------|
| Airdrop (30%) | Yes* | — |
| Founder + team (10%) | — | 36mo linear vest |
| Legion liquid tier | Yes | — |
| Legion lock tier | — | 12 months |
| Emissions | — | Released via gauges |
| Treasury | — | Governed sales only |

*If raise is heavily oversubscribed, airdrop recipients may choose lock-for-bonus.

---

## Initial Gauges (TGE)

| Pool | Chain |
|------|-------|
| cHYPE / HYPE | HyperEVM |
| cHYPE Pendle market | HyperEVM |

Additional gauges added via governance.

---

## Reporting

| Metric | Frequency |
|--------|-----------|
| Vault NAV + exchange rate | Real-time (on-chain) |
| Allocation breakdown | Weekly |
| Fee accrual | Weekly |
| Performance vs hurdle | Monthly |

---

## Contact

- **Email:** grow@compost.fi
- **Twitter:** [@compostfi](https://twitter.com/compostfi)
- **Docs:** [docs.compost.fi](https://docs.compost.fi)

---

> This spec is current as of TGE planning. Terms may adjust based on market conditions. All changes will be communicated in advance.
