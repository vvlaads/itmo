import matplotlib.pyplot as plt
from src.util.validator import *
from src.util.methods import *
from src.data.choices import *


def select_one(message, choices):
    while True:
        print(message)
        for key, value in choices.items():
            print(f"{key}. {value[0]}")

        key = input()

        value = choices.get(key)
        if key in choices:
            return value[1]
        print("Ошибка выбора")


def open_file(mode):
    while True:
        print("Введите путь к файлу")
        filename = input()
        try:
            return open(filename, mode)
        except FileNotFoundError:
            print("Не найден файл " + filename)
        except PermissionError:
            print("Ошибка доступа " + filename)


def read_file(f):
    while True:
        start = f.readline()
        end = f.readline()
        e = f.readline()
        if not validate_float(start) or not validate_float(end) or not validate_float(e):
            print("Ошибка преобразования в число, выберите другой файл")
            f = open_file('r')
            continue
        start = float(start)
        end = float(end)
        e = float(e)
        if not validate_interval(start, end):
            print("Неверно определен интервал, выберите другой файл")
            f = open_file('r')
            continue
        return start, end, e


def input_float(message):
    while True:
        print(message)
        value = input()
        if validate_float(value):
            return float(value)
        print("Ошибка преобразования в число")


def input_interval():
    while True:
        start = input_float("Введите левую границу интервала")
        end = input_float("Введите правую границу интервала")
        if validate_interval(start, end):
            return start, end
        print("Неверно выбран интервал")


def input_start_approx():
    while True:
        print("Введите начальное приближение в формате: x0 y0")
        coordinates = input().split(" ")
        if len(coordinates) != 2:
            print("Неверно введено приближение")
            continue
        x0 = coordinates[0]
        y0 = coordinates[1]
        if validate_float(x0) and validate_float(y0):
            return float(x0), float(y0)
        print("Ошибка преобразования в число")


def check_condition(start, end, function):
    if not check_necessary_condition(start, end, function):
        print("Не выполнено необходимое условие")
    count_of_roots = check_count_of_roots(start, end, function)
    if count_of_roots == 0:
        print("Не найдено корней")
    elif count_of_roots > 1:
        print("Найдено более одного корня на интервале: " + str(count_of_roots))


def print_graph(start, end, function):
    try:
        function(start)
    except ValueError:
        start = 0.1
    array_x = np.linspace(start, end, 1000)
    x_values = []
    y_values = []
    for x_value in array_x:
        x_values.append(x_value)
        y_values.append(function(x_value))
    plt.plot(x_values, y_values)
    plt.grid(True)
    plt.show()


def add_dot(x_coord, y_coord):
    plt.scatter(x_coord, y_coord, color="red", s=50, zorder=2)


def print_graphs(start, end, function_1, function_2):
    array_x = np.linspace(start, end, 1000)
    array_y = np.linspace(start, end, 1000)
    x_1 = []
    y_1 = []
    x_2 = []
    y_2 = []

    for x_value in array_x:
        for y_value in array_y:
            if abs(function_1(x_value, y_value)) < 0.01:
                x_1.append(x_value)
                y_1.append(y_value)
            if abs(function_2(x_value, y_value)) < 0.01:
                x_2.append(x_value)
                y_2.append(y_value)

    plt.scatter(x_1, y_1, s=5)
    plt.scatter(x_2, y_2, s=5)
    plt.xlim(start, end)
    plt.ylim(start, end)
    plt.grid(True)
    plt.show()


method_mode = select_one(get_method_choices_message(), get_method_choices())
method = get_method_by_mode(method_mode)

if method_mode != MethodMode.NEWTON_METHOD:
    func_mode = select_one(get_func_choices_message(), get_func_choices())
    funcs = get_funcs_by_mode(func_mode)
    print_graph(-5, 5, funcs[0])
    input_mode = select_one(get_input_choices_message(), get_input_choices())

    if input_mode == InputMode.FILE:
        file = open_file('r')
        a, b, epsilon = read_file(file)
        file.close()
    else:
        a, b = input_interval()
        epsilon = input_float("Введите погрешность вычисления")

    check_condition(a, b, funcs[0])
    output_mode = select_one(get_output_choices_message(), get_output_choices())

    res1, res2, res3 = method(a, b, funcs, epsilon)
    result = "Найденное значение x: " + str(res1) + "\n"
    result += "Значение функции: " + str(res2) + "\n"
    result += "Номер итерации: " + str(res3) + "\n"

    if output_mode == OutputMode.SCREEN:
        print(result)
    else:
        file = open_file('w')
        file.write(result)
        file.close()
    add_dot(res1, res2)
    print_graph(a, b, funcs[0])

else:
    system_mode = select_one(get_system_choices_message(), get_system_choices())
    funcs = get_funcs_system_by_mode(system_mode)
    print_graphs(-10, 10, funcs[0], funcs[2])
    x_start, y_start = input_start_approx()
    epsilon = input_float("Введите погрешность вычисления")
    x, y, k, delta_x, delta_y = method(funcs, x_start, y_start, epsilon)

    result = "Найденный вектор: " + str(x) + " " + str(y) + "\n"
    result += "Количество итераций: " + str(k) + "\n"
    result += "Вектор погрешностей: " + str(delta_x) + " " + str(delta_y) + "\n"
    print(result)
    add_dot(x, y)
    print_graphs(x - 3, x + 3, funcs[0], funcs[2])
