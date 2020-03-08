"""
Write a Python function adigits that receives 3 strings, each one with a single character, representing a decimal digit.
The function returns the highest integer number that you can assemble with the 3 digits given as parameters.
For example:
    adigits("4", "2", "5") returns the integer 542
    adigits("9", "1", "9") returns the integer 991
"""


def adigits(a, b, c):
    return int(''.join(sorted([a, b, c], reverse=True)))

print(adigits('0', '8', '7'))
print(adigits('5', '1', '9'))
print(adigits('8', '6', '7'))
print(adigits('7', '1', '2'))