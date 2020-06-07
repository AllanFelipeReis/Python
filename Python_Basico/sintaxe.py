"""
configurando atraves de comentarios na primeira linha do programa
# !/usr/bin/env python2
# -*-coding: latin1 -*-
"""


# Print imprime no terminal
print('Allan Reis')


# Linha quebrada por '/'
print('Hoje o clima\
ta tenso')


# Lista quebrada por virgula
lista = [1, 3, 4, 5, 5,
'a', 'd']


# Funcao dividida por virgula
a = range(1,
 100)


# Exemplo de função
def soma(x: int, y: int) -> int:
    return x + y


# Print da functon
print(soma(1, 5))


# Controle de fluxo
def validacao(valor: int):
    if isinstance(valor, int):
        return f'Realamente o {valor} é um inteiro'
    elif isinstance(valor, float):
        return f'Realmente o {valor} é um float'
    else:
        return 'Isso não é int irmao'


# Print da validacao
print(validacao(3))
print(validacao(3.9))


if soma(1, 3) > 2: print('Maior que dois')
