---
name: Brand
description: Full brand development system. Triggers on requests for brand identity, logos, visual systems, or design guidelines. Covers strategy through delivery.
---

# Brand Skill

Build complete brand identities from scratch: strategy, logo, design system, packaged assets.

## Structure

```
brand-skill/
├── SKILL.md                      # Overview and routing
├── Workflows/
│   ├── 01-Discovery.md           # Strategy and positioning
│   ├── 02-VisualDirection.md     # Reference exploration
│   ├── 03-MarkDevelopment.md     # Logo iteration
│   ├── 04-Wordmark.md            # Type and lockups
│   ├── 05-DesignSystem.md        # Tokens and components
│   └── 06-Packaging.md           # Final delivery
├── Templates/                    # Starter documents
└── Examples/
    └── sorted-brand-kit/         # Real-world example
```

## Triggers

- "Build a brand for [project]"
- "Create brand guidelines"
- "Design a logo and visual system"
- "I need a complete identity"

## Output

All generated files go to `~/Downloads/[brand]-brand-kit/` for review before use.

---

## The Process

Six phases, each producing specific artifacts:

| Phase | Output |
|-------|--------|
| 1. Discovery | Brand positioning, voice guidelines |
| 2. Visual Direction | Reference images exploring directions |
| 3. Mark Development | Iterated logo mark (SVG) |
| 4. Wordmark | Typography lockups |
| 5. Design System | Colors, type scale, components |
| 6. Packaging | Zipped kit with documentation |

**How it works:** This is iterative. Present options, get feedback, refine. User judgment drives decisions — your job is execution and expertise.

**Context-aware start:** When running in a session with codebase access, read the project files first (README, docs, code). Draft a positioning hypothesis, then present it for feedback. Don't open with a questionnaire.

---

## Phase Summaries

### Phase 1: Discovery

Establish the strategic foundation.

**With codebase access:**
1. Read project files to understand what it does and who it's for
2. Draft a brand positioning (core metaphor, personality, direction)
3. Present: "Based on what I see, here's my take..."
4. Refine based on feedback
5. Write philosophy docs

**Without context:**
1. Ask targeted questions about audience, personality, references
2. Identify the core metaphor
3. Write philosophy docs

**Outputs:** `[brand]-philosophy.md`, `[brand]-visual-philosophy.md`

### Phase 2: Visual Direction

Generate reference images to find the visual territory before committing to detailed work.

1. Write 3-4 prompts exploring different interpretations
2. Generate reference images
3. Present options with descriptions
4. User picks direction(s)
5. Generate refinements if needed

**Outputs:** Reference images (PNG)

### Phase 3: Mark Development

Iterate on the logo through SVG sketches. This is typically 15-30 versions.

1. Create initial batch (v1-v5) exploring the chosen direction
2. Present with descriptions
3. Get feedback, refine
4. Repeat until user locks a version
5. Always test at favicon size (32px, 16px)

**Outputs:** `[brand]-mark-final.svg`, favicon PNG

### Phase 4: Wordmark

Pair the mark with typography.

1. Choose font direction (sans, mono, etc.)
2. Create lockup variants
3. Refine alignment (this takes iteration)
4. Create system: horizontal, stacked, text-only

**Outputs:** `[brand]-wordmark-final.svg`, variants

### Phase 5: Design System

Define the complete visual language.

1. Color palette (backgrounds, text, functional, accents)
2. Typography (fonts, scale, weights)
3. Spacing (base unit, scale)
4. Components (buttons, inputs, cards)
5. Write comprehensive guidelines doc

**Outputs:** `[brand]-design-guidelines.md`

### Phase 6: Packaging

Collect everything for handoff.

1. Create kit folder
2. Copy all final assets
3. Write quick-start README
4. Zip for delivery

**Outputs:** `[brand]-brand-kit.zip`

---

## Guidelines

### On Iteration

Don't aim for perfection on the first try. The process is:
- Generate options
- Get reaction
- Refine
- Repeat

Version 15 is usually much better than version 3.

### On User Input

You bring expertise; they bring taste. Present options with your reasoning, but let them choose. Use `AskUserQuestion` when you genuinely need direction, not for validation.

### On Testing

Logos exist at multiple sizes: hero (200px+), app icon (64px), favicon (32px, 16px). Test all of them. If it falls apart small, simplify.

### On Color

Dark backgrounds should have warmth — pure #000 feels lifeless. Functional colors (green for success, red for error) carry meaning; don't use them decoratively.

### On Quality

Avoid generic patterns: purple-blue gradients, overly rounded shapes, meaningless geometric decorations. Create something distinctive that the brand can own.

---

## Dependencies

### Image Generation (Optional)

Phase 2 can use AI image generation for reference exploration. Options:

1. **Art skill** — If you have the Art skill installed, use its Generate.ts tool
2. **Manual references** — User provides mood board images or links
3. **Skip to SVG** — Go directly to Phase 3, iterate on concepts through code

If skipping image generation, start Phase 3 with more initial variations (8-10 instead of 4-5) to explore directions through SVG itself.

### SVG to PNG Conversion

For favicon generation, you need `rsvg-convert`:

```bash
# macOS
brew install librsvg

# Ubuntu/Debian
sudo apt-get install librsvg2-bin

# Check installation
rsvg-convert --version
```

**Alternative:** If rsvg-convert isn't available, create favicons by:
- Using an online SVG-to-PNG converter
- Opening the SVG in a browser and taking a screenshot
- Asking the user to export from their preferred tool

### Fonts

Uses system fonts by default. For web fonts:
- **Inter** — `https://fonts.google.com/specimen/Inter`
- **JetBrains Mono** — `https://fonts.google.com/specimen/JetBrains+Mono`

---

## Workflow Files

Each phase has detailed instructions in `Workflows/`:

- `01-Discovery.md` — Full discovery process with context-aware mode
- `02-VisualDirection.md` — Reference image generation guide
- `03-MarkDevelopment.md` — SVG iteration techniques
- `04-Wordmark.md` — Typography pairing and alignment
- `05-DesignSystem.md` — Token and component definitions
- `06-Packaging.md` — Asset collection and handoff

Read the relevant workflow file when executing each phase.
