#!/usr/bin/env python
import sys

from math import factorial


def lexicographical_index2(p):
    p = int(p)


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


if __name__ == '__main__':
    #print lexicographic_index("47056132")
    #print lexicographic_index("QUESTION")
    print lexicographic_index("AB")
