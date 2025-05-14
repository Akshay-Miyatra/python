#1
def sum(a,b):
    add = a+b
    sub = a-b
    mul = a * b
    div = a / b
    return add,sub,mul,div
x = int(input("Enetr number 1"))
y = int(input("Enetr number 2"))
ad,su,mu,di = sum(x,y)
print("addtion is",ad)
print("subtraction is",su)

#2
a = int(input("Enetr any number"))
i=1
while i<=10:
    print(f"{a} * {i} ={a *i}")
    i+=1

#3
state = ['gujarat','maharastra']
capital = ['gandhinager','mumbai']
dict1 = zip(state,capital)
dict2 = dict(dict1)
print(dict2)

#4
import numpy as np
a = np.array([10,20,30,40,50])
total_sub = sum(a)
print("sum of all subjects",total_sub)
avg = total_sub / len(a)
print("Average of array is",avg)

5
f=open('xyz.txt','w')
a = input("Enetr the content that you want to enter in file")
f.write(a)
f.close()
print("content write")

f=open("xyz.txt",'r')
print(f.read())
# 

#6
#i
import re
a = "hello 2how r u 3uuu"
result = re.findall(r'\b\d\w+',a)
print(result)

ii
a = "hello how are you"
result = re.findall(r'\b\w{5}\b',a)
print(result)

iii
a = "india is a great country"
result = re.sub('india','bharat',a)
print(result)

#7
import matplotlib.pyplot as plt
state1 = {
    'india': 222,
    'america': 123,
    'china': 456,
}
state=list(state1.keys())
vote = list(state1.values())

plt.bar(state,vote)
plt.xlabel("county")
plt.ylabel("vote")
plt.legend(title="Country - Votes")
plt.show()

#8
import matplotlib.pyplot as plt

# Assumed data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 180, 220, 240, 210]

# Create line chart
plt.plot(months, sales)

# Add titles and labels
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (in units)")
plt.legend()

# Show chart
plt.tight_layout()
plt.show()





