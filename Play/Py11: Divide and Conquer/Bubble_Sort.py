"""
Write a Python function called bubble_sort(alist) that receives a list alist and returns its sorted version.

The way this algorithm works is by comparing each element against its neighbor and swapping if the second is bigger than the first.
"""
def bubble_sort(alist, swapped = True):
    while swapped:
        swapped = False
        for x in range(1, len(alist)):
            if alist[x-1] > alist[x]:
                alist[x-1], alist[x] = alist[x], alist[x-1]
                swapped = True
    return alist
