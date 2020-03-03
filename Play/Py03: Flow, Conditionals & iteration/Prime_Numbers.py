"""
Write a Python program that outputs all the prime numbers within a closed interval of numbers between lower and upper, given by user input.

For example:

    for lower=2 and upper=23 the output is: Prime numbers between 2 and 23 are: 2 3 5 7 11 13 17 19 23
    for lower=5 and upper=27 the output is: Prime numbers between 5 and 27 are: 5 7 11 13 17 19 23
    for lower=-2 and upper=5 the output is: Prime numbers between -2 and 5 are: 2 3 5
"""
lower = int(input("Lower: "))
upper = int(input("Upper: "))

print("Prime numbers between", lower, "and", upper, "are:", end = " ")

for n in range(lower, upper + 1):
   if n > 1:
       for d in range(2, n):
           if (n % d) == 0:
               break
       else:
           print(n, end = " ")
