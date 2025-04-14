import numpy as np
from math import sqrt


def get_sigma(s1, s2, n1, n2):
    return sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def check_confidence_interval(param, x1, x2, s, z):
    low = x1 - x2 - z * s
    high = x1 - x2 + z * s
    return low <= param <= high


mu1 = 2
mu2 = 1

sigma1 = sqrt(1)
sigma2 = sqrt(0.5)

tau = mu1 - mu2

size1 = 25
size2 = 10000

z_quantile = 1.96

sigma = get_sigma(sigma1, sigma2, size1, size1)
sigma_large = get_sigma(sigma1, sigma2, size2, size2)

count = 0
for i in range(1000):
    selection1 = np.random.normal(loc=mu1, scale=sigma1, size=size1)
    selection2 = np.random.normal(loc=mu2, scale=sigma2, size=size1)
    average1 = np.average(selection1)
    average2 = np.average(selection2)
    if check_confidence_interval(tau, average1, average2, sigma, z_quantile):
        count += 1
print("Количество попаданий в доверительный интервал с объемом выборки 25:", count)

count = 0
for i in range(1000):
    selection1 = np.random.normal(loc=mu1, scale=sigma1, size=size2)
    selection2 = np.random.normal(loc=mu2, scale=sigma2, size=size2)
    average1 = np.average(selection1)
    average2 = np.average(selection2)
    if check_confidence_interval(tau, average1, average2, sigma_large, z_quantile):
        count += 1
print("Количество попаданий в доверительный интервал с объемом выборки 10000:", count)
