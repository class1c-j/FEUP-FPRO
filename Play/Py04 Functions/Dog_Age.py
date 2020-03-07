"""
Write a Python function dogs(h_age) that receives the dog's age in human years h_age and returns the corresponding dog's age in dog's years. For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
"""
def dogs(h_age):
    d_age = 0
    if h_age >= 2:
        d_age += 2 * 10.5
        h_age -= 2
    d_age += h_age * 4
    if h_age == 1:
        d_age = 10.5
    
    return d_age
