# Write a Python program to count the number of even and odd numbers from a series of numbers. 
# Sample numbers : numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Output : 
# Number of even numbers : 4
# Number of odd numbers : 5


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evenNum = 0
oddNum = 0

for num in numbers:
    if num % 2 == 0:
        evenNum += 1
    elif num % 2 != 0:
        oddNum += 1

print('Number of even numbers: ', evenNum)
print('Number of odd numbers: ', oddNum)