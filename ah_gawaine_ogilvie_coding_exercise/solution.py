#!/usr/bin/env python
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def lexicographic_index(p):
    """
    Return the lexicographic index of the permutation `p` among all
    permutations of its elements. `p` must be a sequence and all elements
    of `p` must be distinct.

    >>> lexicographic_index('dacb')
    19
    >>> from itertools import permutations
    >>> all(lexicographic_index(p) == i
    ...     for i, p in enumerate(permutations('abcde')))
    True
    """
    result = 0
    for j in range(len(p)):
        k = sum(1 for i in p[j + 1:] if i < p[j])
        result += k * factorial(len(p) - j - 1)
    return result + 1


def alpha_seq_rank(word):
    # sort word sequence in alphabetical order
    rank_list = sorted(word)
    word_score = 1                  # initiate lowest rank

    print "Rank List: ", rank_list
    for i in word:
        rank = rank_list.index(i)
        word_score += factorial(rank) * rank
        rank_list.remove(rank_list[rank])
        #print rank, word_score

    return word_score


if __name__ == '__main__':
    #print lexicographic_index("QUESTION")
    print alpha_seq_rank("QUESTION")
