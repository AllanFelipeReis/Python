"""

Aplicar a função matematica: 3n**2 + 2/n + 1 em uma lista e retorna o resultado

"""


def funcMath(lista_numeros: list) -> float:
    resultados = []

    for valor in lista_numeros:
        resposta = ((3 * (valor ** 2)) + (2 / valor) + 1)
        resultados.append(round(resposta, 2))

    return resultados


def funcMath_2(lista_numeros: list) -> float:
    return list(map(lambda valor: round(((3 * (valor ** 2)) + (2 / valor) + 1),
                                        2), lista_numeros))


def funcMath_3(lista_numeros: list) -> float:
    return [round(((3 * (valor ** 2)) + (2 / valor) + 1), 2)
            for valor in lista_numeros]


if __name__ == '__main__':

    lista_numeros = [1, 2, 3, 4, 5]

    print(funcMath_3(lista_numeros))
