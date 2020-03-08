"""
Consider student records, given as a nested tuple of N tuples in the format (name, number, (grade_1, grade_2, …)).
Write a Python function sort_grades(records) to sort the student records according to the following criteria:
    Sort based on the average grade (descending order);
    Then sort based on student name (ascending order);
    Then sort based on student number (ascending order);
where name and number are strings, and each grade is an integer between 0 and 100.
Hint: For sorting, you should use the built-in function sorted(), in which you can define your own key-sorting function.
Work in Spyder and save the program in the file grades.py.
"""

def average(records):
    return sum(records[2]) / len(records[2])

def name_and_up(records):
    return (records[0], records[1])


def sort_grades(records):
    sort_1 = sorted(records, key = name_and_up)
    sort_2 = sorted(sort_1, key = average, reverse = True)
    return tuple(sort_2)

print(sort_grades((('Pedro', 'up2015254', (45, 55, 52)), ('Diogo', 'up20182017', (50, 51, 52)),
                   ('Almeida', 'up20186063', (70, 90, 80)), ('Josefina', 'up20182016', (0, 100, 100)),
                   ('Clementina', 'up2018034', (100, 100, 100)))))
print(sort_grades((('Rafael', 'up2015254', (45, 55, 52, 48)), ('Luis', 'up2018201', (50, 51, 52, 53)),
                   ('Tomás', 'up2018606', (70, 90, 70, 50)), ('Tomás', 'up2018201', (35, 100, 45, 100)),
                   ('Edgar', 'up2018045', (100, 100, 0, 0)))))
print(sort_grades((('Aluno A', 'up2011111', (50,)), ('Aluno B', 'up2012112', (60,)), ('Aluno C', 'up2011112', (59,)),
                   ('Aluno A', 'up2012111', (60,)), ('Aluno D', 'up2013000', (61,)))))
print(sort_grades((('Tate', 'up2011111', (50, 60, 40, 30, 80, 100)), ('Jarred', 'up2012112', (60, 45, 29, 31, 42, 81)),
                   ('Ayan', 'up2011112', (59, 61, 71, 52, 37, 0)), ('James', 'up2012111', (60, 60, 60, 70, 55)),
                   ('Tatiana', 'up2013000', (61, 62, 63, 64, 65, 66)), ('Jasper', 'up2013010', (50, 100, 100, 90, 0, 15)),
                   ('Jarrod', 'up2011110', (10, 30, 50, 70, 90, 100)))))