#working with string
# string1='India'
# print(string1)
# print(type(string1))
# charractor= string1[0]
# print(charractor)
# charractor=string1[4]
# print(charractor)
# charractor = string1[0:3]
# print(charractor)

#check the type of a charactor
# string1 = input('enter a charactor : ')
# charctor =string1[0]
# if charctor.isalpha():
#     print('you are enter the alphabhet')
#     if charctor.isupper():
#         print('the charcter is an upper case')
#     else:
#         print('the charcter is an lower case')
# else:
#     print('you enter digit whether special symbol')

#working with list
# list1= range(11)
# for i in list1:
#     print(i,end='')

# list1=range(10)
# for i in list1:
#     print(i,end='')

# list1 = range(11,16)
# for i in list1:
#     print(i,end=' ')

#update the value of list using append()
# list1=[1,2,3,4,5,6,7,8]
# list1.append(11) #append are used to add a element at the end of list

#update the specfic loaction
# list1[6] = 60


#deleteting the value 
# list1.remove(60)
# print(list1)

# list1.remove(1)
# print(list1)

#deletinf the value by index
# del list1[0] #del are used to delete the specific index
# print(list1)

#finding the length of string
# a=len(list1)
# print(a)

#deleting the all element 
# list1.clear()
# print(list1)

#display a list with all reverse element
# list1 = ['rajkot','gujarat','india']
# list1.reverse()
# print(list1)

#concate th two string
# list1 = ['gujarat','maharastra','madhya pradesh']
# list2 = ['gandhinager','mumbai','bhopal']
# print(list1 + list2)

# printing the same list many times
# list1 = ['gujarat','maharastra','madhya pradesh']
# print(list1*5)

#membership 
#use of in and not in
# list1 = [1,2,3,4,5,6,7,8,9,10]
# n1= 1
# # n2 = 30
# print(n1 in list1 )
#we can alieas the list
# list1 = [10,20,30,40,50]
# print(list1)
# list2=list1
# print(list2)
# list2[3]=100
# print(list1)
# print(list2)

#clone the list
# from ast import alias
# from itertools import count
# from turtle import clone


# list1 = [10,20,30,40,50]
# list2 = list1[:]
# print(list1)
# print(list2)
# list2[3] = 100
# print(list1)
# print(list2)

#clone and alieas same as the copy and view
# th difference betwwen a alieas and opy is the alias do the chages in both but clone chnage only one

# list1 = []
# num = int(input('how many element you want to enter'))
# for i in range(num):
#     print('enter the element',end=' ')
#     list1.append(int(input()))
# to_find=int(input('which element do you want to find'))
# print(list1)
# count=0
# for i in list1:
#     if(to_find==i):
#         count=count + 1
# print('{} is found {} times'.format(to_find,count))

#working with nestede list,accesing the element
# list1 = [10,20,30,40,[1,2,3,4,]]
# print(list1)
# for i in list1[0:4]:
#     print(i)
# for i in list1[4]:
#     print(i)


