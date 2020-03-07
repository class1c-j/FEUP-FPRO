"""
A number is called a Looping Number if all adjacent digits in it differ by 1. The difference between 9 and 0 is considered as 1. All single digit numbers are considered looping numbers.

Write a Python program that receives an integer n, provided by the user, and checks whether the number is a jumping number or not. If the number is a looping number, print the message Looping number, otherwise print the message Not a looping number.

You can assume that all inputs are non-negative numbers.
"""

n = int(input('Enter number: '))

while True:
    digit_1 = int(n % 10)
    digit_2 = int((n % 100 - digit_1) / 10)
    n = n // 10
    if abs(digit_1 - digit_2) == 1 or abs(digit_1 - digit_2) == 9:
        pass
    else:
        print('Not a looping number')
        break
    print('Looping number')
    break
