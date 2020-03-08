"""
Write a Python program that, given two numbers n1 and n2 provided by the user (each one in a different input() statement) produces a new number result by joining both of them, in the order they are given.

Converting the numbers into strings is forbidden.

For example: if the numbers given are n1=23 and n2=567, the resulting number 23567
"""

n1 = int(input("Insert n1: "))
n2 = int(input("Insert n2: "))
aux = n2
count = 0

while aux != 0:
    aux //= 10
    count += 1

if n2 == 0:
    print(n1 * 10)
else:
    print(n1 * (10 ** count) + n2)
