#!/usr/bin/env python3
"""
check-svgs.py — pre-push guard for inline SVGs on the New Tripoli site.

SVG geometry/animation bugs parse fine and never throw; they only show up
visually (a wall crossing buildings, an element off-canvas, an animation
pointing at a missing id). This lints the cheap-to-catch cases and reminds
you to eyeball the rest on localhost.

HARD errors (exit 1):
  - an animation/reference (#id, url(#id), mpath, begin="id.…") whose target
    id does not exist in the same file
  - a per-file regression assertion fails (see REGRESSIONS)

WARNINGS (do not fail the build):
  - a static coordinate sits well outside its <svg> viewBox

Run from the repo root:  python scripts/check-svgs.py
Also runs in the deploy Action's preflight job.
"""
import os, re, sys, glob

# ---- per-file regression assertions ------------------------------------------
# Locks in fixes so a future edit can't silently reintroduce a known bug.
REGRESSIONS = {
    "ch-sims/index.html": {
        # cavern "tuna-can": near-vertical walls, flat floor. Must NOT go back
        # to the deep parabola whose sides swept over the ring buildings.
        "must_contain": ["M40 104 L40 342"],
        "must_not_contain": ["C40 104 40 360 120 360"],
    },
}

SVG_RE   = re.compile(r"<svg\b[^>]*>.*?</svg>", re.DOTALL | re.IGNORECASE)
VIEWBOX  = re.compile(r'viewBox\s*=\s*"([\d.\-\s]+)"')
ID_RE    = re.compile(r'\bid\s*=\s*"([^"]+)"')
# references that must resolve to an id in the same file
REF_RE   = re.compile(r'(?:xlink:href|href)\s*=\s*"#([^"]+)"'
                      r'|url\(#([^)]+)\)'
                      r'|begin\s*=\s*"([A-Za-z_][\w\-]*)\.')
COORD_RE = re.compile(r'\b(cx|cy|x|y)\s*=\s*"(-?\d+(?:\.\d+)?)"')

def files():
    for p in glob.glob("**/*.html", recursive=True):
        p = p.replace("\\", "/")
        if p.startswith((".git/", "latest/", "node_modules/")):
            continue
        yield p

def check():
    errors, warnings, animated = [], [], []
    for path in files():
        try:
            src = open(path, encoding="utf-8").read()
        except Exception as e:
            errors.append(f"{path}: cannot read ({e})")
            continue

        file_ids = set(ID_RE.findall(src))
        for grp in REF_RE.findall(src):
            ref = grp[0] or grp[1] or grp[2]
            if ref and ref not in file_ids:
                errors.append(f"{path}: reference #{ref} has no matching id")

        for m in SVG_RE.finditer(src):
            block = m.group(0)
            if "<animate" in block or "animateMotion" in block:
                animated.append(path)
            vb = VIEWBOX.search(block)
            if not vb:
                continue
            nums = [float(x) for x in vb.group(1).split()]
            if len(nums) != 4:
                continue
            minx, miny, w, h = nums
            mx, my = minx - w * 0.05, miny - h * 0.05
            Mx, My = minx + w * 1.05, miny + h * 1.05
            for name, val in COORD_RE.findall(block):
                v = float(val)
                if name in ("cx", "x") and (v < mx or v > Mx):
                    warnings.append(f"{path}: {name}={val} outside viewBox x[{minx:.0f},{minx+w:.0f}]")
                if name in ("cy", "y") and (v < my or v > My):
                    warnings.append(f"{path}: {name}={val} outside viewBox y[{miny:.0f},{miny+h:.0f}]")

    for path, rules in REGRESSIONS.items():
        if not os.path.exists(path):
            errors.append(f"{path}: expected file for regression check is missing")
            continue
        src = open(path, encoding="utf-8").read()
        for s in rules.get("must_contain", []):
            if s not in src:
                errors.append(f"{path}: regression — expected marker absent: {s!r}")
        for s in rules.get("must_not_contain", []):
            if s in src:
                errors.append(f"{path}: regression — known-bad pattern present: {s!r}")

    return errors, warnings, sorted(set(animated))

def main():
    errors, warnings, animated = check()
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    if animated:
        print("\nManual visual review (SVG animations) — eyeball on localhost, hard-refresh:")
        for p in animated:
            print(f"  - {p}")
    if errors:
        print(f"\ncheck-svgs: {len(errors)} error(s). Fix before pushing.")
        return 1
    print(f"\ncheck-svgs: OK ({len(warnings)} warning(s)).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
