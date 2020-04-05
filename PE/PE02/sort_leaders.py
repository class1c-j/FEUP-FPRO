"""
Write a Python function sort_leaders(records) to sort the leaderboard records 
according to the following criteria:

    Sort based on the maximum score (descending order);
    Then sort based on minimum number of tries (ascending order);
    Then sort based on student name (ascending order);

""" 


def max_score(records):
    return max(records[1])

def number_tries(records):
    return len(records[1])

def name(records):
    return records[0]

def sort_leaders(records):
    a = sorted(records, key = name)
    b = sorted(a, key = number_tries)
    c = sorted(b, key = max_score, reverse = True)
    return tuple(c)



print(sort_leaders((('João', (80, 90, 100)), ('Ana', (90, 100)), ('José', (100,)), ('Ana', (50, 90)), ('Rui', (50, 90)))))
print(sort_leaders((('José', (100,)), ('Ana', (90, 100)), ('João', (80, 90, 100)), ('Ana', (50, 90)), ('Rui', (50, 90)))))
print(sort_leaders((('Bruno', (60, 20, 10)), ('Carlos', (20, 10, 60)), ('João', (10, 50, 30)), ('Ana', (90, 60)), ('José', (75,)))))
print(sort_leaders((('Bruno', (90, 80, 50)), ('Carlos', (50, 70, 60)), ('José', (100,)), ('Ana', (10, 0)), ('João', (5,)))))
print(sort_leaders((('Guilherme', (99, 100)), ('Beatriz', (100, 99, 10)), ('Afonso', (99, 10, 100)))))
print(sort_leaders((('Ana', (70, 40, 55)), ('Carlos', (70, 60)), ('Sofia', (55,)), ('Patricia', (35, 60, 30)), ('Sonia', (40, 70, 65)), ('Diogo', (15, 90, 70)))))
print(sort_leaders((('A', (80, 10, 50)), ('B', (90, 30, 55)), ('E', (100, 50, 30)), ('D', (90, 100, 20)), ('H', (90, 50, 70)), ('B', (75,)), ('K', (60, 0, 100)), ('L', (80, 100)))))
print(sort_leaders((('Americo', (0, 50, 55)), ('Americano', (80, 90)), ('Amelia', (50, 80, 82)), ('Augusta', (81,)), ('Ambrosio', (83,)), ('Alfredo', (15, 88, 67)))))
