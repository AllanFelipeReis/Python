"""
Conjuntos
"""


# Iniciando um set
set_simples = {'Allan', 'Reis', 'Rafaela', 'Campos'}
print(set_simples)


# Acessando itens, como n tem index voce precisa iterar
for itens in set_simples:
    print(itens)


# Verficando existencia
print('Allan' in set_simples)
print('Allan' not in set_simples)


# Adicionando itens
set_simples.add('Fernanda')
print(set_simples)


# Adicionando varios itens
set_simples.update(['Jose', 'Lima', 'Reis'])
print(set_simples)


# Pegando o tamnanho da set
print(len(set_simples))


# Removendo item (Obs: Se o iten nao existir vai lançar excessao)
set_simples.remove('Allan')
print(set_simples)


"""
Removendo item usando discard('') (obs: se o item nao exister
nao vai lancar excessao)
"""
set_simples.discard('Rafaela')
print(set_simples)


"""
Tambem é possivel excluir um item usando o metodo pop(), mas o metodo
Remove o ultimo item e como set nao ha ordem voce nao sabe que item
sera excluido, porem o metodo retorrna o item excluido
"""
item_removido = set_simples.pop()
print(item_removido)


# O metodo clear apaga todos os item do set
set_simples.clear()
print(set_simples)


# O metodo DEL apaga a variavel
del set_simples
# print(set_simples)  # retorrna um erro pois a variavel nao é definida


# Join entre sets
set_x = {'Allan', 'Reis'}
set_y = {'Rafaela', 'Campos'}

set_resultado = set_x.union(set_y)
print(set_resultado)


# Outra forma de fazer um join é uasndo o update
set_x.update(set_y)
print(set_x)


# Criando um set com o construtor
set_construtor = set(('Allan', 'Reis', 'Dolly', 'Arroz'))
print(set_construtor)
