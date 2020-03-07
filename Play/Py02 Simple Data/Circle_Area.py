 """
 Write a Python script that given the radius r of a circle by user input, prints the value of its area. Please use round with two decimal places. Consider pi = 3.14159.
 """
pi = 3.14159
r = float(input())
a = round(r ** 2 * pi, 2)
print(a)
