"""
Given a tuple of n integers, with n > 3, write a Python function triplet(atuple) that finds a triplet (a, b, c) such
that their sum is zero (a + b + c = 0).
In case there is more than one triplet that sums up to zero, you should return the triplet with the lowest index (idx),
such that (idxa , idxb, idxc) < (idxan , idxbn, idxcn). In case there are no triplets that sum up to zero, the function
returns an empty tuple ().
Work in Spyder and save the program in the file triplet.py.
"""

def triplet(atuple):
    for i in range(len(atuple) + 1):
        for j in range(i + 1, len(atuple)):
            for k in range(j + 1, len(atuple)):
                if (atuple[i] + atuple[j] + atuple[k]) == 0:
                    return atuple[i], atuple[j], atuple[k]

print(triplet((0, -1, -5, -2, 4, 5, 15, 21, 42, 3)))
print(triplet((-3, 5, 4, 6, 1, -4, 7, 2, 1, -1, -1)))
print(triplet((-5, -4, -1, 4, 2, -2, -7, -4)))
print(triplet((9, 9, 4, -8, -7, 1, 4, 4, -1, 1, 0)))