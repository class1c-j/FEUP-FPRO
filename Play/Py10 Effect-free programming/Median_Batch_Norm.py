"""


Write a generator function batch_norm(alist, batch_size) that, given a list of integers alist, yields a normalized batch of elements of alist of a given size batch_size. Each batch must be normalized by the median value of the batch. That is, each batch is subtracted by the median within that batch. A batch is a sublist with size=batch_size.

For example:

    batch_norm([-1, 0, 1, 1, 2, 4], 3) returns a generator that produces [[-1, 0, 1], [-1, 0, 2]]
    batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5) returns a generator that produces [[9, 0, -13, 4, 0], [0.0, 4.0, 0.0, 0.0]]


"""

from statistics import median

def batches(alist, batch_size):
    for i  in range(0, len(alist), batch_size):
        yield alist[i:i+batch_size]

def batch_norm(alist, batch_size):
    for x in batches(alist, batch_size):
        yield [i - median(x) for i in x]

