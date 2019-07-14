# Write a Python program to convert temperatures to and from celsius, fahrenheit. 
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
# Expected Output : 
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius  

def tempConverter(temp):
    if temp[-1].lower() == 'f':
        f = int(temp[:len(temp) - 1])
        c = ((f - 32) * 5) / 9
        result = str(round(c)) + '°C'
    elif temp[-1].lower() == 'c':
        c = int(temp[:len(temp) - 1])
        f = ((9 * c) + (32 * 5)) / 5
        result = str(round(f)) + '°F'
    return result

print('45 Degree fahrenheit is', tempConverter('45F'))
print('60 Degree celsius is', tempConverter('60C') )