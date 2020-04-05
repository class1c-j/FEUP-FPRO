"""
Write a Python program that, given an integer num by user input, computes its reverse (the number with the digits by the reverse order) and prints it.

You are not allowed to use string manipulation (for example string concatenation).
""" 

num = int(input())
num_aux = num
digits = 0
inversed = 0
power = 0
num_aux2 = num

if num_aux2 < 0:
    num = num_aux2 * (-1)
    num_aux = num


# count digits
while num_aux > 0:
    if num_aux == 0:
        digits = 1
    num_aux //= 10
    digits += 1

for r in range(digits):
    power = digits - r
    inversed += (num % 10) * (10 ** (power - 1))
    num //= 10

if num_aux2 >= 0:    
    print(inversed)
else:
    print(-1 * inversed)

"""
public tests:
766
789
45654
190

private tests:
1
12
1900
32893474237
"""
