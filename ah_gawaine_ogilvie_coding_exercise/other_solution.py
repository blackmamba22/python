#!/usr/bin/env python
#import os
#import psutil
import sys

"""
Author: Gawaine O'Gilvie
Date Create: 10/1/2015
Language: Python 2.7.9
Purpose: Returns the index of a given permutation without generating the list of
         permutations.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def get_word_rank(word):
    """Back-end to rank for 0-based rank of a list permutation"""

    word_length = len(word)

    # trivial case
    if word_length < 2 :
        return 0

    sorted_word = sorted(word)

    duplicate_count = 1

    # portion to consider repitition
    for index, item in enumerate(sorted_word):
        n = 1
        while index + n < len(sorted_word) and sorted_word[index + n] == item:
            n += 1

        duplicate_count *= n

    # starting letters alphabetically before current letter
    pos = sorted_word.index(word[0])

    #recurse to list without its head
    return factorial(word_length - 1) * pos / duplicate_count + get_word_rank(word[1:])


def return_rank(word):
    """Adds one to the get_word_rank(s) function because it is zero-based.
       And converts every word to uppercase as well.
    """
    if len(word) > 20:
        print "Error: Word must be less than or equal to 20 letters. Please try again."
        sys.exit(1)

    return get_word_rank(list(word.upper())) + 1



if __name__ == '__main__':

    ### TESTING OUTPUT
    #test_word_set = ["ab","ba","abab","aaab","BAAA","QUESTION", "BOOKKEEPER", "NONINTUITIVENESS"]

    ### print test set with word score
    #print [(i, return_rank(i)) for i in test_word_set]

    if len(sys.argv) > 1:
        print return_rank(sys.argv[1])
    else:
        print "Error: No string provided. Enter a string."


#process = psutil.Process(os.getpid())
#print "RAM Usage: ", process.get_memory_info()[0] / float(2**20), "MB"
