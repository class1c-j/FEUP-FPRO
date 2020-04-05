 """
 Write a Python function called collisions(alist) that receives a list of positive 
 integers alist and returns a dictionary with the frequency of the hash associated 
 to each element in the list. As the hash function, use the modulus-8 of the sum of 
 the digits in the number.
 """
 
 
 def collisions(alist):
    al = [str(x) for x in alist]
    col = {}
    hashes = []
    a = 0
    for x in al:
      for c in x:
        a += int(c)
        print(a)
      hashes.append(a % 8)
      a = 0
    for v in hashes:
      col[v] = col.get(v, 0) + 1
    return col

print(collisions([24, 42]))
print(collisions([1, 789, 100, 9807, 1208, 92, 101]))
print(collisions([101, 40, 5, 7, 13, 1100, 79, 12, 15]))
print(collisions([15, 3, 10, 72, 9, 8, 20, 12]))
print(collisions([]))
print(collisions([1, 289, 9493, 123, 5, 1241, 7, 6, 70, 124, 13, 17, 22]))
print(collisions([21, 43, 56, 72, 131, 211, 311]))
print(collisions([90, 120, 80, 10, 60, 80, 90, 900, 45, 18, 81]))
