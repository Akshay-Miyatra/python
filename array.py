# import array 
# a=array.array('i',[2,3,4,5,6,7,8,9])
# print(a)

#2nd way
# import array as arr
# a=arr.array('i',[22,3,4,5,3,2,])
# print(a)

#3rd way
# from array import *
# a=array('i',[2,5,3,4])
# print(a)

#using for loop
from array import *
a=array('i',[3,4,5,6,7,8])
print(a)
no=len(a)
for i in range(no):
	print(a[i])

