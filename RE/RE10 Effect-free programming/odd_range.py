"""
Write a generator function odd_range(start, stop, step) that yields the odd numbers between start 
and stop with a step increment between odd numbers.
""" 

def odds(start, stop):
    for i in range(start, stop):
        if i % 2 == 1:
            yield i

def odd_range(start, stop, step):
    for j in range(0, len(list(odds(start, stop))), step):
        yield list(odds(start, stop))[j]

print(odd_range(1, 10, 1))
print(odd_range(0, 20, 2))
print(odd_range(100, 150, 5))
print(odd_range(3, 35, 10))
print(odd_range(10, 0, 1))
print(odd_range(-5, 5, 2))
print(odd_range(-50, 50, 4))
print(odd_range(-50, 50, 5))
