 
"""
Write a Python function move_ball(board) that, given the board as board, returns a list with the positions where the ball has traveled through.
"""

def move_ball(board):
    alist = [(x,y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y] in ['N','S','E','W']]
    pos = alist[0]
    final = [(x,y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y] == 'X'][0]
    a = board[pos[0]][pos[1]]
    if a == 'N':
        pos = (pos[0]-1,pos[1])
    elif a == 'S':
        pos = (pos[0]+1,pos[1])
    elif a == 'E':
        pos = (pos[0],pos[1]+1)
    elif a == 'W':
        pos = (pos[0],pos[1]-1)
    alist.append(pos)
    while pos != final:
        b = board[pos[0]][pos[1]]
        if b == '/':
            if a == 'N':
                a = 'E'
                pos = (pos[0],pos[1] + 1)
            elif a =='S':
                a = 'W'
                pos = (pos[0],pos[1]-1)
            elif a == 'E':
                a = 'N'
                pos = (pos[0]-1,pos[1])
            elif a == 'W':
                a = 'S'
                pos = (pos[0]+1,pos[1])
        elif b == '\\':
            if a == 'N':
                a = 'W'
                pos = (pos[0],pos[1] - 1)
            elif a =='S':
                a = 'E'
                pos = (pos[0],pos[1]+1)
            elif a == 'E':
                a = 'S'
                pos = (pos[0]+1,pos[1])
            elif a == 'W':
                a = 'N'
                pos = (pos[0]-1,pos[1])
        else:
            if a == 'N':
                pos = (pos[0]-1,pos[1])
            elif a == 'S':
                pos = (pos[0]+1,pos[1])
            elif a == 'E':
                pos = (pos[0],pos[1]+1)
            elif a == 'W':
                pos = (pos[0],pos[1]-1)
        alist.append(pos)
    return alist

print(move_ball(['E \\', '/ /', '   ', '\\ X']))
print(move_ball(['SX', '\\/']))
print(move_ball(['XS\\', '// ', '\\ /']))
print(move_ball(['/\\/\\X', ' \\/\\W', '\\   /']))
print(move_ball(['X \\ ', '  \\\\', '   N']))
print(move_ball(['S ', '\\\\', '//', '\\\\', '//', '\\\\', '//', 'X ']))
print(move_ball(['/ X', ' E\\', '\\ /']))
print(move_ball(['X\\  ', ' \\\\ ', '  \\W']))
