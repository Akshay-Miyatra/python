#1
# text = input("Enter a long string: ")
# print("Here is your text with \\n and \\t:\n" + text + "\n\t" + text)

#2
# string = input("Enter a string: ")
# print("3rd character:", string[2])  
# print("5th character:", string[4])

#3
# values = input("Enter 3 numbers separated by space: ")
# num1, num2, num3 = map(int, values.split())
# sum_result = num1 + num2 + num3

# print("The sum of {}, {} and {} is: {}".format(num1, num2, num3, sum_result))
# n1,n2,n3 = [int(i) for i in input("Enetr three value separated by space").split(' ')]
# sum = n1+n2+n3
# print("sum",sum)

#4
# a = 2
# b = 16
# result = a * 7 / b + a
# print("Result is:", result)

#5
# num = int(input("Enter a number: "))
# string = input("Enter a string: ")
# lst = input("Enter a list (comma-separated values): ").split(",")
# print("Number:", num)
# print("String:", string)
# print("List:", lst)

# #6
# print(f"The name of file is abc.py and its values are {lst}")

#7
# my_str = input("Enter a string: ")
# print("The type of the variable is:", type(my_str))
# print("The string is:", my_str)
# print("3rd character:", my_str[2])
# print("Character from 4th to 6th:", my_str[3:6])

# # Strings are immutable, so we have to create a new one
# new_str = my_str[:2] + 'A' + my_str[3:]
# print("Modified string:", new_str)

#8
# Octal to decimal
# oct_value = int('17', 8)
# print("Octal 17 to decimal:", oct_value)

# # Binary to decimal
# bin_value = int('1010', 2)
# print("Binary 1010 to decimal:", bin_value)

# # Float value
# float_value = int(45.67)  # Converts to int
# print("Float 45.67 to int:", float_value)

#9
# my_list = [10, "hello", 4.5, True, [1,2,3]]
# print("List elements:", my_list)
# print("Class of list:", type(my_list))
# print("First element:", my_list[0])
# print("4th element (using negative index):", my_list[-2])

# # Change 4th element
# my_list[3] = "changed"
# print("List after change:", my_list)

#10
# my_tuple = tuple([1, 2, 3, 4, 5, 6, 7, 8])

# # Tuples are immutable, so we can't modify directly
# # But we can convert it to a list, modify, and back to tuple
# temp = list(my_tuple)
# temp[0] = 100
# my_tuple = tuple(temp)
# print("Modified tuple:", my_tuple)

# print("3rd to 6th elements:", my_tuple[2:6])
# print("3rd to 6th elements (negative index):", my_tuple[-6:-2])

#11
# my_dict = {
#     1: "one", 2: "two", 3: "three",
#     4: "four", 5: "five", 6: "six",
#     7: "seven", 8: "eight", 9: "nine", 10: "ten"
# }
# print("Dictionary elements:", my_dict)
# print("Class of dictionary:", type(my_dict))
# print("Value of key 7:", my_dict[7])

# # Change value of key 7
# my_dict[7] = "new_seven"
# print("Updated dictionary:", my_dict)

# print("All values:", list(my_dict.values()))


#12
# my_set = {1, 2, 3, "hello", 4.5}

# # Try to insert duplicate
# my_set.add(2)
# print("After adding duplicate 2:", my_set)

# # Add two values
# my_set.add(99)
# my_set.add("new")
# print("After adding two values:", my_set)

# # Remove two values
# my_set.remove(1)
# my_set.remove("hello")
# print("After removing two values:", my_set)

#13
# my_frozenset = frozenset([1, 2, 3, "hello", 4.5])

# # Can't add or remove in frozenset - it will give error if we try
# print("Frozen set:", my_frozenset)

# # Trying to add or remove will cause error
# # my_frozenset.add(5)  # Error
# # my_frozenset.remove(1)  # Error

#14
# my_bytes = bytes([10, 20, 30, 40])

# # Access using negative and positive index
# print("First element (using positive index):", my_bytes[0])
# print("Last element (using negative index):", my_bytes[-1])

# # Bytes are immutable, so can't modify directly
# # But we can create new bytes
# new_bytes = my_bytes + bytes([50, 60])
# print("Bytes after adding two values:", new_bytes)

#15
# my_bytearray = bytearray([10, 20, 30, 40])

# print("First element (positive index):", my_bytearray[0])
# print("Last element (positive index):", my_bytearray[-1])

# # Add two values
# my_bytearray.extend([50, 60])
# print("After adding two values:", my_bytearray)

# # Modify last element
# my_bytearray[-1] = 70
# print("After modifying last element:", my_bytearray)

# # Remove last value
# my_bytearray.pop()
# print("After removing last value:", my_bytearray)



















