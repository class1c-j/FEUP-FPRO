"""
Write a Python function called logic(s, operations) that applies a series of "logic" 
operations between sets.
""" 


def logic(s, opperations):
  for opp in opperations:
    if opp == 'and':
      s = s.intersection(opperations[opp])
    elif opp == 'or':
      s = s.union(opperations[opp])
    elif opp == 'xor':
      s = s ^ opperations[opp]
    elif opp == 'not':
      s = opperations[opp].difference(s)
  return s

print(logic({1, 2, 3, 4}, {'and': {3, 4, 5, 6}}))
print(logic({1, 2, 3, 4}, {'not': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}}))
print(logic({1, 2, 3, 4}, {'xor': {0, 3, 4}, 'not': {0, 1, 2, 3, 4, 5, 6}}))
print(logic({'Carlos', 'Bernardo', 'Eduardo', 'Diana'}, {'and': {'Goncalo', 'Filipe', 'Eduardo', 'Diana'}, 'or': {'Ana', 'Filipe'}}))
print(logic({1, 2, 6, 7}, {'xor': {0, 4, 6, 7, 9}}))
print(logic({1, 2, 6, 7}, {'and': {0, 1, 6, 7}, 'xor': {0, 4, 6, 7, 9}}))
print(logic({0, 8, 4, 5}, {'not': {0, 1, 2, 3, 4, 5, 6, 7, 8}, 'and': {0, 1, 6, 7}, 'xor': {0, 4, 6, 7}}))
print(logic({'Ana', 'Filipe', 'Ivo', 'Eduardo'}, {'not': {'Bernardo', 'Eduardo', 'Henrique', 'Ivo', 'Diana', 'Ana', 'Goncalo', 'Carlos', 'Filipe'}, 'and': {'Ana', 'Bernardo', 'Henrique', 'Goncalo'}, 'xor': {'Ana', 'Henrique', 'Goncalo', 'Eduardo'}}))
