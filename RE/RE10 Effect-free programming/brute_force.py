"""
Write a function brute_force(f, l) that receives two arguments:

    f(login): a function that represents the login. This function receives a string login and 
    returns a boolean.
    l: a list of possible characters.

The function calculates the combinations of 3 characters and return a list of those combinations 
that break into the function.
""" 

import itertools
def brute_force(f, l):
    a = list(itertools.product(l, repeat=3))
    a = list(map(lambda x: ''.join(list(x)), a))
    return list(filter(f, a))


print(brute_force(lambda x: x in ('abc', 'bac', 'cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))
print(brute_force(lambda x: x[0] == 'c' and x not in ('cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))
print(brute_force(lambda x: abs(int(x)) == 1 if x.isdigit() else False, ['-', '0', '1', '2']))
print(brute_force(lambda x: int(x) ** 2 < 5, ['0', '1', '2', '3', '4']))
print(brute_force(lambda x: int(x) % 50 == 0, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
print(brute_force(lambda x: int(x) % 100 == 0, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
print(brute_force(lambda x: x[0] == 'x', ['v', 'w', 'x', 'y', 'z']))
print(brute_force(lambda x: x[:2] == 'xw', ['v', 'w', 'x', 'y', 'z']))
