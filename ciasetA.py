#1
def sum(a,b):
    c=a+b
    print("sum of two number is = ",c) 
# sum(10,20)
x = int(input("Enter number one"))
y = int(input("Enter number two"))
sum(x,y)

#2
a = int(input("Enetr the number"))
for i in range(1,11):
    print(f"{a} * {i} = {a * i}")

#3
lst1 = ['karnataka','mp','rajsthan','maharastra','gujarat']
las2 =['bengaluru','bhopal','mumbai','gandhinager']

dict1 = zip(lst1,las2)
# print(dict1)

dict2 = dict(dict1)
print(dict2)

#4
voting = []
for i in range(1,6):
    vote = int(input(f"Enter city {i}"))
    voting.append(vote)
total_vot  = sum(voting)
print("Total vote is = ",total_vot)
avg_sum = total_vot / len(voting)
print("Average of the vote is = ",avg_sum)

#5
f1 = open('thor.jpeg','rb')
f2  = open('thor1.jpeg','wb')
f2.write(f1.read())
f1.close()
f2.close()
print("image copy successfully")

#6
(i)
import re
str1 = "hello@@world12345welcome"
result = re.split(r'\W+',str1)
print(result)

(ii)
str1= "january march may june october"
result = re.findall(r'\b\w{5,}\b',str1)
print(result)

III
str1 = "1 2 12 one two"
result = re.findall(r'\b\d\b',str1)
print(result)

\w  = any alphanumeric(A-Z,a-z,0-9)
\W = any non alphanumeric
\d = any digit 0-9
\D = any non digit
\s = white space
\S = any non white space
\b = sapce around word 
\A = matches at the start of the string
\Z = matches at the end of the 

#7
import matplotlib.pyplot as plt

# Data input as tuple
states = ("Maharashtra", "Karnataka", "Gujarat", "Punjab", "Tamil Nadu")
votes = (1200, 950, 1100, 700, 1300)

# Create bar chart
plt.bar(states, votes, color='skyblue')

plt.title("Voting Results by State")
plt.xlabel("States")
plt.ylabel("Number of Votes")
plt.legend()

# Show the chart
plt.tight_layout()
plt.show()


#8
import matplotlib.pyplot as plt

# Data input as tuple
states = ("Maharashtra", "Karnataka", "Gujarat", "Punjab", "Tamil Nadu")
votes = (1200, 950, 1100, 700, 1300)
colors = ['red','blue','green','yellow','black']
# Create bar chart
plt.pie(votes,labels=states,colors=colors)

# Add titles and labels
plt.title("Voting Results by State")


# Add legend
plt.legend()

# Show the chart
plt.tight_layout()
plt.show()


