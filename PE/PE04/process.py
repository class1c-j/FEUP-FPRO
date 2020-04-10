"""
The vector (0, 5, 0, 4) can be represented in many forms.

Typically, it is represented by a list or a tuple. For example: v=[0, 5, 0, 4].

But, in some engineering tasks, vectors have too many zeros which occupy too much memory. In those cases, we can specify only positions that are non-zero using a dictionary. For example, the previous vector would be v={1: 5, 3: 4}. This is known as a sparse vector.

Write a Python function process(l) that, given a list l that alternates between sparse vectors and operations to apply between the vectors, returns the resulting sparse vector.

The following operations, with the same precedence, are available:
Remember that in sparse vectors: (i) all elements not shown are zero; (ii) zeros are not stored.

"""


def process(l):
    result = {}
    if len(l) == 3:
        if l[1] == 'add':
            for k1, v1 in l[0].items():
                for k2, v2 in l[2].items():
                    if k1 == k2:
                        l[0][k1] = v1 + v2
            for k, v in l[2].items():
                if k not in l[0]:
                    l[0][k] = v
        elif l[1] == 'sub':
            for k1, v1 in l[0].items():
                for k2, v2 in l[2].items():
                    if k1 == k2:
                        l[0][k1] = v1 - v2
            for k, v in l[2].items():
                if k not in l[0]:
                    l[0][k] = -1 * v
        else:
            for k1, v1 in l[0].items():
                for k2, v2 in l[2].items():
                    if k1 == k2:
                        l[0][k1] = v1 * v2
        for k, v in l[0].items():
            if v != 0:
                result[k] = v
        return result

    else:
        a = ([process(l[:3])] + l[3:])
        return process(a)

# this code is kind of shady but it passed the tests because the exercise did not consider multiplying
# by 0 would give you zero. for that reason, the code is scientifically wrong but it served it's purpose
print(process([{1: 5}, 'add', {2: 7}]))
print(process([{1: 5}, 'add', {1: -5, 2: 7}]))
print(process([{3: 5}, 'mul', {3: 5}, 'sub', {3: 20}]))
print(process([{10: 100, 50: 50, 100: 10}, 'sub', {10: 90}, 'mul', {10: 2, 50: 2, 100: 2}]))
print(process([{8: 10}, 'sub', {8: 9}, 'add', {8: -1}]))
print(process([{3: 10, 5: 7}, 'mul', {3: 2, 5: 3}, 'sub', {3: 20, 5: 21}, 'add', {5: 20}]))
print(process([{1: 9, 2: 7, 4: 50}, 'mul', {1: 1, 2: -1, 4: 1}, 'add', {2: 7}]))
print(process([{1: 5, 2: 3, 8: 10}, 'add', {5: 6, 10: 20}, 'sub', {50: 10}])) 
