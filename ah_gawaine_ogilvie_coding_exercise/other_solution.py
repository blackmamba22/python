#!/usr/bin/env python

#   http://stackoverflow.com/questions/24054434/word-ranking-partial-completion

def fact(n):
    """factorial of n, n!"""

    f = 1

    while n > 1:
         f *= n
         n -= 1

    return f


def rrank(s):
    """Back-end to rank for 0-based rank of a list permutation"""

    # trivial case
    if len(s) < 2: return 0

    order = s[:]
    order.sort()

    denom = 1

    # account for multiple occurrences of letters
    for i, c in enumerate(order):
        n = 1
        while i + n < len(order) and order[i + n] == c:
            n += 1

        denom *= n

    # starting letters alphabetically before current letter
    pos = order.index(s[0])

    #recurse to list without its head
    return fact(len(s) - 1) * pos / denom + rrank(s[1:])


def rank(s):
    """Determine 1-based rank of string permutation"""

    return rrank(list(s)) + 1


strings = [
    "ABC", "CBA",
    "ABCD", "BADC", "DCBA", "DCAB", "FRED",
    "QUESTION", "BOOKKEEPER", "JACBZPUC",
    "AAAB", "AABA", "ABAA", "BAAA", "ABAB"
]

for s in strings:
    print s, rank(s)
