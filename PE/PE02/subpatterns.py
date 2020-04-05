"""
Write a Python function subpatterns(astring) that receives a string astring and computes the number of
 its substrings that follow a certain pattern.
"""


def subpatterns(astring):
    count = 0
    for i in substrings(astring):
        if pattern_matched(i):
            count += 1
    return "The string '{0}' contains {1} substring patterns.".format(astring, count)


def pattern_matched(substring):
    grows = 0
    shrinks = 0
    for i in range(1, len(substring)):
        if substring[i - 1] > substring[i]:
            shrinks += 1
        elif substring[i - 1] < substring[i]:
            grows += 1
    return grows == shrinks and len(substring) > 1


def substrings(astring):
    return [astring[i:j] for i in range(len(astring)) for j in range(i + 1, len(astring) + 1)]


print(subpatterns('ceda'))
print(subpatterns('aghljcb'))
print(subpatterns('abcdefedcba'))
print(subpatterns('ejmnpzyxwxst'))
print(subpatterns(''))
print(subpatterns('fhwzrscbfeoasw'))
print(subpatterns('anxbwiownsgqxchnqw'))
print(subpatterns('ujwdhwiqopndbvwfqyh')) 
