"""
Write a recursive Python function permutations(atuple) that returns a set of permutations of the tuple atuple. Notice that since the result is a set, then order does not matter.

A suggestion is to use induction. Start by doing a function that works for len(atuple) == 1, then for len(atuple) == 2, then for len(atuple) == 3. It should then become clear how you can do a permutation by breaking it down into smaller subproblems that can be solved with recursion.

You cannot use itertools.

"""
def permutations(atuple):
    if len(atuple) == 0:
        return set()
    elif len(atuple) == 1:
        return set((atuple,))
    else:
        result = set()
        for i in range(len(atuple)):
            fixed = atuple[i]
            rest = atuple[:i] + atuple[i+1:]
            for p in permutations(rest):
                result.add((fixed,) + p)
        return result
