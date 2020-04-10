"""
Write a generator function aliquot(n) that iteratively yields the next term in the Aliquot sequence, starting in n.
Aliquot is a sequence of integers in which each term is the sum of the proper divisors of the previous term. Proper 
divisors are divisors of a number excluding the number itself.
"""


def aliquot(n):
    while (n != 0):
        divisors = [x for x in range(1, n) if n % x == 0]
        yield n
        n = sum(divisors)

print(list(aliquot(33)))
print(list(aliquot(9)))
print(list(aliquot(10)))
print(list(aliquot(44))) 
