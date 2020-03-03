"""
Write a Python function to_celsius(t) that, given a list t of temperatures in Fahrenheit degrees, uses map() with a lambda function to compute the corresponding Celsius degrees, rounded to 1 decimal.
"""
def to_celsius(t):
    return list(map(lambda x: round((x-32)*5/9, 1), t))
