"""
Write a function tic_tac_toe(board, player) that, given a matrix representing the game in the string board, returns
 where the next move should be played so that the player in the string player wins.
"""


def tic_tac_toe(board, player):
    result = ''
    letters = {0: 'A', 1:'B', 2:'C'}
    lines = board.split('\n')
    cols_aux = [lines[j][i] for i in range(len(lines[0])) for j in range(3)]
    cols = [''.join(cols_aux[n:n+3]) for n in range(0, len(cols_aux), 3)]
    diags = [''.join([lines[i][i] for i in range(3)])] + [''.join([lines[2-i][i]
                                for i in range(3)])]
    for x in lines:
        if x.count(player) == 2 and ' ' in x:
            result = str(letters[lines.index(x)]) + str(x.index(' ')+1)
    for x in cols:
        if x.count(player) == 2 and ' ' in x:
            result = str(letters[x.index(' ')]) + str(cols.index(x)+1)
    for x in diags:
        if x.count(player) == 2 and ' ' in x:
            result = str(letters[2-x.index(' ')]) + str(x.index(' ') + 1)
    return result


print(tic_tac_toe(' xx\n o \noxo', 'x'))
print(tic_tac_toe('xo \n xo\no  ', 'x'))
print(tic_tac_toe('x x\n o \nxoo', 'o'))
print(tic_tac_toe('xx \n ox\n oo', 'o'))
print(tic_tac_toe('xx \n o \noxo', 'o'))
print(tic_tac_toe(' xo\nxo \n  x', 'o'))
print(tic_tac_toe('o o\n x \nxxo', 'x'))
print(tic_tac_toe('  o\n xx\no  ', 'x')) 
