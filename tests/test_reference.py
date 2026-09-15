import math
import unittest
from itertools import product
from src.renyi_reference import (power_integral, divergence, product_law,
    markov_power, predictable_values, mixture_moments, rare_gate)


class ReferenceTests(unittest.TestCase):
    def test_nonidentical_product_additivity(self):
        pm = [[.2, .8], [.65, .35], [.4, .6]]
        qm = [[.4, .6], [.3, .7], [.55, .45]]
        p, q = product_law(pm), product_law(qm)
        for a in (.25, .5, .8, 1.5, 2):
            with self.subTest(alpha=a):
                direct = divergence(list(p.values()), list(q.values()), a)
                self.assertAlmostEqual(direct, sum(divergence(x, y, a)
                                                  for x, y in zip(pm, qm)), places=12)

    def test_markov_recursion(self):
        pi, qi = [.35, .65], [.6, .4]
        pt = [[[.8, .2], [.3, .7]], [[.6, .4], [.2, .8]]]
        qt = [[[.6, .4], [.5, .5]], [[.3, .7], [.4, .6]]]
        paths = list(product(range(2), repeat=3))
        p = [pi[x[0]] * pt[0][x[0]][x[1]] * pt[1][x[1]][x[2]] for x in paths]
        q = [qi[x[0]] * qt[0][x[0]][x[1]] * qt[1][x[1]][x[2]] for x in paths]
        for a in (.25, .5, 1.5, 2):
            with self.subTest(alpha=a):
                self.assertAlmostEqual(markov_power(pi, qi, pt, qt, a),
                                       power_integral(p, q, a), places=12)

    def test_predictable_unbiasedness(self):
        p = {(0, 0): .1, (0, 1): .2, (1, 0): .3, (1, 1): .4}
        q = {(0, 0): .3, (0, 1): .1, (1, 0): .4, (1, 1): .2}
        for a in (.2, .5, .8, 1.5, 2):
            with self.subTest(alpha=a):
                values = predictable_values(p, q, a)
                mean, _ = mixture_moments(p, q, values)
                gap = abs(power_integral(list(p.values()), list(q.values()), a) - 1)
                self.assertAlmostEqual(mean, gap, places=12)
                self.assertGreaterEqual(min(values.values()), -1e-12)

    def test_rare_gate_relative_variance(self):
        for a in (.5, 1.5, 2):
            for tau in (.1, .01, .001):
                with self.subTest(alpha=a, tau=tau):
                    p, q = rare_gate(tau)
                    mean, second = mixture_moments(p, q, predictable_values(p, q, a))
                    self.assertAlmostEqual(second / mean**2, 1/tau, places=7)

    def test_equal_laws(self):
        p, _ = rare_gate(.1)
        for a in (.5, 2):
            values = predictable_values(p, p, a)
            self.assertLess(max(abs(v) for v in values.values()), 1e-12)

    def test_one_coordinate_is_deterministic(self):
        p, q = {(0,): .2, (1,): .8}, {(0,): .6, (1,): .4}
        values = predictable_values(p, q, .5)
        self.assertAlmostEqual(values[(0,)], values[(1,)])

    def test_zero_support_orders_below_one(self):
        self.assertEqual(power_integral([1., 0.], [0., 1.], .5), 0)
        self.assertTrue(math.isinf(divergence([1., 0.], [0., 1.], .5)))

    def test_zero_support_orders_above_one(self):
        self.assertTrue(math.isinf(power_integral([1., 0.], [0., 1.], 2)))
        self.assertTrue(math.isinf(divergence([1., 0.], [0., 1.], 2)))

    def test_invalid_order(self):
        for a in (0, 1, -1, math.inf, math.nan):
            with self.subTest(alpha=a), self.assertRaises(ValueError):
                power_integral([.5, .5], [.5, .5], a)

    def test_invalid_probabilities(self):
        for p in ([.2, .2], [-.2, 1.2], [math.nan, .5], []):
            with self.subTest(p=p), self.assertRaises(ValueError):
                power_integral(p, [.5, .5], .5)

    def test_conditioned_product_identity(self):
        p = product_law([[.2, .8], [.7, .3], [.4, .6]])
        q = product_law([[.4, .6], [.5, .5], [.6, .4]])
        event = [x for x in p if sum(x) >= 2]
        pe, qe = sum(p[x] for x in event), sum(q[x] for x in event)
        for a in (.5, 1.5):
            with self.subTest(alpha=a):
                full = power_integral(list(p.values()), list(q.values()), a)
                tilt_event = sum(p[x]**a * q[x]**(1-a) for x in event) / full
                direct = power_integral([p[x]/pe for x in event], [q[x]/qe for x in event], a)
                self.assertAlmostEqual(direct, full * tilt_event / (pe**a * qe**(1-a)), places=12)

    def test_relative_gap_conversion_above_one(self):
        for gap in (1e-6, .1, 1, 100):
            eps = .1
            truth = math.log1p(gap)
            for estimate in ((1-eps)*gap, (1+eps)*gap):
                self.assertLessEqual(abs(math.log1p(estimate)/truth - 1), eps + 1e-12)


if __name__ == '__main__':
    unittest.main()
