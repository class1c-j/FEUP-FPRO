"""
The path to the treasure is given as a sequence of commands that are steps of length 1: up, left, right or down. Write a function map(pos, steps) that takes a coordinate pos, which is a tuple with values x and y as (x,y), and a sequence of commands in a string steps, with the steps separated by a hyphen, and computes the final position in the map.
"""
def map(pos, steps):
    x, y = pos
    steps_list = steps.split('-')
    for i in steps_list:
        if i == 'up':
            y += 1
        elif i == 'down':
            y -= 1
        elif i == 'right':
            x += 1
        elif i == 'left':
            x -= 1
    return (x, y)
