"""
Write a function sort_by_field(filename, field) that, given a CSV (Comma Separated Values) file filename and a string field, sorts the lines of the CSV file by field in ascending order. In case of ties, keep the order of the original file.
""" 


def sort_by_field(filename, field):
    file = open(filename, "r")
    words_list = list(file)
    without_n_words = []
    
    for word in words_list:
        without_n_words.append(word.strip("\n"))
        
    list_of_lists = []
    
    for string in without_n_words:
        list_of_lists.append(string.split(","))
        
    if field == list_of_lists[0][0]:
        sorting_field = 0
    elif field == list_of_lists[0][1]:
        sorting_field = 1
    elif field == list_of_lists[0][2]:
        sorting_field = 2
    
    joined_once = []
    joined_once.append(",".join(list_of_lists[0]))
    
    list_of_lists = sorted(list_of_lists[1:], key = lambda x: x[sorting_field])
    
    
    for l in list_of_lists:
        joined_once.append(",".join(l))
        
                
    joined_twice = '\n'.join(joined_once)
    
    return joined_twice



print(sort_by_field('emails.txt', 'surname'))
print(sort_by_field('emails.txt', 'mail'))
print(sort_by_field('us.csv', 'first_name'))
print(sort_by_field('us.csv', 'last_name'))
print(sort_by_field('emails.txt', 'name'))
print(sort_by_field('uk.csv', 'first_name'))
print(sort_by_field('uk.csv', 'last_name'))
print(sort_by_field('uk.csv', 'company_name'))
