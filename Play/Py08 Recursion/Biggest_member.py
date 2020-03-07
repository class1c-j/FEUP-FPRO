"""
Define a function biggest_member(atuple) that given a tuple atuple, returns the member of the tuple or any sub-tuple which is the biggest (in length). You should not care about ties.
"""
def biggest_member(atuple):
    list_of_tuples = [atuple]
    for x in atuple:
        if type(x) is tuple:
            list_of_tuples.append(x)
            list_of_tuples.append(biggest_member(x))
    return max(list_of_tuples, key= len)
