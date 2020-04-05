"""
Write a Python function isomorphic(astring1, astring2) that given two strings of the 
same length, determines if they are isomorphic. Two strings are called isomorphic if 
the characters in one string can be remapped to get the other string.
""" 


def isomorphic(astring1, astring2):
    let_ind = {}
    a = ''
    pairs = []
    pairs_ = []
    for l in astring1:
      let_ind[l] = astring2[astring1.index(l)]
      print(list(let_ind.values()))
    for x in astring1:
      if x in let_ind:
        a += let_ind[x]
    if a == astring2 and len(list(let_ind.values())) == len(set(list(let_ind.values()))) :
      for x in astring1:
        pairs.append((x, let_ind[x]))
      for p in pairs:
        if p not in pairs_:
          pairs_.append(p)
      return "'{0}' and '{1}' are isomorphic because we can map: {2}".format(astring1, astring2, pairs_)
    else:
      return "'{0}' and '{1}' are not isomorphic".format(astring1, astring2)
  
  
  print(isomorphic('ab', 'aa'))
  print(isomorphic('paper', 'title'))
  print(isomorphic('foo', 'bar'))
  print(isomorphic('turtle', 'tletur'))
  print(isomorphic('fpro', 'ezua'))
  print(isomorphic('fpro', 'fppo'))
  print(isomorphic('FEUP', 'FCUP'))
  print(isomorphic('programming', 'zoumobppklm'))
