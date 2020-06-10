from dml import db_delete, db_insert, db_update, db_select
from pprint import pprint

# db_insert('Allan', '19999390426', 'allanfera123@gmail.com')
# db_insert('Rafaela', '19999390426', 'rafalindinha@gmail.com')
# db_insert('Jose', '19999390426', 'joselimao@gmail.com')
# db_insert('Fernanda', '19999390426', 'fernandaspeedrun@gmail.com')


# db_delete('4')


pprint(db_select('phone_user', '19999390426'))
