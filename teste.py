import datetime

import MySQLdb
from datetime import date

conn = MySQLdb.connect(user='root',
                       passwd='root',
                       db='nodis_devops_test',
                       host='127.0.0.1',
                       port=3306)

cursor = conn.cursor()

cursor.execute('INSERT INTO product (title, sku, price, created, last_updated)'
               'VALUES (%s, %s, %s, %s, %s)', ('teste','teste',0.3, datetime.datetime.now(), datetime.datetime.now()))

conn.commit()