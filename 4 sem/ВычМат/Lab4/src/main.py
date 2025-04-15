from src.validators import *

from src.data import *
from src.funcs import *
import matplotlib.pyplot as plt


# Ввод целого числа
def input_int():
    while True:
        value = input()
        if is_int(value):
            return int(value)
        print("Введите целое число")


# Ввод числа с плавающей точкой
def input_float():
    while True:
        value = input()
        if is_float(value):
            return float(value)
        print("Введите число")


# Выбор пользователя одного из вариантов
def select(message, options):
    print(message)
    while True:
        for i in range(len(options)):
            print(options[i][1])
        value = input_int()
        for i in range(len(options)):
            if value == i + 1:
                return options[i][0]
        print("Не найдено такой опции, повторите попытку")


# Загрузить таблицу значений из файла
def load_file():
    print("Введите название файла")
    x_arr = []
    y_arr = []
    while True:
        filename = input()
        try:
            with open(filename, "r") as file:
                count = 0
                for line in file:
                    count += 1
                    if count > 12:
                        raise ValueError
                    row = line.split()
                    if not is_float(row[0]) or not is_float(row[1]):
                        raise ValueError
                    x_arr.append(float(row[0]))
                    y_arr.append(float(row[1]))
                if count < 8:
                    raise ValueError
                if check_inc_array(x_arr):
                    return x_arr, y_arr
                print("Значения x указаны в неверной последовательности")
        except (FileNotFoundError, PermissionError):
            print("Невозможно открыть файл:", filename)
        except ValueError:
            print("Некорректные данные в файле")
        print("Введите путь к файлу повторно")
        x_arr.clear()
        y_arr.clear()


# Сохранить полученные данные в файл
def save_file(x_arr, y_arr, descr, phi_arrays, epsilon_arrays):
    print("Введите название файла:")
    while True:
        filename = input()
        try:
            with open(filename, "w") as file:
                file.write("x: " + str(x_arr) + "\n")
                file.write("y: " + str(y_arr) + "\n")
                for i in range(len(descr)):
                    file.write("Функция: " + descr[i] + "\n")
                    file.write("phi: " + str(phi_arrays[i]) + "\n")
                    file.write("epsilon: " + str(epsilon_arrays[i]) + "\n")
            print("Файл успешно сохранён как", filename)
            return
        except (FileNotFoundError, PermissionError):
            print("Введите путь к файлу повторно:")


# Вывести полученные данные в консоль
def print_result(x_arr, y_arr, descr, phi_arrays, epsilon_arrays):
    print("x: ", *x_arr)
    print("y: ", *y_arr)
    for i in range(len(descr)):
        print_separator()
        print(descr[i])
        print("phi: ", *phi_arrays[i])
        print("epsilon: ", *epsilon_arrays[i])


# Ввод данных в массив
def input_array(message, size):
    print(message)
    arr = []
    for i in range(size):
        arr.append(input_float())
        print("Введено", i + 1, "из", size)
    return arr


# Ввод размера таблицы
def input_size():
    print("Введите количество точек (от 8 до 12)")
    while True:
        size = input_int()
        if between(size, 8, 12):
            return size
        print("Повторите ввод")


# Получить массив значений функций по массиву значений x
def array_from_func(x_arr, func):
    y_arr = []
    for i in range(len(x_arr)):
        y_arr.append(func(x_arr[i]))
    return y_arr


# Вывести коэффициент детерминации
def print_determination(value, descr):
    if value >= 0.95:
        print(f"Функция {descr} имеет высокую точность аппроксимации")
    elif value >= 0.75:
        print(f"Функция {descr} имеет удовлетворительную точность аппроксимации")
    elif value >= 0.5:
        print(f"Функция {descr} имеет слабую точность аппроксимации")
    else:
        print(f"Функция {descr} имеет недостаточную точность аппроксимации")
    print("Значение R^2:", value)


# Выбор функции с самым большим коэффициентом детерминации
def best_func(funcs, det_values):
    max_det = 0
    index = []
    funcs_arr = []
    for i in range(len(funcs)):
        if det_values[i] >= max_det:
            max_det = det_values[i]
    for i in range(len(funcs)):
        if det_values[i] == max_det:
            index.append(i)
    for i in range(len(funcs)):
        if i in index:
            funcs_arr.append(funcs[i])

    return funcs_arr, max_det


# Получение разности между значениями функций
def get_epsilon(y_arr, phi_arr, size):
    result = []
    for i in range(size):
        result.append(abs(y_arr[i] - phi_arr[i]))
    return result


# Вывод разделителя
def print_separator():
    print("---- ---- ---- ---- ---- ---- ----")


# === Основной код ===
# Ввод данных с возможностью выбора
input_mode = select("Выберите формат ввода данных (введите 1 или 2):", get_options_to_input())
if input_mode == InputMode.CONSOLE:
    n = input_size()
    x = input_array("Введите значения x:", n)
    while not check_inc_array(x):
        print("Неверная последовательность x")
        x = input_array("Введите значения x:", n)
    y = input_array("Введите значения y:", n)
else:
    x, y = load_file()
    n = len(x)

funcs_descr = []
det_arr = []
phis = []
epsilons = []

plt.plot(x, y, label="Исходная функция", color="blue")

# Аппроксимация линейной функцией
try:
    a, b, phi1, cor = linear_func(x, y, n)
    phi1_arr = array_from_func(x, phi1)
    phi1_descr = f'y = {a}x + {b}'
    det1 = determination(y, phi1_arr, n)
    print_determination(det1, phi1_descr)
    print("Коэффициент корреляции:", cor)
    print_separator()
    plt.plot(x, phi1_arr, linestyle="--", label=phi1_descr, color="red")

    funcs_descr.append(phi1_descr)
    det_arr.append(det1)
    phis.append(phi1_arr)
    epsilons.append(get_epsilon(y, phi1_arr, n))
except OverflowError:
    print("Переполнение при попытке аппроксимации")

# Аппроксимация полиномиальной функцией 2-й степени
try:
    a0, a1, a2, phi2 = polynomial_func2(x, y, n)
    phi2_arr = array_from_func(x, phi2)
    phi2_descr = f'y = {a0} + {a1}x + {a2}x^2'
    det2 = determination(y, phi2_arr, n)
    print_determination(det2, phi2_descr)
    print_separator()
    plt.plot(x, phi2_arr, linestyle="--", label=phi2_descr, color="green")

    funcs_descr.append(phi2_descr)
    det_arr.append(det2)
    phis.append(phi2_arr)
    epsilons.append(get_epsilon(y, phi2_arr, n))
except OverflowError:
    print("Переполнение при попытке аппроксимации")

# Аппроксимация полиномиальной функцией 3-й степени
try:
    b0, b1, b2, b3, phi3 = polynomial_func3(x, y, n)
    phi3_arr = array_from_func(x, phi3)
    phi3_descr = f'y = {b0} + {b1}x + {b2}x^2 + {b3}x^3'
    det3 = determination(y, phi3_arr, n)
    print_determination(det3, phi3_descr)
    print_separator()
    plt.plot(x, phi3_arr, linestyle="--", label=phi3_descr, color="orange")

    funcs_descr.append(phi3_descr)
    det_arr.append(det3)
    phis.append(phi3_arr)
    epsilons.append(get_epsilon(y, phi3_arr, n))
except OverflowError:
    print("Переполнение при попытке аппроксимации")

# Аппроксимация степенной функцией
try:
    c, d, phi4 = power_func(x, y, n)
    phi4_arr = array_from_func(x, phi4)
    phi4_descr = f'y = {c}x^{d}'
    det4 = determination(y, phi4_arr, n)
    print_determination(det4, phi4_descr)
    print_separator()
    plt.plot(x, phi4_arr, linestyle="--", label=phi4_descr, color="black")

    funcs_descr.append(phi4_descr)
    det_arr.append(det4)
    phis.append(phi4_arr)
    epsilons.append(get_epsilon(y, phi4_arr, n))
except ValueError:
    print("Нельзя аппроксимировать степенной функцией")
except OverflowError:
    print("Переполнение при попытке аппроксимации")

# Аппроксимация экспоненциальной функцией
try:
    e, f, phi5 = exponential_func(x, y, n)
    phi5_arr = array_from_func(x, phi5)
    phi5_descr = f'y = {e}e^{f}x'
    det5 = determination(y, phi5_arr, n)
    print_determination(det5, phi5_descr)
    print_separator()
    plt.plot(x, phi5_arr, linestyle="--", label=phi5_descr, color="brown")

    funcs_descr.append(phi5_descr)
    det_arr.append(det5)
    phis.append(phi5_arr)
    epsilons.append(get_epsilon(y, phi5_arr, n))
except ValueError:
    print("Нельзя аппроксимировать экспоненциальной функцией")
except OverflowError:
    print("Переполнение при попытке аппроксимации")

# Аппроксимация логарифмической функцией
try:
    g, h, phi6 = logarithmic_func(x, y, n)
    phi6_arr = array_from_func(x, phi6)
    phi6_descr = f'y = {g}ln(x) + {h}'
    det6 = determination(y, phi6_arr, n)
    print_determination(det6, phi6_descr)
    print_separator()
    plt.plot(x, phi6_arr, linestyle="--", label=phi6_descr, color="violet")

    funcs_descr.append(phi6_descr)
    det_arr.append(det6)
    phis.append(phi6_arr)
    epsilons.append(get_epsilon(y, phi6_arr, n))
except ValueError:
    print("Нельзя аппроксимировать экспоненциальной функцией")
except OverflowError:
    print("Переполнение при попытке аппроксимации")

# Вывод наиболее точных функций
print_separator()
best_func_descr_arr, best_det = best_func(funcs_descr, det_arr)
print("Наиболее точные функции:")
for function in best_func_descr_arr:
    print(function)
print("Значения коэффициента детерминации:", best_det)

# Вывод результатов с возможностью выбора
output_mode = select("Выберите формат вывода данных (введите 1 или 2):", get_options_to_output())
if output_mode == OutputMode.CONSOLE:
    print_result(x, y, funcs_descr, phis, epsilons)
else:
    save_file(x, y, funcs_descr, phis, epsilons)

# Отрисовка графиков
plt.legend()
plt.xlim(x[0], x[len(x) - 1])
plt.ylim(-50, 50)
plt.grid(True)
plt.show()
