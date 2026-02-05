# Vault Page Research & Analysis

## Similar Projects Identified

### 1. **Liquid Staking Protocols**
Projects that allow users to stake native tokens and receive liquid receipt tokens in return.

#### Lido (stake.lido.fi)
- **Product**: Stake ETH → Receive stETH
- **TVL**: $33.9B
- **APR**: 3.2% net (10% protocol fee)
- **Minimum**: 0.0001 ETH
- **Most similar to Compost**: Yes - same core model (stake → receive liquid token → earn yield)

#### Rocket Pool
- **Product**: Stake ETH → Receive rETH
- **TVL**: $2.1B
- **APR**: 3.4% net (15% fee)
- **Focus**: Decentralization, permissionless validators

#### StakedHYPE (www.stakedhype.fi)
- **Product**: Stake HYPE → Receive stHYPE (Hyperliquid ecosystem)
- **TVL**: $122.28M
- **APY**: 2.1%
- **Most directly competitive**: Yes - same underlying asset (HYPE), same chain
- **Key features**: Instant unstake, real-time balance increases, governance rights

#### Hyperbeat beHYPE (app.hyperbeat.org)
- **Product**: Stake HYPE → Receive beHYPE (collaboration with Etherfi)
- **Additional feature**: liquidHYPE vault (automated yield strategy on top of staking)
- **Most directly competitive**: Yes - same underlying asset, integrates with Felix/Hyperlend/Hypurrfi

### 2. **Vault Aggregators**
Projects that pool capital and allocate across multiple yield strategies.

#### Yearn Finance
- **Product**: Deposit → Automated yield optimization across protocols
- **TVL**: Growing daily
- **Key innovation**: v3.0 - transaction simulation, predicted earnings, detailed APY breakdown
- **Most similar to Compost**: Partial - Compost allocates across markets similar to how Yearn allocates across protocols

#### Beefy Finance
- **Product**: Multi-chain yield aggregator with auto-compounding
- **Focus**: Reasonable fees, transparent strategies, multi-chain

### 3. **Index/Pooled Staking**
Projects that pool capital for diversified exposure.

#### Index Coop - icETH
- **Product**: Leveraged liquid staking (2.5x ETH staking yield)
- **TVL**: $3.2M
- **Mechanism**: Deposits stETH on Aave v2, borrows ETH, converts to more stETH (leverage loop)
- **Key feature**: Passive yield compounds to token price, automated rebalancing
- **Most similar to Compost**: Partial - single token that appreciates, sophisticated strategy

#### Index Coop - dsETH
- **Product**: Diversified basket of liquid staking tokens (rETH + stETH + sETH2)
- **Focus**: Diversification across validators, decentralization
- **Most similar to Compost**: Yes - diversification model similar to Compost allocating across multiple builder markets

---

## Vault Page UI/UX Patterns Analysis

### **1. Hero/Metrics Section** (Universal)

All projects prominently display:

**Lido:**
- Clean minimalist design
- Large "Stake Ether" headline
- FAQ accordion immediately visible

**StakedHYPE:**
- Top banner: TVL ($122.28M) | HYPE STAKED (4.0M) | APY (2.1%)
- "Stay Liquid" tagline
- Strong visual brand identity (logo prominent)

**Hyperbeat beHYPE:**
- Tab navigation: Stake | Unstake | Instant Redeem
- TVL, Hype staked, APY, Holders shown as cards
- Validator selection dropdown

**Index Coop icETH:**
- "$3,208,574.06 in TVL" as trust signal
- "Multiply returns on ETH staking rewards by up to 2.5x" value prop
- Available networks badge

**Yearn:**
- Simple: "$0 deposited in Yearn Vaults" (personalized when connected)
- "Earn on your Crypto" headline
- Minimal, trust-focused

**Pattern identified**: 
- Large, clear metrics (TVL, APY) establish credibility
- Personalized view when wallet connected
- Simple value proposition headline

---

### **2. Main Action Panel** (Deposit/Withdraw)

**Lido:**
- Single input box (no tabs needed - separate pages for withdrawals)
- Shows: Amount input → stETH you'll receive
- Clean, minimal friction

**StakedHYPE:**
- Dedicated `/stake` page (based on CTA)
- Likely similar to Hyperbeat pattern below

**Hyperbeat beHYPE:**
- **Three tabs**: Stake | Unstake | Instant Redeem
- **Stake tab shows**:
  - Input: HYPE amount (with "Half" and "Max" buttons)
  - Validator selection dropdown
  - Output: Calculated beHYPE amount
  - "Staking breakdown" section
  - Exchange rate shown
  - Network cost estimate (~$0.01)
- **Validator table** below with columns: Name, behype Stake, validator Stake, Uptime, APR, Status

**Lido Withdrawals:**
- **Two-step process**:
  1. Request tab: Lock stETH/wstETH, wait 1-5 days for processing
  2. Claim tab: Claim ETH once ready
- NFT-based request tracking (each withdrawal = NFT)
- Shows estimated waiting time
- Clear warnings about 14-day periods

**Index Coop icETH:**
- "Earn on ETH" CTA button
- Likely routes to app.indexcoop.com with ETH→icETH trade interface

**Pattern identified**:
- Tab structure (Stake/Unstake) is standard
- Input/Output preview with exchange rate
- Helper buttons (Half, Max) reduce friction
- Clear network cost estimates
- Validator selection for decentralization

---

### **3. Yield Details & Performance**

**Lido:**
- FAQ section explaining APR calculation:
  - Protocol APR = (CL + EL rewards) / total pooled ETH
  - Your APR = Protocol APR × (1 - 10% fee)
- 7-day moving average
- Warning: "APR figures are estimates, subject to change"

**Hyperbeat beHYPE:**
- APY displayed prominently
- "Have beHYPE? Earn up to [X] APY" - promotes vault product
- Shows liquidHYPE vault as next step

**StakedHYPE:**
- 2.1% APY shown in header
- "Maximised Rewards" - explains HYPE distributed to top validators
- Validator partners showcased

**Index Coop icETH:**
- "Multiply returns... by up to 2.5x"
- No live APY shown (strategy-dependent)
- Detailed methodology section explaining leverage mechanics

**Yearn:**
- Individual vault cards show APY per vault
- Historical performance data available
- Detailed APY breakdown (Base APY + Boost APY + Rewards)

**Pattern identified**:
- Transparency in APY calculation
- Historical data builds trust
- Always include disclaimers about estimates
- Show components of yield (base staking + additional sources)

---

### **4. Allocation/Strategy Transparency**

**StakedHYPE:**
- "Fully Transparent" - Every stHYPE backed 1:1 with native HYPE
- "Validator Partners" section with logos (ASXN, B-Harvest, Infinite Field, HyperStake, ValiDAO, HypurrCollective)

**Hyperbeat beHYPE:**
- Validator table shows exact distribution
- "More DeFi opportunities" table lists protocols/markets (with Supply APY, Borrow APY, TVL)
- Rewards badges (Etherfi, Hyperlend, Felix, Hypurrfi logos)

**Lido:**
- "Committee of elected, best-in-class validators"
- Not granularly shown on main page

**Yearn:**
- Strategy details in vault-specific pages
- "Transparent strategies with clear documentation"

**Index Coop dsETH (diversified):**
- Shows basket composition: rETH + stETH + sETH2
- Weightings favor decentralization

**Pattern identified**:
- Show where capital is allocated (validators, protocols, markets)
- Visual trust signals (partner logos, validator names)
- For Compost: Could show "Allocated to: trade.xyz (40%), Kinetiq (30%), Ventuals (20%)" etc.
- Link to on-chain verification

---

### **5. Trust & Security Section**

**StakedHYPE:**
- "Audited & Secure" - links to GitHub audits
- "Smart contracts audited by top tier auditors"
- "Fully non-custodial"
- "User Governed" - stHYPE holders vote

**Lido:**
- Extensive FAQ on security measures:
  - Open-source code
  - Multiple audits (Certora, StateMind, Hexens, ChainSecurity, etc.)
  - Immunefi bug bounty program
  - Non-custodial
  - DAO governance
- Separate FAQ on risks:
  - Smart contract security
  - Slashing risk
  - stToken price risk

**Index Coop:**
- "8+ audits from industry leading security firms"
- Links to: Audits | Protocol Documentation | Bug Bounty Program
- All contracts open source

**Hyperbeat:**
- Custody partners shown via logos
- "Non-custodial" mentioned

**Pattern identified**:
- Audits are mandatory trust signal (link to reports)
- Open source emphasized
- Bug bounty programs
- Clear risk disclosures (especially for liquid staking: slashing, smart contract)
- For Compost: Highlight Infrasingularity (vault) + Fireblocks (custody)

---

### **6. Activity/Portfolio View** (Connected wallet)

**Hyperliquid Native Staking:**
- Clean dashboard with sections:
  - **Staking Balance**: Available to Transfer, Available to Stake, Total Staked, Pending Transfers
  - **Validator Performance** table
  - **Staking Reward History** (7D view)
  - **Staking Action History**
- "View All" links for deeper views

**Yearn:**
- "$0 deposited in Yearn Vaults" updates to show your position
- Likely detailed portfolio view in app

**Lido:**
- Separate "Rewards" page
- Tracks your staking rewards over time

**Pattern identified**:
- Dashboard splits into: Position | History | Actions
- Clear balance breakdowns
- Historical performance of YOUR position
- For Compost: Show "Your HYPE staked", "Your cHYPE balance", "Your current value", "Lifetime fees earned"

---

### **7. Additional Features/Next Steps**

**StakedHYPE:**
- "Use in DeFi" section
- "stHYPE can be used across the Hyperliquid ecosystem for additional yield, borrowing, lending"
- Simple staking value prop: "Your underlying HYPE balance increases in real-time... instant unstake"

**Hyperbeat beHYPE:**
- **Promotes vault on staking page**: "Have beHYPE? Earn up to [X] APY"
- Shows liquidHYPE vault card with deposit option
- "More DeFi opportunities" table links to lending protocols

**Index Coop icETH:**
- "Automatically Managed" - no gas costs or manual upkeep
- FAQs explain: No need to claim/compound (accrues to token price)
- Instantly redeemable

**Lido:**
- "Earn" tab shows vault opportunities (integrations)
- Link to ecosystem page with all integrations

**Pattern identified**:
- Cross-sell additional yield opportunities
- Educate on composability (use receipt token elsewhere)
- For Compost: Could show "cHYPE integrations coming soon" or "Trade cHYPE on [DEX]"

---

## Design Patterns Summary

### Layout Structure (Most Common):

```
1. HERO/METRICS BAR
   - TVL, APY, Key Metrics
   - Value proposition headline

2. MAIN ACTION PANEL (center focus)
   - Tab navigation: Stake | Unstake
   - Input amount → Output preview
   - Helper buttons (Half, Max)
   - Exchange rate display
   - Action button (large, prominent)

3. DETAILS PANEL (below or side)
   - Yield breakdown
   - Network cost estimate
   - Transaction preview

4. ALLOCATION/STRATEGY SECTION
   - Where capital goes (validators, markets, protocols)
   - Visual logos/names
   - Performance metrics per allocation

5. TRUST/SECURITY SECTION
   - Audits (link to reports)
   - Partners (custody, infrastructure)
   - Risk disclosures

6. PORTFOLIO/ACTIVITY (if connected)
   - Your position
   - Historical rewards
   - Action history

7. EDUCATION/FAQ
   - How it works
   - Risk explanations
   - Process details

8. NEXT STEPS/INTEGRATIONS
   - Use your receipt token
   - Additional yield opportunities
```

---

## Key UX Principles Observed

1. **Progressive Disclosure**: Simple interface upfront, details available on demand
2. **Transaction Simulation**: Show expected output BEFORE user commits
3. **Clear Status Indicators**: Loading, confirmation, error states
4. **Mobile-First**: All projects work well on mobile (tab patterns, large buttons)
5. **Trust Signals Early**: TVL, audits, partners visible immediately
6. **Realistic Disclaimers**: APY estimates, risks clearly stated
7. **Low Friction**: Max/Half buttons, single-click actions where possible
8. **Validator Choice**: For decentralization, let users pick (or show auto-selection logic)

---

## Compost-Specific Considerations

### What makes Compost different:

1. **Capital allocation to builder markets** (not generic staking)
   - Need to show: Which markets we're allocated to
   - Market performance metrics
   - Links to individual market pages

2. **Dual yield sources**:
   - Base HYPE staking rewards (~2-4% APY)
   - Builder fee splits (variable, depends on volume)
   - Should show breakdown: "Base: X% + Builder fees: Y% = Total: Z%"

3. **cHYPE exchange rate appreciation** (not rebasing)
   - Show: "1 cHYPE = X HYPE" (increases over time)
   - Graph: cHYPE/HYPE exchange rate history

4. **14-day unstake period** (important friction point)
   - Must warn prominently
   - Show: "Unstake now → Claimable in 14 days"
   - Consider: Instant exit via DEX (if liquidity exists)

5. **Market selection/allocation transparency**
   - Compost decides allocation (not user)
   - Must show: Why these markets? Performance? Fees earned?
   - "View all allocations on-chain" CTA

---

## Recommended Vault Page Structure for Compost

### **Section 1: Hero/Metrics**
```
┌─────────────────────────────────────────┐
│  compost.fi                    [Connect]│
├─────────────────────────────────────────┤
│                                         │
│   TVL: $X.XM  |  APY: X.X%  |  Users: X│
│                                         │
│   Stake HYPE. Earn from Hyperliquid    │
│   builder market fees.                  │
│                                         │
└─────────────────────────────────────────┘
```

### **Section 2: Main Action Panel**
```
┌─────────────────────────────────────────┐
│  [ Stake ]  [ Unstake ]                │
├─────────────────────────────────────────┤
│                                         │
│  You stake                              │
│  [_________] HYPE     [Half] [Max]     │
│  Balance: X.XX HYPE                     │
│                                         │
│  You receive                            │
│  X.XXXX cHYPE                          │
│                                         │
│  Exchange rate: 1 cHYPE = X.XX HYPE    │
│  Network cost: ~$0.01                   │
│                                         │
│  [    STAKE HYPE    ]  ← large button  │
│                                         │
└─────────────────────────────────────────┘
```

### **Section 3: Yield Breakdown**
```
┌─────────────────────────────────────────┐
│  Current APY: X.X%                      │
│  ├─ Base staking: X.X%                 │
│  └─ Builder fees (30d avg): X.X%       │
│                                         │
│  [APY Chart: 7D | 30D | 90D | All]     │
│                                         │
│  Projected earnings:                    │
│  If you stake 1000 HYPE for 1 year...  │
│  → Earn ~XX HYPE (at current rates)    │
└─────────────────────────────────────────┘
```

### **Section 4: Market Allocations**
```
┌─────────────────────────────────────────┐
│  Where your HYPE is working             │
├─────────────────────────────────────────┤
│  ┌─────────────────────────┐            │
│  │ trade.xyz        40%    │            │
│  │ $12.7B volume | Live    │            │
│  │ Fees earned: $XXk (30d) │            │
│  └─────────────────────────┘            │
│                                         │
│  ┌─────────────────────────┐            │
│  │ Kinetiq Markets  30%    │            │
│  │ $363M volume | Live     │            │
│  │ Fees earned: $XXk (30d) │            │
│  └─────────────────────────┘            │
│                                         │
│  [View all allocations on-chain →]     │
└─────────────────────────────────────────┘
```

### **Section 5: Trust/Security**
```
┌─────────────────────────────────────────┐
│  Built on trusted infrastructure       │
├─────────────────────────────────────────┤
│  ✓ Vault: Infrasingularity             │
│  ✓ Custody: Fireblocks                 │
│  ✓ Audited by [Name]                   │
│  ✓ All allocations verifiable on-chain │
│                                         │
│  [View audits] [View contracts]        │
└─────────────────────────────────────────┘
```

### **Section 6: Your Position** (if connected)
```
┌─────────────────────────────────────────┐
│  Your position                          │
├─────────────────────────────────────────┤
│  HYPE staked: X.XX                     │
│  cHYPE held: X.XXXX                    │
│  Current value: X.XX HYPE ($XXX)       │
│  Lifetime fees earned: X.XX HYPE       │
│                                         │
│  Recent activity:                       │
│  • Staked X HYPE - 2 days ago          │
│  • Claimed X HYPE - 5 days ago         │
│                                         │
│  [View all history →]                  │
└─────────────────────────────────────────┘
```

### **Section 7: FAQ/Risks**
```
┌─────────────────────────────────────────┐
│  Frequently Asked Questions             │
├─────────────────────────────────────────┤
│  > How does Compost earn yield?         │
│  > What is the unstaking period?        │
│  > What are the risks?                  │
│  > How are markets selected?            │
│  > What is cHYPE?                       │
└─────────────────────────────────────────┘
```

---

## Competitive Differentiation for Compost

### vs. StakedHYPE:
- **StakedHYPE**: Generic HYPE staking, instant unstake
- **Compost**: Staking HYPE + allocating to builder markets for additional fees
- **Advantage**: Higher yield potential from builder fee splits

### vs. Hyperbeat beHYPE:
- **beHYPE**: HYPE staking + liquidHYPE vault (lending/borrowing yields)
- **Compost**: HYPE staking + HIP-3 builder market fee participation
- **Advantage**: Exposure to builder market growth, not just lending yields

### Unique selling points:
1. "Capital formation layer" - you're helping builders deploy markets
2. Dual yield: Base staking + builder fees (unique to HIP-3 participation)
3. Diversified exposure to best builder markets (like dsETH diversification model)
4. Direct link between TVL growth and Hyperliquid builder ecosystem growth

---

## Design Recommendations

### Visual Language:
- Follow Compost brand (dark mode, accent green #4dcf6a, earth tones for trust)
- Use growth metaphor: "Your capital grows the ecosystem"
- Progress indicators for unstaking periods
- Live metrics (TVL, APY update in real-time)

### Interaction Patterns:
- **Stake flow**: Input → Preview → Confirm → Success
- **Unstake flow**: Input → Warning (14 days) → Confirm → Pending → Claimable → Claim
- Transaction simulation (show expected cHYPE before confirming)
- Loading states with progress indication

### Content Tone:
- Technical but accessible (match landing page "ELI18" style)
- Lead with opportunity, not mechanics
- Be transparent about risks and timeline
- Use "e.g." when listing potential integrations

### Mobile Considerations:
- Tabs instead of side-by-side panels
- Sticky action button at bottom
- Collapsible sections for details
- Large touch targets (48px minimum)

---

## Next Steps

1. **Mockup Options**:
   - Static HTML page (matching index.html design system)
   - Interactive prototype (with state management)
   - Figma/design file first, then implement

2. **Data Requirements**:
   - Live APY calculation endpoint
   - Market allocation data (real-time or cached)
   - Historical performance data
   - Exchange rate feed (cHYPE/HYPE)

3. **Backend Needs**:
   - Smart contract interaction (stake/unstake)
   - Transaction simulation
   - Position tracking
   - Fee distribution calculation

Would you like me to build out a functional mockup based on these patterns?
