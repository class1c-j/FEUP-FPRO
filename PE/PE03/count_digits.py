"""
Write a Python function count_digits(n) that computes the frequency of each digit in 
the number n, with n > 0, and returns it in the form of a dictionary.
You cannot use cycles or global variables.
""" 

def count_digits(n, dic={}):
    if len(str(n)) == 1:
        current_n = n % 10
        if current_n not in dic:
            dic[current_n] = 1
        else:
            dic[current_n] += 1
        return dic
    else:
        current_n = n % 10
        if current_n not in dic:
            dic[current_n] = 1
        else:
            dic[current_n] += 1
        return count_digits(n//10, dic)


print(count_digits(28742))
print(count_digits(123123))
print(count_digits(1))
print(count_digits(3243232432))
print(count_digits(3281018213))
print(count_digits(28376243891))
print(count_digits(7))
print(count_digits(2020))
