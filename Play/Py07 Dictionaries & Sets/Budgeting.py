"""
Write a Python function budgeting(budget, products, wishlist) that, given an integer budget, products and purchases that a buyer intends to do (wishlist), checks if the budget is not exceeded, making the appropriate adjustments, if needed. The argument products is a dictionary where each key is the product name and the value is the price (per unit); the wishlist is a dictionary where each key is the product name and the value the quantity desired.

Due to lack of attention, the buyer might have wanted more than he could afford. The function should uncover these cases and calculate what products should have their desired quantity lowered (or even be removed) in order to reduce the total amount to fit the budget. Examine products with lower price first. The function should return the updated wishlist.

"""
def budgeting(budget, products, wishlist):
    price = sum([wishlist[a]*products[a] for a in wishlist])
    while price > budget:
        
        wlist = []
        for x in wishlist:
            for a in range(wishlist[x]):
              wlist.append(x)
        sorted_wl = sorted(wlist, key= lambda x: products[x]) 
        wishlist[sorted_wl[0]] -= 1
        if wishlist[sorted_wl[0]] == 0:
            del wishlist[sorted_wl[0]]
        print(wishlist)
        price = sum([wishlist[a]*products[a] for a in wishlist])
    return wishlist
