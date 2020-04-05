"""
Write a function days_until_empty(C, l) that returns at which day the tank will become empty.
""" 

def days_until_empty(C, l, days=0):
    maxC = C
    while C > 0:
        C += l
        if C > maxC:
            C = maxC
        C -= days
        days += 1
    return  days - 1

print(days_until_empty(5, 2))
print(days_until_empty(60, 1))
print(days_until_empty(90, 3))
print(days_until_empty(10, 0))
print(days_until_empty(70, 5))
print(days_until_empty(50, 20))
print(days_until_empty(75, 2))
print(days_until_empty(100, 100))
