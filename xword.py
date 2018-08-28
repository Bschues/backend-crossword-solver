#!/usr/bin/env python
"""Crossword Solver Program"""

# Can this be done in a single regex??
# Probably a 6 kyu difficulty level.


def check_word(test_word, dictionary):
    result = []
    nonBlanks = len(test_word) - test_word.count(' ')
    for word in dictionary:
        incLetter = 0
        incMatch = 0
        if len(word) == len(test_word):
            for letter in test_word:
                if letter == word[incLetter]:
                    incMatch += 1
                incLetter += 1
            if incMatch == nonBlanks:
                result.append(word)
    return result


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unkown letters: ').lower()
    print(check_word(test_word, words))


if __name__ == '__main__':
    main()
