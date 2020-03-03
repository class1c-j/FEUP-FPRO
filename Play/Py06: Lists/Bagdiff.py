"""
Write a Python function bagdiff(xs, ys) that returns items from the first list (xs) that are not eliminated by a matching element in the second list (ys). An item in the second list may "knock out" just one matching item in the first list.
"""
def bagdiff(xs, ys):
    for y in ys:
        if y in xs:
            xs.remove(y)
    return xs
