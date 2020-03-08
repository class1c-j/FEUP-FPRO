"""
Write a Python function sum_numbers(n) that returns the sum of all positive integers up to and including n.
For example:
    for n=10, the function returns the integer 55 (because 1+2+3+. . . +10)
"""


def sum_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


print(sum_numbers(0))
print(sum_numbers(543))
print(sum_numbers(5))
print(sum_numbers(194))