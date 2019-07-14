# Problem 15: Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of  6 to 21 , print Weird
# If  is even and greater than 21, print Not Weird

num = int(input('Type a number. '))

even = (num % 2 == 0)

if not even:
	print('Weird')
elif even and (num in range(2, 6)):
	print('Not Weird')
elif even and (num in range(6, 22)):
	print('Weird')
elif even and num > 21:
	print('not Weird')
