"""

The path to the treasure is given as a sequence of commands that are steps of length 1: up, left, right or down. Write a function map(pos, steps) that takes a coordinate pos, which is a tuple with values x and y as (x,y), and a sequence of commands in a string steps, with the steps separated by a hyphen, and computes the final position in the map.
"""
def map(pos, steps):
    pos = list(pos)
    if steps == 'up':
        pos[1] += 1
    elif steps == 'down':
        pos[1] -= 1
    elif steps == 'right':
        pos[0] += 1
    elif steps == 'left':
        pos[0] -= 1
    elif len(steps) > 0:
        pos = map(pos, steps[0])
        return tuple(map(pos, steps[1:]))
    return tuple(pos)
