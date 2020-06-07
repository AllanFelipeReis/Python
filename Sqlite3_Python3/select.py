"""

Select

"""

import sqlite3

con = sqlite3.connect('base.db')

cur = con.cursor()

sql_query = """
    SELECT * FROM users
"""

cur.execute(sql_query)

print(cur.fetchone())

con.close()
