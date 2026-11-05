# bench contracts (mirrored from the browser SIMP core)

Each reference JSON pins: grid, volfrac, penal, rmin, iteration count,
uniform-density FE tip (+ beam-theory check where applicable) and the full
compliance trajectory. Checker: `tools/compare_topo.py ref.json cand.json`
(tip within 1%, every trajectory point within 2%).

- reference.json — cantilever 120x20 (contract topo-bench-v1)
- reference-bridge.json — bridge 120x20
- reference-mbb.json — mbb 120x20
- reference-lbracket.json — lbracket 60x60
