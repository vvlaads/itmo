import numpy as np
import sympy as sp
from src.util.modes import MethodMode

MAX_COUNT_OF_ITERATION = 100


def get_method_by_mode(mode):
    methods = {
        MethodMode.CHORD_METHOD: chord_method,
        MethodMode.SECANT_METHOD: secant_method,
        MethodMode.SIMPLE_ITERATION_METHOD: simple_iteration_method,
        MethodMode.NEWTON_METHOD: newton_method,
    }
    return methods.get(mode)


def chord_method(a, b, funcs, epsilon):
    func = funcs[0]
    number_of_iteration = 0
    x = 0
    for k in range(1, MAX_COUNT_OF_ITERATION):
        number_of_iteration = k
        x = a - func(a) * (b - a) / (func(b) - func(a))
        if abs(func(x)) <= epsilon:
            break
        if func(x) * func(b) < 0:
            a = x
        else:
            b = x
    return x, func(x), number_of_iteration


def secant_method(a, b, funcs, epsilon):
    number_of_iteration = 0

    func = funcs[0]
    x_symbol = sp.symbols('x')
    func_df1 = sp.diff(funcs[1], x_symbol)
    func_df2 = sp.diff(func_df1, x_symbol)

    if func(a) * func_df2.subs(x_symbol, a) > 0:
        x_old = a
        x = a + (2 * epsilon)
    else:
        x_old = b
        x = b - (2 * epsilon)

    for k in range(1, MAX_COUNT_OF_ITERATION):
        number_of_iteration = k
        x_next = x - func(x) * (x - x_old) / (func(x) - func(x_old))
        if abs(x_next - x) <= epsilon or abs(func(x_next)) <= epsilon:
            x = x_next
            break
        x_old = x
        x = x_next
    return x, func(x), number_of_iteration


def simple_iteration_method(a, b, funcs, epsilon):
    number_of_iteration = 0
    func = funcs[0]
    phi = funcs[2]

    x_symbol = sp.symbols('x')
    func_df1 = sp.diff(funcs[1], x_symbol)
    func_df2 = sp.diff(func_df1, x_symbol)

    section = np.linspace(a, b, 100)
    max_func_df1 = 0
    for element in section:
        value = abs(func_df1.subs(x_symbol, element))
        if value > max_func_df1:
            max_func_df1 = value

    if func_df1.subs(x_symbol, a).evalf() > 0:
        lam = - 1 / max_func_df1
    else:
        lam = 1 / max_func_df1

    print("Лямбда: ", lam)
    phi_df1 = sp.diff(funcs[3].subs('lam', lam), x_symbol)

    max_phi_df1 = 0
    for element in section:
        value = abs(phi_df1.subs(x_symbol, element).evalf())
        if value > max_phi_df1:
            max_phi_df1 = value

    if max_phi_df1 >= 1:
        print("Не выполнено условие сходимости")

    if func_df2.subs(x_symbol, a).evalf() * func(a) > 0:
        x_old = a
    else:
        x_old = b
    x = x_old

    for k in range(1, MAX_COUNT_OF_ITERATION):
        number_of_iteration = k
        x = phi(x_old, lam)
        if abs(x - x_old) < epsilon and abs(func(x)) < epsilon:
            break
        x_old = x
    return x, func(x), number_of_iteration


def newton_method(funcs, x0, y0, epsilon):
    number_of_iteration = 0
    func_1 = funcs[0]
    func_2 = funcs[2]

    x_symbol, y_symbol = sp.symbols('x y')

    func_1_dfx = sp.diff(funcs[1], x_symbol)
    func_1_dfy = sp.diff(funcs[1], y_symbol)

    func_2_dfx = sp.diff(funcs[3], x_symbol)
    func_2_dfy = sp.diff(funcs[3], y_symbol)

    delta_x, delta_y = 1, 1
    x, y = x0, y0

    for k in range(1, MAX_COUNT_OF_ITERATION):
        number_of_iteration = k

        jacobian = np.array([
            [func_1_dfx.subs({x_symbol: x, y_symbol: y}).evalf(), func_1_dfy.subs({x_symbol: x, y_symbol: y}).evalf()],
            [func_2_dfx.subs({x_symbol: x, y_symbol: y}).evalf(), func_2_dfy.subs({x_symbol: x, y_symbol: y}).evalf()]
        ], dtype=np.float64)

        right_part = np.array([-func_1(x, y), -func_2(x, y)])

        delta_x, delta_y = np.linalg.solve(jacobian, right_part)

        x += delta_x
        y += delta_y

        if abs(delta_x) < epsilon and abs(delta_y) < epsilon:
            print(func_1(x, y), func_2(x, y))
            break

    return x, y, number_of_iteration, delta_x, delta_y
