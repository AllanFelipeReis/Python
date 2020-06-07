"""

Adciona Sr no inicio dos nomes

"""


def addSr(lista_nomes: list) -> list:

    for indice in range(len(lista_nomes)):

        lista_nomes[indice] = 'Sr. ' + lista_nomes[indice]

    return lista_nomes


def addSr_2(lista_nomes: list) -> list:
    return list(map(lambda nome: 'Sr. ' + nome, lista_nomes))


def addSr_3(lista_nomes: list) -> list:
    return ['Sr. ' + nome for nome in lista_nomes]


if __name__ == '__main__':

    lista_nomes = ['Allan', 'Felipe', 'Jose', 'Luan']

    # print(adiconaSr(lista_nomes))
    print(addSr_3(lista_nomes))
