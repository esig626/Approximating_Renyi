"""Small finite alphabet reference calculations, not production estimators.

Natural logarithms. Full path enumeration is intentionally exponential.
No support smoothing or probability clipping is performed.
"""
from itertools import product
import math
from collections.abc import Mapping, Sequence

Path = tuple[int, ...]
Law = Mapping[Path, float]


def _order(alpha: float) -> None:
    if not math.isfinite(alpha) or alpha <= 0 or alpha == 1:
        raise ValueError("Require finite alpha > 0 with alpha != 1")


def _probabilities(p: Sequence[float]) -> None:
    if not p or any(not math.isfinite(x) or x < 0 for x in p):
        raise ValueError("Probabilities must be finite and nonnegative")
    if not math.isclose(math.fsum(p), 1.0, rel_tol=0, abs_tol=1e-12):
        raise ValueError("Probabilities must sum to one")


def _power_term(p: float, q: float, alpha: float) -> float:
    if p == 0:
        return 0.0
    if q == 0:
        return math.inf if alpha > 1 else 0.0
    return math.exp(alpha * math.log(p) + (1 - alpha) * math.log(q))


def power_integral(p: Sequence[float], q: Sequence[float], alpha: float) -> float:
    """Return sum p**alpha q**(1-alpha), with exact zero semantics."""
    _order(alpha)
    _probabilities(p)
    _probabilities(q)
    if len(p) != len(q):
        raise ValueError("Alphabet sizes differ")
    return math.fsum(_power_term(x, y, alpha) for x, y in zip(p, q))


def divergence(p: Sequence[float], q: Sequence[float], alpha: float) -> float:
    h = power_integral(p, q, alpha)
    if h == 0 or math.isinf(h):
        return math.inf
    return math.log(h) / (alpha - 1)


def product_law(marginals: Sequence[Sequence[float]]) -> dict[Path, float]:
    if not marginals:
        raise ValueError("Provide at least one coordinate")
    for row in marginals:
        _probabilities(row)
    return {x: math.prod(marginals[i][c] for i, c in enumerate(x))
            for x in product(*(range(len(row)) for row in marginals))}


def markov_power(initial_p: Sequence[float], initial_q: Sequence[float],
                 transitions_p: Sequence[Sequence[Sequence[float]]],
                 transitions_q: Sequence[Sequence[Sequence[float]]],
                 alpha: float) -> float:
    """Exact algebraic forward recursion, evaluated in ordinary floating point.

    Strictly positive rows are required here to avoid ambiguous zero times
    infinity at unreachable states. The separate power_integral handles zeros.
    """
    _order(alpha)
    if len(initial_p) != len(initial_q) or len(transitions_p) != len(transitions_q):
        raise ValueError("Model dimensions differ")
    size = len(initial_p)
    rows = [initial_p, initial_q]
    for sequence in (transitions_p, transitions_q):
        for matrix in sequence:
            if len(matrix) != size or any(len(row) != size for row in matrix):
                raise ValueError("Transition matrices must be square")
            rows.extend(matrix)
    for row in rows:
        _probabilities(row)
        if any(x == 0 for x in row):
            raise ValueError("This Markov reference requires positive probabilities")
    v = [_power_term(p, q, alpha) for p, q in zip(initial_p, initial_q)]
    for p, q in zip(transitions_p, transitions_q):
        v = [math.fsum(v[x] * _power_term(p[x][y], q[x][y], alpha)
                       for x in range(size)) for y in range(size)]
    return math.fsum(v)


def predictable_values(p: Law, q: Law, alpha: float) -> dict[Path, float]:
    """Enumerate the predictable gap estimator on every path.

    Requires matching, strictly positive finite path supports. Conditional
    probabilities are formed by enumeration, so this is NOT a fast oracle.
    """
    _order(alpha)
    if not p or set(p) != set(q):
        raise ValueError("Provide matching nonempty supports")
    _probabilities(list(p.values()))
    _probabilities(list(q.values()))
    n = len(next(iter(p)))
    if n == 0 or any(len(x) != n for x in p):
        raise ValueError("Paths must have a common positive length")
    if any(v <= 0 for v in (*p.values(), *q.values())):
        raise ValueError("This reference requires strictly positive path masses")
    sign = 1 if alpha > 1 else -1
    cache: dict[Path, float] = {}
    for i in range(n):
        for prefix in {x[:i] for x in p}:
            paths = [x for x in p if x[:i] == prefix]
            pp = math.fsum(p[x] for x in paths)
            qq = math.fsum(q[x] for x in paths)
            symbols = sorted({x[i] for x in paths})
            pc = [math.fsum(p[x] for x in paths if x[i] == c) / pp for c in symbols]
            qc = [math.fsum(q[x] for x in paths if x[i] == c) / qq for c in symbols]
            a, b = pp / (pp + qq), qq / (pp + qq)
            w = 2 * _power_term(a, b, alpha)
            increment = sign * w * (power_integral(pc, qc, alpha) - 1)
            if increment < -1e-12:
                raise ArithmeticError("Unexpected negative increment")
            cache[prefix] = increment  # Tiny roundoff is retained, not clipped.
    return {x: math.fsum(cache[x[:i]] for i in range(n)) for x in p}


def mixture_moments(p: Law, q: Law, values: Mapping[Path, float]) -> tuple[float, float]:
    if set(p) != set(q) or set(p) != set(values):
        raise ValueError("Supports differ")
    mean = math.fsum((p[x] + q[x]) * values[x] / 2 for x in p)
    second = math.fsum((p[x] + q[x]) * values[x] ** 2 / 2 for x in p)
    return mean, second


def rare_gate(tau: float) -> tuple[dict[Path, float], dict[Path, float]]:
    """Common Bernoulli gate; differing conditional laws only on gate=1."""
    if not 0 < tau < 1:
        raise ValueError("Require 0 < tau < 1")
    p = {(0, 0): (1-tau)/2, (0, 1): (1-tau)/2,
         (1, 0): tau*0.75, (1, 1): tau*0.25}
    q = {(0, 0): (1-tau)/2, (0, 1): (1-tau)/2,
         (1, 0): tau*0.25, (1, 1): tau*0.75}
    return p, q
