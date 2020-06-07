'''
List -- Collections
'''


# Create List
lista_simples = ['Allan', 'Reis', 'Rafaela', 'Campos']


# Print List
print(lista_simples)


# Acessando itens
print(lista_simples[1])  # == 'Reis'


# Negativo index
print(lista_simples[-1])  # == 'Campos'


# Range de index
print(lista_simples[0:3])  # == 'Allan', 'Reis', 'Rafaela'


# Do inicio ate a parada
print(lista_simples[:2])  # == 'Allan', 'Reis'


# Do item selecionado como inicial ate o final
print(lista_simples[1:])  # == 'Reis', 'Rafaela', 'Campos'


# Trocando o valor do item
lista_simples[3] = 'Reis'
print(lista_simples)


# Loop na lista criada
for index in lista_simples:
    print(index)


# Verificando existencia de item na lista
if 'Allan' in lista_simples:
    print('O Allan esta convidado')


# Tamanho da lista
print(len(lista_simples))


# Adicionando item append()
lista_simples.append('Fernada')
print(lista_simples)


# Inserindo itens em qualque lugar da lista insert()
lista_simples.insert(3, 'Amora')
print(lista_simples)


# Removendo item da lista remove()
lista_simples.remove('Amora')
print(lista_simples)


# Remover o ultimo item da lista pop()
lista_simples.pop()
print(lista_simples)


# Remover o item de determinado index del
del lista_simples[0]
print(lista_simples)


# Deletar Lista del
del lista_simples


# Removendo todos itens da lista clear()
lista_simples = ['Allan', 'Reis', 'Sidoka', 'Chapado']
print(lista_simples)

lista_simples.clear()
print(lista_simples)


# Copiando a lista copy()
lista_simples = ['Allan', 'Reis', 'Sidoka', 'Chapado']
print('Lista Simples {}'.format(lista_simples))

lista_copia = lista_simples.copy()
print('Lista Copia {}'.format(lista_copia))


# Copiando a lista list()
lista_copia_list = list(lista_simples)
print('Lista Copia usando list(): {}'.format(lista_copia_list))


# Mesclando duas listas
lista_simples_2 = ['Pizza', 'Hamburguer', 'Coxinha']
print(lista_simples_2)

lista_mesclada = lista_simples + lista_simples_2
print(lista_mesclada)


# Mesclando duas listas utilizando append e loop
for index in lista_simples_2:
    lista_simples.append(index)
print(lista_simples)


# Mesclando duas listas utilizando o extend()
lista_simples_2.extend(lista_simples)
print(lista_simples_2)


# Criando uma lista usando o construtor
lista_simples = list(('Allan', 'Felipe', 'Pereira', 'Lima', 'Reis'))
print(lista_simples)
