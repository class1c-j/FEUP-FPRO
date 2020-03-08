"""
Write a Python program that uses the Babylonian method for printing square roots.
For a number num given by user input, to find its square root, do the following:
    Make an initial guess: any positive number
    Improve the guess: apply the formula ; the number is a better approximation to sqrt(num)
    Iterate until convergence: apply the formula until the process converges; convergence is achieved when the digits of and agree on 2 decimal places.
Please use round with three two decimal places.
The use of the math module is forbidden.
For example:
    for num=20 the output is 4.47
    for num=25 the output is 5.0
"""
num = int(input("Insert number: "))
guess = num / 2
last_guess = 0

while abs(last_guess - guess) > 0.01:
    last_guess = guess
    guess = (guess + (num / guess)) / 2

print(round(guess, 2))
