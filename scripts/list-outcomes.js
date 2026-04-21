/**
 * Compost — List live HIP-4 testnet outcomes with current YES/NO prices.
 * Use this to find the outcomeId values for trigger-config.json.
 *
 * Usage: node scripts/list-outcomes.js
 */

const TESTNET_URL = "https://api.hyperliquid-testnet.xyz";

async function hlInfo(type) {
  const res = await fetch(`${TESTNET_URL}/info`, {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify({ type }),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

const [outcomeMeta, spotData] = await Promise.all([
  hlInfo("outcomeMeta"),
  hlInfo("spotMetaAndAssetCtxs").catch(() => null),
]);

const ctxByCoin = new Map();
if (Array.isArray(spotData) && spotData.length >= 2) {
  const universe = spotData[0]?.universe ?? [];
  const ctxs     = spotData[1] ?? [];
  universe.forEach((asset, i) => {
    if (asset?.name) ctxByCoin.set(asset.name, ctxs[i]);
  });
}

const outcomes = outcomeMeta.outcomes ?? [];

if (outcomes.length === 0) {
  console.log("No outcomes found on testnet — try again later.");
  process.exit(0);
}

console.log(`\n${"─".repeat(72)}`);
console.log(`  HIP-4 Testnet Outcomes  (${outcomes.length} found)`);
console.log(`${"─".repeat(72)}\n`);

for (const outcome of outcomes) {
  const yesCoin = `#${outcome.outcome * 10}`;
  const noCoin  = `#${outcome.outcome * 10 + 1}`;
  const yesCtx  = ctxByCoin.get(yesCoin);
  const noCtx   = ctxByCoin.get(noCoin);

  const px      = (ctx) => ctx ? Number(ctx.markPx ?? ctx.midPx ?? 0) : null;
  const yesP    = px(yesCtx);
  const noP     = px(noCtx);
  const yesStr  = yesP !== null ? `${(yesP * 100).toFixed(1)}%` : "—";
  const noStr   = noP  !== null ? `${(noP  * 100).toFixed(1)}%` : "—";
  const status  = yesP === null ? "no price yet" :
                  yesP >= 0.95  ? "RESOLVED YES ✅" :
                  yesP <= 0.05  ? "RESOLVED NO  ❌" :
                  "open";

  console.log(`  outcomeId: ${outcome.outcome}    ${outcome.name}`);
  if (outcome.description) console.log(`  desc:      ${outcome.description}`);
  console.log(`  prices:    YES ${yesStr}  ·  NO ${noStr}  ·  ${status}`);
  console.log();
}

console.log(`${"─".repeat(72)}`);
console.log(`  Copy an outcomeId into scripts/trigger-config.json`);
console.log(`${"─".repeat(72)}\n`);
