"""

Verifica se existe uma letra na palavra

"""

# print('c' in 'caio')


def charFound(char, string):

    for c in string:
        if c == char:
            return True

    return False


def charFound_2(char, string):
    return bool(list(filter(lambda c: c == char, string)))


def charFound_3(char, string):
    return bool([c for c in string if c == char])


if __name__ == '__main__':
    print(charFound('A', 'Allan'))
    print(charFound('a', 'Allan'))
    print(charFound('b', 'Allan'))

    print(charFound_2('A', 'Allan'))
    print(charFound_2('a', 'Allan'))
    print(charFound_2('b', 'Allan'))

    print(charFound_3('A', 'Allan'))
    print(charFound_3('a', 'Allan'))
    print(charFound_3('b', 'Allan'))
