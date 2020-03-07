"""
Define a function digits_average(n) that given an integer, calculates the mean of each pair of consecutive digits to create a new integer, and then repeats this process until the integer is a single digit number, and return it.

If the average of two digits isn't an integer, round the result up.

Forbidden: Indexing of lists or strings; using cycles; using global variables.

You may use this solution as your code base:

import math
def average(a, b):
    return math.ceil((a + b) / 2)

def digits_average(n):
    while n >= 10:
        avg = 0
        power = 0
        while n >= 10:
            avg = avg + average(n % 10, (n//10) % 10) * 10**power
            n //= 10
            power += 1
        n = avg
    return n

Example:

    digits_average(158) should return 5

"""
import math
def average(a, b):
    return math.ceil((a + b) / 2) 
def digits_average(n):
    m =0
    if n <10:
        return n
    else:
        def avg(n,m):
            if n<10:
                return m
            else:
                m =m*10 + average(n%10, (n//10)%10)
                print(m)
                return avg(n//10,m)
        m = avg(n,m)
        return digits_average(m)  
