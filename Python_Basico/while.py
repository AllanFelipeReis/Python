"""
While continua enquanto a condicao for verdadeira
"""


# Whilw simples
i = 0
while i < 5:
    print(i)
    i += 1


# Break para parada forçada no while
i = 0
while i < 5:
    if i == 3:
        print('Fim')
        break
    print(i)
    i += 1


# Continue para pular para a proxima iteracao
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# Else para quando a condicao nao for verdade
while i < 6:
    print(i)
    i += 1
else:
    print('i não é menor que seis')
