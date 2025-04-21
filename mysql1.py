#unit 4
#database connection with mysql
# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# print(mydb)

#creating the databse
# import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABase mypy')
# print("databse created successfully")

#list of database
# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
#     print(i)

#create the table
# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='mypy'
# )
# mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE STUD(ENR INT,NAME VARCHAR(20))')
# print("table created")

#insert record
 