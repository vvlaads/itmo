import cmath
import math


def custom_sqrt(z):
    r = abs(z)  # Модуль числа
    theta = cmath.phase(z)  # Аргумент числа
    if theta < 0:
        theta += 2 * math.pi  # Переводим аргумент в [0, 2pi)
    return cmath.rect(math.sqrt(r), theta / 2)
