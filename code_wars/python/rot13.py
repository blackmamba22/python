"""
Description:

How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is
frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters.
Not spaces, punctuation, numbers etc. Test examples:
"""

def rot13(message):
    import re
    import string

    alphabets = list(string.ascii_lowercase)
    sentenceLen = len(message)

    rot13_result = ""
    for i in range(sentenceLen):
        match_alpha_only = re.match(r'^[A-z]+$', message[i], re.I)

        if match_alpha_only:
            if message[i].islower():
                rot13_result += alphabets[(alphabets.index(message[i].lower()) + 13) % len(alphabets)]
            else:
                rot13_result += alphabets[(alphabets.index(message[i].lower()) + 13) % len(alphabets)].upper()
            print rot13_result
        else:
            rot13_result += message[i]

    return rot13_result
