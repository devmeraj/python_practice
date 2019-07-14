# Write a Python function that checks whether a passed string is palindrome or   not. 

def isPalindrome(n):
    if (n == n[::-1]):
        return n + ' is palindrome'
    else:
        return n + ' isn\'t a palindrome'

print(isPalindrome('madam'))
print(isPalindrome('nurse'))
