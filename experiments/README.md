# Prespecified comparisons

These experiments are planned, not completed. The initial completed checks are deterministic tests under `tests/`.

Begin with alpha values 1/4, 1/2 and 3/4 and horizons small enough for exact enumeration. Treat alpha above one separately. Expand horizons only after exact agreement and oracle costs are understood.

| Family | Required comparison |
| --- | --- |
| Nonidentical products | Exact additive divergence, predictable gap, zero and nearby laws |
| Observed Markov laws | Finite horizon matrix recursion versus path enumeration |
| Common rare gate | Second moment ratio 1/tau and direct gate integration |
| Product mixtures | Direct paths versus component stratification; cancellation cases |
| Hidden observation models | Observable divergence, filter cost and history sensitivity |
| Common selected products | Direct conditioning versus three tilted event probabilities |
| Small overlap and high orders | Gap conversion failure, tails and numerical precision |

For stochastic runs, fix seeds in committed configuration files and use independent repetitions to assess coverage. Record the model, all probabilities, order, horizon, algorithm, seed, sample or particle count, exact reference when available, variance, runtime, error criterion and commit. Use increased precision checks for cancellation. Report adverse examples and separate statistical, numerical and model approximation errors.

Do not launch a broad parameter sweep before completing Task 01. Do not store large generated path tables in Git.
