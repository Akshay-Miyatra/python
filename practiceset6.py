#1
# with open("simple.txt", "w") as file:
#     user_data = input("Enter the data you want to store: ")
#     file.write(user_data)
# print("Data successfully saved to simple.txt")

#2
# f=open('simple.txt',"r")
# b=f.read()
# print(b)

#3
# with open("simple.txt",'w') as file:
#     user_data = input("Enter the data")
#     file.write(user_data)
# print("data succesfully stored")


#4
# import os
# file_name = input("Enter the file name: ")
# if os.path.exists(file_name):
#     with open(file_name, "r") as file:
#         print(file.read())
# else:
#     print("The file does not exist.")


#5
import os,sys
file_name = input('Enetr the file name')
if os.path.isfile(file_name):
    with open(file_name,'r') as file:
       new = file.read()
       charcter = len(new)
       print("the number of charcter",charcter)

       words =len(new.split())
       print("the number of words",words)

       lines = new.count("\n") + 1 
       print('the number of lines in the file is',lines)




