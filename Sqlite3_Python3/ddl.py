"""

Aprendendo o basico da persitencia em python3
com sqlite3

DDL - Manipulação da tabela

"""

import sqlite3

# Crio e conecto uma base de dados
# CREATE db
con = sqlite3.connect('base.db')

# Cria um cursor que vai navegar dentro do banco
cur = con.cursor()


# CREATE table
sql_query = """
CREATE TABLE users (
    id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name_user TEXT NOT NULL,
    phone_user TEXT NOT NULL,
    email_user TEXT NOT NULL UNIQUE
)
"""

# CUrsor recebe a query
cur.execute(sql_query)

# AQui executa o commit do que esta no cursor
con.commit()

# Aqui eu fecho a conexão
con.close()
