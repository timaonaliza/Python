#https://github.com/sanpingz/mysql-connector
import mysql.connector

config = {
  'user': 'wwe',
  'password': 'wwe',
  'host': '127.0.0.1',
  'database': 'servidor',
  #'raise_on_warnings': True,
  #'use_pure': False,
}

qry = "INSERT INTO `clientes`(`nome`) VALUES ('jao zim da silvha')"
cnx = mysql.connector.connect(**config)
cur = cnx.cursor()
cur.execute(qry)
cnx.close()