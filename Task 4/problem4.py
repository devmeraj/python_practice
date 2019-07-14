# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def uniqueList(ls):
    newList = set(ls)
    return list(newList)


sampleList = [1,2,3,3,3,3,4,5]
print(uniqueList(sampleList))