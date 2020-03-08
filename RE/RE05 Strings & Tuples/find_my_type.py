"""
Write a Python function find_dtype(atuple, data_type) that, given a tuple atuple, returns another tuple containing
just the elements of type data_type.  It should be assumed that data_type is a string with one of the following values:
'int', 'float', 'complex', 'bool', 'str' or 'tuple'.
Hint: Look at __name__ in the Python Standard Library.
Work in Spyder and save the program in the file find_dtype.py.
"""
def find_dtype(atuple, data_type):
    result = ()
    for a in atuple:
        if type(a).__name__ == data_type:
            result = result + (a, )
    return result

print(find_dtype((1, False, 'False', 2.0, 10, '3j'), 'int'))
print(find_dtype((1, False, 2.0, 'True', '25+2j', 9.5), 'bool'))
print(find_dtype(((1,), 2, [3, 4, 5], (6, 7), 8, [9]), 'tuple'))
print(find_dtype((1, 1.0, (1,), '(1,)', '1.0'), 'str'))