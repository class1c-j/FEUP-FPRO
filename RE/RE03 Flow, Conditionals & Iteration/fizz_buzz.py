"""
Write a Python program that “plays” a version of the known game FizzBuzz over a sequence of natural numbers, up to an integer n provided by the user.

The program should build and finally print a string result with each number in the sequence separated by a space. However:

    If the number is a multiple of 3, appends the word "Fizz" instead
    If the number is a multiple of 5, appends the word "Buzz" instead
    If the number is both a multiple of 3 and 5, nothing is done

For example: for n=7, the final string should be 1 2 Fizz 4 Buzz Fizz 7
"""

n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz", end=' ')
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz", end=' ')
    elif i % 5 == 0 and i % 3 == 0:
        pass
    else:
        print(i, end=' ')