"""
Write a Python function fib(n) that returns a list of the first n Fibonacci numbers. The next number in a Fibonacci sequence is defined as the sum of the previous two numbers, and the first two numbers are defined as 0 and 1, respectively.

    fib(1) should return the list: [0]
    fib(5) should return the list: [0, 1, 1, 2, 3]
"""
def fibnum(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibnum(n - 1) + fibnum(n - 2)


def fib(n):
    result = []
    for n in range(1, n + 1):
        result.append(fibnum(n))
    return result
