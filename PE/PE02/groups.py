"""
Write a Python function groups(students) that returns a tuple containing tuples with
the possible combinations of groups of three students. If no group is possible, 
return an empty tuple.
""" 


def groups(students):
    new_tuple = ()
    for i in range(0, len(students) - 2):
        for ii in range(i + 1, len(students) - 1):
            for iii in range(ii + 1, len(students)):
                new_pair = tuple((students[i], students[ii], students[iii]))
                new_tuple += (new_pair,)
    return new_tuple


print(groups(('Ana', 'Bernardo', 'Carla', 'Daniel')))
print(groups(('Bart', 'Homer', 'Marge', 'Lisa', 'Maggie')))
print(groups(('Beatriz', 'Sofia', 'Carlos', 'Fernando', 'Julio')))
print(groups(('Bernardo',)))
print(groups(('Alfredo', 'Marcos', 'Joao', 'Alipio Sa', 'Emanuel', 'Jesus')))
print(groups(('Batatinha', 'Companhia')))
print(groups(('A', 'B', 'C', 'D')))
print(groups(('A', 'B', 'C', 'D', 'E', 'F', 'G')))
