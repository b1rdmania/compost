# Compost

Execution primitives for Hyperliquid HIP-3 and HIP-4, built in public.

[compost.fi](https://compost.fi) · [@compostfi](https://twitter.com/compostfi) · [grow@compost.fi](mailto:grow@compost.fi)

---

Live dashboards tracking HIP-3 builder market activity and HIP-4 outcome trading. A conditional trigger that fires perp orders when HIP-4 outcomes resolve. A working ERC4626 vault on HyperEVM testnet. All open source, all testnet.

## What's here

**[WAR.MARKET](https://war.market)** — Winner, Hyperliquid London Hackathon @ Encode Club. One-click long/short baskets from narrative macro views, routed via Pear Protocol and settled on Hyperliquid. Live at [war.market](https://war.market) · Code at [b1rdmania/WarGames](https://github.com/b1rdmania/WarGames).

**[Conditional Trigger](https://compost.fi/trigger)** — A HIP-4 binary market resolves → a signed perp order fires. Polls live testnet outcomes every 8 seconds via raw fetch (the `@nktkas/hyperliquid` SDK's schema validation rejects testnet data, so the info layer uses raw fetch; the exchange client handles EIP-712 order signing). Configure which outcomes to watch and what to do on resolution in `scripts/trigger-config.json`.

**[HIP-3 Intelligence Board](https://compost.fi/hip3)** — Live dashboard pulling builder market data from the Hyperliquid API. Active deployers, volume, fee structures, market metadata.

**[HIP-4 Outcome Board](https://compost.fi/hip4)** — Live testnet board for HIP-4 binary prediction markets. YES/NO prices, settlement mechanics, how outcome trading sits alongside the perp book.

**[cHYPE Vault Demo](https://compost.fi/litepaper)** — ERC4626 vault on HyperEVM testnet. Deposit `vHYPE`, receive `cHYPE` shares, `pricePerShare` accrues via synthetic APR. Contracts deployed and working; the capital formation concept behind it is parked until HIP-3 builder fee routing matures.

## Running the trigger

```bash
npm run outcomes     # list live HIP-4 outcomes on testnet
npm run trigger:dry  # log what would fire — no orders placed
npm run trigger      # live mode (requires TRIGGER_PRIVATE_KEY in .env)
```

Configure which outcomes to watch in `scripts/trigger-config.json`:

```json
{
  "triggers": [
    {
      "outcomeId": 4751,
      "label": "BTC > $75,615 by 2026-04-22 03:00 UTC",
      "perpAsset": "BTC",
      "onYes": { "direction": "long",  "size": 0.001, "leverage": 5 },
      "onNo":  { "direction": "short", "size": 0.001, "leverage": 3 }
    }
  ]
}
```

Get live outcome IDs from `npm run outcomes` or the [HIP-4 board](https://compost.fi/hip4). Use an API-only wallet key from Hyperliquid settings — never your main wallet.

## HyperEVM vault

Deployed testnet contracts:
- `MockHype` (vHYPE): `0xAdBc75586E2F5338F460410B87F7AFde0374Fc31`
- `CompostProofVault` (cHYPE): `0x89bBacDACA0D20CB48FA617b57CF6779979AEC4E`

## Repo structure

```
index.html              Landing page
hip3.html               HIP-3 live intelligence board
hip4.html               HIP-4 outcome board + explainer
trigger.html            Conditional trigger frontend
litepaper.html          cHYPE concept + vault demo
war.html                WAR.MARKET writeup
scripts/
  trigger-monitor.js    HIP-4 resolution → perp order monitor
  trigger-config.json   Trigger configuration
  list-outcomes.js      List live testnet HIP-4 outcomes
contracts/
  CompostProofVault.sol ERC4626-style vault
  MockHype.sol          vHYPE test token with faucet
assets/                 Design system, icons, nav
```

## License

MIT
