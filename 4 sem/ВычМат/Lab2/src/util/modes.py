from enum import Enum


class MethodMode(Enum):
    CHORD_METHOD = 1,
    SECANT_METHOD = 2,
    SIMPLE_ITERATION_METHOD = 3,
    NEWTON_METHOD = 4


class FuncMode(Enum):
    FIRST_FUNC = 1,
    SECOND_FUNC = 2,
    THIRD_FUNC = 3,
    FOURTH_FUNC = 4,
    FIFTH_FUNC = 5


class SystemMode(Enum):
    FIRST_SYSTEM = 1,
    SECOND_SYSTEM = 2


class InputMode(Enum):
    FILE = 1,
    CONSOLE = 2


class OutputMode(Enum):
    FILE = 1,
    SCREEN = 2
