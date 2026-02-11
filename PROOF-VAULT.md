# HyperEVM Proof Vault (Testnet)

This is a scoped mechanism demo for Compost:

- `MockHype.sol` (`vHYPE`) test asset with wallet drip
- `CompostProofVault.sol` vault share model (`cHYPE`)
- synthetic APR accrual (default `10.00%`, `1000` bps)
- simple UI in `/vault-test.html`

## What this proves

- Vault accounting works on HyperEVM testnet.
- Users can mint test asset, approve, deposit, withdraw.
- Share price (`pricePerShare`) increases over time from APR accrual.

This does **not** route production yield from HIP-3 yet.

## Prerequisites

- Node 18+
- funded wallet on HyperEVM testnet (gas)

## Setup

```bash
npm install
cp .env.example .env
```

Set `DEPLOYER_PRIVATE_KEY` in `.env`.

## Compile and deploy

```bash
npm run vault:compile
npm run vault:deploy:testnet
```

Deployment prints:

- `MockHype` address
- `CompostProofVault` address

Paste both into `/vault-test.html` (Connection section), click **Save addresses**.

Current deployed testnet instance:

- `MockHype`: `0xAdBc75586E2F5338F460410B87F7AFde0374Fc31`
- `CompostProofVault`: `0x89bBacDACA0D20CB48FA617b57CF6779979AEC4E`

## Run UI locally

```bash
npm run dev
```

Open `http://localhost:3000/vault-test.html`.

## Faucet links

- HyperEVM testnet gas faucet: <https://faucet.chainstack.com/hyperliquid-testnet-faucet>
- If link changes, use Hyperliquid docs: <https://hyperliquid.gitbook.io/hyperliquid-docs>

## Contract model

- Vault asset: `vHYPE`
- Vault share: `cHYPE`
- `totalAssets` grows linearly with APR and elapsed time
- `accrue()` mints synthetic `vHYPE` interest into the vault
- `deposit(assets, receiver)` mints shares
- `withdraw(assets, receiver)` burns shares

## Notes

- APR can be updated by owner via `setAprBps(uint256)`.
- UI intentionally keeps scope small for a demo and avoids production complexity.
