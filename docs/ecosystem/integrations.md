# Integrations

cHYPE is a standard ERC-20 token. It's composable across DeFi.

---

## Where cHYPE Can Be Used

| Integration | Use Case |
|-------------|----------|
| **Pendle** | Split into PT (principal) + YT (yield) — trade future yield |
| **Lending** (Morpho, Euler, Felix) | Use as collateral, borrow against yield position |
| **DEX** (Beets, etc.) | Provide liquidity in cHYPE pairs |
| **Yield aggregators** | Auto-compound strategies |
| **Structured products** | Use as underlying for other protocols |

---

## Pendle Integration

Split cHYPE into:

| Token | Description |
|-------|-------------|
| **PT (Principal Token)** | Fixed yield, redeemable at maturity for underlying |
| **YT (Yield Token)** | Variable yield exposure until maturity |

### Use Cases
- Lock in fixed yield by selling YT
- Speculate on yield by buying YT
- Leverage yield exposure

---

## Lending Integration

Use cHYPE as collateral on lending protocols.

### Benefits
- Borrow against your yield position
- No need to sell cHYPE
- Continue earning yield while borrowing

### Parameters (example)
| Parameter | Value |
|-----------|-------|
| LTV | 70-80% |
| Liquidation threshold | 85% |
| Oracle | cHYPE/HYPE exchange rate |

---

## API Access

For protocols and platforms integrating Compost.

### Endpoints

| Endpoint | Function |
|----------|----------|
| `POST /deposit` | Deposit HYPE, receive cHYPE |
| `POST /withdraw` | Burn cHYPE, queue HYPE withdrawal |
| `GET /balance` | cHYPE balance, HYPE value, yield accrued |
| `GET /nav` | Current cHYPE/HYPE exchange rate |
| `GET /yield` | Current APY, breakdown by source |
| `GET /allocations` | Current market allocations |

### Webhooks

- `deposit_confirmed`
- `withdrawal_ready`
- `yield_accrued` (daily)

Full API documentation: TBC

---

## Partnership Models

| Model | How It Works | Best For |
|-------|--------------|----------|
| **Standard integration** | Use API, no fee arrangement | Small integrations |
| **Revenue share** | Reduced protocol fee (10%), partner gets kickback | Large AUM partners |
| **Referral** | 10-20% of protocol fees on referred TVL | Affiliates, influencers |
| **White-label** | Full API, their brand, their clients | Platforms, neobanks |

---

## Get Started

Contact **grow@compost.fi** to discuss integration.

---

{% hint style="info" %}
**Next:** [Institutional Access](institutional.md)
{% endhint %}
