# WASM port map: rodin DensityOptimization -> browser SIMP core

Source example: `examples/DensityOptimization/TemperatureMinimization.cpp`
(SIMP, projected regularized density updates, adjoint, XDMF export).
Live browser core: unified C++ SIMP (2D corpus + 3D) compiled with Emscripten
SINGLE_FILE, differential-tested against bench contracts on every push.

## Feature map (professional -> WASM)

| rodin (professional) | browser core (this project) | status |
|---|---|---|
| Projected regularized density update (ell=4, mu=0.01, alpha=0.05, gmin=1e-4, gmax=1) | Heaviside projection: x_phys=(tanh(b*e)+tanh(b*(x-e)))/(tanh(b*e)+tanh(b*(1-e))), eta=0.5, beta schedule 1-2-4-8-16 | shipped (opt-in, default off = bit-identical legacy path) |
| Adjoint state + descent field exported before each update | Compliance history per iteration + CSV export; sensitivities chain-ruled through projection | shipped |
| Sensitivity filtering (rmin) | Sensitivity filter (default) + density-filter option (filter x, chain-rule dc) | shipped (opt-in) |
| P1/Triangle UniformGrid mesh, XDMF export | Q4 quads (2D) / hex (3D); .msh (Gmsh) + .vtk (ParaView) + SVG/PNG at crisp threshold | shipped |
| OC-style update with move limits | OC update, move=0.2, bisection on lambda 1e-4 | same |
| MPI / PETSc / MMG / Scotch | OUT of WASM scope: single-threaded, structured grids, Jacobi-CG | documented |

## Why opt-in defaults

The bench contracts (bench/*.json) pin the legacy trajectory bit-for-bit
(tip 1%, trajectory 2%). Projection and density-filter change the trajectory
by design, so they ship OFF by default; enabling them is one click and the
page labels the run pro-filtered.

## Contracts (from the browser core, mirrored here)

- cantilever 120x20: FE tip 880.2047 (beam theory 864.0, 1.88% off, CG 402 it)
- bridge 120x20: tip 36.4412, CG 328 it
- mbb 120x20: tip 62.9389, CG 578 it
- lbracket 60x60: tip 49.8555, CG 470 it
