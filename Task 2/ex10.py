a = input('Type any interger number. ')

n1 = int('%s' % a)
n2 = int('%s%s' % (a, a))
n3 = int('%s%s%s' % (a, a, a))

output = n1 + n2 + n3
print(output)