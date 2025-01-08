from cmath import exp, pi

from my_math import custom_sqrt


def func_w1(z):
    return z * z


def func_w2(w1):
    return w1 + 1


def func_w3(w2):
    return custom_sqrt(w2)


def func_w4(w3):
    return custom_sqrt(w3)


def func_w(w4):
    return exp(pi * 1j / 4) * w4


def func_z_to_w(z):
    return exp(pi * 1j / 4) * custom_sqrt(custom_sqrt(z * z + 1))


def func_w_to_z(w):
    return custom_sqrt(exp(-pi * 1j) * w ** 4 - 1)


def generate_after_func(array_x, array_y, x_after, y_after, func):
    for i in range(len(array_x)):
        z = array_x[i] + 1j * array_y[i]
        w = func(z)
        x_after.append(w.real)
        y_after.append(w.imag)
