"""
Consider the following set of commands:
    insert i e: Insert integer e at position i.
    print: Save list to result string.
    remove e: Delete the first occurrence of integer e.
    append e: Insert integer e at the end of the list.
    sort: Sort the list in ascending order.
    pop: Remove the last element from the list.
    reverse: Reverse the list.
Write a Python function manipulator(l, cmds) that, given a list of commands from the previous list as a list of strings,
applies them sequentially to a list l and returns a string which contains the result of all print commands (separated by
a single space). You can assume all command arguments are valid (e.g. insertion index is valid and remove specifies an
element that exists in the list at that time).
"""

def manipulator(l, cmds):
    result = ''
    for i in cmds:
        cmds = i.split(' ')
        l = [int(x) for x in l]
        print(cmds)
        if 'insert' in i:
            ind = int(cmds[-2])
            char = int(cmds[-1])
            l.insert(ind, char)
        elif i == 'print':
            result += str(l) + ' '
        elif 'remove' in i:
            l.remove(int(cmds[-1]))
        elif 'append' in i:
            l.append(cmds[-1])
        elif i == 'sort':
            l.sort()
        elif i == 'pop':
            l.pop()
        elif i == 'reverse':
            l.reverse()
    return result

print(manipulator([], ['insert 0 10', 'append 10', 'insert 0 6', 'print', 'pop', 'remove 10', 'print', 'reverse',
                       'print']))
print(manipulator([-2, 5, 10, 20], ['remove 20', 'insert 3 5', 'insert 3 7', 'insert 3 -2', 'print', 'sort', 'print',
                                    'reverse', 'print']))
print(manipulator([1, 2, 3], ['print']))
print(manipulator([], ['append 5', 'append -2', 'append 3', 'sort', 'print']))