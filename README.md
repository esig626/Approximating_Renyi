# Approximating Rényi divergences

A research workspace for finite horizon approximation of Rényi divergences between dependent probability laws.

## Start here

Read [AGENTS.md](AGENTS.md), the [research plan](docs/RESEARCH_PLAN.md), and the [claims register](docs/CLAIMS.md). The next executable brief is [Task 01](prompts/01_foundations.md).

Independent coordinates need not be identically distributed for Rényi divergence to be additive. The research target is dependence after mixing, conditioning, adaptation or marginalisation, not merely nonidentical marginals.

The initial direction is a predictable increment estimator for the power integral gap. Begin with orders strictly between zero and one; retain exact products and observed Markov chains as controls. Treat orders above one separately. No general linear time theorem for dependent laws is claimed.

## Workspace

| Path | Purpose |
| --- | --- |
| `docs/RESEARCH_PLAN.md` | Mathematical target, proofs, obstacles and staged work |
| `docs/CLAIMS.md` | Established facts, local derivations and open claims |
| `prompts/01_foundations.md` | First executable research brief |
| `sources/` | Source record, author PDF link and bibliography |
| `src/renyi_reference.py` | Small finite alphabet reference calculations |
| `tests/test_reference.py` | Deterministic mathematical regression tests |
| `experiments/README.md` | Prespecified experiment families |
| `results/VALIDATION.md` | Initial validation and provenance |
| `notes/` | Dated research notes |

## Validation

The reference code uses only the Python standard library. From the repository root run:

```sh
python -m unittest discover -s tests -v
```

The initial twelve tests passed locally under Python 3.13.5. No remote CI run is claimed. This is an ordinary floating point verification aid, not a production approximation algorithm; full path enumeration is deliberately restricted to tiny models.

## Source status

The motivating paper is Anand, Benford and Guo, arXiv:2607.27088v1. Its HTML and author hosted PDF were inspected on 16 September 2026. See the [source record](sources/2607.27088/record.md) for canonical links and reading notes.

A full article copy is not mirrored here. The displayed arXiv licence does not establish permission to republish the complete text in this public repository. The source record includes a direct author PDF link; it is not a substitute article or a claim that PDF bytes have been archived.

## Conventions

Use natural logarithms and preserve support conditions. Separate divergence, power integral and power integral gap. Distinguish proofs, numerical checks, conjectures and literature results. Do not upload third party full texts without suitable permission. No project wide software licence is selected on the owner's behalf.
