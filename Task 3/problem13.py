#Write a function that computes the running total of a list.

li = [4, 6, 7, 8, 9, 2, 6]
sum = 0

for l in li:
    print('{:<5} {}'.format(sum, l))
    sum += l