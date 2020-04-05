"""
Write a Python function fsm(transitions, input) that receives a list of dictionaries as transitions and a string
as input. The size of the list transitions corresponds to the number of states in the automata.
"""


def fsm(transitions, input):
    state = 0
    while input != '':
        if input[0] in transitions[state]:
            state = transitions[state][input[0]]
        else:
            return -1
        input = input[1:]
    return state


print(fsm([{'a': 1}, {'b': 2}, {'a': 1, 'b': 2}], 'ab'))
print(fsm([{'a': 1}, {'b': 2}, {'a': 1, 'b': 2}], 'ax'))
print(fsm([{'h': 1}, {'e': 2}, {'l': 2, 'o': 3}], 'hi'))
print(fsm([{'h': 1}, {'e': 2}, {'l': 2, 'o': 3}], 'hello'))
print(fsm([{'a': 2, 'y': 1}, {'a': 3, 'y': 0}], 'yyyyyya'))
print(fsm([{'a': 2, 'y': 1}, {'a': 3, 'y': 0}], 'yyyyyyya'))
print(fsm([{'n': 2, 'y': 1}, {'e': 3}, {'o': 4}, {'s': 5}], 'yes'))
print(fsm([{'n': 2, 'y': 1}, {'e': 3}, {'o': 4}, {'s': 5}], 'no')) 
