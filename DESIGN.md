# Compost Design System

> ⚠️ **CANONICAL SOURCE OF TRUTH**
> This document defines the authoritative Compost brand and design system.
> All implementations (index.html, vault.html, process.html, docs) must follow these specifications.
> **Do not modify without explicit approval.** This file is locked to prevent accidental changes.

## Logo

The Compost logo represents growth emerging from layered infrastructure—a single shoot rising from stacked sedimentary layers (the "pot"). The mark reads at all sizes while maintaining the brand's earthy, institutional character.

### Primary Lockup

**compost.fi** — lowercase, .fi in green (#4dcf6a)

This is the primary brand expression:
- Web-native, modern, confident
- The green .fi ties to the shoot color
- Distinctive — stands out from ALL CAPS DeFi brands
- Works at all sizes

### Logo Files

All production-ready assets in `/assets/logo/`:

| File | Use Case | Notes |
|------|----------|-------|
| `logo-primary.svg` | Mark only (dark backgrounds) | +15% saturated green |
| `logo-favicon.svg` | Favicon, 32px and below | Bolder shoot, 2 layers |
| `logo-light-bg.svg` | Mark for light backgrounds | Darker layers |
| `logo-single-grey.svg` | Monochrome mark | All layers same grey |
| `lockup-domain-horizontal.svg` | Primary lockup | Breakout mark + compost.fi |
| `lockup-domain-stacked.svg` | Stacked lockup | Mark above, compost.fi below |
| `lockup-primary.svg` | Formal lockup | Mark + COMPOST (caps) |
| `wordmark-primary.svg` | COMPOST standalone | For formal contexts |
| `wordmark-domain.svg` | compost.fi text only | Footer, inline refs |

### Mark Construction

The mark consists of two elements:

**1. The Shoot (Growth)**
- Flowing curved path representing organic growth
- Two-tone green: lighter leaf (#4dcf6a), darker stem (#2ba84a)
- Tilts slightly right, suggesting upward momentum
- In breakout version, extends above pot to break the bounding box

**2. The Pot (Infrastructure)**
- Three stacked horizontal layers
- Progressively narrower from top to bottom
- Earth tones: #8a7d6d → #5c5347 → #3d3630
- Rounded corners (rx="4") for organic feel

### Size Guidelines

| Size | Version | Notes |
|------|---------|-------|
| 16px | Favicon | Use `logo-favicon.svg` |
| 32px | Favicon retina | Use `logo-favicon.svg` |
| 64px+ | Primary | Use `logo-primary.svg` or lockup |
| 128px+ | Profile pics | Mark only or stacked lockup |
| 256px+ | Hero / display | Horizontal or stacked lockup |

---

## Color Palette

### Primary Colors

```
--bg-deep:        #0a0a09    (near black)
--bg-layer-1:     #111110
--bg-layer-2:     #1a1918
--bg-layer-3:     #252422
```

### Earth Tones

```
--stone:          #3d3a36
--sand:           #8a8279
--warm-gray:      #6b665e
```

### Text

```
--text-primary:   #e8e4df    (warm white)
--text-secondary: #9a958d
--text-muted:     #5c574f
```

### Accent (The Living Green)

```
--accent-bright:  #4dcf6a    (leaf, .fi, highlights)
--accent:         #2ba84a    (stem, UI elements)
--accent-muted:   #1d7a35    (subtle backgrounds)
```

### Logo-Specific Colors

```
Leaf:             #4dcf6a
Stem:             #2ba84a
Pot layer 1:      #8a7d6d
Pot layer 2:      #5c5347
Pot layer 3:      #3d3630
```

---

## Typography

### Font

**Outfit** — Google Fonts
- Weights: 200 (formal wordmark), 300 (primary/body), 400 (emphasis)

### Wordmark System

| Use Case | Text | Weight | Tracking | Notes |
|----------|------|--------|----------|-------|
| **Primary** | compost.fi | 300 | 0.02em | .fi in green |
| Hero | compost.fi | 300 | 0.02em | Large display |
| Nav header | compost.fi | 300 | 0.02em | With breakout mark |
| Footer | compost.fi | 300 | 0.02em | Text only |
| Formal/pitch | COMPOST | 200 | 0.12em | All caps for gravitas |
| Body reference | Compost | 400 | normal | Title case |

### Primary Wordmark (compost.fi)

```css
font-family: 'Outfit', -apple-system, sans-serif;
font-weight: 300;
letter-spacing: 0.02em;
/* .fi in --accent-bright (#4dcf6a) */
```

Web-native, modern, confident. Not shouty.

### Formal Wordmark (COMPOST)

```css
font-family: 'Outfit', -apple-system, sans-serif;
font-weight: 200;
letter-spacing: 0.12em;
text-transform: uppercase;
```

For pitch decks, legal, formal contexts.

### Body Text

```css
font-family: 'Outfit', -apple-system, sans-serif;
font-weight: 300;
letter-spacing: 0.02em;
line-height: 1.7;
```

---

## Lockup Variants

### Horizontal Breakout (Primary)

Mark with shoot extending above cap height + compost.fi
- Used for: nav headers, docs header, wide layouts
- The breakout creates visual interest and upward momentum

### Stacked

Mark centered above, compost.fi below
- Used for: square formats, app icons, profile pictures
- More formal, centered composition

### Standard Horizontal

Mark aligned with text + compost.fi
- Used for: tight spaces, when breakout isn't appropriate

---

## Usage Guidelines

### Do

- Use compost.fi as primary brand expression
- Use breakout mark for nav/header lockups
- Use mark only for favicon and small applications
- Let the green .fi tie to the shoot color
- Use COMPOST (caps) for formal contexts only

### Don't

- Use COMPOST.FI (all caps + domain) — too loud
- Mix lowercase compost with caps .FI
- Place on busy backgrounds
- Stretch or distort proportions
- Add effects (shadows, glows, etc.)

---

## Brand Applications

| Application | Asset | Notes |
|-------------|-------|-------|
| **Landing hero** | compost.fi + mark | Large display |
| **Nav header** | Breakout mark + compost.fi | Horizontal |
| **Footer** | compost.fi text only | .fi in green |
| **Favicon** | `logo-favicon.svg` | Mark only |
| **Social pfp** | `logo-primary.svg` | Mark only |
| **Twitter bio** | Mark + compost.fi | Stacked or horizontal |
| **OG image** | `og-image.svg` | Updated with compost.fi |
| **Pitch deck** | COMPOST | Formal contexts |
| **Docs header** | Breakout mark + compost.fi | Web-native feel |

---

## Asset Locations

```
/assets/
├── logo/                           # Production logo files
│   ├── logo-primary.svg            # Mark only (+15% saturated)
│   ├── logo-favicon.svg            # Mark for small sizes
│   ├── logo-light-bg.svg           # Mark for light backgrounds
│   ├── logo-single-grey.svg        # Monochrome mark
│   ├── lockup-domain-horizontal.svg # PRIMARY: breakout + compost.fi
│   ├── lockup-domain-stacked.svg   # Stacked: mark above, domain below
│   ├── lockup-primary.svg          # Formal: mark + COMPOST
│   ├── wordmark-primary.svg        # COMPOST standalone
│   └── wordmark-domain.svg         # compost.fi text only
├── logo.svg                        # Quick access (mark)
├── favicon.svg                     # Quick access (favicon mark)
├── og-image.svg                    # Social sharing image
└── [test files]                    # Reference pages
```

---

---

## iOS & Mobile Design

### Philosophy

Compost respects the device. We extend content to screen edges (full-bleed) while honoring iOS safe areas. This creates an immersive, app-like experience that feels native, not clipped or cramped.

**Principles:**
- Full-bleed design (edge-to-edge)
- Respect safe areas (notch, Dynamic Island, home indicator)
- Handle dynamic viewport (address bar collapse)
- No content bleed behind device chrome
- Solid backgrounds in safe areas (not transparent)

### Viewport Strategy

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
```

**`viewport-fit=cover`**: Extends content to physical screen edges, behind safe areas. This is the foundation for full-bleed iOS design.

**Why:** Creates immersive, edge-to-edge layouts. Without this, iOS adds white bars on notched devices.

### Safe Area Handling

Use `env(safe-area-inset-*)` to add padding that pushes interactive content away from device chrome.

#### Navigation Bar (Fixed)

```css
.nav {
  position: fixed;
  top: 0;
  padding: 1.5rem 3rem;
  padding-top: calc(1.5rem + env(safe-area-inset-top));
  background: var(--bg-deep); /* Solid, not transparent */
}
```

**Why:**
- `safe-area-inset-top` accounts for notch/Dynamic Island
- Solid background prevents content bleed
- Maintains visual continuity across devices

#### Hero Sections

```css
.hero {
  min-height: 100vh;
  min-height: 100dvh; /* Dynamic viewport height */
  padding: 8rem 0;
}
```

**`100dvh`** (dynamic viewport height): Adjusts as mobile browser address bar shows/hides.

**Why:**
- `100vh` on iOS includes address bar, causing content to be cut off
- `100dvh` dynamically adjusts to visible viewport
- Prevents awkward scrolling on mobile

#### Container Padding (Mobile)

```css
@media (max-width: 640px) {
  .container {
    padding-left: max(1.5rem, env(safe-area-inset-left));
    padding-right: max(1.5rem, env(safe-area-inset-right));
    padding-bottom: calc(1.5rem + env(safe-area-inset-bottom));
  }
}
```

**Why:**
- Landscape mode on iPhone 14 Pro/15 Pro has safe areas on sides
- Home indicator at bottom needs padding
- `max()` ensures minimum 1.5rem padding even if no safe area

#### Bottom Navigation / Fixed Elements

```css
.bottom-nav {
  position: fixed;
  bottom: 0;
  padding-bottom: calc(1rem + env(safe-area-inset-bottom));
  background: var(--bg-deep); /* Solid */
}
```

**Why:**
- Home indicator area needs padding
- Prevents tap targets from being obscured
- Solid background prevents content showing through

### Scrollable Containers

```css
.scrollable-list {
  max-height: calc(100dvh - 120px);
  overflow-y: auto;
  -webkit-overflow-scrolling: touch; /* Smooth iOS scrolling */
}
```

**Why:**
- `100dvh` ensures list fits in visible viewport
- Subtract fixed header height (120px)
- `-webkit-overflow-scrolling: touch` enables momentum scrolling

### Thematic Rules

| Pattern | Use Case | Safe Area | Background |
|---------|----------|-----------|------------|
| **Fixed nav (top)** | Site header | `inset-top` | Solid |
| **Fixed nav (bottom)** | Mobile tabs, CTAs | `inset-bottom` | Solid |
| **Hero sections** | Full-screen landing | `100dvh` | — |
| **Containers** | Content padding | `inset-left/right` | — |
| **Modals/overlays** | Full-screen dialogs | All insets | Solid |
| **Inputs (bottom)** | Keyboards push up | `inset-bottom` | — |

### Testing Checklist

When implementing iOS layouts:

- [ ] **Notch devices**: iPhone 14 Pro, 15 Pro (Dynamic Island)
- [ ] **Home indicator**: All modern iPhones
- [ ] **Landscape**: Safe areas on sides
- [ ] **Address bar collapse**: Test scroll behavior
- [ ] **Solid backgrounds**: No transparent nav over safe areas
- [ ] **Touch targets**: 44px minimum, not obscured by safe areas
- [ ] **Dynamic content**: Scrollable areas use `100dvh` correctly

### Don't

- ❌ Use `100vh` without fallback `100dvh`
- ❌ Use transparent backgrounds in safe areas (causes content bleed)
- ❌ Ignore `safe-area-inset-bottom` for fixed bottom elements
- ❌ Use `viewport-fit=contain` (adds white bars on notched devices)
- ❌ Place touch targets within 44px of screen edges without safe area padding

### Do

- ✅ Use `viewport-fit=cover` for full-bleed design
- ✅ Add `env(safe-area-inset-*)` to all fixed elements
- ✅ Use `100dvh` for full-height sections
- ✅ Use solid backgrounds (not transparent) in safe areas
- ✅ Test on physical iPhone 14 Pro / 15 Pro (Dynamic Island)
- ✅ Use `max()` to ensure minimum padding even without safe areas

---

## Reference

See `compost-philosophy.md` for the full brand philosophy.

**Key principles:**
- Web-native, not corporate
- Quiet infrastructure, not loud marketing
- Horizontal layers suggesting accumulation
- Earth tones with one living green accent
- Typography that whispers, not shouts
- The green .fi ties everything together
- Respect the device (iOS full-bleed + safe areas)
