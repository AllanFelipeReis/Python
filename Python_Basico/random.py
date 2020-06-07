"""
Random
"""

import random

lista_simples = list(('Allan', 'Felipe', 'Pereira', 'Lima', 'Reis'))
print(lista_simples)
# random.shuffle(lista_simples)
print(random.choices(lista_simples, weights=[0.5, 0.1, 0.1, 0.2, 0.1], k=100))
# print(lista_simples)

print(random.randint(a=1, b=10))
