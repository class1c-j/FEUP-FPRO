"""
Write a Python function mult(M, N) that computes the matrix multiplication between matrices M and N, in that order.
When the dimensions disagree, return an empty list.
You cannot use numpy.
"""


def mult(M, N):
    alist = []
    if len(M[0]) == len(N):
        for i in range(len(M)):
            row = []
            for j in range(len(N[0])):
                sum = 0
                for k in range(len(N)):
                    sum += M[i][k] * N[k][j]
                    if k == (len(N) - 1):
                        row.append(sum)
            alist.append(row)

    return alist

print(mult([[0, 1, 2], [2, 1, 0], [4, 1, 3], [1, 6, -2]], [[2, 1], [7, 8], [2, -10]]))
print(mult([[2, 1], [7, 8], [2, -10]], [[2, 1, 8, 10, -2], [7, 8, -2, -6, 10]]))
print(mult([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[2, 1, 5], [7, 8, 10], [2, -10, -2], [-8, 10, 1], [-4, 6, 7]]))
print(mult([[-7, 8, -10], [1, -4, 7]], [[2, -1], [7, -8], [-2, 10]]))