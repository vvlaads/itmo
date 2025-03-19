from src.data.functions import *
from src.data.systems import *
from src.util.modes import *


def get_method_choices_message():
    return "Выберите метод (введите 1, 2, 3 или 4):"


def get_func_choices_message():
    return "Выберите функцию (введите 1, 2, 3, 4 или 5):"


def get_system_choices_message():
    return "Выберите систему (введите 1 или 2):"


def get_input_choices_message():
    return "Выберите формат ввода (введите 1 или 2):"


def get_output_choices_message():
    return "Выберите формат вывода (введите 1 или 2):"


def get_method_choices():
    return {
        "1": ("Метод хорд (для нелинейных уравнений)", MethodMode.CHORD_METHOD),
        "2": ("Метод секущих (для нелинейных уравнений)", MethodMode.SECANT_METHOD),
        "3": ("Метод простой итерации (для нелинейных уравнений)", MethodMode.SIMPLE_ITERATION_METHOD),
        "4": ("Метод Ньютона (для систем нелинейных уравнений)", MethodMode.NEWTON_METHOD)
    }


def get_func_choices():
    return {
        "1": (func_1_to_string(), FuncMode.FIRST_FUNC),
        "2": (func_2_to_string(), FuncMode.SECOND_FUNC),
        "3": (func_3_to_string(), FuncMode.THIRD_FUNC),
        "4": (func_4_to_string(), FuncMode.FOURTH_FUNC),
        "5": (func_5_to_string(), FuncMode.FIFTH_FUNC)
    }


def get_system_choices():
    return {
        "1": (system_1_to_string(), SystemMode.FIRST_SYSTEM),
        "2": (system_2_to_string(), SystemMode.SECOND_SYSTEM),
    }


def get_input_choices():
    return {
        "1": ("Ввод с помощью файла", InputMode.FILE),
        "2": ("Ввод через консоль", InputMode.CONSOLE)
    }


def get_output_choices():
    return {
        "1": ("Вывод в файл", OutputMode.FILE),
        "2": ("Вывод на экран", OutputMode.SCREEN)
    }
