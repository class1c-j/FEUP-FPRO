"""


Write a Python function solve_sudoku(board) that, given an incomplete Sudoku matrix in board, returns the complete version.

For example, if you are given this board:
8	4	1	7	2	6	3	5	9
7	5	3	8	1	9	4	6	2
0	9	2	5	3	4	1	8	7
1	2	8	9	5	7	6	4	3
9	6	5	1	4	3	2	7	8
4	3	7	6	8	2	9	1	5
3	1	4	2	7	8	5	9	6
2	8	9	4	6	5	7	0	1
5	7	6	3	9	1	8	2	4

Then, you must complete all values equal to zero, and return the completed board. In this case, the first should be 6 and the second should be 3.

The rules of Sudoku are:

    Each cell must have a value between 1 and 9
    For each line, all values should be different
    For each column, all values should be different
    For each of the nine 3x3 square, all values should be different.


"""

def solve_sudoku(board):
    for i in range(81):
        row, col = i//9, i%9
        if not board[row][col]:
            curr_c = [x[col] for x in board]
            curr_r = board[row]
            if row < 3 and col < 3:
                curr_s = [board[i][0:3] for i in range(3)]
            elif row < 3 and col < 6:
                curr_s = [board[i][3:6] for i in range(3)]
            elif row < 3 and col < 9:
                curr_s = [board[i][6:9] for i in range(3)]
            elif row < 6 and col < 3:
                curr_s = [board[i][0:3] for i in range(3, 6)]
            elif row < 6 and col < 6:
                curr_s = [board[i][3:6] for i in range(3, 6)]
            elif row < 6 and col < 9:
                curr_s = [board[i][6:9] for i in range(3, 6)]
            elif row < 9 and col < 3:
                curr_s = [board[i][0:3] for i in range(6, 9)]
            elif row < 9 and col < 6:
                curr_s = [board[i][3:6] for i in range(6, 9)]
            elif row < 9 and col < 9:
                curr_s = [board[i][6:9] for i in range(6, 9)]
            # print(curr_c)
            # print(curr_r)
            # print(curr_s)
            for i in range(1, 10):
                if i not in curr_r and i not in curr_c and i not in curr_s:
                    board[row][col] = i

    return board
