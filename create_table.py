# CIMS_CREATE_TABLES.PY

import mysql.connector as sql 
mycon=sql.connect(host='localhost', user='', passwd='', database='cims')
if mycon.is_connected():
  print("Successfully Connected")
cursor=mycon.cursor()
cursor.execute('create table candidate_details(adm_no int primary key, candidate_name varchar(50), course varchar(20))')
print("Table created")