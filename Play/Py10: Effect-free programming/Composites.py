"""
Write a generator function get_composites(n) that yields a sequence of composite numbers in the interval [4, n].

There are two kinds of positive numbers: prime numbers and composite numbers. A composite number is the product of a sequence of prime numbers.
"""
def get_composites(n):
    for x in range(4, n+1):
        for y in range(2, x):
            if x % y == 0:
                yield x
                break
