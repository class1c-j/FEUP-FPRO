"""
Write the Python function repeated(nlist) that, given a list of integers in nlist, returns the difference between
the number of repetitions of even numbers and the number of repetitions of odd numbers. A number that occurs n 
times in the list counts as n-1 repetitions. Zero is an even number.

You cannot use cycles, only map/filter/reduce or list comprehensions.
"""


def repeated(nlist):
    return sum([[x for x in nlist if x % 2 == 0].count(x) - 1 for x in list(set([x for x in nlist if x % 2 == 0]))])\
           - sum([[x for x in nlist if x % 2 == 1].count(x) - 1 for x in list(set([x for x in nlist if x % 2 == 1]))])


print(repeated([2, 3, 3]))
print(repeated([2, 0, 5, -1, 2, 3, -1, 5, 0, 2, -1]))
print(repeated([0, 4, 0, 6, 4, 5, 3, 0, 5, 8, 3, 0, 2, 3, 4, 4, 6, 6, 2, 4, 5, 6, 3, 6, 2, 0, 3]))
print(repeated([7, 5, 8, 8, 5, 9, 2, 2, 8, 6, 4, 6, 9, 6, 7, 7, 8, 2, 3, 7, 8, 0, 0, 3, 0]))
print(repeated([2, 0, 3, 0, 3, 3, 0]))
print(repeated([4, 1, 3, 5, 4, 1, 8, 9, 4, 3, 5, 1, 3, 9, 5, 3, 9, 4, 5, 5, 9]))
print(repeated([4, 8, 5, 6, 9, 4, 4, 3, 3, 8, 8, 6, 4, 7, 0, 2, 2, 4, 6, 1, 6, 3, 1, 2, 3, 7]))
print(repeated([42, 78, 42, 96, 12, 4, 90, 15, 56, 96, 81, 93, 51, 30, 13, 14, 76, 72, 52, 76, 4, 85, 78, 14, 46,
                42, 31, 63, 93, 26, 98, 6, 13, 90, 34, 31, 50, 49, 92, 0, 26, 57, 56, 77, 44, 91, 74, 98, 29, 65, 28,
                92, 68, 51, 18, 98, 2, 59, 63, 61, 85, 51, 87, 89, 66, 30, 5, 74, 78, 12, 7, 51, 68, 77, 71, 58, 94, 65,
                2, 81, 21, 45, 81, 7, 72, 5, 91, 46, 51, 2, 30, 46, 98, 22, 34, 32, 73, 92, 73, 61, 10, 22, 32, 3, 0,
                70, 62, 8, 68, 11, 83, 61, 17, 78, 47, 25, 65, 48, 47, 6, 15, 53, 87, 64, 61, 33, 32, 35, 52, 47, 79,
                22, 19, 28, 23, 36, 19, 19, 90, 96, 5, 65, 86, 13, 13, 42, 35, 57, 44, 52, 58, 60, 28, 42, 54, 67, 27,
                76, 6, 75, 57, 17, 6, 90, 11, 72, 84, 73, 25, 26, 8, 92, 77, 7, 58, 59, 43, 0, 32, 22, 22, 52, 67, 56,
                55, 23, 47, 0, 40, 8, 55, 46, 44, 76, 28, 43, 19, 46, 40, 97, 67, 7, 89, 57, 92, 28, 31, 65, 5, 2, 90,
                3, 57, 4, 16, 77, 75, 5, 53, 43, 6, 44, 16, 43, 67, 85, 78, 63, 34])) 
