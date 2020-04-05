"""
Write a Python function file_finder(dirs, file_name) that returns the full path of a 
file file_name (given as a string), or None if it is not in the directory tree dirs.
""" 

def file_finder(dirs, file_name):
    # base case
    if dirs == file_name:
        return file_name
    else:
        for i in dirs[1:]:
            if file_finder(i, file_name) != None:
                return dirs[0] + "/" + file_finder(i, file_name)


print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'Documents'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'page.html'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'hello_world.py'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], '22'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'tuples.py'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'recursion.pdf'))
print(file_finder(['user', ['Torrents', ['Movies', 'incredibles.mp4', 'mile22.mp4'], ['Books', 'how-to-think-like-a-computer-scientist.pdf']], ['Trabalhos', ['FPRO', 'RE09.py', 'RE10.py'], ['Alga', 'ex1.docx', 'ex2.docx']], 'a.out'], 'mile22.mp4'))
print(file_finder(['user', ['Torrents', ['Movies', 'incredibles.mp4', 'mile22.mp4'], ['Books', 'how-to-think-like-a-computer-scientist.pdf']], ['Trabalhos', ['FPRO', 'RE09.py', 'RE10.py'], ['Alga', 'ex1.docx', 'ex2.docx']], 'a.out'], 'RE10.py'))
