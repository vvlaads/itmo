from methods import *


def func(x, y):
    return 7 * x ** 2 + 3 * y ** 2 + 0.5 * x * y - 3 * x - 5 * y + 2


def func_dx(x, y):
    return 14 * x + 0.5 * y - 3


def func_dy(x, y):
    return 6 * y + 0.5 * x - 5


x0, y0 = 2, -2
epsilon = 0.0001

res_func, res_x, res_y, iterations = coordinate_descent(func, x0, y0, epsilon)
print("Метод покоординатного спуска")
print("Значение функции:", res_func)
print("Найденный вектор:", res_x, res_y)
print("Количество итераций:", iterations)
print("---- ---- ---- ---- ----")

res_func, res_x, res_y, iterations = gradient_descent(func, x0, y0, epsilon, func_dx, func_dy)
print("Метод градиентного спуска")
print("Значение функции:", res_func)
print("Найденный вектор:", res_x, res_y)
print("Количество итераций:", iterations)
print("---- ---- ---- ---- ----")

res_func, res_x, res_y, iterations = fastest_descent(func, x0, y0, epsilon, func_dx, func_dy)
print("Метод наискорейшего спуска")
print("Значение функции:", res_func)
print("Найденный вектор:", res_x, res_y)
print("Количество итераций:", iterations)
print("---- ---- ---- ---- ----")
