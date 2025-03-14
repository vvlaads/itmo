# Метод половинного деления
def half_division_method(a, b, epsilon, func):
    count_of_iteration = 0
    for k in range(1, 1000):
        count_of_iteration = k
        x1 = (a + b - epsilon) / 2
        x2 = (a + b + epsilon) / 2
        y1 = func(x1)
        y2 = func(x2)
        if y1 > y2:
            a = x1
        else:
            b = x2

        if b - a <= 2 * epsilon:
            break
    xm = (a + b) / 2
    ym = func(xm)
    return xm, ym, count_of_iteration


# Метод золотого сечения
def golden_ratio_method(a, b, epsilon, func):
    count_of_iteration = 0
    x1 = a + 0.382 * (b - a)
    x2 = b + 0.618 * (b - a)
    y1 = func(x1)
    y2 = func(x2)
    for k in range(1, 1000):
        count_of_iteration = k
        if y1 < y2:
            b = x2
            x2 = x1
            x1 = a + 0.382 * (x2 - a)
            y2 = y1
            y1 = func(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + 0.618 * (b - x1)
            y1 = y2
            y2 = func(x2)
        if (b - a) < epsilon:
            break
    return x1, y1, count_of_iteration


# Метод хорд
def chord_method(a, b, epsilon, func, func_df1):
    count_of_iteration = 0
    x = a - func_df1(a) / (func_df1(a) - func_df1(b)) * (a - b)
    for k in range(1, 1000):
        count_of_iteration = k
        f_df = func_df1(x)
        if abs(f_df) <= epsilon:
            break
        if f_df > 0:
            b = x
            x = a - func_df1(a) / (func_df1(a) - f_df) * (a - b)
        else:
            a = x
            x = a - f_df / (f_df - func_df1(b)) * (a - b)
    return x, func(x), count_of_iteration


# Метод Ньютона
def newton_method(a, b, epsilon, func, func_df1, func_df2):
    count_of_iteration = 0
    x_old = a
    x = b
    for k in range(1, 1000):
        count_of_iteration = k
        x = x_old - func_df1(x_old) / func_df2(x_old)
        if abs(func_df1(x_old)) <= epsilon:
            break
        x_old = x
    return x, func(x), count_of_iteration
