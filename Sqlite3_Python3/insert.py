"""

Inserindo dados na tabela

"""

import sqlite3


def db_insert(name, phone, email):
    return """
    INSERT INTO users(name_user, phone_user, email_user)
    VALUES('{}', '{}', '{}')
    """.format(name, phone, email)


con = sqlite3.connect('base.db')

cur = con.cursor()

# sql_query = """
#     INSERT INTO users(name_user, phone_user, email_user)
#         VALUES('Allan', 19999390426, 'allanreis@gmail.com'),
#             ('Felipe', 19993890629, 'felipereis@gmail.com')
# """

# cur.execute(sql_query)

cur.execute(db_insert('Pereira', '1999490425', 'Pereira.lima@gmail.com'))

con.commit()

con.close()
