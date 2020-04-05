"""
Write a Python function comprehensions(i, j) that, given two integers i and j, return a tuple with three components computed in the interval [i, j]:
    A list with all numbers in that range that end in 3 or 8.
    A tuple with the square root, rounded to 2 decimals, of numbers in that range.
    A dictionary where the key is a number and the value is the corresponding character from the 
    ASCII table, of numbers in that range.
""" 

def comprehensions(i, j):
    ends3or8 = [x for x in range(i, j+1) if x%10 == 3 or x%10 == 8]
    sqrts = tuple([round(x**0.5, 2) for x in range(i, j+1)])
    asciival = dict(zip([x for x in range(i, j+1)], [chr(x) for x in range(i, j+1)]))
    return (ends3or8, sqrts, asciival)

print(comprehensions(0, 0))
print(comprehensions(100, 102))
print(comprehensions(110, 115))
print(comprehensions(48, 57))
print(comprehensions(65, 90))
print(comprehensions(97, 122))
print(comprehensions(65, 90))
print(comprehensions(60, 62))
