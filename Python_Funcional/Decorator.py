"""

Decorator um metodo para envolver uma funçao
modificando seu comportamento

https://github.com/lord63/awesome-python-decorator

"""
from functools import wraps


def log(func):
    @wraps(func)
    def inner(*args):
        print(func.__name__, f'args: {args}')
        return func(*args)
    return inner


def validate_type(type):
    def validate(func):
        @wraps(func)
        def inner(*args):
            if all(isinstance(val, type) for val in args):
                return func(*args)

            else:
                raise Exception(f'Digite apenas {type}')

        return inner
    return validate


@validate_type(str)
@log
def soma(parcela_1, parcela_2):
    return parcela_1 + parcela_2
