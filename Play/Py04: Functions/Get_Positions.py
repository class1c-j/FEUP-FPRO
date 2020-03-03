"""
Write a function get_positions that receives two arguments: sentence (a string) and word_list (a list with 3 strings).

The first argument contains 2 words that appear in the second argument concatenated with a single space in between.

The function returns a string with the position in the list of the first word and the position of the second word in the list, separated by a single space. When any of the words of the sentence are not in the list, the function returns the empty string. Positions start counting at zero.
"""
def get_positions(sentence, word_list):

    if sentence.split()[0] not in word_list or sentence.split()[1] not in word_list:
        return ''
    elif sentence.split()[0] == sentence.split()[1]:
        result = ''
        for i in range(len(word_list)):
            if word_list[i] == sentence.split()[0]:
                result += str(i) + ' '
        return result
        
    elif word_list.count(sentence.split()[0]) > 1 or word_list.count(sentence.split()[1]) > 1:
        result = ''
        for i in sentence.split():
            for j in range(len(word_list)):
                if i == word_list[j]:
                    result += str(j) + ' '
        return result
    else:
        return ' '.join([str(word_list.index(i)) for i in sentence.split()])
    


