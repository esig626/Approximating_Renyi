# Task 01: audit foundations and test component integration

Read `AGENTS.md`, `docs/RESEARCH_PLAN.md` and `docs/CLAIMS.md`. Work on a new descriptive research branch; do not merge to main without instruction.

## Objective

Determine whether conditioning on a finite mixture component improves the predictable estimator of the observed Rényi power integral gap, without changing the target law.

## Required sequence

1. Independently verify the proofs in plan Sections 5, 6 and 9. Record exact hypotheses and any correction. Check the common event identity in Section 7. Do not present an already known identity as novel.
2. Reproduce all twelve existing tests. Add explicit tests for the remaining gain identity and the conditional second moment lemma on tiny examples. Preserve the rare gate failure.
3. Implement finite mixtures of explicit positive binary products. Supply exact prefix likelihoods, component posterior weights, conditional observation vectors and exact sequential sampling. Keep the simulation label out of the observable posterior filtration.
4. Verify all conditional vectors and observed power integrals against path enumeration for short horizons. Measure the full conditional oracle cost, not only the estimator arithmetic.
5. Compare direct mixture path sampling with separate estimates conditional on each known component, recombined with the correct weights. For independent strata, derive the variance as the sum of squared stratum weights times within stratum variance divided by allocated sample count. State how allocation is chosen without assuming unknown variances for free.
6. Test identical observed mixtures with different component representations, nearby mixtures with cancellation, rare informative components and the common rare gate. Work initially at alpha = 1/2, then check 1/4 and 3/4. Include a representative order above one only as a separate comparison.
7. Audit R1 against earlier filtered Monte Carlo and Hellinger process work. Record what was actually read. Search for existing finite horizon Rényi approximation guarantees for mixtures before making a novelty claim.

## Deliverables

A reviewed derivation note under `notes/`, a small mixture implementation with tests, a reproducible comparison under `experiments/`, a result record with parameters and commit, and an updated claims register.

Finish with one precise statement: a proved improvement under explicit assumptions, a counterexample to the proposed improvement, or a narrower unresolved condition. A favourable plot alone does not complete the task. Do not silently substitute divergence of latent and observed variables for divergence of observations.
