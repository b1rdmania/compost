# Vault Page - Design Critique

Based on brand guidelines (DESIGN.md, CLAUDE.md) and screenshots provided.

---

## What's Working Well

### ✅ Color System (Strong)
- **Accent green (#4dcf6a)** used correctly: APY stat, output values, position gains, allocations
- **Background hierarchy** maintained: `--bg` (#0a0a0a) base, `--bg-subtle` (#111111) for stats bar, `--bg-card` for panels
- **Border system** consistent: subtle #1a1a1a borders throughout
- **Text hierarchy** working: primary/secondary/muted properly applied
- **Button styling** matches landing page: green bg, dark text, uppercase, letter-spaced

### ✅ Typography (Consistent)
- **Outfit font** throughout
- **Weight hierarchy**: 200 for stats, 300 for body, 500 for labels/headings
- **Letter-spacing** on uppercase elements matches brand (0.05-0.06em)
- **Line height** appropriate for readability

### ✅ Layout & Structure (Solid)
- **Max-width 1200px** container matches landing page
- **Card-based sections** with proper spacing
- **Progressive disclosure** working: stats → position → action → details
- **Responsive approach** (stats stack on mobile)

### ✅ Interaction Design (Good)
- **Tab system** clean with accent underline
- **Input helpers** (Half/Max) follow crypto app patterns
- **Live calculation** responsive
- **Button states** properly handled (disabled when invalid)

---

## Issues & Recommendations

### ⚠️ Typography Hierarchy Issues

**1. Stats Bar Labels**
```css
/* Current */
.stat-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em; /* ← TOO WIDE */
  color: var(--text-muted);
}
```

**Issue**: Letter-spacing 0.1em is wider than brand standard (0.02-0.06em for body, 0.12em for formal wordmark only).

**Recommendation**:
```css
.stat-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.06em; /* Match button style */
  color: var(--text-muted);
}
```

**2. Section Headings Weight**
```css
/* Current */
.section h2 {
  font-size: 1.5rem;
  font-weight: 500; /* ← Correct per guidelines */
  margin-bottom: 2rem;
  text-align: center;
}
```
✅ This is correct per brand guidelines ("Headlines: 500 weight")

**3. Position Card Heading**
```css
/* Current */
.position-card h2 {
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em; /* ← OK */
  color: var(--text-secondary);
}
```
✅ This works

---

### ⚠️ Color Variance from Guidelines

**Issue**: Your CSS uses slightly different colors than DESIGN.md specifies.

**Current (vault.html)**:
```css
:root {
  --bg: #0a0a0a;
  --bg-subtle: #111111;
  --bg-card: #0f0f0f;
  --border: #1a1a1a;
  --text-primary: #e5e5e5;
  --text-secondary: #a3a3a3;
  --text-muted: #666666;
  --accent: #4dcf6a;
  --accent-dim: #2ba84a;
}
```

**DESIGN.md specifies**:
```css
/* Backgrounds */
--bg-deep:        #0a0a09    (not #0a0a0a)
--bg-layer-1:     #111110    (not #111111)
--bg-layer-2:     #1a1918    (not used)
--bg-layer-3:     #252422    (not used)

/* Text */
--text-primary:   #e8e4df    (not #e5e5e5) - warmer white
--text-secondary: #9a958d    (not #a3a3a3) - warmer gray
--text-muted:     #5c574f    (not #666666) - warmer muted
```

**Analysis**: 
- You're using **neutral grays** (index.html style)
- DESIGN.md specifies **warm earth tones**
- Both work, but DESIGN.md is more distinctive

**Recommendation**: 
If DESIGN.md represents the "final" brand system, adopt those warmer tones. They're more unique and tie to the earth-tones pot aesthetic. But if index.html is your production standard, keep consistency.

**Decision needed**: Which is the source of truth? DESIGN.md or index.html colors?

---

### ⚠️ Navigation Lockup Missing

**Current**: You're using inline SVG for the mark in nav, which is fine.

**Brand guideline**: Primary lockup should be `lockup-domain-horizontal.svg` (breakout mark + compost.fi)

**From DESIGN.md**:
> ### Horizontal Breakout (Primary)
> Mark with shoot extending above cap height + compost.fi
> - Used for: nav headers, docs header, wide layouts
> - The breakout creates visual interest and upward momentum

**Current implementation** (vault.html line 666-675):
```html
<a href="/" class="nav-lockup">
  <svg class="nav-mark" viewBox="0 0 64 80">...</svg>
  <div class="nav-wordmark">compost<span class="tld">.fi</span></div>
</a>
```

**Issue**: Your mark is the standard version, not the "breakout" version where shoot extends above cap height.

**Recommendation**: 
1. Use `/assets/logo/lockup-domain-horizontal.svg` directly, or
2. Update the inline SVG to match the breakout version (shoot extends above viewBox)

The breakout version adds visual interest and upward momentum (per guidelines).

---

### ⚠️ Stats Bar Typography Scale

**Current**:
```css
.stat-value {
  font-size: 2.5rem;
  font-weight: 200;
}
```

**Landing page hero** for comparison (index.html line 172-177):
```css
.hero-headline {
  font-size: clamp(4rem, 10vw, 6.5rem);
  font-weight: 200;
}
```

**Analysis**: Your stats at 2.5rem feel appropriate for an app page (not hero). This is fine. However, consider using `clamp()` for better responsive scaling:

**Recommendation**:
```css
.stat-value {
  font-size: clamp(2rem, 5vw, 2.5rem);
  font-weight: 200;
}
```

This scales down gracefully on mobile without media query.

---

### ⚠️ Button Hover Effect

**Current** (vault.html):
```css
.btn:hover {
  box-shadow: 0 0 40px var(--accent-glow-strong);
}
```

**Landing page** (index.html line 240-246):
```css
.btn:hover::before {
  transform: translateX(100%);
}

.btn:hover {
  box-shadow: 0 0 40px var(--accent-glow-strong);
}
```

✅ You have both the shimmer effect (::before) and the glow. This matches landing page. Good.

---

### ⚠️ Sharp Corners (Brand Requirement)

**From CLAUDE.md**:
> ### Buttons
> - Uppercase, letter-spaced (0.06em)
> - **Sharp corners (no border-radius)**
> - Green background, dark text

**Current vault.html**: 
Checking cards and inputs for border-radius...

Looking at your CSS, I don't see any `border-radius` declarations. ✅ Good - this maintains the sharp aesthetic.

However, **the pot layers in logo use `rx="4"`** (rounded corners), which is correct for the organic pot feel. Just making sure you're not adding border-radius to UI cards/panels.

---

### ⚠️ Input Token Label Positioning

**Current**:
```css
.input-token {
  position: absolute;
  right: 5.5rem; /* ← Fixed pixel value */
  font-size: 0.875rem;
  color: var(--text-muted);
  pointer-events: none;
}
```

**Issue**: `right: 5.5rem` assumes Half/Max buttons are always that width. If button text changes or fonts load differently, this could overlap.

**Recommendation**:
```css
.input-token {
  position: absolute;
  right: calc(100% - (100% - 9rem)); /* Or use right: auto; left calculation */
  /* OR: Remove absolute positioning, keep token in input-wrapper flow */
}
```

Actually, looking at your HTML structure:
```html
<div class="input-wrapper">
  <input type="text" class="input-field">
  <span class="input-token">HYPE</span> <!-- This is in flow -->
  <div class="input-helpers">...</div>
</div>
```

The `input-token` is absolutely positioned inside `input-wrapper`, but `input-helpers` is also in flow. This could cause overlap.

**Better approach**: Put token inside the input field (right padding), or calculate position based on button widths dynamically.

---

### ⚠️ Responsive Stats Grid

**Current**:
```css
@media (max-width: 968px) {
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
```

**Issue**: On tablet (between 640-968px), might look better as 3 columns still, then stack on mobile only.

**Recommendation**:
```css
@media (max-width: 640px) {
  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
/* Keep 3 columns for 640-968px */
```

---

### ⚠️ Yield Breakdown Border

**Current**:
```css
.yield-row:last-of-type {
  border-bottom: 2px solid var(--accent-dim);
  margin-bottom: 1rem;
}
```

**Issue**: Using `--accent-dim` (#2ba84a) for border. This is the stem color, which is fine, but consider using a very subtle accent-muted for less visual weight.

**From DESIGN.md**:
```css
--accent-muted:   #1d7a35    (subtle backgrounds)
```

**Recommendation**: Either keep `--accent-dim` (more prominent) or use a 1px border for subtlety:
```css
.yield-row:last-of-type {
  border-bottom: 1px solid var(--accent-dim);
}
```

---

## Missing Elements (Compared to Research)

### 1. Not Connected State
Your mockup assumes wallet is connected. From research (Hyperbeat, Lido), apps show:
```
┌────────────────────────────────┐
│ [ CONNECT WALLET ]             │
│                                │
│ Connect your wallet to view    │
│ your position and stake HYPE.  │
└────────────────────────────────┘
```

**For mockup purposes**: This is fine to skip. But note it for production.

---

### 2. Warning Icon in Unstake Disclaimer

**Current**:
```html
<div class="disclaimer">⚠ 14-day waiting period...</div>
```

**Issue**: Using unicode ⚠ is fine, but consider styling it accent color:
```css
.disclaimer-warning {
  color: var(--accent);
}
```

Or use a proper warning icon from your icon library (`/assets/icons/warning.svg`).

---

## Content Review

### ✅ Copy Follows Guidelines

**ELI18 style** ✓
- "Your HYPE is allocated across vetted HIP-3 builder markets"
- "As markets generate trading volume, you earn a share of the fees"

**Avoids guaranteed-yield language** ✓
- Uses "fee-backed" not "guaranteed"
- "appreciates over time" not "guaranteed returns"

**Specific, not vague** ✓
- Shows actual markets (trade.xyz, Kinetiq)
- Shows actual fees earned ($124k, $42k)
- Shows specific APY breakdown (2.1% + 4.2%)

---

## Technical Issues

### ⚠️ JavaScript Calculation Edge Cases

**Current**:
```javascript
function calculateStakeOutput(hypoValue) {
  return hypoValue / EXCHANGE_RATE;
}

stakeInput.addEventListener('input', updateStakeOutput);
```

**Missing validation**:
- No check for negative numbers
- No check for non-numeric input (letters)
- No max decimals enforcement

**Recommendation**:
```javascript
stakeInput.addEventListener('input', (e) => {
  // Sanitize input
  let value = e.target.value.replace(/[^0-9.]/g, '');
  // Prevent multiple decimals
  const parts = value.split('.');
  if (parts.length > 2) {
    value = parts[0] + '.' + parts.slice(1).join('');
  }
  e.target.value = value;
  updateStakeOutput();
});
```

---

## Accessibility

### ⚠️ Missing ARIA Labels

**Issue**: Input fields lack proper labels for screen readers.

**Current**:
```html
<input type="text" class="input-field" id="stake-input" placeholder="0.00">
```

**Recommendation**:
```html
<input 
  type="text" 
  class="input-field" 
  id="stake-input" 
  placeholder="0.00"
  aria-label="Amount of HYPE to stake"
  aria-describedby="stake-balance-hint"
>
<div id="stake-balance-hint" class="balance-hint">Balance: 1,234.56 HYPE</div>
```

### ⚠️ Button Disabled State

**Current**:
```html
<button class="btn" id="stake-btn" disabled>STAKE HYPE</button>
```

**Missing**: `aria-disabled` and explanation why disabled.

**Recommendation**:
```html
<button 
  class="btn" 
  id="stake-btn" 
  disabled
  aria-disabled="true"
  aria-describedby="stake-btn-hint"
>
  STAKE HYPE
</button>
<div id="stake-btn-hint" class="sr-only">
  Button will be enabled once you enter a valid amount
</div>
```

---

## Performance

### ✅ Inline Styles
You're using inline `<style>` tag. For a single-page mockup, this is fine. For production, extract to external CSS for caching.

### ⚠️ Font Loading
**Current**:
```html
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600&display=swap" rel="stylesheet">
```

**Recommendation**: Add `font-display: swap` (you already have it via `display=swap` param). ✅ Good.

---

## Visual Hierarchy

### ✅ Strong
- Stats bar establishes credibility
- Position card shows user's stake
- Action panel is clear focal point
- Details sections are secondary but accessible

### ⚠️ Market Cards Could Use More Hierarchy

**Current**: All market cards look equal weight.

**Consideration**: Could emphasize top allocation visually:
```css
.market-card:first-child {
  border-color: var(--accent-dim);
  /* OR: slightly larger, or different background */
}
```

But this might be over-designed. Current equal treatment is fine.

---

## Brand Consistency Check

### ✅ Matches Landing Page
- Same dark aesthetic
- Same green accent usage
- Same button style
- Same typography system
- Same noise texture overlay

### ✅ Appropriate for App vs Marketing
- More functional (tabs, inputs)
- Less marketing copy
- More data-dense
- Still maintains brand feel

---

## Final Recommendations (Prioritized)

### HIGH PRIORITY

1. **Decide on color palette**: Use DESIGN.md warm tones or stick with index.html neutral grays? Pick one source of truth.

2. **Fix letter-spacing**: Stats labels at 0.1em → 0.06em to match brand standard.

3. **Use breakout lockup**: Nav should use `lockup-domain-horizontal.svg` with shoot extending above.

4. **Input validation**: Add number-only, max decimals, negative number handling.

5. **Accessibility**: Add ARIA labels to inputs and buttons.

### MEDIUM PRIORITY

6. **Input token positioning**: Fix hardcoded `right: 5.5rem` to be dynamic or remove absolute positioning.

7. **Responsive stats**: Keep 3 columns until 640px, don't stack at 968px.

8. **Warning icon styling**: Color the ⚠ accent green or use SVG icon.

### LOW PRIORITY (Polish)

9. **Yield divider**: Consider 1px instead of 2px for subtle hierarchy.

10. **Add clamp() to stats**: `font-size: clamp(2rem, 5vw, 2.5rem)` for better scaling.

11. **Extract CSS**: Move to external stylesheet for production.

---

## Overall Grade: A-

**Strengths**:
- ✅ Follows research patterns (tabs, position card, allocations)
- ✅ Brand-consistent (colors, typography, buttons)
- ✅ Functional mockup with working interactions
- ✅ Clean, professional execution
- ✅ Content follows guidelines (ELI18, no guarantee language)

**Areas for improvement**:
- ⚠️ Minor color/typography variance from DESIGN.md
- ⚠️ Missing breakout lockup in nav
- ⚠️ Input validation edge cases
- ⚠️ Accessibility labels

**Bottom line**: This is production-ready with minor refinements. The design works, the interactions work, and it feels like Compost. Fix the high-priority items and you're golden.
