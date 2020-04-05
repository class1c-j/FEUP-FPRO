 """
Given a list of strings, write a Python function anagrams(alist) that groups anagrams together
and returns them in a nested list. An anagram is a word or phrase formed by rearranging the
letters of another word or phrase by using all the original letters exactly once.
"""


def anagrams(alist):
    result = []
    nwspace = [i.replace(' ', '').lower() for i in alist]
    sorted_letters = [''.join(sorted([j for j in i])) for i in nwspace]
    for i in range(len(alist)):
        if sorted_letters.count(sorted_letters[i]) == 1:
            result.append([alist[i]])
        else:
            aux = []
            for j in range(len(alist)):
                if sorted_letters[i] == sorted_letters[j]:
                    aux.append(alist[j])
            result.append(sorted(aux))

    no_repeats = []
    [no_repeats.append(x) for x in result if x not in no_repeats]

    return sorted(no_repeats, key=lambda x: x[0].lower())


print(anagrams(['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']))
print(anagrams(['sentence', 'lives', 'ten scene', 'bat', 'Elvis', 'CE sennet']))
print(anagrams([]))
print(anagrams(['William Shakespeare', 'I am a weakish speller', 'Madam Curie', 'Radium came']))
print(anagrams(['funeral', 'restful', 'fluster', 'apple', 'real fun']))
print(anagrams(['ferrari', 'Elon Musk', 'Muskmelon', 'rrarife', 'tenerife']))
print(anagrams(['Edward Gorey', 'Ogdred Weary', 'Regera Dowdy', 'E G Deadworry']))
print(anagrams(['Vladimir Nabokov', 'Vivian Darkbloom', 'Vivian Bloodmark', 'Blavdak Vinomori', 'Dorian Vivalkomb']))
