"""


Write a Python function reciprocals(alist) that, given alist, returns another list with the integers that are the reciprocals of the integers of the given list. The reciprocal of the number n is computed as 1/n. The function catches the exceptions to continue doing the reciprocals, as possible.

"""
def reciprocals(alist):
    poss = []
    for x in alist:
        try:
            res = 1 / x
        except:
            pass
        else:
            poss.append(x)
    return list(map(lambda x: 1/x, poss))
