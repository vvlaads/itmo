from math import sin, log
import sympy as sp
from src.util.modes import FuncMode


def get_funcs_by_mode(mode):
    funcs = {
        FuncMode.FIRST_FUNC: (func_1, func_1_symbol(), phi_1, phi_1_symbol()),
        FuncMode.SECOND_FUNC: (func_2, func_2_symbol(), phi_2, phi_2_symbol()),
        FuncMode.THIRD_FUNC: (func_3, func_3_symbol(), phi_3, phi_3_symbol()),
        FuncMode.FOURTH_FUNC: (func_4, func_4_symbol(), phi_4, phi_4_symbol()),
        FuncMode.FIFTH_FUNC: (func_5, func_5_symbol(), phi_5, phi_5_symbol())
    }
    return funcs.get(mode)


def func_1(x):
    return x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458


def func_1_symbol():
    x = sp.symbols('x')
    return x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458


def phi_1(x, lam):
    return x + (x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458) * lam


def phi_1_symbol():
    x = sp.symbols('x')
    lam = sp.symbols('lam')
    return x + (x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458) * lam


def func_1_to_string():
    return "x^3 - 3.125x^2 - 3.5x + 2.458"


def func_2(x):
    return x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907


def func_2_symbol():
    x = sp.symbols('x')
    return x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907


def phi_2(x, lam):
    return x + (x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907) * lam


def phi_2_symbol():
    x = sp.symbols('x')
    lam = sp.symbols('lam')
    return x + (x ** 3 + 2.28 * x ** 2 - 1.934 * x - 3.907) * lam


def func_2_to_string():
    return "x^3 + 2.28x^2 - 1.934x - 3.907"


def func_3(x):
    return 2 * x ** 3 - 1.89 * x ** 2 - 5 * x + 2.34


def func_3_symbol():
    x = sp.symbols('x')
    return 2 * x ** 3 - 1.89 * x ** 2 - 5 * x + 2.34


def phi_3(x, lam):
    return x + (2 * x ** 3 - 1.89 * x ** 2 - 5 * x + 2.34) * lam


def phi_3_symbol():
    x = sp.symbols('x')
    lam = sp.symbols('lam')
    return x + (2 * x ** 3 - 1.89 * x ** 2 - 5 * x + 2.34) * lam


def func_3_to_string():
    return "2x^3 - 1.89x^2 - 5x + 2.34"


def func_4(x):
    return sin(x) - x / 2


def func_4_symbol():
    x = sp.symbols('x')
    return sp.sin(x) - x / 2


def phi_4(x, lam):
    return x + (sin(x) - x / 2) * lam


def phi_4_symbol():
    x = sp.symbols('x')
    lam = sp.symbols('lam')
    return x + (sp.sin(x) - x / 2) * lam


def func_4_to_string():
    return "sin(x) - x / 2"


def func_5(x):
    return log(x) - x ** 2 + 1


def func_5_symbol():
    x = sp.symbols('x')
    return sp.log(x) - x ** 2 + 1


def phi_5(x, lam):
    return x + (log(x) - x ** 2 + 1) * lam


def phi_5_symbol():
    x = sp.symbols('x')
    lam = sp.symbols('lam')
    return x + (sp.log(x) - x ** 2 + 1) * lam


def func_5_to_string():
    return "ln(x) - x^2 + 1"
