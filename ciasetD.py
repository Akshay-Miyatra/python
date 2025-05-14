#1
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print("Simple Interest is:", interest)

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years): "))

si = calculate_simple_interest(p, r, t)

#2
import numpy as np
array1 = np.array([1,2,3,4,5])
new_array = array1.view()

new_array[0] = 10
print(new_array)
print(array1)

#3
water = int(input('how much water you want in liters'))

if(water<=90):
    bill_amount = 0
    print("Water is free Rs 0")
elif(water>90 and water<=150):
    bill_amount = (water - 90) * 2
    print('bill amount',bill_amount)
elif(water>150 and water<=250):
     bill_amount = (60 * 2) + (water - 150) * 5 #here we write 60 beacuse a difference between a 90-150 is 60
     print('bill amount',bill_amount)
elif(water>250):
    bill_amount = (60 * 2) + (water - 250) * 10

    print('bill amount',bill_amount)
else:
    print('please enter valid info')

#4
import re
a = "1 2 33 34 hello"
result  = re.findall(r'\b\d\b',a)
print(result)

a= "1hello how are you 2wowww"
result = re.findall(r'\b\d\w+',a)
print(result)

#5
f = open('atmiyauni.txt','a+')
f.write('the wrost university i have seen')

b =f.read()
print(b)
f.close()

#6
import os,sys
a = input("Enter the file name")
if os.path.isfile(a):
    f = open(a, 'r')
    str = f.read()
    print(str)
    f.close()
else:
    print("does not open a file")
    sys.exit()

#7
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Book2.csv")
print(df)
x = df['year']
y = df['admission']
plt.bar(x,y)
plt.show()







