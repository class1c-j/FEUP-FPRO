"""
diff ★★★

In Linux, there is a command called diff which displays the difference between two files. Write a function diff(filename1, filename2) that receives two filenames filename1 and filename2 as its parameters and returns the contiguous difference between the files until two lines finally match again.

For example, given the two files:

1. file1d.txt

I need to buy apples.
I need to run the laundry.
I need to wash the dog.
I need to get the car detailed.
And then I go sleep!

2. file2d.txt

I need to buy apples.
I need to do the laundry.
I need to wash the car.
And then I go sleep!

    diff("file1d.txt", "file2d.txt") should return the string

- I need to run the laundry.
- I need to wash the dog.
- I need to get the car detailed.
+ I need to do the laundry.
+ I need to wash the car.

"""
import difflib
def diff(filename1, filename2):
    result = ''
    with open(filename1) as f1:
        f1_text = f1.readlines()
    with open(filename2) as f2:
        f2_text = f2.readlines()
    # Find and print the diff:
    for line in difflib.unified_diff(f1_text, f2_text,                 fromfile='f1', tofile='f2', lineterm=''):
        if line.startswith('-') or line.startswith('+'):
            result += line
    return result.replace('--- f1+++ f2', '').replace('-', '- ').replace('+', '+ ')
