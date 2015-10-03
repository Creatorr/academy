"""
  Remove Characters

    Write a program which removes specific characters from a string.

    Input sample:
        The first argument is a path to a file. The file contains the source strings and the characters that need to be
        scrubbed. Each source string and characters you need to scrub are delimited by comma.

    Output sample:
        Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on each line
        you print.
"""

import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open(r"C:\work\Academy\academy\test_for_scripts\test_2015_10_CODEEVAL_Remove characters.txt", 'r')

for test in test_cases:
    pos_sep = test.find(', ')
    sentence = test[:pos_sep]
    letters = test.replace("\n", "", 1)[pos_sep + 2:]
    out_sentense = ""
    for letter in sentence:
        if letters.find(letter) == -1:
            out_sentense += letter
    print out_sentense
test_cases.close()
