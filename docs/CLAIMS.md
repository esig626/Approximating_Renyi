# Claims register

Date: 16 September 2026. This register distinguishes mathematical derivations from novelty and computational claims.

| ID | Claim | Status and evidence |
| --- | --- | --- |
| C01 | Rényi divergence is additive over independent, nonidentical coordinates | Established literature: R2, Theorem 28 |
| C02 | Observed finite Markov power integrals have a matrix recursion | Elementary derivation in plan Section 4; enumeration regression test |
| C03 | The predictable estimator has mean Delta for strictly positive finite sequence laws | Derived with proof in Section 5; deterministic checks; independent review and novelty audit pending |
| C04 | R at every history bounded by K times global Delta implies second moment at most 2K Delta squared | Derived with proof in Section 6; conditional statement, not a verified model specific assumption |
| C05 | Positivity and bounded likelihood ratios alone uniformly control the estimator's relative variance | False for this estimator: the common rare gate gives relative variance 1/tau minus 1 |
| C06 | No algorithm can efficiently handle the rare gate model | Not claimed; exact Markov recursion and gate integration solve that example |
| C07 | Conditioning two products on a common event reduces the power integral to three event probabilities | Derived algebraically in Section 7; deterministic regression test |
| C08 | Relative gap accuracy automatically implies relative divergence accuracy uniformly for orders below one | False without additional overlap control; Section 9 states a sufficient promise and conversion |
| C09 | Relative gap accuracy transfers to relative divergence accuracy for orders above one | Elementary logarithmic concavity argument; regression check |
| C10 | A practical explicit K is available for arbitrary mixtures or hidden observation laws | Open; no such bound established here |
| C11 | The proposed method has linear cost in the horizon for general dependent laws | Not established; path cost, variance and conversion must all be included |
| C12 | The predictable identity is a new publishable result | Not asserted; filtered Monte Carlo and Hellinger process literature must be audited |

R1 to R5 refer to the research plan bibliography. The initial code is ordinary floating point on small finite models; numerical tests are not independent proofs. No stochastic performance experiment or remote CI run is reported as completed.
