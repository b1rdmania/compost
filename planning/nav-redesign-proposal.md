# Navigation Redesign Proposal

## Current Problems

### 1. **Alignment Chaos**
- Logo: `align-items: flex-end` (baseline)
- Nav-left: `align-items: center` (vertical center)
- Nav-inner: `align-items: center` (vertical center)
→ **Result:** Everything feels misaligned

### 2. **Typography Hierarchy Too Weak**
- Wordmark: 1.125rem / weight 300
- Links: 0.875rem / weight 400
- **Gap is too big:** 18px vs 14px creates visual disconnect

### 3. **Color Hierarchy Invisible**
- Links default: `--text-muted` (#5c574f) - barely visible
- **Problem:** User can't see navigation options clearly

### 4. **Spacing Inconsistency**
- Left side gap: 2rem
- Right side gap: undefined (browser default ~4px)
- Logo internal: 0.625rem
→ **No rhythm**

### 5. **Logo Not Following DESIGN.md**
- Using inline SVG (old)
- Should use `lockup-domain-horizontal.svg` (breakout)
- Current height 22px too small

---

## Proposed Solution

### **Principle: Optical Alignment + Clear Hierarchy**

Per DESIGN.md philosophy:
> Typography that whispers, not shouts.

But whispers must still be legible.

---

## Redesign Specifications

### **1. Use Breakout Lockup (DESIGN.md Canonical)**

```html
<a href="/" class="nav-lockup">
  <img src="/assets/logo/lockup-domain-horizontal.svg" alt="compost.fi" class="nav-lockup-img">
</a>
```

**Why:**
- DESIGN.md specifies breakout as primary for nav
- Shoot extends above creates visual interest
- Eliminates alignment issues with inline SVG
- Proper baseline established by the image itself

**Size:** Height 32px (up from 22px)
- Larger presence
- Better proportion to link text
- Breakout shoot extends ~8px above

---

### **2. Unified Alignment Strategy**

```css
.nav-inner {
  display: flex;
  justify-content: space-between;
  align-items: center; /* Vertical center everything */
}

.nav-left {
  display: flex;
  align-items: center; /* Match parent */
  gap: 2.5rem; /* Slightly more breathing room */
}

.nav-right {
  display: flex;
  align-items: center; /* Match parent */
  gap: 2rem; /* Defined gap */
}

.nav-lockup-img {
  height: 32px;
  display: block; /* Remove inline spacing */
}
```

**Why:**
- Everything uses `align-items: center` (optical center)
- Lockup image handles its own baseline
- Consistent centering strategy

---

### **3. Typography Hierarchy (Tighter)**

```css
.nav-link {
  font-size: 0.9375rem; /* 15px, up from 14px */
  font-weight: 400;
  color: var(--text-secondary); /* #9a958d, up from text-muted */
  letter-spacing: 0.01em; /* Subtle tracking */
}

.nav-link:hover {
  color: var(--accent-bright);
}

.nav-link.active {
  color: var(--text-primary);
  font-weight: 500; /* Slightly bolder */
}
```

**Why:**
- 15px links feel closer to 18px wordmark (in lockup image)
- `text-secondary` is visible but still quiet
- Active state gets weight + color for clarity
- Subtle letter-spacing improves readability

---

### **4. Spacing Rhythm (8px Grid)**

```css
.nav {
  padding: 1.25rem 3rem; /* 20px vertical (was 24px) */
  padding-top: calc(1.25rem + env(safe-area-inset-top));
}

.nav-left {
  gap: 2.5rem; /* 40px */
}

.nav-right {
  gap: 2rem; /* 32px */
}
```

**Why:**
- Tighter vertical padding (20px) makes nav less bulky
- Left gap 40px (logo → links)
- Right gap 32px (link → link)
- Follows 8px grid system

---

### **5. Color Hierarchy (Legible Quiet)**

| Element | Current | Proposed | Hex | Rationale |
|---------|---------|----------|-----|-----------|
| Lockup (.fi) | accent-bright | accent-bright | #4dcf6a | Keep (brand color) |
| Links default | text-muted | **text-secondary** | **#9a958d** | Visible but quiet |
| Links hover | accent-bright | accent-bright | #4dcf6a | Keep (interactive feedback) |
| Links active | text-primary | text-primary | #e8e4df | Keep (current page) |
| Separator (optional) | — | border | #1a1918 | Subtle divider between links |

**Why:**
- `text-muted` (#5c574f) is too dim for navigation
- `text-secondary` (#9a958d) is warm, legible, still quiet
- Maintains "whisper" philosophy but functional

---

## Visual Comparison

### Current
```
[tiny logo svg] compost.fi   Vault                    Docs @compostfi
    ↓              ↓            ↓                        ↓       ↓
  baseline      flex-end    too small              too dim  no gap
```

### Proposed
```
[breakout lockup]   Vault                          Docs    @compostfi
        ↓             ↓                               ↓          ↓
   optical center  legible                       legible    consistent gap
```

---

## Implementation Checklist

- [ ] Replace inline SVG with `lockup-domain-horizontal.svg`
- [ ] Set lockup image height to 32px
- [ ] Unify alignment: everything `align-items: center`
- [ ] Update link font-size: 0.875rem → 0.9375rem
- [ ] Update link color: `text-muted` → `text-secondary`
- [ ] Add font-weight: 500 to `.nav-link.active`
- [ ] Add letter-spacing: 0.01em to links
- [ ] Define `.nav-right` with gap: 2rem
- [ ] Reduce nav padding: 1.5rem → 1.25rem vertical
- [ ] Test on mobile for safe-area-inset

---

## Why This Works

### **1. Follows DESIGN.md**
- Uses canonical breakout lockup
- Maintains warm tone palette
- "Whispers" but legibly

### **2. Optical Alignment**
- Everything centered vertically
- No competing alignment strategies
- Feels balanced

### **3. Clear Hierarchy**
- Logo is prominent (32px)
- Links are legible (15px, text-secondary)
- Active state is obvious (weight + color)

### **4. Consistent Spacing**
- 8px grid rhythm
- Defined gaps everywhere
- Professional polish

---

## Mobile Considerations

```css
@media (max-width: 640px) {
  .nav {
    padding: 1rem 1.5rem;
    padding-top: calc(1rem + env(safe-area-inset-top));
  }

  .nav-lockup-img {
    height: 28px; /* Slightly smaller on mobile */
  }

  .nav-link {
    font-size: 0.875rem; /* Back to 14px on small screens */
  }

  .nav-left {
    gap: 1.5rem; /* Tighter on mobile */
  }

  .nav-right {
    gap: 1.5rem;
  }
}
```

---

## Test Cases

1. **Landing page:** Logo + Vault + Docs + @compostfi
2. **Vault page:** Logo + Vault (active) + Docs + @compostfi
3. **Process page:** Logo + Vault + Docs + @compostfi
4. **Mobile:** All three pages at 375px width
5. **iPhone 14 Pro:** Test safe-area-inset-top with Dynamic Island

---

## Expected Outcome

**Before:**
- Misaligned elements fighting each other
- Links too small and too dim
- Inconsistent spacing
- Logo feels weak

**After:**
- Everything optically centered
- Links legible but still quiet
- Consistent spacing rhythm
- Logo has presence (breakout + proper size)
- Follows DESIGN.md canonical specs

**Brand voice maintained:** Quiet infrastructure, not loud marketing. But functional and legible.
