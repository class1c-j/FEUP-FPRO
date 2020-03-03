"""


Write a recursive Python function permuta(alist, step=0) that returns the list of permutations. The step controls the order by which the permutations are created.

At each step, each element whose index ≥ step permutates (changes the order) with the element whose index = step.

For example, permuta(['A', 'B', 'C']),

                           f(ABC)
                   /         |        \
step=0       f(ABC)       f(BAC)       f(CBA)
             /    \       /    \       /    \
step=1   f(ABC) f(ACB) f(BAC) f(BCA) f(CBA) f(CAB)


"""
def permuta(alist, step=0):
    result = []
    if step == len(alist) -1:
        result.append(alist)
        return result
    for i in range(step, len(alist)):
        acopy = alist.copy()
        acopy[i],acopy[step] = alist[step],alist[i]
        result += permuta(acopy, step+1)
    return result
    

print(permuta(['A', 'B', 'C']))
