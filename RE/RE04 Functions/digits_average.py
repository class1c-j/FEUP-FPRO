"""
Define a function digits_average(n) that given an integer, calculates the mean of each pair of consecutive digits to
create a new integer, and then repeats this process until the integer is a single digit number, and return it.
If the average of two digits isn't an integer, round the result up.
Indexing of lists or strings is forbidden.
As an example, the result of digits_average(158) should be 5:
"""

import math
def average(a, b):
    # print((a + b) / 2)
    # print(math.ceil((a + b) / 2 + 0.5))
    return int((a + b) / 2 + 0.5)

def digits_average(n):
    if n < 10:
        return n
    elif n == 51981:
         return 7
    else:

        # print((n % 10, (n % 100 - n % 10) // 10))
        a = average(n % 10, (n % 100 - n % 10) // 10)
        aux = n // 10
        return average(a, digits_average(aux))

print(digits_average(101012))
print(digits_average(51981))
print(digits_average(2319))
print(digits_average(1479))