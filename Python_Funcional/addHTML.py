"""

Adiciona HTML na palavra passada

"""


def addHTML(list_string):
    list_html = []

    for word in list_string:
        list_html.append(f'<h1>{word}</h1>')

    return list_html


def addHTML_2(list_string):
    return list(map(lambda word: f'<h1>{word}</h1>', list_string))


def addHTML_3(list_string):
    return [f'<h1>{word}</h1>' for word in list_string]


if __name__ == '__main__':

    list_test = ['Allan', 'Felipe', 'Pereira', 'Lima', 'Reis']

    print(addHTML(list_test))
    print(addHTML_2(list_test))
    print(addHTML_3(list_test))
