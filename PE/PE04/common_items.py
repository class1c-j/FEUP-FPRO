 """
Write a Python function common_items(alist, aset) that, given a list alist and a set aset,
 returns how many elements from alist appear in aset.
"""


def common_items(alist, aset):
    return len([x for x in alist if x in aset])


print(common_items([3, 1, 1, 2], {1, 3}))
print(common_items([1, 2, 2, 3, 4], {1, 3, 4}))
print(common_items([], {1}))
print(common_items([1, -5, -5, -5, 7, 9], {9, -5}))
print(common_items([-20, 10, 5, 50], {-20}))
print(common_items([100, 80, 90, 20, 30, 55], {80, 10, 50, 90}))
print(common_items([1, 2, 3, 4, 5], {}))
print(common_items([60, 11, 10, 60, 20], {10, 11}))
