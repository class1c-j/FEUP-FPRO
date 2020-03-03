"""
Rewrite the following flow diagram as a Python script.

Note that := is assignment.
"""
l = int(input())
s = int(input())
r = l

if r > s:
    pass
else:
    l = r
    r = s
    s = l
while not(s > r):
    r = r - s
while not(r == 0):
    l = r
    r = s
    s = l
    while not(s > r):
        r = r - s
print(s)
