"""
Write a Python function count_chars(astring) that returns a tuple containing the number of characters that are alphabetic, digits and special symbols, in the respective order.
"""

def count_chars(astring):
    letters = 0
    numbers = 0
    symbols = 0
    for i in str(astring):
        if i.isalpha() == True:
            letters += 1
        elif i.isdigit() == True:
            numbers += 1
        else:
            symbols += 1
    return (letters, numbers, symbols)
