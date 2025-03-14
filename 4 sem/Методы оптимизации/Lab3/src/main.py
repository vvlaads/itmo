from math import log
from method import *


def func(x):
    return 1 / 3 * x ** 3 - 5 * x + x * log(x)


x1 = 1.5
delta_x = 1
epsilon1 = 0.0001
epsilon2 = 0.0001

x_res, f_res, k = method(x1, delta_x, epsilon1, epsilon2, func)
print("Метод квадратичной аппроксимации")
print("Значение x: ", x_res)
print("Значение функции в точке: ", f_res)
print("Количество итераций: ", k)
