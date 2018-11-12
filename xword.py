#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Bschues"

import re


# YOUR HELPER FUNCTION GOES HERE
def find_matches(test_word, words):
    test_word = test_word.replace(' ', '\\w')
    matches = []
    for word in words:
        if len(word) == len(test_word):
            match = re.search(test_word, word)
            if match:
                matches.append(match.group())
            # print('hit')
    return(matches)


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()
    test_word = str(input(
        'Enter a word to solve.\nUse spaces for unknown letters: ').lower())
    print(find_matches(test_word, words))
    # YOUR ADDITIONAL CODE HERE
    # raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()
