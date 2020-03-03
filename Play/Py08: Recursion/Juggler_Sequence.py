"""
Write a recursive Python function juggler(n, p) that, given two integers n and p, calculates the p-th term in the juggler sequence for n. The juggler sequence for a non-negative integer n is defined as follows:

    juggler(n, 0) = n
    juggler(n, p) = ⌊juggler(n, p-1)1/2⌋, if juggler(n, p-1) is even
    juggler(n, p) = ⌊juggler(n, p-1)3/2⌋, if juggler(n, p-1) is odd
"""
import math
def juggler(n, p):
    if p == 0:
        return n
    else:
        if juggler(n, p - 1) % 2 == 0:
            return math.floor(juggler(n, p-1)**(1/2))
        else:
            return math.floor(juggler(n, p-1)**(3/2))
