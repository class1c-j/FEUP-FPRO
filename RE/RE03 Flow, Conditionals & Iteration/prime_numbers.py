"""
Write a Python program that takes an integer num, provided by the user, and outputs: True when num is a prime number and False otherwise.

A prime number (or a prime) is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers [wikipedia].

For example for num = 7 the output is True.
"""

n = int(input("Insert number: "))

if n == 1:
    print("False")
else:
    for i in range(3, int(n**0.5)):
        if n % i == 0:
            print("False")
            break
    else:
        print("True")