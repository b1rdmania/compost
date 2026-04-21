/**
 * Compost — HIP-4 Conditional Trigger Monitor
 *
 * Watches HIP-4 outcome markets on the Hyperliquid testnet.
 * When a monitored outcome resolves YES or NO, fires a perp order
 * on the configured market via the HL exchange API.
 *
 * Usage:
 *   node scripts/trigger-monitor.js
 *   node scripts/trigger-monitor.js --config scripts/trigger-config.json
 *   node scripts/trigger-monitor.js --dry-run   (log only, no orders placed)
 *
 * Config: scripts/trigger-config.json
 * Env:    TRIGGER_PRIVATE_KEY  — HL API wallet private key (0x-prefixed)
 *                                Use an API-only key from HL settings, not your main wallet.
 */

import { HttpTransport, ExchangeClient } from "@nktkas/hyperliquid";
import { privateKeyToAccount } from "viem/accounts";
import { readFileSync } from "fs";
import { resolve } from "path";

// ─── Constants ────────────────────────────────────────────────────────────────

const TESTNET_URL      = "https://api.hyperliquid-testnet.xyz";
const POLL_INTERVAL_MS = 8_000;   // poll every 8 seconds
const YES_RESOLVED     = 0.95;    // YES price ≥ this → resolved YES
const NO_RESOLVED      = 0.05;    // YES price ≤ this → resolved NO

// ─── CLI flags ────────────────────────────────────────────────────────────────

const args       = process.argv.slice(2);
const isDryRun   = args.includes("--dry-run");
const cfgIdx     = args.indexOf("--config");
const configPath = cfgIdx !== -1
  ? resolve(args[cfgIdx + 1])
  : resolve("scripts/trigger-config.json");

// ─── Logger ───────────────────────────────────────────────────────────────────

function log(level, msg, data) {
  const ts     = new Date().toISOString().slice(11, 23);
  const icons  = { info: "·", ok: "✅", warn: "⚠️ ", error: "❌", fire: "🔥" };
  const icon   = icons[level] ?? "·";
  const suffix = data ? `  ${JSON.stringify(data)}` : "";
  console.log(`[${ts}] ${icon}  ${msg}${suffix}`);
}

// ─── Config loader ────────────────────────────────────────────────────────────

function loadConfig(path) {
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch (err) {
    log("error", `Cannot read config at ${path}: ${err.message}`);
    process.exit(1);
  }
}

// ─── HL exchange client (signing only — info uses raw fetch) ──────────────────

function buildExchange(privateKey) {
  if (!privateKey || isDryRun) return null;
  const transport = new HttpTransport({ url: TESTNET_URL });
  const wallet    = privateKeyToAccount(privateKey);
  return new ExchangeClient({ wallet, transport });
}

// ─── Perp asset index lookup ──────────────────────────────────────────────────

async function buildPerpIndex() {
  const data  = await hlInfo("meta");
  const index = {};
  (data.universe ?? []).forEach((asset, i) => {
    index[asset.name] = i;
  });
  return index;
}

// ─── Raw HL info request (bypasses SDK schema validation for testnet compat) ──

async function hlInfo(type) {
  const res = await fetch(`${TESTNET_URL}/info`, {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify({ type }),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status} from /info?type=${type}`);
  return res.json();
}

// ─── Fetch live HIP-4 outcomes with YES/NO prices ─────────────────────────────

async function fetchOutcomes() {
  const [outcomeMeta, spotData] = await Promise.all([
    hlInfo("outcomeMeta"),
    hlInfo("spotMetaAndAssetCtxs").catch(() => null),
  ]);

  // Build coin → ctx map  (coin names look like "#90", "#91" for outcome 9)
  const ctxByCoin = new Map();
  if (Array.isArray(spotData) && spotData.length >= 2) {
    const universe = spotData[0]?.universe ?? [];
    const ctxs     = spotData[1] ?? [];
    universe.forEach((asset, i) => {
      if (asset?.name) ctxByCoin.set(asset.name, ctxs[i]);
    });
  }

  return (outcomeMeta.outcomes ?? []).map((outcome) => {
    const yesCoin = `#${outcome.outcome * 10}`;
    const noCoin  = `#${outcome.outcome * 10 + 1}`;
    const yesCtx  = ctxByCoin.get(yesCoin);
    const noCtx   = ctxByCoin.get(noCoin);

    // Prefer markPx; fall back to midPx
    const px = (ctx) => ctx ? Number(ctx.markPx ?? ctx.midPx ?? 0) : null;

    return {
      outcomeId:   outcome.outcome,
      name:        outcome.name || "(unnamed)",
      description: outcome.description || "",
      sideSpecs:   outcome.sideSpecs ?? [],
      yesCoin,
      noCoin,
      yesPrice:    px(yesCtx),
      noPrice:     px(noCtx),
    };
  });
}

// ─── Resolution detection ─────────────────────────────────────────────────────

function detectResolution(outcome) {
  const p = outcome.yesPrice;
  if (p === null || !Number.isFinite(p)) return null;
  if (p >= YES_RESOLVED) return "YES";
  if (p <= NO_RESOLVED)  return "NO";
  return null;
}

// ─── Order placement ──────────────────────────────────────────────────────────

async function placeOrder(exchange, perpIdx, trigger, side) {
  const action = side === "YES" ? trigger.onYes : trigger.onNo;

  if (!action || action.skip) {
    log("info", `No action for ${side} on #${trigger.outcomeId} — skipping`);
    return;
  }

  const { direction, size, leverage = 1 } = action;
  const isBuy = direction === "long";

  log("fire", `Trigger fired: ${direction.toUpperCase()} ${size} ${trigger.perpAsset}`, {
    outcome: trigger.outcomeId,
    resolvedSide: side,
    dryRun: isDryRun,
  });

  if (isDryRun) {
    log("info", "DRY RUN — no order sent");
    return;
  }

  try {
    // Set leverage
    await exchange.updateLeverage({
      asset: perpIdx,
      isCross: true,
      leverage,
    });

    // Market order: use IOC with wide limit price
    const limitPx = isBuy ? "9999999" : "0.000001";

    const result = await exchange.order({
      orders: [{
        a: perpIdx,
        b: isBuy,
        p: limitPx,
        s: String(size),
        r: false,
        t: { limit: { tif: "FrontendMarket" } },
      }],
      grouping: "na",
    });

    const status = result?.response?.data?.statuses?.[0];
    if (status?.filled) {
      log("ok", `Filled — avgPx ${status.filled.avgPx}, sz ${status.filled.totalSz}`);
    } else if (status?.resting) {
      log("ok", `Resting — oid ${status.resting.oid}`);
    } else if (status?.error) {
      log("error", `Order error: ${status.error}`);
    } else {
      log("warn", "Unknown order status", status);
    }
  } catch (err) {
    log("error", `Order failed: ${err.message}`);
  }
}

// ─── Main ─────────────────────────────────────────────────────────────────────

async function run() {
  const config     = loadConfig(configPath);
  const privateKey = process.env.TRIGGER_PRIVATE_KEY ?? null;

  if (!privateKey && !isDryRun) {
    log("warn", "TRIGGER_PRIVATE_KEY not set — running in dry-run mode");
  }

  const exchange = buildExchange(privateKey);

  log("info", "Compost trigger monitor starting", {
    testnet:  TESTNET_URL,
    dryRun:   isDryRun || !privateKey,
    triggers: config.triggers.length,
    pollMs:   POLL_INTERVAL_MS,
  });

  // Build trigger map: outcomeId → config
  const triggerMap = new Map(config.triggers.map((t) => [t.outcomeId, t]));
  for (const [id, t] of triggerMap) {
    log("info", `Watching #${id} "${t.label ?? ""}"`);
  }

  // Fetch perp asset index (BTC → 0, ETH → 1, etc.)
  let perpIndex = {};
  try {
    perpIndex = await buildPerpIndex();
    log("info", `Loaded ${Object.keys(perpIndex).length} perp markets`);
  } catch (err) {
    log("warn", `Could not load perp meta: ${err.message}`);
  }

  // Track fired outcomes to avoid duplicate orders
  const fired = new Set();

  // ── Poll tick ──────────────────────────────────────────────────────────────

  async function tick() {
    let outcomes;
    try {
      outcomes = await fetchOutcomes();
    } catch (err) {
      log("error", `Fetch error: ${err.message}`);
      return;
    }

    const byId = new Map(outcomes.map((o) => [o.outcomeId, o]));

    for (const [id, trigger] of triggerMap) {
      if (fired.has(id)) continue;

      const outcome = byId.get(id);
      if (!outcome) {
        log("warn", `Outcome #${id} not in feed — may be settled or not yet deployed`);
        continue;
      }

      const resolution = detectResolution(outcome);

      if (resolution) {
        fired.add(id);

        log("fire", `#${id} "${outcome.name}" → resolved ${resolution}`, {
          yesPrice: outcome.yesPrice?.toFixed(4),
          noPrice:  outcome.noPrice?.toFixed(4),
        });

        const assetIdx = perpIndex[trigger.perpAsset];
        if (assetIdx === undefined) {
          log("error", `Unknown perp "${trigger.perpAsset}" — check config`);
          continue;
        }

        await placeOrder(exchange, assetIdx, trigger, resolution);

      } else {
        // Still open — log the current probability
        const pct = outcome.yesPrice !== null
          ? `${(outcome.yesPrice * 100).toFixed(1)}% YES`
          : "no price";
        log("info", `#${id} "${outcome.name}" — ${pct} (watching)`);
      }
    }
  }

  // Run once immediately then on interval
  await tick();
  const timer = setInterval(tick, POLL_INTERVAL_MS);

  process.on("SIGINT", () => {
    log("info", "Shutting down");
    clearInterval(timer);
    process.exit(0);
  });
}

run().catch((err) => {
  console.error("Fatal:", err);
  process.exit(1);
});
