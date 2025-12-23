# CIMS_CREATE_DATABASE.PY

import mysql.connector as sql 
try:
  mycon=sql.connect(host='localhost', user='root', passwd='manager')
  if mycon.is_connected():
    print("Successfully Connected")
    cursor=mycon.cursor()
except:
  print("Wrong Credentials! Please enter correct Credentials.")
  exit(0)
  
cursor.execute("create database cims")
print("Database created")
mycon.close()