"""

Recebe uma lista de numeros e retorna apenas os valores pares

"""


def onlyPair(list_numers):

    list_pair = []

    for number in list_numers:

        if number % 2 == 0:
            list_pair.append(number)

    return list_pair


def onlyPair_2(list_numers):
    return list(filter(lambda number: number % 2 == 0, list_numers))


def onlyPair_3(list_numers):
    return [number for number in list_numers if number % 2 == 0]


if __name__ == '__main__':

    print(onlyPair(range(0, 50)))
    print(onlyPair_2(range(0, 50)))
    print(onlyPair_3(range(0, 50)))
