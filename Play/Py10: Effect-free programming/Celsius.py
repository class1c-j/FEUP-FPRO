"""
Write a Python function to_celsius(t) that, given a list t of temperatures in Fahrenheit degrees, uses comprehensions to compute the corresponding Celsius degrees, rounded to 1 decimal.
"""
def to_celsius(t):
    return [round((x-32)*5/9, 1) for x in t]
