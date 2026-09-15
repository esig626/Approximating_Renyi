# Initial validation

Date: 16 September 2026  
Environment: local execution container, Python 3.13.5  
Command: `python -m unittest discover -s tests -v`

Result: **12 tests passed**. These were deterministic calculations, including enumeration of small finite path laws. No stochastic performance experiment, large simulation, independent proof review or remote GitHub Actions run is claimed.

## Coverage

The tests check nonidentical product additivity; observed Markov recursion; predictable estimator unbiasedness; the rare gate second moment ratio; equal laws; deterministic one coordinate increments; exact zero support cases below and above one; invalid orders and probabilities; the common conditioning identity; and relative gap conversion above one.

Several tests contain multiple parameter subcases. The reported count of twelve is the number of test methods, not the total number of parameter combinations.

## File provenance

| File | SHA256 |
| --- | --- |
| `src/renyi_reference.py` | `b4a93b2257579c3e58a3181c1c2b8f90a5acf98830365b66a6248bcd6accdf91` |
| `tests/test_reference.py` | `5d9c32fcf67c241f425c1f70d3ef7d3bf321bd46101e99790bb90e6abcf8e704` |

The implementation uses ordinary floating point and is restricted to small models. Exact formulae in the mathematical sense are evaluated numerically; this is not an arbitrary precision implementation. A passing suite is not a proof of a general dependent law approximation theorem.
