"""
Tuple
"""

# Inicializando uma tuple
tupla = ('Allan', 'Reis', 'Rafaela', 'Campos')
print(tupla)


# Acessando itens da tupla
print(tupla[1])


# Acessando itens da tupla com index negativo
print(tupla[-1])


# Range tupla
print(tupla[:3])


# Casting tupla para lista
lista_simples = list(tupla)
print(lista_simples)


# Casting lista para tupla
tupla_simples = tuple(lista_simples)
print(tupla_simples)


# Mudando itens tupla
# tupla[1] = 'Fodas'  # Retorna um erro pois tuplas são imutaveis
# print(tupla)

"""
Diferença entre tuplas e listas são que listas são mutaveis e as tuplas não
"""

# Iterando em uma tupla
for itens in tupla:
    print(itens)


# Verificando a existencia de um item na tupla
print('Allan' in tupla)
print('Allan' not in tupla)


# Length de uma tuplas
print(len(tupla))


"""
Para adicionar uma tupla com apenas um item é necessario adcionar uma virgula
no final
"""
tupla_um_item = ('Allan',)
print(type(tupla_um_item))

nao_eh_uma_tupla = ('Allan')  # Nao eh uma tupla
print(type(nao_eh_uma_tupla))


"""
Nao eh possivel apagar um item de uma tupla, mas e possivel deletar uma tupla
"""
del tupla
# print(tupla)  # Retorna um erro


# Join entre tuplas
tupla_join = tupla_simples + tupla_um_item
print(tupla_join)


# Criando uma tupla com o construtor
tupla_construtor = tuple(('ALlan', 'Fodas', 'Froid', 'Sidoka'))
print(tupla_construtor)
