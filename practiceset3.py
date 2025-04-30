#1

# salary = int(input('enter the employee salary'))
# print('basic slary',salary)

# da= 30 * salary
# hra = 15 * salary

# tax=3 * salary
# pf = 12 * salary

# gross_salary = salary + da + hra
# print('gross salary',gross_salary)

# net_salary = gross_salary-(tax+pf)
# print('net salary',net_salary)

# print()

# 2
# import sys

# if len(sys.argv) != 6:
#     print(" <mark1> <mark2> <mark3> <mark4> <mark5>")
#     sys.exit(1)

# marks = list(map(float, sys.argv[1:6]))

# total_marks = sum(marks)
# max_marks = 5 * 100 
# percentage = (total_marks / max_marks) * 100
# print(f"\nTotal Marks: {total_marks:.2f}")
# print(f"Percentage: {percentage:.2f}%")

#3

# water = int(input('how much water you want in liters'))

# if(water<=90):
#     bill_amount = 0
#     print("Water is free Rs 0")
# elif(water>90 and water<=150):
#     bill_amount = (water - 90) * 2
#     print('bill amount',bill_amount)
# elif(water>150 and water<=250):
#      bill_amount = (60 * 2) + (water - 150) * 5 #here we write 60 beacuse a difference between a 90-150 is 60
#      print('bill amount',bill_amount)
# elif(water>250):
#     bill_amount = (60 * 2) + (water - 250) * 10

#     print('bill amount',bill_amount)
# else:
#     print('please enter valid info')

#4
# Accept marks from the user
# marks = float(input("Enter marks scored by the student: "))

# # Allocate grade based on the marks
# if marks > 90:
#     grade = "A1 grade"
# elif 80 < marks <= 90:
#     grade = "A grade"
# elif 70 < marks <= 80:
#     grade = "B1 grade"
# elif 60 < marks <= 70:
#     grade = "B grade"
# elif 50 < marks <= 60:
#     grade = "Can do Better!"
# else:
#     grade = "Need to work hard"

# # Display the allocated grade
# print(f"The allocated grade is: {grade}")

#5

# income = float(input("Enter the yearly income (in lakhs): "))

# # Calculate tax based on the income
# if income <= 8:
#     tax = 0
#     print("No tax to be paid.")
# elif 8 < income <= 10:
#     tax = 0.15 * income
#     print(f"Tax to be paid: {tax} lakhs")
# elif 10 < income <= 20:
#     tax = 0.20 * income
#     print(f"Tax to be paid: {tax} lakhs")
# else:
#     tax = 0.30 * income
#     print(f"Tax to be paid: {tax} lakhs")

#6
# Accept two integer values
# num1 = int(input("Enter first integer value: "))
# num2 = int(input("Enter second integer value: "))

# # Display the smaller and larger value
# if num1 < num2:
#     print(f"The smaller value is: {num1}")
#     print(f"The bigger value is: {num2}")
# elif num1 > num2:
#     print(f"The smaller value is: {num2}")
#     print(f"The bigger value is: {num1}")
# else:
#     print("Both values are equal.")

#7

# marks1 = float(input("Enter marks for student 1: "))
# marks2 = float(input("Enter marks for student 2: "))
# marks3 = float(input("Enter marks for student 3: "))
# marks4 = float(input("Enter marks for student 4: "))

# # Find the highest mark among the 4
# highest_marks = max(marks1, marks2, marks3, marks4)

# # Display the highest mark
# print(f"The highest mark among all students is: {highest_marks}")
                                    

#8
# Accept the shopping amount from the user
# amount = float(input("Enter the shopping amount: Rs. "))

# # Calculate shipping charges and discount based on the amount
# if amount < 1500:
#     shipping_charges = 100
#     print(f"Please purchase Rs. {1500 - amount} more to avail shipping charge of Rs. 80/-")
#     print(f"Please pay Rs. {amount + shipping_charges}")
# elif 1500 <= amount < 3000:
#     shipping_charges = 70
#     print(f"Please purchase Rs. {3000 - amount} more to avail shipping charge of Rs. 50/-")
#     print(f"Please pay Rs. {amount + shipping_charges}")
# else:
#     discount = amount * 7 / 100
#     print(f"You saved Rs. {discount}")
#     print(f"Please pay Rs. {amount - discount}")






                                                                                                                                                                             
