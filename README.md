# Approximating Rényi divergences

A research workspace for finite horizon approximation of Rényi divergences between dependent probability laws.

## Start here

Read `AGENTS.md`, then `docs/RESEARCH_PLAN.md` and `docs/CLAIMS.md`.

The starting distinction is essential: independent coordinates need not be identically distributed for Rényi divergence to be additive. The research target is dependence after mixing, conditioning, adaptation or marginalisation, not merely nonidentical marginals.

## Research direction

Develop and analyse predictable increment estimators for the power integral gap. Begin with orders strictly between zero and one, keep exact product and observed Markov computations as controls, and investigate dependent observation laws with tractable conditional probabilities. Treat orders above one separately because likelihood ratio tails change the problem.

No general linear time approximation theorem for dependent laws is claimed.

## Workspace

| Path | Purpose |
| --- | --- |
| `docs/RESEARCH_PLAN.md` | Mathematical target, derivations, obstacles and staged work |
| `docs/CLAIMS.md` | Established facts, local derivations and open claims |
| `prompts/01_foundations.md` | First executable research brief |
| `sources/` | Source records, links and bibliography |
| `src/` | Small reference implementations |
| `tests/` | Deterministic mathematical regression tests |
| `experiments/` | Prespecified experiment designs |
| `results/` | Reproducible results and their provenance |
| `notes/` | Dated research notes |

## Validation

The initial reference code uses only the Python standard library. Run:

```sh
python -m unittest discover -s tests -v
```

The code is a small finite alphabet verification aid, not a production approximation algorithm. Numerical agreement does not replace proof.

## Source status

The motivating paper is Anand, Benford and Guo, arXiv:2607.27088v1. Its HTML was read on 16 September 2026. A source record and canonical links are maintained under `sources/2607.27088/`. A complete article copy is not included: the PDF endpoint could not be retrieved, and the displayed arXiv licence does not establish permission to republish the full text in this public repository.

## Working conventions

Use natural logarithms, preserve support conditions, and distinguish the divergence from its power integral and power integral gap. Keep conjectures separate from proofs. Avoid large generated files and do not upload third party full texts without appropriate permission. No project wide software licence is selected on the owner's behalf.
