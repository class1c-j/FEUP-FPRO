"""
Write a Python program that converts a quaternary number (base 4) quat, given by user input, into the corresponding decimal number (base 10).
""" 

quat = int(input())
quat_aux = quat
decimal = 0
digits = 0

# count digits
while quat_aux > 0:
    if quat_aux == 0:
        digits = 1
    quat_aux //= 10
    digits += 1

for r in range(digits):
    decimal += (quat % 10) * (4 ** r)
    quat //= 10

print(decimal)

"""
public:
'123'
'112233'
'11'
'00121'
private:
'3'
'103'
'331120'
'31021203'
"""
