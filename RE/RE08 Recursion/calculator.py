 """
Write a function calculator(expr) that given an expression expr computes its value.
"""


def calculator(expr):
    if expr[1] == '+' and type(expr[0]) == type(expr[2]) == int:
        return expr[0] + expr[2]
    elif expr[1] == '-' and type(expr[0]) == type(expr[2]) == int:
        return expr[0] - expr[2]
    elif expr[1] == '*' and type(expr[0]) == type(expr[2]) == int:
        return expr[0] * expr[2]
    else:
        expr = list(expr)
        for i in range(len(expr)):
            if type(expr[i]) is tuple:
                expr[i] = calculator(expr[i])
        return calculator(expr)


print(calculator((1, '+', 2)))
print(calculator(((1, '+', 2), '*', 3)))
print(calculator((10, '-', 10)))
print(calculator((6, '-', (3, '*', 2))))
print(calculator((6, '-', ((3, '+', 1), '*', (9, '-', 2)))))
print(calculator(((9, '*', 2), '-', ((3, '+', 1), '*', (9, '-', 2)))))
print(calculator((6, '-', (2, '*', 3))))
print(calculator(((9, '-', 2), '*', (2, '*', 3))))
