import math


# Метод половинного деления для поиска минимума в одномерном случае
def half_division_method(a, b, epsilon, func):
    for k in range(1, 1000):
        x1 = (a + b - epsilon) / 2
        x2 = (a + b + epsilon) / 2
        if func(x1) > func(x2):
            a = x1
        else:
            b = x2

        if b - a <= 2 * epsilon:
            break
    return (a + b) / 2


# Метод покоординатного спуска
def coordinate_descent(func, x0, y0, epsilon):
    count_of_iteration = 0
    result = 0
    x_cur = x0
    y_cur = y0

    for n in range(1, 1000):
        count_of_iteration = n

        # Точка на k-ой итерации
        x_start = x_cur
        y_start = y_cur

        # Фиксируем значение y
        def f1(x):
            return func(x, y_cur)

        # Находим минимум по x
        a = x_cur - 5
        b = x_cur + 5
        x_cur = half_division_method(a, b, epsilon, f1)

        # Фиксируем значение x
        def f2(y):
            return func(x_cur, y)

        # Находим минимум по y
        a = y_cur - 5
        b = y_cur + 5
        y_cur = half_division_method(a, b, epsilon, f2)

        # Сравниваем значения функций в точках на k-ой итерации и на (k+1)-ой итерации
        if abs(func(x_cur, y_cur) - func(x_start, y_start)) <= epsilon:
            result = func(x_cur, y_cur)
            break

    return result, x_cur, y_cur, count_of_iteration


# Метод градиентного спуска
def gradient_descent(func, x0, y0, epsilon, f_dx, f_dy):
    count_of_iteration = 0
    result = 0
    alpha = 0.1  # Размер шага
    x_cur = x0
    y_cur = y0
    for n in range(1, 1000):
        count_of_iteration = n

        # Точка на k-ой итерации
        x_start = x_cur
        y_start = y_cur

        # Точка на (k+1)-ой итерации
        x_cur = x_start - alpha * f_dx(x_start, y_start)
        y_cur = y_start - alpha * f_dy(x_start, y_start)

        # Уменьшаем шаг, если значение функции больше предыдущего
        if func(x_cur, y_cur) > func(x_start, y_start):
            alpha /= 10

        # Сравниваем значения функций в точках на k-ой итерации и на (k+1)-ой итерации
        if abs(func(x_cur, y_cur) - func(x_start, y_start)) < epsilon:
            result = func(x_cur, y_cur)
            break

    return result, x_cur, y_cur, count_of_iteration


# Метод наискорейшего спуска
def fastest_descent(func, x0, y0, epsilon, f_dx, f_dy):
    count_of_iteration = 0
    result = 0
    x_cur = x0
    y_cur = y0
    for n in range(1, 1000):
        count_of_iteration = n

        # Находим частные производные
        f1 = f_dx(x_cur, y_cur)
        f2 = f_dy(x_cur, y_cur)

        # Выходим, если норма градиента достаточно мала
        norm = math.sqrt(f1 ** 2 + f2 ** 2)
        if norm < epsilon:
            result = func(x_cur, y_cur)
            break

        # Находим оптимальный шаг
        def h_func(value):
            return func(x_cur - value * f1, y_cur - value * f2)

        step = half_division_method(-10, 10, epsilon, h_func)

        x_cur -= step * f1
        y_cur -= step * f2
    return result, x_cur, y_cur, count_of_iteration
