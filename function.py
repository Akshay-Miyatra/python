#syntax
# def name_of_function(parameter1,parameter2):
#     function statment

#add two values using function
# def display(roll,name):
#     print('the roll number is =',roll)
#     print('the name is =',name)
# #calling the function
# display(1,'abc')

#sum of two variable
# def sum(a,b):
#     total=a+b
#     print('the total of a and b',total)
# sum(2,3)

#returning the value from the function
# def sum(a,b):
#     total = a+b
#     return(total)
# #callnig the function
# x = sum(4,5)
# print('the total of given number is =',x)

#to check that number is odd or even
# def evenorodd(a):
#     if a%2==0:
#         print('the number is even')
#     else:
#         print('the number is odd')
# evenorodd(29)

#to check thqt enter number is positive ,negative or zero
# def pos_neg_zero(no):
#     if no>0:
#         print('the number is positive')
#     elif(no == 0):
#         print('the number is zero')
#     else:
#         print('the number is negative')
# # #calling the function
# n=int(input('enter the number'))
# pos_neg_zero(n)

#returning multiple values from a function
# from ast import arguments, keyword
# from email.policy import default
# from tkinter import Variable


# def arith(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div
# #calling the function
# x,y,z,p =arith(20,5)
# print('the addtion of two numbers',x)
# print('the substraction of two numbers',y)
# print('the multiplication of two numbers',z)
# print('the division of two numbers',p)

#pass by the object
#immtuable object: integer,string,float,tuple
#mutable object:list
#to pass an integer to a function and moify it.
# def modify(x):
#     x=25
#     print('the value of x inside the function is:',x,id(x))
# # calling the function
# x=52
# modify(x)
# print('the value of x outside the function is',x,id(x))

#formal and actual arguments
# def sum(a,b): -->formal argumant

#calling the function
# s=2,t=5 -->actual arguments

#there are four types of actual arguments
# 1) positional arguments
# 2) keyword arguments
# 3)default arguments
# 4)Variable length arguments

#1 postional arguments
# the number of arguments and their postions in the function defiantion shoul match exactly 
# with the number and postion of the argumnets in function call
# def combine(a,b):
#     c=a+b
#     print(c)
# #calling the function
# combine('atmiya','university')
# combine('university','atmiya')

#keyword argument
#keyword argument identify parame3ter by their names
#while callnig the function we have to give two values one is argument name and other is its value

# def info(roll,name):
#     print('student roll no is',roll)
#     print('student name is ',name)
# info(name='abc',roll='1')

#default argument

#it enalble to programmer to set the default argument in function
#at the time calling the function parameter not given then defualt paramter given
#if the value pass than value will take by function

# def info(roll,name='abc'):
#     print('the roll no is ',roll)
#     print('the name is ',name)
# info(1,) #or
# info(1)#both are same
# inf(1,'aaa')

#varibale lenght argument
#if the programmer is unaware about the argumemnt than we use variable length argument
#if two parameter is declared and we give three valuye than it will show error

# syntax
# def num_of fun(farg,*args)
# farg stand for formal argument 

def total(farg,*argv):
    sum=0
    for i in argv:
        sum=sum+i
    print('the total of all number is',(farg+sum))
#calling the function
total(10,10,10,10,10,10,10,10,10,10)
# total(10,2)

#anonymous funtion(lambda)
#while using the normal function we need to define a function and give name to it
# def name_of _function(a,b)

#while using the anonymous function there is no need of giving the name tp function
#def sqr(no):
    # return no*no
#finding the square of a number using lambda
sqr=lambda no:no*no
no=int(input('Ente the number'))
print('the square of given number is :',sqr(no))




    