"""
Write a recursive Python function sum_digits_rec(n) that returns the sum of the digits of an integer number.

Using global variables or cycles is forbidden.
Adapted from: www.w3resource.com 
"""
def sum_digits_rec(n):
    if n >= 0 and n < 10:
        return n
    else:
        return (n % 10) + sum_digits_rec(n // 10)
