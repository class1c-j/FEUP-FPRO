"""
In a circle of people, represented by a list of integers alist, a game will take place. Counting will start at the beginning of the list, and after counting a certain number of people, specified by step, the person where the counting stopped is out of the game.

Write a Python function last_man_standing(alist, step) that returns the last person left on the circle.
Adapted from: Inspired by the Josephus problem 
"""
def last_man_standing(alist, step):
    target = 0
    while len(alist) > 1:
        target = (target + step - 1) % len(alist)  # if you see this recursion sucks
        alist.remove(alist[target])
    return alist[0]
