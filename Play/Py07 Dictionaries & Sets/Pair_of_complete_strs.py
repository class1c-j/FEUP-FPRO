"""
Pairs of complete strings ★★★

Write a Python function complete_pairs(s1, s2) that, given two sets s1 and s2, of sizes n and m respectively, finds the pairs that are complete strings on concatenating each string from s1 to each string from s2 and returns those concatenated pairs as a set.

Two strings are said to be complete if on concatenation, they contain all the 26 letters of the English alphabet. For example, “abcdefghi” and “jklmnopqrstuvwxyz” are complete as they together have all characters from ‘a’ to ‘z’.
Adapted from: GeeksForGeeks.org 
"""
def complete_pairs(s1, s2):
    pairs = set()
    for y in s1:
        for x in s2:
            a = y + x
            if set(x for x in 'abcdefghijklmnopqrstuvwxyz') == set(x for x in a):
                pairs.add(a)
    return pairs
