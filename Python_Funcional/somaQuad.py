"""

Somar os Quadrados de x e y

"""


# Preocupado com a saida do terminal, mas só deveria ser a func
def soma_quadrados(x: int, y: int) -> int:

    x_quadrado = x ** 2
    y_quadrado = y ** 2

    return print(f'{x_quadrado} + {y_quadrado} = {x_quadrado + y_quadrado}')


# Func mais funcional
def soma_quadrados_func(x: int, y: int) -> int: return x ** 2 + y ** 2


if __name__ == '__main__':

    lista_valores_de_x = [2, 4, 6, 8, 10]
    lista_valores_de_y = [1, 3, 5, 7, 9]

    for x in lista_valores_de_x:
        for y in lista_valores_de_y:

            soma_quadrados(x, y)

            print(soma_quadrados_func(x, y))
