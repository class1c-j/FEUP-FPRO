"""
Write a Python program that computes and prints the number by using the Ramanujan formula:

You can use the math package for the factorial and square root (only!). The number controls the precision of the formula. Use K=50. Round the result to 8 decimal places.
Adapted from: Universidade Aberta 
"""
import math
sum_k = 0
k = 0

while k < 50:
    sum_k = sum_k + ((math.factorial(4 * k) * (1103 + 26390 * k)) /
    ((math.factorial(k) ** 4 ) * (396 ** (4 * k))))
    k += 1

pi = 1 / ((2 * math.sqrt(2) / 9801) * sum_k)

print(round(pi, 8))
