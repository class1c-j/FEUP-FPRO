"""
Write a Python function knapsack(money, products, wishlist) that receives an integer 
indicating how much money the person has, a products dictionary showing the price of 
each item, and a wishlist dictionary indicating how much quantity we want of each 
product. Your goal is to return the basket of products where you spend as much of 
your money as you can.
"""


def flatten(alist):
    
    final = []
    
    for i in alist:
        if type(i) is list:
            final += flatten(i)
        else:
            final.append(i) 
    return final    

def powerset(lst):
    
    result = [[]]
    
    for x in lst:
        result.extend([subset + [x] for subset in result])
        
    return sorted(result, key=lambda x:len(x))

def best_choice(bdg, dict, ps_wish):
    
    final_dict = {}
    bc = []
    cost = 0

    for i in ps_wish:
        price = 0
        for j in flatten(i):
            price += dict[j]
        if price <= bdg and price >= cost:
            cost = price
            bc = flatten(i)
     
    for i in bc:
        if i in final_dict:
            final_dict[i] += 1
        else:
            final_dict[i] = 1
        
    return final_dict


def knapsack(budget, products, wishlist):
    
    wish_list = sorted([[k] for k,v in wishlist.items() for i in range(0, v)], key=lambda x:len(x))
    
    return best_choice(budget, products, powerset(wish_list))  

print(knapsack(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
print(knapsack(1500, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}))
print(knapsack(1200, {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}, {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}))
print(knapsack(800, {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}, {'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}))
print(knapsack(300, {'printer': 75, 'cellphone': 30, 'shoes': 50, 'powerbank': 25, 'socks': 5}, {'cellphone': 1, 'shoes': 2, 'powerbank': 1, 'socks': 10}))
print(knapsack(4000, {'laptop': 900, 'mechanical keyboard': 120, 'book': 20, 'watch': 125, 'painting': 299}, {'laptop': 3, 'mechanical keyboard': 3, 'book': 1, 'watch': 1, 'painting': 4}))
print(knapsack(750, {'laptop': 900, 'mechanical keyboard': 120, 'book': 20, 'watch': 125, 'painting': 299}, {'laptop': 3, 'mechanical keyboard': 3, 'book': 1, 'watch': 1, 'painting': 4}))
print(knapsack(700, {'sofa': 239, 'chair': 130, 'bed': 101, 'mattress': 200, 'sticker': 2}, {'sofa': 2, 'chair': 1, 'bed': 2, 'sticker': 8}))
