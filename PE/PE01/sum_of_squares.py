"""
Write a Python program that, given an integer with one digit d and another integer num, both provided by user input in that order, prints the sum of the squares of the digits of num greater than d.
""" 

d = int(input())
num = int(input())
sum_squares = 0
num_aux = num
digits = 0

# count digits
while num_aux > 0:
    if num_aux == 0:
        digits = 1
    num_aux //= 10
    digits += 1


for r in range(digits):
    if num % 10 > d:
        sum_squares += (num % 10) ** 2
    num //= 10

        
print(sum_squares)

"""
public tests:
'2', '135'
'3', '135'
'5', '135'
'5', '8109'

private tests:
'0', '123'
'4', '1025'
'9', '234781'
'3', '234781'
"""
