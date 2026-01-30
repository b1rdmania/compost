# Phase 5: Design System

Define the complete visual language: colors, type, spacing, components.

## Time

15-30 minutes.

## Prerequisites

- Mark and wordmark locked

---

## Process

### 1. Colors

Build outward from the mark's colors.

**Backgrounds (dark mode):**
```
Deep       #0e0e10   Main background
Warm       #16151a   Cards, surfaces
Surface    #201e24   Inputs, wells
Elevated   #2a2830   Hover states
```

**Text:**
```
Primary    #e4e1e8   Headings, emphasis
Secondary  #a8a2b2   Body copy
Muted      #625e6c   Labels, hints
Whisper    #3a3741   Disabled states
```

**Borders:**
```
Default    #37343e
Light      #484452
```

**Functional:**
```
Green      #22c55e   Success, active, CTAs
Green dim  #187840   Hover states
Amber      #cf9a37   Warnings
Red        #dc2626   Errors
Blue       #5886b0   Links, info
```

**Brand accents** (from visual philosophy):
```
Copper     #b07e58   Premium touches
```

### 2. Typography

**Fonts:**
```css
--font-sans: 'Inter', -apple-system, sans-serif;
--font-mono: 'JetBrains Mono', 'SF Mono', monospace;
```

**Scale:**
```
Display    48px / 500 / 1.1    Heroes
H1         32px / 500 / 1.2    Page titles
H2         24px / 500 / 1.3    Sections
H3         18px / 500 / 1.4    Cards
Body       15px / 400 / 1.6    Prose
Small      14px / 400 / 1.5    Secondary
Caption    12px / 400 / 1.4    Labels
Mono       14px / 400 / 1.5    Code
```

**Labels:**
- 11-12px, weight 500
- UPPERCASE, 0.08em tracking
- Muted color

### 3. Spacing

**Base:** 8px

**Scale:**
```
xs     4px
sm     8px
md     16px
lg     24px
xl     32px
2xl    48px
3xl    64px
```

**Component padding:**
```
Buttons   12px 20px
Inputs    12px 16px
Cards     20px 24px
Modals    24px 32px
```

### 4. Components

**Primary button:**
```css
background: var(--green);
color: var(--bg-deep);
font-weight: 500;
padding: 12px 20px;
border-radius: 6px;
```

**Secondary button:**
```css
background: transparent;
border: 1px solid var(--border);
color: var(--text-primary);
```

**Input:**
```css
background: var(--bg-surface);
border: 1px solid var(--border);
padding: 12px 16px;
border-radius: 6px;
```
Focus: `border-color: var(--green)`

**Card:**
```css
background: var(--bg-warm);
border: 1px solid var(--border);
border-radius: 8px;
padding: 20px 24px;
```

**Status dots:**
- 8px diameter
- Green = healthy
- Amber = warning
- Red = error
- Gray = inactive

### 5. Layout

**Max widths:**
```
Content    720px    Prose
Dashboard  1200px   Apps
Full       1440px   Marketing
```

**Grid:** 12 columns, 24px gutters

### 6. Motion

**Timing:**
```
Micro      100ms    Hovers
Default    200ms    Transitions
Enter      300ms    Appearances
Exit       200ms    Removals
```

**Principles:**
- Purposeful, not decorative
- Status changes visible
- No gratuitous animation

### 7. Write Guidelines Doc

Compile everything into `[brand]-design-guidelines.md`:
- Logo usage (mark, wordmarks, spacing, don'ts)
- Color palette with hex codes
- Type scale with specs
- Spacing system
- Component patterns
- Voice notes (from Phase 1)
- CSS variables (copy-paste ready)

---

## Outputs

- `[brand]-design-guidelines.md`

## Gate

Review with user. Adjust as needed.

---

## Notes

**Warm darks:** Pure #000 feels dead. Add slight warmth.

**Functional color:** Green = success/go. Use it for meaning, not decoration.

**Density:** Developer tools can be information-dense. Don't waste space, but maintain hierarchy.

**CSS variables:** Developers need copy-paste code. Include a complete `:root` block.
