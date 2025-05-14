#1
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 60, 65, 70, 75]

plt.scatter(study_hours, marks,)

plt.title('Study Hours vs Marks')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Scored')

plt.show()

#2
import re
a = 'bscit bscnursing bmaa ba mca bca'
result = re.findall(r's[b,s][\w]*', a)
print(result)

#3
square = lambda x:x**2
a=3
print("suqare of given number",square(a))

#4
import os, sys

a = input("Enter a file name: ")

if os.path.isfile(a):
    f = open(a, 'r')
else:
    print("File does not open")
    sys.exit()

# Initialize counters
lc = wc = cc = 0

# Process the file line by line
for line in f:
    lc += 1
    words = line.split()
    wc += len(words)
    cc += len(line)

# Close the file
f.close()

# Print results
print("Number of lines:", lc)
print("Number of words:", wc)

print("Number of characters:", cc)

#5
# Yearly premium amount
premium = 25000

# Input age
age = int(input("Enter the age of the policy holder: "))

# Determine discount percentage
if age <= 20:
    discount_percent = 20
elif age <= 30:
    discount_percent = 18
elif age <= 40:
    discount_percent = 15
else:
    discount_percent = 0

# Calculate discount amount
discount_amount = (discount_percent / 100) * premium

# Display results
print("Applicable discount:", discount_percent, "%")
print("Discount amount: Rs.", discount_amount)
print("Premium after discount: Rs.", premium - discount_amount)

#7
import numpy as np

# Create an array and fill it with values
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

# 1. Insert value at a specific position (e.g., insert 25 at index 2)
arr = np.insert(arr, 2, 25)
print("\nArray after inserting 25 at index 2:", arr)

# 2. Append a value (e.g., append 60)
arr = np.append(arr, 60)
print("\nArray after appending 60:", arr)

# 3. Delete a specific value (e.g., delete value 40)
arr = arr[arr != 40]  # Using boolean indexing to remove 40
print("\nArray after deleting value 40:", arr)

# 4. Find the position of a specific element (e.g., find the position of 30)
position = np.where(arr == 30)[0][0] if 30 in arr else None
print("\nPosition of element 30:", position)

# 5. Convert array to list
arr_list = arr.tolist()
print("\nArray converted to list:", arr_list)

#6
import numpy as np

# Step 1: Create a 1D array with 6 elements
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original 1D array:", arr)

# Step 2: Convert to 2x3 shape
arr_2d = arr.reshape(2, 3)
print("\n2x3 Array:\n", arr_2d)

# Step 3: Convert back to 1D
arr_1d_again = arr_2d.flatten()
print("\nBack to 1D array:", arr_1d_again)







