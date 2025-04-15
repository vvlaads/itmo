# Проверка на целое число
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# Проверка на число с плавающей точкой
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Проверка, что число находится в указанных границах
def between(value, start, end):
    return start <= value <= end


# Проверка, что массив упорядочен по возрастанию
def check_inc_array(array):
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            return False
    return True
