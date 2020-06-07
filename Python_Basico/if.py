"""
If, elif e else
"""


# Condiciões logicas py
"""
igual a == b
n igual a != b
menor a < b
menor igual a <= b
maior a > b
maior a => b
"""


# IF simples 'se'
a = 10
b = 10
if a == b:
    print('\'a\' é igual a \'b\'')


# IF e elif 'se nao se'
if a < b:
    print('\'a\' é menor que \'b\'')
elif a == b:
    print('\'a\' é igual a \'b\'')


# else se senao
if a > b:
    print('\'a\' é maior que \'b\'')
elif a < b:
    print('\'a\' é menor que \'b\'')
else:
    print('\'a\' é igual a \'b\'')


# if curto
if a == b: print('\'a\' é igual a \'b\'')


# if e else curto
print('\'a\' é menor que \'b\'') if a < b else print('\'a\' é igual a \'b\'')


# 3 condicoes em uma linha
print(a) if a > b else print(b) if a < b else print('=')


# And operador logico para combinar condicoes
c = 10
if a == b and b == c:
    print('A é igual a b e b é igual a a entao a é igual a c')


# OR operador logico que precisa so de uma vdd
if a == b or b < c:
    print('Voce esta open')


# if alinhados
if a == b:
    if b == c:
        print('ok tudo igual')
    else:
        print('A algo de diferente')


# pass server para passar
if a == b:
    pass
