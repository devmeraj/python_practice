def palindrom(x):
    if (x == x[::-1]):
        return 'The string is a palindrom'
    else:
        return 'The string is not a palindrom'


print(palindrom('madam'))
print(palindrom('nurse'))