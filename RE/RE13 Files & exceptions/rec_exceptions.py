"""
Write a function rec_exceptions(alist) that receives a list alist of functions. When you call each one of these functions, it will either (i) also return a list of functions or (ii) raise an exception. You should transverse the list until you have caught all exceptions and return them in a flat list.
""" 

def rec_exceptions(alist):
    result = []
    
    for f in alist:
        try:
            if type(f()) == list:
                result.extend(rec_exceptions(f()))
        except Exception as error:
            result.append(error)
    return result



print(rec_exceptions([lambda: 1/0]))
print(rec_exceptions([lambda: [lambda: [1, 2, 3].index(-1), lambda: ''[2]], lambda: [1, 2, 3][4], lambda: [lambda: [lambda: 1/0]]]))
print(rec_exceptions([lambda: [lambda: [1, 2, 3, 4].index(10), lambda: eval('** 2'), lambda: eval('5 **')], lambda: [lambda: [1, 2, 3, 4][9], lambda: [1, 2, 3, 4][5], 4+'a']]))
print(rec_exceptions([lambda: [lambda: [lambda: open("whatever"), lambda: [lambda: 2+"3"], lambda: [lambda: 1/0]]]]))
print(rec_exceptions([]))
print(rec_exceptions([lambda: [lambda: [lambda: 1/0]], lambda: [1, 2, 3][4], lambda: [lambda: [1, 2, 3].index(-1), lambda: ''[2], lambda: [lambda: []]]]))
print(rec_exceptions([lambda: [lambda: [1, 2, 3, 4][-10], lambda: [lambda: -4/0, lambda: [lambda: 1/0, lambda: eval(']5, 2[')], lambda: 1/0]]]))
print(rec_exceptions([lambda: [lambda: [lambda: 5/0], lambda: [lambda: 0/0, lambda: 1/0], lambda: [lambda: [lambda: [lambda: [lambda: [lambda: [[1, 2, 3, 4].index(10), lambda: [[1, 2, 3, 4].index(-2)]]]]]]]]]))
