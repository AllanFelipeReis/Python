"""
Dicionarios
"""


# Criando um dicionario
dict_simples = {
                'Nome': 'Allan',
                'Sobrenome': 'Reis',
                'Cargo': 'TI'
                }


# Acessando item
print(dict_simples['Nome'])


# Tambem é possivel acessar usando o metodo get()
print(dict_simples.get('Sobrenome'))


# Mudando valores
print(dict_simples['Cargo'])
dict_simples['Cargo'] = 'Programador'
print(dict_simples['Cargo'])


# Loop no dicionario printando os nomes das chaves
for itens in dict_simples:
    print(itens)


# Loop no dicionario printando os valores das chaves
for itens in dict_simples:
    print(dict_simples[itens])


# Loop no dicionario printando os valores usando o metodo value() das chaves
for itens in dict_simples.values():
    print(itens)


# Loop no dicionario printando os valores e as chaves
for chave, item in dict_simples.items():
    print(chave, item)


# Checando existencia dentro do dict
print('Nome' in dict_simples)


# tamanho da dict
print(len(dict_simples))


# Adicionando itens
dict_simples['Sexo'] = 'Masculino'
print(dict_simples)


# Removendo itens com a key especifica
dict_simples.pop('Sexo')
print(dict_simples)


# removendo itens aleatoriamente
dict_simples.popitem()
print(dict_simples)


# Utilizano o del para deletar um item especifico
del dict_simples['Nome']
print(dict_simples)


# Utilizando o del para excluir o dicionario inteiro
# del dict_simples
# print(dict_simples)  # Retorna erro pois o dicionario nao existe mais


# Apagando os itens da dict
dict_simples.clear()
print(dict_simples)


# Copiando um dicionario
new_dict_simples = dict_simples.copy()
print(new_dict_simples)


# Copiando uma dict usando o dict
new_dict_usando_dict = dict(dict_simples)
print(new_dict_simples)


# Criando dicionarios aninhados
minha_familia = {
    'Irma': {
        'Velha': {
            'Nome': 'Thais',
            'Idade': '21'
        },
        'Nova': {
            'Nome': 'Thayanny',
            'Idade': '17'
        }
    },
    'Pai': {
        'Nome': 'Jose',
        'Idade': '53'
    },
    'Mae': {
        'Nome': 'Fernanda',
        'Idade': '40'
    }
}
print(minha_familia)


# Ou voce pode sedimentar isso tudo
Velha = {
    'Nome': 'Thais',
    'Idade': '21'
}


Nova = {
    'Nome': 'Thayanny',
    'Idade': '17'
}


Pai = {
    'Nome': 'Jose',
    'Idade': '53'
}


Mae = {
    'Nome': 'Fernanda',
    'Idade': '40'
}

minha_familia_2 = {
    'Irma': {
        'Nova': Nova,
        'Velha': Velha
    },
    'Pai': Pai,
    'Mae': Mae
}
print(minha_familia_2)


# Criando um dicionario usando o construtor dict
dict_construtor = dict(Nome='Allan', Idade='19')
print(dict_construtor)
