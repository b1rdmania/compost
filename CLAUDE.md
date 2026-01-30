# Compost Finance

Capital formation layer for Hyperliquid builder markets (HIP-3).

## Project Structure

```
/                     # Main marketing site (static HTML)
├── index.html        # Landing page
├── process.html      # Design process page
├── api/
│   └── waitlist.js   # Serverless function for email collection
├── assets/           # Logos, SVGs, design explorations
└── docs/             # VitePress documentation site
    ├── .vitepress/   # VitePress config and theme
    └── [content]/    # Markdown docs
```

## Deployment

- **Main site**: Vercel → compost.fi / www.compost.fi
- **Docs**: Vercel → docs.compost.fi
- **Database**: Neon Postgres (waitlist emails)

## Brand Guidelines

### Colors

| Name | Hex | Usage |
|------|-----|-------|
| Accent | `#4dcf6a` | Primary green, CTAs, links |
| Accent Dim | `#2ba84a` | Hover states, secondary green |
| Earth 1 | `#8a7d6d` | Tertiary, pot layer 1 |
| Earth 2 | `#5c5347` | Pot layer 2 |
| Earth 3 | `#3d3630` | Pot layer 3 |
| Background | `#0a0a0a` | Main bg |
| Surface | `#111111` | Cards, elevated surfaces |
| Border | `#1a1a1a` | Dividers, borders |
| Text Primary | `#e5e5e5` | Main text |
| Text Secondary | `#a3a3a3` | Subtitles, descriptions |
| Text Muted | `#666666` | Captions, hints |
| Error | `#ef4444` | Error states |

### Typography

- **Font**: Outfit (Google Fonts)
- **Weights**: 200 (light), 300 (book), 400 (regular), 500 (medium), 600 (semibold)
- **Headlines**: 500 weight
- **Body**: 300-400 weight

### Logo

The logo is a sprouting plant in a layered pot:
- Green sprout: `#4dcf6a` / `#2ba84a`
- Pot layers: Earth tones (`#8a7d6d`, `#5c5347`, `#3d3630`)

Files:
- `/assets/logo.svg` - Primary mark
- `/assets/logo-horizontal.svg` - Horizontal lockup
- `/docs/public/logo.svg` - Docs logo

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
- iOS Safari: uses `viewport-fit=cover` with `env(safe-area-inset-top)` for notch handling, `100dvh` for dynamic viewport height, solid nav background to prevent content bleed

### Docs (VitePress)

- Default dark mode (`appearance: 'dark'`)
- Custom theme in `.vitepress/theme/custom.css`
- Sidebar navigation with collapsible sections

### Environment Variables

```
DATABASE_URL=postgresql://... (Neon connection string)
```

## Content Guidelines

- Markets and integrations mentioned (Felix, Ventuals, Pendle, etc.) are **examples/potential** - use "e.g." prefix
- No confirmed partnerships - docs have warning blocks noting this
- ELI18 style for explanations - lead with opportunity, then mechanics

## Key URLs

- Website: https://compost.fi
- Docs: https://docs.compost.fi
- Twitter: https://twitter.com/compostfi
- Email: grow@compost.fi
- HIP-3 Stats: https://dune.com/yandhii/hip3
