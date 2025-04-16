# where()
# syntax
# where(condition,expression1,expression2)
# from numpy import *
# a=array([2,8,13,17,9,16])
# b=array([1,9,12,6,15,10])
# c=where(b==a,b,a)
# print(a)
# print(b)
# print(c)

# using nonzero()method
# from numpy import *
# a=array([2,8,13,17,9,16])
# c=nonzero(a)
# print(a)
# print(c)
# print(type(c))

#view(it is also known as 'shallow copying)
#the change and modification effect o every array
# from numpy import *
# a=array([2,8,13,17,9,16])
# b=a.view()
# a[3] = 22
# print(a)
# print(b)

#copy()
# same as the view also make a copy of array but only difference is the element of array does not modifying in copy() method
# from numpy import *
# a=array([2,8,13,17,9,16])
# b=a.copy()
# b[0] = 33
# print(a)
# print(b)


#indexing
# from numpy import *
# a=array([2,8,0,17,9,16])
# print(a)
# i=0
# while(i<len(a)):
#     print(a[i])
#     i=i+1

#attributes of array
# (1)ndim 
# ndim diaplay which type of array we created 1 from one dimensional and 2 for multidimensional
# from numpy import *
# a=array([[2,8],[1,9]])
# print(a)
# print(a.ndim)
