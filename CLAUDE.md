# Compost Finance

Capital formation layer for Hyperliquid builder markets (HIP-3).

## Project Structure

```
/                     # Main marketing site (static HTML)
├── index.html        # Landing page ("Product" in nav)
├── demo.html         # Demo hub (routes to vault.html or vault-test.html)
├── vault.html        # Vault dashboard (static mockup, "Vault Preview")
├── vault-test.html   # Live HyperEVM testnet demo UI
├── hip3.html         # HIP-3 live intelligence board (perp builder markets)
├── hip4.html         # HIP-4 outcome trading explainer + live testnet board
├── litepaper.html    # Litepaper page
├── yield.html        # Yield page
├── process.html      # Design process page
├── PROOF-VAULT.md    # Developer doc for testnet vault setup
├── api/
│   └── waitlist.js   # Serverless function for email collection
├── assets/
│   ├── logo/         # Logo lockups and variants (see DESIGN.md)
│   │   ├── lockup-domain-horizontal.svg  # PRIMARY nav lockup
│   │   ├── lockup-domain-stacked.svg
│   │   ├── logo-primary.svg
│   │   └── logo-favicon.svg
│   └── icons/        # Icon library (18 SVGs)
├── contracts/
│   ├── CompostProofVault.sol   # ERC4626-style vault with synthetic APR accrual
│   └── MockHype.sol            # vHYPE test asset with wallet drip faucet
├── scripts/
│   └── deploy-proof-vault.js   # Hardhat deploy script
├── test/
│   └── CompostProofVault.test.js
├── hardhat.config.js           # Hardhat config (HyperEVM testnet)
├── package.json                # Node deps (hardhat, ethers, vite)
├── planning/         # Internal planning docs
│   ├── vault-design-pitch.md
│   ├── vault-design-critique.md
│   └── nav-redesign-proposal.md
├── DESIGN.md         # 🔒 CANONICAL design system (read-only)
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
  - Wordmark (compost.fi): `0.02em` in lockup SVG, `0.01em` in nav
  - Formal (COMPOST): `0.12em`
  - Buttons: `0.06em`
  - Nav links: `0.01em`
- **Headlines**: 500 weight
- **Body**: 300-400 weight
- **Nav links**: 15px (0.9375rem), weight 400, active gets weight 500

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

## Site Pages

### index.html (Landing Page)
- Nav active: "Overview"
- Hero: **"Hyperliquid builder markets, watched live."** Twin primary CTAs (HIP-3 board, HIP-4 board); secondary links to vault demos + concept paper; small `grow@compost.fi` aside.
- **HIP-3 ecosystem snapshot** — live HIP-3 stats (Dune), labelled as ecosystem aggregates, not Compost TVL. Includes HIP-3 spec link + HIP-4 board link.
- **What you can do here** — three action-led cards: track HIP-3 deployers / watch HIP-4 outcome books / try the vault demo. Each card is a link to its destination.
- **Who's shipping on HIP-3** — example deployers (trade.xyz, Kinetiq, Felix, Ventuals) + CTAs to boards and Dune source.
- **The cHYPE concept** — short two-paragraph block linking to `/litepaper.html` (Sept 2025 concept paper).
- **Building HL-native?** — single direct collab CTA: `grow@compost.fi`. **No email signup form** (was removed; `/api/waitlist` endpoint still exists but is no longer wired into the homepage).

### demo.html (Demo Hub)
- Nav active: "Demo"
- Routes between two experiences:
  - **Experience A – Vault Preview** → `/vault.html` (static mockup, no wallet needed)
  - **Experience B – Live Demo** → `/vault-test.html` (HyperEVM testnet, wallet required)

### vault.html (Vault Dashboard — Vault Preview)
- **Static mockup** of stake/unstake interface
- Stats bar: TVL, APY, cHYPE/HYPE rate
- Your Position card (shows staked amounts)
- Tabs: Stake | Unstake
- Yield breakdown: Base staking (2.1%) + Builder fees (4.2%)
- Market allocations: trade.xyz, Kinetiq, Ventuals, Felix
- **Note:** Uses example data, not connected to live contracts

### vault-test.html (Live HyperEVM Testnet Demo)
- Wallet connect (MetaMask / injected provider)
- Drip `vHYPE` test tokens from MockHype faucet
- Approve → Deposit vHYPE → receive cHYPE shares
- Withdraw cHYPE → receive vHYPE
- Displays live `pricePerShare` (grows with synthetic APR)
- Configurable contract addresses (saved to localStorage)

### litepaper.html (Concept Paper)
- Long-form document page; **September 2025 cHYPE concept paper** (hero + archive callout links to current homepage framing)
- Nav active: "Concept" (file path stays at `/litepaper.html` for URL stability; nav label is "Concept")

### yield.html (Yield Page)
- Yield mechanics explainer

### process.html (Design Process)
- Article layout about building compost.fi
- Tool showcases and philosophy

---

## Navigation Design (Applied Site-Wide)

### Structure
```html
<nav class="nav">
  <div class="nav-inner">
    <div class="nav-left">
      <a href="/" class="nav-lockup">
        <img src="/assets/logo/lockup-domain-horizontal.svg" class="nav-lockup-img">
      </a>
      <a href="/" class="nav-link active">Overview</a>       <!-- active on index -->
      <a href="/demo.html" class="nav-link active">Demo</a>  <!-- active on demo + vault.html + vault-test.html -->
      <a href="/hip3.html" class="nav-link active">HIP-3</a> <!-- active on hip3.html -->
      <a href="/hip4.html" class="nav-link active">HIP-4</a> <!-- active on hip4.html -->
      <a href="/litepaper.html" class="nav-link active">Concept</a> <!-- active on litepaper.html (file stays, nav label changed) -->
    </div>
    <div class="nav-right">
      <a href="https://docs.compost.fi" class="nav-link">Docs</a>
    </div>
  </div>
</nav>
```

Only one link gets `active` per page — shown above for illustration.

### CSS Specs
- **Alignment:** Everything uses `align-items: center` (optical center)
- **Logo:** Breakout lockup at 32px height (28px on mobile)
- **Links:** 15px (0.9375rem), weight 400, letter-spacing 0.01em
- **Link color:** `--text-secondary` (#9a958d) - legible but quiet
- **Active state:** `class="nav-link active"` → `--text-primary` + weight 500 (never use inline styles)
- **Hover:** `--accent-bright` (#4dcf6a) — inactive links only
- **Spacing:**
  - Vertical padding: 20px
  - Left gap (logo → links): 40px
  - Right gap (link → link): 32px
  - Mobile: 24px gaps, tighter padding

### Design Philosophy
- Unified optical alignment (no competing strategies)
- Legible but quiet (follows "whispers not shouts")
- Clear hierarchy via size + color + weight
- Follows DESIGN.md canonical specs

---

## Proof Vault (HyperEVM Testnet)

Scoped mechanism demo proving vault accounting on-chain. Does **not** route production HIP-3 yield yet.

### Contracts
- **`MockHype.sol`** (`vHYPE`) — test asset with wallet drip faucet
- **`CompostProofVault.sol`** (`cHYPE`) — ERC4626-style vault
  - `totalAssets` grows linearly from synthetic APR (default 10% / 1000 bps, max 30%)
  - `accrue()` mints synthetic vHYPE interest into vault
  - `pricePerShare` increases over time (exchange-rate model, not rebasing)
  - `deposit(assets, receiver)` → mints shares
  - `withdraw(assets, receiver)` → burns shares
  - `setAprBps(uint256)` — owner only

### Deployed Testnet Addresses
- `MockHype`: `0xAdBc75586E2F5338F460410B87F7AFde0374Fc31`
- `CompostProofVault`: `0x89bBacDACA0D20CB48FA617b57CF6779979AEC4E`

### Dev Commands
```bash
npm run vault:compile
npm run vault:deploy:testnet
npm run dev          # local dev server → localhost:3000
```

See `PROOF-VAULT.md` for full setup instructions.

---

## Key Technical Details

### Main Site

- Static HTML, no framework
- CSS variables in `:root` (DESIGN.md warm tones)
- Scroll reveal animations
- iOS/Mobile: Complete implementation per `/DESIGN.md` → "iOS & Mobile Design"
  - viewport-fit=cover (full-bleed)
  - safe-area-inset-* (notch, home indicator, landscape)
  - 100dvh (dynamic viewport height)
  - Solid backgrounds in safe areas

### Docs (VitePress)

- Default dark mode (`appearance: 'dark'`)
- Custom theme in `.vitepress/theme/custom.css`
- Sidebar navigation with collapsible sections

### iOS Implementation Status

**✅ Complete across all pages** (index.html, vault.html, vault-test.html, demo.html, litepaper.html, yield.html, process.html)

All pages implement DESIGN.md iOS patterns:
- ✅ `viewport-fit=cover` (full-bleed design)
- ✅ `safe-area-inset-top` (notch/Dynamic Island padding)
- ✅ `safe-area-inset-bottom` (home indicator padding)
- ✅ `safe-area-inset-left/right` (landscape mode on iPhone Pro)
- ✅ `100dvh` (dynamic viewport height for address bar)
- ✅ Solid backgrounds in safe areas (no content bleed)

**Testing:** Verified on iPhone 14 Pro / 15 Pro with Dynamic Island

### Environment Variables

```
DATABASE_URL=postgresql://...       # Neon connection string (waitlist)
DEPLOYER_PRIVATE_KEY=0x...          # Wallet key for Hardhat deploy (never commit)
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
