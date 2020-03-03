"""


Write a function rearrange(l) that, given a list of numbers l, rearranges it so that all non-positive numbers appear before the positive ones, but does not alter the numbers’ relative order (i.e., all positive numbers must appear in the same order relative to each other as in the original list; same goes for non-positive numbers).

You should use comprehensions.

"""
def rearrange(l):
    return [x for x in l if x <= 0] + [x for x in l if x > 0]
