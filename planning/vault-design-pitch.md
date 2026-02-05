# Vault Page - Design Pitch & Content

## Design Philosophy

**Follow the patterns that work.**

Based on research of StakedHYPE, Hyperbeat beHYPE, Lido, and other liquid staking apps, there's a proven structure:
- Stats bar (establishes credibility)
- Tabs (Stake/Unstake)
- Position card (shows what you have)
- Action panel (input → output → button)
- Details sections (yield, allocations, security)

We're not reinventing the wheel. We're applying proven patterns to Compost's unique value prop: **builder market fee participation**.

---

## Visual Approach

### Layout
- **App-style interface** (not landing page minimalism)
- Max-width 1200px (accommodates position card + action panel side-by-side on desktop)
- Dark background, Compost brand colors
- Card-based sections with subtle borders

### Hierarchy
1. **Stats bar** (TVL, APY, Rate) - prove it's real
2. **Position card** (if connected) - show what you have
3. **Tabs + Action panel** - core functionality
4. **Yield breakdown** - show the mechanism
5. **Market allocations** - show where capital goes
6. **Trust signals** - infrastructure and security

### Interaction Pattern (Standard)
- **Tabs**: Stake | Unstake
- **Input helpers**: Balance display, Half/Max buttons
- **Live preview**: Output calculates as you type
- **Transaction flow**: Input → Preview → Confirm → Pending → Success

---

## Content Strategy

### Tone
- **Technical but not academic**: "cHYPE appreciates via exchange rate" not "algorithmic value accrual mechanism"
- **Specific, not vague**: "Allocated to 4 live builder markets" not "diversified across opportunities"
- **Opportunity-first**: Lead with what you earn, then explain how

### Language Rules
- Use "allocated" not "invested"
- Use "fees" not "returns" or "yield farming"
- Use "builder markets" not "protocols" or "strategies"
- No "guaranteed", "passive income", "infrastructure-grade"

---

## Page Structure

```
┌─ Navigation ──────────────────────────────┐
│ [Logo] compost.fi    Docs | @compostfi   │
└───────────────────────────────────────────┘

┌─ Stats Bar ───────────────────────────────┐
│ TVL           APY          cHYPE/HYPE     │
│ $4.2M         6.3%         1.024          │
└───────────────────────────────────────────┘

┌─ Your Position ──────────────────────────┐
│ (Shows if wallet connected)              │
└──────────────────────────────────────────┘

┌─ Main Section ───────────────────────────┐
│                                          │
│ [ Stake ] [ Unstake ]                   │
│                                          │
│ [Action Panel]                          │
│                                          │
└──────────────────────────────────────────┘

┌─ Yield Breakdown ────────────────────────┐
│ Where yield comes from                   │
└──────────────────────────────────────────┘

┌─ Market Allocations ─────────────────────┐
│ Where your HYPE is working              │
└──────────────────────────────────────────┘

┌─ Trust & Security ───────────────────────┐
│ Built on trusted infrastructure         │
└──────────────────────────────────────────┘
```

---

## Page Content

### 1. Navigation
```
┌────────────────────────────────────────────────┐
│ [Logo] compost.fi         Docs | @compostfi  │
└────────────────────────────────────────────────┘
```

**Design note**: Simple nav bar. Logo left, links right. Not sticky (this is an app page, not marketing).

---

### 2. Stats Bar
```
┌────────────────────────────────────────────────┐
│                                                │
│   TVL              APY            cHYPE/HYPE   │
│   $4.2M            6.3%           1.024        │
│                                                │
└────────────────────────────────────────────────┘
```

**Copy**: 
- Label 1: "TVL" | Value: "$4.2M"
- Label 2: "APY" | Value: "6.3%"
- Label 3: "cHYPE/HYPE" | Value: "1.024"

**Design note**: 
- Three columns, equal width, centered
- Labels: font-size 0.75rem, uppercase, letter-spaced, muted
- Values: font-size 2.5rem, weight 200, text-primary (APY in accent green)
- Full-width background (bg-subtle), subtle border bottom

---

### 3. Your Position Card (if wallet connected)

```
┌────────────────────────────────────────────────┐
│ Your position                                  │
├────────────────────────────────────────────────┤
│                                                │
│ HYPE staked              1,234.56 HYPE        │
│ cHYPE balance            1,205.38 cHYPE       │
│ Current value            1,264.23 HYPE        │
│                          ↑ +29.67 (+2.4%)     │
│                                                │
└────────────────────────────────────────────────┘
```

**Copy**:
- Headline: "Your position"
- Row 1: "HYPE staked" | "X.XX HYPE"
- Row 2: "cHYPE balance" | "X.XX cHYPE"
- Row 3: "Current value" | "X.XX HYPE"
- Row 4: (small, muted) "↑ +X.XX (+X.X%)" - shows appreciation

**Design note**:
- Card with border, subtle background
- Two-column layout (label left, value right)
- Values right-aligned, accent green for positive gains
- Max-width 600px, centered
- Only shows if wallet connected

**Not connected state**:
```
┌────────────────────────────────────────────────┐
│ [ CONNECT WALLET ]                             │
│                                                │
│ Connect your wallet to view your position      │
│ and stake HYPE.                                │
└────────────────────────────────────────────────┘
```

---

### 4. Tabs + Action Panel

```
┌────────────────────────────────────────────────┐
│                                                │
│ [ Stake ]  [ Unstake ]                        │
│                                                │
├────────────────────────────────────────────────┤
│                                                │
│ You stake                                      │
│ [______________] HYPE      [Half]  [Max]      │
│ Balance: 1,234.56 HYPE                        │
│                                                │
│ You receive                                    │
│ 976.56 cHYPE                                  │
│                                                │
│ Exchange rate                                  │
│ 1 cHYPE = 1.024 HYPE                          │
│                                                │
│ Network cost                                   │
│ ~$0.01                                        │
│                                                │
│ [       STAKE HYPE       ]                    │
│                                                │
│ 14-day unstake period applies                 │
│                                                │
└────────────────────────────────────────────────┘
```

**Copy - Stake Tab**:
- Tab labels: "Stake" | "Unstake"
- Input label: "You stake"
- Input placeholder: "0.00"
- Helper buttons: "Half" | "Max"
- Balance: "Balance: X.XX HYPE" (small, muted)
- Output label: "You receive"
- Output value: "X.XX cHYPE" (calculated, accent green, larger text)
- Exchange rate label: "Exchange rate"
- Exchange rate value: "1 cHYPE = X.XXX HYPE" (small, muted)
- Network cost label: "Network cost"
- Network cost value: "~$0.01" (small, muted)
- Button: "STAKE HYPE" (uppercase)
- Disclaimer: "14-day unstake period applies" (small, muted, below button)

**Copy - Unstake Tab** (simplified for mockup):
```
│ You unstake                                    │
│ [______________] cHYPE      [Half]  [Max]     │
│ Balance: 1,205.38 cHYPE                       │
│                                                │
│ You receive                                    │
│ 1,232.63 HYPE                                 │
│                                                │
│ [      UNSTAKE       ]                        │
│                                                │
│ ⚠ 14-day waiting period after unstaking       │
│ Your HYPE will be claimable after the period. │
```

**Design note**:
- Tabs: border-bottom style, active tab has accent underline
- Card with border, max-width 600px, centered
- Input field: dark surface (#111111), border (#1a1a1a), green border on focus
- Half/Max buttons: small, uppercase, border only, inline with input
- Output preview: font-size 1.5rem, accent green, prominent
- Exchange rate & network cost: smaller text, stacked, muted
- Main button: full width, padding 1rem, uppercase, letter-spaced, green bg
- Warning icon (⚠) for unstake disclaimer

---

---

### 5. Yield Breakdown Section

```
┌────────────────────────────────────────────────┐
│                                                │
│ Where yield comes from                         │
│                                                │
│ Base staking rewards            2.1%           │
│ Builder market fee splits       4.2%           │
│                                ─────           │
│ Total APY                      6.3%           │
│                                                │
│ Your HYPE is allocated across vetted HIP-3     │
│ builder markets. As markets generate trading   │
│ volume, you earn a share of the fees. cHYPE   │
│ appreciates over time—no rebasing, fully       │
│ transferable.                                  │
│                                                │
└────────────────────────────────────────────────┘
```

**Copy**:
- Headline: "Where yield comes from"
- Line 1: "Base staking rewards" | "2.1%"
- Line 2: "Builder market fee splits" | "4.2%"
- Divider line: "─────"
- Total: "Total APY" | "6.3%" (accent green)
- Explanation paragraph: "Your HYPE is allocated across vetted HIP-3 builder markets. As markets generate trading volume, you earn a share of the fees. cHYPE appreciates over time—no rebasing, fully transferable."

**Design note**:
- Card with border, max-width 800px, centered
- Breakdown: two-column layout (label left-aligned, value right-aligned)
- Divider: thin line (1px, accent-dim)
- Total row: slightly larger, accent green
- Paragraph: font-size 0.9375rem, weight 300, text-secondary, max-width 600px, centered

---

### 6. Market Allocations Section

```
┌────────────────────────────────────────────────┐
│                                                │
│ Where your HYPE is working                     │
│                                                │
│ ┌──────────────────────────────────────────┐  │
│ │ trade.xyz                           40%  │  │
│ │ Equities  •  $12.7B volume  •  Live      │  │
│ │ Fees earned (30d): $124k                 │  │
│ └──────────────────────────────────────────┘  │
│                                                │
│ ┌──────────────────────────────────────────┐  │
│ │ Kinetiq Markets                     30%  │  │
│ │ Global Indices  •  $363M 30d vol  •  Live│  │
│ │ Fees earned (30d): $42k                  │  │
│ └──────────────────────────────────────────┘  │
│                                                │
│ ┌──────────────────────────────────────────┐  │
│ │ Ventuals                            20%  │  │
│ │ Pre-IPO  •  SpaceX, OpenAI  •  Live      │  │
│ │ Fees earned (30d): $18k                  │  │
│ └──────────────────────────────────────────┘  │
│                                                │
│ ┌──────────────────────────────────────────┐  │
│ │ Felix                               10%  │  │
│ │ Equities  •  TSLA + more  •  Live        │  │
│ │ Fees earned (30d): $8k                   │  │
│ └──────────────────────────────────────────┘  │
│                                                │
│ View all allocations on-chain →               │
│                                                │
└────────────────────────────────────────────────┘
```

**Copy - Per Market Card**:
- Line 1: [Market Name] | [Allocation %]
  - Example: "trade.xyz" | "40%"
- Line 2: [Category] • [Key Stat] • [Status]
  - Example: "Equities • $12.7B volume • Live"
- Line 3: "Fees earned (30d): $XXk"

**All Markets**:
1. **trade.xyz**
   - Category: "Equities"
   - Stat: "$12.7B volume"
   - Fees: "$124k"
   - Allocation: "40%"

2. **Kinetiq Markets**
   - Category: "Global Indices"
   - Stat: "$363M 30d vol"
   - Fees: "$42k"
   - Allocation: "30%"

3. **Ventuals**
   - Category: "Pre-IPO"
   - Stat: "SpaceX, OpenAI"
   - Fees: "$18k"
   - Allocation: "20%"

4. **Felix**
   - Category: "Equities"
   - Stat: "TSLA + more"
   - Fees: "$8k"
   - Allocation: "10%"

**Footer link**: "View all allocations on-chain →"

**Design note**:
- Section headline: "Where your HYPE is working"
- Each market is a card with subtle border (#1a1a1a)
- Hover state: border changes to accent-dim, subtle lift (translateY -2px)
- Market name: font-size 1.125rem, weight 500, left-aligned
- Allocation %: accent green, right-aligned
- Details line: smaller (0.8125rem), muted, bullet-separated
- Fees earned: smaller, text-secondary
- Cards stack vertically, max-width 800px
- Footer link: accent color, small arrow →

---

### 7. Trust & Security Section

```
┌────────────────────────────────────────────────┐
│                                                │
│ Built on trusted infrastructure               │
│                                                │
│ Vault infrastructure         Infrasingularity  │
│ Custody                      Fireblocks        │
│ Security                     Audited by [Name] │
│                                                │
│ All allocations verifiable on-chain.           │
│                                                │
│ [View audits]  [View contracts]                │
│                                                │
└────────────────────────────────────────────────┘
```

**Copy**:
- Headline: "Built on trusted infrastructure"
- Row 1: "Vault infrastructure" | "Infrasingularity"
- Row 2: "Custody" | "Fireblocks"
- Row 3: "Security" | "Audited by [Name]"
- Footer: "All allocations verifiable on-chain."
- Links: "View audits" | "View contracts"

**Design note**:
- Card with border, max-width 800px, centered
- Two-column layout (labels left, providers right)
- Labels: text-secondary
- Providers: text-primary, slightly larger
- Footer text: small, muted, centered
- Links: accent color, small, centered below footer

---

### 8. Footer

```
┌────────────────────────────────────────────────┐
│                                                │
│ Questions? Read the docs →                     │
│ Or get in touch: grow@compost.fi               │
│                                                │
└────────────────────────────────────────────────┘
```

**Design note**: Simple, centered, small text. Links in accent color.

---

## Button & Input States

### Button States
- **Default**: "STAKE HYPE"
- **Wallet not connected**: "CONNECT WALLET"
- **Insufficient balance**: "INSUFFICIENT BALANCE" (disabled, muted)
- **No input**: Button disabled (muted)
- **Loading**: "STAKING..." (with subtle pulse animation)
- **Success**: Button hidden, success message shows

### Input States
- **Empty**: Placeholder "0.00"
- **Valid input**: Output calculates, button enabled
- **Invalid input** (letters, etc.): "Enter a valid amount"
- **Exceeds balance**: "Insufficient balance" (red text)
- **Max clicked**: Fills with full balance

### Success State (replaces action panel)

```
┌────────────────────────────────────────────────┐
│                                                │
│   ✓  Staked successfully                       │
│                                                │
│   1,000 HYPE → 976.56 cHYPE                    │
│                                                │
│   Your cHYPE will appear in your wallet        │
│   shortly. Transaction confirmed.              │
│                                                │
│   [View on Hyperliquid Explorer →]            │
│                                                │
└────────────────────────────────────────────────┘
```

**Copy**:
- Headline: "✓ Staked successfully" (with checkmark)
- Transaction: "X HYPE → X cHYPE"
- Details: "Your cHYPE will appear in your wallet shortly. Transaction confirmed."
- Link: "View on Hyperliquid Explorer →"

---

## Edge Cases

### Wallet Not Connected
- "Your Position" card shows "CONNECT WALLET" button
- Action panel shows "CONNECT WALLET" button
- Stats bar still visible (shows protocol metrics)

### No Balance
- Input works normally
- Button shows "INSUFFICIENT BALANCE" (disabled)
- Helper text under balance shows "Balance: 0.00 HYPE"

### Transaction Pending
```
┌────────────────────────────────────────────────┐
│                                                │
│   Staking in progress...                       │
│                                                │
│   Waiting for confirmation.                    │
│   [Subtle spinner/pulse animation]             │
│                                                │
└────────────────────────────────────────────────┘
```

### Transaction Failed
```
┌────────────────────────────────────────────────┐
│                                                │
│   ✗  Transaction failed                        │
│                                                │
│   Your HYPE was not staked.                    │
│   Please try again.                            │
│                                                │
│   [Try Again]                                  │
│                                                │
└────────────────────────────────────────────────┘
```

---

## Microcopy & Tooltips

### Tooltips (optional, on hover)
- **TVL**: "Total value locked in the vault"
- **APY**: "Annual percentage yield - estimated based on current rates"
- **cHYPE/HYPE**: "Current exchange rate - cHYPE appreciates as fees accrue"
- **14-day unstake period**: "After unstaking, HYPE is claimable after 14 days"

### Helper Text
- Under input: "Balance: X.XX HYPE"
- Under exchange rate: "Rate updates as fees accrue"
- Under unstake warning: "Your HYPE will be claimable after the period"

---

## Data Requirements

### Real-time Data
1. **TVL**: Fetch from vault contract
2. **APY**: Calculate from:
   - Base staking APR (from Hyperliquid)
   - 30-day average builder fee yield
   - Formula: `(base + feeYield30d) * 100`
3. **Exchange Rate**: Fetch from vault contract (`totalHYPE / totalcHYPE`)
4. **User Balance**: Fetch from wallet
5. **User Position**: Fetch from vault contract (if staked)
6. **Market Allocations**: Fetch allocation percentages and fee data

### Static Mockup Data
- TVL: $4.2M
- APY: 6.3% (Base: 2.1%, Fees: 4.2%)
- Exchange rate: 1.024
- User balance: 1,234.56 HYPE
- User staked: 1,234.56 HYPE
- User cHYPE: 1,205.38 cHYPE
- Market allocations: trade.xyz 40%, Kinetiq 30%, Ventuals 20%, Felix 10%

---

## Why This Structure Works

### 1. Follows Proven Patterns
- **Tabs** (Stake/Unstake) - universal in crypto apps
- **Position card** - users want to see what they have immediately
- **Input → Output preview** - standard transaction UX
- **Helper buttons** (Half/Max) - reduces friction

### 2. Progressive Disclosure
- See your position → Take action → Understand mechanism → Verify allocations → Trust infrastructure
- Each section answers the next logical question

### 3. Transparency Without Overwhelm
- Show 4 markets (not 20)
- Show 2 yield sources (not complex formula)
- Show key stats (not every data point)

### 4. Compost-Specific Value Props
- **Dual yield breakdown**: Shows base staking + builder fees separately
- **Market allocations**: Shows specific builder markets with fees earned
- **Capital formation narrative**: "Where your HYPE is working"

---

## What Makes This Different from Competitors

### vs. StakedHYPE
- **They show**: Generic APY (2.1%)
- **We show**: Base 2.1% + Builder fees 4.2% = 6.3%
- **Difference**: We explain the upside from builder market participation

### vs. Hyperbeat beHYPE
- **They have**: Validator selection, DeFi opportunities table
- **We have**: Builder market allocations with fees earned
- **Difference**: We show HIP-3 specific value, they show generic DeFi yields

### vs. Lido
- **They show**: Generic validator committee
- **We show**: Specific markets (trade.xyz, Kinetiq) with volume/fees
- **Difference**: We show where capital goes and what it earns

---

## Responsive Design Notes

### Desktop (> 968px)
- Stats bar: 3 columns
- Position card: max-width 600px, centered
- Action panel: max-width 600px, centered
- Market cards: 2 columns if needed, or stack

### Mobile (< 968px)
- Stats bar: Stack into rows or compress
- Position card: Full width, padded
- Action panel: Full width
- Tabs: Full width
- Half/Max buttons: Stay inline
- Market cards: Full width, stack

### Mobile-Specific
- Sticky "STAKE HYPE" button at bottom of viewport
- Larger touch targets (48px minimum)
- Collapsible sections for yield/allocations (optional)

---

## Implementation Plan

### Phase 1: Static Mockup
1. Build HTML structure
2. Apply Compost brand styles (reuse CSS from index.html)
3. Use example values (no calculation)
4. Show one state (wallet connected, has balance)

### Phase 2: Interactive Mockup
1. Add input → output calculation (`cHYPE = HYPE / 1.024`)
2. Add button state logic (disabled if empty/invalid)
3. Add Half/Max functionality
4. Add tab switching (Stake ↔ Unstake)
5. Add success state (after button click)

### Phase 3: Real Data (Later)
1. Connect to wallet
2. Fetch real TVL/APY/rate
3. Fetch user balance/position
4. Execute real transactions
5. Poll for transaction status

**For now: Build Phase 1 (static mockup) to review design.**

---

## Files to Create

1. **vault.html** - Main vault page
2. Reuse CSS from **index.html** (variables, button styles, etc.)
3. Small inline `<style>` for vault-specific components
4. Small inline `<script>` for input calculation (Phase 2)

---

## Final Checklist

Does this page answer:

✓ **What is this?** → Stats bar + "Where yield comes from"  
✓ **What do I have?** → Your Position card  
✓ **What can I do?** → Tabs (Stake/Unstake) + Action panel  
✓ **How does it work?** → Yield breakdown section  
✓ **Where does my money go?** → Market allocations  
✓ **Can I trust this?** → Trust & security section  
✓ **What do I do now?** → Big "STAKE HYPE" button  

**Yes. This matches proven patterns and shows Compost's unique value.**

---

Ready to build the static mockup?
