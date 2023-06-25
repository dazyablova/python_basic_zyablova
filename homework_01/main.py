"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    """
    Функция, которая проверяет, является ли число простым
    :param n: целое число
    :return: True, если число простое, иначе False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_numbers(numbers, filter_type):
    """
    Функция, которая фильтрует список чисел по заданному типу
    :param numbers: список целых чисел
    :param filter_type: тип фильтрации (ODD - нечётные, EVEN - чётные, PRIME - простые)
    :return: отфильтрованный список чисел
    """
    if filter_type == ODD:
        return [n for n in numbers if n % 2 != 0]
    elif filter_type == EVEN:
        return [n for n in numbers if n % 2 == 0]
    elif filter_type == PRIME:
        return [n for n in numbers if is_prime(n)]
    else:
        return []
