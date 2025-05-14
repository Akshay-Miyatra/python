#1
a = input("Enter a string")
result = a.replace(" ","").lower()
if result == result[::-1]:
    print("Enter string is pelindrome")
else:
    print("Enter string is not a pelindrom")

#2
import numpy as np
array1 = np.array([10,20,30,40,50])
array2 = np.array([20,30,40,50,60])

for i in range(5):
    if array1[i] > array2[i]:
        print(array1[i],'array 1 is big')
    else:
        print(array2[i],'array two is big')

#3
import re
a = "hello howare aa aa aaa"
result = re.findall(r'\b\w{5,}\b',a)
print(result)

a = "india is the best country"
result = re.sub('india','bharat',a)
print(result)

#4
marks = float(input("Enter the student's marks: "))

if marks > 90:
    print("A1 grade")
elif marks > 80 and marks <= 90:
    print("A grade")
elif marks > 70 and marks <= 80:
    print("B1 grade")
elif marks > 60 and marks <= 70:
    print("B grade")
elif marks > 50 and marks <= 60:
    print("Can do Better!")
else:
    print("Need to work hard")

#5
def new(rn,name="abc"):
    f = open('student.txt','w')
    f.write(f" {rn},  {name}")
    print("roll no of the student = ",rn)
    print("name of the student = ",name)
new(1)
new(2,'aaa')

#6
f1 = open('thor.jpeg','rb')
f2 = open('thor1.jpeg','wb')
f2.write(f1.read())

from zipfile import *
f =ZipFile('demo.zip','w',ZIP_DEFLATED)
f.write('thor1.jpeg')

#unzip
from zipfile import *
f=ZipFile('demo.zip','r')
f.extractall('d:')
print("unzip")

#7
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Book1.xlsx")
print(df)
x=df['program']
y=df['admission']
plt.bar(x,y)
plt.xlabel("Program")
plt.ylabel("Admission")
plt.title("Admission info")
plt.legend()
plt.show()




