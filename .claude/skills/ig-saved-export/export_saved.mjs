/**
 * Export your Instagram *Saved* posts to a JSON file.
 *
 * Runs on YOUR computer (not in a cloud session) because Instagram blocks
 * datacenter logins and requires your account. A real browser window opens so
 * you can log in by hand (including 2FA) the first time; the login is then
 * cached in ./ig-user-data so later runs skip straight to scraping.
 *
 * Usage:
 *   npm i playwright && npx playwright install chromium   # one-time setup
 *   node export_saved.mjs <your_ig_username>
 *
 * Optional flags:
 *   --collection "Name"   Only scrape one saved collection (default: All Posts)
 *   --limit 200           Stop after N posts (default: no limit)
 *   --out saved_posts.json  Output path (default: saved_posts.json next to this script)
 *   --headless            Run without a visible window (only works once login is cached)
 *
 * Output: saved_posts.json — an array of
 *   { url, shortcode, type, author, caption, thumbnail, savedFrom, scrapedAt }
 *
 * Then drop saved_posts.json into the vault and run the `ig-content-router`
 * skill to turn each post into Content Engine entries.
 */

import { chromium } from "playwright";
import { fileURLToPath } from "node:url";
import { dirname, join, isAbsolute } from "node:path";
import { writeFileSync, existsSync, readFileSync } from "node:fs";

const HERE = dirname(fileURLToPath(import.meta.url));

// ---- tiny arg parser --------------------------------------------------------
const argv = process.argv.slice(2);
const flags = {};
const positional = [];
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a.startsWith("--")) {
    const key = a.slice(2);
    const next = argv[i + 1];
    if (next && !next.startsWith("--")) { flags[key] = next; i++; }
    else { flags[key] = true; }
  } else {
    positional.push(a);
  }
}

const username = positional[0] || flags.user;
if (!username) {
  console.error("Usage: node export_saved.mjs <your_ig_username> [--collection \"Name\"] [--limit N] [--out file.json]");
  process.exit(1);
}
const collection = flags.collection || null;
const limit = flags.limit ? parseInt(flags.limit, 10) : Infinity;
const outPath = flags.out
  ? (isAbsolute(flags.out) ? flags.out : join(process.cwd(), flags.out))
  : join(HERE, "saved_posts.json");
const headless = Boolean(flags.headless);

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// Resume support: keep already-scraped posts so a crash/re-run doesn't lose work.
function loadExisting() {
  if (!existsSync(outPath)) return [];
  try { return JSON.parse(readFileSync(outPath, "utf8")); } catch { return []; }
}

async function main() {
  const userDataDir = join(HERE, "ig-user-data");
  console.log(`\n▶ Launching browser (profile cached in ${userDataDir})`);
  const ctx = await chromium.launchPersistentContext(userDataDir, {
    headless,
    viewport: { width: 1280, height: 900 },
    args: ["--disable-blink-features=AutomationControlled"],
  });
  const page = ctx.pages()[0] || (await ctx.newPage());

  // ---- 1. ensure logged in --------------------------------------------------
  await page.goto("https://www.instagram.com/", { waitUntil: "domcontentloaded" });
  await sleep(2500);
  const loggedIn = await page.evaluate(() =>
    !document.querySelector('input[name="username"]')
  );
  if (!loggedIn) {
    if (headless) {
      console.error("Not logged in and --headless was set. Run once WITHOUT --headless to log in.");
      await ctx.close();
      process.exit(1);
    }
    console.log("\n🔑 Log in to Instagram in the browser window that just opened.");
    console.log("   Complete any 2FA / 'save login' prompts. I'll wait up to 5 minutes...");
    try {
      await page.waitForFunction(
        () => !document.querySelector('input[name="username"]'),
        { timeout: 300000 }
      );
    } catch {
      console.error("Timed out waiting for login. Re-run and log in faster.");
      await ctx.close();
      process.exit(1);
    }
    console.log("✅ Logged in. Login is cached for next time.\n");
    await sleep(2000);
  } else {
    console.log("✅ Already logged in (cached session).\n");
  }

  // ---- 2. go to the saved collection ---------------------------------------
  const savedUrl = collection
    ? `https://www.instagram.com/${username}/saved/` // land on list, then click
    : `https://www.instagram.com/${username}/saved/all-posts/`;
  await page.goto(savedUrl, { waitUntil: "domcontentloaded" });
  await sleep(3000);

  if (collection) {
    // Click the named collection tile.
    const clicked = await page.evaluate((name) => {
      const links = Array.from(document.querySelectorAll("a"));
      const match = links.find((a) => a.textContent.trim().toLowerCase() === name.toLowerCase());
      if (match) { match.click(); return true; }
      return false;
    }, collection);
    if (!clicked) {
      console.error(`Could not find a saved collection named "${collection}". Check the exact name.`);
      await ctx.close();
      process.exit(1);
    }
    await sleep(3000);
  }

  // ---- 3. scroll to load every thumbnail, collecting shortcodes ------------
  console.log("⏬ Scrolling to load all saved posts...");
  const shortcodes = new Set();
  let stagnant = 0;
  let lastCount = 0;
  while (stagnant < 4 && shortcodes.size < limit) {
    const found = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('a[href*="/p/"], a[href*="/reel/"]').forEach((a) => {
        const m = a.getAttribute("href").match(/\/(p|reel)\/([^/]+)\//);
        if (m) out.push({ type: m[1] === "reel" ? "reel" : "post", code: m[2] });
      });
      return out;
    });
    found.forEach((f) => shortcodes.add(JSON.stringify(f)));
    await page.evaluate(() => window.scrollBy(0, window.innerHeight * 2));
    await sleep(1500 + Math.floor(Math.random() * 800));
    if (shortcodes.size === lastCount) stagnant++;
    else { stagnant = 0; lastCount = shortcodes.size; }
    process.stdout.write(`\r   collected ${shortcodes.size} posts...`);
  }
  const items = Array.from(shortcodes).map((s) => JSON.parse(s)).slice(0, limit);
  console.log(`\n📌 Found ${items.length} saved posts. Fetching details...\n`);

  // ---- 4. visit each post, extract caption/author/media --------------------
  const existing = loadExisting();
  const byCode = new Map(existing.map((e) => [e.shortcode, e]));
  let i = 0;
  for (const it of items) {
    i++;
    if (byCode.has(it.code)) { continue; } // already have it from a prior run
    const url = `https://www.instagram.com/${it.type === "reel" ? "reel" : "p"}/${it.code}/`;
    try {
      await page.goto(url, { waitUntil: "domcontentloaded" });
      await sleep(1800 + Math.floor(Math.random() * 900));
      const data = await page.evaluate(() => {
        const og = (p) => document.querySelector(`meta[property="${p}"]`)?.content || "";
        // Author handle: from the header link, fall back to og:title.
        let author = "";
        const header = document.querySelector("header a[href^='/']");
        if (header) author = header.getAttribute("href").replace(/\//g, "");
        const title = og("og:title"); // e.g. 'Name (@handle) on Instagram: "caption"'
        if (!author) {
          const m = title.match(/\(@([^)]+)\)/);
          if (m) author = m[1];
        }
        return {
          author,
          caption: og("og:description") || "",
          thumbnail: og("og:image") || "",
          ogTitle: title,
        };
      });
      const record = {
        url,
        shortcode: it.code,
        type: it.type,
        author: data.author || "",
        caption: data.caption || "",
        thumbnail: data.thumbnail || "",
        savedFrom: collection || "All Posts",
        scrapedAt: new Date().toISOString(),
      };
      byCode.set(it.code, record);
      // Incremental save so nothing is lost mid-run.
      writeFileSync(outPath, JSON.stringify(Array.from(byCode.values()), null, 2));
      process.stdout.write(`\r   [${i}/${items.length}] @${record.author || "?"} ${record.type}   `);
    } catch (e) {
      console.log(`\n   ⚠ skipped ${url}: ${e.message}`);
    }
  }

  const all = Array.from(byCode.values());
  writeFileSync(outPath, JSON.stringify(all, null, 2));
  console.log(`\n\n✅ Done. Wrote ${all.length} posts to:\n   ${outPath}\n`);
  console.log("Next: copy saved_posts.json into your vault and run the `ig-content-router` skill.\n");
  await ctx.close();
}

main().catch((e) => {
  console.error("Fatal:", e);
  process.exit(1);
});
