import numpy as np
from math import sqrt, log, exp


# Коэффициент корреляции Пирсона
def correlation(x_arr, y_arr, size):
    x_average = 0
    y_average = 0
    for i in range(size):
        x_average += x_arr[i]
        y_average += y_arr[i]
    x_average /= size
    y_average /= size

    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for i in range(size):
        x = x_arr[i]
        y = y_arr[i]
        numerator += (x - x_average) * (y - y_average)
        denominator1 += (x - x_average) ** 2
        denominator2 += (y - y_average) ** 2
    return numerator / sqrt(denominator1 * denominator2)


# Коэффициент детерминации
def determination(y_arr, phi_arr, size):
    phi_average = 0
    for i in range(size):
        phi_average += phi_arr[i]
    phi_average /= size

    numerator = 0
    denominator = 0
    for i in range(size):
        y = y_arr[i]
        phi = phi_arr[i]
        numerator += (y - phi) ** 2
        denominator += (y - phi_average) ** 2
    return 1 - (numerator / denominator)


# Линейная функция phi(x) = a * x + b
def linear_func(x_arr, y_arr, size):
    sx = 0
    sxx = 0
    sy = 0
    sxy = 0
    for i in range(size):
        x = x_arr[i]
        y = y_arr[i]

        sx += x
        sxx += x * x
        sy += y
        sxy += x * y

    # a sxx + b sx = sxy
    # a sx + b size = sy
    left = np.array([[sxx, sx], [sx, size]])
    right = np.array([sxy, sy])

    a, b = np.linalg.solve(left, right)

    def phi(value):
        return a * value + b

    return a, b, phi, correlation(x_arr, y_arr, size)


# Полиномиальная функция 2-й степени phi(x) = a0 + a1 * x + a2 * x ** 2
def polynomial_func2(x_arr, y_arr, size):
    sx = 0
    sxx = 0
    sxxx = 0
    sxxxx = 0
    sy = 0
    sxy = 0
    sxxy = 0
    for i in range(size):
        x = x_arr[i]
        y = y_arr[i]

        sx += x
        sxx += x * x
        sxxx += x ** 3
        sxxxx += x ** 4
        sy += y
        sxy += x * y
        sxxy += x * x * y

    # a0 size + a1 sx + a2 sxx = sy
    # a0 sx + a1 sxx + a2 sxxx = sxy
    # a0 sxx + a1 sxxx + a2 sxxxx = sxxy
    left = np.array([[size, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]])
    right = np.array([sy, sxy, sxxy])

    a0, a1, a2 = np.linalg.solve(left, right)

    def phi(value):
        return a0 + a1 * value + a2 * value ** 2

    return a0, a1, a2, phi


# Полиномиальная функция 3-й степени phi(x) = a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3
def polynomial_func3(x_arr, y_arr, size):
    sx = 0
    sxx = 0
    sxxx = 0
    sxxxx = 0
    sxxxxx = 0
    sxxxxxx = 0
    sy = 0
    sxy = 0
    sxxy = 0
    sxxxy = 0
    for i in range(size):
        x = x_arr[i]
        y = y_arr[i]

        sx += x
        sxx += x * x
        sxxx += x ** 3
        sxxxx += x ** 4
        sxxxxx += x ** 5
        sxxxxxx += x ** 6
        sy += y
        sxy += x * y
        sxxy += x * x * y
        sxxxy += x ** 3 * y

    # a0 size + a1 sx + a2 sxx + a3 sxxx = sy
    # a0 sx + a1 sxx + a2 sxxx + a3 sxxxx = sxy
    # a0 sxx + a1 sxxx + a2 sxxxx + a3 sxxxxx = sxxy
    # a0 sxxx + a1 sxxxx + a2 sxxxxx + a3 sxxxxxx = sxxxy
    left = np.array(
        [[size, sx, sxx, sxxx], [sx, sxx, sxxx, sxxxx], [sxx, sxxx, sxxxx, sxxxxx], [sxxx, sxxxx, sxxxxx, sxxxxxx]])
    right = np.array([sy, sxy, sxxy, sxxxy])

    a0, a1, a2, a3 = np.linalg.solve(left, right)

    def phi(value):
        return a0 + a1 * value + a2 * value ** 2 + a3 * value ** 3

    return a0, a1, a2, a3, phi


# Экспоненциальная функция phi(x) = a * e^bx
def exponential_func(x_arr, y_arr, size):
    y_log = []
    for i in range(size):
        y_log.append(log(y_arr[i]))
    b, a, phi_l, cor = linear_func(x_arr, y_log, size)

    a = exp(a)

    def phi(value):
        return a * exp(b * value)

    return a, b, phi


# Логарифмическая функция phi(x) = a ln(x) + b
def logarithmic_func(x_arr, y_arr, size):
    x_log = []
    for i in range(size):
        x_log.append(log(x_arr[i]))
    a, b, phi_l, cor = linear_func(x_log, y_arr, size)

    def phi(value):
        return a * log(value) + b

    return a, b, phi


# Степенная функция phi(x) = a * x^b
def power_func(x_arr, y_arr, size):
    x_log = []
    y_log = []
    for i in range(size):
        x_log.append(log(x_arr[i]))
        y_log.append(log(y_arr[i]))
    b, a, phi_l, cor = linear_func(x_log, y_log, size)
    a = exp(a)

    def phi(value):
        return a * value ** b

    return a, b, phi
