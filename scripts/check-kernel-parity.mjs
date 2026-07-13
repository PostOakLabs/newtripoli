// Browser↔worker parity gate (NEWTRIPOLI-CIGOLD-PARITY-SPEC.md §1.5.3, buildplan 1.5).
// Proves the site's vendored L1 kernels reproduce the worker's OCG execution_hash byte-for-byte —
// the machine-checkable form of "a browser slider run at defaults reproduces the worker's hash."
//
// Two assertions per tool:
//   (1) BYTE-EQUALITY  — repo/ch-sims/kernels/<slug>.kernel.mjs and repo/ch-sims/lib/_hash.mjs
//                        byte-equal the sibling worker originals. Missing sibling → SKIP (warn), so
//                        the site repo still builds standalone; when present the gate is authoritative.
//   (2) HASH REPRO     — import the SITE-copy kernel + _hash, assemble the same preimage the worker
//                        wraps (execution_backend:'js', canon_version from canon.js, fixture inputs),
//                        hash it, and assert it equals the worker golden.
//
// Run before any site deploy, alongside scripts/check-svgs.py (see svg-preflight-check memory).
// Read-only: does NOT write or touch the worker repo. Exit 1 on any failure.
import { readFileSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const imp = (p) => import(pathToFileURL(p).href);
import { executionHash } from '../ch-sims/lib/_hash.mjs';

const REPO = dirname(dirname(fileURLToPath(import.meta.url)));           // repo/
const SITE = resolve(REPO, 'ch-sims');                                   // repo/ch-sims/
const WORKER = resolve(REPO, '..', 'newtripoli-mcp-worker');             // sibling worker tree

// tool id → { slug } for all 12 tools (3 P1 L1 + 9 L2), master-table order (L2-CONSOLIDATE-SPEC §0.1).
const TOOLS = [
  { id: 'nt_time_dilation',        slug: 'time-dilation' },
  { id: 'nt_kinetic_probe',        slug: 'kinetic-probe' },
  { id: 'nt_vat_feasibility',      slug: 'vat-feasibility' },
  { id: 'nt_acceleration_ceiling', slug: 'acceleration-ceiling' },
  { id: 'nt_comms_lag',            slug: 'comms-lag' },
  { id: 'nt_ring_density',         slug: 'ring-density' },
  { id: 'nt_birthday_sacrifice',   slug: 'birthday-sacrifice' },
  { id: 'nt_synthetic_body',       slug: 'synthetic-body' },
  { id: 'nt_selection_cost',       slug: 'selection-cost' },
  { id: 'nt_interface_bandwidth',  slug: 'interface-bandwidth' },
  { id: 'nt_tech_tree_path',       slug: 'tech-tree' },
  { id: 'nt_provenance',           slug: 'provenance' },
];

let failed = 0;
const fail = (m) => { console.error('  ✗ ' + m); failed++; };
const ok = (m) => console.log('  ✓ ' + m);

// canon_version from the SITE canon.js (the string CH_CANON.CANON_VERSION exposes to the browser).
function siteCanonVersion() {
  const src = readFileSync(resolve(SITE, 'data', 'canon.js'), 'utf8');
  const m = /CANON_VERSION:\s*"([^"]+)"/.exec(src);
  if (!m) throw new Error('CANON_VERSION not found in repo/ch-sims/data/canon.js');
  return m[1];
}

function readFixture(slug) {
  // Fixtures are the canonical default inputs; they live only in the worker repo.
  return JSON.parse(readFileSync(resolve(WORKER, 'kernels', 'fixtures', `${slug}.fixture.json`), 'utf8'));
}

// ── (1) byte-equality of the vendored copies vs the worker originals ──────────
const workerPresent = existsSync(WORKER);
console.log(`\n[1] byte-equality of vendored kernels + _hash.mjs vs sibling worker`);
if (!workerPresent) {
  console.warn(`  ⚠ sibling worker tree not found at ${WORKER} — SKIPPING byte-equality (site builds standalone).`);
} else {
  const pairs = [
    ...TOOLS.map(t => [`kernels/${t.slug}.kernel.mjs`, `kernels/${t.slug}.kernel.mjs`]),
    ['lib/_hash.mjs', 'lib/_hash.mjs'],
  ];
  for (const [sitePath, workerPath] of pairs) {
    const a = readFileSync(resolve(SITE, sitePath));
    const b = readFileSync(resolve(WORKER, workerPath));
    if (Buffer.compare(a, b) === 0) ok(`byte-equal: ch-sims/${sitePath}`);
    else fail(`DRIFT: ch-sims/${sitePath} ≠ newtripoli-mcp-worker/${workerPath}`);
  }
}

// ── (2) hash reproduction: site kernel → same preimage → worker golden ────────
console.log(`\n[2] hash reproduction vs worker goldens`);
const canon_version = siteCanonVersion();
console.log(`  canon_version = ${canon_version}`);

// Worker goldens (may carry a null/blocked entry pre-freeze — handled below).
let goldens = {};
if (workerPresent) {
  try { goldens = JSON.parse(readFileSync(resolve(WORKER, 'kernels', 'fixtures', 'goldens.json'), 'utf8')); }
  catch { console.warn('  ⚠ could not read worker goldens.json — comparing against live worker recompute only.'); }
}

const reproduced = {};
for (const t of TOOLS) {
  const { compute } = await imp(resolve(SITE, "kernels", `${t.slug}.kernel.mjs`));
  const input_parameters = readFixture(t.slug);
  const policy_parameters = { execution_backend: 'js', canon_version, input_parameters };
  const { output_payload } = compute(policy_parameters);
  const hex = await executionHash(policy_parameters, output_payload);
  reproduced[t.id] = hex;

  const golden = goldens[t.id]?.execution_hash ?? null;
  if (golden === null) {
    // Pre-freeze (e.g. kinetic-probe before the post-parity freeze): no frozen hex to match yet.
    // Cross-check against a fresh worker-side recompute so parity is still proven end-to-end.
    if (workerPresent) {
      const { compute: wCompute } = await imp(resolve(WORKER, "kernels", `${t.slug}.kernel.mjs`));
      const { output_payload: wPayload } = wCompute(policy_parameters);
      const wHex = await executionHash(policy_parameters, wPayload);
      if (wHex === hex) ok(`${t.id}: site == worker recompute (${hex}) — golden not yet frozen, awaits post-parity freeze`);
      else fail(`${t.id}: site ${hex} ≠ worker recompute ${wHex}`);
    } else {
      console.warn(`  ⚠ ${t.id}: golden null and no worker tree — reproduced ${hex} (unverified)`);
    }
  } else if (golden === hex) {
    ok(`${t.id}: reproduced == frozen golden (${hex})`);
  } else {
    fail(`${t.id}: reproduced ${hex} ≠ frozen golden ${golden}`);
  }
}

console.log('\nreproduced hexes:');
for (const t of TOOLS) console.log(`  ${t.id}: ${reproduced[t.id]}`);

if (failed) { console.error(`\nPARITY GATE FAILED (${failed} check${failed > 1 ? 's' : ''}).`); process.exit(1); }
console.log('\nPARITY GATE PASSED — site kernels reproduce the worker execution_hash byte-for-byte.');
