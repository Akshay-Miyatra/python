#1

# def bigorsmall(a,b):
#     if a>b:
#         print("Number one is big")
#     else:
#         print("number two is big") 
# # bigorsmall(10,20)
# x=int(input("Enter number one"))
# y=int(input("Enter number two"))
# bigorsmall(x,y)

#2
# def divisible(a):
#     if a/5==0:
#         print("Number is divisible by 5")
#     else:
#         print("Number is not divisible by 5")
# x=int(input("Enetr the number"))
# divisible(x)

#3
# def check(a):
#     if a>=0 and a<=100:
#         print("Number is between 0 and 100")
#     else:
#         print("number is not between 0 to 100")
# x=int(input("Enter any number"))
# check(x)

#4
# def length1(a):
#     b=str(a)
#     print("length of enetered number is",len(b))
#     if len(b) == 4:
#         print("Length of string is 4")
# x=int(input("enter any number"))
# length1(x)

#5
# def checkday(a):
#     days = {
#         1:"monday",2:"tuesday",3:"wednesday",4:"thurseday",5:"friday",6:"satureday",7:"sunday"
#     }
#     # print(type(days))
#     if a in days:
#         print("day is",days[a])
# x=int(input("enter the day number between 1 to 7"))
# checkday(x)

#6
# def arithmatic(a,b):
#     num = int(input("Enter your choice Between 1 to 4"))
#     if num == 1:
#         print("Addition of two numbers is",a+b)
#     elif num == 2:
#         print("Subtraction of two numbers is",a-b)
#     elif num == 3:
#         print("Multiplication of two numbers is",a*b)
#     elif num == 4:
#         print("Division of two numbers is",a/b)
#     else:
#         print("Invalid number")
# x=int(input("Enetr number 1"))
# y=int(input("Enetr number 2"))
# arithmatic(x,y)

#7
# def count_vowels_consonants(s):
#     vowels = "aeiouAEIOU"
#     v = 0
#     c = 0

#     for ch in s:
#         if ch.isalpha():  # only letters
#             if ch in vowels:
#                 v += 1
#             else:
#                 c += 1

#     print("Vowels:", v)
#     print("Consonants:", c)

# Input from user
# text = input("Enter a string: ")
# count_vowels_consonants(text)

# 8
# def table(a):
#     for i in range(1,11):
#         print(f"{a} * {i} = {a*i}")
# x=int(input("enter any number to get that number table"))
# table(x)

#9
# def square_and_cube(a):
#     square = a ** 2
#     print("the square of eneter number is",square)
#     cube = a ** 3
#     print("the cube of enter number is",cube)
# x=int(input("enetr the number : "))
# square_and_cube(x)

#10
# def convert(a):
#     b =  a.upper()
#     print("the upper case of enetered string is",b)
# convert("hello")

#11                                                                                         
# def loop1():
    # print("1 to 10")
    # for i in range(1,11):
    #     print(i)
    # print("10 to 1")
    # for v in range(10,0,-1):
    #     print(v)
    # print("iii")
    # for a in range(1,11,2):
    #     print(a)
    # print(iv)
    # for b in range(2,11,2):
    #     print(b)
# loop1()

#12
# def all(num):
#     while num<=1024:
#         print(num)
#         num *= 2 
# all(1)

#14 
# def sum(a,b):
#     add=a+b
#     print(add)
# x=int(input("Enter the number one"))
# y=int(input("Enter the number two"))
# sum(x,y)

#15
# count = 0
# print("enter numbers one by one. Type 'q' to quit.")
# while True:
#     user_input = input("enter a number (or 'q' to quit): ")
#     if user_input.lower() == 'q':
#         break
#     try:
#         number = float(user_input)  
#         count += 1
#     except ValueError:
#         print("Invalid input")
# print(f"Total numbers entered:{count}")


#16
# number = input("Enter a number: ")
# zero_count = number.count('0')
# print(f"Number of zeros: {zero_count}")

#17
# Function to check if a number is even or odd
# def check_even_odd(number):
#     if number % 2 == 0:
#         return f"{number} is an even number"
#     else:
#         return f"{number} is an odd number"

# Loop to repeatedly ask the user for numbers
# while True:
#     # Accept an integer from the user
#     num = int(input("Enter the number: "))
    
#     # Display whether the number is even or odd
#     result = check_even_odd(num)
#     print(result)
    
#     # Ask if the user wants to check another number
#     choice = input("Do you want to check another number? Y/N: ").strip().lower()
    
#     # Exit the loop if the user chooses 'N'
#     if choice != 'y':
#         break




    

