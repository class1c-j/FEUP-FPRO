"""
Write a Python function roman_to_integer(astring) that, given a valid roman numeral as a string, returns its corresponding decimal value.
""" 


def roman_to_integer(astring):
    total = 0
    conversion = {'I':'1', 'V':'5', 'X':'10', 'L':'50', 'C':'100', 'D':'500', 'M':'1000'}
    for x in range(len(astring)):
        if x == len(astring) - 1:
            total += int(conversion[astring[x]])
        elif int(conversion[astring[x]]) < int(conversion[astring[x+1]]):
            total -= int(conversion[astring[x]])
        else:
            total += int(conversion[astring[x]])
    return total


print(roman_to_integer('XV'))
print(roman_to_integer('LXXXIV'))
print(roman_to_integer('XLIII'))
print(roman_to_integer('MMMCMXCIX'))
print(roman_to_integer('MCMLXVI'))
print(roman_to_integer('MMCDVI'))
print(roman_to_integer('MMXIX'))
print(roman_to_integer('MCMXCV'))
