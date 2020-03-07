"""


Write a Python function called nested_exceptions(tree) that, given a tree of functions in the form of nested tuples tree where each element is a function, returns a tree with the same structure containing True if the function raises an exception or False otherwise.

Hint: You can use the built-in callable() to see if an object is a function or not.

"""
def nested_exceptions(tree):
    result = []
    for i in tree:
        if callable(i):
            try:
                i()
            except:
                result.append(True)
            else:
                result.append(False)
        else:
            result.append(nested_exceptions(i))

    return tuple(result)
