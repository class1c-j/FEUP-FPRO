"""


Write a Python function count_zeros(f) that receives a function f that when called produces a list of integers alist. This list has several 1s followed by 0s (for example, alist=[1, 1, 1, 0, 0]). Your function must count the number of zeros on that list.

The naive solution would iterate through the list in O(n) time. Take advantage of the fact that the list is ordered to reduce that time to O(log n).
Adapted from: Geeks for Geeks 
"""
def count_zeros(f):
    alist = f()
    lb = 0
    ub = len(alist)
    while lb < ub:
        mid = (ub + lb) // 2
        if alist[mid] == 0 and (mid == 0 or alist[mid-1] != 0):
            return len(alist) - mid
        elif alist[mid] == 1:
            lb = mid
        else:
            ub = mid
