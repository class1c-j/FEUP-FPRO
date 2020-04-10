"""
Write a Python function clean_list(alist, adict) that receives a list of integers as alist and a dictionary where the
keys are strings and the values are lists of integers as adict. The function returns a set with the dictionary's keys
which have in the corresponding value any of the integers of alist.
"""


def clean_list(alist, adict):
    return {k for (k, v) in adict.items() if [alist.count(i) for i in v] != len(v)*[0]}


print(clean_list([1, 2, 3], {'a': [1, 2], 'b': [4, 5]}))
print(clean_list([1, 2, 3, 4, 5], {'John': [1, 6], 'Kelly': [1], 'Emma': [8, 9], 'Jason': [10]}))
print(clean_list([47, 64, 69, 37, 76, 83, 95, 97], {'Emma': [69], 'John': [47], 'Jason': [97], 'Kelly': [76]}))
print(clean_list([19, 50, 46, 70, 30, 48, 57, 19, 11, 14], {'Adolfo': [8, 10], 'Bernardo': [], 'Manuel': [46, 70, 57],
    
