# Write a Python program to sum all the items in a list

# Question 2
#  Write a Python program to get the smallest number from a list.

# Question 3
# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def strCount(string):
    result = 0
    for s in string:
        strLength = len(s)
        if strLength >= 2:
            if s[0] == s[-1]:
                result += 1
    return result
print(strCount(['abc', 'xyz', 'aba', '1221']))