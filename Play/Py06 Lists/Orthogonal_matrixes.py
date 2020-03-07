"""
Write a function is_orthogonal(mx) that given a square matrix (list of lists where each list represents a row), determines if the matrix is orthogonal, returning the appropriate boolean value. A matrix M is orthogonal if MMᵀ = I (i.e. the product of M by its transpose is equal to the identity matrix). The identity matrix is a square matrix in which all the elements of the principal diagonal are ones and all other elements are zeros.

    for the matrix mx=[[-1, 0], [0,1]], the output should be True
    for the matrix [[-2,3], [4,-1]], the output should be False
"""
def transposed(mx):
    rows = []
    for r in range(len(mx)):
        for x in mx:
            rows.append(x[r])

    return [rows[x:x+len(mx)] for x in range(0, len(rows), len(mx))]

def matrix_mult(m1, m2):
    alist = []
    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
            row = []
            for j in range(len(m2[0])):
                sum = 0
                for k in range(len(m2)):
                    sum = sum + (m1[i][k] * m2[k][i])
                    if k == (len(m2)-1):
                        row.append(sum)
            alist.append(row)
    return alist

def identity(i):
    result = i*[i*[0]]
    for a in range(i):
        for b in range(i):
            if a == b:
                result[a][b] = 1
    return result
                

def is_orthogonal(mx):
    return matrix_mult(mx, transposed(mx)) == identity(len(mx))
