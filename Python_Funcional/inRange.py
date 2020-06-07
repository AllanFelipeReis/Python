"""

Recebe uma lista de valores e retorna apenas os maiores que 1 e
menores que 100, inclusive ambos.

"""


def inRange(list_numbers):

    list_in_range = []

    for number in list_numbers:
        if number >= 1 and number <= 100:
            list_in_range.append(number)

    return list_in_range


def inRange_2(list_numbers):
    return list(
        filter(lambda number: number >= 1 and number <= 100, list_numbers))


def inRange_3(list_numbers):
    return [number for number in list_numbers if number >= 1 and number <= 100]


if __name__ == '__main__':
    print(inRange(range(-50, 50, 2)))
    print(inRange_2(range(-50, 50, 2)))
    print(inRange_3(range(-50, 50, 2)))
