import pandas_xlsx_test as pd
import sqlite3
from PyQt5.QtSql import *

# db_connect = QSqlDatabase.addDatabase("QSQLITE")
# db_connect.setDatabaseName("avito_sql.db")
# db_connect.open()
# query = QSqlQuery()
# query.exec_('select * from Offers')
# query.first()
#
# df = pd.DataFrame(columns=['id','title','price'])
#
# i = 0
# while query.next():
#     rec = query.record()
#     df.at[i, 'id'] = rec.value('id')
#     df.at[i, 'title'] = rec.value('title')
#     df.at[i, 'price'] = rec.value('price')
#     i += 1
# print(df)


# con = sqlite3.connect('avito_sql.db')
# cursor = con.cursor()
# cursor.execute('select id, title, price from Offers')
# res = cursor.fetchall()
# columnHeaders = ['id','title','price']
# df = pd.DataFrame(columns=columnHeaders, data=res)
# print(df)
#
# df.to_excel('test.xlsx', index=False)
# df.to_html('test.html', index=False)

df = pd.read_excel('data/test.xlsx')