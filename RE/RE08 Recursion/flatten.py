"""
Given a nested list alist (i.e., a list which may contain lists which themselves may 
contain other lists, and so on), write a recursive Python function flatten(alist) 
that returns a single list with each of the non-list elements, in order of occurrence
""" 

result = []

def flatten(alist):
    for x in alist:
        if type(x).__name__ == 'list':
            flatten(x)
        else:
            result.append(x)
    return result


print(flatten([]))
print(flatten(['Hello', [2, [[], False]], [True]]))
print(flatten([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(flatten([1]))
print(flatten([[], [], []]))
print(flatten(['a', 'b', [[0, [1, [2, [3, [4, [5, 6]]]]]], 7, 8]]))
print(flatten(['a', ['b'], [['c'], ['d', 'e', 'f']]]))
print(flatten([['hello', ','], 'how', 'are', [[['you']]], '?']))
