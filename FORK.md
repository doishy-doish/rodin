# rodin fork (doishy-doish/rodin)

Upstream: https://github.com/cbritopacheco/rodin (Boost Software License 1.0).
Forked 2026-11-05 to (a) track upstream, (b) add a WASM-port layer mapping
rodin's professional density-optimization features onto a small browser SIMP core.

## What this fork adds (no upstream file modified)

- `WASM-PORT.md` — feature map: projected/regularized density updates,
  adjoint-consistent sensitivities, density vs sensitivity filtering, Heaviside
  projection + continuation, XDMF/VTK export, compliance history; plus what
  stays out of WASM (MPI, PETSc, MMG remeshing, Scotch partitioning).
- `bench/reference*.json` — verified 2D SIMP contracts from the browser core
  (cantilever/bridge/MBB/L-bracket: FE tips + compliance trajectories).
- `tools/compare_topo.py` — stdlib-only contract checker (tip 1%, trajectory 2%).

## Policy

- Upstream files are never edited in this fork; upgrades live in added files
  or in follow-up PRs upstream.
- License: BSL-1.0 preserved. Original copyright notices intact.
  Added files carry the same BSL-1.0 terms.
- Sync: rebase onto upstream master periodically; added files are
  upstream-agnostic (docs + bench + stdlib tool) so conflicts are ~nil.
