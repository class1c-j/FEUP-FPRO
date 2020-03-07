"""
You're helping a teller decide how to give change. Write a Python script that given the price of the sale and the amount received by user input, then prints a string indicating how many notes of each amount they have to give as change. Consider that the largest note available is the 50€ note and that all prices and amounts received are multiples of 5 (no coins!).

The result should be a string with the number of notes of each amount, separated by a space: "#50 #20 #10 #5".

Hint: To help format the result, use type conversions to string.
"""
price = int(input())
received = int(input())
change = received - price
fifty = 0
twenty = 0
ten = 0
five = 0
if (change % 5 == 0) and (change % 10 != 0):
    five = five + 1
    change = change - 5
while change >= 50:
    fifty = fifty + 1
    change = change - 50
if change >= 20:
    twenty = twenty + 1
    change = change - 20
if change >= 10:
    ten = ten + 1
    change = change - 10
formated = f"{fifty} {twenty} {ten} {five}"
print(formated)
