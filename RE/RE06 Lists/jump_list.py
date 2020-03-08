"""
Write a Python function jump(l) that, given a list of integers l:
    Start with an index = 0
    Set the index value (jump) to the value defined at that position
    Go back to 2 until index = -1
    Return the number of jumps.
"""
def jump(l):
    i = 0
    count = 0
    while i != -1:
        i = l[i]
        count += 1
    return count - 1

print(jump([5, -1, 3, 4, -1, 2]))
print(jump([6, 8, 4, 7, -1, 1, 2, -1, 3]))
print(jump([5, 8, 4, 7, -1, 1, 2, -1, 3]))
print(jump([7, 4, 1, -1, 3, 6, 9, 2, 8, 7]))