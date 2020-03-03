"""
In a circle of people, represented by a list of integers alist, a game will take place. Counting will start at the beginning of the list, and after counting a certain number of people, specified by step, the person where the counting stopped is out of the game.

Write a Python function last_man_standing(alist, step) that returns the last person left on the circle.

Using global variables or cycles is forbidden.
Adapted from: Inspired by the Josephus problem 
"""
def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    elif len(alist) > 0:
        ac = alist.copy()
        a = alist.pop((step - 1) % len(alist))
        alist = alist[ac.index(a):] + alist[:ac.index(a)]
        return last_man_standing(alist, step)

# a quem vir isto, espero que acordes feliz amanhã
