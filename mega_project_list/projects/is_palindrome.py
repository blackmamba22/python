#!/usr/bin/env python3

def check_paliindrome(string):
    """Returns true if string is palindrome"""
    import re
    mainstr = re.sub(r'[^a-zA-Z0-9]', r'', string)
    return mainstr[::-1].lower() == mainstr.lower()

if __name__ == '__main__':
    print(check_paliindrome("racecar"))
    print(check_paliindrome("A Santa at Nasa"))
