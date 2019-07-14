# Write a Python program to sum all the items in a list

def sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


print('Total:', sum([1, 2, 3, 4, 5, 6]))