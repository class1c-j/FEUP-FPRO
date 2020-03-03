"""
Write a Python function most_frequent(alist) that, given a list alist of integers, using a dictionary, returns the most frequent element in alist. In case of ties, return the element with the greatest value.

    most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]) returns the integer: -1
    most_frequent([-1, 111, 1, 11, -1, 11, 1, 111]) returns the integer: 111
"""
def most_frequent(alist):
    frequency = {}
    for x in alist:
        frequency[x] = frequency.get(x, 0) + 1
    for key, value in sorted(frequency.items(), reverse = True):
        if value == max((frequency.values())):
            return key
