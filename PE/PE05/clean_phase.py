 """
Write a Python function clean_phrase(astr) that receives a string of lowercase words separated by
whitespace as astr and returns the words after removing all duplicate words and sorting them in
lexicographical order.
"""


def clean_phrase(astr):
    return ' '.join(sorted(list(set([x for x in astr.split()]))))


print(clean_phrase('dozen pack five dozen liquor five jugs'))
print(clean_phrase('hello world and practice makes perfect and hello world again'))
print(clean_phrase('an eye for an eye makes the whole world blind'))
print(clean_phrase('she sells sea shells by the sea shore'))
