# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints: 
# Consider use range(#begin, #end) method, ‘and’

numbers = []
for num in range(2000, 3201):
  if (num % 7 == 0) and (num % 5 != 0):
      numbers = numbers + [num]
      print(num, end=', ')