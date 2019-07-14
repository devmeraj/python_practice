# Problem 13: write a program that takes a string and check whether the letter is lowercase or uppercase
# sample input:
# hasib
# output:
# lower case
# Hints: use islower() method


name = input('Type your name. ')

if name.islower():
	print('Lower case')
else:
	print('Uppercase')
