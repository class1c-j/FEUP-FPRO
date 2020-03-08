"""
Write a Python function rm_letter_rev(ch, astr) that removes all occurrences of a given character ch (case sensitive)
 from the given string astr (case sensitive) and returns the resulting string with its characters in the reverse order.
Work in Spyder and save the program in the file rm_letter_rev.py.
"""

def rm_letter_rev(l, astr):
    reverse_string = ''
    for i in astr:
        if i != l:
            reverse_string = i + reverse_string
    return reverse_string

print(rm_letter_rev('b', 'bbb'))
print(rm_letter_rev('b', 'aabbbcc'))
print(rm_letter_rev(',', '1,2,3,4'))
print(rm_letter_rev('O', 'nothing'))