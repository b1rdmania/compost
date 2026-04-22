# Compost

**Experimental Hyperliquid ideas, built in public.**

[compost.fi](https://compost.fi) · [@compostfi](https://twitter.com/compostfi) · [grow@compost.fi](mailto:grow@compost.fi)

---

Compost is a lab for exploring what can be built on and around Hyperliquid — HIP-3 builder markets, HIP-4 outcome trading, and execution primitives that connect them. Nothing here is production-ready. Everything here is real and running on testnet.

## What's live

### [HIP-3 Intelligence Board](https://compost.fi/hip3)
Live dashboard pulling builder market data from the Hyperliquid API. Tracks active deployers, volume, fee structures, and market metadata. Updated continuously.

### [HIP-4 Outcome Board](https://compost.fi/hip4)
Live testnet board for HIP-4 binary prediction markets. Shows active outcomes, YES/NO prices, settlement mechanics, and how outcome trading sits alongside the perp book. HIP-4 is testnet only for now.

### [Conditional Trigger](https://compost.fi/trigger)
The first conditional execution primitive on HIP-4. A HIP-4 binary market resolves → a perp order fires automatically. Watches live testnet outcomes every 8s; when a monitored outcome crosses the resolution threshold, it places a signed market order on the HL perp book via the exchange API. The frontend shows live probability bars, trigger rules, and a real-time activity log.

The server-side monitor (`scripts/trigger-monitor.js`) is a Node.js script using `@nktkas/hyperliquid` for EIP-712 signed order placement and raw fetch for outcome polling (the SDK's schema validation rejects testnet data).

### [cHYPE Vault Demo](https://compost.fi/litepaper)
ERC4626-style proof vault on HyperEVM testnet. Synthetic APR accrual, deposit/withdraw with `vHYPE` test tokens, live `pricePerShare`. Worked concept, parked for now — HIP-3 builder fee routing wasn't viable at the time.

### [WAR.MARKET](https://compost.fi/war)
Hackathon side project (winner, Hyperliquid London Hackathon @ Encode Club). Packages narrative macro views into one-click long/short baskets via Pear Protocol, settled on Hyperliquid. Lives at [war.market](https://war.market).

## Repo structure

```
/
├── index.html          # Landing page
├── hip3.html           # HIP-3 live intelligence board
├── hip4.html           # HIP-4 outcome board + explainer
├── trigger.html        # Conditional trigger frontend
├── litepaper.html      # cHYPE concept + vault demo links
├── war.html            # WAR.MARKET writeup
├── vault.html          # Static vault mockup
├── vault-test.html     # Live HyperEVM testnet demo
├── scripts/
│   ├── trigger-monitor.js      # HIP-4 resolution → perp order monitor
│   ├── trigger-config.json     # Trigger configuration (outcomes + actions)
│   ├── list-outcomes.js        # List live testnet HIP-4 outcomes
│   └── deploy-proof-vault.cjs  # Hardhat deploy for cHYPE vault
├── contracts/
│   ├── CompostProofVault.sol   # ERC4626-style vault
│   └── MockHype.sol            # vHYPE test token with faucet
└── assets/                     # Design system, icons, nav
```

## Running the conditional trigger monitor

```bash
# Install deps
npm install

# See what HIP-4 outcomes are live on testnet
npm run outcomes

# Dry run — logs what would fire, no orders placed
npm run trigger:dry

# Live mode — requires TRIGGER_PRIVATE_KEY in .env
npm run trigger
```

Copy `.env.example` to `.env` and add an API-only wallet key from your Hyperliquid settings. Never use your main wallet.

Configure which outcomes to watch and what to do on resolution in `scripts/trigger-config.json`.

## HyperEVM vault

```bash
npm run vault:compile
npm run vault:deploy:testnet
```

Deployed testnet contracts:
- `MockHype` (vHYPE): `0xAdBc75586E2F5338F460410B87F7AFde0374Fc31`
- `CompostProofVault` (cHYPE): `0x89bBacDACA0D20CB48FA617b57CF6779979AEC4E`

## Status

Experimental. Testnet only. Ideas get built here to see if they're real — some get parked, some keep going. HIP-4 mainnet is what determines whether the trigger primitive becomes something bigger.

If you're building on Hyperliquid and want to talk: [grow@compost.fi](mailto:grow@compost.fi)
