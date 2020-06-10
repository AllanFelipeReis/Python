"""

Recursão pode ser interessante, mas pode trazer problemas para a
performance

"""
from functools import reduce, lru_cache


@lru_cache()
def factorial(number):
    if number == 0:
        return 1

    else:
        return number * factorial(number-1)


print(reduce(lambda x, y: x * y, range(1, 11)))

print(factorial(10))
