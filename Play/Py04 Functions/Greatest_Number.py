"""
Write a Python function greatest(num) that, given a non-negative integer num, computes the greatest number that can be made using all digits of num.
"""
def greatest(num):
    atuple = ()
    result = ''
    for x in str(num):
        atuple += (x,)
    ordered = sorted(atuple, reverse = True)
    for i in ordered:
        result += i
    return int(result)
