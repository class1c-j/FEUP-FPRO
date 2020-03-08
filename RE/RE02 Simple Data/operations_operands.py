"""
The formula for computing the final amount if one is earning compound interest is given on Wikipedia as:

Use Spyder3 to write a program that replaces these letters with something a bit more human-readable and calculate the final amount () at the end of the second year, for some varying amounts of money (), payment frequency () at realistic interest rates ().

Please round the result for 3 digits.

For example:

    for P = 1000, n = 2, and r = 1% the result is 1020.151
    for P = 650, n = 1 and r = -0.05% the result is 643.516

"""
year = 2
initial_amount = float(input())
pay_freq = float(input())
interest_rate = float(input())


final_amount = initial_amount * (1 + interest_rate/pay_freq)**(2 * pay_freq)

print(round(final_amount, 3))