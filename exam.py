# basic = float(input("Enter your basic salary"))

# ta = 0.04 * basic
# da = 0.30 * basic
# hra = 0.15 * basic

# tax = 0.03 * basic
# pf = 0.12 * basic

# net = basic + ta + da +hra -tax -pf
# print("Net salary =",net)

# Get marks for 5 subjects in one line
# marks = [float(i) for i in input("Enter marks of 5 subjects separated by space: ").split()]

# # Calculate total
# total = sum(marks)

# # Calculate percentage
# percentage = total / 5

# # Display results
# print("Total Marks:", total)
# print("Percentage:", percentage, "%")

# water = int(input("Enetr water in liter"))

# if water<=90:
#     print('water is freee')
# elif water>90 and water <= 150:
#     bill = (water - 90) * 2
#     print('your water is above 90 liter so bill is',bill)
# elif water >150 and water<=250:
#     bill = (water - 60) + (water - 150) *5

# def check(s):
#     vovel = 'aeiouAEIOU'
#     v = 0
#     c = 0
#     for ch in s:
#         if ch.isalpha():
#             if ch in vovel:
#                 v +=1
#             else:
#                 c += 1
#     print("voels",v)
#     print('con',c)
# x = input("Enter any string :")
# check(x)

# str1 = input("enter string")
# str1 =  str1.replace(" ","").lower()
# if str1 == str1[::-1]:
#     print("pelindrom")
# else:
#     print('not pelindrom')

# Array
# import array
# a = array.array('i',[1,2,3,4,5])
# print(a)

# 2nd way
# import array as ar
# a = ar.array('i',[1,2,3,4,5])
# print(a)

#3rd way
# from array import *
# a = array('i',[1,2,3])
# print(a)

# from array import *
# a = array('u',['a','b','c'])
# print(a)

# from array import *
# a = array('i',[1,2,3,4,5,6,7,8,9,10])
# n = len(a)
# for i in range(n):
#     print(a[i])

#array slicing
# from array import *
# a = array('i',[1,2,3,4,5,6,7,8,9,10])
# print(a)
# print(a[0])
# print(a[0:5])
# print(a[0:])
# print(a[-7])

# from array import *
# a = array('i',[1,2])
# a.append(3) #append at the last position
# a.insert(0,0) #insert at particular position
# a.insert(1,11) 
# a.remove(11) #remove a specific elemet
# a.pop() #rremove the last element of array
# b = a.index(0) #find the index of paricualr element
# a.reverse() #reverse the array last to top
# print(b)
# print(a)

#numpy

# import numpy
# a = numpy.array([1,2,3])
# print(a)

#string testing method

# a ="mynameisakshaymiyatra"
# b = a.isalpha() #return true if string conatin only alfabets
# b = a.isdigit() # retun true if all string member are digit
# b = a.isupper() #return true if the string are in uppercase
# b = a.islower() #return true if the all string are in lowercase
# print(b)

# list
# lst1 = ['akshay',10,20,30,'abc']
# print(lst1)
# #append the list
# lst1.append(11)
# print(lst1)

# #insert the vlue
# lst1.insert(0,'hi')
# print(lst1)

# #remove
# lst1.remove('hi')
# print(lst1)

# #deleting
# del lst1[0]
# print(lst1)

# #reverse the list
# lst1.reverse()
# print(lst1)

# #finding the index
# a = lst1.index(10)
# print(a)

# #concate two lsit
# lst2 = ['hiii',1,2,3]
# lst3 = (lst1 + lst2)
# print(lst3)

#dictionary
# dict1 = {1:'abc',2:'xyz',3:'aaa',4:'bbb'}
# print(dict1)

# #copy the dictionary
# dict2 = dict1.copy()
# print(dict2)

# #keys()
# dict = dict1.keys()
# print(dict)

# #values()
# values = dict1.values()
# print(values)

# #pop()
# pop = dict1.pop(1)
# print(pop)

# #popitem()
# popitem = dict1.popitem()
# print(popitem)

# #update()
# update = ({3:'bbb'})
# print(update)

#unit 5

# #dictionary to dataframe
import pandas as pd

student = {'rn':[1,2,3,4,5],'name':['aaa','vvv','bbb','ccc','ddd'],'city':['amreli','chalala','dhari','savar kundla','malila']}
df = pd.DataFrame(student)




