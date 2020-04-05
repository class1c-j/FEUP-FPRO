"""
Write a function reduce_map_filter(args) that receives a collection of arguments called args and 
returns the result of processing args.
""" 

from functools import reduce

def reduce_map_filter(args):
    if type(args[2]) is list:
        if args[0] == 'map':
            return list(map(args[1], args[2]))
        elif args[0] == 'filter':
            return list(filter(args[1], args[2]))
        elif args[0] == 'reduce':
            return reduce(args[1], args[2])
    else:
        args = list(args)
        args[2] = reduce_map_filter(args[2])
        return reduce_map_filter(tuple(args))


print(reduce_map_filter(('map', lambda x: 2*x, [1, 2, 3])))
print(reduce_map_filter(('filter', lambda x: x%2 != 0, [1, 2, 3])))
print(reduce_map_filter(('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1, 2, 3]))))
print(reduce_map_filter(('reduce', lambda a,b: a+b, ('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1, 2, 3])))))
print(reduce_map_filter(('map', lambda x: x**3, ('map', lambda x: -x, [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10]))))
print(reduce_map_filter(('filter', lambda x: x%2 == 0, ('filter', lambda x: x >= 0, [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10]))))
print(reduce_map_filter(('filter', lambda x: x >= 0, ('map', lambda x: -x, [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10]))))
print(reduce_map_filter(('reduce', lambda a,b: a+b, ('filter', lambda x: x >= 0, ('map', lambda x: -x, [-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])))))
