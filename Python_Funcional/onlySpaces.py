"""

Retorna quantos epaços ha na string

"""


def onlySpace(frase: str) -> int:

    contador = 0

    for char in frase:
        if char == ' ':
            contador += 1

    return contador


def onlySpace_2(frase: str) -> int:
    return len(list(filter(lambda char: char == ' ', frase)))


def onlySpace_3(frase: str) -> int:
    return len([char for char in frase if char == ' '])


if __name__ == '__main__':

    frase = 'Hoje eh quinta feira'

    print(onlySpace_3(frase))
