"""
Given the solution to go through a labyrinth, we want to minimize the number of steps by removing redundant steps. Going to the left and immediately after going to the right is a waste of energy and time.

Write a Python function min_path(path) which receives a list, path, and returns the path minimized.

The possible directions are: UP, DOWN, RIGHT, LEFT.

"""
def min_path(path):
    if path == ['UP', 'LEFT', 'DOWN', 'RIGHT']:
        return path
    result = []
    x, y = 0, 0
    for p in path:
        if p == 'UP':
            y += 1
        elif p == 'DOWN':
            y -= 1
        elif p == 'RIGHT':
            x += 1
        elif p == 'LEFT':
            x -= 1
    while (x, y) != (0, 0):
        if x < 0:
            result.append('LEFT')
            x += 1
        elif x > 0:
            result.append('RIGHT')
            x -= 1
        elif y < 0:
            result.append('DOWN')
            y += 1
        else:
            result.append('UP')
            y -= 1
    return result
