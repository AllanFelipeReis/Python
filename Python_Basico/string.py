"""
String
"""

# Assign String
a = 'Allan Reis'


# Print a
print(a)


# Frases
b = '''
    Allan Reis
    O mais Brabo
    DokaLanguage
    '''

# Print Frase
print(b)


# String sao listas
print(a[1])  # == 'l'


# Range da frase usando slice
print(a[1:3])  # == 'll'


# Negative index
print(a[-3:-1])  # == 'ei'


# String Lenth len()
print(len(a))


# Remover espaços no começo e no final da frase strip()
a_com_espaco = ' Allan Reis '


# Print sem strip()
print(a_com_espaco)


# Print com strip()
print(a_com_espaco.strip())


# Transforma a string em lower case lower()
print(a.lower())


# Transforma a strinf em upper case uper()
print(a.upper())


# Substitui letra na strifg replace()
print(a.replace('n', 'm'))


# Divide a frase em palavras split()
print(b.split('\n'))


# Checando se ha na String
print('Re' in a)


# O contrario
print('Re' not in a)


# Concantenado
print(a + b)


# Concantenado com espaços ou pulando linha
print(a + "\n" + b)


# Format
txt = 'Meu nome é {}'
print(txt.format(a))


# Escape caracter
txt = 'Allan \'Reis\' Tudo certo'
print(txt)
