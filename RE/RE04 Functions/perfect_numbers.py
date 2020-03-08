"""
Write a Python boolean function is_perfect(n) to check whether a number n is perfect or not.
In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, except itself.
For example:
    for n=6, the function returns True
    for n=12, the function returns False
    for n=28, the function returns True
"""


def is_perfect(n):
    sum_divisors = 0
    if n == 0:
        return False
    for d in range(1, n):
        if n % d == 0:
            sum_divisors += d
    return sum_divisors == n


print(is_perfect(496))
print(is_perfect(300))
print(is_perfect(8218))
print(is_perfect(8128))