"""
Write a Python function longest_word(url) that given the string url returns the longest word in the Web resource that is also in the words file that may be found at /usr/share/dict/words or here.
""" 

import urllib.request
import string



def longest_word(url):
    lines = []
    words = []
    letters = ''
    
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    for i in html:
        if i not in string.punctuation and i not in string.digits:
            letters += i
            
    a = set([x for x in letters.split() if len(x) <= 23])
    print(a)
    
    with open('words')  as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            lines.append(line)
            
    for x in lines:
        if x in a:
            words.append(x)
    
    
    
    return max(words, key=len)



print(longest_word('https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/sheet'))
print(longest_word('https://en.wikipedia.org/w/index.php?title=Monty_Python'))
print(longest_word('https://en.wikipedia.org/w/index.php?title=University_of_Porto'))
print(longest_word('https://www.w3schools.com/python/python_intro.asp'))
print(longest_word('https://en.wikipedia.org/w/index.php?title=Python_(programming_language)'))
print(longest_word('https://docs.python-guide.org/writing/documentation/'))
print(longest_word('https://www.gnu.org/licenses/gpl.txt'))
print(longest_word('https://en.wikipedia.org/w/index.php?title=Tower_of_Hanoi'))
