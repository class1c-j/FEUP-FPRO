"""
Write a Python function longest(s) that, given a string s, returns the length of its longest word.
"""
def longest(s):
    s_list = s.split()
    return len(max(s_list, key = len))
