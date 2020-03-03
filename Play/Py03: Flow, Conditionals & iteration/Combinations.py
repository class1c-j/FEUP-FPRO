"""
Write a Python function C that receives the number of objects to choose from n, the number of objects selected r and produces all combinations possible.

Remember the formula:

Round the result to the floor, for example the floor of 8.4 is 8 and the floor of 5.7 is 5. 

You cannot use the math package.
"""
def factorial(f):
    factorial = 1
    for x in range(1, f + 1):
        factorial = factorial * x
    return factorial


def C(n, r):
    combinations = factorial(n) / (factorial(r) * factorial(n - r))
    return int(combinations)
