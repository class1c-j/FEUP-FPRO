"""
Write a Python function iterate_rev(names, numbers, emails) that given three tuples of equal size names (strings),
phone numbers (integers) and emails (strings), returns a string with "name - number - email" in each line,
in reverse order.
""" 

def iterate_rev(names, numbers, emails):
    a = []
    s = ''
    for i in range(len(names)):
        a.append('{0} - {1} - {2}\n'.format(names[i], numbers[i], emails[i]))
    b = a[::-1]
    for x in b:
        s += x
    return s

print(iterate_rev(('ana', 'bernando', 'carlos'), (938421028, 916381961, 939090082), ('ana.serra@gmail.com', 'b1999@hotmail.com', 'up201945321@fe.up.pt')))
print(iterate_rev(('silvia ferreira', 'bernardo silva', 'filipe ramos', 'helder campos'), (924873278, 935423231, 9108932240, 97242372387), ('silvia.ferreira@gmail.com', 'silva@google.com', 'filipe.ramos@fe.up.pt', 'hcampos@fc.up.pt')))
print(iterate_rev(('carlos ferreira', 'bianca silva', 'fernando ramos', 'olivia campos'), (97242372387, 924873278, 9108932240, 935423231), ('carlos.ferreira@gmail.com', 'silva@google.com', 'fernando.ramos@fe.up.pt', 'ocampos@fc.up.pt')))
print(iterate_rev((), (), ()))
print(iterate_rev(('eduardo',), (931001928,), ('edu98@hotmail.com',)))
print(iterate_rev(('diana', 'eduardo'), (9822741920, 931001928), ('diana@fe.up.pt', 'edu98@hotmail.com')))
print(iterate_rev(('bernando', 'carlos', 'diana', 'eduardo'), (916381961, 939090082, 9822741920, 931001928), ('b1999@hotmail.com', 'up201945321@fe.up.pt', 'diana@fe.up.pt', 'edu98@hotmail.com')))
print(iterate_rev(('ana', 'bernando', 'carlos', 'diana', 'eduardo'), (938421028, 916381961, 939090082, 9822741920, 931001928), ('ana.serra@gmail.com', 'b1999@hotmail.com', 'up201945321@fe.up.pt', 'diana@fe.up.pt', 'edu98@hotmail.com')))
