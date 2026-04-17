# Compost Finance - Project Overview (Early Stage)

**For discussion with Hyperliquid ecosystem stakeholders**

---

## What is this?

**Capital formation layer for HIP-3 builder markets.**

Compost pools HYPE to help teams deploy builder markets. Depositors receive cHYPE (a liquid receipt token) and earn:
- Base HYPE staking rewards (~2-4% APY)
- Share of builder market fee splits (50% to builder, we allocate across multiple markets)

Think: Liquid staking (like Lido) meets yield aggregator (like Yearn) for HIP-3 markets specifically.

---

## The Problem We're Solving

**HIP-3 markets require ~500k HYPE stake (~$20M at current prices).**

Most people can't deploy a market alone. Even if you could:
- Which market do you pick?
- How do you vet operators?
- What if it doesn't generate volume?

**Compost diversifies across vetted builder markets** so depositors get:
- Exposure to multiple markets (trade.xyz, Kinetiq, Ventuals, Felix, etc.)
- Professional allocation/vetting
- One token (cHYPE) instead of managing multiple stakes

---

## Current Status

**Very early exploration. Not launched.**

What exists:
- ✅ Brand/landing page (compost.fi)
- ✅ Mockup vault interface (vault.html)
- ✅ Research on staking patterns (Lido, Rocket Pool, StakedHYPE, beHYPE)
- ✅ Basic tokenomics thinking (cHYPE appreciates via exchange rate, not rebasing)

What doesn't exist:
- ❌ Smart contracts
- ❌ Vault implementation
- ❌ Legal structure
- ❌ Capital raise
- ❌ Team beyond founder exploration

---

## Key Questions for Hyperliquid Ecosystem

### 1. **Timing / Market Readiness**

HIP-3 markets are in growth mode with 90% fee reduction. This impacts our thesis:
- Current builder fees are minimal (10% of normal)
- Market volume is growing but still limited
- HIP-4 is on testnet (not live yet)

**Question**: Is this too early? Should we wait until:
- Fee reduction ends (more builder revenue)
- More markets are live (more diversification)
- HIP-4 launches (more market types)

Or is there value in building infrastructure now during the growth phase?

### 2. **API / Integration Requirements**

To build Compost, we'd need:
- **Staking API**: Programmatic HYPE staking (is this exposed? Rate limits?)
- **Market fee tracking**: Real-time or historical fee data per builder market
- **Allocation management**: Ability to stake/unstake across multiple markets
- **Validator selection**: Can we specify validators or is it automatic?

**Question**: What does Hyperliquid expose for programmatic staking? Are there rate limits, minimum stakes, or other constraints we should know about?

### 3. **Competitive Landscape**

**StakedHYPE** ($122M TVL, 2.1% APY): Generic HYPE staking, instant unstake  
**Hyperbeat beHYPE**: HYPE staking + lending/borrowing yields  
**Compost** (proposed): HYPE staking + HIP-3 builder market fee participation

**Question**: Is there demand for a builder-market-focused product? Or do users prefer generic staking + DeFi composability (like beHYPE)?

### 4. **Builder Market Selection**

Current markets: trade.xyz, Kinetiq, Ventuals, Felix, etc.

**Question**: How do we vet builder markets? What signals matter?
- Volume history
- Operator reputation
- Market category (equities, pre-IPO, indices)
- Fee generation track record

And: Do builder deployers want this kind of pooled capital? Or do they prefer direct relationships with large stakers?

### 5. **Fee Splits & Yield Reality**

With 90% fee reduction active:
- Builder gets 5% of fees (instead of 50%)
- Our share would be tiny right now
- Base staking (~2-4%) would be most of the yield

**Question**: Once fee reduction ends, what's realistic APY from builder fees? 
- Depends on volume, obviously
- But order of magnitude: 2-5%? 10%+? 
- Helps us model whether the value prop is compelling

---

## What I'm Looking For

**Honest feedback on viability:**

1. **Timing**: Too early? Wait for more markets / fee reduction to end?
2. **Technical feasibility**: What APIs exist? What's missing?
3. **Market demand**: Would Hyperliquid whales/users use this?
4. **Builder perspective**: Do market deployers want pooled capital or not?
5. **Competitive position**: Better than StakedHYPE/beHYPE or niche too narrow?

**Not looking for:**
- Investment / capital commitments
- Partnership confirmations
- Marketing hype

Just trying to gauge if this is worth building or if the market timing / product-market fit isn't there yet.

---

## Links

- Landing page: https://compost.fi
- Vault mockup: https://compost.fi/vault.html
- HIP-3 stats: https://dune.com/yandhii/hip3

---

## Contact

grow@compost.fi  
@compostfi
