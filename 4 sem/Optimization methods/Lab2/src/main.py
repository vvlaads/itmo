import sympy as sp
from math import log
from methods import *


def func(x):
    return 1 / 3 * x ** 3 - 5 * x + x * log(x)


def func_symbol():
    x = sp.symbols('x')
    return 1 / 3 * x ** 3 - 5 * x + x * sp.log(x)


def func_df1(x):
    return func_symbol().diff('x').subs('x', x).evalf()


def func_df2(x):
    return func_symbol().diff('x').diff('x').subs('x', x).evalf()


def print_separator():
    print("---- ---- ---- ---- ---- ---- ---- ---- ---- ----")


a = 1.5
b = 2

epsilon = 0.0001

x_res, f_res, k = half_division_method(a, b, epsilon, func)
print("Метод половинного деления")
print("Найденное значение x: ", x_res)
print("Значение функции в точке: ", f_res)
print("Количество итераций: ", k)
print_separator()

x_res, f_res, k = golden_ratio_method(a, b, epsilon, func)
print("Метод золотого сечения")
print("Найденное значение x: ", x_res)
print("Значение функции в точке: ", f_res)
print("Количество итераций: ", k)
print_separator()

x_res, f_res, k = chord_method(a, b, epsilon, func, func_df1)
print("Метод хорд")
print("Найденное значение x: ", x_res)
print("Значение функции в точке: ", f_res)
print("Количество итераций: ", k)
print_separator()

x_res, f_res, k = newton_method(a, b, epsilon, func, func_df1, func_df2)
print("Метод Ньютона")
print("Найденное значение x: ", x_res)
print("Значение функции в точке: ", f_res)
print("Количество итераций: ", k)
