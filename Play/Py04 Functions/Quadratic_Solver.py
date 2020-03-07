"""
Define a function solver(a, b, c) that returns the solution to the quadratic formula of the type: ax²+bx+c=0. Return the result in the form of a list: empty list if no solution exists in ℝ, a list with one or two elements if one or two solutions exist, respectively; if there are two solutions, use ascending order.
"""
def solver(a, b, c):
    result = []
    delta = (b ** 2) - 4 * a * c
    if delta > 0:
        x1 = (-b + (delta)**0.5) / (2*a)
        x2 = (-b - (delta)**0.5) / (2*a)
        result.append(x1)
        result.append(x2)
    elif delta == 0:
        x = (-b + (delta)**0.5) / (2*a)
        result.append(x)
    elif delta < 0:
        pass

    return sorted(result)
