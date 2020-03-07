"""


Write a function maximum_depth(l) that receives a list l, which can contain other lists, and returns what is the maximum depth in that list.

The depth corresponds to the number of sub-lists: [] has depth=1, [[]] has depth=2, [[[]]] has depth=3.

"""
def maximum_depth(l):
    if l == []:
        return 1
    maximum = 0
    for i in l:
        if maximum_depth(i) > maximum:
            maximum = maximum_depth(i)
    return maximum +1

print(maximum_depth([[], [[]], [], [[]]]))
