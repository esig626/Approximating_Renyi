# Research working instructions

Read `docs/RESEARCH_PLAN.md`, `docs/CLAIMS.md` and the relevant task in `prompts/` before changing scientific code or claims.

## Scope and correctness

1. Nonidentical independent coordinates still give additive Rényi divergence. Do not mistake a product of conditional kernels for a product measure.
2. Use natural logarithms and the exact definitions of H, Delta and D in the plan. State the order range, support assumptions, access model, horizon and error criterion.
3. The observed law is the target for mixtures and hidden Markov models. Do not replace it by an augmented latent law. For composite families, state any optimisation separately.
4. Keep local proofs, literature results, conjectures and numerical evidence distinct. A useful model specific variance bound is not yet established. The elementary identities have not been certified as novel.
5. Preserve the rare gate example. It disproves a uniform variance bound for the unmodified estimator, not the existence of every possible efficient algorithm.
6. Include probability evaluation, filtering, sampling, numerical precision and any backward calculations in complexity. Do not assume an unavailable conditional oracle.
7. Do not smooth exact zeros, clip invalid estimates into a success claim, or infer equality or absence of support violations from sampled paths.

## Workflow

Use a descriptive research branch for substantive follow on work. Preserve existing files and results. Never force push, rewrite unrelated history, or merge research changes without instruction. The initial workspace was created directly on the previously empty default branch at the owner's request.

Run `python -m unittest discover -s tests -v` after code changes. Add a regression test for every confirmed defect. Tiny enumeration is a reference calculation, not the proposed efficient implementation. Keep large simulations separate from deterministic tests.

Each result must record model, parameters, order, horizon, method, seed where relevant, path count, exact comparison where available, error criterion, runtime, software version and commit. Keep statistical, numerical and model approximation errors separate. Do not describe local tests as remote CI.

Update `docs/CLAIMS.md` whenever a claim is established, refuted or qualified. Record adverse examples as well as favourable ones. Store unresolved reasoning in dated notes rather than silently changing assumptions.

## Sources and publication

Record source version, theorem or page where relevant, reading status and limitations. Preserve third party attribution and licence boundaries. The motivating article is linked, not mirrored. Do not upload private correspondence, credentials or unrelated personal context. Do not add a software or manuscript licence without the owner's choice.
