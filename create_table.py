# CIMS_CREATE_TABLES.PY

import mysql.connector as sql
try:
  mycon=sql.connect(host='localhost', user='krishna', passwd='kkp079', database='cims')
  if mycon.is_connected():
    print("Successfully Connected")
    cursor=mycon.cursor()
except:
  print("Wrong Credentials! Please enter correct Credentials.")
  exit(0)

cursor.execute('create table candidate_details(adm_no int primary key, candidate_name varchar(50), course varchar(20))')
print("Table created")