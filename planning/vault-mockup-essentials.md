# Vault Page Mockup - Essential Elements

## Design Philosophy
Keep it **sparse, intentional, and elegant** - matching the landing page aesthetic. Only what's necessary.

---

## The Absolute Essentials

### **1. Hero Stats Bar** (top)
```
TVL: $4.2M  |  APY: 6.3%  |  cHYPE/HYPE: 1.024
```
- Three numbers that matter
- One line, centered or spanning width
- Updates the story: "vault is growing, yield is real, your token appreciates"

---

### **2. The Main Action** (center, prominent)

```
┌─────────────────────────────────────┐
│                                     │
│   Stake HYPE                        │
│   ──────────────────────            │
│                                     │
│   [____________] HYPE    [Max]      │
│   Balance: 1,234.56                 │
│                                     │
│   You receive                       │
│   1,205.38 cHYPE                    │
│                                     │
│   [ STAKE HYPE ]                    │
│                                     │
└─────────────────────────────────────┘
```

**That's it for the main interaction.**
- Input field
- Output preview (calculated)
- One button
- No tabs (keep it single-purpose for mockup)

---

### **3. The Yield Explanation** (below, concise)

```
Where yield comes from

Base staking            2.1%
Builder market fees     4.2%
                       ────
Total APY              6.3%

Your HYPE is allocated across vetted HIP-3 builder 
markets. As markets generate trading volume, you earn 
a share of the fees.
```

- Simple breakdown
- 2-3 lines of explanation
- No chart needed for mockup

---

### **4. Current Allocations** (trust/transparency)

```
Allocated markets

trade.xyz               40%  |  $12.7B vol
Kinetiq Markets         30%  |  $363M vol  
Ventuals                20%  |  Live
Felix                   10%  |  TSLA + more

View all allocations on-chain →
```

- Show where the money goes
- Minimal info per market (name, %, quick stat)
- Link to verify
- 4-6 markets max for mockup

---

### **5. Trust Footer** (minimal)

```
Vault: Infrasingularity  |  Custody: Fireblocks  |  Audited
```

- One line
- Three trust signals
- No need for elaborate section in mockup

---

## What to EXCLUDE from mockup

❌ **Unstake tab** - keep it single-purpose  
❌ **Portfolio view** - not needed to show the concept  
❌ **Activity history** - adds complexity  
❌ **FAQ accordion** - can link to docs  
❌ **Charts** - static mockup, just show the numbers  
❌ **Transaction simulation details** - implied in output preview  
❌ **Network cost estimates** - too much detail  
❌ **Validator selection** - Compost handles this  

---

## Visual Design Principles

### Layout
- **Single column, centered, max-width ~600px**
- Generous whitespace (like landing page)
- Dark background (#0a0a0a)
- Sections separated by subtle dividers or spacing

### Typography
- Same as landing page: Outfit font
- Weight hierarchy: 200 (large numbers), 300 (body), 500 (labels)
- Let the numbers breathe

### Color Usage
- Accent green (#4dcf6a) for:
  - APY percentage
  - CTA button
  - Output amount (cHYPE received)
- Text hierarchy:
  - Primary (#e5e5e5) for main content
  - Secondary (#a3a3a3) for labels
  - Muted (#666666) for supporting info

### Components
- Input field: Dark surface (#111111), green focus border
- Button: Same as `.btn` class from index.html (uppercase, green, sharp corners)
- Cards: Minimal borders (#1a1a1a), subtle hover states

---

## The Flow (Interaction)

```
1. User lands on page
   → Sees stats, understands the opportunity

2. User enters HYPE amount
   → Output preview calculates instantly
   → Shows "You receive X cHYPE"

3. User clicks "STAKE HYPE"
   → (Mockup: just show success state)
   → Real app: wallet connection, transaction

4. User scrolls down
   → Sees where their HYPE goes (markets)
   → Understands yield sources
   → Feels trust signals
```

---

## Copy Tone (ELI18, from brand guidelines)

**Do:**
- "Your HYPE is allocated across vetted builder markets"
- "As markets generate volume, you earn fees"
- "cHYPE appreciates over time - no rebasing"

**Don't:**
- "Guaranteed returns"
- "Infrastructure-grade yield"
- "Earn passive income effortlessly"

---

## Mockup Sections (In Order)

```
┌─ Navigation ────────────────────────┐
│ compost.fi              [Docs] [App]│
└─────────────────────────────────────┘

┌─ Hero Stats ────────────────────────┐
│ TVL: $4.2M │ APY: 6.3% │ Rate: 1.024│
└─────────────────────────────────────┘

        [Logo/Mark]

    Stake HYPE, Earn Yield
    Capital formation for Hyperliquid
    builder markets

┌─ Main Action ───────────────────────┐
│                                     │
│  [Input Field]                      │
│  Preview: X cHYPE                   │
│  [STAKE HYPE Button]                │
│                                     │
└─────────────────────────────────────┘

┌─ Yield Breakdown ───────────────────┐
│ Where yield comes from              │
│ Base: 2.1% + Fees: 4.2% = 6.3%     │
└─────────────────────────────────────┘

┌─ Allocations ───────────────────────┐
│ Allocated markets                   │
│ • trade.xyz        40%              │
│ • Kinetiq          30%              │
│ • Ventuals         20%              │
│ • Felix            10%              │
└─────────────────────────────────────┘

┌─ Trust Footer ──────────────────────┐
│ Vault: Infrasingularity             │
│ Custody: Fireblocks                 │
│ Audited by [Name]                   │
└─────────────────────────────────────┘
```

---

## Implementation Options

### Option A: Static HTML Page
- Match index.html exactly (same CSS variables, classes)
- No real functionality, just visual mockup
- **Best for**: Quick visual review, design approval

### Option B: Interactive Mockup
- Real input/output calculation (cHYPE = HYPE / exchange rate)
- Form validation
- Hover states, transitions
- **Best for**: User testing, stakeholder demos

### Option C: Figma/Design First
- Design in Figma, then implement
- **Best for**: Iteration on visual design before coding

---

## Key Decision: What to Mock

For a **functional mockup**, we need:

1. **Input field that accepts numbers**
2. **Live calculation**: `cHYPE = HYPE / 1.024` (example rate)
3. **Button states**: Default, hover, disabled (if no input)
4. **Success state** (after "staking"): Confirmation message

For a **static mockup**, we need:
1. **Example filled state** showing 1000 HYPE → 976.56 cHYPE
2. **Visual hierarchy** to guide eye from stats → action → explanation

---

## Recommended Approach

**Start with static, then add interaction if needed.**

1. Build HTML page with example values filled in
2. Style to perfection (match landing page aesthetic)
3. Add simple JS for input→output calculation
4. Polish transitions and states

This way you can:
- Review the design quickly
- Make visual adjustments without dealing with logic
- Layer in functionality once the design feels right

---

## Open Questions for You

1. **Static or interactive** for first version?
2. **Should we show a "Connect Wallet" state** or assume connected?
3. **Do you want the Compost logo/mark** at the top of the page?
4. **Should this be a separate page** (`/vault.html`) or integrated into main site?
5. **Real numbers or placeholder numbers** for the mockup?

Let me know and I'll build it out.
