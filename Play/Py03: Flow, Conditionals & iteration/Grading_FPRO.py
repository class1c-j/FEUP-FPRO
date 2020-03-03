"""
Write a Python program that, given the four components of the FPRO grade, by user input, returns the student's grade, an integer from 0 to 20, by using the formula:

grade = (LE + RE + 5 * PE + 3 * TE) / 50

The program returns:

    "Input error", if the any of the components is not between 0 and 100
    "RFC", if the PE < 40 or the TE < 40
    the grade as an integer, otherwise
"""
import math

LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())

grade = (LE + RE + 5 * PE + 3 * TE) / 50

if LE in range(101) and RE in range(101) and PE in range(101) and TE in range(101):
    if PE < 40 or TE < 40:
        print("RFC")
    else:
        print(int(grade + 0.5))  # Fix rounding error
else:
    print("Input error")
