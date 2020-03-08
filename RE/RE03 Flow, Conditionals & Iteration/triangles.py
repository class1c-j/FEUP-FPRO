"""
Write a Python program that checks if a triangle is equilateral, isosceles or scalene, with the 3 sides provided by the user, each one in a different input() statement.

The output result to be printed is computed accordingly ("Equilateral", "Isosceles", "Scalene"), and must be equal to "Not a triangle", when the sides given do not form a valid triangle.
"""

a = float(input())
b = float(input())
c = float(input())

if a + b <= c or a + c <= b or b + c <= a:
    print('Not a triangle')
elif a == b and b == c:
    print('Equilateral')
elif (a == b and a != c) or (b == c and a != b) or (a == c and b != a):
    print('Isosceles')
else:
    print('Scalene')