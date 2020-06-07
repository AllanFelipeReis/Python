'''
Boleanos
'''


# Retornam booleanos
print(10 > 9)  # == True
print(10 == 9)  # == False
print(10 < 9)  # == False


# Len maior que 0 retornam true
a = 'Allan Reis'
print(bool(a))  # == True


class allan(object):
    def __len__(self):
        return 0


reis = allan()
print(bool(reis))  # == False


"""
 isintance() retorna True para a variavel do tipo especificado e
 False para o contrario
"""

print(isinstance(a, str))  # == True
