"""
Casting Entre tipos de variaveis
"""


"""
int()
float()
str()
"""


# --------------Casting para inteiro
a = '3'  # string
b = 3.0  # float

# Printando os tipos
print(type(a))
print(type(b))

# Casting
int_a = int(a)
int_b = int(b)


# Printando os tipos
print(type(int_a))
print(type(int_b))


# --------------Casting para float
a = '3'  # string
b = 3  # int

# Printando os tipos
print(type(a))
print(type(b))

# Casting
float_b = float(b)
float_a = float(a)


# Printando os tipos
print(type(float_a))
print(type(float_b))


# --------------Casting para string
a = 3  # int
b = 3.0  # float

# Printando os tipos
print(type(a))
print(type(b))

# Casting
str_a = str(a)
str_b = str(b)


# Printando os tipos
print(type(str_a))
print(type(str_b))
