"""
An interval list is a list of tuples that represent intervals. Each tuple represents an interval in the form
(min, max). Tuples appear in increasing order in the list and the intervals are disjoint.
For example, the list of intervals intlist=[(1,1), (3,5), (10,15)] represents the full sequence 1, 3, 4, 5, 10, 11,
12, 13, 14, 15.
Write a generator function generator(intlist) that iteratively yields the next term in the full sequence, encoded in
the list intlist.
"""

def generator(intlist):
    for i in range(len(intlist)):
        for j in range(intlist[i][0], intlist[i][1]+1):
            yield j
 
print(list(generator([(1, 1), (3, 5), (10, 15)])))
print(list(generator([(0, 5), (10, 15), (100, 102)])))
print(list(generator([(0, 0), (2, 2)])))
print(list(generator([(-10, -5), (2, 10), (70, 72), (102, 105)])))
print(list(generator([(-120, -116), (-3, 3)])))
print(list(generator([(5, 6), (7, 9), (11, 15)])))
print(list(generator([(8, 10), (15, 18), (21, 24), (29, 36), (38, 40), (50, 55)])))
print(list(generator([(4, 7), (9, 11), (20, 23)])))
