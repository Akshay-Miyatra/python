#databse

#create databse
# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
# )
# mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')
# print('database created')

#create table
# import mysql.connector
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mypy"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE student(rn INT , name VARCHAR(255))")
# print('table created')

#insert record
# import mysql.connector
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mypy"
# )
# mycursor = mydb.cursor()

# insert_query = "insert into student(rn,name) values (%s,%s)"
# new = [(1,'abc'),(2,'xyz'),(3,'aaa')]
# mycursor.executemany(insert_query,new)
# mydb.commit()
# print('record inserted')

#select 

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mypy"
# )
# mycursor = mydb.cursor()
# select_query = "SELECT * FROM student"
# mycursor.execute(select_query)
# for i in mycursor:
#     print(i)

#select particular record
# import mysql.connector
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mypy"
# )
# mycursor = mydb.cursor()
# select_query = "SELECT * FROM student WHERE rn = 1"
# mycursor.execute(select_query)
# for i in mycursor:
#     print(i)

#update
# import mysql.connector
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mypy"
# )
# mycursor = mydb.cursor()
# update_query = "UPDATE student SET name = 'bbb' WHERE rn = 1"
# mycursor.execute(update_query)
# mydb.commit()
# print('record updated')

#delete
# import mysql.connector
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password="",
#     database = 'mypy'
# )
# mycursor = mydb.cursor()
# delete_query = "DELETE FROM student WHERE rn = 1"
# mycursor.execute(delete_query)
# mydb.commit()
# print('record deleted')

#sqllite

import sqlite3
#connect to database
conn = sqlite3.connect('mydata.db')
#cursor object
# cur = conn.cursor()
# cur.execute('Create table student(rn INTEGER, name varchar)')
# print('table created')

#insert record
# cur = conn.cursor()
# cur.execute('''
#         insert into student(rn,name) values(1,'abc'),(2,'xyz'),(3,'aaa')
# ''')
# conn.commit()
# print('record inserted')

#selct record
# cur = conn.cursor()
# cur.execute('SELECT * FROM student')
# new = cur.fetchall()
# for i in new:
#     print(i)


#update the record
# cur = conn.cursor()
# update_query = "UPDATE student SET name = 'bbb' WHERE rn = 1"
# cur.execute(update_query)
# conn.commit()
# print('record updated')

#delete the record
# cur = conn.cursor()
# delete_query = "DELETE FROM student WHERE rn = 1"
# cur.execute(delete_query)
# conn.commit()
# print('record deleted')


