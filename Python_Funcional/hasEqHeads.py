"""

Verifica se as listas possuem o mesmo primeiro elemento

"""


def primeiro_elemento_igual(lista_1: list, lista_2: list) -> bool:
    return lista_1[0] == lista_2[0]


if __name__ == '__main__':

    lista_1 = [0, 1, 2, 3, 4]
    lista_2 = [5, 6, 7, 8, 9]
    lista_3 = [0, 2, 4, 6, 8]

    # entradas lista_1 e lista_2
    # saida esperada False
    print(primeiro_elemento_igual(lista_1, lista_2))

    # entradas lista_1 e lista_3
    # saida esperada True
    print(primeiro_elemento_igual(lista_1, lista_3))
