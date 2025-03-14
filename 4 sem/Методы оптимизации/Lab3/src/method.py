# Метод квадратичной аппроксимации
def method(x1, delta_x, epsilon1, epsilon2, func):
    count_of_iteration = 0
    f1, f2, f3 = 0, 0, 0
    x2, x3 = 0, 0
    x_average, f_average = 0, 0
    skip = False
    for k in range(1, 1000):
        count_of_iteration = k
        if not skip:
            # Шаг 2
            x2 = x1 + delta_x
            # Шаг 3
            f1 = func(x1)
            f2 = func(x2)
            # Шаг 4
            if f1 > f2:
                x3 = x1 + 2 * delta_x
            else:
                x3 = x1 - delta_x
            # Шаг 5
            f3 = func(x3)

        # Шаг 6
        f_min = min(f1, f2, f3)
        if f_min == f1:
            x_min = x1
        elif f_min == f2:
            x_min = x2
        else:
            x_min = x3

        # Шаг 7
        denominator = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3
        if denominator == 0:
            x1 = x_min
            skip = False  # Перейти к шагу 2
            continue

        numerator = (x2 ** 2 - x3 ** 2) * f1 + (x3 ** 2 - x1 ** 2) * f2 + (x1 ** 2 - x2 ** 2) * f3
        x_average = 1 / 2 * (numerator / denominator)
        f_average = func(x_average)

        # Шаг 8
        if abs((f_min - f_average) / f_average) < epsilon1 and abs((x_min - x_average) / x_average) < epsilon2:
            break  # Конец
        elif x1 <= x_average <= x3:
            points = [x1, x2, x3, x_min, x_average]
            left_point = x1
            right_point = x3

            if f_min < f_average:
                small_point = x_min
            else:
                small_point = x_average

            for point in points:
                if left_point < point < small_point:
                    left_point = point
                if small_point < point < right_point:
                    right_point = point
            x1 = left_point
            x2 = small_point
            x3 = right_point
            f1 = func(x1)
            f2 = func(x2)
            f3 = func(x3)
            skip = True  # Перейти к шагу 6
            continue
        else:
            x1 = x_average
            skip = False  # Перейти к шагу 2
            continue

    return x_average, f_average, count_of_iteration
