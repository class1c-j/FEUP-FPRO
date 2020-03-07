"""
Write a Python function repeated_letter(s) which returns the first character to repeat itself.
"""
def repeated_letter(s):
    for i in s:
        if s.count(i) >= 2:
            return i
