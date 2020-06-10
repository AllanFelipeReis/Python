"""

Uma funcão que retorna outra funcao

"""


def base(num):
    def expoente(x):
        return num ** x
    return expoente


print(base(2)(4))
