"""
Write a Python function called reorder(ltuples) that receives a list ltuples of
tuples. Each tuple is of the form (c, i) where c is a character and i is the position
where it should be placed in the string.
""" 


def reorder(ltuples):
    result = ''
    sorted_tuples = sorted(ltuples, key = lambda x: x[1])
    for x in sorted_tuples:
        result += x[0]
    return result


print(reorder([('g', 3), ('d', 1), ('o', 2)]))
print(reorder([('t', 4), ('i', 2), ('k', 1), ('t', 3), ('e', 5), ('n', 6)]))
print(reorder([('c', 4), ('o', 5), ('r', 2), ('a', 3), ('d', 1)]))
print(reorder([('r', 3), ('h', 1), ('o', 2), ('e', 5), ('s', 4)]))
print(reorder([('f', 1), ('r', 3), ('o', 4), ('p', 2)]))
print(reorder([('x', 5), ('u', 4), ('l', 1), ('n', 3), ('i', 2)]))
print(reorder([('t', 3), ('o', 5), ('h', 4), ('n', 6), ('y', 2), ('p', 1)]))
print(reorder([('g', 3), ('a', 7), ('r', 8), ('e', 4), ('y', 9), ('n', 5), ('d', 6), ('e', 2), ('l', 1)]))
