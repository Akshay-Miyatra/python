#1
#lst1 =['apple','banana','mango','kivi']
#lst2=input("Enetr the search string")
#if lst2 in lst1:
#    print("Enter string is available")
#else:
#     print("Enter valid string")

#2
# str1 = input("Enter the string :")
# str1 = str1.replace(" ", "").lower()
# if str1 == str1[::-1]:
#     print("Enter string is pelindrom")
# else:
#     print("Enetr string is not pelindrom")


#3
# user_input = input("Enter a string: ")
# reversed_text = user_input[::-1]
# print("Reversed string:", reversed_text)

#4
# user_input = input("Enter a string: ")

# print("\nChoose an option:")
# print("i) Convert to UPPER case")
# print("ii) Convert to lower case")
# print("iii) Convert to sWAP case")
# print("iv) Convert to Title Case")

# choice = input("\nEnter your choice (i/ii/iii/iv): ")

# if choice == 'i':
#     print("Upper case:", user_input.upper())
# elif choice == 'ii':
#     print("Lower case:", user_input.lower())
# elif choice == 'iii':
#     print("Swap case:", user_input.swapcase())
# elif choice == 'iv':
#     print("Title case:", user_input.title())
# else:
#     print("Invalid choice!")

#5
# string_list = []
# count = int(input("How many strings do you want to enter? "))

# for i in range(count):
#     s = input("Enter string: ")
#     string_list.append(s)

# string_list.sort()

# print("\nStrings in alphabetical order:")
# for s in string_list:
#     print(s)

#6
# Create a tuple
# my_tuple = (10, 20, 30, 40, 50)
# print("Original tuple:", my_tuple)

# # Convert tuple to list to modify it
# temp_list = list(my_tuple)

# # Insert 25 at the third position (index 2)
# temp_list.insert(2, 25)

# # Convert back to tuple
# my_tuple = tuple(temp_list)
# print("Updated tuple:", my_tuple)

# 7
# library = {
#     "Bookid": "B101",
#     "Title": "Python Programming",
#     "Author": "John Smith",
#     "Price": 499,
#     "Publisher": "Tech Books Publishing"
# }

# a. Display the dictionary
# print("a. Library Dictionary:")
# print(library)

# # b. Display the name of Author
# print("\nb. Author Name:")
# print(library["Author"])

# # c. Display the Bookid
# print("\nc. Book ID:")
# print(library["Bookid"])

# # d. Display the length of the dictionary
# print("\nd. Length of the dictionary:")
# print(len(library))

# # e. Update the price
# library["Price"] = 550
# print("\ne. Updated Price:")
# print(library["Price"])

# # f. Insert 'Year' as a new key and display the updated dictionary
# library["Year"] = 2025
# print("\nf. Updated Dictionary with Year:")
# print(library)

#8
# Create a numeric array (list)
# numbers = [10, 20, 30, 40, 50]
# print("Original array:", numbers)

# # Add 2 to each element
# add_2 = [x + 2 for x in numbers]
# print("After adding 2:", add_2)

# # Subtract 3 from each element
# subtract_3 = [x - 3 for x in numbers]
# print("After subtracting 3:", subtract_3)

# # Multiply each element by 3
# multiply_3 = [x * 3 for x in numbers]
# print("After multiplying by 3:", multiply_3)

# # Divide each element by 2
# divide_2 = [x / 2 for x in numbers]
# print("After dividing by 2:", divide_2)

# # Find max and min
# maximum = max(numbers)
# minimum = min(numbers)
# print("Maximum value:", maximum)
# print("Minimum value:", minimum)

# # Find average
# average = sum(numbers) / len(numbers)
# print("Average value:", average)

#9
# import array

# # Create a numeric array using the array module
# arr = array.array('i', [5, 10, 15, 20, 25])
# print("Original array:", arr)

# # Append an element (e.g., 30)
# arr.append(30)
# print("After appending 30:", arr)

# # Pop the last element
# arr.pop()
# print("After popping an element:", arr)

# # Insert an element at the desired position (e.g., 100 at index 2)
# arr.insert(2, 100)
# print("After inserting 100 at position 2:", arr)

# # Reverse the elements in the array
# arr.reverse()
# print("After reversing:", arr)

# # Convert the array to a list
# arr_list = arr.tolist()
# print("Converted array to list:", arr_list)


#10
import array

# Accept numeric elements from the user
# num_elements = int(input("How many elements do you want to enter? "))
# arr = array.array('i', [])  # Create an empty array

# Accept the elements and append them to the array
# for _ in range(num_elements):
#     num = int(input("Enter a number: "))
#     arr.append(num)

# # Display the array
# print("Array:", arr)

# # Ask the user to enter a search element
# search_element = int(input("Enter the element to search for: "))

# # Check if the element is in the array
# if search_element in arr:
#     position = arr.index(search_element)  # Find the position of the element
#     print(f"Element {search_element} found at position {position}.")
# else:
#     print(f"Element {search_element} not found in the array.")

#11
# import array

# # Create two empty integer arrays
# arr1 = array.array('i', [])
# arr2 = array.array('i', [])

# print("Enter 5 numbers for the first array:")
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     arr1.append(num)

# print("\nEnter 5 numbers for the second array:")
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     arr2.append(num)

# # Compare corresponding elements and display the bigger one
# print("\nBigger numbers from each position:")
# for i in range(5):
#     if arr1[i] > arr2[i]:
#         print(arr1[i])
#     else:
#         print(arr2[i])

#12
# import array

# Ask the user for the dimension (number of elements)
# n = int(input("Enter the number of elements for the array: "))

# # Create an empty integer array
# arr = array.array('i', [])

# # Accept values from the user
# print("Enter", n, "integer values:")
# for i in range(n):
#     val = int(input(f"Enter value {i + 1}: "))
#     arr.append(val)

# # Display the created array
# print("The created array is:", arr)

#13
# Function to calculate simple interest
# def calculate_simple_interest(principal, rate, time):
#     interest = (principal * rate * time) / 100
#     return interest

# # Input values from user
# p = float(input("Enter principal amount: "))
# r = float(input("Enter rate of interest (%): "))
# t = float(input("Enter time (in years): "))

# # Call the function
# si = calculate_simple_interest(p, r, t)

# # Display result
# print(f"Simple Interest = {si}")

#14
# Function to perform arithmetic operations
# def arithmetic_operations(a, b):
#     print(f"Addition: {a} + {b} = {a + b}")
#     print(f"Subtraction: {a} - {b} = {a - b}")
#     print(f"Multiplication: {a} * {b} = {a * b}")
#     if b != 0:
#         print(f"Division: {a} / {b} = {a / b}")
#     else:
#         print("Division: Cannot divide by zero.")

# # Take input from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Call the function
# arithmetic_operations(num1, num2)

#15
# Function to accept multiple strings and store them in a list
# def get_strings():
#     string_list = []
#     print("Enter strings one by one. Type 'stop' to finish.")
#     while True:
#         s = input("Enter a string: ")
#         if s.lower() == 'stop':
#             break
#         string_list.append(s)
#     return string_list

# # Call the function and store the result
# user_strings = get_strings()

# # Display the list
# print("List of entered strings:", user_strings)

#16
# Lambda function to find the biggest of three numbers
# biggest = lambda a, b, c: max(a, b, c)

# # Input three numbers from the user
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
# z = float(input("Enter third number: "))

# # Call the lambda function and display the result
# print("The biggest number is:", biggest(x, y, z))


#17
# print("Demonstrating 'break':")
# for i in range(1, 10):
#     if i == 5:
#         print("Breaking the loop at i =", i)
#         break
#     print("i =", i)

# print("\nDemonstrating 'pass':")
# for i in range(1, 5):
#     if i == 3:
#         pass  # Placeholder — does nothing
#     print("i =", i)














