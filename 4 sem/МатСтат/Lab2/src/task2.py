import numpy as np
from scipy.stats import norm

lambda_ = 1
true_median = np.log(2)
z = norm.ppf(0.975)
repeats = 1000


def coverage_rate(n):
    covered = 0
    for _ in range(repeats):
        sample = np.random.exponential(scale=1 / lambda_, size=n)
        sample_median = np.median(sample)
        ci_half_width = z / np.sqrt(n)
        lower = sample_median - ci_half_width
        upper = sample_median + ci_half_width
        if lower <= true_median <= upper:
            covered += 1
    return covered / repeats


coverage_25 = coverage_rate(25)
coverage_10000 = coverage_rate(10000)

print(f"Доля покрытий для n=25: {coverage_25:.3f}")
print(f"Доля покрытий для n=10000: {coverage_10000:.3f}")
