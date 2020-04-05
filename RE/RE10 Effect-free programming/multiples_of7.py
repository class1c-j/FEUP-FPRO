"""
Write a generator function multiples_of7(n) which can iterate the numbers, which are divisible by 7, in the interval [0, n[.
""" 

def multiples_of7(n):
    for i in range(n):
        if i % 7 == 0:
            yield i

print(multiples_of7(21))
print(multiples_of7(22))
print(multiples_of7(8))
print(multiples_of7(100))
print(multiples_of7(0))
print(multiples_of7(40))
print(multiples_of7(50))
print(multiples_of7(1000))
