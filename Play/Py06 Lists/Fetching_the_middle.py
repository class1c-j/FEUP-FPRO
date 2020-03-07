"""
Write a Python function fetch_middle(llists) that, given a list of lists llists, returns a new list containing the middle element from each list in llists. If the list's length is even, consider the middle element to be the average between its two central elements (i.e. for the list [1, 2, 3, 4], the middle element would be (2+3)/2 = 2.5).
Adapted from: CodingBat 
"""
def fetch_middle(llists):
    result = []
    for l in llists:
        if len(l) % 2 == 0:
            a = (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
            result.append(a)
        else:
            result.append(l[len(l) // 2])
    return result
