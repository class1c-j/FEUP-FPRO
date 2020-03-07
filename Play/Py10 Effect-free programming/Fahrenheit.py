"""
Write a Python function to_fahrenheit(t) that, given a list t of temperatures in Celsius degrees, uses comprehensions to compute the corresponding Fahrenheit degrees, rounded to 2 decimals.
"""
def to_fahrenheit(t):
    return [round((x*9/5) + 32, 2) for x in t]
