import numpy as np


def validate_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def validate_interval(a, b):
    if a < b:
        return True
    return False


def check_necessary_condition(a, b, func):
    if func(a) * func(b) < 0:
        return True
    return False


def check_count_of_roots(a, b, func):
    count = 0
    if func(a) < 0:
        sign = -1
    else:
        sign = 1
    array = np.linspace(a, b)
    for element in array:
        if func(element) * sign < 0:
            count += 1
            sign *= -1
    return count
