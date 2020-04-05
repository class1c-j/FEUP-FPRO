"""
Write a Python function sort_by_f(alist) that, given a list alist, returns the list sorted using a lambda function, defined as:
f(x) = 5-x if x ≥ 5, x otherwise.
"""

 def sort_by_f(alist):
    return sorted(alist, key = lambda x: 5-x if x >= 5 else x)

print(sort_by_f([-10, -6, 2, 5, 90]))
print(sort_by_f([-1, -2, 2, 15, 99]))
print(sort_by_f([50, -10, 5, 5, 10, 20, -5]))
print(sort_by_f([0]))
print(sort_by_f([10, 11, -12, 2, -2, -13, 14, 15, -16]))
print(sort_by_f([-16, 15, 14, 0, -13, -12, 11, 10]))
print(sort_by_f([-1, 1, 2, -2, -3, 3, -4, 4, 5, -5, -6, 6, 7, -7]))
print(sort_by_f([]))
