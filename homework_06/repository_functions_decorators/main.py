from pprint import pprint

from operator import pow
from time import time
from functools import wraps


def pow_list(*args, power=2) -> list:
    """Return list of powered numbers
    :param power: power value (int)
    """
    arr = []
    power_list = []
    for i in args:
        try:
            arr.append(int(i))
        except ValueError:
            print(i, ' is not an integer, missed')
    for _ in range(len(arr)):
        power_list.append(power)
    result_list = list(map(pow, arr, power_list))
    return result_list


def pow_list_input(power=2) -> list:
    """Return list of powered numbers from user input
    :param power: power value (int)
    """

    while True:
        try:
            n = int(input('Give a number of integers: '))
            break
        except ValueError:
            print('Give an integer please!')

    arr = []
    while n > 0:
        try:
            arr.append(int(input('Give an integer: ')))
            n -= 1
        except ValueError:
            print('Give an integer please!')

    result_list = [pow(i, power) for i in arr]
    return result_list

# *****************************************************************


EVEN = 'even'
ODD = 'odd'
PRIME = 'prime'


def runtime_checker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        finish_time = time()
        print('computed in ', finish_time - start_time)
        return res
    return wrapper


@runtime_checker
def int_filter(*args, filter_key=None) -> list:
    """
    Takes list of integers and only returns even/odd/prime in accordance of filter_key parameter
    :param filter_key: available values: 'even', 'odd' and 'prime'
    """
    if filter_key.lower() == EVEN:
        # using filter and lambla
        answer = list(filter(lambda x: (x % 2) != 1, args))
    elif filter_key.lower() == ODD:
        # using list comprehension
        answer = [x for x in args if (x % 2) == 1]
    elif filter_key.lower() == PRIME:
        answer = list(filter(is_prime, args))
    else:
        answer = []
        print(f'Wrong filter_key parameter! You need to chose between {EVEN}, {ODD}, and {PRIME}.')
    return answer


def is_prime(num: int) -> bool:
    """ Checks whether a given number is prime or not
    :param num: (int)
    """
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Iterate from 2 to n
    for i in range(2, num):
        # If num is divisible by any number between 2 and n, it is not prime
        if (num % i) == 0:
            return False
    else:
        return True

#     *******************************************************************


def trace(ind: str):
    """
    Trace calls made to the decorated function.
    """
    def decorator(func):
        lvl_count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal lvl_count
            print(f'{ind*lvl_count} --> {func.__name__}({args[0]})')
            lvl_count += 1
            res = func(*args, **kwargs)
            lvl_count -= 1
            print(f'{ind*lvl_count} <-- {func.__name__}({args[0]}) == {res}')

            return res

        return wrapper
    return decorator


@trace("____")
def fib(x):
    """Return fibonacci of x, where x is a non-negative int"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


if __name__ == '__main__':
    pprint(pow_list(1, 2, 3, 7, power=3))
    # pow_list_input(3)
    pprint(int_filter(1, 3, 2, 4, 2, 3, 5, 7, 11, filter_key='even'))
    pprint(is_prime(3))
    fib(3)
