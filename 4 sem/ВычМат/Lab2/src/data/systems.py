from math import sin, cos, tan
from src.util.modes import SystemMode
import sympy as sp


def get_funcs_system_by_mode(mode):
    funcs_system = {
        SystemMode.FIRST_SYSTEM: (func_1_system_1, func_1_system_1_symbol(), func_2_system_1, func_2_system_1_symbol()),
        SystemMode.SECOND_SYSTEM: (func_1_system_2, func_1_system_2_symbol(), func_2_system_2, func_2_system_2_symbol())
    }
    return funcs_system.get(mode)


def func_1_system_1(x, y):
    return sin(x + 0.5) - y - 1


def func_1_system_1_symbol():
    x, y = sp.symbols('x y')
    return sp.sin(x + 0.5) - y - 1


def func_2_system_1(x, y):
    return cos(y - 2) + x


def func_2_system_1_symbol():
    x, y = sp.symbols('x y')
    return sp.cos(y - 2) + x


def system_1_to_string():
    result = "Система:" + "\n"
    result += "sin(x + 0.5) - y = 1" + "\n"
    result += "cos(y - 2) + x = 0"
    return result


def func_1_system_2(x, y):
    return tan(x * y) - x ** 2


def func_1_system_2_symbol():
    x, y = sp.symbols('x y')
    return sp.tan(x * y) - x ** 2


def func_2_system_2(x, y):
    return 0.5 * x ** 2 + 2 * y ** 2 - 1


def func_2_system_2_symbol():
    x, y = sp.symbols('x y')
    return 0.5 * x ** 2 + 2 * y ** 2 - 1


def system_2_to_string():
    result = "Система:" + "\n"
    result += "tg(xy) = x^2" + "\n"
    result += "0.5x^2 + 2y^2 = 1"
    return result
