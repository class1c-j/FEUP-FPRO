"""
Write a Python function order_digits(n) that, given an integer number n greater or
equal to zero, returns a tuple with the digits of the given number in decreasing 
order.
""" 


def order_digits(n):
    atuple = ()
    n = str(n)
    for x in n:
        atuple += (int(x),)
    return tuple(sorted(atuple, reverse = True))


print(order_digits(9013322))
print(order_digits(1234543288))
print(order_digits(10298))
print(order_digits(1))
print(order_digits(27857893902191142))
print(order_digits(98428923712))
print(order_digits(234853000000))
print(order_digits(0))
