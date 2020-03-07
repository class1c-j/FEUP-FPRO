"""


Four in a Line is a popular game where two players (red and yellow) compete against each other trying to form lines with 4 circles of the same color. These lines can be (i) horizontal, (ii) vertical or (iii) diagonal in both directions.

Write a Python function four_in_line(board) that given a matrix called board of varying size, returns a set with the two extrema points: the coordinates where the winner line starts and ends. The board matrix contains either 0 (empty), 1 (red) or 2 (yellow). Return an empty set if there is no winner. At most, one winner exists.

The first test is illustrated in the picture above.

"""
def four_in_line(board):
    win = set()
    
    # check horizontal
    for c in range(len(board[0])-3):
        for r in range(len(board)):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] != 0:
                win.add((r, c))
                win.add((r, c+3))
                      
    # check vertical
    for c in range(len(board[0])):
        for r in range(len(board)-3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] != 0:
                win.add((r, c))
                win.add((r+3, c))
    
    # check pos diag
    for c in range(len(board[0])-3):
        for r in range(len(board)-3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] != 0:
                win.add((r, c))
                win.add((r+3, c+3))
                
    # check neg diag
    for c in range(len(board[0])-3):
        for r in range(3, len(board)):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] != 0:
                win.add((r, c))
                win.add((r-3, c+3))

    
    
    return win
