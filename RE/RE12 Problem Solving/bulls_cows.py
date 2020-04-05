 """
 Write a Python function bulls_cows(seed) that, given an integer seed, calls random.seed(seed) to initialise the random generator. Then, the function creates a random number of 4-digits (correct) and a closure function to be returned. That closure function, when called with a number guess, calculates the score of the "bulls and cows" game of the correct versus guess numbers, and returns it as a tuple of the form (cows, bulls).
 """
 
 import random

def bulls_cows(seed):
    random.seed(seed)
    random_num = str(random.randint(1000, 9999))
    random_num = list(random_num)
    def closure_func(guess):
        cows = 0
        bulls = 0
        guess = list(str(guess))
        b_str = guess.copy()
        b_guess = random_num.copy()
        for i in range(len(guess)):
            if guess[i] == random_num[i]:
                cows += 1
                b_str.remove(guess[i])
                b_guess.remove(guess[i])
        for i in range(len(b_str)):
            if b_str[i] in b_guess:
                bulls += 1
                b_guess.remove(b_str[i])
        return (cows,bulls,)
    return closure_func
 
 print(bulls_cows(12345))
 print(bulls_cows(510))
 print(bulls_cows(62678))
 print(bulls_cows(60712))
 print(bulls_cows(68489))
 print(bull_cows(4255))
 print(bulls_cows(89432))
 print(bulls_cows(156))
