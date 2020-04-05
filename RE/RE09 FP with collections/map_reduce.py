"""
Write a Python function map_reduce(n1, n2) whereby you create a list of the square of 
the odd numbers between n1 and n2 ([n1, n2[). Then use reduce to multiply if the 
accumulated result is smaller than 50 or add the numbers otherwise.
""" 

from functools import reduce
def map_reduce(n1, n2):
    alist = list(map(lambda x: x**2, filter(lambda x: x % 2 == 1, range(n1, n2))))
    return reduce(lambda x, y: x * y if x * y < 50 else x + y, alist)

print(map_reduce(0, 5))
print(map_reduce(0, 10))
print(map_reduce(5, 100))
print(map_reduce(40, 60))
print(map_reduce(25, 74))
print(map_reduce(-5, 0))
print(map_reduce(100, 102))
print(map_reduce(0, 4))
