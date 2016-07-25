#!/usr/bin/env python3

"""Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found."""

def count_vowels(string):
    vowels = "a e i o u".split()
    vowels_dict = {}
    vowels_count = 0
    for v in string:
        if v in vowels:
            vowels_count += 1
            if v in vowels_dict.keys():
                vowels_dict[v] += 1
            else:
                vowels_dict[v] = 1

    for i, j in vowels_dict.items():
        print(i, j)
    print("Total vowels: ", vowels_count)

if __name__ == '__main__':
    count_vowels("banana")
