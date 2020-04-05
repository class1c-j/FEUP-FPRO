"""
Write a Python function raise_exception(alist, value) that receives a list of integers alist and an integer value and raises an exception for each element of alist that is not greater than value.
""" 

def raise_exception(alist, value):
    result = []
    for n in alist:
        if n <= value:
            result.append(ValueError('{0} is not greater than {1}'.format(n, value),))
    return result


print(raise_exception([1, -2, 3, 0], 3))
print(raise_exception([3], 2))
print(raise_exception([0, 1, 0, -10], -1))
print(raise_exception([-10, 1, 50, -20], 0))
print(raise_exception([-10.78, 50.6, -20.1, -1.1, -0.9, -1], -1))
print(raise_exception([0, 1000, 2000, 1000, 5000, 0], 1000))
print(raise_exception([-5, -5, -5], -2))
print(raise_exception([], -2))
