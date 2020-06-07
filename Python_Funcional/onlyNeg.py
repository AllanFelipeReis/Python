"""

Recebe uma lista com numeros e retorna apenas os negativos

"""


def only_negatives(list_numbers):

    numbers_negatives = []

    for number in list_numbers:
        if number < 0:
            numbers_negatives.append(number)

    return numbers_negatives


def only_negatives_2(list_numbers):
    return list(filter(lambda number: number < 0, list_numbers))


def only_negatives_3(list_numbers):
    return [number for number in list_numbers if number < 0]


if __name__ == '__main__':

    list_test = [-1, 2, -3, 4, -5, 6, -7, 8, -9]

    print(only_negatives(list_test))
    print(only_negatives_2(list_test))
    print(only_negatives_3(list_test))
