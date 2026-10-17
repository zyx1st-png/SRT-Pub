"""Pure-statistical calibration check for the proposed 48-test NC-0a screen.

This is NOT an NC-0a connected-graph diagnostic and uses no neural data.
Its iid-normal toy differences check only the theoretical false-rejection
behavior of the Bonferroni/paired-t decision rule under its ideal assumptions.
"""

from __future__ import annotations

import math
import random
import statistics
import unittest

NUMBER_OF_COMPARISONS = 48
NUMBER_OF_CHAINS = 8
FAMILYWISE_ALPHA = 0.05
# t_(1 - 0.05 / (2 * 48), df=7), checked independently from scipy.stats.t.
PAIRED_T_CRITICAL = 5.369862606270659


def abs_paired_t(differences: list[float]) -> float:
    if len(differences) != NUMBER_OF_CHAINS:
        raise ValueError("Must supply exactly eight paired chain differences")
    if not all(math.isfinite(x) for x in differences):
        raise ValueError("Non-finite diagnostic")
    mean = statistics.mean(differences)
    sd = statistics.stdev(differences)
    if sd == 0.0:
        return 0.0 if mean == 0.0 else math.inf
    return abs(mean) / (sd / math.sqrt(NUMBER_OF_CHAINS))


def familywise_toy_rejection_rate(
    *,
    seed: int = 20261011,
    trials: int = 2500,
) -> float:
    """Monte Carlo toy with 48 independent normally distributed metrics.

    Every metric has eight independent *chain pairs* with zero-mean normal
    differences; it is not a random-graph stationary distribution test.
    """
    rng = random.Random(seed)
    rejected_families = 0
    for _ in range(trials):
        rejected = False
        for _ in range(NUMBER_OF_COMPARISONS):
            differences = [rng.gauss(0.0, 1.0)
                           for _ in range(NUMBER_OF_CHAINS)]
            if abs_paired_t(differences) > PAIRED_T_CRITICAL:
                rejected = True
                # Still advance the RNG across all fixed comparison slots.
        rejected_families += int(rejected)
    return rejected_families / trials


class StatisticalScreenTests(unittest.TestCase):
    def test_zero_and_nonzero_constant_differences(self):
        self.assertEqual(abs_paired_t([0.0] * 8), 0.0)
        self.assertEqual(abs_paired_t([2.0] * 8), math.inf)

    def test_fixed_large_shift_rejects(self):
        differences = [7.8, 8.1, 8.3, 7.7, 8.0, 7.9, 8.2, 8.1]
        self.assertGreater(abs_paired_t(differences), PAIRED_T_CRITICAL)

    def test_ideal_stationary_toy_false_rejection_is_near_five_percent(self):
        observed_rate = familywise_toy_rejection_rate()
        # Broad deterministic tolerance for a 2,500-family, toy-only check.
        # Passing does not show real graph chains are stationary at 4E.
        self.assertGreater(observed_rate, 0.03)
        self.assertLess(observed_rate, 0.07)


if __name__ == "__main__":
    unittest.main()
