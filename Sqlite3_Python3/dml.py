"""

Inserindo dados na tabela

"""

import sqlite3


def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator


@commit_close
def db_insert(name, phone, email):
    return """
    INSERT INTO users(name_user, phone_user, email_user)
        VALUES('{}', '{}', '{}')
    """.format(name, phone, email)


@commit_close
def db_update(name, email):
    return """
    UPDATE users SET name_user = '{}' WHERE id_user = '{}'
    """.format(name, email)


@commit_close
def db_delete(id):
    return """
    DELETE FROM users WHERE id_user='{}'
    """.format(id)


def db_select(field, data):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    sql = """
    SELECT *
    FROM users
    WHERE {} = {}
    """.format(field, data)
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data


# con = sqlite3.connect('base.db')
# cur = con.cursor()
# sql_query = """
#     INSERT INTO users(name_user, phone_user, email_user)
#         VALUES('Allan', 19999390426, 'allanreis@gmail.com'),
#             ('Felipe', 19993890629, 'felipereis@gmail.com')
# """
# cur.execute(sql_query)
# cur.execute(db_insert('Pereira', '1999490425', 'Pereira.lima@gmail.com'))
# cur.execute(db_update('Fernando', '2'))
# cur.execute(db_delete('2'))
# cur.execute(db_select('id_user', '1'))
# con.commit()
# con.close()
