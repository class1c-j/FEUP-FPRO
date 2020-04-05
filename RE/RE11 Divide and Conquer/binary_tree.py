"""
Write a function binary_tree(key, tree) that, given a string as key and the first node as tree, 
returns the corresponding value. The key always exists in the tree.
""" 

def binary_tree(key, tree):
    # each node is represented by a tuple of the form (key, value, left, right)
    while True:
        if tree[0] == key:
            return tree[1]
        elif tree[0] < key:
            tree = tree[3]()
        elif tree[0] > key:
            tree = tree[2]()


print(binary_tree('hummer', ('aptitudes', 495, lambda: 1/0, lambda: ('roadblock', 25, lambda: ('paramedic', 211, lambda: ('bizets', 115, lambda: 1/0, lambda: ('modernizes', 848, lambda: ('lees', 937, lambda: ('gusty', 472, lambda: 1/0, lambda: ('haggles', 648, lambda: 1/0, lambda: ('jaclyns', 170, lambda: ('implication', 297, lambda: ('hummer', 561, lambda: 1/0, lambda: 1/0), lambda: 1/0), lambda: 1/0))), lambda: 1/0), lambda: 1/0)), lambda: 1/0), lambda: 1/0))))
print(binary_tree('unseals', ('scholars', 885, lambda: 1/0, lambda: ('tailcoats', 709, lambda: 1/0, lambda: ('tibets', 689, lambda: 1/0, lambda: ('tyrones', 704, lambda: 1/0, lambda: ('uncluttered', 533, lambda: 1/0, lambda: ('underrating', 264, lambda: 1/0, lambda: ('vehicles', 898, lambda: ('unseals', 414, lambda: 1/0, lambda: 1/0), lambda: 1/0)))))))))
print(binary_tree('washing', ('interrelationship', 214, lambda: 1/0, lambda: ('slithers', 810, lambda: 1/0, lambda: ('vastly', 876, lambda: 1/0, lambda: ('verizon', 150, lambda: 1/0, lambda: ('whigs', 350, lambda: ('vitim', 328, lambda: 1/0, lambda: ('waiter', 928, lambda: 1/0, lambda: ('washing', 744, lambda: 1/0, lambda: 1/0))), lambda: 1/0)))))))
print(binary_tree('stalemate', ('hibernate', 887, lambda: 1/0, lambda: ('lanolin', 442, lambda: 1/0, lambda: ('nozzles', 51, lambda: 1/0, lambda: ('woolgatherings', 490, lambda: ('tamer', 809, lambda: ('ouijas', 347, lambda: 1/0, lambda: ('tacitnesss', 998, lambda: ('paunches', 912, lambda: 1/0, lambda: ('submissive', 138, lambda: ('profited', 517, lambda: 1/0, lambda: ('seeking', 921, lambda: 1/0, lambda: ('sieved', 16, lambda: 1/0, lambda: ('sows', 96, lambda: 1/0, lambda: ('stools', 687, lambda: ('spaceship', 232, lambda: 1/0, lambda: ('stalemate', 367, lambda: 1/0, lambda: 1/0)), lambda: 1/0))))), lambda: 1/0)), lambda: 1/0)), lambda: 1/0), lambda: 1/0))))))
print(binary_tree('smatterings', ('compartmentalizes', 745, lambda: 1/0, lambda: ('undergrounds', 903, lambda: ('desideratums', 87, lambda: 1/0, lambda: ('sweats', 541, lambda: ('displacements', 613, lambda: 1/0, lambda: ('smatterings', 488, lambda: 1/0, lambda: 1/0)), lambda: 1/0)), lambda: 1/0))))
print(binary_tree('melanies', ('preparations', 295, lambda: ('irelands', 769, lambda: 1/0, lambda: ('pillars', 449, lambda: ('pigtails', 846, lambda: ('opels', 380, lambda: ('misdemeanors', 580, lambda: ('math', 458, lambda: 1/0, lambda: ('mirthless', 524, lambda: ('melanies', 212, lambda: 1/0, lambda: 1/0), lambda: 1/0)), lambda: 1/0), lambda: 1/0), lambda: 1/0), lambda: 1/0)), lambda: 1/0)))
print(binary_tree('hibiscuss', ('unimportant', 892, lambda: ('hisses', 994, lambda: ('ferguson', 726, lambda: 1/0, lambda: ('grenadiers', 15, lambda: 1/0, lambda: ('guarantees', 513, lambda: 1/0, lambda: ('hinder', 97, lambda: ('hibiscuss', 469, lambda: 1/0, lambda: 1/0), lambda: 1/0)))), lambda: 1/0), lambda: 1/0)))
print(binary_tree('syllabifications', ('credulitys', 868, lambda: 1/0, lambda: ('recedes', 971, lambda: 1/0, lambda: ('tippecanoe', 105, lambda: ('reeducated', 237, lambda: 1/0, lambda: ('regulators', 235, lambda: 1/0, lambda: ('thickenings', 263, lambda: ('tchaikovskys', 586, lambda: ('spouted', 819, lambda: 1/0, lambda: ('stengels', 273, lambda: 1/0, lambda: ('syndromes', 277, lambda: ('syllabifications', 635, lambda: 1/0, lambda: 1/0), lambda: 1/0))), lambda: 1/0), lambda: 1/0))), lambda: 1/0)))))
