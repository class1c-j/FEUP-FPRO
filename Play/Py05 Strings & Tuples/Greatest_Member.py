"""
Define a function greatest_member(atuple) that given a tuple atuple, returns the member of the tuple who has the highest score; for tiebreakers return the member that appears first in the tuple.

The score is calculated by summing the ASCII code of each character for every string the member contains.

A member can be either a string or another tuple. In the second case, the total score of the member is the sum of all scores of each sub-member.

If the initial tuple has no members, return an empty tuple.

"""

def values(x):
    if type(x) is str:
        return sum([ord(i) for i in x])
    elif type(x) is tuple:
        return sum(values(i) for i in x)

def greatest_member(atuple):
    return max(atuple, key = lambda x: values(x)) 
