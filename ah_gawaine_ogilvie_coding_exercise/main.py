#!/usr/bin/env python
import sys
from itertools import permutations

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#word = '01234567'
#sorted_word = sorted(word)
#unique_letters_list = list(set(sorted_word))

#perms = [''.join(p) for p in permutations(unique_letters_list)]

#perms = sorted(perms)
#print perms.index("47056132")
#print "Length: ", len(perms)
#print sorted("QUESTION")

def perm(seq):
    perms = [''.join(p) for p in permutations(seq)]
    perms = set(perms)
    for i in sorted(perms):
        print i
    return len(perms) #len(seq)**3


print perm("ABCD")
