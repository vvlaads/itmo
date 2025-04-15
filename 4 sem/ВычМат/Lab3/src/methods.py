MAX_COUNT_OF_ITERATION = 20


def is_defined(func, x):
    try:
        func(x)
        return True
    except (ValueError, ZeroDivisionError):
        return False


def fix_limits(func, a, b, epsilon):
    delta = epsilon
    if is_defined(func, a) and is_defined(func, b):
        return a, b
    while a <= b:
        if not is_defined(func, a):
            a += delta
        if not is_defined(func, b):
            b -= delta
        if is_defined(func, a) and is_defined(func, b):
            print("Изменены пределы интегрирования:")
            print("Нижний предел:", a)
            print("Верхний предел:", b)
            return a, b
    print("Ошибка вычисления функции на выбранном интервале")
    exit(1)


def rectangle_method_left(a, b, func, epsilon):
    n = 4
    a, b = fix_limits(func, a, b, epsilon)
    h = (b - a) / n
    int_sum = 0
    x_i = a
    for i in range(n):
        int_sum += func(x_i)
        x_i += h
    int_sum *= h

    for repeat in range(MAX_COUNT_OF_ITERATION):
        n *= 2
        h = (b - a) / n
        int_sum2 = 0
        x_i = a
        for i in range(n):
            int_sum2 += func(x_i)
            x_i += h
        int_sum2 *= h
        if abs(int_sum2 - int_sum) < epsilon:
            break
        int_sum = int_sum2
    return int_sum, n


def rectangle_method_right(a, b, func, epsilon):
    n = 4
    a, b = fix_limits(func, a, b, epsilon)
    h = (b - a) / n
    int_sum = 0
    x_i = a
    for i in range(n):
        x_i += h
        int_sum += func(x_i)
    int_sum *= h

    for repeat in range(MAX_COUNT_OF_ITERATION):
        n *= 2
        h = (b - a) / n
        int_sum2 = 0
        x_i = a
        for i in range(n):
            x_i += h
            int_sum2 += func(x_i)
        int_sum2 *= h
        if abs(int_sum2 - int_sum) < epsilon:
            break
        int_sum = int_sum2
    return int_sum, n


def rectangle_method_center(a, b, func, epsilon):
    n = 4
    a, b = fix_limits(func, a, b, epsilon)
    h = (b - a) / n
    int_sum = 0
    x_i = a
    for i in range(n):
        x_i += h / 2
        int_sum += func(x_i)
        x_i += h / 2
    int_sum *= h

    for repeat in range(MAX_COUNT_OF_ITERATION):
        n *= 2
        h = (b - a) / n
        int_sum2 = 0
        x_i = a
        for i in range(n):
            x_i += h / 2
            int_sum2 += func(x_i)
            x_i += h / 2
        int_sum2 *= h
        if abs(int_sum2 - int_sum) < epsilon:
            break
        int_sum = int_sum2
    return int_sum, n


def trapezoid_method(a, b, func, epsilon):
    n = 4
    a, b = fix_limits(func, a, b, epsilon)
    h = (b - a) / n
    int_sum = (func(a) + func(b)) / 2
    x_i = a
    for i in range(n - 1):
        x_i += h
        int_sum += func(x_i)
    int_sum *= h

    for repeat in range(MAX_COUNT_OF_ITERATION):
        n *= 2
        h = (b - a) / n
        int_sum2 = (func(a) + func(b)) / 2
        x_i = a
        for i in range(n - 1):
            x_i += h
            int_sum2 += func(x_i)
        int_sum2 *= h
        if abs(int_sum2 - int_sum) < epsilon:
            break
        int_sum = int_sum2
    return int_sum, n


def simpson_method(a, b, func, epsilon):
    n = 4
    a, b = fix_limits(func, a, b, epsilon)
    h = (b - a) / n
    int_sum = func(a) + func(b)
    part1 = 0
    part2 = 0
    x_i = a
    for i in range(n - 1):
        x_i += h
        if i % 2 == 0:
            part1 += func(x_i)
        else:
            part2 += func(x_i)
    int_sum = h / 3 * (int_sum + 4 * part1 + 2 * part2)

    for repeat in range(MAX_COUNT_OF_ITERATION):
        n *= 2
        h = (b - a) / n
        int_sum2 = func(a) + func(b)
        part1 = 0
        part2 = 0
        x_i = a
        for i in range(n - 1):
            x_i += h
            if i % 2 == 0:
                part1 += func(x_i)
            else:
                part2 += func(x_i)
        int_sum2 = h / 3 * (int_sum2 + 4 * part1 + 2 * part2)
        if abs(int_sum2 - int_sum) < epsilon:
            break
        int_sum = int_sum2
    return int_sum, n


def get_method_by_id(number):
    methods = [rectangle_method_left, rectangle_method_right, rectangle_method_center, trapezoid_method, simpson_method]
    return methods[number - 1]


def get_all_methods():
    return [
        (1, "Метод прямоугольников (левый)"),
        (2, "Метод прямоугольников (правый)"),
        (3, "Метод прямоугольников (средний)"),
        (4, "Метод Трапеций"),
        (5, "Метод Симпсона")
    ]
