"""
Write a Python program that for an integer n (1-9), given by user input, prints a numerical triangle of height n-1, like the one below:

1
22
333
4444
55555
""" 

n = int(input())

for i in range(1, n):
    print(int(str(i) * i))

"""
public:
'1'
'3'
'4'
'6'
private:
'2'
'5'
'8'
'9'
"""
