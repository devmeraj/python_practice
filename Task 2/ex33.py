def sum(x, y, z):
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z


print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))