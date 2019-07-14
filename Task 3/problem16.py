# Write a program that prints the next 20 leap years.

leapYear = []
year = 2018
while len(leapYear) < 20:
    if (year % 4 == 0) and (year % 100 != 0):
        leapYear += [year]
        print(year)
    elif (year % 4 == 0) and (year % 100 == 0):
        if (year % 400 == 0):
            leapYear += [year]
            print(year)
    year += 1

print(leapYear)