"""
Write a Python function prod_zip(functions, arguments) that, given a list of functions and a list of arguments of the
same size (≥ 1), returns the product of each function applied to each argument of the same index.
"""
from functools import reduce


def prod_zip(functions, arguments):
    return reduce(lambda x, y: x * y, [functions[i](arguments[i]) for i in range(len(functions))])


print(prod_zip([lambda x: x*2, lambda x: x**2, lambda x: -x], [-5, 10, 3]))
print(prod_zip([lambda x: x*2, lambda x: x**2], [2, 9]))
print(prod_zip([lambda x: x+2], [1]))
print(prod_zip([lambda x:5, lambda x: x//3, lambda x: x%3, lambda x: [x][0]], [10, 67, 67, 10]))
 
