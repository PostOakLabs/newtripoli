# New Tripoli

**newtripoli.xyz** — an interactive portal for *New Tripoli*, a hard-SF alt-history/speculative-world scenario. It pairs long-form world-bible prose with a set of live, hash-verifiable physics instruments (the "Sim Terminal") and an MCP server that exposes the same instruments as tools for AI agents.

## What's here

- **Sim Terminal** (`ch-sims/`) — a phosphor-green, CRT-styled console of ~13 interactive instruments (time dilation, kinetic-probe delivery, vat feasibility, acceleration ceiling, comms lag, orbital ring density, synthetic-body mass, tech-tree solver, feasibility crosswalk, and more) plus narrative demo pages. Every instrument pulls its constants from a single canon source (`ch-sims/data/canon.js`) cited to section numbers in the underlying world-bible document, so numbers in the sims and numbers in the prose never drift apart.
- **Execution-hash provenance** — every sim run can emit a tamper-evident "Policy Mandate": a SHA-256 hash over its exact inputs, canon version, and outputs (OpenChainGraph artifact envelope). Anyone can recompute the hash and verify a result wasn't altered after the fact. See `ch-sims/mcp.html` for the full provenance story, `chaingraph.json` for the machine-readable tool/chain graph, and `llms.txt` for the discovery doc AI agents read first.
- **MCP server** — the same instruments are exposed as Model Context Protocol tools at `https://mcp.newtripoli.xyz/mcp`, so an AI agent can run New Tripoli physics calculations directly and get back the same hash-verifiable results a human sees in the browser. Source: [`PostOakLabs/newtripoli-mcp-worker`](https://github.com/PostOakLabs/newtripoli-mcp-worker).
- **Content manifest** (`manifest.json`) — frozen navigation index over the prose corpus (world bibles, canon documents, alt-history scenarios). The corpus itself is maintained off-repo; `scripts/build-manifest.py` rebuilds the manifest from it when the corpus is present, and `manifest.json` records the last built state (8 documents).

## Structure

```
repo/
├── ch-sims/        Sim Terminal portal app (sims/, demos/, data/canon.js, about.html, mcp.html)
├── manifest.json   frozen content-corpus manifest (corpus maintained off-repo)
├── scripts/        QA + build scripts (chaingraph/kernel/SVG checks; build-manifest.py)
├── manifest.json   navigation index for the portal
├── chaingraph.json machine-readable tool/chain graph (OCG catalog v0.8.0)
├── llms.txt         discovery doc for AI agents/crawlers
└── index.html       site home
```

## Live site

- Portal: https://newtripoli.xyz
- MCP + provenance explainer: https://newtripoli.xyz/ch-sims/mcp.html
- MCP endpoint: https://mcp.newtripoli.xyz/mcp

## License

- **Code:** MIT
- **Prose:** CC BY 4.0
- **Data:** CC0
