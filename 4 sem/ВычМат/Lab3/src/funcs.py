from math import sin, log
import sympy as sp


def func_1(x):
    return x ** 3 - 3 * x ** 2 + 7 * x - 10


def func_2(x):
    return -x ** 3 - x ** 2 - 2 * x + 1


def func_3(x):
    return sin(x ** 2) - log(x) + 5 * x


def func_4(x):
    return log(x) - x ** 2


def func_5(x):
    return 1 / x


def get_func_by_id(number):
    funcs = [func_1, func_2, func_3, func_4, func_5]
    return funcs[number - 1]


def get_all_funcs():
    return [
        (1, "x^3 - 3x^2 + 7x - 10"),
        (2, "-x^3 - x^2 - 2x + 1"),
        (3, "sin(x^2) - ln(x) + 5x"),
        (4, "ln(x) - x^2"),
        (5, "1/x")
    ]


def get_primitive_by_id(number):
    primitives = [primitive_1, primitive_2, primitive_3, primitive_4, primitive_5]
    return primitives[number - 1]


def primitive_1(value):
    x = sp.symbols('x')
    primitive = sp.integrate(x ** 3 - 3 * x ** 2 + 7 * x - 10, x)
    return primitive.subs(x, value).evalf()


def primitive_2(value):
    x = sp.symbols('x')
    primitive = sp.integrate(-x ** 3 - x ** 2 - 2 * x + 1, x)
    return primitive.subs(x, value).evalf()


def primitive_3(value):
    x = sp.symbols('x')
    primitive = sp.integrate(sp.sin(x ** 2) - sp.log(x) + 5 * x, x)
    return primitive.subs(x, value).evalf()


def primitive_4(value):
    x = sp.symbols('x')
    primitive = sp.integrate(sp.log(x) - x ** 2, x)
    return primitive.subs(x, value).evalf()


def primitive_5(value):
    x = sp.symbols('x')
    primitive = sp.integrate(1 / x, x)
    return primitive.subs(x, value).evalf()
