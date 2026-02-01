# Risk

Understanding and mitigating risks in Compost.

---

## Smart Contract Risk

Vault contracts may contain bugs or vulnerabilities.

### Impact
Loss of funds if exploited.

### Mitigation

| Measure | Status |
|---------|--------|
| Audit | TBC |
| Bug bounty | TBC |
| Multisig controls | Yes |
| Gradual TVL ramp-up | Yes |

---

## Slashing Risk

HIP-3 deployers can be slashed for malicious behaviour.

### Slashing Conditions
- Bad oracles (manipulated or stale price feeds)
- Market manipulation
- Parameter abuse

### Impact
If Compost stakes directly and is slashed, the loss is absorbed by the vault (all cHYPE holders).

### Mitigation

| Measure | Implementation |
|---------|----------------|
| Careful market selection | Due diligence process |
| Diversification | No single market >25% of vault |
| Monitoring | Real-time alerts |
| Conservative approach | Structured exposure only for unproven markets (no large direct concentration) |

---

## Operator Risk

Deployers (Felix, Ventuals, etc.) may mismanage markets, have technical issues, or act against staker interests.

### Impact
Reduced yield, potential losses, reputational damage.

### Mitigation

| Measure | Implementation |
|---------|----------------|
| Due diligence | Background checks on operators |
| Diversification | Spread across operators |
| Monitoring | Track market health metrics |
| Relationships | Direct communication with teams |

---

## Liquidity Risk

In a bank run scenario, the vault may not have enough liquid HYPE to cover all redemptions immediately.

### Impact
Delayed withdrawals, potential NAV discount on secondary market.

### Mitigation

| Measure | Implementation |
|---------|----------------|
| Liquidity buffer | 20-30% in validator staking |
| Secondary market | Alternative exit path |
| Tranched redemptions | Large withdrawals processed gradually |
| Communication | Clear updates during stress events |

---

## Regulatory Risk

HIP-3 markets (especially equities, pre-IPO) may face regulatory scrutiny.

### Impact
Forced shutdown of certain markets, compliance requirements.

### Mitigation

| Measure | Implementation |
|---------|----------------|
| Legal review | Structure reviewed by counsel |
| Institutional onboarding | KYC/AML for large depositors |
| Geographic restrictions | Where required |
| Monitoring | Track regulatory developments |

---

## Risk Summary

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Smart contract | High | Low | Audit, bug bounty, gradual rollout |
| Slashing | High | Low | Diversification, monitoring |
| Operator | Medium | Medium | Due diligence, diversification |
| Liquidity | Medium | Low | Buffer, secondary market |
| Regulatory | Medium | Medium | Legal review, compliance |

---

::: warning
**No investment is risk-free.** Only deposit what you can afford to lose. Do your own research.
:::

---

::: info
**Next:** [Integrations](../ecosystem/integrations.md)
:::
