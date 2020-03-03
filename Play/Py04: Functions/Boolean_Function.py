"""
Write a boolean function in Python called validate that validates a grade by outputting whether the grade is correct or incorrect. A grade is a number between 0 and 100.

You cannot use if.
"""
def validate(n):
    type_n = type(n) == int or type(n) == float
    result = type_n and 0 <= float(n) <= 100
    return result 
