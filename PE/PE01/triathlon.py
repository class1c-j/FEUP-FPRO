"""
Write a Python program that, given three times of completion tS, tC and tR (in hours; one for each stage) by user input, in this order, checks if the participant met all the requirements. If so, it should print the total time. Otherwise, it should print the first factor that caused the disqualification (“Time”, “Swimming”, “Cycling” or “Running”, in this order).
""" 

tS = float(input())
tC = float(input())
tR = float(input())

tT = tS + tC + tR

vS = 1.5 / tS
vC = 40 / tC
vR = 10 / tR

if tT >= 4:
    print('Time')
elif vS < 2:
    print('Swimming')
elif vC < 20:
    print('Cycling')
elif vR < 8:
    print('Running')
else:
    print(tT)


"""
public:
'0.4', '1.2', '0.4'
'1', '1', '4'
'0.5', '1', '2.2'
'0.2', '1.8', '0.5'
public:
'0.4', '1.3', '0.8'
'1', '2', '0.9'
'0.6', '3', '0.1'
'0.5', '2', '1.4'
"""
