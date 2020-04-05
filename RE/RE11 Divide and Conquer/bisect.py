"""
Write a Python function called bisect(f, n) that, given a function f and steps n, returns the 
root approximation at that step.
"""

def bisect(f, n):
    upper = 1
    lower = 0
    for _ in range(n):
        c = (upper + lower) / 2
        if f(lower) * f(c) > 0:
            lower = c
        else:
            upper = c
    return round(c, 5)

print(bisect(lambda x: (1-(x+0.2))*(x+0.2), 10))
print(bisect(lambda x: x**2-0.1, 8))
print(bisect(lambda x: x**0.5-0.9, 10))
print(bisect(lambda x: 2*x-20*x**2+1.5, 12))
print(bisect(lambda x: -5*x+3, 4))
print(bisect(lambda x: x**2-0.8, 8))
print(bisect(lambda x: x**0.5-0.9, 10))
print(bisect(lambda x: -2*x+20*x**2-1.5, 12))
