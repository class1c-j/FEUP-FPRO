"""
Write a Python function find_me(f, limits) that, given a function f and a tuple limits with two 
integers representing the search limits, return how many iterations were necessary until the 
desired number was found.
""" 

def find_me(f, limits):
    xs = list(range(limits[0], limits[1]))
    iterations = 0
    lb = 0
    ub = len(xs)
    mid_ind = (lb + ub) // 2
    mid_el = xs[mid_ind] 
    
    while True:
        if iterations > 0:
            mid_ind = (lb + ub) // 2
            mid_el = xs[mid_ind] 
        if f(mid_el) == -1:
            ub = mid_ind 
        elif f(mid_el) == 1:
            lb = mid_ind
        else:
            return iterations
        iterations += 1

print(find_me(lambda n: -1 if n > 31 else 1 if n < 31 else 0, (0, 100)))
print(find_me(lambda n: -1 if n > 563 else 1 if n < 563 else 0, (-5000, 5000)))
print(find_me(lambda n: -1 if n > 891 else 1 if n < 891 else 0, (100, 10000)))
print(find_me(lambda n: 0 if n == 99 else 1, (0, 100)))
print(find_me(lambda n: -1 if n > 3 else 1 if n < 3 else 0, (0, 100)))
print(find_me(lambda n: -1 if n > -563 else 1 if n < -563 else 0, (-5000, 5000)))
print(find_me(lambda n: -1 if n > 121 else 1 if n < 121 else 0, (100, 10000)))
print(find_me(lambda n: 0 if n == 0 else -1, (0, 500)))
