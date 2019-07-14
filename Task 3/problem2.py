#  Write a Python program to get the smallest number from a list.

def min(numbers):
    num = numbers[0]
    for n in numbers:
        if n < num:
            num = n
    
    return num

print('Smallest number is: ', min([5, -1, 10, 2222, 1, 0]))