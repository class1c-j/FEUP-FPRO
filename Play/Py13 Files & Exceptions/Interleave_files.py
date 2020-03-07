"""


Write a Python function interleave(f1, f2) to combine each line from first file (f1) with the corresponding line in second file (f2), while there's lines in both files.

For example:

    Considering that exists in the current directory a file shakespeare.txt with the content of shakespeare.txt and another file with the content of monty.txt, then interleave("monty.txt", "shakespeare.txt") returns a string with the same content of mixed.txt.


"""
def interleave(f1, f2):
    lines1 = []
    lines2 = []
    with open(f1, "r") as f1:
        for the_line in f1:
           lines1.append(the_line)
    with open(f2, "r") as f2:
        for the_line in f2:
           lines2.append(the_line)
    small = min([lines1, lines2], key=len)
    
    result = ''
    for i in range(len(small)):
        result += lines1[i]
        result += lines2[i]
    
    return result
