#!/usr/bin/env python3
"""Compare a SIMP candidate JSON against a bench reference JSON.
Usage: compare_topo.py <ref.json> <cand.json>
PASS iff |tip-tip_ref|/tip_ref <= 1% and every trajectory point <= 2%.
Matches bench/check.py + bench/check_corpus.py tolerances. Stdlib only.
"""
import json, sys

def main():
    if len(sys.argv) != 3:
        print("usage: compare_topo.py <ref.json> <cand.json>")
        return 2
    ref = json.load(open(sys.argv[1]))
    cand = json.load(open(sys.argv[2]))
    fails = []
    for k in ("contract", "preset", "nelx", "nely", "volfrac", "penal", "rmin", "iters"):
        if ref.get(k) != cand.get(k):
            fails.append(f"meta {k}: ref={ref.get(k)} cand={cand.get(k)}")
    tt, tc = ref["tip_full_density"], cand["tip_full_density"]
    if abs(tc - tt) / abs(tt) > 0.01:
        fails.append(f"tip {tc} vs {tt} (>1%)")
    for i, (a, b) in enumerate(zip(ref["compliance_trajectory"], cand["compliance_trajectory"])):
        if abs(b - a) / abs(a) > 0.02:
            fails.append(f"traj[{i}] {b} vs {a} (>2%)")
            break
    if fails:
        print("FAIL")
        for f in fails:
            print(" -", f)
        return 1
    print(f"PASS preset={ref['preset']} tip={tc} iters={ref['iters']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
