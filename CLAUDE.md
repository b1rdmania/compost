# Compost Finance

Capital formation layer for Hyperliquid builder markets (HIP-3).

## Project Structure

```
/                     # Main marketing site (static HTML)
├── index.html        # Landing page
├── process.html      # Design process page
├── api/
│   └── waitlist.js   # Serverless function for email collection
├── assets/
│   ├── logo.svg      # Primary mark
│   ├── logo-horizontal.svg
│   └── icons/        # Icon library (18 SVGs)
├── planning/         # Internal planning docs (launch spec, tokenomics, playbook)
└── docs/             # VitePress documentation site
    ├── .vitepress/   # VitePress config and theme
    ├── public/icons/ # Icons copied for docs use
    └── [content]/    # Markdown docs
```

## Deployment

- **Main site**: Vercel → compost.fi / www.compost.fi
- **Docs**: Vercel → docs.compost.fi
- **Database**: Neon Postgres (waitlist emails)

## Brand Guidelines

> **⚠️ DESIGN.MD IS THE SOURCE OF TRUTH**
>
> **ALL design work must follow `/DESIGN.md` specifications.**
>
> Before implementing any visual changes:
> 1. Read `/DESIGN.md` for authoritative guidelines
> 2. Check colors, typography, logo usage, and iOS patterns
> 3. Never modify DESIGN.md without explicit user approval
>
> DESIGN.md is locked and canonical. The guidelines below are a quick reference only.

---

### Quick Reference (see DESIGN.md for full specs)

### Colors (from DESIGN.md)

**Backgrounds (warm tones):**
| Name | Hex | Usage |
|------|-----|-------|
| Deep | `#0a0a09` | Main bg |
| Layer 1 | `#111110` | Cards, elevated surfaces |
| Layer 2 | `#1a1918` | Borders, dividers |
| Layer 3 | `#252422` | Elevated borders |

**Text (warm tones):**
| Name | Hex | Usage |
|------|-----|-------|
| Primary | `#e8e4df` | Main text (warm white) |
| Secondary | `#9a958d` | Subtitles, descriptions |
| Muted | `#5c574f` | Captions, hints |

**Accent (the living green):**
| Name | Hex | Usage |
|------|-----|-------|
| Bright | `#4dcf6a` | Leaf, .fi, highlights, CTAs |
| Standard | `#2ba84a` | Stem, UI elements, hover states |
| Muted | `#1d7a35` | Subtle backgrounds |

**Logo pot layers:**
| Name | Hex |
|------|-----|
| Earth 1 | `#8a7d6d` |
| Earth 2 | `#5c5347` |
| Earth 3 | `#3d3630` |

**System:**
| Name | Hex | Usage |
|------|-----|-------|
| Error | `#ef4444` | Error states |

### Typography (from DESIGN.md)

- **Font**: Outfit (Google Fonts)
- **Weights**: 200 (formal wordmark), 300 (primary/body), 400 (emphasis), 500 (headings), 600 (semibold)
- **Letter-spacing**:
  - Wordmark (compost.fi): `0.02em`
  - Formal (COMPOST): `0.12em`
  - Buttons: `0.06em`
- **Headlines**: 500 weight
- **Body**: 300-400 weight

### Logo (from DESIGN.md)

The logo is a sprouting plant in a layered pot:
- Green sprout: `#4dcf6a` / `#2ba84a`
- Pot layers: Earth tones (`#8a7d6d`, `#5c5347`, `#3d3630`)

**Primary lockup:** `lockup-domain-horizontal.svg` (breakout mark + compost.fi)
- Use for nav headers, docs header, wide layouts
- Breakout version has shoot extending above cap height

Files:
- `/assets/logo/lockup-domain-horizontal.svg` - **PRIMARY** (breakout + compost.fi)
- `/assets/logo/lockup-domain-stacked.svg` - Stacked (mark above, domain below)
- `/assets/logo/logo-primary.svg` - Mark only
- `/assets/logo/logo-favicon.svg` - Favicon (small sizes)

See `/DESIGN.md` for complete logo specs and usage guidelines.

### Icon Library

18 icons in `/assets/icons/` (also in `/docs/public/icons/`):
- **Actions**: deposit, withdraw
- **Assets**: token, vault, wallet
- **Finance**: yield, chart, fee
- **Distribution**: allocate, markets, link
- **Trust**: verify, eye, shield
- **Status**: clock, check, info, warning

All icons use 64x64 viewBox, same color palette as logo.

### Homepage Growth Icons

The "How it works" section uses 6 growth-stage icons showing plant progression:
1. Empty pot with soil
2. Seed sprouting
3. Small shoot with leaves
4. Growing plant (multiple leaves)
5. Standard logo (clean)
6. Full plant with mirrored second leaf

### Buttons

- Uppercase, letter-spaced (`0.06em`)
- Sharp corners (no border-radius)
- Green background, dark text
- See `.btn` class in index.html

## Key Technical Details

### Main Site

- Static HTML, no framework
- CSS variables in `:root`
- Scroll reveal animations
- Waitlist form → `/api/waitlist` → Neon Postgres
- iOS/Mobile: See `/DESIGN.md` → "iOS & Mobile Design" for viewport, safe areas, and dynamic height patterns

### Docs (VitePress)

- Default dark mode (`appearance: 'dark'`)
- Custom theme in `.vitepress/theme/custom.css`
- Sidebar navigation with collapsible sections

### Environment Variables

```
DATABASE_URL=postgresql://... (Neon connection string)
```

## Partners

- **Vault**: Infrasingularity
- **Custody**: Fireblocks

## Content Guidelines

- Markets and integrations mentioned (Felix, Ventuals, Pendle, etc.) are **examples/potential** - use "e.g." prefix
- No confirmed partnerships for integrations - docs have warning blocks noting this
- ELI18 style for explanations - lead with opportunity, then mechanics

### Language (avoid guaranteed-yield vibes)

| Don't say | Say instead |
|-----------|-------------|
| Infrastructure-grade yield | Fee-backed yield |
| Earn yield from day one | Start earning via base staking rewards |
| Protocol-enforced | Protocol-defined |
| Generating real fees today | Accruing on-chain trading fees |
| Guaranteed | (don't use) |

### Token

- Don't promise "no governance token" - may do one later
- cHYPE is the vault receipt token, appreciates via exchange rate (not rebasing)

## Key URLs

- Website: https://compost.fi
- Docs: https://docs.compost.fi
- Twitter: https://twitter.com/compostfi
- Email: grow@compost.fi
- HIP-3 Stats: https://dune.com/yandhii/hip3
