"""
Write a function mastermind(g1, g2, g3, c1, c2, c3) to evaluate a single line of a mastermind game.
The function receives 6 single character strings. Each string can be "b" for blue, "w" for white and "y" for yellow.
The first 3 arguments are the user guess. The last 3 arguments are the correct key. Argument 1 is the user guess for
the value at argument 4 and so on.
You should give 3 points for each user guess that is completely correct, that is, the same color at the same position
in the key and 1 point if the user guessed the color right but at the wrong position (that is, the color exists in the
key but at another wrong position).
Note that one right guess (position or color) counts only once.
For example:
    mastermind("b", "w", "y", "w", "y", "w") returns the integer 2
    mastermind("b", "w", "y", "b", "w", "y") returns the integer 9
    mastermind("b", "b", "y", "b", "w", "b") returns the integer 4
"""

def mastermind(g1, g2, g3, c1, c2, c3):
    guess = [g1, g2, g3]
    key = [c1, c2, c3]
    points = 0
    for i in range(len(guess)):
        if guess[i] == key[i]:
            points += 3
            key[i] = 0
    if g1 != c1 and g1 in key:
        points += 1
    if g2 != c2 and g2 in key:
        points += 1
    if g3 != c3 and g3 in key:
        points += 1
    return points

print(mastermind('w', 'w', 'b', 'w', 'w', 'b'))
print(mastermind('y', 'y', 'y', 'y', 'w', 'y'))
print(mastermind('y', 'w', 'b', 'b', 'y', 'y'))
print(mastermind('b', 'w', 'w', 'b', 'b', 'b'))