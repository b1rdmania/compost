# Landing Page Copy Handoff

Designer handoff doc for refining the "Opportunity / Barrier" sections and related copy on `index.html`.

---

## Summary

The current landing page presumes visitors already understand HIP-3 mechanics. It jumps to ecosystem stats ("$32B volume") before explaining **what Compost actually is**. The goal is to rewrite Opportunity/Barrier so that a first-time visitor understands the product in under 10 seconds:

> Compost pools HYPE to help teams deploy HIP-3 markets (which require a 500k HYPE stake). In return, depositors earn a share of the builder fees those markets generate.

---

## What's Wrong Today

### 1. Hero defines category, not mechanism

**Current copy (lines 1280-1287):**
```html
<h1 class="hero-headline">compost<span class="tld">.fi</span></h1>
<p class="hero-tagline">The capital formation layer for Hyperliquid builder markets.</p>
...
<p class="hero-punchline">One token. Fee-backed yield.</p>
```

**Problem:**  
"Capital formation layer" is abstract. A first-time visitor doesn't know what that means or why they should care.

---

### 2. Opportunity/Barrier presumes knowledge

**Current copy (lines 1319-1356):**
```html
<p>Hyperliquid is the fastest-growing perpetuals exchange in crypto.</p>
<p>Anyone can now launch new markets — stocks, commodities, FX, prediction markets — all on-chain.</p>
...
<h3 class="barrier-headline">But there's a barrier.</h3>
...
<p class="barrier-subtext">This is protocol-defined — fee splits are on-chain, not discretionary.</p>
```

**Problem:**  
- Never explicitly states: "To deploy a market, teams must stake 500k HYPE (~$20M)."
- Never defines Compost's role: "We help teams raise that stake and share the resulting builder fees with depositors."
- The "Barrier" headline ("But there's a barrier") is vague—it should say *what* the barrier is.

---

### 3. "Exchange rate" phrasing reads like FX

**Current copy (lines 1418-1419):**
```html
<h3>Receive cHYPE</h3>
<p>Your receipt token. Appreciates via exchange rate as yield accrues — not rebasing, fully transferable</p>
```

**Problem:**  
"Exchange rate" sounds like forex. Crypto-native readers expect terms like "redeems for more HYPE" or "worth more HYPE over time."

---

## Proposed Narrative (Two-Sided)

The site should speak to **both audiences**:

| Audience | What they need |
|----------|----------------|
| **Teams** | 500k HYPE (~$20M) to deploy a new HIP-3 market |
| **Depositors** | Diversified exposure to builder fees without deploying themselves |

**Framing:**
1. **Opportunity**: HIP-3 markets pay builders 50% of fees (protocol-defined).
2. **Barrier**: Deploying requires staking 500k HYPE (~$20M).
3. **Compost**: The capital formation layer that helps fund deployments and routes a share of fees to depositors (via cHYPE).

---

## Drop-In Copy (Ready to Implement)

### Opportunity Section

**Replace the two intro paragraphs (lines 1320-1321) with:**

```
HIP-3 lets teams launch new perp markets on Hyperliquid.

Deployers earn 50% of trading fees — protocol-defined, on-chain.

To deploy, you must stake 500,000 HYPE (~$20M).
```

**Optional kicker (add after the above if needed):**

```
Compost is the layer that helps teams deploy — and lets anyone earn a share of those fees.
```

---

### Barrier Section

**Replace headline (line 1341):**

| Current | Proposed |
|---------|----------|
| "But there's a barrier." | "The barrier is deployment capital." |

**Update flow box subtitle (line 1345):**

| Current | Proposed |
|---------|----------|
| (~$15M) | (~$20M) |

**Replace subtext (line 1356):**

| Current | Proposed |
|---------|----------|
| "This is protocol-defined — fee splits are on-chain, not discretionary." | "Compost pools HYPE to back new HIP-3 deployments. In return, it earns a share of builder fees and passes them through to depositors." |

---

### Punchline Section

**Replace the punchline paragraph (line 1380):**

| Current | Proposed |
|---------|----------|
| "Compost gives you diversified access to this yield — without needing $15M or picking individual markets yourself." | "Compost is a capital formation layer for HIP-3: we help teams raise the 500k HYPE stake to deploy markets, then route a share of builder fees back to depositors in one token (cHYPE)." |

---

### "How It Works" Step 2

**Replace the description (line 1419):**

| Current | Proposed (Recommended) |
|---------|------------------------|
| "Your receipt token. Appreciates via exchange rate as yield accrues — not rebasing, fully transferable" | "Your receipt token. As fees accrue, cHYPE redeems for more HYPE over time — not rebasing, fully transferable." |

**Alternative option:**

```
Your receipt token. Fees compound into the vault, so cHYPE is worth more HYPE over time — not rebasing, fully transferable.
```

---

## Layout / Hierarchy Guidance

1. **Definition before stats**: Ensure "What is Compost?" appears *before* the big volume/fees numbers.

2. **Anchor with three numbers** (keep these prominent):
   - **500k HYPE (~$20M)** — deployment stake required
   - **50%** — share of fees to deployers
   - **$32B+ / $5M+** — volume and fees generated (proof)

3. **Use explicit nouns**: "deploy a market," "builder fees," "stake HYPE" — avoid abstract terms like "capital formation layer" in body copy (fine for tagline).

4. **No "exchange rate"**: Replace with "redeems for more HYPE" or "worth more HYPE over time."

5. **Two-sided language**: Acknowledge both teams (need capital) and depositors (want yield exposure) in the narrative flow.

---

## Quick Reference: Line Numbers in `index.html`

| Section | Lines | What to change |
|---------|-------|----------------|
| Hero tagline | 1281 | Optional: clarify mechanism |
| Hero punchline | 1287 | Optional: tighten |
| Opportunity intro | 1320-1321 | Replace paragraphs |
| Opportunity stats | 1324-1335 | Keep, but ensure ~$20M consistency |
| Barrier headline | 1341 | Change to "The barrier is deployment capital." |
| Barrier box subtitle | 1345 | Change (~$15M) → (~$20M) |
| Barrier subtext | 1356 | Replace with Compost definition |
| Punchline paragraph | 1380 | Replace with two-sided explanation |
| How it works step 2 | 1419 | Remove "exchange rate" phrasing |

---

## Checklist for Designer

- [ ] Replace Opportunity intro paragraphs
- [ ] Update Barrier headline
- [ ] Update Barrier box subtitle to ~$20M
- [ ] Replace Barrier subtext with Compost definition
- [ ] Replace Punchline paragraph
- [ ] Update "How it works" step 2 copy
- [ ] Verify all dollar figures use ~$20M (not $15M)
- [ ] Confirm no "exchange rate" language remains
