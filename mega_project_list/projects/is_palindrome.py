#!/usr/bin/env python3

def check_palindrome(string):
    """Returns true if string is palindrome"""
    import re
    mainstr = re.sub(r'[^a-zA-Z0-9]', r'', string)
    return mainstr[::-1].lower() == mainstr.lower()

if __name__ == '__main__':
    print(check_palindrome("racecar"))
    print(check_palindrome("A Santa at Nasa"))
