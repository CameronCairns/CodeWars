# Given a string s return a string that repeats each character in s once
def double_char(string):
    return ''.join([''.join(list) for list in [[char, char] for char in string]])
