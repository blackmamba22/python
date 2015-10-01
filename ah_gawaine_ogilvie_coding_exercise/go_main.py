#!/usr/bin/env python
import sys

#   http://stackoverflow.com/questions/24054434/word-ranking-partial-completion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_sorted_word_value(word):
    """
    This function calculates the total word value of the first word
    in a sorted list.
    """
    word_length = len(word)

    if word_length <= 0:
        print "Error: empty string provided."
        sys.exit(0)

    sorted_word = sorted(word)
    unique_letters_list = list(set(sorted_word))
    val_dict = {}

    for letter in unique_letters_list:
        val_dict[letter] = unique_letters_list.index(letter) + 1

    max_number = 0

    for i in range(0, word_length):
        max_number += val_dict[sorted_word[i]] * (i + 1)

    #print val_dict, max_number, sorted_word
    #print sorted_word, val_dict
    return (max_number, val_dict)

def compute_word_order_score(word):
    word_length = len(word)

    if word_length > 20 or word_length <= 0:
        print "User Error: Please use a word of at least 20 letters."
        print "User Error: You submitted a word with %s letters" % (word_length)
        sys.exit(1)

    (max_number, val_dict) = calculate_sorted_word_value(word)

    current_number = 0
    for i in range(0, word_length):
        current_number += val_dict[word[i]] * (i + 1)

    order =  (max_number - current_number) + 1
    print word, ' ', order


if __name__ == '__main__':
    args_length = len(sys.argv)

    if args_length > 1:
        print "\nProgram starting..."
        #print ' Number of arguments: ', args_length, 'arguments'
        #print ' Arguments List: ', str(sys.argv), '\n'
        print compute_word_order_score(sys.argv[1])
    else:
        print "Error: Please enter a word, for example: ./script.py abracadabra"
        sys.exit(1)

    #print calculate_sorted_word_value("QUESTION")
    #compute_word_order_score('QUESTION')
