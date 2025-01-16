from math import sqrt
from math import log
import matplotlib.pyplot as plt
from tabulate import tabulate


def var_series(array):
    var_array = sorted(array.copy())
    print("Вариационный ряд:", *var_array, "\n")
    return var_array


def extreme_values(sorted_array):
    extr_min = sorted_array[0]
    extr_max = sorted_array[len(sorted_array) - 1]
    print("Экстремальные значения:", extr_min, extr_max, "\n")
    return extr_min, extr_max


def scope(sorted_array):
    extr_min = sorted_array[0]
    extr_max = sorted_array[len(sorted_array) - 1]
    res = extr_max - extr_min
    print("Размах:", res, "\n")
    return res


def empirical_func(x, sorted_array):
    count = 0
    for i in range(len(sorted_array)):
        if sorted_array[i] < x:
            count += 1
    return count / len(sorted_array)


def build_empirical_func(sorted_array):
    x_array = sorted_array.copy()
    y_array = []
    for x in x_array:
        y_array.append(empirical_func(x, x_array))
    fig, ax = plt.subplots()
    ax.step(x_array, y_array, marker=".")
    ax.set_title("Эмпирическая функция")
    ax.set(xlim=(-2, 2), ylim=(0, 1), xlabel="Значения с.в.", ylabel="F(x)")
    plt.grid()


def print_empirical_func(sorted_array):
    dictionary = {}
    print("Аналитический вид функции:")
    count = 0
    for i in range(len(sorted_array)):
        count += 1
        dictionary[sorted_array[i]] = empirical_func(sorted_array[i], sorted_array)
        if count == 1:
            print("При x <", sorted_array[i], "функция принимает значение", dictionary.get(sorted_array[i]))
        else:
            print("При ", sorted_array[i - 1], "<= x < ", sorted_array[i], "функция принимает значение",
                  dictionary.get(sorted_array[i]))
    print("При x >= ", sorted_array[len(sorted_array) - 1], "функция принимает значение 1\n")


def build_statistical_series(array):
    dictionary = {}
    n = len(array)
    for x in array:
        if dictionary.get(x) is None:
            dictionary[x] = 1 / n
        else:
            dictionary[x] += 1 / n
    print("Статистический ряд:")
    print(tabulate(dictionary.items(), tablefmt="grid", headers=("x", "p")))
    return dictionary


def sample_average(dictionary):
    x = 0
    for key in dictionary.keys():
        x += dictionary.get(key) * key
    print("Выборочное среднее:", x, "\n")
    return x


def sample_variance(dictionary, s_average):
    variance = 0
    for key in dictionary.keys():
        variance += (key - s_average) ** 2 * dictionary.get(key)
    print("Выборочная дисперсия:", variance, "\n")
    return variance


def sample_msd(s_variance):
    msd = sqrt(s_variance)
    print("Выборочное СКО:", msd, "\n")
    return msd


def correct_sample_variance(array, s_variance):
    n = len(array)
    correct_variance = (n * s_variance) / (n - 1)
    print("Исправленная выборочная дисперсия:", correct_variance, "\n")
    return correct_variance


def correct_sample_msd(correct_s_variance):
    correct_msd = sqrt(correct_s_variance)
    print("Исправленное выборочное СКО:", correct_msd, "\n")
    return correct_msd


def fashion(dictionary):
    frequency = max(dictionary.values())
    for key in dictionary.keys():
        if dictionary.get(key) == frequency:
            print("Мода:", key, "\n")
            return key


def median(sorted_array):
    length = len(sorted_array)
    if length % 2 == 0:
        med = (sorted_array[length // 2 - 1] + sorted_array[length // 2]) / 2
    else:
        med = sorted_array[length // 2]
    print("Медиана:", med, "\n")
    return med


def math_expectation(array):
    n = len(array)
    math_exp = 0
    for x in array:
        math_exp += x
    math_exp /= n
    print("Оценка м.о.:", math_exp, "\n")
    return math_exp


def sturgess_formula(sorted_array):
    n = len(sorted_array)
    min_x = sorted_array[0]
    max_x = sorted_array[n - 1]
    m = int(1 + log(n, 2))
    h = (max_x - min_x) / m
    return h, m + 1


def interval_series(sorted_array, h, m):
    start_x = sorted_array[0] - (h / 2)
    end_x = start_x + h
    print("Интервальный ряд:")
    for i in range(m):
        count = 0
        for x in sorted_array:
            if start_x <= x < end_x:
                count += 1
        print("[", float('{:.3f}'.format(start_x)), ",", float('{:.3f}'.format(end_x)), ")", "частота:", count)
        start_x = end_x
        end_x += h


def interval_histogram(sorted_array, h, m):
    start_x = sorted_array[0] - (h / 2)
    end_x = start_x + h
    x_array = []
    y_array = []
    for i in range(m):
        count = 0
        for x in sorted_array:
            if start_x <= x < end_x:
                count += 1
        x_array.append("[" + str(float('{:.3f}'.format(start_x))) + ", " + str(float('{:.3f}'.format(end_x))) + ")")
        y_array.append(count)
        start_x = end_x
        end_x += h
    fig, ax = plt.subplots()
    ax.set_title("Гистограмма")
    plt.bar(x_array, y_array)


def polygon(sorted_array, h, m):
    start_x = sorted_array[0] - (h / 2)
    end_x = start_x + h
    x_array = []
    y_array = []
    for i in range(m):
        count = 0
        for x in sorted_array:
            if start_x <= x < end_x:
                count += 1
        x_array.append(start_x + h / 2)
        y_array.append(count)
        start_x = end_x
        end_x += h
    fig, ax = plt.subplots()
    ax.set_title("Полигон выборки")
    plt.plot(x_array, y_array, marker='.')
    plt.grid()
