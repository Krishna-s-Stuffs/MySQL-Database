# CIMS_CREATE_DATABASE.PY

import mysql.connector as sql 
mycon=sql.connect(host='', user='', passwd='')
if mycon.is_connected():
  print("Successfully Connected")
cursor=mycon.cursor()
cursor.execute("create database cims")
print("Database created")
mycon.close()