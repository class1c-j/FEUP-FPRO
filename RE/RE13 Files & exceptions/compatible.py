"""
Write a Python function compatible(A, B) that receives two matrices A and B, given as nested lists (each list represents a row), and checks if A and B can be multiplied.
""" 

def compatible(A, B):
    if len(A[0]) != len(B): return AssertionError('A and B cannot be multiplied',)
    return 'A and B can be multiplied'

print(compatible([[2, 2], [1, 1]], [[5, 5, 5, 5], [5, 5, 5, 5]]))
print(compatible([[2, 2, 3], [1, 1, 1]], [[5, 5, 5, 5], [5, 5, 5, 5]]))
print(compatible([[1, 2, 2], [1, 2, 2]], [[1, 2, 3, 4], [1, 2, 3, 4]]))
print(compatible([[1]], [[1]]))
print(compatible([[1, 2, 3, 4]], [[1]]))
print(compatible([[1, 2, 3, 4]], [[1], [2], [3], [4]]))
print(compatible([[1, 2, 3, 4]], [[1, 2, 3, 4]]))
print(compatible([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]]))
