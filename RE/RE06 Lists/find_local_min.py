"""
Given a list of integers alist, write a Python function local_minima(alist, n) that finds all the local minima on it,
within a specified odd neighborhood n. The function should return a list with all (local minimum, index) pairs found
in alist.
An element alist[x] is a local minimum if it is less than or equal to its neighbors. The number of neighbors of an
element alist[x] depends on the neighborhood n. For example, if the neighborhood is 3, the element alist[x] has two
neighbors: alist[x-1] and alist[x+1]. If n=5, alist[x] has four neighbors: alist[x-2], alist[x-1], alist[x+1] and
alist[x+2].
Note that for corner elements, you have to consider only the neighbours that lie within the list range (in one side
only). Furthermore, if there are adjacent local minima (i.e., with the same value within the neighborhood range), you
have to return just the local minima with the lowest index.
"""


def local_minima(alist, n):
    n = n // 2
    final = []

    for ind, num in enumerate(alist):
        if (ind - n) < 0:
            test = alist[:(ind + n + 1)]
            if num == min(test):
                final = final + [(num, ind)]
        else:
            test = alist[(ind - n):(ind + n + 1)]
            if num == min(test):
                final = final + [(num, ind)]

    for i in range(1, n + 1):
        for j in range(len(final) - i):
            if final[j][0] == final[j + 1][0] and ((int(final[j][1]) + i) == int(final[j + 1][1])):
                final.remove(final[j + 1])
                break

    return final

print(local_minima([1, 5, 5, 2, 10, 10, 3], 3))
print(local_minima([1, 5, 5, 2, 10, 10, 3], 1))
print(local_minima([1, 5, 5, 2, 10, 10, 3], 5))
print(local_minima([1, 70, 20, 5, 5, 80, 2, 90, 100, 10, 15, 10, 3, 30, 10, 20, 50, 10, 1, -2], 5))