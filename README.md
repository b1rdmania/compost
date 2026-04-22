# Compost

**Execution primitives for Hyperliquid HIP-3 and HIP-4, built in public.**

[compost.fi](https://compost.fi) · [@compostfi](https://twitter.com/compostfi) · [grow@compost.fi](mailto:grow@compost.fi)

---

Compost is a lab for what can be built on and around Hyperliquid — live market intelligence, outcome trading infrastructure, and execution primitives that connect HIP-4 resolution to HIP-3 order placement. Everything here is real. Most of it runs on testnet.

## What's live

### [Conditional Trigger](https://compost.fi/trigger)
A HIP-4 binary market resolves → a perp order fires automatically. The first conditional execution primitive on HIP-4.

The server-side monitor (`scripts/trigger-monitor.js`) polls live testnet outcomes every 8 seconds. When a monitored outcome crosses its resolution threshold, it constructs and signs a market order on the HL perp book via the exchange API (EIP-712, `@nktkas/hyperliquid`). The frontend shows live probability bars, trigger rules, and a real-time activity log.

```bash
npm run outcomes       # list live HIP-4 outcomes on testnet
npm run trigger:dry    # dry run — logs what would fire, places nothing
npm run trigger        # live mode (requires TRIGGER_PRIVATE_KEY in .env)
```

Configure outcomes to watch and what to do on resolution in `scripts/trigger-config.json`. Use an API-only wallet key from Hyperliquid settings — never your main wallet.

### [HIP-3 Intelligence Board](https://compost.fi/hip3)
Live dashboard pulling builder market data from the Hyperliquid API. Tracks active deployers, volume, fee structures, and market metadata. Updated continuously.

### [HIP-4 Outcome Board](https://compost.fi/hip4)
Live testnet board for HIP-4 binary prediction markets. Shows active outcomes, YES/NO prices, settlement mechanics, and how outcome trading sits alongside the perp book. HIP-4 is testnet-only for now.

### [WAR.MARKET](https://war.market)
Winner, Hyperliquid London Hackathon @ Encode Club. Packages narrative macro views into one-click long/short baskets routed via Pear Protocol, settled on Hyperliquid. Lives at [war.market](https://war.market) — this repo has the writeup, the code is at [b1rdmania/WarGames](https://github.com/b1rdmania/WarGames).

### [cHYPE Vault Demo](https://compost.fi/litepaper)
ERC4626-style proof vault on HyperEVM testnet. Deposit `vHYPE`, receive `cHYPE` shares, watch `pricePerShare` accrue via synthetic APR. Contracts deployed and working — the capital formation concept behind it is parked until HIP-3 builder fee routing matures.

```bash
npm run vault:compile
npm run vault:deploy:testnet
```

Deployed testnet contracts:
- `MockHype` (vHYPE): `0xAdBc75586E2F5338F460410B87F7AFde0374Fc31`
- `CompostProofVault` (cHYPE): `0x89bBacDACA0D20CB48FA617b57CF6779979AEC4E`

## Repo structure

```
/
├── index.html              # Landing page
├── hip3.html               # HIP-3 live intelligence board
├── hip4.html               # HIP-4 outcome board + explainer
├── trigger.html            # Conditional trigger frontend
├── litepaper.html          # cHYPE concept + vault demo links
├── war.html                # WAR.MARKET writeup
├── vault.html              # Static vault mockup
├── vault-test.html         # Live HyperEVM testnet demo
├── scripts/
│   ├── trigger-monitor.js      # HIP-4 resolution → perp order monitor
│   ├── trigger-config.json     # Trigger configuration (outcomes + actions)
│   ├── list-outcomes.js        # List live HIP-4 outcomes
│   └── deploy-proof-vault.cjs  # Hardhat deploy for cHYPE vault
├── contracts/
│   ├── CompostProofVault.sol   # ERC4626-style vault
│   └── MockHype.sol            # vHYPE test token with faucet
└── assets/                     # Design system, icons, nav
```

## Status

Testnet. Ideas get built here to see if they're real — some keep going, some get parked. Whether the trigger primitive becomes a production product depends on HIP-4 mainnet.

If you're building on Hyperliquid: [grow@compost.fi](mailto:grow@compost.fi)
