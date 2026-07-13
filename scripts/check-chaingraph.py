#!/usr/bin/env python3
"""Validate chaingraph.json structure/counts and cross-check against the worker's
committed tools-manifest.json (SSOT). Run from repo/:  python3 scripts/check-chaingraph.py

Per NEWTRIPOLI-PHASE3-SPEC.md §4: chaingraph.json is hand-authored (not generated) while
alt-history stays HELD. This script is the sync gate that catches drift against the SSOT.
If the worker repo isn't checked out beside repo/, the cross-check is skipped with a
printed WARNING but structure/count validation still runs (so this is DreamHost-safe too).
"""
import json
import os
import sys

CG_PATH = "chaingraph.json"
MANIFEST_PATH = os.path.join("..", "newtripoli-mcp-worker", "data", "tools-manifest.json")

EXPECTED_TOOL_COUNT = 13
EXPECTED_CHAIN_COUNT = 7
EXPECTED_VERSION = "0.8.0"


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)


def main():
    with open(CG_PATH, encoding="utf-8") as fh:
        cg = json.load(fh)

    tools = cg.get("tools")
    chains = cg.get("chains")
    if not isinstance(tools, list):
        fail("chaingraph.json: 'tools' is not a list")
    if not isinstance(chains, list):
        fail("chaingraph.json: 'chains' is not a list")

    if len(tools) != EXPECTED_TOOL_COUNT:
        fail(f"expected {EXPECTED_TOOL_COUNT} tools, found {len(tools)}")
    if len(chains) != EXPECTED_CHAIN_COUNT:
        fail(f"expected {EXPECTED_CHAIN_COUNT} chains, found {len(chains)}")
    if cg.get("chaingraph_version") != EXPECTED_VERSION:
        fail(f"chaingraph_version expected {EXPECTED_VERSION!r}, "
             f"found {cg.get('chaingraph_version')!r}")

    required_tool_keys = {"tool_id", "mandate_type", "tool_version", "register", "guest_legal", "url"}
    for t in tools:
        missing = required_tool_keys - t.keys()
        if missing:
            fail(f"tool {t.get('tool_id', '?')} missing keys: {sorted(missing)}")

    required_chain_keys = {"chain_name", "title", "register", "tier", "gate", "step_tool_ids", "run_via"}
    for c in chains:
        missing = required_chain_keys - c.keys()
        if missing:
            fail(f"chain {c.get('chain_name', '?')} missing keys: {sorted(missing)}")

    print(f"structure OK: {len(tools)} tools, {len(chains)} chains, "
          f"chaingraph_version {EXPECTED_VERSION}")

    if not os.path.isfile(MANIFEST_PATH):
        print(f"WARNING: {MANIFEST_PATH} not found beside repo/ — skipping SSOT cross-check")
        return

    with open(MANIFEST_PATH, encoding="utf-8") as fh:
        manifest = json.load(fh)

    manifest_tools_by_id = {v["tool_id"]: v for v in manifest["tools"].values()}
    for t in tools:
        tid = t["tool_id"]
        if tid not in manifest_tools_by_id:
            fail(f"tool_id {tid} not found in tools-manifest.json")
        m = manifest_tools_by_id[tid]
        if t["mandate_type"] != m["mandate"]:
            fail(f"{tid}: mandate_type drift ({t['mandate_type']!r} != {m['mandate']!r})")
        if t["register"] != m["register"]:
            fail(f"{tid}: register drift ({t['register']!r} != {m['register']!r})")
        if t["guest_legal"] != m["guest_legal"]:
            fail(f"{tid}: guest_legal drift ({t['guest_legal']!r} != {m['guest_legal']!r})")
        expected_url = f"https://newtripoli.xyz/{m['path']}"
        if t["url"] != expected_url:
            fail(f"{tid}: url drift ({t['url']!r} != {expected_url!r})")

    manifest_chain_names = set(manifest["chains"].keys())
    for c in chains:
        if c["chain_name"] not in manifest_chain_names:
            fail(f"chain_name {c['chain_name']!r} not found in tools-manifest.json chains")

    print(f"SSOT cross-check OK against {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
