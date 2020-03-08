"""
Use Spyder3 to write a program that asks the user to input a tag string tag and a string text and prints an HTML valid element of the form <tag>text</tag>.

For example: for a user input tag="h1" and a text="I’m an HTML text", the output must be "<h1>I'm an HTML text</h1>".
"""

h = input()
text = input()

h_beginning = "<" + h + ">"
h_end = "</" + h + ">"

print(h_beginning + text + h_end)