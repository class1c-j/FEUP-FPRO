"""
Write a Python function sparse_dot_product(dict1, dict2) that computes the inner product of two sparse vectors, dict1 and dict2, represented as dictionaries.
"""

 def sparse_dot_product(dict1, dict2):
    result = 0
    for key in dict1:
        if key in dict2:
            result += dict1[key] * dict2[key]
    return result

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))
print(sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1}))
print(sparse_dot_product({10: 10, 3: 5}, {1: 10, 3: 1}))
print(sparse_dot_product({2: 90, 9: 80, 1: -5, 8: 7}, {2: -4, 9: 1, 1: 6}))
print(sparse_dot_product({}, {}))
print(sparse_dot_product({8: -1, 7: 20, 10: 50}, {8: -10, 3: 1, 10: -1}))
print(sparse_dot_product({5: -4, 3: 10}, {5: 10, 3: -10}))
print(sparse_dot_product({6: 10, 2: 5, 9: 1}, {4: 10, 3: 9, 9: 7}))
