"""
Write a function override(l1, l2) that, given two lists of tuples, performs the operation l1 ++ l2 known as override.
""" 

print(override([('c', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'd')], [('a', 'c'), ('b', 'd')]))
print(override([('a', 'b', 'c', 'e'), ('f', 'p', 'r', 'o')], [('a', 'c'), ('b', 'd')]))
print(override([('a', 'b'), ('c', 'd')], [('b', 'a'), ('d', 'c')]))
print(override([('a', 'a', 'a'), ('a', 'a', 'b')], [('a', 'a', 'c')]))
print(override([('z', 'x', 'y', 'w'), ('z', 'w', 'y', 'w')], [('z', 'x'), ('w', 'a', 'b')]))
print(override([('b', 'x'), ('b', 'a', 'b'), ('w', 'w', 'w')], [('b', 'x'), ('a', 'y'), ('c', 
                                                                                         'w')]))
print(override([('f', 'p', 'r'), ('p', 'r', 'o')], [('f', 'p', 'o')]))
print(override([('i', 'u'), ('u', 'i', 'i')], [('u', 'a', 'c'), ('a', 'b', 'c'), ('u', 'w', 
                                                                                  'v')]))
