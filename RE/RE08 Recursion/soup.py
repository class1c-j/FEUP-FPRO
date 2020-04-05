 """
Write a function soup(matrix, word) that, given a matrix of letters, returns the first location
of the word in the matrix.
"""


def soup(matrix, word):
    lines = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G"}
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            if find(matrix, line, column, word):
                return lines[line] + str(column + 1)


def find(matrix, i, j, word):
    if i >= 0 and j >= 0:
        if matrix[i][j] == word[0]:
            if len(word) == 1:
                return True
            else:
                for (a, b) in [(i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1), (i, j + 1), (i, j - 1),
                               (i - 1, j), (i + 1, j)]:
                    if a >= 0 and b >= 0 and a < len(matrix) and b < len(matrix[0]):
                        if matrix[a][b] == word[1]:
                            return find(matrix, a, b, word[1:])


print(soup((('X', 'A', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'),
            ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z')), 'PORTO'))
print(soup((('X', 'A', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'),
             ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z')), 'HOTEL'))
print(soup((('R', 'T', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'),
             ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z')), 'RIO'))
print(soup((('R', 'T', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'),
             ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z')), 'TIRNO'))
print(soup((('J', 'D', 'C', 'P', 'C', 'P', 'X', 'O', 'A', 'A'), ('Z', 'X', 'V', 'O', 'V', 'X', 'F', 'R', 'V', 'V'),
             ('N', 'D', 'L', 'E', 'I', 'R', 'B', 'I', 'E', 'A'), ('Y', 'T', 'R', 'Q', 'O', 'M', 'O', 'I', 'I', 'O'),
             ('F', 'Z', 'Z', 'A', 'P', 'Z', 'E', 'R', 'T', 'Q'), ('X', 'A', 'U', 'E', 'O', 'E', 'O', 'O', 'T', 'O'),
             ('P', 'O', 'R', 'T', 'U', 'O', 'A', 'Z', 'L', 'Z'), ('C', 'Z', 'N', 'O', 'Q', 'U', 'P', 'U', 'O', 'P')),
            'PORTO'))
print(soup((('J', 'D', 'C', 'P', 'C', 'P', 'X', 'O', 'A', 'A'), ('Z', 'X', 'V', 'O', 'V', 'X', 'F', 'R', 'V', 'V'),
             ('N', 'D', 'L', 'E', 'I', 'R', 'B', 'I', 'E', 'A'), ('Y', 'T', 'R', 'Q', 'O', 'M', 'O', 'I', 'I', 'O'),
             ('F', 'Z', 'Z', 'A', 'P', 'Z', 'E', 'R', 'T', 'Q'), ('X', 'A', 'U', 'E', 'O', 'E', 'O', 'O', 'T', 'O'),
             ('P', 'O', 'R', 'T', 'U', 'O', 'A', 'Z', 'L', 'Z'), ('C', 'Z', 'N', 'O', 'Q', 'U', 'P', 'U', 'O', 'P')),
            'AVEIRO'))
print(soup((('J', 'D', 'C', 'P', 'C', 'P', 'X', 'O', 'A', 'A'), ('Z', 'X', 'V', 'O', 'V', 'X', 'F', 'R', 'V', 'V'),
             ('N', 'D', 'L', 'E', 'I', 'R', 'B', 'I', 'E', 'A'), ('Y', 'T', 'R', 'Q', 'O', 'M', 'O', 'I', 'I', 'O'),
             ('F', 'Z', 'Z', 'A', 'P', 'Z', 'E', 'R', 'T', 'Q'), ('X', 'A', 'U', 'E', 'O', 'E', 'O', 'O', 'T', 'O'),
             ('P', 'O', 'R', 'T', 'U', 'O', 'A', 'Z', 'L', 'Z'), ('C', 'Z', 'N', 'O', 'Q', 'U', 'P', 'U', 'O', 'P')),
            'COIMBRA'))
print(soup((('J', 'D', 'C', 'P', 'C', 'P', 'X', 'O', 'A', 'A'), ('Z', 'X', 'V', 'O', 'V', 'X', 'F', 'R', 'V', 'V'),
                 ('N', 'D', 'L', 'E', 'I', 'R', 'B', 'I', 'E', 'A'), ('Y', 'T', 'R', 'Q', 'O', 'M', 'O', 'I', 'I', 'O'),
                 ('F', 'Z', 'Z', 'A', 'P', 'Z', 'E', 'R', 'T', 'Q'), ('X', 'A', 'U', 'E', 'O', 'E', 'O', 'O', 'T', 'O'),
                 ('P', 'O', 'R', 'T', 'U', 'O', 'A', 'Z', 'L', 'Z'), ('C', 'Z', 'N', 'O', 'Q', 'U', 'P', 'U', 'O', 'P')),
                'FARO'))
