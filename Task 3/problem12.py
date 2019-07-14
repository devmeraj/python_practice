# Write a function that returns the elements on odd positions in a list.
li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def oddPos(x):
    return x[1::2]

print(oddPos(li))