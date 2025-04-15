from enum import Enum


# Виды ввода данных
class InputMode(Enum):
    CONSOLE = 0,
    FILE = 1


# Виды вывода данных
class OutputMode(Enum):
    CONSOLE = 0,
    FILE = 1


# Опции для ввода данных
def get_options_to_input():
    return [(InputMode.CONSOLE, "1. Ввод через консоль"), (InputMode.FILE, "2. Ввод через файл")]


# Опции для вывода данных
def get_options_to_output():
    return [(OutputMode.CONSOLE, "1. Вывод в консоль"), (OutputMode.FILE, "2. Вывод в файл")]
