"""
Use a list comprehension inside a function square_odds(values) that, given a string values with a comma-separated list of numbers, returns a string with comma-separated squares of each odd number in a list.
""" 
def square_odds(values):
    val = values.split(',')
    ints = [int(x) for x in val]
    odds = [x**2 for x in ints if x%2==1]
    strs = [str(x) for x in odds]
    return ','.join(strs)


print(square_odds('1,2,3,4,5,6,7,8,9'))
print(square_odds('115'))
print(square_odds('1,2,3,5,7,11,13'))
print(square_odds('2,4,8,10,20,100'))
print(square_odds('2,3,8,5,10,27,101'))
print(square_odds('8,9,11'))
print(square_odds('5,6,1,2,301,10,2'))
print(square_odds('13,15,2,3,5,6,8,10,11'))
