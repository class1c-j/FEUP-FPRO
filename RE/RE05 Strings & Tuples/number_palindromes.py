"""
Write a Python function palindrome(astring) that receives a string and computes the number of palindromic substrings.
A palindrome is a string that reads the same forwards and backwards. Do not count the palindromic substrings with just
one character and use the function format() to have result as required.
Work in Spyder and save the program in the file palindrome.py.
"""

def rev(astr):
    reverse_string = ''
    for i in astr:
            reverse_string = i + reverse_string
    return reverse_string

def palindrome(astring):
    count = 0
    substrings = []
    for i in range(len(astring)):
        for j in range(i + 1, len(astring) + 1):
            if len(astring[i:j]) > 1:
                substrings.append(astring[i:j])
    for sub in substrings:
        if sub == rev(sub):
            count += 1
    return "The string '{0}' contains {1} palindrome substrings.".format(astring, count)

print(palindrome('gym'))
print(palindrome('mym'))
print(palindrome('mmymm'))
print(palindrome('abcee'))