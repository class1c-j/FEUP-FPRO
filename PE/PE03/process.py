"""
Write a Python function process(commands) that receives a list of commands to be processed
over sets by the given order.
"""


def process(commands):
    if len(commands) == 3:
        if commands[1] == '|':
            return commands[0].union(commands[2])
        elif commands[1] == '&':
            return commands[0].intersection(commands[2])
        if commands[1] == '-':
            return commands[0].difference(commands[2])
        if commands[1] == 'x':
            return {(a, b) for a in commands[0] for b in commands[2]}
    else:
        aux = process(commands[0:3])
        commands[0:2] = []
        commands[0] = aux
        return process(commands)


print(process([{1, 3, 4}, '|', {2, 5}]))
print(process([{1, 3, 4}, '|', {2, 5}, '&', {8, 2, 3}]))
print(process([{1, 3}, 'x', {2, 5}]))
print(process([{1, 3}, 'x', {2, 5}, '&', {(1, 2), (3, 2), (1, 1)}]))
print(process([{1, 3, 4}, '&', {2, 5}]))
print(process([{1, 3, 4}, '|', {2, 5}, '-', {8, 2, 3}]))
print(process([{8, 10, 2}, 'x', {1, 2}, '-', {5, (10, 1), (2, 2), (8, 1), (10, 2)}]))
print(process([{8, 10, 2}, 'x', {1, 2}, 'x', {1}, '-', {1, 2, '1)', 5, '2)', '(2', '(8', '(10'}, '|', {1, 5}])) 
