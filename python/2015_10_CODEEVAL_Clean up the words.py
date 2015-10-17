"""
  Clean up the words

    You have a list of words. Letters of these words are mixed with extra symbols, so it is hard to define the beginning
    and end of each word. Write a program that will clean up the words from extra numbers and symbols.

    Input sample:
        The first argument is a path to a file. Each line includes a test case with a list of words: letters are both
        lowercase and uppercase, and are mixed with extra symbols.
    Output sample:
        Print the cleaned up words separated by spaces in lowercase letters.
"""

import sys
import re

try:
    test_cases = open(sys.argv[1], 'r')
except IndexError:
    test_cases = open(r"C:\work\Academy\academy\test_for_scripts\test_2015_10_CODEEVAL_Clean up the words.txt", 'r')

search_mask = re.compile('[a-zA-Z]')
for test in test_cases:
    word = ""
    for letter in test:
        if search_mask.match(letter) is not None:
            word += letter.lower()
        else:
            word += " "
    words = word.split()
    print " ".join(words)
test_cases.close()
